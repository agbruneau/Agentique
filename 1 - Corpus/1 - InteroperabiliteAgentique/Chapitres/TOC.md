# TOC — Table des matières commentée du Volume I

| Champ | Valeur |
|---|---|
| Version | **1.0 — rétro-documentation d'un volume achevé** (18 juillet 2026). Contrairement aux `TOC.md` des Vol. III et du *Compendium*, qui sont des **spécifications d'ouvrages à écrire**, celui-ci est établi **à partir du texte livré** : chaque thèse, chaque liste de sections et chaque décompte ci-dessous a été relevé sur `Monographie.md` et sur les fichiers de `Chapitres/`, non projeté. |
| Date | 18 juillet 2026 |
| Statut | **Rédaction terminée, PDF publiés.** Socle documentaire arrêté à **juin 2026** ; double passe de vérification adverse close le **24 juin 2026** ; passe de finalisation en **juillet 2026**. Le travail courant est la maintenance : corrections, vérification adverse des citations, régénération des PDF. |
| Filiation | Premier panneau du triptyque : Vol. I (**théorie mondiale**, gel juin 2026) → Vol. II *L'autonomie encadrée* (cas canadien réglementé) → Vol. III *L'entreprise agentique*. Les volumes aval citent le Vol. I sous **deux numérotations distinctes** : les renvois §7.x résolvent contre `Monographie.md` (numérotation par chapitre), les renvois §10, §11.5 et tableau 15 contre `Synthese Monographie.md` (numérotation §3-§12) — nommer le fichier à chaque renvoi. |
| Autorité | Ce fichier **décrit** ; il ne prescrit pas. Les conventions de rédaction qui font autorité sur ce volume sont au [`CLAUDE.md`](../CLAUDE.md) du dossier ; en cas d'écart entre les deux, c'est le `CLAUDE.md` qui tranche et ce fichier qui est à corriger. |

---

## Titre

# Interopérabilité agentique en entreprise dans le domaine des services financiers
## Monographie en science et génie informatique — André-Guy Bruneau, M.Sc. IT, juin 2026

---

## Thèse d'ensemble

L'apparition, à partir de 2024-2025, d'une famille de protocoles d'interopérabilité agentique (MCP pour l'axe agent-outil, A2A pour l'axe agent-agent, plus les initiatives concurrentes de découverte, d'identité et de paiement) a produit un foisonnement de spécifications dont la cohérence d'ensemble reste à établir. L'ouvrage soutient que cette transposition **n'abolit pas les acquis de l'intégration d'entreprise : elle les *réinstancie*** à un niveau d'abstraction supérieur, où les mêmes tensions fondamentales — hétérogénéité, autonomie, distribution — resurgissent sous des mécanismes nouveaux.

Question directrice : *quelles propriétés architecturales permettent à des agents d'intelligence artificielle d'interopérer de manière sûre, gouvernée et évolutive au sein de l'entreprise, en particulier dans le domaine exigeant des services financiers ?* La réponse est énoncée comme un **invariant transversal** — **découplage** (réduction des dépendances mutuelles), **contrat** (interface explicite qui rend le découplage opérationnel), **évolution** (capacité du contrat à changer sans rompre la coopération) — éprouvé du niveau le plus technique jusqu'au niveau agentique, où il prend la forme de la *découverte*, de la *sémantique partagée*, de l'*identité* et de la *gouvernance des frontières*. Le ch. 4 lui adjoint une dimension d'**exploitation** (§4.12.4), reprise et élargie au ch. 7 (§7.0) : un parc d'agents doit rester non seulement interopérable, mais *opérable*.

Ce quatrième terme est le legs explicite du Vol. I au Vol. III, dont la Partie VIII (AgentOps) le prend pour fondement.

## Publics visés

Double lectorat, servi sans cloisonner le propos : public **recherche** (modèles, taxonomies, formalismes, questions ouvertes) et public **praticien-architecte** (normes, protocoles, technologies, décisions de mise en œuvre datées). Deux dispositifs parcourent le texte à cette fin — les encadrés *Perspective recherche*, qui isolent les apports théoriques, et les encadrés *Mise en œuvre*, qui isolent les normes datées et les considérations de déploiement.

## Volumétrie mesurée

