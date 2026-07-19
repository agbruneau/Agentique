# TOC — Table des matières commentée du Volume III

| Champ | Valeur |
|---|---|
| Version | **0.4 — révision finale de cadrage, antérieure au PRD** (18 juill. 2026 : recentrage thématique — l'**entreprise agentique** devient le cadre d'ensemble, l'identité sa fondation ; titre arrêté ; corrections de renvois après vérification contre les Vol. I-II : « §8.2.3 » → PRD Vol. II §8.2.1/§8.2.7, « plan de contrôle obligatoire » réattribué au Vol. I et « points de contrôle obligatoires » au Vol. II §19.3, numérotation §10/§11.5/tableau 15 rapportée à la *Synthèse* du Vol. I ; renvoi `commun/faits-partages.md` marqué **à créer**. Historique : v0.3 — corpus livresque, discipline des patrons (annexe E), maturité au ch. 27, HITL §9.4, agent apprenant §25.5, empoisonnement de mémoire §12.3 ; v0.2 — Parties VII (maillage) et VIII (AgentOps), blueprint en Partie IX ; v0.1 — cadrage initial) |
| Date | 18 juillet 2026 |
| Statut | Proposition — aucun socle F-xx constitué ; les « socles candidats » sont des repérages [C] à instruire |
| Filiation | Troisième panneau du triptyque : Vol. I (théorie mondiale, gel juin 2026) → Vol. II (cas canadien réglementé, gel 16-17 juillet 2026) → Vol. III (**l'entreprise agentique** : le verrou commun aux deux). Convention de renvoi : les pointeurs Vol. I §10, §11.5 et tableau 15 résolvent contre `Synthese Monographie.md` (numérotation §3-§12) ; les pointeurs §7.x contre `Monographie.md` — la double numérotation du Vol. I impose de nommer le fichier à chaque renvoi |
| Lacunes héritées instruites | Vol. II : Q2 (mécanique des attaques), Q3 (valeur cryptographique des Agent Cards), Q5 (organisme de normalisation du cadre bancaire) — jeu de questions du ch. 21 §21.2, à ne pas confondre avec l'homonyme du ch. 16 §16.3 ; ch. 8 §8.4 (« ce qui n'existe pas encore ») ; ch. 19 §19.3 (les cinq points de contrôle obligatoires) et ch. 20 (instrumentation) — prolongés au grain du maillage ; Vol. I (*Synthèse*) : tableau 15 §11.6, strate Entreprise — verrou « identité non humaine et délégation multi-saut » ; §11.5 (délégation au-delà de deux sauts, métrique d'horizon de tâche) ; §7.4 (KYA, passeport d'agent, PQC) ; §7.0.1 et §10 (l'*exploitation* comme quatrième terme de l'invariant — fondement de la Partie VIII) |

---

## Titre

# L'entreprise agentique
## La fabrique de confiance : identité non humaine, délégation vérifiable, maillage d'agents et AgentOps à l'horloge post-quantique (2026-2030)

*Justification du titre : le triptyque progresse par élargissement du sujet réel — les protocoles (Vol. I), les cadres (Vol. II), l'organisation qui doit les faire tenir ensemble (Vol. III). « L'entreprise agentique » nomme ce sujet ; « la fabrique de confiance » nomme la thèse (la confiance ne se décrète pas, elle se fabrique — émission, application, exploitation) ; le sous-titre énumère les quatre chantiers et borne l'horloge. Le « passeport d'agent » demeure l'objet-pivot (ch. 8) mais redevient ce qu'il est : une pièce de la fabrique, pas le sujet du livre.*

## Thèse d'ensemble

L'entreprise agentique — celle qui confie à des agents non humains des tâches qui engagent sa responsabilité — n'existe pas encore comme discipline : les protocoles savent faire coopérer les agents (Vol. I), les cadres savent les encadrer (Vol. II), mais l'organisation qui les déploie ne sait pas répondre à la question préalable — *qui est cet agent, pour le compte de qui agit-il, et jusqu'où sa délégation est-elle vérifiable ?* La thèse défendue : **l'entreprise agentique se construit sur une fondation identitaire, et cette fondation ne sera pas une invention mais une extension gouvernée** — les standards existants (OAuth/OIDC, SCIM, X.509, VC/DID) sont étirés jusqu'à leur point de rupture, et c'est la localisation exacte de ce point de rupture, strate par strate, qui constitue l'apport de l'ouvrage. Corollaire structurant : l'identité est la **fondation de la défense** — la majorité des attaques propres aux systèmes multi-agents sont des attaques d'identité ou de délégation, ce qui permet d'absorber la taxonomie des menaces (Q2) dans le cadre identitaire plutôt que d'en faire un ouvrage séparé. L'ensemble est tendu par une horloge datée : la migration post-quantique (jalons NIST 2030/2035), qui transforme la crypto-agilité de vertu en exigence de conception.

Trois capacités font l'entreprise agentique, et elles ordonnent l'ouvrage. La première est d'**émettre** : donner à chaque agent une identité opposable — le passeport (Parties I-III). La deuxième est d'**appliquer** : une identité ne vaut que là où elle est vérifiée, et ce lieu est le **maillage d'agents** (*agent mesh*), transposition agentique du *service mesh* qui médiatise chaque arête du graphe d'interaction (Partie VII) — le mesh est à l'identité ce que le tribunal est à la loi : l'endroit où elle devient opposable. La troisième est d'**exploiter** : une identité vérifiée à l'admission ne dit rien du comportement en exploitation, et c'est l'**AgentOps** — observabilité, évaluation continue, cycle de vie, réponse à incident (Partie VIII) — qui referme la boucle, en prolongeant le quatrième terme que le Vol. I avait ajouté à l'invariant : l'*exploitation*. Les menaces (Partie IV), l'horloge cryptographique (Partie V) et le droit (Partie VI) traversent les trois capacités ; le blueprint (Partie IX) les compose en une organisation — car l'entreprise agentique est d'abord une entreprise : des rôles, des responsabilités, une trajectoire de maturité, pas seulement une pile technique.

## Corpus d'appui (déposé au dépôt, 18 juillet 2026)

Trois ouvrages rejoignent le socle candidat comme **littérature secondaire de cadrage** — cadres conceptuels et vocabulaire, jamais sources primaires de spécification (les specs restent citées directement) :

| Ouvrage | Référence | Ce qu'il apporte à l'ouvrage | Réserve |
|---|---|---|---|
| *Agentic Architectural Patterns for Building Multi-Agent Systems* — Arsanjani & Bustos | Packt ; préface T. Kurian (Google Cloud) | La **discipline des patrons** (gabarit problème/forces/solution/conséquences) appliquée au multi-agents ; patrons d'explicabilité-conformité, de robustesse et d'interaction humain-agent ; **trois modèles de maturité** articulés (GenAI Maturity Model, Agentic AI Maturity Spectrum, Implementation Maturity Levels) ; cas fil rouge *loan processing* mono → multi-agent | Auteurs et préfacier Google Cloud — biais d'écosystème possible (A2A) ; traiter les patrons comme cadre, vérifier chaque affirmation protocolaire à la source |
| *Agentic AI for Engineers* — Nagasubramanian | Apress, 2026, ISBN 979-8-8688-2361-9 | La **progression automatisation → autonomie** comme bascule d'ingénierie ; sûreté-alignement-robustesse au niveau agent ; boucles de rétroaction ; test, débogage, évaluation et déploiement — matière directe des ch. 24-25 | Manuel généraliste ; profondeur inégale sur l'identité — mobiliser en cadrage, pas en preuve |
| *Agentic AI in Enterprise* — Ranjan, Chembachere & Lobo | Apress, 2025, ISBN 979-8-8688-1542-3 | La **préparation organisationnelle** (« making agentic AI enterprise-ready » : sécurité-vie privée comme socle de confiance, gouvernance IA et API, facteur humain et culture) ; études de cas d'adoption — matière du ch. 27 §27.5, où la thématique de l'entreprise agentique trouve son répondant livresque | Antérieur à la stabilisation protocolaire (2025) — dates et mécanismes à revalider systématiquement |

Statut épistémique commun : repérage [C] à l'entrée, élévation [B] par extraction citée chapitre par chapitre ; aucun des trois ne peut porter seul une affirmation centrale (règle du Vol. II reconduite).

## Publics visés

Architectes d'entreprise et responsables IAM/CIAM des institutions réglementées ; RSSI et équipes de sécurité offensive/défensive ; équipes plateforme, SRE et exploitation (AgentOps/MLOps) ; responsables conformité (E-23, Loi 25) ; dirigeants instruisant la trajectoire de maturité agentique de leur organisation ; chercheurs en identité décentralisée et en sécurité des systèmes multi-agents.

## Volumétrie indicative

≈ 100 000 mots — 28 chapitres en 9 parties, avant-propos, annexes A-E. Fourchette ajustable, non normative (leçon du Vol. II : un écart se documente, il ne se corrige pas par amputation).

---

## Avant-propos et note méthodologique *(~2 500 mots)*

Origine : le verrou commun des deux volumes précédents (Vol. I, *Synthèse*, tableau 15 §11.6, strate « Entreprise » ; Q3 et ch. 8 du Vol. II). Définition de travail posée d'entrée : l'**entreprise agentique** est une construction d'auteur — organisation qui délègue à des agents non humains des tâches engageant sa responsabilité, et qui en assume l'émission d'identité, l'application au maillage et l'exploitation dans la durée ; le terme circule au marché sans définition normative, et l'ouvrage le dit. Méthode reconduite : socle factuel daté, niveaux de preuve [A]/[B]/[C] (héritage Vol. II), vote adversarial sur les affirmations centrales, tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF (héritage Vol. I) pour tout énoncé prospectif. Avertissements : pas de conseil juridique ; neutralité fournisseur (Entra Agent ID et consorts traités comme cas documentés, non comme recommandations). Convention nouvelle : tout mécanisme cryptographique est qualifié par ce que sa spécification *démontre*, jamais par ce qu'elle *promet* — l'ouvrage naît de Q3, il ne peut pas reproduire la faute que Q3 dénonce.

---

## Partie I — L'héritage : l'identité machine avant l'entreprise agentique *(4 chapitres, ~11 000 mots)*

### Chapitre 1 — Un demi-siècle d'identités non humaines
**Thèse** : l'identité machine n'est pas née avec les agents — comptes de service, certificats X.509, clés d'API, secrets d'atelier logiciel forment un passif considérable et mal gouverné, et l'entreprise qui se veut agentique hérite de ce passif avant d'y ajouter le sien.
Sections : 1.1 Généalogie (comptes de service → workload identity) ; 1.2 L'écart de gouvernance NHI : ratio identités machines/humaines, prolifération des secrets ; 1.3 Pourquoi l'agent casse le modèle — l'identité stable face au comportement non déterministe.
*Socle candidat : littérature IAM d'entreprise, rapports d'éditeurs NHI (métriques à traiter en auto-déclaré), SPIFFE/SPIRE (CNCF). Garde-fou : chiffres de prolifération = illustration, jamais preuve.*

### Chapitre 2 — Les standards étirés : OAuth, OIDC, SCIM face à l'agent
**Thèse** : la première vague de l'identité agentique est une extension des RFC existantes, non une rupture — et chaque extension révèle une hypothèse implicite du standard d'origine (un humain au bout du flux) qui cesse de tenir.
Sections : 2.1 OAuth 2.x et l'agent : *client* ou *resource owner* ? ; 2.2 Les drafts IETF pertinents (délégation, transaction tokens, extensions d'identité d'agent — état exact et dates d'expiration des drafts) ; 2.3 SCIM et le provisionnement d'agents ; 2.4 Ce que les RFC ne disent pas.
*Socle candidat : RFC et drafts IETF (sources primaires datées — reprendre le repérage du ch. 8 §8.3 du Vol. II et le porter au niveau [B]).*

