# Conspectus — La somme agentique

## Interopérabilité, autonomie encadrée et fabrique de confiance : déployer des agents en services financiers réglementés (2024-2032)

| Champ | Valeur |
|---|---|
| Nature | **Conspectus** : vue synoptique du compendium intégral (Vol. IV) — l'argument de l'ouvrage, livre par livre, en lecture continue. Ce document ne porte aucune décision de fusion, aucun socle, aucun garde-fou nouveau : tout ce qu'il énonce est tenu par le [`TOC.md`](TOC.md), qui seul fait autorité |
| Source | [`TOC.md`](TOC.md) **v0.14** (23 juillet 2026) — 57 chapitres en 10 livres, avant-propos, 9 annexes, ≈ 369 000–394 000 mots projetés. Les v0.10 et v0.11 n'ajoutent aucune structure : la v0.10 porte huit relèves datées sur la **couche d'exécution** et déclare l'angle mort correspondant (risque 14 du TOC) ; la v0.11 porte six relèves datées sur **l'après-agentique**, relevées sur arXiv exclusivement — les deux sont reprises en fin de ce document. La v0.12 est une passe d'appareil (reconstruction de `check-toc.py`, validé par mutation) ; la **v0.13** met la filiation à jour sur constats de dépôt — **le Vol. III est rédigé** (34 pièces, socle F-01…F-98, gel du 21 juillet 2026, « rédigé ne vaut pas publiable ») et **la décision P0.2 est tranchée** (filiation livresque retirée, réversible) — sans toucher à la structure ; la **v0.14** collationne la carte des chapitres du plan contre les trois monographies rédigées — couverture complète des 7 + 24 + 28 chapitres sources, onze renvois de section au Vol. III résolus contre le texte rédigé —, la collation de fond restant réservée (porte G-4) |
| Date | 23 juillet 2026 |
| Statut | Le compendium **n'est pas rédigé** : tant qu'il ne l'est pas, les trois volumes sources font foi, et ce conspectus décrit un *plan*, non un ouvrage. En cas d'écart entre ce document et le `TOC.md`, **c'est le `TOC.md` qui prime** ; un conspectus n'est pas une source, pas plus qu'une thèse de plan n'est une entrée de socle (décision 8 du TOC) |
| Régénération | À chaque nouvelle version du `TOC.md`, ce document se réaligne ou déclare son retard en tête |

---

## L'objet et la thèse

Déployer des agents non humains qui engagent la responsabilité d'une institution financière réglementée est **un seul problème d'ingénierie continu** — non trois. Les trois volumes sources le prouvaient chacun à demi : le Vol. I posait la théorie de l'interopérabilité mais s'arrêtait au seuil du droit applicable ; le Vol. II instruisait le droit canadien mais présupposait la théorie ; le Vol. III isolait le verrou commun — l'identité — mais le traitait comme un ouvrage à part. La somme tient les trois ensemble, sur quatre plans qui sont des coupes du même objet :

1. **Coopérer** — l'interopérabilité : protocoles, sémantique, maillage (Livres I et II, et le premier mouvement du Livre VII) ;
2. **Encadrer** — l'autonomie sous contrôle de finalité que la réglementation impose : orchestration déterministe, frames normatifs (Livres IV, V et VI) ;
3. **Faire confiance** — ce que la coopération encadrée présuppose sans jamais le produire : identité non humaine, délégation vérifiable, exploitation dans la durée (Livre III, et le second mouvement du Livre VII) ;
4. **Livrer** *(quatrième plan, ajout v0.8 — matière neuve sans socle hérité, déclarée telle)* — l'agent comme artefact logiciel qui se compose, se met en service et produit des effets (Livre IX).

Le tout est tendu par une horloge datée : convergence protocolaire (2024-2026), entrées en vigueur réglementaires canadiennes (1ᵉʳ mai 2027), jalons post-quantiques du NIST (dépréciation **visée** 2030, retrait **visé** 2035).

Deux armatures héritées structurent l'ensemble. **L'invariant à quatre termes** du Vol. I — découplage, contrat, évolution, *exploitation* — traverse l'ouvrage : posé à l'avant-propos, éprouvé au ch. 1, appliqué à la couche cryptographique au ch. 24 (trois premiers termes), refermé au Livre VII (le quatrième). **Les trois capacités** du Vol. III — *émettre* une identité opposable, l'*appliquer* là où elle est vérifiée, *exploiter* le comportement dans la durée — structurent le Livre III (émettre, avec ses versants hostile et post-quantique) et le Livre VII (appliquer, exploiter) ; tout contenu de maillage ou d'exploitation sans lien à l'identité ou à la délégation est hors périmètre.