| Ensemble | Mesure | Méthode |
|---|:---:|---|
| Corps doctrinal (ch. 1-7, hors bibliographies) | **≈ 171 600 mots** | `wc -w` sur les sept fichiers `Chapitre N - {Sujet}.md` |
| Sections numérotées `N.x` du corps | **91** | 13 + 13 + 14 + 12 + 15 + 12 + 12 |
| Entrées de la Bibliographie générale | **1 270** | comptage des entrées de `Monographie.md`, §Bibliographie générale, par chapitre : 235 + 208 + 165 + 175 + 261 + 71 + 155 |
| Annexe B — ADS | ≈ 17 500 mots, 18 sections, 6 sous-annexes, 28 diagrammes | décompte déclaré en tête d'ADS |
| `Monographie.pdf` | **569 p.** | `pypdf` |
| `Synthese Monographie.pdf` | **69 p.** | `pypdf` |

⚠ **Écart signalé, non arbitré.** Les décomptes ci-dessus sont ceux de l'**ouvrage consolidé**. Les bilans de vérification portés en tête de chaque fichier `Chapitre N - Bibliographie - {Sujet}.md` annoncent des totaux **inférieurs** pour les ch. 1, 4 et 7 (228, 173 et 140 entrées) : ces bilans n'ont pas été reportés après les révisions v3/v4 fusionnées dans `Monographie.md`. L'écart est ici constaté, pas corrigé — le rapprochement relève d'une passe de vérification propre.

## Conventions structurelles du volume