### Chapitre 3 — L'identité décentralisée : VC, DID et la promesse du portable
**Thèse** : le corpus W3C (Verifiable Credentials, DID) fournit le vocabulaire conceptuel du « passeport d'agent », mais son adoption en entreprise financière reste à démontrer — la distinction promesse/production est le fil du chapitre.
Sections : 3.1 VC Data Model et DID Core : ce que les recommandations établissent ; 3.2 DIF et les profils d'interopérabilité ; 3.3 Les Community Groups agentiques du W3C (signal faible identifié au Vol. I §7.3.2 — état 2026) ; 3.4 Le fossé adoption : qui vérifie quoi, en production, à date.
*Socle candidat : recommandations W3C (datées), chartes des CG. Garde-fou : une charte de groupe n'est pas un standard.*

### Chapitre 4 — Grille d'analyse : les cinq questions que l'entreprise pose à son agent
**Thèse** : cinq questions — *qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond* — forment la grille de lecture de tout mécanisme d'identité agentique ; ce sont les questions que l'entreprise doit pouvoir poser à chacun de ses agents, et aucun mécanisme de 2026 ne répond aux cinq.
Sections : 4.1 Dérivation de la grille depuis les axes du Vol. I (identité et confiance, gouvernance des frontières) ; 4.2 Application-témoin à trois mécanismes ; 4.3 La grille comme critère de structure des Parties II-IV ; 4.4 Grille et maturité : croisement des cinq questions avec le spectre de maturité agentique (Arsanjani-Bustos) — plus l'autonomie monte, plus les questions sans réponse coûtent cher, ce qui ordonne les exigences d'identité par palier de maturité plutôt qu'en absolu.
*Chapitre de méthode — grille transversale, à la manière de la matrice du ch. 18 du Vol. II. La §4.4 mobilise le corpus d'appui en cadrage ; la correspondance maturité-exigences est une construction d'auteur, marquée comme telle.*