---

## Parcours de l'ouvrage

### Avant-propos et note méthodologique unifiée

Pose la définition de travail (l'**agent d'entreprise** : système non humain à qui une organisation délègue des tâches engageant sa responsabilité), le patron directeur « autonomie graduée sous contrôle de finalité » avec ses quatre durcisseurs financiers, les deux armatures, et la méthode unifiée : socle factuel daté et cité, niveaux de preuve [A]/[B]/[C], tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF, attribution systématique des métriques auto-déclarées, distinction lien documenté / inférence d'auteur.

### Livre I — Fondements : interopérabilité et ingénierie agentique *(ch. 1-6)*

Le socle pré-agentique, posé une seule fois. L'interopérabilité comme propriété à maintenir dans le temps et problème économique avant d'être technique (ch. 1) ; l'accord sur le sens que les protocoles présupposent sans savoir l'établir (ch. 2) ; l'héritage IAM et zero-trust — identité fédérée, OAuth/OIDC, SPIFFE/SPIRE — que la fabrique de confiance étirera jusqu'à rupture (ch. 3, chapitre-charnière auquel les Livres III et VII renvoient sans le reconstruire). Puis l'ingénierie agentique proprement dite : l'agent comme LLM augmenté d'une boucle perception-raisonnement-action-observation (ch. 4) ; l'ancrage informationnel — mémoire, contexte, RAG gouverné (ch. 5) ; le multi-agent, son surcoût, son évaluation et sa sûreté (ch. 6).

### Livre II — Couche protocolaire agentique *(ch. 7-11)*

En dix-sept mois, la couche protocolaire s'est consolidée sous gouvernance neutre — condition **nécessaire et non suffisante** de sa crédibilité en entreprise réglementée (ch. 7). Anatomie des deux spécifications maîtresses : MCP côté agent-outil, A2A côté agent-agent — « MCP dans les agents, A2A entre les agents », doctrine déclarée par le projet A2A, non un accord des deux (ch. 8) ; ⚠ la révision MCP dont la ratification est **annoncée** pour le 28 juillet 2026 (cœur sans état, extensions, politique de dépréciation) périmera cette anatomie et donne au Livre II sa première échéance de péremption datée. Suivent la découverte, les registres et la portabilité (ch. 9) ; AP2 et AGNTCY, deux objets aux statuts inégaux — lecture d'auteur pour la centralité financière d'AP2, positionnement déclaré pour AGNTCY (ch. 10 ; le don d'AP2 à la FIDO Alliance, annoncé en avril 2026, reste **à instruire à la source primaire**) ; et les modes d'échec protocolaires, nommés par les protocoles mais ni datés ni outillés au socle (ch. 11).

### Livre III — Identité, délégation et fabrique de confiance *(ch. 12-24)* — capacité : **émettre**, avec ses versants hostile et post-quantique

Le cœur doctrinal du plan « confiance ». L'identité machine précède l'agent : un demi-siècle de comptes de service et de clés mal gouvernés (ch. 12) ; la première vague agentique étire les RFC existantes — OAuth, OIDC, SCIM — et chaque extension révèle l'hypothèse d'un humain au bout du flux (ch. 13) ; le corpus W3C (VC, DID) fournit le vocabulaire du portable, l'adoption financière restant à démontrer (ch. 14). La **grille des cinq questions** — *qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond* — devient l'instrument de lecture de tout mécanisme d'identité : aucun n'y répond en entier en 2026 (ch. 15). Sur cette grille : l'émission (Agent Card signée, annuaires commerciaux, registres gouvernés — ch. 16, chapitre déclaré à plus haut risque de surinterprétation) ; le **passeport d'agent**, objet de synthèse qui n'existe dans aucune spécification — normalisation 2027-2028 en statut PROJETÉ (ch. 17) ; la **chaîne de mandat** et le problème des deux sauts — les mécanismes prouvent qu'un agent *a* une identité, presque aucun *au nom de qui* il agit (ch. 18) ; et le KYA, transposition du KYC sans l'infrastructure institutionnelle qui rend le KYC possible (ch. 19).