- **Progression en spirale**, du général au spécifique : chaque chapitre suppose les précédents et **y renvoie plutôt que de les réexpliquer**. Les ch. 5, 6 et 7 ouvrent chacun sur une section « acquis / ajouté » qui formalise cette frontière ; le ch. 6 la durcit d'une phrase-test de non-redondance (§6.0.1).
- **Numérotation préfixée du numéro de chapitre** : sections `N.x` (`##`), sous-sections `N.x.y` (`###`), items feuilles `N.x.y.z` (`####`). *Exception documentée :* les **ch. 2 et 4 ouvrent à `N.1`** (pas de section `N.0`) — ne pas renuméroter.
- **En-tête de chapitre** uniforme : titre `#`, bloc `> **Résumé.**`, puis ligne *Public visé / Fil conducteur / dates*.
- **Marqueur ⚠** = ressource vivante (spécification versionnée par date, texte réglementaire en cours d'adoption, communiqué, rapport d'analyste) dont la version doit être figée au moment de citer.
- **Tri épistémique au ch. 7 seul** : **PROGRAMMÉ** (engagement daté — un *fait sur le futur*), **PROJETÉ** (prévision millésimée d'analyste), **SPÉCULATIF** (pari de recherche). Aucun autre chapitre ne projette au-delà de juin 2026.

---

## Liminaires (`Monographie.md`, avant le ch. 1)

Page titre (bloc Typst brut), **Résumé** + mots-clés, table des matières (`#outline`, profondeur 2), **Liste des figures** — qui acte que le corps doctrinal n'en comporte aucune, les tableaux étant présentés *en place* et l'Annexe B faisant seule exception avec ses 28 diagrammes —, **Liste des abréviations** (109 sigles), **Remerciements**, **Avant-propos** (dont la déclaration relative à l'usage de l'IA générative et la note d'édition et de vérification), **Introduction** (problématique, question de recherche, invariant, double public et méthode, plan de l'ouvrage).

---

## Chapitre 1 — L'interopérabilité des systèmes d'information *(≈ 26 100 mots, 13 sections)*

**Thèse** : l'interopérabilité n'est pas un choix de protocole mais une **propriété d'ensemble** que l'organisation acquiert puis maintient ; traitée comme problème d'intégration d'entreprise, elle se laisse ramener à l'invariant découplage/contrat/évolution, dont ce chapitre établit la généalogie théorique avant que les six suivants ne l'éprouvent sur des objets agentiques.

Sections : 1.0 Introduction — l'interopérabilité comme problème d'intégration d'entreprise ; 1.1 Fondements et théorie ; 1.2 Cadres de référence et modèles de maturité ; 1.3 Architectures d'intégration, de la SOA aux maillages ; 1.4 Styles d'API, conception et gestion ; 1.5 Messagerie, MOM et architecture événementielle ; 1.6 Patrons d'intégration et orchestration de processus ; 1.7 Interopérabilité des données, formats et plan analytique ; 1.8 Interopérabilité sémantique, ontologies et graphes de connaissances ; 1.9 Sécurité, identité et confiance ; 1.10 Gouvernance, test et observabilité ; 1.11 Tendances 2024-2026 et interopérabilité des agents IA ; 1.12 Synthèse et questions ouvertes.

*Socle : 235 entrées — fondateurs (Wegner, Hohpe & Woolf, Akkoyunlu et al., Brewer), normes et spécifications (84 entrées), cadres de maturité dont le LCIM, réglementation européenne, développements 2024-2026. Le §1.11 est la charnière : il amorce MCP et A2A que le ch. 3 traitera de plein droit.*

---

## Chapitre 2 — L'ingénierie des systèmes agentiques (IA agentique) *(≈ 27 200 mots, 13 sections)*

**Thèse** : la bascule du LLM qui *répond* à l'agent qui *agit* élargit le **rayon d'impact** — une hallucination textuelle se corrige par relecture, une hallucination qui déclenche une action irréversible engage le système producteur ; c'est ce changement de rayon qui fait de l'agentique un problème d'ingénierie distinct, non un raffinement de l'usage conversationnel.

Trois fils transversaux, posés puis rappelés : l'**économie des jetons** comme contrainte de premier ordre ; le **choix et le service du modèle** comme décision d'architecture ; la **sécurité**, singulièrement l'injection d'invite — *non résoluble au niveau du modèle*, donc traitée par défense en profondeur.

Sections : 2.1 Introduction — l'essor des systèmes agentiques et l'enjeu d'ingénierie ; 2.2 Fondements et définitions ; 2.3 Architectures d'agent et boucle agentique ; 2.4 Raisonnement, planification et calcul à l'inférence ; 2.5 Utilisation d'outils et accès aux outils (MCP) ; 2.6 Ancrage informationnel I — mémoire et contexte ; 2.7 Ancrage informationnel II — RAG agentique ; 2.8 Systèmes multi-agents, orchestration et frameworks ; 2.9 Évaluation, bancs d'essai et observabilité ; 2.10 Sécurité, sûreté et alignement ; 2.11 Opérationnalisation et gouvernance (AgentOps) ; 2.12 Applications et tendances 2024-2026 ; 2.13 Synthèse d'ingénierie et questions ouvertes.

*Socle : 208 entrées, dont 111 articles de recherche sur les agents LLM (2022-2026). Les formalismes classiques (agent rationnel, BDI, MAS, (PO)MDP, RL) servent d'ancrage, non de fil dominant. Ouvre à `2.1` — pas de section `2.0`.*

---

## Chapitre 3 — L'interopérabilité agentique *(≈ 23 300 mots, 14 sections)*

**Thèse** *(point de convergence des ch. 1 et 2)* : ce qui transite entre systèmes d'IA n'est plus seulement de la donnée structurée mais des **intentions**, des **tâches** et des **capacités** négociées à l'exécution — glissement des noms vers les verbes qui déplace le problème du contrat déterministe vers le **contrat comportemental probabiliste**, de la connectivité vers la négociation, et de la sécurité d'un agent vers la **sécurité des frontières entre agents**.

Verrou central identifié : mobilisant la grille communication / syntaxique / sémantique (Yuan et al., *Beyond Message Passing*), le chapitre montre que les protocoles de 2026 **excellent au technique et au syntaxique mais repoussent le sémantique et le pragmatique vers la couche applicative**. C'est le front que le ch. 7 §7.6 reprend comme programme de recherche.

Sections : 3.0 Introduction — la convergence des ch. 1 et 2 ; 3.1 Les niveaux d'interopérabilité du ch. 1 appliqués aux agents ; 3.2 Agent-outil — MCP comme couche de contrat ; 3.3 Agent-agent — A2A et ANP (et la fusion d'ACP-agent) ; 3.4 Découverte, registres et nommage ; 3.5 Interopérabilité sémantique — de l'accord-de-protocole à la compréhension ; 3.6 Identité, confiance et axe agent-humain ; 3.7 La pile de protocoles agentiques et son étagement ; 3.8 Portabilité inter-modèles et inter-cadriciels ; 3.9 Interopérabilité du commerce et des paiements agentiques ; 3.10 Sécurité de la couche d'interopérabilité ; 3.11 Modes d'échec propres à l'interopérabilité agentique ; 3.12 Évaluation, conformité et observabilité ; 3.13 Gouvernance, standardisation et questions ouvertes.

