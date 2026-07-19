# TOC — Table des matières commentée du Volume IV (compendium intégral)

| Champ | Valeur |
| --- | --- |
| Version | **0.4 — passe de cohérence interne et de discipline épistémique** (19 juill. 2026). Quatre garde-fous R-N du Vol. II laissés **nus** dans des chapitres consommant le Vol. III (ch. 16, ch. 34, ch. 41 et ch. 54) sont nommés — la parade du risque 10, déclarée complète en v0.3, ne l'était pas sur ce front ; un contrôle exécutable la couvre désormais (`check-toc.py`, contrôle 11, validé par mutation). L'énoncé « refonte pure — aucun contenu neuf » de la v0.3 est **qualifié** : son propre journal consigne quatre enrichissements intra-chapitres, dont un front déclaré neuf à sources primaires à établir (ch. 18) — la somme est une refonte *à ces enrichissements déclarés près*. Titre du ch. 37 aligné sur sa propre réserve (« RTR visé », non « imminent »). Révisions d'A2A ajoutées aux événements de péremption (ch. 54) ; ordre d'instruction suggéré des trois fronts écartés consigné au périmètre ; deux défauts de forme corrigés (ch. 43, Annexe E). Détail au journal v0.4 en fin de fichier |
| Historique | **v0.3** (19 juill. 2026) — rebalancement structurel et audit de couverture : trois audits indépendants ont collationné chaque ligne « Fusion » contre les sources (Vol. I : 91 sections relevées sur les sept chapitres ; Vol. II : 29 pièces, socle de 46 entrées, R-1…R-8 ; Vol. III : plan v0.4) ; structure rééquilibrée à 54 chapitres en 12 livres, plus de livre à chapitre unique ; contrôles exécutables ajoutés (`check-toc.py`). **v0.2** (18 juill. 2026) — révision des renvois : §3.5 réacheminé, Annexe B du Vol. II rattachée, double affectation du §5.12 tranchée, sections orphelines réaffectées, convention du renvoi nommé posée (décision 7), corpus d'appui du Vol. III intégré avec ses réserves, Annexe I ajoutée. **v0.1** — cadrage initial : première fusion des trois volumes en une somme à numérotation continue, décisions de déduplication posées, deux divergences héritées tranchées, méthode et gel unifiés |
| Date | 19 juillet 2026 |
| Statut | Proposition de compilation — se substitue à la lecture des trois volumes une fois rédigée ; jusque-là, les trois volumes sources font foi |
| Nature | **Compendium intégral** : omnibus qui absorbe Vol. I, II et III en un seul ouvrage réordonné, dédoublonné, à lecture autonome. Ce n'est ni un panneau du triptyque ni un méta-index — c'est la *somme* qui les remplace |
| Filiation | Quatrième opus, terminal. Absorbe : **Vol. I — Interopérabilité agentique** (cadre mondial et théorique, méthode ArchiMate/ADS Boréalis, gel juin 2026) ; **Vol. II — L'autonomie encadrée** (cas canadien réglementé, socle F-01…F-48 + F-23b, niveaux [A]/[B]/[C], gel 16-17 juillet 2026) ; **Vol. III — L'entreprise agentique** (identité, délégation, maillage, AgentOps, PQC — proposition v0.4, non encore rédigée). Le README racine (état du 18 juill. 2026) décrit un *triptyque* et ne mentionne pas encore le compendium : la somme clôt la série ; le README sera réécrit pour l'annoncer (risque 8) |
| Décisions structurantes de la fusion | (1) **Numérotation continue** des chapitres (1→54) et des figures/tableaux/faits — un compendium n'a qu'une seule table. (2) **Déduplication** : tout sujet traité par ≥2 volumes est fusionné en un chapitre unique, la provenance et l'arbitrage de fusion étant tracés sous chaque entrée (ligne « Fusion »). (3) **Divergences tranchées** (voir Annexe C). (4) **Méthode unifiée** (voir Annexe A). (5) **Gel unique** à fixer au lancement de la rédaction, avec re-datation de tout fait périssable hérité des trois gels distincts. (6) **Couverture totale tracée** : chaque section des trois sources est affectée à un chapitre d'arrivée ou coupée explicitement (mention « coupe assumée ») — aucune perte silencieuse ; les **annexes et l'avant-propos** des volumes sources sont soumis à la même règle que leurs chapitres. (7) **Renvoi nommé, série nommée, identifiant nommé** : tout renvoi vers un document source nomme ce document — *Monographie*, *Synthèse* ou *PRD* — car le Vol. I vit en numérotation **triple** et non double (Monographie §1-§7 ; *Synthèse* **§1-§12**, et non §3-§12 comme l'écrivaient les v0.1-v0.2 ; Annexe B §0-§17) et les §8.x/§10.x du Vol. II existent à la fois dans sa Monographie et dans son PRD. **Tout renvoi vers une série d'identifiants internes nomme aussi sa série** : le Vol. II porte deux séries « Q n » indépendantes (*Monographie* ch. 16 §16.3, cinq questions AP2/RTR ; ch. 21 §21.2, six questions d'agenda). **Et tout garde-fou nomme son volume** : le Vol. II numérote **R-1…R-8**, le Vol. III **R-01…R-14** — deux séries distinctes portant sur des objets différents, dont les libellés courts se confondent à l'œil. Un « R-7 » nu est indécidable dans un chapitre qui consomme les deux volumes. |
| Contrôles | `python check-toc.py` — numérotation continue, contiguïté des livres, renvois internes pendants, décomptes annoncés, arithmétique du budget, mention du corpus d'appui, traçabilité de chaque chapitre, garde-fous R-N nus dans les chapitres consommant le Vol. III. À exécuter avant toute publication de ce fichier |

---

## Titre

# La somme agentique

## Interopérabilité, autonomie encadrée et fabrique de confiance : déployer des agents en services financiers réglementés (2024-2032)

*Justification du titre : les trois volumes portaient chacun une thèse partielle — « autonomie graduée sous contrôle de finalité » (I), « autonomie encadrée / framed autonomy » (II), « la confiance se fabrique » (III). Le compendium ne les juxtapose pas : il montre qu'elles sont trois coupes d'un même objet. « La somme agentique » revendique le genre — une* summa*, non une anthologie — et le sous-titre énumère les trois plans (interopérabilité, encadrement, confiance) et borne le domaine (services financiers réglementés) et l'horloge (2024-2032, des premiers protocoles ouverts aux jalons PQC).*

## Thèse d'ensemble