**Le versant hostile (ch. 20-22).** Le versant adverse. Une taxonomie des attaques d'identité et de délégation — dont la thèse quantitative (« une part majoritaire ») est **à instruire par dénombrement avant rédaction**, le socle hérité ne portant aucune attaque documentée propre à A2A (ch. 20) ; l'asymétrie émission soignée / révocation négligée, qui rejoue l'histoire des PKI, et le rug-pull après admission (ch. 21) ; la défense qui s'agentifie elle-même — les agents défensifs, premiers porteurs du passeport (ch. 22).

**L'horloge post-quantique (ch. 23-24).** Toute la fabrique d'émission repose sur des signatures classiques. Les jalons du NIST IR 8547 — dépréciation **visée** 2030, retrait **visé** 2035, document au statut de brouillon — tombent dans la durée de vie des architectures conçues aujourd'hui (ch. 23) ; la crypto-agilité est l'application des trois premiers termes de l'invariant à la couche cryptographique, avec une dette de migration réelle mais non chiffrée — méthode d'estimation plutôt que chiffre, fenêtre d'action 2026-2029 (ch. 24).

### Livre IV — Autonomie encadrée : orchestration en entreprise *(ch. 25-28)*

Le plan « encadrer » commence par un choix objectivable : la taxonomie OO1-OO4 place toute architecture agentique sur un continuum d'encadrement (ch. 25) ; le paradigme APM distingue l'autonomie de l'automatisation et la gouverne par frames normatifs et opérationnels (ch. 26) ; l'offre s'est industrialisée en 2025-2026, avec un support protocolaire répandu mais inégalement établi (ch. 27) ; le passage à l'échelle intègre les agents au tissu existant — sans dupliquer l'IAM ni l'observabilité en place (ch. 28).

### Livre V — Cadre réglementaire canadien *(ch. 29-34)*

E-23 couvre l'IA agentique *par inférence*, via sa définition de « modèle », avec échéance au 1ᵉʳ mai 2027 — et ses attentes s'écrivent « **attendues** », jamais « exigées » (ch. 29). La mort de la LIAD laisse un vide fédéral que C-36 ne comble pas (ch. 30). Le Québec porte le cadre le plus explicite : ligne directrice IA de l'AMF (finale le 30 mars 2026, en vigueur le 1ᵉʳ mai 2027 — seules ses *dates* sont au socle, jamais son *contenu*) et l'article 12.1 de la Loi 25, en friction directe avec la décision agentique autonome (ch. 31). Les ACVM confirment que les lois existantes s'appliquent (ch. 32). Le **pont** — chapitre-pivot — traduit les exigences canadiennes en frames déterministes d'architecture (ch. 33) ; le maillage international (AI Act, ISO 42001, RGPD) et la normalisation institutionnelle ferment le tour (ch. 34).

### Livre VI — Terrain canadien : interopérabilité financière et adoption *(ch. 35-40)*

Le vertical financier durcit l'agentique par des contraintes qui préexistent à l'agent (ch. 35). Le cadre des services bancaires axés sur le consommateur est légiféré, supervisé, réglementairement en cours — et son standard technique n'est **pas** désigné, fait négatif vérifié (ch. 36). La couche sémantique des paiements est en place : Lynx accompli, RTR **visé** au T4 2026 — quatre cibles successives, à attribuer, jamais à affirmer au futur catégorique (ch. 37). Suivent les sous-domaines — banque, assurance, patrimoine (ch. 38) ; les études de cas de la production agentique canadienne 2025-2026, documentées par sources primaires et inégalement documentables (ch. 39) ; et la prospective AP2 sur les rails canadiens — chapitre explicitement prospectif : aucune source ne documente l'articulation, le chapitre pose les conditions de possibilité sans affirmer (ch. 40).

### Livre VII — AgentMesh et AgentOps *(ch. 41-45)* — capacités : **appliquer et exploiter**

« AgentMesh » désigne ici le **patron d'infrastructure** — plan de données médiatisant chaque arête, plan de contrôle centralisant la politique — et rien d'autre (désambiguïsation imposée en tête de livre). Généalogie et anatomie : le maillage d'agents comme réinstanciation du *service mesh*, filiation qui trie le réel du marketing (ch. 41) ; puis le maillage comme lieu où le passeport devient opposable — PEP/PDP, zero trust transposé au graphe d'agents, jamais de confiance héritée de la topologie (ch. 42). Le maillage est à l'identité ce que le tribunal est à la loi.