*Socle : 165 entrées, dont 43 spécifications et protocoles (MCP / A2A / ANP / ACP / AP2 / x402 + RFC). Piège de nomenclature traité en tête de chapitre et rappelé à chaque première occurrence : **ACP-agent** (Agent Communication Protocol, IBM/BeeAI, §3.3.4) ≠ **ACP-commerce** (Agentic Commerce Protocol, OpenAI/Stripe, §3.9.2).*

---

## Chapitre 4 — L'interopérabilité agentique en entreprise *(≈ 23 400 mots, 12 sections)*

**Thèse** : « les protocoles s'entendent » n'est pas « les agents créent de la valeur sous contrainte organisationnelle ». Le déplacement du ch. 4 est un **déplacement d'échelle** — du couple agent-outil vers l'organisation comme système-de-systèmes, où les composants préexistent, appartiennent à des propriétaires différents et ne peuvent être réécrits à volonté. Ce qui s'y résout ne se résout pas au niveau du protocole mais à celui de l'architecture d'entreprise et de son modèle opérationnel.

Trois plans d'interaction structurent le chapitre : **agent-outil** (§4.2, §4.5), **agent-agent** (§4.6, §4.10) et **agent-humain** — transverse, sans section propre, ancré aux §4.6.4, §4.7.4, §4.8.5 et §4.11.4. Proposition économique : le passage **N×M → N+M**, rebouclé à la grille de décision finale (§4.12.3) et érigé en moteur prospectif au ch. 7.

Sections : 4.1 L'enjeu d'entreprise — de la dette d'intégration à la prolifération d'agents ; 4.2 Intégrer les agents au tissu d'intégration existant ; 4.3 Plateformes d'agents d'entreprise et stratégie de standards ouverts ; 4.4 Identité et accès des agents à l'échelle ; 4.5 Accès aux données et ancrage gouverné ; 4.6 Orchestration et collaboration humain-agent, inter-équipes et B2B ; 4.7 Sécurité du parc d'agents à l'échelle ; 4.8 Gouvernance et conformité (AI Act, ISO 42001, RGPD, sectoriel) ; 4.9 Observabilité, fiabilité, évaluation en production et FinOps ; 4.10 Interopérabilité inter-entreprises, commerce agentique et *data spaces* ; 4.11 Adoption organisationnelle, modèle opérationnel et maturité ; 4.12 Architectures de référence, études de cas et questions ouvertes (synthèse ch. 1-4).

*Socle : 175 entrées, dont 70 plateformes et outils d'entreprise et 30 rapports d'analystes. Règle éditoriale du chapitre : chaque sous-section est menée par un **patron** ou un **critère** d'architecture, les produits nommés venant en illustration datée — annonce / preview / GA systématiquement distinguées. L'encadré §4.1.6 fixe la convention de lecture des chiffres. Ouvre à `4.1` — pas de section `4.0`.*

---

## Chapitre 5 — L'interopérabilité agentique dans le domaine financier *(≈ 30 500 mots, 15 sections — le plus long du volume)*

**Thèse** : le vertical financier n'est pas un cas d'usage parmi d'autres mais le plus exigeant, parce qu'il combine **quatre durcisseurs** que le ch. 4 ne traite qu'en générique — irréversibilité et finalité du règlement, exigences de fonds propres et risque systémique, risque-modèle formalisé (SR 11-7 remplacé par SR 26-2, OSFI E-23, PRA SS1/23), auditabilité réglementaire avec ségrégation des tâches. L'exigence agentique est **dérivée de ces propriétés intrinsèques**, non d'un catalogue de produits.

Patron directeur transférable : l'**autonomie graduée sous contrôle de finalité** — *human-in/on-the-loop* calibré sur l'irréversibilité et la matérialité financière de l'action. C'est ce patron que l'Annexe B décline en geste *préparation → release*.