Déployer des agents non humains qui engagent la responsabilité d'une institution financière réglementée est **un seul problème d'ingénierie continu**, non trois — et c'est la démonstration de cette continuité qui justifie de refondre trois volumes en une somme. Le problème se lit sur trois plans qui ne sont pas des sujets séparés mais des coupes du même objet : **faire coopérer** les agents (l'interopérabilité — protocoles, sémantique, maillage), **les encadrer** sous un contrôle de finalité que la réglementation impose (l'autonomie encadrée — orchestration déterministe, frames normatifs), et **fonder la confiance** que cette coopération encadrée présuppose sans jamais la produire elle-même (la fabrique — identité non humaine, délégation vérifiable, exploitation dans la durée).

Les trois volumes sources le prouvaient chacun à demi : le Vol. I posait la théorie mais s'arrêtait au seuil du droit applicable ; le Vol. II instruisait le droit canadien mais présupposait la théorie du Vol. I sans la reconstruire ; le Vol. III isolait le verrou commun — l'identité — mais le traitait comme un ouvrage à part. Le compendium tient les trois ensemble : l'invariant du Vol. I (découplage, contrat, évolution) devient le fil qui traverse l'orchestration encadrée (II) et la crypto-agilité (III) ; le « pont » du Vol. II (des contraintes réglementaires aux frames déterministes) devient l'articulation centrale entre les plans I et III ; le « passeport d'agent » du Vol. III redevient ce qu'il est — une pièce d'une architecture de référence unique, formalisée en ArchiMate (méthode-signature du Vol. I) et instanciée sur un cas financier canadien (continuité Boréalis → portefeuille IBM). L'ensemble est tendu par une horloge datée : la convergence protocolaire (2024-2026), les entrées en vigueur réglementaires (1ᵉʳ mai 2027) et la migration post-quantique (jalons NIST 2030/2035).


## Publics visés

Architectes d'entreprise et directions technologiques des institutions financières canadiennes ; responsables IAM/CIAM, RSSI et équipes de sécurité offensive/défensive ; responsables risque, conformité et audit (E-23, AMF, Loi 25, ACVM) ; équipes plateforme, SRE et exploitation (AgentOps/MLOps/FinOps) ; dirigeants instruisant la trajectoire de maturité agentique de leur organisation ; chercheurs en interopérabilité, identité décentralisée et sécurité des systèmes multi-agents. *Un lecteur pressé côté canadien peut entrer directement au Livre VII (réglementaire) ou au Livre XI (blueprint), en remontant aux Livres I-III au besoin — le compendium conserve les parcours différenciés des sources.*

## Corpus d'appui hérité du Vol. III — ⚠ introuvable au dépôt, décision en attente

Le Vol. III adossait plusieurs de ses chapitres à trois ouvrages de **littérature secondaire de cadrage** : Arsanjani & Bustos, *Agentic Architectural Patterns for Building Multi-Agent Systems* (Packt — discipline des patrons, trois modèles de maturité, cas fil rouge *loan processing*) ; Nagasubramanian, *Agentic AI for Engineers* (Apress, 2026 — progression automatisation → autonomie, test-évaluation-déploiement) ; Ranjan, Chembachere & Lobo, *Agentic AI in Enterprise* (Apress, 2025 — préparation organisationnelle).

⚠ **Ce corpus n'est pas un acquis, et le compendium ne peut pas en hériter comme s'il l'était.** La vérification du 18 juillet 2026 consignée au PRD du Vol. III (§7.7) établit que **les trois ouvrages sont introuvables au dépôt** — inventaire exhaustif des formats, recherche par auteur, titre et ISBN, balayage de l'historique Git : aucun n'y a jamais existé. La lacune **L-15** est ouverte et déclarée **bloquante au sens fort** ; sept sections du Vol. III et son Annexe E sont bloquées ; la **décision d'auteur P0.2 n'est pas prise**, et l'une de ses deux issues est le **retrait pur et simple de la filiation livresque** — auquel cas le croisement grille × maturité se rebâtit sur l'autonomie graduée et la grille des cinq questions, et le catalogue de patrons sur le seul héritage GoF/EIP. **Tant que P0.2 n'est pas tranchée, aucun chapitre du compendium ne peut être rédigé en s'appuyant sur ces ouvrages** ; les mentions « corpus d'appui » ci-dessous marquent des emplacements conditionnels, pas des sources disponibles. Le renvoi « TOC du Vol. III, § *Corpus d'appui* » est lui-même à manier avec précaution : son titre annonce un dépôt effectué, ce que le PRD ordonne de corriger (J-1).

**Réserves reconduites, si le corpus est acquis** : statut [C] à l'entrée avec élévation [B] par extraction citée ; règle du « jamais seul » (aucune affirmation centrale portée par le corpus sans source primaire concordante) ; datation au bouclage éditorial du livre et revalidation de tout fait périssable à la source primaire ; antériorité à la stabilisation protocolaire de 2025 (Ranjan et al.) ; **biais d'écosystème attaché au seul Arsanjani & Bustos** — la formule « deux ouvrages d'auteurs Google Cloud », reprise de la v0.2, est une incohérence que le Vol. III a lui-même relevée dans ce fichier (J-1) : elle avance un second ouvrage que sa source ne nomme pas, et elle est retirée ; « manuel généraliste, profondeur inégale sur l'identité » (Nagasubramanian) ; « traiter les patrons comme cadre, **vérifier chaque affirmation protocolaire à la source primaire** » (Arsanjani & Bustos).

Chapitres consommateurs : 15 (grille × maturité), 18 (patrons d'interaction humain-agent), 44 (cycle de vie), 47 (modèles de maturité), 49 (préparation organisationnelle) et 50 (cas fil rouge), **plus l'Annexe G** (catalogue de patrons). Les deux derniers rattachements manquaient à la v0.2.

## Volumétrie indicative

Somme naïve des trois volumes (décomptes bruts `wc`, non comparables entre eux — voir la mise en garde) : **Vol. I ≈ 241 000 mots** (dont l'ADS Boréalis en annexe, ≈ 90 000), **Vol. II ≈ 92 000 mots** (décompte de référence PRDPlan §4.2 ; ≈ 200 000 en brut avec pièces de gouvernance), **Vol. III ≈ 102 500 mots** (planifié, non écrit — chiffre re-sommé par le Vol. III lui-même, et non l'arrondi à 100 000 de son TOC). Après déduplication des recouvrements (protocoles, identité, blueprint, réglementaire — estimés à 25-35 % du matériau), le compendium est projeté à **≈ 300 000–326 000 mots**, 54 chapitres en 12 livres, avant-propos, 9 annexes. La borne haute est la **somme exacte des enveloppes par livre déclarées ci-dessous** (326 000) ; la borne basse suppose la déduplication effectivement réalisée. **Fourchette indicative, non normative** (leçon du Vol. II : un écart se documente, il ne se corrige pas par amputation). *⚠ Ces chiffres agrègent des décomptes pris par des commandes différentes ; aucun n'est une mesure unifiée. La première tâche de la rédaction est de re-mesurer les trois corpus par une commande de référence unique (héritage direct de l'incident de décompte du Vol. II).*

---

## Avant-propos et note méthodologique unifiée *(~4 000 mots)*

Origine : la refonte des trois volumes en une somme, motivée par leur continuité démontrée. Définition de travail posée d'entrée : l'**agent d'entreprise** est un système non humain à qui une organisation délègue des tâches qui engagent sa responsabilité, et qu'elle doit rendre interopérable, encadrer et rendre digne de confiance. Reprise du **mode d'emploi de lecture** hérité du Vol. I *Monographie* §5.0.1 (ce qui est acquis des livres amont, ce qui est ajouté) et du patron directeur **« autonomie graduée sous contrôle de finalité »** (§5.0.2, avec les quatre durcisseurs financiers), que la thèse d'ensemble revendique et qui doit donc être posé avant d'être invoqué. **Méthode unifiée** (détail Annexe A) : socle factuel daté et cité ; niveaux de preuve [A]/[B]/[C] (héritage Vol. II) ; tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF pour tout énoncé prospectif (héritage Vol. I) ; vote adversarial multi-juges sur les affirmations centrales ; attribution systématique des métriques auto-déclarées (**PRD Vol. II §7.5**, à chaque occurrence) ; distinction stricte entre lien documenté et inférence d'auteur ; corpus d'appui mobilisé en cadrage, jamais en preuve (règle du « jamais seul », héritage Vol. III) ; **convention de qualification cryptographique** (héritage Vol. III, garde-fou R-02) — un mécanisme est qualifié par ce que sa spécification *démontre*, jamais par ce qu'elle *promet* : c'est cette règle, et non un jugement d'humeur, qui fait du ch. 16 le chapitre « à plus haut risque de surinterprétation » ; **échelle des trois degrés d'absence** (héritage Vol. III, R-14) — *fait négatif vérifié* (établi par balayage documenté) > *fait négatif établi* > *absence de documentation*, jamais interchangeables, le troisième n'autorisant aucune conclusion. **Convention de datation** : gel unique de l'ouvrage + date de gel par chapitre pour les faits périssables. **Décompte** : commande de référence unique à fixer au lancement — le Vol. III en a déjà une (`LC_ALL=C.UTF-8`, PRDPlan §1.5), le Vol. II a assumé un sous-compte de 1,3 % en locale `C` qu'il ne pouvait plus corriger sans invalider ses chiffres publiés ; la somme n'a pas cette contrainte et doit choisir avant de mesurer. **Escalade** : règle d'arbitrage posée *avant* la première rédaction et non apprise en cours de route (héritage Vol. III, PRDPlan §5.3 — au Vol. II, un chapitre pivot a dû trancher seul une remontée non arbitrée). **Motifs de balayage** : les critères d'acceptation et les motifs qui les contrôlent ne se séparent pas (Vol. III, PRD Annexe A §A.6) ; la somme doit se doter des siens, faute de quoi sa méthode n'est pas vérifiable. Avertissements : pas de conseil juridique ni d'investissement ; neutralité fournisseur (Entra Agent ID, watsonx, Boréalis traités comme cas documentés, non comme recommandations). Note sur la fusion : ce qui, dans les trois volumes, était renvoi inter-volumes devient renvoi interne ; les deux divergences factuelles héritées sont tranchées et non plus signalées comme ouvertes — **sans que la clôture d'une divergence vaille clôture d'une lacune** (Annexe C).

*Fusion : Vol. II avant-propos + Vol. I* Monographie *§5.0.1/§5.0.3 (mode d'emploi, convention de sourçage) et §5.0.2 (patron directeur et quatre durcisseurs).*

---

# LIVRE I — Fondements : interopérabilité et ingénierie agentique

*(absorbe Vol. I ch. 1-2 ; ~40 000 mots)*

### Chapitre 1 — L'interopérabilité comme problème d'intégration d'entreprise

**Thèse** : l'interopérabilité n'est pas un attribut mais une propriété à maintenir dans le temps ; la dette d'intégration et le coût de la non-interopérabilité en font un problème économique avant d'être technique.
Sections : définition et taxonomie des niveaux (LCIM) ; couplage, découplage, conception orientée contrat ; SOA → ESB → microservices → maillage de services et d'événements ; styles et contrats d'API ; MOM, courtiers et architecture événementielle ; patrons d'intégration d'entreprise (EIP), orchestration/chorégraphie, exécution durable.
*Fusion : Vol. I* Monographie *§1.0-1.6, condensé. Le §1.3.4 (maillage de services/événements) est **scindé** — le socle transposable y reste, la déclinaison agentique part au Livre IX (ch. 41). Le §1.6.3 (orchestration agentique) part au Livre VI (ch. 25). Coupes assumées : §1.11 (tendances agentiques 2024-2026 — matériau daté, remplacé par les Livres II et XII) et §1.12 (synthèse du chapitre source, absorbée ici).*

### Chapitre 2 — Données, sémantique et ontologies

**Thèse** : l'interopérabilité sémantique — accord sur le sens, pas seulement sur le format — est le niveau que les protocoles agentiques présupposent et que peu savent établir.
Sections : formats, sérialisation, schémas et registres ; transformation, modèle canonique, contrats de données, formats de table ; pile du Web sémantique, médiation ontologique, graphe de connaissances d'entreprise ; LLM et automatisation de l'interopérabilité sémantique.
*Fusion : Vol. I* Monographie *§1.7-1.8. Aval agentique (§3.5) consolidé au Livre II (ch. 9).*

### Chapitre 3 — Sécurité, identité et gouvernance de l'interopérabilité

**Thèse** : le passage du périmètre réseau à la confiance par échange, et l'identité fédérée à autorisation déléguée, sont l'héritage IAM que la fabrique de confiance agentique (Livre III) étire jusqu'à rupture.
Sections : du périmètre à la confiance par échange ; identité fédérée, OAuth/OIDC, autorisation déléguée (**socle pré-agentique** — sa transposition aux agents est au ch. 13) ; zero-trust, identité de charge de travail (SPIFFE/SPIRE), confiance décentralisée ; gouvernance de l'intégration, cycle de vie des contrats, test/certification, observabilité comme condition opérationnelle.
*Fusion : Vol. I* Monographie *§1.9-1.10. **Chapitre-charnière dédoublonné** : pose le socle IAM classique une seule fois. Les ch. 13 (Livre III) et ch. 42 (Livre IX) **y renvoient sans le reconstruire** — ils n'héritent donc pas de §1.9.2 ni de §1.9.3, qui restent ici en entier. C'est la principale économie de la fusion côté identité, et elle n'a lieu que si ces deux chapitres s'y tiennent.*

### Chapitre 4 — L'ingénierie des systèmes agentiques : anatomie, raisonnement, outils

**Thèse** : l'agent est un LLM augmenté d'une boucle perception-raisonnement-action-observation ; son ingénierie est une discipline distincte du prompt, gouvernée par des régimes de contrôle et des niveaux d'autonomie.
Sections : de l'agent conversationnel à l'agent qui agit ; cadre de l'agent rationnel (PEAS, BDI, MAS) ; architectures de boucle mono-agent, séparation contrôleur/exécuteur ; raisonnement, planification, test-time compute ; utilisation d'outils et **MCP comme protocole agent-outil** (anatomie détaillée reportée au ch. 8).
*Fusion : Vol. I* Monographie *§2.1-2.5. L'anatomie protocolaire de MCP (§2.5.4) est **consolidée au ch. 8** ; ici, seul l'usage d'outils au niveau ingénierie.*

### Chapitre 5 — Ancrage informationnel : mémoire, contexte, RAG agentique

**Thèse** : l'agent persistant se construit par l'ingénierie du contexte et une pile de récupération gouvernée ; l'empoisonnement de la mémoire et des sources y est un risque d'identité des *sources* (repris au ch. 20).
Sections : taxonomie de la mémoire, ingénierie du contexte ; architectures de mémoire long terme ; RAG agentique (planifier-récupérer-critiquer-itérer) ; données structurées, accès d'entreprise, gouvernance d'ancrage.
*Fusion : Vol. I* Monographie *§2.6-2.7. Le versant sécurité (empoisonnement) renvoie au ch. 20 (Livre IV).*

### Chapitre 6 — Systèmes multi-agents, évaluation et sûreté

**Thèse** : le multi-agent a un surcoût que seuls certains gains justifient ; son évaluation (succès de tâche vs trajectoire) et sa sûreté (triade létale, vecteurs d'attaque) sont les deux fronts encore ouverts.
Sections : pourquoi le multi-agent, topologies, raisonnement collectif ; communication inter-agents (A2A/ACP — anatomie au ch. 8) ; frameworks d'orchestration et frontière déterministe/agentique (**consolidé au ch. 27**) ; évaluation, LLM-comme-juge, bancs d'essai, red-teaming (la mise en œuvre en production est au ch. 44) ; modèle de menace, vecteurs d'attaque, défense architecturale, alignement.
*Fusion : Vol. I* Monographie *§2.8-2.10, **partagé explicitement** : §2.8.1-2.8.3 et §2.9.1-2.9.5 restent ici ; §2.8.4 (frameworks) fusionne au ch. 27 ; §2.9.6 (observabilité, OTel GenAI) part au ch. 43 ; §2.10.1-2.10.2 (modèle de menace, vecteurs) partent au ch. 20 ; §2.10.3-2.10.5 (défense architecturale, garde-fous d'exécution, alignement) restent ici, le ch. 42 les reprenant au grain de l'infrastructure. Le §2.11.3 (gouvernance par les normes) part au ch. 34, les §2.11.4-2.11.5 (HITL opérationnel, réponse aux incidents, AIOps agentique) au ch. 44, le §2.13.1 (grille « quand agentifier ») au ch. 47 et le §2.13.2 (questions ouvertes) au ch. 53. Coupe assumée : §2.12 (applications et tendances 2024-2026 — remplacé par les Livres VIII et XII).*

---

# LIVRE II — La couche protocolaire agentique

*(fusionne Vol. I ch. 3 — hors §3.6, consolidé au Livre III — + Vol. II Partie I ; ~25 000 mots)*

### Chapitre 7 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts

**Thèse** : en dix-sept mois, la couche protocolaire agentique s'est consolidée sous gouvernance neutre (Linux Foundation) — condition de sa crédibilité en entreprise réglementée ; mais « soutien ≠ production » et AP2 n'a aucun transfert de gouvernance documenté.
Sections : définition et niveaux de l'interopérabilité agentique (LCIM appliqué aux agents, taxonomie des quatre axes) ; chronologie 2024-2026 (MCP → A2A → AGNTCY) ; gouvernance comparée des fondations ; **encadré de désambiguïsation R-8** (collision « (agentic) control plane » à quatre branches) ; lecture critique des métriques d'adoption (**PRD Vol. II §8.2.1** : « soutien ≠ production »).
*Fusion : Vol. II ch. 1 (charpente) + Vol. I* Monographie *§3.0-3.1 (fondements et quatre axes — socle amont de la grille du ch. 15) + §3.13.1 (fondations neutres : AAIF, FIDO). ⚠ Le reste du §3.13 (coexistence/souveraineté, programme de recherche sémantique, synthèse) et le §7.3 (bifurcation de la gouvernance par couche : AAIF, FIDO, W3C, IETF, DIF) vont au **ch. 52** — ne pas les traiter deux fois. Socle : F-01, F-02, F-04, F-05, F-43. Garde-fous : R-1, R-8.*

### Chapitre 8 — Anatomie : MCP (agent-outil) et A2A (agent-agent)

**Thèse** : « MCP dans les agents, A2A entre les agents » — doctrine de complémentarité **déclarée par le projet A2A** (non un accord des deux projets) qui fournit le premier critère de découpage architectural, sans le contraindre.
Sections : MCP (JSON-RPC 2.0, cadre d'autorisation OAuth — « cadre », jamais « sécurisé » ; révision 2025-11-25 ; RC sans état du 28 juillet 2026 à revalider) ; A2A v1.0 (Agent Cards signées, multi-protocole, multi-location) ; MCP comme couche de contrat, A2A et fusion d'ACP-agent ; intégrations infonuagiques (Azure/AWS/Google Cloud).
*Fusion : Vol. I* Monographie *§3.2-3.3 + §2.5.4 + Vol. II ch. 2. Socle : F-01, F-02, F-03, F-16. Garde-fous : réserve F-01.*

### Chapitre 9 — Découverte, registres, portabilité et pile protocolaire

**Thèse** : la découverte et le nommage des agents, et la portabilité inter-modèles/inter-cadriciels, sont les propriétés que l'étagement de la pile protocolaire rend possibles — ou trahit.
Sections : découverte, registres et nommage (pont vers ch. 16) ; la pile de protocoles agentiques et son étagement ; portabilité inter-modèles et inter-cadriciels ; interopérabilité sémantique des agents (de l'accord-de-protocole à la compréhension) ; test de conformité et certification des protocoles.
*Fusion : Vol. I* Monographie *§3.4, §3.5, §3.7-3.8 + §3.12 (conformité protocolaire ; la propagation de trace inter-agents §3.12.3 part au ch. 43). Les registres gouvernés (versant identité/conformité) sont **consolidés au ch. 16** ; ici, le versant protocolaire seul.*

### Chapitre 10 — Transaction et infrastructure : AP2 et AGNTCY

**Thèse** : la transaction pilotée par agents (AP2) est l'aboutissement financier de la pile ; AGNTCY en est la couche d'infrastructure, non un concurrent.
Sections : AP2 (60+ organisations financières — endossement, pas production ; anatomie non documentée au socle, lacune assumée) ; AGNTCY (annuaires, transport SLIM) ; interopérabilité du commerce et des paiements agentiques ; le destin d'ACP (fusion dans A2A — plus haut risque R-1) ; **les feuilles de route de séquencement protocolaire comme jalon historiographique, jamais comme prescription** (réserve F-06 : la séquence MCP → ACP → A2A → ANP est périmée du fait même de la fusion d'ACP).
*Fusion : Vol. I* Monographie *§3.9 + Vol. II ch. 3. **Divergence tranchée** : gouvernance d'AP2 — aucun transfert documenté à date de gel ; **cette absence ne vaut pas fait négatif vérifié** (PRD Vol. II §10.9e), et la lacune reste ouverte au registre de l'Annexe C. Socle : F-04, F-05, F-43 ; **réserve F-06**. Garde-fous : R-1, R-8.*

### Chapitre 11 — Modes d'échec et taxonomie des risques protocolaires

**Thèse** : la sécurité des protocoles dépend de l'implémentation ; empoisonnement d'outils et injection d'invites sont **nommés par les protocoles comme risques attachés**, sans que le socle en date la documentation ni en établisse la mécanique.
Sections : surface d'attaque (outils, invites, mémoire) ; modes d'échec propres à l'interopérabilité agentique ; réponses protocolaires (Signed Agent Cards, autorisation) ; ce que les protocoles ne couvrent pas (renvoi passerelles ch. 42, taxonomie d'identité ch. 20).
*Fusion : Vol. I* Monographie *§3.10-3.11 + Vol. II ch. 4. Socle : F-01, F-02, F-36. Garde-fou : réserve F-01 (« cadre d'autorisation », jamais « sécurisé »).*

---

# LIVRE III — Identité, délégation et fabrique de confiance

*(fusionne Vol. III Parties I-IV + Vol. I §2.11.2/§3.6/§5.5.4/§7.4.2 + Vol. II ch. 8 ; ~30 000 mots)*

### Chapitre 12 — L'héritage : un demi-siècle d'identités non humaines

**Thèse** : l'identité machine n'est pas née avec les agents — comptes de service, X.509, clés d'API forment un passif mal gouverné dont l'entreprise agentique hérite avant d'y ajouter le sien.
Sections : généalogie (comptes de service → workload identity) ; l'écart de gouvernance NHI (ratio machines/humains, prolifération des secrets — illustration, jamais preuve) ; pourquoi l'agent casse le modèle (identité stable vs comportement non déterministe).
*Fusion : Vol. III ch. 1, adossé au ch. 3 (socle IAM déjà posé, non repris). Garde-fou : chiffres de prolifération auto-déclarés.*

### Chapitre 13 — Les standards étirés : OAuth, OIDC, SCIM face à l'agent

**Thèse** : la première vague de l'identité agentique est une extension des RFC existantes, non une rupture — et chaque extension révèle une hypothèse implicite (un humain au bout du flux) qui cesse de tenir.
Sections : OAuth 2.x et l'agent (client ou resource owner ?) ; drafts IETF (délégation, transaction tokens, identité de charge de travail appliquée aux agents) ; SCIM et provisionnement d'agents ; Entra Agent ID **comme extension des RFC** (GA, licences — son traitement comme annuaire commercial est au ch. 16, et n'est pas repris ici) ; ce que les RFC ne disent pas.
*Fusion : Vol. III ch. 2 + Vol. II ch. 8 §8.1/§8.3 + Vol. I* Monographie *§3.6.1-3.6.2 (OAuth 2.1/OIDC appliqués aux agents, Token Exchange). ⚠ Le socle IAM pré-agentique (§1.9.2) **reste au ch. 3** et n'est pas repris ici. Socle : F-07, F-08. Garde-fou : **PRD Vol. II §8.2.5** — statuts pré-normatifs : un brouillon IETF n'est pas une norme, et celui de SCIM-agents est **expiré depuis le 19 avril 2026**. (R-2 et R-3 ne sont pas portés ici : ils vivent au §8.4 et au §8.2 du Vol. II, donc aux ch. 17 et ch. 16.)*

### Chapitre 14 — L'identité décentralisée : VC, DID et la promesse du portable

**Thèse** : le corpus W3C (VC, DID) fournit le vocabulaire du « passeport d'agent », mais son adoption en entreprise financière reste à démontrer — la distinction promesse/production est le fil.
Sections : VC Data Model et DID Core ; DIF et profils d'interopérabilité ; Community Groups agentiques du W3C (signal faible, état 2026) ; le fossé adoption (qui vérifie quoi, en production).
*Fusion : Vol. III ch. 3 + Vol. I* Monographie *§3.6.4 (SPIFFE/SPIRE, DID, WIMSE) et **§7.4.3** (identité vérifiable inter-domaines — le §7.4 est partagé : §7.4.1 et §7.4.4 vont au Livre V, §7.4.2 au ch. 17, §7.4.3 se partage entre ici et le ch. 19). Garde-fou : une charte de groupe n'est pas un standard.*

### Chapitre 15 — La grille des cinq questions

**Thèse** : cinq questions — *qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond* — forment la grille de lecture de tout mécanisme d'identité agentique ; aucun mécanisme de 2026 ne répond aux cinq.
Sections : dérivation depuis les axes du Vol. I (*Monographie* §3.1.7, repris au ch. 7) ; application-témoin à trois mécanismes ; la grille comme critère de structure des chapitres suivants ; croisement grille × maturité (corpus d'appui — construction d'auteur).
*Fusion : Vol. III ch. 4 (chapitre de méthode transversal, homologue de la matrice du ch. 46).*

### Chapitre 16 — Émettre : Agent Card signée, annuaires, registres gouvernés

**Thèse** *(instruit Q3 de la série d'agenda du Vol. II — Monographie ch. 21 §21.2)* : la signature d'une Agent Card vaut ce que valent son ancrage de confiance, sa révocation et sa gouvernance des clés ; le registre gouverné devient la pièce de conformité maîtresse, mais trois modèles concurrents répondent à des questions différentes de la grille.
Sections : Agent Card signée (format, chaîne, ancrage, révocation, valeur probante) ; annuaires commerciaux (Entra Agent ID et pairs — GA/annonce/feuille de route) ; registres gouvernés (spécification CSA `toolAccessList`/`permissionBoundaries`, registres A2A/AGNTCY) ; **le risque de standard de fait** (Vol. III §6.3 : un annuaire commercial dominant fixe la norme sans passer par une norme) ; le registre comme objet réglementaire (pont vers Livre VII).
*Fusion : Vol. III ch. 5-7 + Vol. II ch. 8 §8.2 + Vol. I* Monographie *§3.4 (découverte) et §3.6.3 (preuve cryptographique : Agent Cards signées et VC). Chapitre à plus haut risque de surinterprétation — relecture adversariale prioritaire. Socle : F-07, F-08 + spécifications A2A/CSA/AGNTCY. Garde-fous : **R-3 du Vol. II** (la spécification CSA s'appuie sur SPIFFE/SPIRE comme fondation ; l'exigence stricte n'est pas établie) et **PRD Vol. II §8.2.5** (la spécification CSA est un brouillon de laboratoires, pas une norme).*

### Chapitre 17 — Le passeport d'agent : synthèse d'un objet encore virtuel

**Thèse** : le « passeport d'agent » n'existe dans aucune spécification de 2026 — objet de synthèse assemblant carte signée, inscription au registre, chaîne de mandat et attestations ; sa normalisation 2027-2028 est projetée en statut PROJETÉ. Pour l'entreprise, rien n'entre au maillage sans lui.
Sections : les quatre pièces du passeport ; **ce qui n'existe toujours pas** (Vol. III §7.4 — inventaire des manques côté émission, prolongé ici par le §8.4 du Vol. II) ; qui l'émettrait, qui le vérifierait ; trois scénarios de normalisation (PROGRAMMÉ/PROJETÉ/SPÉCULATIF) ; le passeport par la grille du ch. 15 — la seule construction qui répond aux cinq questions, sur le papier.
*Fusion : Vol. III ch. 8 (chapitre-pivot) + Vol. III §7.4 + Vol. II ch. 8 §8.4 (« ce qui n'existe pas encore ») + Vol. I* Monographie *§7.4.2 (de l'identité au passeport : la normalisation 2027-2028 — siège du statut PROJETÉ ici repris). Garde-fous : **R-2 et R-3**, dont le §8.4 du Vol. II est le siège (encadré « Affirmations écartées »). Inférences d'auteur marquées systématiquement.*

### Chapitre 18 — La chaîne de mandat et le problème des deux sauts

**Thèse** *(instruit le front ouvert du Vol. I,* Synthèse *§11.5)* : la délégation est le maillon faible — les mécanismes de 2026 prouvent qu'un agent *a* une identité, presque aucun ne prouve *au nom de qui* il agit ; au-delà de deux sauts, aucun mécanisme documenté ne maintient une traçabilité opposable de bout en bout.
Sections : le mandat dans les protocoles (AP2, on-behalf-of OAuth, transaction tokens) ; **ce que le droit civil du mandat éclaire — et où l'analogie casse** (Vol. III §9.3, seule occurrence : le versant québécois du mandat est au ch. 31, l'analyse de la limite de l'analogie est ici) ; chaîne de délégation comme objet de première classe ; l'humain premier et dernier maillon (approbation/escalade/HITL relus comme actes de délégation datés ; **patrons d'interaction humain-agent — corpus d'appui, cadrage et non preuve**) ; **le biais d'automatisation et la supervision de façade** — le tamponnage comme mode d'échec documenté de la révision humaine, et le paradoxe de l'explicabilité (une justification mieux rédigée augmente la déférence, pas le discernement) : c'est la limite empirique de la parade sur laquelle reposent l'art. 12.1 (ch. 31) et la supervision E-23 (ch. 29) ; le problème des deux sauts (où chaque mécanisme perd le fil, pistes et limites, question de recherche).
*Fusion : Vol. III ch. 9-10 + Vol. I* Monographie *§2.11.2 (chaînes multi-saut) et §3.6.6 (l'axe agent-humain : HITL négocié). Socle : spécification AP2 (**divergence de gouvernance déjà tranchée au ch. 10**) ; **le versant biais d'automatisation est un front neuf — aucun des trois volumes ne le porte, sources primaires à établir.** Frontière de la connaissance vérifiable exposée, non comblée.*

### Chapitre 19 — Know Your Agent : la vérification d'agent tiers inter-domaines

**Thèse** : le KYA transpose la logique du KYC — vérifier avant d'admettre — sans l'infrastructure institutionnelle qui rend le KYC possible ; la *trust fabric* inter-entreprises reste privée et fragmentée, et c'est elle qui décide si l'entreprise agentique s'arrête à ses murs.
Sections : état des propositions KYA ; admission d'un agent tiers (point de contact identité/frontières) ; fédérations de confiance (eIDAS, FIDO) et transposabilité.
*Fusion : Vol. III ch. 11 + Vol. I* Monographie *§5.5.4 (SIÈGE du KYA), §3.6.5 et §7.4.3 (trust fabric inter-domaines, partagé avec le ch. 14). Garde-fou : « KYA » est un terme de marché avant d'être un terme de norme.*

---

# LIVRE IV — La confiance hostile : attaques et défense

*(fusionne Vol. III Partie IV + Vol. I §2.10.1-2.10.2/§7.5 ; ~10 000 mots)*

### Chapitre 20 — Taxonomie des attaques d'identité et de délégation

**Thèse** *(instruit Q2 de la série d'agenda du Vol. II — Monographie ch. 21 §21.2)* : une part majoritaire des attaques propres aux systèmes multi-agents documentées à date sont des attaques d'identité (usurpation, confusion de délégué) ou de délégation (élévation par chaîne de mandat) — ce qui justifie d'absorber la sécurité dans le cadre identitaire.
Sections : recension (identifiants de vulnérabilité, incidents datés, littérature) ; taxonomie par la grille du ch. 15 ; empoisonnement de la mémoire et des sources (provenance RAG comme problème d'identité des sources — reprend le ch. 5) ; ce que la recension ne trouve pas.
*Fusion : Vol. III ch. 12 + Vol. I* Monographie *§2.10.1-2.10.2. ⚠ **La thèse de ce chapitre est le premier énoncé à instruire avant rédaction** : le Vol. II pose Q2 précisément parce que son socle ne porte **aucune** attaque propre à A2A (PRD §10.8 — absence de documentation, non fait négatif vérifié). La proportion affirmée doit être établie par dénombrement sur un corpus déclaré, ou l'énoncé retombe à « une part notable » sans quantificateur. Traitement défensif exclusif : mécanique au niveau architectural, sans recette d'exploitation.*

### Chapitre 21 — Usurpation, rug-pull et révocation

**Thèse** : la vérification à l'admission ne protège pas contre la dérive après admission (rug-pull d'un serveur d'outils ou d'un agent tiers) ; et chaque mécanisme spécifie l'émission avec soin et la révocation avec négligence — asymétrie qui reproduit l'histoire des PKI.
Sections : le rug-pull documenté ; vérification continue vs à l'admission ; attestation d'intégrité à l'exécution ; inventaire de la révocation par mécanisme ; précédent PKI (CRL, OCSP) ; révocation en cascade dans une chaîne de délégation (problème ouvert).
*Fusion : Vol. III ch. 13-14. Renvoi ch. 44 (dérive en exploitation) et ch. 50 (révocation dans le cycle de vie).*

### Chapitre 22 — L'agentic SOC et la boucle défensive

**Thèse** : la défense s'agentifie elle-même, et l'identité distingue un SOC agentique gouvernable d'un système auto-organisé ingouvernable — les agents défensifs sont les premiers à devoir porter le passeport du ch. 17.
Sections : état de l'agentic SOC (offres datées, périmètres réels) ; symétrie attaque/défense relue par l'identité ; référentiels de sécurité agentique en mouvement (état 2026).
*Fusion : Vol. III ch. 15 + Vol. I* Monographie *§7.5 (trajectoire de la menace).*

---

# LIVRE V — L'horloge post-quantique

*(fusionne Vol. III Partie V + Vol. I §7.4.1/§7.4.4 ; ~10 000 mots)*

### Chapitre 23 — La menace quantique appliquée à la pile identitaire agentique

**Thèse** : toute la fabrique d'émission (Livre III) repose sur des signatures classiques ; les jalons du NIST IR 8547 — dépréciation **visée** pour 2030, retrait **visé** pour 2035 — tombent dans la durée de vie des architectures conçues aujourd'hui, la PQC est donc une contrainte de conception et non une annexe.
Sections : échéances et sources (⚠ **garde-fou R-11 du Vol. III** : écrire « visée », jamais « fixée » ni « ~2030 » ; et porter le **statut du document** — IR 8547 est au socle hérité un *Initial Public Draft*, avec réserve « dates à re-vérifier ». Les quatre statuts de l'Annexe D — annoncé / visé / attendu / incertain — s'appliquent ici comme ailleurs) ; *harvest now, decrypt later* appliqué aux artefacts d'identité longue durée ; inventaire (quels artefacts cassent, et quand).
*Fusion : Vol. III ch. 16 + Vol. I* Monographie *§7.4.1.*

### Chapitre 24 — Crypto-agilité et dette de migration

**Thèse** : la crypto-agilité est l'application de l'invariant du Vol. I (découplage, contrat, évolution) à la couche cryptographique ; la dette de migration PQC est réelle mais largement non chiffrée — méthode d'estimation plutôt que chiffre.
Sections : définition opérationnelle, état des recommandations NIST ; audit de crypto-agilité des mécanismes du Livre III ; **méthode d'inventaire pour une institution** (Vol. III §18.2 — la section qui porte la « méthode d'estimation plutôt que chiffre » annoncée à la thèse) ; patrons de migration sans rupture de chaîne de confiance ; ce que les études de coût couvrent (et pas) ; fenêtre d'action 2026-2029.
*Fusion : Vol. III ch. 17-18 + Vol. I* Monographie *§7.4.4 (l'horloge de l'horizon ; §7.4.2 et §7.4.3 sont au Livre III). Garde-fou : refus d'extrapoler un chiffre non porté par le socle.*

---

# LIVRE VI — L'autonomie encadrée : orchestration en entreprise

*(fusionne Vol. II Partie II + Vol. I ch. 4 + §1.6.3/§2.8.4 ; ~30 000 mots)*

### Chapitre 25 — Les options d'orchestration : la taxonomie OO1-OO4

**Thèse** : le choix d'architecture agentique est un choix de position sur un continuum d'encadrement, objectivable par cinq propriétés et sept critères.
Sections : OO1-OO4 ; cinq propriétés (autonomie, spécificité, réactivité, correction, traçabilité) ; critères de sélection ; métriques quantitatives (illustration — préprint) ; exécution durable et pipelines (du ch. 1).
*Fusion : Vol. II ch. 5 + Vol. I* Monographie *§1.6.3. Socle : F-37. Garde-fou : source unique (préprint v1).*

### Chapitre 26 — Le paradigme APM : l'autonomie encadrée

**Thèse** : l'autonomie n'est pas l'automatisation ; elle se gouverne par des frames normatifs et opérationnels et quatre capacités (encadrement, explicabilité, actionnabilité conversationnelle, auto-modification).
Sections : système APM, distinction autonomie/automatisation ; frames normatifs vs opérationnels ; quatre capacités ; frames locaux comme frontière de sécurité ; « responsibility gap » (préparé ici, exploité au ch. 33).
*Fusion : Vol. II ch. 6. Socle : F-36. Garde-fou : R-1 (mention ACP du manifeste antérieure à la fusion).*

### Chapitre 27 — Les frameworks d'orchestration d'entreprise

**Thèse** : l'offre s'est industrialisée en 2025-2026 (Agent Framework, LangGraph, orchestration événementielle Kafka/Confluent) avec un support MCP **répandu et inégalement établi** et un support A2A de périmètre inégal.
Sections : Microsoft Agent Framework ; LangGraph Platform (A2A pour la plateforme commerciale seulement) ; orchestration événementielle (Streaming Agents, A2A sur Kafka ; Confluent acquise par IBM, clôture 17 mars 2026) ; encadrés Temporal [C], CrewAI [B] ; grille OO1-OO4 des patrons.
*Fusion : Vol. II ch. 7 + Vol. I* Monographie *§2.8.4. Socle : F-15, F-16, F-32, F-33, F-41. Garde-fou : PRD Vol. II §8.2.3 (chiffres d'éditeurs auto-déclarés).*

### Chapitre 28 — Le passage à l'échelle de l'entreprise

**Thèse** : de la dette d'intégration à la prolifération d'agents, l'entreprise doit intégrer les agents à son tissu existant, gouverner le parc à l'échelle et instruire sa maturité — sans dupliquer l'IAM et l'observabilité en place.
Sections : intégrer les agents au tissu d'intégration existant ; plateformes d'agents d'entreprise et stratégie de standards ouverts ; **identité et accès des agents à l'échelle du parc** (application des Livres III-IV au grain de la plateforme, sans reconstruire leur doctrine) ; accès aux données d'entreprise et ancrage gouverné ; orchestration/collaboration humain-agent inter-équipes et B2B ; sécurité du parc à l'échelle ; capacité d'inférence, budget de latence et contention comme contraintes de dimensionnement ; adoption organisationnelle, modèle opérationnel, maturité.
*Fusion : Vol. I* Monographie *ch. 4 (§4.1-4.7, §4.10-4.11), le §4.4 (identité et accès à l'échelle) recevant enfin une section d'accueil. Le §4.8 (gouvernance/conformité) part au Livre VII ; le §4.9 (observabilité/FinOps) au Livre X ; le §4.12 (architectures de référence) au Livre XI.*

---

# LIVRE VII — Le cadre réglementaire canadien

*(fusionne Vol. II Partie III + Vol. III Partie VI + Vol. I §4.8/§5.3 ; ~25 000 mots)*

### Chapitre 29 — E-23 : le risque de modèle à l'ère de l'IA

**Thèse** : E-23 couvre l'IA agentique *implicitement*, par sa définition de « modèle » — couverture par inférence que les institutions doivent traiter comme acquise d'ici le 1ᵉʳ mai 2027 ; l'identité agentique est le prérequis technique d'obligations qui ne la mentionnent pas.
Sections : genèse et calendrier ; définition de « modèle » et anticipation des systèmes autonomes ; l'inférence agentique ; le registre du ch. 16 comme condition d'inventaire ; la supervision humaine exigée et sa limite empirique (ch. 18) ; **ce que les cadres n'exigent pas — ne pas leur faire dire plus** (Vol. III §19.3) ; rapport BSIF-ACFC (risque de causalité indéterminable).
*Fusion : Vol. II ch. 9 + Vol. III ch. 19, **volet E-23 seul** — la relecture de la ligne directrice AMF par la grille des cinq questions (§19.1, seconde moitié) va au ch. 31, qui est son siège. Socle : F-09 (les deux strates), F-10. Garde-fous : PRD Vol. II §8.2.4 (couverture E-23 = inférence d'analystes) et PRD Vol. II §8.2.6 (projections).*

### Chapitre 30 — Le vide fédéral : de C-27 à C-36

**Thèse** : la mort de la LIAD laisse le Canada sans régulation fédérale spécifique de l'IA ; C-36 (loi sur la vie privée, non loi IA autonome) ne comble pas ce vide — la couverture effective passe par les régulateurs sectoriels.
Sections : prorogation du 6 janvier 2025, mort de C-27 ; ministre de l'IA et C-36 (réforme LPRPDE, *Digital Safety and Data Protection Commission*) ; conséquences pour les institutions financières.
*Fusion : Vol. II ch. 10. Socle : F-24 [B, revalidé].*

### Chapitre 31 — Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25

**Thèse** : le Québec dispose du cadre le plus explicite ; l'art. 12.1 (révision humaine sur demande) entre en friction directe avec la décision agentique autonome, et son imputabilité pèse sur l'assujetti.
Sections : ligne directrice AMF (**finale le 30 mars 2026** — divergence tranchée, voir Annexe C ; en vigueur 1ᵉʳ mai 2027 ; ⚠ **seules ses dates sont au socle, jamais son contenu** — lacune PRD Vol. II §10.4, la plus coûteuse du volume, à rouvrir par extraction de la source primaire avant rédaction ; ne jamais écrire « en attente », réserve F-25) ; art. 12.1 (trois obligations, texte officiel) ; critère « exclusivement » et HITL (nuance Fasken vs CAI ; le biais d'automatisation du ch. 18 comme limite empirique de la parade) ; la ligne directrice AMF relue par la grille des cinq questions (Vol. III §19.1) ; le mandat en droit civil québécois (Vol. III §20.2 ; la limite de l'analogie est au ch. 18) ; le droit des renseignements personnels et la chaîne de délégation (qui traite, qui décide, qui répond).
*Fusion : Vol. II ch. 11 + Vol. III ch. 20 (**volet Loi 25 seul** — le volet RGPD va au ch. 34) + Vol. III ch. 19 §19.1 (moitié AMF). Socle : F-25, F-27. Garde-fou renforcé : aucun avis juridique ; ⚠ la position « finale le 30 mars 2026 » porte une **dette de vérification déclarée** au Vol. II (source primaire renvoyant 403 aux outils employés le 17 juillet 2026) — la divergence est tranchée, la vérification reste due.*

### Chapitre 32 — Valeurs mobilières : l'avis ACVM 11-348

**Thèse** : les lois existantes s'appliquent — la définition retenue des systèmes d'IA (autonomie et adaptativité variables) capture nativement l'agentique.
Sections : portée et doctrine (« ne crée ni ne modifie aucune exigence ») ; attentes (gouvernance, explicabilité, supervision) ; suites de la consultation.
*Fusion : Vol. II ch. 12. Socle : F-26.*

### Chapitre 33 — Le pont : des contraintes réglementaires aux frames déterministes

**Thèse** *(pivot)* : la plupart des exigences canadiennes lues se traduisent en frame d'architecture ; l'encadrement déterministe des processus réglementés est le principe sur lequel convergent trois sources **non indépendantes**, dont le socle n'établit l'application ni au Canada ni à la finance canadienne — la portée de la convergence, pas son autorité majorée.
Sections : table de traduction exigences → frames (⚠ la ligne AMF y est la seule entrée qui ne produit **aucune** contrainte, faute de contenu au socle — l'écrire, ne pas la combler) ; verdict empirique (F-37) et convergence à trois sources (F-36, F-37, F-46) ; imputabilité (qui répond du comportement émergent) ; énoncé du principe directeur repris aux Livres XI-XII.
*Fusion : Vol. II ch. 13 (chapitre-pivot conservé intact). Socle : F-09 (deux strates), F-25, F-26, F-27, F-36, F-37, F-46 ; F-10, F-35 en renvoi.*

### Chapitre 34 — Le maillage réglementaire international et la normalisation institutionnelle

**Thèse** : hors Canada, l'AI Act, ISO 42001, le RGPD et les cadres sectoriels dessinent le maillage transversal que l'agent en finance régulée doit satisfaire ; et la désignation de l'organisme de normalisation technique du cadre bancaire canadien fixera qui écrit les règles d'identité des agents financiers.
Sections : gouvernance et conformité d'entreprise (AI Act, ISO 42001, RGPD, sectoriel — du Vol. I *Monographie* §4.8) ; maillage réglementaire UE/US/Canada-Québec et double-qualification agent = modèle + tiers TIC (Vol. I *Monographie* §5.3) ; normalisation institutionnelle du cadre bancaire (Q5 de la série d'agenda du Vol. II — *Monographie* ch. 21 §21.2) ; normalisation internationale (ISO/IEC SC 42, CEN-CENELEC, NIST) appliquée à l'identité d'agent.
*Fusion : Vol. III ch. 21 + Vol. III ch. 20 (**volet RGPD** — le volet Loi 25 est au ch. 31) + Vol. I* Monographie *§4.8/§5.3/§2.11.3 (gouvernance par les normes) + Vol. II ch. 21 §21.2 (Q5). Instruit la lacune PRD Vol. II §10.1 (aucun arrêté au 16 juill. 2026). Garde-fou : R-5 du Vol. II.*

---

# LIVRE VIII — Le terrain canadien : interopérabilité financière et adoption

*(fusionne Vol. II Parties IV-V + Vol. I ch. 5 ; ~35 000 mots)*

### Chapitre 35 — Le vertical financier : pourquoi l'agentique y est durcie

**Thèse** : la finance durcit l'agentique par des contraintes transverses (standards de données, maillage réglementaire, risque-modèle, sécurité/AML-KYC/KYA, résidence/souveraineté) qui préexistent à l'agent et le contraignent.
Sections : positionnement du vertical et rappel des quatre durcisseurs (posés à l'avant-propos) ; standards de données financières (substrat sémantique) ; risque-modèle, auditabilité, explicabilité ; sécurité, fraude, AML-KYC et identité d'agent ; données, résidence et souveraineté.
*Fusion : Vol. I* Monographie *§5.1-5.6. Le §5.0 (orientation, durcisseurs, convention de sourçage) est **acheminé à l'avant-propos**, dont il fournit le mode d'emploi de lecture. Le §5.5.4 (KYA) est déjà consolidé au ch. 19 — les §5.5.1-5.5.3 (triade létale, fraude, AML-KYC) restent ici ; cadrage financier transverse.*

### Chapitre 36 — Le cadre des services bancaires axés sur le consommateur

**Thèse** : le cadre est légiféré (C-15), supervisé par la Banque du Canada, réglementairement en cours — et son standard technique n'est **pas** désigné (fait négatif vérifié).
Sections : de 2024 à C-15 (mobilité des données) ; supervision Banque du Canada, accréditation, registre ; règlement prépublié (27 juin 2026, entrée échelonnée) ; le standard technique (organisme à désigner par arrêté — FDX = anticipation d'industrie).
*Fusion : Vol. II ch. 14. Socle : F-11, F-23, F-34, F-35. Garde-fou : R-5.*

### Chapitre 37 — ISO 20022 : Lynx accompli, RTR visé

**Thèse** : la couche sémantique commune des paiements canadiens est en place — Lynx a achevé sa bascule ; Paiements Canada annonce un RTR nativement ISO 20022 dès son lancement, **visé** au T4 2026 (cible plusieurs fois repoussée — attribuer, ne pas affirmer au futur catégorique).
Sections : Lynx (fin de coexistence MT/MX, 22 nov. 2025, alignée CBPR+) ; RTR (chronologie vérifiée, partenaires, cible T4 2026 ; ⚠ **formulation imposée — « la cible a été successivement reportée : 2019, puis 2022, puis 2023, puis 2026 » : ce sont quatre *cibles successives*, non quatre reports ni les dates auxquelles les reports ont été décidés** — PRDPlan Vol. II §4.4) ; By-law no 10 ; ce que la couche sémantique change — et ce que le socle n'en dit pas.
*Fusion : Vol. II ch. 15. Socle : F-28, F-29, F-45. Garde-fous : R-4 (la cible T4 2026 *est* officiellement annoncée) et réserve F-29 (ne jamais écrire « lancé » ni « en production »).*

### Chapitre 38 — Les sous-domaines financiers : banque, assurance, patrimoine

**Thèse** : l'agentique se décline différemment selon le sous-domaine — bancaire, IARD, assurance de personne, gestion de patrimoine, services TI financiers — chacun avec sa maturité et ses points de durcissement propres.
Sections : bancaire (détail, gros, paiements, crédit, core banking) ; assurance dommage (IARD/P&C) ; assurance de personne (vie & santé) ; gestion de patrimoine & d'actifs ; services TI dans le domaine financier ; synthèse par sous-domaine (études de cas datées, bancs d'essai sectoriels, questions ouvertes, bacs à sable réglementaires) ; **synthèse et transition du bloc financier** (Vol. I *Monographie* §5.14).
*Fusion : Vol. I* Monographie *§5.7-5.11 + §5.12.4-5.12.7 + §5.14 (synthèse de chapitre — **rattachement corrigé en v0.3** : le §5.14 est la clôture du ch. 5, non un développement sur les paiements agentiques). Les §5.12.1-5.12.3 (architecture de référence, maturité, grille de décision) sont consolidés au ch. 47 ; le §5.13 (interop B2B, commerce et paiements agentiques) au ch. 40.*

### Chapitre 39 — Études de cas : la production agentique canadienne (2025-2026)

**Thèse** : l'agentique canadienne est en production, documentée par sources primaires, gouvernée au niveau C-suite — et inégalement documentable selon les institutions.
Sections : TD (Layer 6, pré-adjudication RESL) ; Scotiabank (AIDox ; consortium Agentic Control Plane) ; RBC (AI Group, FINOS) ; Manuvie (runtime Akka, Global CAIO) ; Desjardins (plan 2026-2029) ; CIBC (assistive — ne pas surqualifier) ; Intact (~600 modèles, sans terminologie agentique) ; BMO et Sun Life (élevés en P0) ; gouvernances comparées et code de conduite volontaire.
*Fusion : Vol. II ch. 17 (conservé intact). Socle : F-17 à F-23b (F-18, F-19, F-20, F-21 et F-22 à nommer un à un à la rédaction, la plage seule ne les désignant pas), F-30, F-31, F-47, F-48. Garde-fous : **PRD Vol. II §7.5** (métriques institutionnelles auto-déclarées, attribution à chaque occurrence), R-8.*

### Chapitre 40 — Prospective : AP2 sur les rails canadiens ?

**Thèse** *(explicitement prospectif)* : aucune source ne documente l'articulation AP2 ↔ rails canadiens — le chapitre pose le cadre d'analyse et les conditions de possibilité, sans affirmer (énumérer des conditions n'est pas prédire).
Sections : état de la question (lacune assumée) ; interopérabilité B2B, commerce et paiements agentiques en finance (Vol. I *Monographie* §5.13) ; conditions de possibilité ; questions de recherche (série AP2/RTR — Vol. II *Monographie* ch. 16 §16.3, Q1-Q5).
*Fusion : Vol. II ch. 16 + Vol. I* Monographie *§5.13. Socle : F-04, F-29. Garde-fou : ne pas combler la lacune par de la fiction.*

---

# LIVRE IX — AgentMesh : le maillage d'agents comme patron d'infrastructure

*(fusionne Vol. III Partie VII + Vol. I §1.3.4 ; ~15 000 mots)*

⚠ **Désambiguïsation obligatoire, garde-fou R-04 du Vol. III, branche (f).** « AgentMesh » désigne ici — et partout dans la somme — le **patron d'infrastructure** (plan de données médiatisant chaque arête, plan de contrôle centralisant la politique). Le terme sert ailleurs dans l'industrie à nommer une **équipe plateforme**, un **produit commercial** et une **couche de courtage** ; la branche (f) de R-04 a précisément été ouverte parce que la v0.1 de ce fichier employait le mot dans deux sens incompatibles à trente lignes d'écart. Le glossaire (Annexe E) porte les six emplois ; aucun chapitre n'emploie le terme sans que le sens visé soit déterminable de sa phrase.

### Chapitre 41 — Du service mesh à l'agent mesh : généalogie et anatomie

**Thèse** : le maillage d'agents est la réinstanciation, au niveau agentique, du patron *service mesh* — un plan de données qui médiatise chaque arête, un plan de contrôle qui centralise la politique ; cette filiation trie ce que le terme recouvre réellement de ce qu'il recouvre en marketing.
Sections : généalogie (sidecar, passerelle, plan de contrôle/données ; mTLS, SPIFFE/SPIRE transposables — repris du ch. 1) ; anatomie du maillage agentique (passerelles d'outils, courtage A2A, transport SLIM, routage sémantique) ; ce que l'arête change (la sûreté n'est pas compositionnelle) ; grille du ch. 15 appliquée.
*Fusion : Vol. III ch. 22 + Vol. I* Monographie *§1.3.4. Garde-fous : « agent mesh » terme de fournisseur ; désambiguïsation R-8 du Vol. II (« control plane » — le patron décrit ici comporte un plan de contrôle, terme dont les quatre branches de la collision sont le siège de ce garde-fou) ; la désambiguïsation d'« AgentMesh » lui-même relève de R-04 du Vol. III, branche (f), imposée en tête de livre.*

### Chapitre 42 — Le maillage comme point d'application : PEP/PDP et zero trust agentique

**Thèse** : le maillage est le lieu où le passeport du ch. 17 devient opposable — PEP adossé à un PDP, transposition du zero trust au graphe d'agents : vérifier chaque arête, sans confiance héritée de la topologie.
Sections : PEP/PDP agentiques (langages de politique, état des mécanismes) ; garde-fous d'exécution au grain de l'arête (application des principes de défense architecturale du ch. 6) ; zero trust transposé (« jamais confiance au graphe ») ; le maillage et la chaîne de mandat (ce qu'il trace du problème des deux sauts, ch. 18 — et ce qu'il ne résout pas) ; coûts (latence, complexité, point de défaillance — conditions qui renversent la recommandation).
*Fusion : Vol. III ch. 23 + Vol. I* Monographie *§2.10.3-2.10.4 (défense architecturale et garde-fous, appliqués ici, posés au ch. 6). ⚠ Le socle zero-trust pré-agentique (§1.9.3) **reste au ch. 3** et n'est pas reconstruit ici. Socle : NIST SP 800-207. Prolonge les points de contrôle obligatoires (Vol. II ch. 19 §19.3) au grain de l'infrastructure.*

---

# LIVRE X — AgentOps : exploiter la confiance dans la durée

*(fusionne Vol. III Partie VIII + Vol. I §2.9.6, §2.11.1/§2.11.4-2.11.5 et §4.9 ; ~12 000 mots)*

### Chapitre 43 — L'observabilité agentique

**Thèse** : l'AgentOps commence par l'observabilité, dont le socle de standardisation est les conventions sémantiques GenAI/agents d'OpenTelemetry — mais tracer un *appel* n'est pas tracer une *délégation* : la corrélation trace ↔ chaîne de mandat est le chaînon manquant.
Sections : de l'APM à l'AgentOps (non-déterminisme, coût par jeton, horizon de tâche) ; état des conventions OTel (stable/expérimental — à dater) ; journalisation probatoire (pont vers E-23, ch. 29) ; corréler la trace au passeport (l'identité comme clé de jointure).
*Fusion : Vol. III ch. 24 + Vol. I* Monographie *§2.9.6 (observabilité, OTel GenAI — **seule affectation**, le ch. 6 ne la conserve pas), §3.12.3 (propagation de trace inter-agents) et §4.9.1-4.9.2 (OTel étagé, journal d'audit probatoire). Garde-fou : « AgentOps » désigne la discipline, non un produit homonyme.*

### Chapitre 44 — Le cycle de vie opérationnel : évaluation continue, dérive et incident

**Thèse** : l'exploitation d'un parc d'agents est une boucle — évaluer, détecter la dérive, répondre à l'incident, réviser le mandat — réalisation opérationnelle du quatrième terme de l'invariant ; sans elle, le passeport certifie un comportement passé, jamais le comportement courant.
Sections : évaluation en production (des jeux d'essai à l'évaluation continue) ; dérive agentique (modèle, outil — rug-pull du ch. 21 relu en signal —, autonomie) ; réponse à incident (révocation d'urgence ch. 21, confinement par le maillage ch. 42, agentic SOC ch. 22) ; GitOps du parc ; l'agent qui apprend (revalidation après apprentissage) ; **cycle de vie et modèles de maturité — corpus d'appui, cadrage et non preuve**.
*Fusion : Vol. III ch. 25 + Vol. I* Monographie *§2.11.4-2.11.5 (HITL opérationnel, réponse aux incidents, AIOps agentique). ⚠ Le §2.9 n'est **pas** repris ici : ses fondements restent au ch. 6, son versant observabilité va au ch. 43. Chapitre de synthèse refermant les fils des Livres III-V.*

### Chapitre 45 — Les indicateurs de l'AgentOps et le FinOps des agents

**Thèse** : la discipline naissante n'a pas ses indicateurs de référence ; les métriques publiées sont hétérogènes et auto-déclarées — grille minimale dérivée des obligations des Livres VII-IX, présentée comme construction d'auteur ; le modèle de coût agentique est une contrainte d'ingénierie de premier ordre.
Sections : recension critique des métriques publiées ; grille minimale (disponibilité du parc, couverture de traçabilité, délai de révocation, fraîcheur des évaluations) ; métrique d'horizon de tâche déléguée ; **indicateurs de la supervision humaine** (délai médian de révision, taux de renversement — proxies imparfaits du tamponnage, ch. 18) ; FinOps des agents (coût par résolution, budget par jeton, routage de modèles et mise en cache comme leviers, latence comme contrainte d'usage).
*Fusion : Vol. III ch. 26 + Vol. I* Monographie *§4.9.3-4.9.5 et **§2.11.1** (modèle de coût agentique — **seule affectation**, le ch. 43 ne la revendique plus). Garde-fou : chaque indicateur marqué construction d'auteur, chaque chiffre attribué.*

---

# LIVRE XI — Synthèse architecturale et blueprint

*(fusionne Vol. I ch. 6 + Annexe B ADS + Vol. II Partie VI + ch. 21-22 + Vol. III Partie IX ; ~35 000 mots)*

### Chapitre 46 — La matrice protocoles × exigences réglementaires

**Thèse** : croiser la pile protocolaire (MCP/A2A/AP2) avec les exigences canadiennes (E-23, AMF, art. 12.1, 11-348, cadre bancaire) et la grille des cinq questions révèle où les standards suffisent et où l'architecture doit compenser — et, à date, quinze croisements sans lien documenté.
Sections : construction de la matrice ; lecture par protocole ; lecture par exigence ; zones de compensation architecturale.
*Fusion : Vol. II ch. 18 + Vol. II Annexe B (matrice détaillée — source des quinze croisements) + Vol. III Annexe B (matrice des mécanismes). Socle transversal (Livres II-VIII, énuméré à la rédaction).*

### Chapitre 47 — L'architecture de référence unifiée par couches

**Thèse** : les Livres I-X se composent en une architecture cible neutre à couches (protocoles, identité/registre, orchestration, maillage, exploitation, gouvernance), structurée par OO1-OO4, avec OO3/OO4 et la fabrique d'identité imposés sous exigence réglementaire stricte.
Sections : couches et responsabilités (fabrique d'identité, maillage, AgentOps — les trois étages) ; positionnement OO par cas d'usage et grille « quand agentifier » ; points de contrôle obligatoires ; le plan de contrôle d'agents comme architecture de référence ; le modèle de maturité de l'entreprise agentique (confrontation des trois modèles de maturité — **corpus d'appui**, cadrage et non preuve, sous réserve de la décision P0.2 — et de l'échelle **assistance → copilote → orchestration sous revue → autonomie bornée** ; ⚠ **garde-fou R-13 du Vol. III** : ne jamais écrire « l'autonomie graduée du Vol. I » sans autre précision, ce volume portant trois échelles distinctes — celle-ci, le continuum 0-5 du *Monographie* §2.2.4 et la graduation L0-L3 de son Annexe B §1.3) ; alternatives et variantes.
*Fusion : Vol. II ch. 19 + Vol. III ch. 27 §27.1/§27.4 + Vol. I* Monographie *§5.12.1-5.12.3, §6.10 (maturité et feuille de route par plateaux — **prélevé au ch. 6 du Vol. I, que le ch. 48 traite par ailleurs en bloc**), §4.12 (plan de contrôle d'agents) et §2.13.1 (grille « quand agentifier »). Socle : F-36, F-37, F-46 + Livre VI.*

### Chapitre 48 — La formalisation ArchiMate

**Thèse** : l'architecture de référence se formalise en ArchiMate (méthode-signature) — les domaines Motivation, Strategy, Business, Application et Technology captent intentions réglementaires, capacités agentiques, rôles humain-agent, agents/protocoles/runtime/résidence, avec des points de vue transverses sécurité/conformité/observabilité.
Sections : primer ArchiMate et patrons pour concepts agentiques ; Motivation (exigences réglementaires traçables) ; Strategy (capacités, chaînes de valeur financières) ; Business (rôles, collaborations, objets financiers) ; Application & Technology (agents, protocoles, runtime, résidence) ; points de vue transverses ; gouvernance des vues ; bibliothèque de patrons et anti-patrons.
*Fusion : Vol. I* Monographie *ch. 6 **hors §6.8 et §6.10**, prélevés respectivement par les ch. 50 et ch. 47. Consolide les fonctions d'identité, points d'application du maillage et boucle d'exploitation (Vol. III §27.2) dans le formalisme ArchiMate.*

### Chapitre 49 — Le blueprint instancié : de Boréalis au portefeuille IBM à la fabrique de confiance

**Thèse** : le blueprint applique les principes directeurs à un portefeuille réel documenté ; chaque couche porte son positionnement OO, son statut de preuve et son point d'intégration avec l'IAM et l'observabilité en place — étendre, jamais dupliquer.
Sections : principes directeurs (dont « aucune interaction IA non gouvernée ») ; C1-C8 avec composants IBM datés (GA/préversion/déprécié ; pivot Confluent clôturé le 17 mars 2026 — écrire au passé) ; correspondance réglementaire (statuts explicites — **aucune conformité E-23/B-13 revendiquée par IBM : fait négatif *établi*, non *vérifié***, garde-fou R-07 du Vol. III et échelle des trois degrés d'absence) ; l'organisation de la fabrique (rôles entre plateforme, IAM, sécurité, exploitation ; préparation organisationnelle — **corpus d'appui**, cadrage et non preuve, sous réserve de la décision P0.2 ; facteur humain et conduite du changement).
*Fusion : Vol. II ch. 22 (**scindé avec le ch. 50** : l'architecture du portefeuille ici, les flux de bout en bout là) + Vol. III ch. 27 §27.3/§27.5 + Vol. I Annexe B (ADS Boréalis, résumée ici, complète en Annexe H). **Décision de fusion** : les deux instanciations (Boréalis du Vol. I, portefeuille IBM du Vol. II) sont présentées comme deux réalisations de la même architecture de référence, non comme deux blueprints concurrents. Socle : F-38 à F-46 (F-39, F-40 et F-42 à nommer un à un, la plage seule ne les désignant pas) ; Vol. II Annexe B §B.1-B.2. Garde-fous : **CA-8** (chaque composant tracé au socle, chaque lien réglementaire marqué « documenté » ou « inférence »), PRD Vol. II §8.4 (neutralité fournisseur), **R-5, R-6, R-7 et R-8 du Vol. II** — nommés par volume, ce chapitre consommant aussi du Vol. III, dont les R-05…R-08 portent sur d'autres objets (décision 7).*

### Chapitre 50 — Instanciation : le cycle de vie complet d'un agent d'entreprise

**Thèse** : le blueprint se prouve par le parcours — de l'enregistrement à la révocation, chaque transition est jouée contre l'architecture, au grain d'un cas financier canadien (continuité Boréalis).
Sections : naissance (enregistrement, émission du passeport, admission au maillage) ; vie (délégations, vérifications par arête, traces d'exploitation, évaluations continues, migration PQC) ; mort (révocation, cascade dans la chaîne de mandat, retrait, archivage probatoire) ; trois flux de bout en bout (décision de crédit OO4 art. 12.1 outillé ; paiement ISO 20022 vers Lynx ; accès cadre bancaire sous passerelle d'outils) ; confrontation externe (cas fil rouge *loan processing* — **corpus d'appui**, cadrage et non preuve).
*Fusion : Vol. III ch. 28 (**hors §28.5 et §28.6**, prélevés par les ch. 53 et ch. 54) + Vol. II ch. 23 (flux, **scindé avec le ch. 49**) + Vol. I* Monographie *§6.8 (exemple de bout en bout : souscription vie augmentée et variante FNOL — **prélevé au ch. 6**). Socle : F-38 à F-46, F-27, F-28, F-34, F-35 ; Vol. II Annexe B §B.3-B.4. Garde-fou : **CA-8**.*

### Chapitre 51 — Instrumentation et feuille de route vers le 1ᵉʳ mai 2027

**Thèse** : les métriques d'évaluation des orchestrations (correction, réactivité, traçabilité) sont l'instrumentation candidate des programmes E-23/AMF ; la feuille de route se séquence sur l'entrée en vigueur commune (inventaire → encadrement → surveillance).
Sections : des métriques académiques aux indicateurs de risque de modèle ; feuille de route type par plateaux ; jalons externes à surveiller.
*Fusion : Vol. II ch. 20. Socle : F-09, F-25, F-37, F-44. Garde-fou : **R-7 du Vol. II** (instrumentation d'E-23 par watsonx.governance = inférence d'auteur) — à ne pas confondre avec le R-07 du Vol. III, qui porte lui aussi sur l'inférence produit ↔ réglementation : le renvoi nu était plausible dans les deux lectures, donc indécidable (décision 7).*

---

# LIVRE XII — Horizon et frontière de la connaissance vérifiable

*(fusionne Vol. I ch. 7 + §3.13.2-3.13.4 + Vol. II ch. 21/24 + Vol. III clôture ; ~20 000 mots)*

### Chapitre 52 — L'horizon 2027-2032

**Thèse** *(prospectif, sans céder à la prédiction)* : une grappe d'échéances datées (PROGRAMMÉ) structure l'horizon ; au-delà, la trajectoire des protocoles, de la gouvernance par couche, de l'identité vérifiable/PQC, de la menace et de la recherche se lit en PROJETÉ, jamais en SPÉCULATIF déguisé en certitude.
Sections : la grappe d'échéances 2027-2032 (squelette daté) ; trajectoire des protocoles (coexistence stratifiée gouvernée, souveraineté) ; bifurcation de la gouvernance par couche (AAIF, FIDO, W3C, IETF, DIF) ; identité vérifiable et PQC (l'horloge — renvoi Livre V) ; trajectoire de la menace (agentic SOC — renvoi ch. 22) ; programme de recherche (sémantique, garanties composables, science de l'évaluation) ; trajectoire macro (capacité, coût, soutenabilité, souveraineté) ; prospective d'entreprise et finance ; responsabilité, assurabilité, gouvernance de l'émergence ; scénarios 2027-2032.
*Fusion : Vol. I* Monographie *ch. 7 (**hors §7.4.2-7.4.3, prélevés par le Livre III, et hors §7.4.1/§7.4.4, prélevés par le Livre V**) + §3.13.2-3.13.4 (coexistence et souveraineté, programme de recherche sémantique, synthèse — **seule affectation du reste de §3.13**, le ch. 7 ne recevant que §3.13.1). Garde-fou : tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF systématique.*

### Chapitre 53 — La frontière de la connaissance vérifiable

**Thèse** : ce que l'on ne sait pas encore, dit honnêtement — lacunes du socle consolidé, questions ouvertes, agenda de recherche, dont le problème des deux sauts (ch. 18) et les indicateurs manquants (ch. 45).
Sections : lacunes résiduelles du socle unifié (dont PRD Vol. II §10.4, contenu de la ligne AMF ; §10.8, absence d'attaque documentée propre à A2A ; §10.9, anatomie et gouvernance d'AP2) ; questions de recherche transmises (les deux séries du Vol. II, nommées — *Monographie* ch. 16 §16.3 et ch. 21 §21.2) ; frontières de la fabrique de confiance.
*Fusion : Vol. II ch. 21 (Socle : PRD Vol. II §10, §8.3) + Vol. III §10.4, §26.3 et §28.5 (**questions transmises seules** — la mécanique du problème des deux sauts reste au ch. 18, qui reçoit les ch. 9-10 ; ici, l'énoncé de recherche qui en sort) + Vol. I* Monographie *§2.13.2 (questions ouvertes : horizon long, fiabilité, sécurité, apprentissage continu). Regroupe en un seul lieu les lacunes des trois volumes.*

### Chapitre 54 — Péremption et protocole de revalidation

**Thèse** : le compendium est daté et le dit — événements qui le périment, protocole de revalidation, conditions de gel des chapitres périssables.
Sections : événements de péremption (désignation du standard technique par arrêté, lancement effectif du RTR, révisions de MCP et d'A2A — la couche protocolaire entière du Livre II se périme au rythme de ses deux spécifications, non de la seule première —, normalisation du passeport, stabilisation OTel, premier incident public d'identité agentique, jalons PQC 2030/2035, entrées en vigueur du 1ᵉʳ mai 2027) ; protocole de revalidation ; registre de gel par chapitre.
*Fusion : Vol. II ch. 24 + Vol. III §28.6. Garde-fous : R-4, R-5 et R-6 du Vol. II et réserve F-29 (balayés ensemble à chaque revalidation). Clôt l'ouvrage par la discipline évidentiaire du Vol. II.*

---

## Annexes *(~35 000 mots, dont l'ADS Boréalis et la bibliographie consolidée)*

- **Annexe A — Méthode unifiée** : la fusion des trois systèmes de preuve en un seul — niveaux [A]/[B]/[C] (Vol. II), tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF (Vol. I), vote adversarial multi-juges, attribution des métriques auto-déclarées, distinction lien documenté/inférence. Table de correspondance des trois méthodes d'origine. Porte aussi ce que la v0.2 laissait hors méthode : la convention de qualification cryptographique (R-02 du Vol. III), l'échelle des trois degrés d'absence (R-14), la commande de décompte de référence, la règle d'escalade et les **motifs de balayage** propres à la somme — un critère d'acceptation sans motif qui le contrôle n'est pas vérifiable. *Fusion : Vol. II Annexe A (méthodologie de constitution du socle) + **Vol. III Annexe A** (méthodologie, dont PRD Annexe A §A.6 pour les motifs) + méthode déclarée du Vol. I.*
- **Annexe B — Socle factuel consolidé** : refonte de F-01…F-48 + F-23b (Vol. II) enrichie des faits datés du Vol. I et des repérages [C] du Vol. III, sous une numérotation unique. *La refonte du socle est la tâche technique centrale du compendium — sans elle, les renvois F-xx des trois volumes ne résolvent pas. Livrable inclus : table de correspondance ancienne numérotation → numérotation unique. ⚠ Le Vol. II n'attribue pas F-12 à F-14 : la renumérotation ne doit pas combler ce trou en décalant les suivants sans table. ⚠ **La renumérotation ne vise que les F-xx.** Le Vol. III pose que ses identifiants ne sont **jamais** renumérotés (PRD §7.1) parce qu'ils vivent en références croisées — les R-xx, CA-xx, L-xx et H-xx des deux volumes sont donc **cités tels quels, préfixés de leur volume** (décision 7), jamais fondus dans une série unique. Les quatorze garde-fous R-01…R-14 du Vol. III, absents de la v0.2, entrent ici au même titre que les R-1…R-8 du Vol. II.*
- **Annexe C — Faits partagés, divergences tranchées et lacunes ouvertes** *(⚠ **réouverture d'une décision prise**, non résorption d'un fichier pendant : le Vol. III a décidé de **ne pas** créer `commun/faits-partages.md`, ses divergences vivant au PRD §7.5 — décision qu'il autorise expressément le Vol. IV à rouvrir s'il entre en rédaction. C'est ce que fait cette annexe, et il faut l'écrire ainsi)* : source unique des faits datés cités par plusieurs livres, et **résolution des deux divergences héritées** — (1) date de finalisation de la ligne directrice IA de l'AMF : **30 mars 2026** (position du Vol. II, la plus récente) ; (2) gouvernance d'AP2 : **aucun transfert documenté** à date de gel. Toute réouverture exige une source primaire nouvelle datée. ⚠ **Une divergence tranchée n'est pas une lacune comblée** : l'annexe tient un registre distinct des absences héritées (contenu de la ligne AMF, PRD Vol. II §10.4 ; anatomie et gouvernance d'AP2, §10.9e ; attaques propres à A2A, §10.8), avec la règle du Vol. II en toutes lettres — *aucune de ces absences n'établit un fait négatif*. Trois entrées seulement sont des faits négatifs vérifiés par balayage documenté (F-09, F-35, F-46).
- **Annexe D — Chronologie fusionnée 2023-2032** : frise unique intégrant la trajectoire protocolaire (F-01…F-05, F-43), réglementaire et d'interopérabilité financière (F-09…F-35), et les jalons PQC — quatre statuts (annoncé / visé / attendu / incertain), **appliqués à chaque entrée sans exception**, y compris aux jalons NIST du ch. 23. *Fusion : Vol. II Annexe C (chronologie réglementaire 2023-2027, 37 événements) + **Vol. III Annexe C** (chronologie 2024-2030), étendues à l'horizon 2032.*
- **Annexe E — Glossaire bilingue unifié** : terminologie français/anglais des trois volumes, avec statut épistémique de chaque terme (norme / marché / construction d'auteur), les quatre branches de **R-8 du Vol. II** (« agentic control plane ») et les six emplois de **R-04 du Vol. III** (« agent mesh »), dont la branche (f) a été ouverte à cause de ce fichier. Fusionne les glossaires des trois sources ; déduplique les entrées. *Fusion : Vol. II Annexe D, dont **§D.1 et §D.7 font autorité** sur R-8 et sur les termes proscrits — cette autorité est reconduite, non réinterprétée — + **Vol. III Annexe D**.*
- **Annexe F — Matrice des mécanismes** : les mécanismes des Livres II-IV et les composants de maillage/exploitation (Livres IX-X) croisés avec la grille des cinq questions, l'état PQC et la couverture d'observabilité — la table de référence de l'ouvrage. *Fusion : **Vol. III Annexe B**, dont cette annexe est le prolongement. ⚠ **Partage à tenir** : le ch. 46 en tire la lecture croisée protocoles × exigences réglementaires ; l'annexe porte la table complète. La v0.2 les revendiquait toutes deux sans arbitrer — une matrice recopiée en deux endroits diverge à la première correction.*
- **Annexe G — Catalogue de patrons de la confiance agentique** : émission, vérification, révocation, chaîne de mandat, points d'application du maillage, boucles d'exploitation, formalisés au gabarit des patrons (contexte, problème, forces, solution, conséquences, patrons liés). *Fusion : **Vol. III Annexe E**. ⚠ **Filiation à ne pas réattribuer** : le Vol. III revendique explicitement la discipline des patrons d'Arsanjani & Bustos — **corpus d'appui**, donc suspendue à la décision P0.2 ; la filiation GoF/EIP du Vol. I est l'héritage de second rang, et devient le seul socle si P0.2 conclut au retrait. La v0.2 avait substitué le second au premier sans le dire.*
- **Annexe H — ADS Boréalis** : l'architecture détaillée de solution du Vol. I (Annexe B de sa Monographie), conservée intégralement comme instanciation de référence du blueprint (ch. 49-50) — inventaire produit, matrice de traçabilité, catalogue de diagrammes, configurations illustratives.
- **Annexe I — Bibliographie générale consolidée** : fusion des bibliographies par chapitre du Vol. I (son Annexe A, plans détaillés et bibliographies), du corpus de sources du Vol. II (PRD §9) et du corpus d'appui du Vol. III ; entrées dédoublonnées et datées, sources primaires distinguées de la littérature secondaire. Une somme qui se substitue à ses sources doit porter leur appareil bibliographique complet.

---

## Corrections apportées en v0.3

Trois audits de couverture, un par volume source, ont collationné chaque ligne « Fusion » contre les documents réels. Ce qu'ils ont trouvé, et ce que cette version en fait :

**Structure.** Le Livre X de la v0.2 ne comptait qu'un chapitre (études de cas) — il est absorbé par le Livre VIII, désormais « Le terrain canadien ». Le Livre III comptait onze chapitres pour un seul thème apparent : sa moitié hostile (attaques, rug-pull, SOC) devient le Livre IV. La somme des enveloppes par livre (326 000 mots en v0.2) dépassait la fourchette annoncée (260 000-320 000) : les deux sont recalculées et concordent.

**Couverture (décision 6).** Vol. I : §5.0 n'était affecté nulle part — il portait le patron directeur « autonomie graduée sous contrôle de finalité » que la thèse d'ensemble revendique ; il alimente l'avant-propos. §4.4 était couvert par une plage sans section d'accueil (ch. 28) ; §2.13.2 et §7.4.2 étaient acheminés sous une glose qui ne les décrivait pas. Vol. II : quatre pièces sur vingt-neuf — avant-propos et annexes A, C, D — n'étaient ni affectées ni coupées ; elles le sont maintenant, à l'avant-propos et aux Annexes A, D et E. La réserve F-06 (feuille de route de séquencement périmée) était tombée à la fusion ; elle revient au ch. 10.

**Gloses inexactes.** Quatre renvois décrivaient une section autrement que ce qu'elle est. Le plus conséquent : §5.14 du Vol. I, *Synthèse du chapitre et transition*, était glosé « commerce/paiements agentiques » et acheminé vers le chapitre prospectif AP2 — il rejoint le ch. 38, et le §5.13 seul va au ch. 40. Également corrigés : §2.13 (dont seule la première sous-section est la grille « quand agentifier »), §3.13 (glosé avec le titre du §7.3) et §1.9.2 (section IAM **pré-agentique**, glosée « appliqués aux agents »).

**Renvoi nommé (décision 7).** Le risque 10 de la v0.2 déclarait la convention « appliquée à ce TOC » ; elle ne l'était que sur un renvoi sur quarante et un. Tous les renvois au Vol. I nomment désormais leur document. La décision est de plus étendue aux **séries d'identifiants** : les trois renvois « Q n du Vol. II » résolvaient contre deux séries homonymes distinctes, et un lecteur ouvrant la mauvaise obtenait trois fois une autre question.

**Double affectation silencieuse.** Sept sections du Vol. I étaient revendiquées par deux chapitres sans partage déclaré (§7.3, §7.4, §2.9, §2.9.6, §2.11.1, §6.10, §6.8) ; chacune porte maintenant son partage explicite. Côté Vol. II, le ch. 22 était affecté deux fois sans mention de scission. Et le ch. 3 annonçait une économie de fusion — poser le socle IAM une seule fois — que les ch. 13 et ch. 42 défaisaient en héritant de §1.9.2 et §1.9.3 : ils y renvoient désormais sans les reprendre.

**Garde-fous mal attachés ou perdus.** R-2 et R-3 étaient cités au ch. 13, qui ne reçoit pas leur matière ; ils vont aux ch. 17 et ch. 16 — ce dernier étant le chapitre déclaré « à plus haut risque de surinterprétation » et jusqu'ici sans aucun garde-fou. Quatre garde-fous du PRD Vol. II sans identifiant R-x n'étaient pas repris : §8.2.5 (statuts pré-normatifs — la spécification CSA est un brouillon de laboratoires et le brouillon SCIM-agents a expiré le 19 avril 2026), §7.5, §8.2.1 et CA-8. Trois chapitres d'arrivée n'avaient ni socle ni garde-fous là où leur source en portait (ch. 49, ch. 53 et ch. 54).

**Faits.** La formulation « cible reportée quatre fois » (RTR) reproduisait une erreur du plan v1.5 du Vol. II que son chapitre publié corrige explicitement : 2019, 2022, 2023 et 2026 sont quatre *cibles successives*. La thèse du ch. 20 (« la majorité des attaques… sont des attaques d'identité ») n'est portée par aucun socle et le Vol. II pose une question ouverte précisément là — elle est signalée comme le premier énoncé à instruire. La lacune la plus coûteuse du Vol. II — seules les *dates* de la ligne directrice AMF sont au socle, jamais son *contenu* — n'était signalée nulle part ; elle l'est aux ch. 31 et ch. 33 et à l'Annexe C.

**Statut épistémique.** L'Annexe C rangeait sous « divergences tranchées » ce que le Vol. II tient pour des lacunes ouvertes. Une divergence arbitrée et une absence de documentation ne sont pas le même objet : l'annexe tient désormais les deux registres, avec la règle du Vol. II en toutes lettres — *aucune de ces absences n'établit un fait négatif*.

**Corpus d'appui — le constat le plus lourd.** La v0.2 écrivait « le compendium hérite de ce corpus et de ses réserves » et bâtissait six chapitres et une annexe dessus. Or les trois ouvrages sont **introuvables au dépôt** et n'y ont jamais figuré (vérification du 18 juillet 2026, lacune L-15 déclarée bloquante, décision P0.2 en attente dont une issue est le retrait de la filiation livresque). Le bloc porte désormais ce statut en tête, la liste des chapitres consommateurs est complétée (ch. 49 et Annexe G manquaient), la réserve « deux ouvrages d'auteurs Google Cloud » — que le Vol. III a relevée comme incohérence en visant nommément ce fichier — est ramenée au seul ouvrage qui la porte, et deux réserves perdues sont rétablies.

**Appareil du Vol. III.** Ses quatorze garde-fous R-01…R-14 avaient purement disparu de la v0.2, qui n'employait que la série R-1…R-8 du Vol. II — au point que les « R-5, R-6, R-7, R-8 » du blueprint et le « R-7 » de l'instrumentation devenaient indécidables dans des chapitres consommant les deux volumes. Quatre de ces garde-fous sont maintenant appliqués là où ils manquaient : R-02 (qualification par ce que la spécification démontre) et R-14 (les trois degrés d'absence) entrent à la méthode ; R-11 corrige les jalons NIST (« visée », et le statut du document) ; R-13 interdit « l'autonomie graduée » nue, le Vol. I portant trois échelles ; R-04 branche (f) impose la désambiguïsation d'« AgentMesh » — branche ouverte, précisément, à cause de ce fichier. L'Annexe B acte de plus que les identifiants R/CA/L/H ne se renumérotent **jamais**, contrairement aux F-xx.

**Sections du Vol. III sans destination.** Sept étaient perdues sans mention de coupe : §9.3 (limite de l'analogie du mandat) va au ch. 18 ; §19.3 au ch. 29 ; la moitié AMF de §19.1 au ch. 31 ; le volet RGPD du ch. 20 au ch. 34 ; §18.2 (méthode d'inventaire) au ch. 24 ; §6.3 (risque de standard de fait) au ch. 16 ; §7.4 (ce qui n'existe toujours pas) au ch. 17. Ses annexes A, C, D et E, jamais citées, sont rattachées aux Annexes A, D, E et G. Deux doubles affectations sont arbitrées : Entra Agent ID (ch. 13 pour l'extension des RFC, ch. 16 pour l'annuaire) et la matrice des mécanismes (ch. 46 pour la lecture croisée, Annexe F pour la table).

**Deux reproches périmés.** La v0.2 faisait de l'arborescence README une précondition à la fusion : le Vol. III a vérifié qu'elle est correcte, le reproche est retiré. Et elle présentait `commun/faits-partages.md` comme « à créer » alors que la décision de ne pas le créer était prise — l'Annexe C la rouvre, ce qui est permis, à condition de le dire.

**Périmètre — trois fronts identifiés puis écartés, délibérément.** L'audit a relevé un angle mort commun aux trois volumes : ils traitent l'agent comme un *interlocuteur* — qui parle à quoi, sous quelle autorité — et rarement comme un *livrable logiciel qui produit des effets*. Trois sujets en découlent, qu'aucun des trois volumes ne porte : la **provenance des composants** dont un agent est fait (serveurs d'outils, poids de modèle, bibliothèques ; nomenclatures logicielles et d'IA, signature d'artefacts) ; la **sémantique d'effet** d'une action d'agent (idempotence, compensation, réconciliation — ce qui advient quand un virement réussit à moitié) ; la **mise en service** d'un artefact au comportement non reproductible (jeux d'essai de référence, barrière d'évaluation, versionnement à quatre horloges). Une version intermédiaire de ce plan en faisait trois chapitres. **Ils sont retirés sur décision d'auteur** : la somme est une refonte de trois volumes, non une thèse nouvelle, et ces trois fronts n'ont aucun socle hérité — les instruire aurait obligé à constituer des sources primaires dans les domaines où la littérature est la plus jeune, tout en alourdissant l'ouvrage de 14 000 mots contre le risque 1. Ils sont consignés ici pour qu'un futur éditeur les retrouve comme un **choix de périmètre**, et non comme une lacune passée inaperçue. *Si ce choix est rouvert, l'ordre d'instruction suggéré — construction d'auteur, à re-vérifier à la réouverture — suit la maturité de la littérature au moment du gel : la provenance des composants d'abord (nomenclatures logicielles et d'IA, signature d'artefacts — le front où normes et outillage ont le plus progressé), la mise en service ensuite, la sémantique d'effet enfin.* Les enrichissements de moindre ampleur issus du même audit sont, eux, conservés à l'intérieur de chapitres existants : le biais d'automatisation et le paradoxe de l'explicabilité au ch. 18, les indicateurs de supervision humaine au ch. 45, la capacité d'inférence et le budget de latence au ch. 28.

---

## Corrections apportées en v0.4

Passe de cohérence interne sur le fichier v0.3, pilotée par contrôle : chaque défaut a d'abord été couvert par un contrôle exécutable qui échoue sur le document fautif, puis corrigé, puis le contrôle a été validé par mutation.

**Garde-fous nus dans des chapitres mixtes — la parade du risque 10 était incomplète.** La v0.3 déclarait la décision 7 « appliquée aux garde-fous des chapitres mixtes » ; quatre chapitres consommant le Vol. III citaient pourtant encore un R-N à un chiffre sans nommer son volume : ch. 16 (« R-3 », dans le chapitre déclaré à plus haut risque de surinterprétation), ch. 34 (« R-5 »), ch. 41 (« R-8 », le cas le plus indécidable — chapitre dont la seule source non-Vol. I est le Vol. III, où un lecteur résout naturellement « R-8 » contre R-08) et ch. 54 (« R-4, R-5, R-6 »). Les quatre sont nommés « du Vol. II » ; au ch. 41, la répartition est explicitée (R-8 du Vol. II pour « control plane », R-04 du Vol. III branche (f) pour « AgentMesh », déjà imposée en tête de livre). Le contrôle 11 de `check-toc.py` couvre désormais la classe entière : tout R-N à un chiffre sans « Vol. II » à portée de phrase, dans un chapitre dont le corps touche le Vol. III, échoue.

**« Refonte pure » qualifiée.** L'en-tête v0.3 affirmait « aucun contenu neuf n'y est introduit » alors que son propre journal consigne quatre enrichissements intra-chapitres issus de l'audit — dont le biais d'automatisation au ch. 18, déclaré « front neuf — aucun des trois volumes ne le porte, sources primaires à établir ». Les deux énoncés ne peuvent être vrais ensemble ; c'est le premier qui cède, et l'en-tête v0.4 porte la qualification.

**Discipline épistémique au titre.** Le ch. 37 s'intitulait « RTR imminent » alors que son propre corps impose « visé au T4 2026 », attribue la cible et rappelle quatre cibles successives ; « imminent » affirmait au titre ce que le chapitre s'interdit d'affirmer au texte. Titre aligné : « RTR visé ».

**Péremption protocolaire complétée.** Les événements de péremption du ch. 54 citaient les révisions de MCP mais pas celles d'A2A, alors que le Livre II repose sur les deux spécifications (A2A v1.0 au ch. 8, fusion d'ACP au ch. 10 — le plus haut risque R-1 du Vol. II). A2A entre dans la liste.

**Périmètre.** Les trois fronts écartés (provenance des composants, sémantique d'effet, mise en service) reçoivent un ordre d'instruction suggéré pour une réouverture éventuelle, marqué construction d'auteur et daté du gel.

**Forme.** Deux défauts : renvoi mal fermé au ch. 43 (« pont vers E-23 ch. 29, ) ») ; virgule manquante à l'Annexe E après « (norme / marché / construction d'auteur) ».

**Non traité, à dessein.** Le dernier commit du dépôt touchant ce fichier s'intitule « TOC v0.4 » alors qu'il livrait la v0.3 — le fichier fait foi ; la présente version est la v0.4 réelle et l'écart est consigné ici plutôt que réécrit dans l'historique Git. La thèse du ch. 20 reste volontairement en forme forte avec son avertissement d'instruction : c'est un dispositif délibéré de la v0.3, non un défaut.

---

## Risques de cadrage propres au compendium

1. **Explosion volumétrique et non-lecture** : une somme de 300 000-326 000 mots est un ouvrage de référence, pas un ouvrage de lecture linéaire. Parade obligatoire : parcours différenciés annoncés (les « contrats de lecture » des trois volumes conservés), renvois internes denses, et l'Annexe F comme table de navigation. Sans cela, le compendium est moins utile que les trois volumes séparés — ce qui invaliderait sa raison d'être.
2. **Déduplication infidèle** : fusionner deux traitements d'un même sujet (ex. identité au ch. 3 vs Livre III ; blueprint Boréalis vs IBM au ch. 49) risque d'effacer une nuance que la séparation préservait. Parade : la ligne « Fusion » de chaque chapitre trace la décision ; toute coupe de contenu est un acte documenté, pas un silence.
3. **Péremption à trois horloges** : les trois gels (juin 2026, 16-17 juillet 2026, proposition Vol. III) ne sont pas synchrones ; un fait vrai au gel du Vol. I peut être faux au gel du Vol. III. Parade : gel unique de l'ouvrage + re-datation systématique de tout fait périssable au socle consolidé (Annexe B), avant toute rédaction.
4. **Socle à refondre, pas à concaténer** : accoler F-01…F-48 (Vol. II), les faits du Vol. I et les repérages [C] du Vol. III produit des collisions d'identifiants et des doublons. Parade : renumérotation unique et dédoublonnage du socle (Annexe B) comme préalable technique — c'est le chemin critique du projet.
5. **Divergences rouvertes par inadvertance — et lacunes fermées par inadvertance** : les deux divergences sont tranchées à l'Annexe C, mais un chapitre repris d'un volume qui portait l'autre position peut les rouvrir silencieusement ; symétriquement, une lacune déclarée peut se refermer sans preuve du seul fait d'être rangée sous « tranché ». Parade : audit de cohérence sur les deux faits (date AMF, gouvernance AP2) à chaque gel de chapitre, et registre distinct des lacunes à l'Annexe C.
6. **Perte de la thèse dans la masse** : trois thèses partielles fondues risquent de diluer la thèse unifiante (le problème d'ingénierie continu). Parade : chaque livre rappelle en ouverture sa place dans les trois plans (coopérer / encadrer / faire confiance) ; tout contenu sans rattachement à l'un des trois est hors périmètre.
7. **Statut du compendium vs volumes sources** : tant que la somme n'est pas rédigée, ce sont les trois volumes qui font foi ; publier un compendium partiel créerait une quatrième source de vérité concurrente des trois autres. Parade : le compendium ne se substitue aux volumes qu'à sa complétion ; jusque-là, il est un plan, et le dit (Statut, en-tête).
8. **Hygiène de dépôt héritée — dont deux reproches périmés que la v0.2 propageait** : la v0.2 reprenait tel quel le risque d'hygiène du Vol. III, alors que son PRD en avait déjà réglé deux volets. (i) *Arborescence README désynchronisée* : **reproche retiré** — vérification du Vol. III, zéro occurrence des chemins fautifs dans le README et le CLAUDE.md racine, le bloc d'arborescence reproduit les dossiers réels ; en faire une précondition à la fusion, comme le faisait la v0.2, retardait le projet sur un défaut inexistant. (ii) *`commun/faits-partages.md` à créer* : la décision de **ne pas** le créer a été prise ; l'Annexe C rouvre cette décision, ce qui est permis, mais doit se dire ainsi (voir Annexe C). Reste vrai et non résolu : la numérotation multiple du Vol. I (risque 10) et la réécriture du README racine, qui décrit encore un triptyque et ignore la somme.
9. **Corpus d'appui hérité sans re-déclaration — aggravé : le corpus lui-même est introuvable** : le Vol. III adossait sept sections et son Annexe E à trois ouvrages de littérature secondaire ; la vérification du 18 juillet 2026 établit qu'**aucun des trois n'est au dépôt et qu'aucun n'y a jamais été** (lacune L-15, bloquante ; décision d'auteur P0.2 non prise). Le risque n'est donc plus seulement de transformer du cadrage [C] en preuve : c'est de bâtir six chapitres et une annexe sur des sources que personne n'a lues. Parades : le bloc « Corpus d'appui » porte le statut bloquant en tête ; les chapitres consommateurs portent la mention « corpus d'appui » — contrôlée par `check-toc.py`, qui a trouvé deux chapitres déclarés consommateurs sans la porter, et dont la liste omettait le ch. 49 et l'Annexe G ; **P0.2 doit être tranchée avant la rédaction de ces sept emplacements**, et son issue « retrait de la filiation livresque » est prévue (l'Annexe G retombe alors sur GoF/EIP, le ch. 47 sur la grille des cinq questions).
10. **Ambiguïté des renvois non nommés** : le Vol. I vit en numérotation **triple** — *Monographie* §1-§7, *Synthèse* **§1-§12** et Annexe B §0-§17 —, les §8.x/§10.x du Vol. II existent dans sa Monographie comme dans son PRD, le Vol. II porte deux séries « Q n » homonymes, et les deux volumes numérotent leurs garde-fous différemment (R-1…R-8 contre R-01…R-14). Un renvoi nu peut résoudre contre le mauvais document, la mauvaise série ou le mauvais volume. Parade : décision structurante (7), **appliquée en v0.3 aux quarante et un renvois du Vol. I, aux trois renvois de série et aux garde-fous des chapitres mixtes** (la v0.2 la déclarait appliquée alors qu'un seul renvoi la respectait — et la décrivait elle-même en s'appuyant sur un intervalle faux, « Synthèse §3-§12 », répété quatre fois).