**L'exploitation (ch. 43-45).** Le quatrième terme de l'invariant, refermé. L'observabilité agentique repose sur des conventions OpenTelemetry encore au statut *Development* à la mi-2026 — et tracer un *appel* n'est pas tracer une *délégation* : la corrélation trace ↔ chaîne de mandat est le chaînon manquant (ch. 43). Le cycle de vie opérationnel — évaluer, détecter la dérive, répondre à l'incident, réviser le mandat — est la boucle sans laquelle le passeport certifie un comportement passé, jamais courant (ch. 44). La discipline n'a pas ses indicateurs de référence : grille minimale en construction d'auteur, FinOps des agents comme contrainte de premier ordre (ch. 45).

### Livre VIII — Synthèse architecturale et blueprint *(ch. 46-51)*

La composition. La matrice protocoles × exigences réglementaires révèle où les standards suffisent et où l'architecture compense — quinze croisements sans lien documenté à date (ch. 46). L'architecture de référence unifiée étage protocoles, identité/registre, orchestration, maillage, exploitation et gouvernance, structurée par OO1-OO4 (ch. 47). La formalisation ArchiMate affronte son verrou : **aucun élément natif** pour les concepts agentiques, seule extension défendable Specialization + stéréotype + Profiles — version de référence ArchiMate 4 (C260), dont la refonte du métamodèle impose une re-vérification préalable (ch. 48). Le blueprint s'instancie deux fois — ADS Boréalis (Vol. I) et portefeuille IBM (Vol. II), présentés comme deux réalisations d'une même architecture de référence (ch. 49) — puis se prouve par le parcours : naissance, vie et mort d'un agent d'entreprise, trois flux financiers de bout en bout (ch. 50). L'instrumentation et la feuille de route se séquencent sur le 1ᵉʳ mai 2027 (ch. 51).

### Livre IX — L'agent comme livrable logiciel *(ch. 52-54)* — plan : **livrer** ⚠ matière neuve

Seul livre sans volume source ni socle hérité — statut déclaré en tête de livre, rédaction en dernier, retrait prévu si le socle ne se constitue pas (décision 9, risque 13 du TOC). Les trois volumes traitent l'agent comme un *interlocuteur* ; ce livre le traite comme un *artefact*. La provenance des composants — nomenclatures logicielles et d'IA, signature d'artefacts — comme chaînon entre passeport et intégrité, front le plus mûr des trois (ch. 52) ; la mise en service d'un artefact non reproductible — jeux d'essai de référence, barrière d'évaluation, versionnement à quatre horloges (ch. 53) ; la sémantique d'effet — idempotence, compensation, réconciliation : ce qui advient quand un virement réussit à moitié, silence maximal en finance (ch. 54).

### Livre X — Horizon et frontière de la connaissance vérifiable *(ch. 55-57)*

La clôture. L'horizon 2027-2032 : une grappe d'échéances datées en PROGRAMMÉ, des trajectoires en PROJETÉ, jamais de SPÉCULATIF déguisé en certitude (ch. 55). La frontière : ce que l'on ne sait pas encore, dit honnêtement — les onze lacunes héritées du PRD du Vol. II reprises par identifiant, les questions de recherche transmises, le problème des deux sauts (ch. 56). Enfin la péremption : le compendium est daté et le dit — événements qui le périment (dont la ratification MCP annoncée au 28 juillet 2026, première à porter une date), protocole de revalidation, registre de gel par chapitre (ch. 57).

---

## Appareil

Neuf annexes ferment l'ouvrage : **A** — méthode unifiée (fusion des trois systèmes de preuve) ; **B** — socle factuel consolidé sous numérotation unique (la tâche technique centrale : sans elle, les renvois F-xx ne résolvent pas) ; **C** — faits partagés, divergences tranchées et registre des onze lacunes héritées ; **D** — chronologie fusionnée 2023-2032 à quatre statuts (annoncé / visé / attendu / incertain) ; **E** — glossaire bilingue avec statut épistémique de chaque terme ; **F** — matrice des mécanismes, table de navigation de l'ouvrage ; **G** — catalogue de patrons de la confiance agentique ; **H** — ADS Boréalis intégrale (20 655 mots mesurés) ; **I** — bibliographie générale consolidée (plancher mesuré : 37 104 mots et 1 270 entrées pour le seul Vol. I).