---

## Partie II — Les mécanismes émergents : émettre l'identité *(4 chapitres, ~12 000 mots)*

### Chapitre 5 — L'Agent Card signée : anatomie et valeur probante
**Thèse** *(instruit Q3 du Vol. II)* : la signature d'une Agent Card vaut exactement ce que valent son ancrage de confiance, son régime de révocation et sa gouvernance des clés — trois éléments que la spécification A2A v1.x documente inégalement.
Sections : 5.1 Le format et la chaîne de signature ; 5.2 Ancrage : qui signe les signataires ; 5.3 Révocation et durée de vie ; 5.4 Verdict par la grille du ch. 4 — ce que la carte prouve, ce qu'elle affirme, ce qu'elle tait.
*Socle candidat : spécification A2A (source primaire), documentation de gouvernance des clés du projet. Chapitre à plus haut risque de surinterprétation — relecture adversariale prioritaire.*

### Chapitre 6 — Les annuaires d'agents commerciaux : Entra Agent ID et ses pairs
**Thèse** : la GA d'Entra Agent ID fait exister l'identité d'agent gérée en production avant tout standard — précédent qui structure le marché et préempte partiellement la normalisation.
Sections : 6.1 Entra Agent ID : périmètre GA réel, licences, extensions des RFC (reprise et approfondissement du ch. 8 §8.1 du Vol. II) ; 6.2 Offres équivalentes des autres fournisseurs infonuagiques (état à dater) ; 6.3 Le risque de standard de fait ; 6.4 Grille du ch. 4 appliquée.
*Garde-fous : neutralité fournisseur ; distinguer GA documentée / annonce / feuille de route.*

### Chapitre 7 — Les registres gouvernés : de la spécification CSA aux registres A2A
**Thèse** : le registre d'agents est en train de devenir la pièce de conformité maîtresse de l'entreprise agentique (intuition du ch. 8 du Vol. II), mais trois modèles concurrents — registre d'entreprise, registre de fédération, annuaire protocolaire — répondent à des questions différentes de la grille.
Sections : 7.1 La spécification CSA (`toolAccessList`, `permissionBoundaries`) : état du brouillon ; 7.2 Registres et découverte A2A/AGNTCY ; 7.3 Le registre comme objet réglementaire (pont vers Partie VI) ; 7.4 Ce qui n'existe toujours pas.
*Socle candidat : brouillon CSA daté, spécifications AGNTCY.*