Structure en trois temps. **Bloc transverse** : 5.0 Orientation (acquis ch. 1-4 vs ajouté) ; 5.1 Pourquoi l'agentique y est durcie ; 5.2 Standards de données financières ; 5.3 Maillage réglementaire UE / US / Canada-Québec ; 5.4 Risque-modèle, auditabilité et explicabilité ; 5.5 Sécurité, fraude, AML-KYC et identité d'agent (KYA) ; 5.6 Données, résidence et souveraineté. **Cinq sous-domaines** : 5.7 Bancaire ; 5.8 Assurance dommage (IARD/P&C) ; 5.9 Assurance de personne (Vie & Santé) ; 5.10 Gestion de patrimoine & d'actifs ; 5.11 Services TI dans le domaine financier. **Clôture** : 5.12 Synthèse financière (architecture de référence, maturité, décision) ; 5.13 Interop B2B et commerce/paiements agentiques en finance ; 5.14 Synthèse du chapitre et transition.

*Socle : 261 entrées — le plus fourni du volume, dont 62 normes et textes réglementaires (classés par sous-domaine puis chronologiquement, exception déclarée à l'ordre alphabétique) et 65 rapports d'analystes et études de cas. Ce qu'ajoute le chapitre est circonscrit à cinq dimensions : intensité réglementaire sectorielle, standards de données financiers, irréversibilité transactionnelle, double qualification de l'agent (modèle **et** tiers TIC), déclinaison en cinq sous-domaines.*

---

## Chapitre 6 — Blueprint d'architecture d'entreprise ArchiMate *(≈ 21 100 mots, 12 sections)*

**Thèse** : le verrou méthodologique est nommé d'emblée — **ArchiMate n'a aucun élément natif** pour l'agent autonome, l'appel d'outil MCP, l'interaction A2A, l'identité non humaine ou le plan de contrôle. La seule extension défendable est le mécanisme officiel **Specialization + stéréotype `<<...>>` + Profiles**, sur le modèle du *Risk & Security Overlay*. La contribution du chapitre est une **traduction structurelle**, jamais une reprise du fond conceptuel.

Garde-fou maintenu de bout en bout, la phrase-test de non-redondance (§6.0.1) : *« si l'on retire le mot ArchiMate et que la phrase tient encore comme un exposé des chapitres 1 à 5, c'est une redondance à renvoyer »*.

Sections : 6.0 Mode d'emploi, contrat de lecture et primer ArchiMate ; 6.1 Le problème de modélisation — patrons ArchiMate pour les concepts agentiques ; 6.2 Motivation — intentions, exigences réglementaires, conformité traçable ; 6.3 Strategy — capacités agentiques et chaînes de valeur ; 6.4 Business — rôles, collaborations humain-agent, objets financiers ; 6.5 Application et Technology — agents, protocoles, runtime, résidence ; 6.6 Points de vue transverses — sécurité/risque, conformité, observabilité/audit ; 6.7 Gouvernance des vues et organisation du blueprint ; 6.8 Exemple de référence de bout en bout — souscription vie augmentée (variante FNOL P&C) ; 6.9 Bibliothèque de patrons et anti-patrons ; 6.10 Maturité et feuille de route par plateaux — transposition LCIM vers agents ; 6.11 Questions ouvertes et synthèse.

*Socle : 71 entrées — le plus resserré, par construction : le chapitre pondère volontairement vers les standards d'architecture (The Open Group, ISO/IEC 42010), la littérature d'EA et les modèles de référence financiers, et renvoie le reste aux bibliographies des ch. 1-5. Version de référence : **ArchiMate 4** (The Open Group, doc **C260**, 27 avr. 2026), équivalents **3.2** (oct. 2022) en notes de transition.*

⚠ *Ressources vivantes du chapitre, à recouper à la lecture : la liste définitive des éléments retirés/renommés de C260 ; l'état du support outils (à la mi-2026, la quasi-totalité des outils EA n'exporte/importe encore que 3.2 nativement) ; le format d'échange v4 ; les programmes de certification en cours de mise à jour.*

*Le §6.1.9 est un point d'appui aval : il tient le **registre des stéréotypes** dont l'Annexe B et le Vol. II se servent.*

---

## Chapitre 7 — L'interopérabilité agentique à l'horizon 2027-2032 *(≈ 20 100 mots, 12 sections)*