## Régimes de preuve — ce que le lecteur doit savoir tenir séparé

La somme porte **trois régimes de preuve**, et les déclare plutôt que de les lisser :

1. **Vérifié** — les livres dérivés des Vol. I et II, rédigés, adossés à un socle F-xx daté et cité ;
2. **Rédigé, non publiable** *(re-libellé v0.13 — « Planifié » jusque-là)* — les Livres III et VII (≈ 26 % du corps), dérivés du Vol. III, rédigé et doté d'un socle propre de 98 entrées depuis le 22 juillet 2026, mais que son propre cadrage déclare non publiable — remontées ouvertes, arbitrages révocables, dette de vote sur deux entrées ; la collation contre son texte rédigé est un préalable déclaré (risque 11 du TOC) ;
3. **À constituer** — le Livre IX, matière neuve sans aucun socle, même hérité (risque 13 du TOC).

## L'angle mort déclaré — la couche d'exécution *(v0.10)*

La somme décrit l'agent sur quatre plans : ce qui le fait coopérer, ce qui l'encadre, ce qui l'accrédite, ce qui le livre. Elle ne décrit nulle part le **harnais** — le programme qui héberge la boucle et porte, en propre, la persistance de session, les modes d'exécution, les sous-agents, la chaîne d'approbation d'outils, l'admission d'extensions et la compression de contexte. Ce n'est ni le protocole (un harnais est un client, pas une spécification), ni le cadriciel d'orchestration du ch. 27 (qui compose des graphes, ne tient pas une session), ni le maillage (le harnais est en deçà de l'arête). L'écart est **déclaré plutôt que comblé** : ajouter un livre à la somme avant que le Livre IX ait constitué le sien aggraverait le défaut qu'elle annonce. Huit relèves datées du 21 juillet 2026, toutes **[C] et à instruire à la source primaire**, sont rattachées à onze chapitres d'accueil (ch. 20, 21, 22, 26, 43, 44, 52, 53, 54, 55, 57) ; l'arbitrage — chapitre neuf, sections dans l'existant, ou périmètre assumé — appartient à l'auteur et se prend avant la rédaction des Livres VII et IX. Détail au risque 14 et au journal v0.10 du [`TOC.md`](TOC.md).

## L'après-agentique — quatre trajectoires relevées *(v0.11)*

La somme borne son domaine (services financiers réglementés) et son horloge (2024-2032) ; la littérature de prépublication de 2025-2026 décrit déjà ce qui déborde ce cadre, et la v0.11 le relève sans l'instruire. Six relèves du 23 juillet 2026, toutes **[C] et à instruire à la source primaire**, relevées sur arXiv exclusivement (métadonnées vérifiées à l'API du dépôt, résumés seuls consultés), sur quatre trajectoires : la généralisation de la pile en « **web agentique** », où l'interaction machine-à-machine devient le cas nominal du web (ch. 9) ; une **économie d'agents** déjà mesurable sur des rails de micropaiement et d'enregistrement sur chaîne que le plan n'instruit pas — fragile, attaquée, parallèle aux rails réglementés du ch. 40 ; l'agent **mutable**, qui prive réputation, admission et révocation de la persistance d'identité qu'elles présupposent (ch. 19) ; l'**auto-évolution**, qui fait de la dérive un comportement recherché (ch. 44). S'y ajoutent, en clôture, l'assurabilité des agents et les échelles d'autonomie au-delà de l'agentique, à tenir respectivement en PROJETÉ et en SPÉCULATIF (ch. 55). Détail au journal v0.11 du [`TOC.md`](TOC.md).

## Horloge de l'ouvrage

2024-2026 : convergence protocolaire sous fondations neutres • 28 juillet 2026 : ratification MCP **annoncée** (premier événement de péremption daté) • T4 2026 : lancement RTR **visé** • 1ᵉʳ mai 2027 : entrée en vigueur commune E-23 / ligne directrice AMF • 2027-2028 : normalisation du passeport d'agent (**PROJETÉ**) • 2030 / 2035 : dépréciation puis retrait des signatures classiques (**visés**, NIST IR 8547, brouillon).