### Chapitre 8 — Le passeport d'agent : synthèse d'un objet encore virtuel
**Thèse** : le « passeport d'agent » n'existe dans aucune spécification de 2026 — c'est un objet de synthèse que l'ouvrage construit en assemblant carte signée, inscription au registre, chaîne de mandat et attestations de conformité, et dont il projette la normalisation 2027-2028 (Vol. I §7.4.2) en statut PROJETÉ. Pour l'entreprise agentique, le passeport est la pièce d'admission : rien n'entre au maillage sans lui.
Sections : 8.1 Assemblage : les quatre pièces du passeport ; 8.2 Qui l'émettrait, qui le vérifierait ; 8.3 Trois scénarios de normalisation (tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF) ; 8.4 Le passeport par la grille du ch. 4 : la seule construction qui répond aux cinq questions — sur le papier.
*Chapitre-pivot de l'ouvrage, homologue du ch. 13 du Vol. II (« le pont »). Inférences d'auteur explicitement marquées.*

---

## Partie III — La délégation : le mandat dans l'entreprise *(3 chapitres, ~9 500 mots)*

### Chapitre 9 — La chaîne de mandat : de l'humain à l'agent, de l'agent à l'agent
**Thèse** : la délégation est le maillon faible — les mécanismes de 2026 prouvent qu'un agent *a* une identité, presque aucun ne prouve *au nom de qui* il agit à l'instant t ; or c'est précisément ce que l'entreprise doit pouvoir démontrer à son auditeur.
Sections : 9.1 Le mandat dans les protocoles (mandats AP2, *on-behalf-of* OAuth, transaction tokens) ; 9.2 Formalisation : chaîne de délégation comme objet de première classe ; 9.3 Ce que le droit civil du mandat éclaire — et où l'analogie casse ; 9.4 L'humain, premier et dernier maillon : approbation, escalade et humain-dans-la-boucle relus comme **actes de délégation datés et signés** — les patrons d'interaction humain-agent (Arsanjani-Bustos) fournissent la typologie, l'ouvrage y ajoute l'exigence probatoire : une approbation qui ne s'inscrit pas dans la chaîne de mandat n'est pas un contrôle, c'est un rituel.
*Socle candidat : spécification AP2 — avec la divergence de gouvernance non tranchée entre les deux volumes (le fichier `commun/faits-partages.md` prévu par le README du dépôt pour la porter reste **à créer** ; l'instruire ici).*

### Chapitre 10 — Le problème des deux sauts : traçabilité de la délégation multi-saut
**Thèse** *(instruit le front ouvert du Vol. I, Synthèse §11.5)* : au-delà de deux sauts de délégation, aucun mécanisme documenté ne maintient une traçabilité opposable de bout en bout — c'est la frontière de la connaissance vérifiable de l'ouvrage, exposée plutôt que comblée.
Sections : 10.1 Pourquoi deux sauts : où chaque mécanisme perd le fil ; 10.2 Pistes (jetons imbriqués, VC chaînées, journalisation corrélée) et leurs limites démontrées ; 10.3 Question de recherche formulée pour instruction.
*Chapitre court et honnête — l'équivalent du ch. 21 du Vol. II (« la frontière de la connaissance vérifiable »), mais localisé.*

### Chapitre 11 — Know Your Agent : la vérification d'agent tiers inter-domaines
**Thèse** : le KYA transpose au domaine agentique la logique du KYC — vérifier avant d'admettre —, mais sans l'infrastructure institutionnelle (registres publics, obligations légales) qui rend le KYC possible ; la *trust fabric* inter-entreprises reste une construction privée et fragmentée — et c'est pourtant elle qui décide si l'entreprise agentique s'arrête à ses murs.
Sections : 11.1 État des propositions KYA (reprise du Vol. I §7.4.3, approfondie) ; 11.2 Admission d'un agent tiers : le point de contact entre identité et gouvernance des frontières ; 11.3 Fédérations de confiance : précédents (eIDAS, FIDO) et transposabilité.
*Garde-fou : « KYA » est un terme de marché avant d'être un terme de norme — l'écrire.*

---

## Partie IV — La confiance hostile : l'identité comme fondation de la défense *(4 chapitres, ~12 000 mots)*

### Chapitre 12 — Taxonomie des attaques sur l'identité et la délégation agentiques
**Thèse** *(instruit Q2 du Vol. II)* : la majorité des attaques propres aux systèmes multi-agents documentées à date sont des attaques d'identité (usurpation, confusion de délégué) ou de délégation (élévation par chaîne de mandat) — ce qui justifie l'absorption de la sécurité dans le cadre identitaire.
Sections : 12.1 Recension : identifiants de vulnérabilité, incidents publics datés, littérature académique (le socle que Q2 réclamait) ; 12.2 Taxonomie par la grille du ch. 4 ; 12.3 L'empoisonnement de la mémoire et des sources : quand l'attaque d'identité passe par les données — provenance des documents RAG et des entrées de mémoire longue comme problème d'identité des *sources*, pas seulement des agents (prolonge l'injection par les outils et les données du Vol. I au grain identitaire) ; 12.4 Ce que la recension ne trouve pas — l'absence d'incident public majeur à date est un fait à interpréter avec prudence, pas une preuve de sûreté.
*Traitement défensif exclusivement : mécanique des attaques au niveau architectural, sans recette d'exploitation.*

### Chapitre 13 — L'usurpation et le *rug-pull* : quand l'identité vérifiée trahit
**Thèse** : la vérification à l'admission ne protège pas contre la dérive après admission — le *rug-pull* d'un serveur MCP ou d'un agent tiers est une attaque de confiance temporelle que l'identité statique ne voit pas.
Sections : 13.1 Le *rug-pull* documenté (reprise du Vol. I, approfondie) ; 13.2 Vérification continue vs vérification à l'admission ; 13.3 Attestation d'intégrité à l'exécution : état des mécanismes.

### Chapitre 14 — La révocation : le mécanisme le moins spécifié de la pile
**Thèse** : chaque mécanisme d'identité examiné en Partie II spécifie l'émission avec soin et la révocation avec négligence — asymétrie qui reproduit l'histoire des PKI, et dont le coût se paiera à l'incident.
Sections : 14.1 Inventaire de la révocation par mécanisme (cartes, jetons, entrées de registre, mandats) ; 14.2 Le précédent PKI : CRL, OCSP, leçons transposables ; 14.3 La révocation en cascade dans une chaîne de délégation — problème ouvert.

### Chapitre 15 — L'*agentic SOC* et la boucle défensive
**Thèse** : la défense s'agentifie elle-même (Vol. I §7.5.2) — et l'identité est ce qui distingue un SOC agentique gouvernable d'un système auto-organisé ingouvernable : les agents défensifs de l'entreprise sont les premiers à devoir porter le passeport du ch. 8.
Sections : 15.1 État de l'*agentic SOC* (offres datées, périmètres réels) ; 15.2 La symétrie attaque/défense relue par l'identité ; 15.3 Référentiels de sécurité agentique en mouvement (état 2026 des cadres cités au Vol. I §7.5.3).

---

## Partie V — L'horloge post-quantique *(3 chapitres, ~9 000 mots)*

### Chapitre 16 — La menace quantique appliquée à la pile identitaire agentique
**Thèse** : toute la Partie II repose sur des signatures classiques ; les jalons de migration (NIST IR 8547 : dépréciation ~2030, retrait ~2035) tombent à l'intérieur de la durée de vie des architectures que les lecteurs conçoivent aujourd'hui — la PQC n'est pas un chapitre d'annexe, c'est une contrainte de conception de l'entreprise agentique.
Sections : 16.1 Les échéances exactes et leurs sources (reprise du Vol. I §7.4.1, revalidée) ; 16.2 *Harvest now, decrypt later* appliqué aux artefacts d'identité longue durée ; 16.3 Inventaire : quels artefacts de la pile agentique cassent, et quand.

### Chapitre 17 — La crypto-agilité comme propriété d'architecture
**Thèse** : la crypto-agilité est l'application de l'invariant du Vol. I (découplage, contrat, évolution) à la couche cryptographique — le mécanisme de signature doit être un contrat versionné, pas une hypothèse câblée.
Sections : 17.1 Définition opérationnelle et état des recommandations (NIST, normes sectorielles) ; 17.2 Audit de crypto-agilité des mécanismes de la Partie II ; 17.3 Patrons de migration sans rupture de la chaîne de confiance.

### Chapitre 18 — La dette de migration : chiffrer ce qui peut l'être, dater le reste
**Thèse** : la dette de migration PQC de la couche agentique est réelle mais largement non chiffrée à date — le chapitre établit ce que les sources portent, refuse d'extrapoler, et fournit au lecteur la méthode d'estimation plutôt qu'un chiffre.
Sections : 18.1 Ce que les études de coût publiées couvrent (et ne couvrent pas) ; 18.2 Méthode d'inventaire pour une institution ; 18.3 Fenêtre d'action 2026-2029 : le calendrier inverse.

---

## Partie VI — Le droit de l'entreprise agentique *(3 chapitres, ~9 500 mots)*

### Chapitre 19 — L'agent devant E-23 et l'AMF : l'identité comme condition d'inventaire
**Thèse** : les cadres en vigueur au 1ᵉʳ mai 2027 (E-23 ; ligne directrice IA de l'AMF, finale depuis mars 2026) exigent un inventaire des modèles et une imputabilité — deux obligations qui présupposent, sans le nommer, un registre d'agents identifiés : l'identité agentique est le prérequis technique d'obligations qui ne la mentionnent pas.
Sections : 19.1 Relecture ciblée d'E-23 et de la ligne directrice AMF par la grille du ch. 4 ; 19.2 Le registre du ch. 7 comme pièce de conformité ; 19.3 Ce que les cadres n'exigent pas — ne pas leur faire dire plus.
*Filiation directe avec le ch. 13 du Vol. II — méthode du pont reconduite.*

### Chapitre 20 — Loi 25, RGPD et l'agent : qui traite, qui décide, qui répond
**Thèse** *(prolonge Q4 du Vol. II — l'applicabilité de l'art. 12.1 à la décision multi-agents avec humain-dans-la-boucle — sans la trancher)* : le droit des renseignements personnels raisonne par responsable et mandataire — la chaîne de délégation agentique met cette dichotomie sous tension, et l'état de la doctrine ne permet qu'une cartographie des lectures possibles.
Sections : 20.1 L'article 12.1 et la décision automatisée multi-agents : état des positions (reprise du ch. 11 §11.2 du Vol. II) ; 20.2 Le mandat agentique en droit civil québécois : ce que l'analogie porte ; 20.3 Cartographie des lectures, sans verdict.
*Garde-fou renforcé : aucun avis juridique ; chaque lecture attribuée à sa source.*

### Chapitre 21 — La normalisation institutionnelle et le cadre bancaire canadien
**Thèse** *(instruit Q5 du Vol. II)* : la désignation de l'organisme de normalisation technique du cadre des services bancaires axés sur le consommateur fixera qui écrit les règles d'identité des agents financiers au Canada — événement à date incertaine mais à conséquences architecturales certaines.
Sections : 21.1 État de la désignation (à revalider au gel) ; 21.2 Scénarios et leurs conséquences sur la pile identitaire ; 21.3 Normalisation internationale (ISO/IEC SC 42, CEN-CENELEC, NIST) appliquée à l'identité d'agent.

---

## Partie VII — Le maillage d'agents : où l'entreprise applique la confiance *(2 chapitres, ~7 000 mots)*

### Chapitre 22 — Du *service mesh* à l'*agent mesh* : généalogie et anatomie
**Thèse** : le maillage d'agents est la réinstanciation, au niveau agentique, du patron *service mesh* — un plan de données qui médiatise chaque arête du graphe d'interaction et un plan de contrôle qui en centralise la politique — et cette filiation permet de trier ce que le terme recouvre réellement chez les fournisseurs de ce qu'il recouvre en marketing.
Sections : 22.1 Généalogie : sidecar, passerelle, plan de contrôle/plan de données — l'acquis service mesh (mTLS, identité de charge de travail SPIFFE/SPIRE) comme socle transposable ; 22.2 Anatomie du maillage agentique : passerelles MCP, courtage A2A, transport AGNTCY (SLIM), routage sémantique — état daté des réalisations ; 22.3 Ce que l'arête change : la leçon du Vol. I (« la sûreté n'est pas compositionnelle — la frontière de confiance se déplace vers chaque arête du graphe ») fait du mesh une conséquence architecturale, pas une mode ; 22.4 Grille du ch. 4 appliquée au maillage : ce qu'un mesh vérifie, ce qu'il transporte, ce qu'il ignore.
*Socle candidat : documentation des passerelles MCP et offres de maillage agentique (état 2026 à recenser — terme à forte charge marketing, tri strict annonce/GA/production), spécifications AGNTCY, corpus service mesh (CNCF). Garde-fous : « agent mesh » est un terme de fournisseur avant d'être un terme de norme — l'écrire ; noter l'homonymie avec le nom de code du dépôt du diptyque (« AgentMesh »), qui désigne l'articulation des deux volumes, non le patron d'infrastructure ; distinguer aussi l'« Agentic Control Plane » (consortium/produit cité au Vol. II) du plan de contrôle au sens infrastructure employé ici.*

### Chapitre 23 — Le maillage comme point d'application : PEP, politiques et *zero trust* agentique
**Thèse** : le maillage est le lieu où le passeport du ch. 8 devient opposable — point d'application des politiques (PEP) adossé à un point de décision (PDP), il transpose l'architecture *zero trust* au graphe d'agents : vérifier chaque arête, à chaque interaction, sans confiance héritée de la topologie.
Sections : 23.1 PEP/PDP agentiques : où se prend et où s'applique la décision d'autorisation (langages de politique, état des mécanismes) ; 23.2 Zero trust transposé : de « jamais confiance au réseau » à « jamais confiance au graphe » — vérification par arête, moindre privilège par délégation ; 23.3 Le maillage et la chaîne de mandat : ce que le mesh peut tracer du problème des deux sauts (ch. 10) — et ce qu'il ne résout pas ; 23.4 Coûts : latence, complexité opérationnelle, point de défaillance — les conditions qui renverseraient la recommandation du maillage.
*Socle candidat : NIST SP 800-207 (zero trust) et déclinaisons agentiques à recenser, documentation des moteurs de politique. Filiation : prolonge le « plan de contrôle obligatoire » du Vol. I (Synthèse, tableau 15) et les cinq **points de contrôle obligatoires** du Vol. II (ch. 19 §19.3) au grain de l'infrastructure.*

---

## Partie VIII — AgentOps : exploiter la confiance dans la durée *(3 chapitres, ~10 000 mots)*

### Chapitre 24 — L'observabilité agentique : voir ce que fait un agent identifié
**Thèse** : l'AgentOps commence par l'observabilité, et l'observabilité agentique a trouvé son socle de standardisation dans les conventions sémantiques GenAI/agents d'OpenTelemetry — mais tracer un *appel* n'est pas tracer une *délégation* : la corrélation entre trace d'exécution et chaîne de mandat est le chaînon manquant que l'ouvrage documente.
Sections : 24.1 De l'APM à l'AgentOps : ce que l'observabilité classique couvre et où l'agent la déborde (non-déterminisme, coût par jeton, horizon de tâche) ; 24.2 État des conventions OpenTelemetry pour l'IA générative et les agents (statut exact des conventions — stable/expérimental — à dater au gel) ; 24.3 La journalisation probatoire : quand la trace d'exploitation devient pièce de conformité (pont vers E-23 ch. 19 — l'inventaire exige l'identité, l'audit exige la trace) ; 24.4 Corréler la trace au passeport : l'identité comme clé de jointure de l'observabilité.
*Socle candidat : conventions sémantiques OTel (source primaire versionnée), documentation des plateformes d'observabilité agentique — métriques auto-déclarées, attribuées à chaque occurrence (règle du Vol. II, avant-propos et PRD §8.2.1, reconduite). Garde-fou : « AgentOps » désigne ici la discipline, non tel produit homonyme — désambiguïsation en encadré à la première occurrence.*

### Chapitre 25 — Le cycle de vie opérationnel : évaluation continue, dérive et incident
**Thèse** : l'exploitation d'un parc d'agents est une boucle — évaluer en continu, détecter la dérive, répondre à l'incident, réviser le mandat — et cette boucle est la réalisation opérationnelle du quatrième terme de l'invariant du Vol. I ; sans elle, le passeport certifie un comportement passé, jamais le comportement courant.
Sections : 25.1 L'évaluation en production : des jeux d'essai à l'évaluation continue (pont vers la science de l'évaluation, front ouvert du Vol. I §7.6.4 ; matière : test-débogage-évaluation-déploiement de Nagasubramanian, transposée au parc) ; 25.2 La dérive agentique : dérive de modèle, dérive d'outil (*rug-pull* du ch. 13 relu en signal d'exploitation), dérive d'autonomie ; 25.3 La réponse à incident agentique : révocation d'urgence (ch. 14), confinement par le maillage (ch. 23), articulation avec l'*agentic SOC* (ch. 15) ; 25.4 GitOps du parc d'agents : versionnement des mandats, promotion entre environnements, retour arrière ; 25.5 L'agent qui apprend : si l'adaptation continue est un objectif de conception (patrons d'apprentissage d'Arsanjani-Bustos ; capacité d'auto-modification du paradigme APM — adaptation éphémère vs évolution persistante, Vol. II ch. 6 §6.3), alors le passeport certifie un comportement *daté* — la question de la revalidation après apprentissage est posée, l'état des mécanismes recensé, et la lacune assumée si le socle ne porte rien.
*Socle candidat : littérature MLOps/LLMOps transposée (filiation à établir explicitement plutôt qu'à réinventer), guides d'exploitation des plateformes agentiques, corpus d'appui (Nagasubramanian ch. 11 et 13 ; Arsanjani-Bustos ch. 11). Chapitre qui referme trois fils ouverts en Parties IV-V — c'est sa fonction de synthèse.*

### Chapitre 26 — Les indicateurs de l'AgentOps : mesurer un parc d'agents sans fabriquer de chiffres
**Thèse** : la discipline naissante n'a pas encore ses indicateurs de référence — les métriques publiées (taux de succès de tâche, coût par résolution, horizon de tâche déléguée) sont hétérogènes et auto-déclarées ; le chapitre propose une grille d'indicateurs minimale dérivée des obligations des Parties VI (conformité) et VII (maillage), en la présentant comme construction d'auteur.
Sections : 26.1 Recension critique des métriques publiées (règle d'attribution du Vol. II : attribution systématique, illustration jamais preuve) ; 26.2 La grille minimale : ce que l'architecte doit pouvoir répondre à l'auditeur (disponibilité du parc, couverture de traçabilité, délai de révocation, fraîcheur des évaluations) ; 26.3 La métrique d'horizon de tâche déléguée : état du front ouvert hérité du Vol. I (Synthèse §11.5).
*Garde-fou : chapitre à haut risque de fabrication — chaque indicateur proposé est marqué construction d'auteur, chaque chiffre cité est attribué.*

---

## Partie IX — Blueprint : l'entreprise agentique de confiance *(2 chapitres + clôture, ~11 000 mots)*

### Chapitre 27 — Architecture de référence : la fabrique de confiance et son organisation
**Thèse** : les Parties I-VIII se composent en une architecture de référence à trois étages — la fabrique d'identité (émission, registre, vérification, révocation), le maillage qui l'applique (PEP/PDP, passerelles), l'AgentOps qui l'exploite (observabilité, évaluation, incident) — formalisée en ArchiMate (méthode-signature du Vol. I) ; mais l'architecture ne suffit pas : l'entreprise agentique est autant une structure de rôles et une trajectoire de maturité qu'une pile technique, et le chapitre traite les deux à parité.
Sections : 27.1 Vue d'ensemble : les trois étages et leurs contrats mutuels ; 27.2 Formalisation ArchiMate — fonctions d'identité, points d'application du maillage, boucle d'exploitation ; 27.3 Points d'intégration avec l'existant IAM et l'observabilité en place — étendre, ne pas dupliquer ; 27.4 Le modèle de maturité de l'entreprise agentique : trajectoire de déploiement par paliers, construite en confrontant les trois modèles de maturité d'Arsanjani-Bustos (GenAI Maturity Model, Agentic AI Maturity Spectrum, Implementation Maturity Levels), l'autonomie graduée du Vol. I et la grille du ch. 4 — à chaque palier, le niveau d'identité, de maillage et d'AgentOps exigible ; les trois modèles sources sont rapportés, la synthèse est une construction d'auteur ; 27.5 L'organisation de la fabrique : qui opère quoi — responsabilités entre équipe plateforme, IAM, sécurité et exploitation, facteur humain et conduite du changement (matière : « making agentic AI enterprise-ready » de Ranjan et al., élevée du constat à la structure de rôles).

### Chapitre 28 — Instanciation et clôture : le cycle de vie complet d'un agent d'entreprise
**Thèse** : le blueprint se prouve par le parcours — de l'enregistrement d'un agent à sa révocation, chaque transition est jouée contre l'architecture du ch. 27, au grain d'un cas financier canadien (continuité avec Boréalis, Vol. I, *Synthèse* §10) — puis l'ouvrage se clôt par la discipline du Vol. II : lacunes exposées, péremption datée, revalidation protocolée.
Sections : 28.1 Naissance : enregistrement, émission du passeport, admission au maillage ; 28.2 Vie : délégations, vérifications par arête, traces d'exploitation, évaluations continues, renouvellements, migration PQC ; 28.3 Mort : révocation, cascade dans la chaîne de mandat, retrait du maillage, archivage probatoire ; 28.4 Confrontation externe : le cas fil rouge *loan processing* d'Arsanjani-Bustos (mono-agent → multi-agent → frameworks) rejoué contre le blueprint — ce que leur trajectoire valide, ce qu'elle ignore (l'identité y est justement le point faible à documenter) ; 28.5 Lacunes résiduelles et questions transmises au volume suivant ; 28.6 Événements de péremption (désignation Q5, normalisation du passeport, stabilisation des conventions OTel, premier incident public d'identité agentique, jalons PQC) et protocole de revalidation.

---

## Annexes *(~9 000 mots)*

- **Annexe A — Méthodologie** : constitution du socle, vote adversarial, niveaux de preuve, tri prospectif (double héritage : [A]/[B]/[C] du Vol. II, PROGRAMMÉ/PROJETÉ/SPÉCULATIF du Vol. I).
- **Annexe B — Matrice des mécanismes** : les mécanismes des Parties II-III et les composants de maillage de la Partie VII croisés avec la grille du ch. 4, l'état PQC et la couverture d'observabilité (Partie VIII) — la table de référence de l'ouvrage.
- **Annexe C — Chronologie 2024-2030** : émission des specs, GA produits, drafts IETF (avec dates d'expiration), jalons des conventions OTel et des offres de maillage, jalons réglementaires (E-23 et ligne directrice AMF : 1ᵉʳ mai 2027) et PQC (2030/2035).
- **Annexe D — Glossaire** : entreprise agentique, NHI, VC/DID, KYA, crypto-agilité, passeport d'agent, *agent mesh*, AgentOps, PEP/PDP, *zero trust* agentique — avec le statut épistémique de chaque terme (norme, marché ou construction d'auteur) ; « agent mesh » et « AgentOps » attendus au statut *marché*, « entreprise agentique » et « passeport d'agent » au statut *construction d'auteur adossée au marché*.
- **Annexe E — Catalogue de patrons de la confiance agentique** : les mécanismes des Parties II-III (émission, vérification, révocation, chaîne de mandat), les points d'application de la Partie VII et les boucles de la Partie VIII, formalisés au gabarit des patrons (contexte, problème, forces, solution, conséquences, patrons liés) — filiation revendiquée avec la discipline d'Arsanjani-Bustos et, en amont, avec l'héritage GoF/EIP que le Vol. I mobilisait déjà ; chaque patron renvoie à son chapitre et à son socle. *(~2 500 mots, comptés dans le bloc annexes.)*

---

## Risques de cadrage identifiés au brouillon (reconduits et complétés en v0.4)

1. **Socle mince par construction** : le sujet est choisi *parce que* les deux volumes le déclarent sous-documenté ; le PRD devra fixer un seuil réaliste de vote adversarial et assumer une proportion [C] supérieure aux volumes précédents.
2. **Péremption rapide des Parties II-III** : drafts IETF et brouillons CSA vivent en mois — discipline de datation par chapitre indispensable, dates de gel individuelles comme au Vol. II.
3. **Double risque du ch. 8 (passeport)** : construction d'auteur au cœur de l'ouvrage — marquage d'inférence systématique, sous peine de fabriquer le standard qu'on prétend décrire.
4. **Partie IV et dualité d'usage** : traitement architectural et défensif strict ; la recension du ch. 12 cite, elle ne reproduit pas.
5. **Vocabulaire de marché en Parties VII-VIII — et au titre** : « entreprise agentique », « agent mesh » et « AgentOps » sont des termes de fournisseur sans définition normative à date — risque double de recension publicitaire (prendre une plaquette pour une capacité) et de périmètre flou (chaque éditeur y met ce qu'il vend). Parade : définition d'auteur posée d'entrée (avant-propos pour « entreprise agentique » ; ch. 22 §22.1 par filiation service mesh ; ch. 24 §24.1 par filiation APM/MLOps), tri strict annonce/GA/production, et statut épistémique explicite au glossaire. Le titre assume le terme de marché ; l'avant-propos le désamorce.
6. **Risque de dilution** : trois objets (identité, maillage, exploitation) dans un ouvrage — la ligne de défense est la thématique unifiante : les trois sont les trois capacités de l'entreprise agentique (émettre, appliquer, exploiter) ; tout contenu de maillage ou d'AgentOps sans lien à l'identité ou à la délégation est hors périmètre et doit être coupé au PRD.
7. **Littérature secondaire de fournisseur** : deux des trois ouvrages du corpus d'appui sont d'auteurs Google Cloud (Arsanjani-Bustos, préface du chef de la direction de Google Cloud) — biais d'écosystème possible en faveur d'A2A et de la pile Google ; le troisième (Ranjan et al., 2025) est antérieur à la stabilisation protocolaire. Parade : règle du « jamais seul » (aucune affirmation centrale portée par le corpus d'appui sans source primaire concordante), attribution systématique, et vérification à la spec de toute affirmation protocolaire reprise d'un livre.
8. **Confusion livre/socle** : la tentation de traiter un manuel publié comme une entrée [B] du socle au motif qu'il est imprimé — un livre date de son bouclage éditorial, pas de sa lecture ; chaque fait daté repris du corpus d'appui porte la date du livre, et tout fait périssable (versions, GA, gouvernance) est revalidé à la source primaire au gel du chapitre.
9. **Hygiène de dépôt (nouveau, v0.4)** : trois écarts constatés à la vérification des renvois — (a) `commun/faits-partages.md` et `eval.md`, cités par le README racine et par ce TOC (ch. 9), n'existent pas : à créer ou à retirer des renvois avant le PRD ; (b) le README racine décrit une arborescence (`vol-1-…/`, `vol-2-…/`) qui ne correspond pas aux dossiers réels : à resynchroniser ; (c) le Vol. I vit en double numérotation (`Monographie.md` §1-§7 ; `Synthese Monographie.md` §3-§12) : tout renvoi du Vol. III doit nommer le fichier. Un renvoi cassé dans un ouvrage qui fait de la traçabilité sa thèse est plus qu'une coquille — c'est un contre-argument.