**Thèse** *(chapitre prospectif et capstone)* : les protocoles d'interopérabilité agentique sont, pour l'essentiel, **livrés** (ch. 3) et déjà gouvernés, déployés et formalisés (ch. 4-6) ; ce qui reste ouvert pour l'horizon n'est plus surtout *technique* mais **institutionnel et économique** — fragmentation de la gouvernance par couche, verrou sémantique/pragmatique non résolu, confiance composable, identité post-quantique, responsabilité et risque systémique. Sous la pression des forces macro (courbe de capacité, économie de l'inférence, soutenabilité, souveraineté), l'interopérabilité cesse d'être un raffinement pour devenir une **condition de marché**.

Deux ancrages datés structurent tout le chapitre : la **grappe d'échéances réglementaires de 2027** et la **migration post-quantique** (dépréciation 2030, interdiction 2035) comme **horloge de l'identité agentique** — horloge que le Vol. III reprend comme tension d'ensemble.

Sections : 7.0 Orientation — lire un chapitre prospectif sans céder à la prédiction ; 7.1 La grappe d'échéances 2027-2032, le squelette daté (PROGRAMMÉ) ; 7.2 Trajectoire des protocoles — de la cadence par jalons à la coexistence stratifiée gouvernée ; 7.3 La bifurcation de la gouvernance par couche (AAIF, FIDO, W3C, IETF, DIF) ; 7.4 Identité vérifiable et cryptographie post-quantique ; 7.5 Trajectoire de la menace — de l'attaque autonome à l'*agentic SOC* ; 7.6 Le programme de recherche — sémantique, garanties composables, science de l'évaluation ; 7.7 Trajectoire technologique et macro — capacité, coût, soutenabilité, souveraineté ; 7.8 Prospective d'entreprise — sortie du pilote, assainissement du marché, organisation agentique ; 7.9 La finance à l'horizon — rails instantanés/tokenisés, commerce agentique, risque systémique ; 7.10 Responsabilité, assurabilité et gouvernance de l'émergence ; 7.11 Scénarios 2027-2032 et synthèse de l'ouvrage.

*Socle : 155 entrées, propres à l'horizon — les ancrages déjà établis aux ch. 1-6 ne sont repris que lorsque leur dimension **future** (calendrier, feuille de route) est directement citée. Le §7.0.2 est le **siège de la discipline** épistémique : il fonde le tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF qui s'applique ensuite à chaque énoncé du chapitre.*

⚠ *Ressources vivantes du chapitre : publication au JOUE du Digital Omnibus (reports de l'AI Act adoptés par le Conseil le 29 juin 2026) ; feuilles de route MCP/A2A, W3C, IETF (sans dates engagées) ; statut de la « spec conjointe MCP/A2A » ; calendriers de migration PQC et ISO 20022 ; toute projection d'analyste (millésime + statut obligatoires).*

---

## Conclusion

Ressaisit la démonstration, dégage les contributions et les limites, et nomme les fronts de recherche ouverts. Les fronts qu'elle laisse explicitement ouverts — délégation au-delà de deux sauts, valeur probante des mécanismes d'identité, exploitation dans la durée — sont ceux que les Vol. II et III instruisent.

## Bibliographie générale

**1 270 entrées**, regroupées **par chapitre** puis par catégorie thématique (six catégories par chapitre : fondateurs / recherche / spécifications et normes / référentiels sécurité-identité-gouvernance / réglementation / ressources praticiennes, l'intitulé variant selon le chapitre). Chaque référence a fait l'objet d'une **vérification adverse** — existence, auteurs, année, numéro de norme, de RFC ou de recommandation — avant d'être affirmée exacte.

Deux réserves de forme, déclarées en tête de la bibliographie et à conserver telles quelles : les renvois « référence → section » ne sont **pas** reportés dans la version consolidée (chaque agent de recherche ayant numéroté selon sa propre vue) ; les accents des noms de mois dans les chaînes de citation sont préservés **verbatim**, même fautifs (« fevrier »), pour ne pas altérer les métadonnées sources.

## Annexe A — Plans détaillés et bibliographies par chapitre

Table de correspondance des documents d'accompagnement : pour chaque chapitre, le **plan détaillé** (table des matières hiérarchique glosée) et la **bibliographie vérifiée**, tous deux tenus dans `Chapitres/` et non reproduits intégralement au corps consolidé. L'annexe porte un tableau d'ampleur par chapitre.

## Annexe B — Architecture détaillée de solution (ADS) *(≈ 17 500 mots)*

**Nature distincte du corps doctrinal**, rendue dans le même PDF : livrable d'ingénierie *prêt au déploiement* qui projette la monographie — surtout les ch. 5-6 — sur une entreprise fictive, la **Coopérative financière Boréalis**, et une **pile IBM consolidée** (v2.2, 7 juillet 2026).

**Insight directeur** : le système n'est pas une plateforme d'agents à gouverner après coup, mais un **plan de contrôle obligatoire** couplé à une **dorsale d'intégration tri-plan** — synchrone requête/réponse, asynchrone événementiel, commande transactionnelle assurée *exactly-once* —, chacun assigné à la classe d'interaction qu'il sert et **non interchangeable**. En une phrase : *l'agent prépare ; un humain ou un contrôle déterministe engage l'irréversible ; toute action transite par un point d'application de politique unique ; tout actif décisionnel est un modèle inventorié.*

Le revers est assumé plutôt que tu : la consolidation IBM maximise la cohérence au prix d'un *vendor lock-in* et d'une dépendance à un tiers TIC critique (CTPP). Le garde-fou est de **maintenir ouvertes les coutures de protocole** — MCP, A2A, ISO 20022, OpenTelemetry GenAI, poids ouverts, échange ArchiMate — pour qu'un changement de fournisseur ne soit jamais une réécriture (tranché en ADR-001).

Sections : §0 Résumé exécutif ; §0.1 Blueprint consolidé — vue d'ouverture ; §0.2 Blueprint EA détaillé — jeu de vues ArchiMate ; §1 Périmètre, hypothèses et invariants ; §2 Vue d'ensemble de la pile ; §3 Plan de contrôle agentique ; §4 Dorsale d'intégration tri-plan *(cœur)* ; §5 Architecture de données et grounding sémantique ; §6 Architecture de sécurité ; §7 Traçabilité réglementaire et résidence ; §8 Architecture physique et topologie ; §9 Exigences non fonctionnelles et SLO ; §10 Modèle opérationnel, observabilité et FinOps ; §11 Stratégie de test et de validation ; §12 Parc d'agents par sous-domaine (autonomie calibrée) ; §13 Projection ArchiMate ; §14 Plan de déploiement par plateaux et runbooks ; §15 Registre des ADR ; §16 Compromis, risques et conditions de renversement ; §17 Réserves de qualification. Sous-annexes **A-F** : inventaire produit, matrice de traçabilité, catalogue des diagrammes, index des configurations, glossaire, sources.

⚠ **Piège de numérotation à ne jamais confondre** — trois homonymies :
- le **§6 de l'ADS** (sécurité) ≠ le **ch. 6** de la monographie (ArchiMate) ;
- l'**Annexe B *interne* de l'ADS** (matrice de traçabilité) ≠ l'**Annexe B de la monographie** (= l'ADS entière) ;
- les renvois de l'ADS vers le corps doctrinal restent **explicites** : `cf. Monographie ch.6 §6.1.3`.

*Conventions propres : diagrammes **Mermaid inline** (aucun fichier image séparé), légendés `**Figure N — …**`, devant passer `mmdc` ; vues en **ArchiMate 4**, équivalent 3.2 noté si requis ; extraits de configuration **illustratifs** — jamais de secret réel ; valeurs chiffrées (SLO, RPO/RTO, débits) = hypothèses à calibrer.*

---

## Livrables associés (hors `Monographie.md`)

| Livrable | Ce qu'il est | Numérotation |
|---|---|---|
| [`Synthese Monographie.md`](../Synthese%20Monographie.md) → **69 p.** | Article de synthèse **autonome** — revue condensée au format académique, 12 sections + bibliographie propre, même pipeline FESP, sans diagramme | **§3-§12 — distincte de celle de la monographie.** C'est cette numérotation que citent les Vol. II et III (tableau 15 §11.6, §11.5, §10) |
| [`Borealis-Go/`](../Borealis-Go/) | Démonstrateur **MCP + A2A** (pré-qualification de crédit) matérialisant le PRD : 9 binaires, 12 ADR. Audit 27/27, gate vert à 96,2 % | Régi par son propre [`CLAUDE.md`](../Borealis-Go/CLAUDE.md), qui **prime dans son répertoire** |

⚠ **La veille technologique n'est pas un livrable de ce volume.** Déplacée à la racine du dépôt (`Veille Technologique.md`, éd. du 18 juillet 2026), elle couvre les trois volumes et cite le Vol. I en §4.12 (démonstrateur `Borealis-Go`, réf. [217]). Ses conventions et sa chaîne de rendu relèvent du [`CLAUDE.md` du dépôt](../../../CLAUDE.md).
