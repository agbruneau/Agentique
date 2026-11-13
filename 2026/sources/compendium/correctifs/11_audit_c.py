"""Correctifs de l'audit du 11 novembre 2026, lot « comp-c » (Compendium, ch. 37 à 50, annexes B, I, N : K08, K09, K10, K11, K12, V2, X1, L08 à L11, coquilles).

Complète 03_livres3_4_5.py et 08_annexes.py : seuls figurent ici les constats que ces modules
laissaient entiers ou à moitié réglés. Chaque passage d'origine porte sur le corps déjà corrigé
(modules 01 à 03, 08, 09 et 10 appliqués avant celui-ci).
"""

CORRECTIONS = [
    # =========================================================================
    # CH. 43 : zones de compensation et points de contrôle (K09-03)
    # =========================================================================

    # K09-03 — le § 43.3 numérotait les zones autrement que le Tableau 42.2 (Z4 = interface d'accès, Z5 = contenu et état)
    ("quatre de ces points correspondent aux quatre premières zones de compensation du ch.\xa042 (Z1 → PC2, Z2 → PC3, Z3 → PC4, Z4 → PC1), chacune assignée à la couche qui doit la porter ; la cinquième zone du ch.\xa042 — l'interface d'accès du cadre bancaire (Z5) — ne devient pas un point de contrôle, faute d'objet (<em>aucun organisme de normalisation technique n'a été désigné et aucun standard n'est nommé dans les textes officiels</em>), mais <strong>une frontière d'abstraction</strong> (§ 43.6). Le cinquième point (PC5, confinement local) est issu de la table de traduction du ch.\xa029 (§ 29.1). Total : cinq.</p>",
     "trois de ces points correspondent aux trois premières zones de compensation du ch.\xa042 (Z1 → PC2, Z2 → PC3, Z3 → PC4), chacune assignée à la couche qui doit la porter ; la quatrième zone du ch.\xa042 — l'interface d'accès du cadre bancaire (Z4) — ne devient pas un point de contrôle, faute d'objet (<em>aucun organisme de normalisation technique n'a été désigné et aucun standard n'est nommé dans les textes officiels</em>), mais <strong>une frontière d'abstraction</strong> (§ 43.6). Les deux autres ne se lisent pas zone par zone : PC1 (l'événement de décision, tiré de l'art. 12.1) n'a pas de ligne au Tableau 42.2, et PC5 (confinement local) est issu de la table de traduction du ch.\xa029 (§ 29.1), le Tableau 42.2 en portant le principe à sa cinquième ligne (Z5, le contenu et l'état). Total : cinq.</p>",
     'K09-03a'),
    ("La frontière d'abstraction, elle, est la cinquième zone du ch.\xa042 — celle qui n'est pas devenue un point de contrôle.",
     "La frontière d'abstraction, elle, est la quatrième zone du ch.\xa042 (Z4) — celle qui n'est pas devenue un point de contrôle.",
     'K09-03b'),
    ("émises par l&#x27;orchestration (zone Z4, art. 12.1). PC2",
     "émises par l&#x27;orchestration (art. 12.1). PC2",
     'K09-03c'),

    # =========================================================================
    # CH. 44 : Tableau 44.1 (K09-18)
    # =========================================================================

    # K09-18 — ni le § 43.5.3 ni le § 46.1 n'emploient <<maturity-gap>> ou <<KPI>>
    ("<td>§ 44.4, <strong>ch.\xa043</strong> § 43.5.3, <strong>ch.\xa046</strong> § 46.1</td>",
     "<td>§ 44.1.1 (les trois substitutions), § 44.4 (<code>&lt;&lt;Contract&gt;&gt;</code>) ; <code>&lt;&lt;maturity-gap&gt;&gt;</code> et <code>&lt;&lt;KPI&gt;&gt;</code> n'ont pas de siège d'emploi ailleurs dans la somme</td>",
     'K09-18'),

    # =========================================================================
    # CH. 43 et 45 : convention de nomination des éditeurs (K09-21)
    # =========================================================================

    # K09-21 — § 43.6 : les trois réalisations d'orchestration, nommées comme au ch. 23 (neutralité : nommer sans recommander)
    ("<em>un cadriciel d'éditeur en disponibilité générale depuis une date nommée, portant les flux à base de graphes, les points de contrôle et l'humain dans la boucle</em> (Vol. II <strong>F-15</strong>) ; <em>une plateforme dont le support d'un protocole n'est confirmé de première main que pour son offre commerciale, non pour sa bibliothèque ouverte</em> (Vol. II <strong>F-32</strong>) ; <em>une orchestration événementielle dont les capacités agentiques déclarent un appel d'outils natif et une intégration en</em>",
     "<em>le cadriciel d'éditeur Microsoft Agent Framework, en disponibilité générale (version 1.0) depuis le 3 avril 2026, portant les flux à base de graphes, les points de contrôle et l'humain dans la boucle</em> (Vol. II <strong>F-15</strong>) ; <em>LangGraph Platform (disponibilité générale le 14 mai 2025, renommée LangSmith Deployment en octobre 2025), dont le support d'un protocole n'est confirmé de première main que pour son offre commerciale, non pour sa bibliothèque ouverte</em> (Vol. II <strong>F-32</strong>) ; <em>l'orchestration événementielle de Confluent, annoncée en août 2025, dont les capacités agentiques déclarent un appel d'outils natif et une intégration en</em>",
     'K09-21a'),
    # K09-21 — § 45.5 : la passerelle d'API est nommée et datée comme au Tableau 45.2 (C1)
    ("<em>une passerelle d'API en version majeure datée, avec cycle de vie, portail développeur et famille de passerelles.</em>",
     "<em>IBM API Connect, en version 10.0.8 (mai 2024), avec cycle de vie, portail développeur et famille de passerelles.</em>",
     'K09-21b'),
    # K09-21 — Tableau 45.1 (ligne 6) : produit et date nommés comme au Tableau 45.2 (C6)
    ("un produit de gouvernance <strong>en disponibilité générale</strong> depuis une date nommée, et sa gouvernance agentique livrée en 2025",
     "<strong>IBM watsonx.governance</strong> <strong>en disponibilité générale</strong> depuis décembre 2023, et sa gouvernance agentique livrée en 2025",
     'K09-21c'),
    # K09-21 — Tableau 45.3 : les « dates nommées » sont écrites (jalons de l'entrée S-043 reconstatés au ch. 33)
    ("<em>l'éditeur est partenaire technologique des deux rails à des dates nommées</em>",
     "<em>l'éditeur est partenaire technologique des deux rails</em> — jalons datés de l'entrée S-043 : sélection pour le rail de grande valeur le 2 mai 2019, lancement de ce rail le 1ᵉʳ septembre 2021, centre de données additionnel annoncé le 16 octobre 2023",
     'K09-21d'),
    # K09-21 — § 45.9 (Migrer) : le gestionnaire de files est nommé et sa version écrite
    ("<em>un gestionnaire de files du portefeuille déclare une cryptographie post-quantique pour le transport, à une version datée</em>",
     "<em>IBM MQ, gestionnaire de files du portefeuille, déclare une cryptographie post-quantique pour le transport, pour la ligne 9.4 LTS (disponibilité générale le 18 juin 2024 ; 9.4.3 en 2025)</em>",
     'K09-21e'),

    # =========================================================================
    # CH. 45 : codes internes, statut de Boréalis, décomptes (K09-26, K09-28, K09-30, K09-31, K09-32)
    # =========================================================================

    # K09-26 — « CA-8 » : code de production jamais défini
    ("CA-8 hérité : chaque lien porte son statut — et un seul est documenté, pour un rôle opérationnel.",
     "Règle héritée : chaque lien porte son statut — et un seul est documenté, pour un rôle opérationnel.",
     'K09-26a'),
    ("CA-8 : chaque lien porte son statut, et le seul lien documenté porte sur un rôle opérationnel",
     "Règle héritée : chaque lien porte son statut, et le seul lien documenté porte sur un rôle opérationnel",
     'K09-26b'),
    # K09-26 — « enveloppe dérivée » : terme de production jamais défini (retiré)
    ("Quatrième chapitre du mouvement, et celui dont l'enveloppe dérivée est la plus haute du Livre : il instancie",
     "Quatrième chapitre du mouvement : il instancie",
     'K09-26c'),

    # K09-28 — Boréalis : le cumul des statuts fédéral et provincial est posé comme hypothèse de travail
    ("voir Tableau 43.3)</em> (Vol. III <strong>H-32</strong>, <strong>[C]</strong>).</p>",
     "voir Tableau 43.3)</em> (Vol. III <strong>H-32</strong>, <strong>[C]</strong>). Le cumul des deux statuts — institution financière fédérale et assujettie à l'autorité provinciale — est une hypothèse de travail du cas fictif : le montage juridique qui le permettrait n'est pas précisé, et la somme ne le tranche pas.</p>",
     'K09-28'),

    # K09-30 — les six gestes ont tous un siège ailleurs : le décompte 4 + 1 + 1 n'était pas une partition
    ("<em>des six gestes de la vie d'un agent, quatre ont un siège ailleurs dans la somme, un est outillé à moitié, et un ne l'est que par une annonce d'éditeur.</em>",
     "<em>des six gestes de la vie d'un agent, tous ont un siège ailleurs dans la somme : trois y sont traités en entier (vérifier par arête, tracer, évaluer), un est repris ici (déléguer), un n'est outillé qu'à moitié (renouveler), et un ne tient ici qu'à une annonce d'éditeur (migrer).</em>",
     'K09-30a'),
    ("<em>Des six gestes de la vie d'un agent, quatre ont un siège ailleurs, un est outillé à moitié, un ne l'est que par une annonce.</em>",
     "<em>Des six gestes de la vie d'un agent, tous ont un siège ailleurs : trois y sont traités en entier, un est repris ici, un n'est outillé qu'à moitié, un ne tient ici qu'à une annonce.</em>",
     'K09-30b'),

    # K09-31 — le positionnement de l'agent observateur n'est pas « sans ambiguïté » : la taxonomie OO ne le prévoit pas
    ("Et le positionnement qui en découle est le seul du chapitre qui ne soit pas ambigu : <em>un agent qui observe",
     "Et le positionnement qui en découle reste une lecture d'auteur, que la taxonomie ne tranche pas : <em>un agent qui observe",
     'K09-31a'),
    ("— mais le socle ne porte toujours aucun positionnement, et <em>cette lecture-ci est d'auteur comme les autres.</em></p>",
     "— mais la taxonomie OO1-OO4 ne prévoit aucune position pour un agent qui ne commande rien et n'est commandé par aucun enchaînement (le Tableau 45.2 range le rail déterministe en OO3 et les agents événementiels sans cadre explicite en OO1, ligne C3), le socle ne porte toujours aucun positionnement, et <em>cette lecture-ci est d'auteur comme les autres.</em></p>",
     'K09-31b'),

    # K09-32 — l'exemple ne situe explicitement que le point d'arrêt humain (PC3)
    ("il montre que les cinq points de contrôle obligatoires du ch.\xa043 § 43.3 ont chacun un lieu dans un modèle, <em>ce qui est une propriété du formalisme et non une propriété du système modélisé.</em> La variante en sinistres ne change ni les patrons ni les points de contrôle — <em>et c'est ce qu'elle est censée montrer.</em>",
     "il montre que le point d'arrêt humain (PC3), l'un des cinq points de contrôle obligatoires du ch.\xa043 § 43.3, a un lieu dans un modèle — le niveau Business, par Assignment —, <em>ce qui est une propriété du formalisme et non une propriété du système modélisé.</em> L'exemple ne situe pas explicitement les quatre autres (PC1, PC2, PC4, PC5) : la preuve de leur place dans un modèle reste à faire. La variante en sinistres ne change ni les patrons ni le point de contrôle situé — <em>et c'est ce qu'elle est censée montrer.</em>",
     'K09-32'),

    # =========================================================================
    # CH. 43 et 46 : renvoi à la lecture des quatre propriétés démontrables (K09-34)
    # =========================================================================

    # K09-34 — le § 43.3 ne citait pas le § 22.2 ni le § 39.2.3 : le renvoi est posé des deux côtés
    ("propriété que le Livre III nomme. Quatre des cinq propriétés",
     "propriété que le Livre III nomme (lecture posée au ch.\xa022 § 22.2, siège). Quatre des cinq propriétés",
     'K09-34a'),
    ("constat repris au <strong>ch.\xa039 § 39.2</strong>, siège). <em>Les cinq points relèvent tous",
     "constat repris au <strong>ch.\xa039 § 39.2.3</strong>, siège). <em>Les cinq points relèvent tous",
     'K09-34b'),

    # =========================================================================
    # CH. 46 : jalons externes (K09-36)
    # =========================================================================

    # K09-36 — un jalon est survenu (révision du protocole agent-outil, 28 juillet 2026) : la lecture et la synthèse le disent
    ("Les cinq autres sont des états d'attente — et un programme séquencé sur des états d'attente n'a qu'un seul point d'ancrage.</em>",
     "Un est survenu depuis le gel (la révision majeure du protocole agent-outil, le 28 juillet 2026) ; les quatre autres sont des états d'attente — et un programme séquencé sur des états d'attente n'a qu'un seul point d'ancrage.</em> Le tableau tient l'état du gel et date ce qui est survenu depuis ; l'annexe N en reprend le détail, dont celui du rail temps réel (règlement administratif en vigueur le 24 août 2026, lancement non survenu).",
     'K09-36a'),
    ("<em>Un seul est</em> <strong><em>PROGRAMMÉ</em></strong><em>.</em> Le ch.\xa050 en est le siège",
     "<em>Un seul est</em> <strong><em>PROGRAMMÉ</em></strong><em> à date fixe ; un est survenu depuis le gel (28 juillet 2026) ; les quatre autres sont des états d'attente.</em> Le ch.\xa050 en est le siège",
     'K09-36b'),

    # =========================================================================
    # CH. 47 : Tableau 47.2 et intertitres des mouvements (K09-38, K09-54)
    # =========================================================================

    # K09-38 — le tableau porte des compléments datés du 30 juillet 2026 : on ne dit plus « sans en ajouter ni en retirer »
    ("Le tableau ci-dessous les reprend avec leurs réserves d'origine, sans en ajouter ni en retirer.",
     "Le tableau ci-dessous les reprend avec leurs réserves d'origine et les compléments datés qu'il indique (précisions et réserves levées au 30 juillet 2026).",
     'K09-38'),

    # K09-54 — le premier mouvement du ch. 47 reçoit un intertitre, comme le second
    ("</em> : les deux sont reprises comme <strong>programme de travail</strong>.</p>\n<h3>47.1 L'agent comme artefact composé</h3>",
     "</em> : les deux sont reprises comme <strong>programme de travail</strong>.</p>\n<h3>Premier mouvement — La provenance des composants : de quoi un agent est fait</h3>\n<h3>47.1 L'agent comme artefact composé</h3>",
     'K09-54'),
    # =========================================================================
    # CH. 12 à 47 : un seul terme pour le champ permissionBoundaries (K09-43)
    # =========================================================================

    # K09-43 — « bornes de privilège » est le terme de la grille du ch. 14 : il remplace « bornes de portée », « limites de portée » et « bornes de permission »
    ("qui portent les limites de portée (Vol. III F-40, <strong>[B]</strong>).",
     "qui portent les bornes de privilège (Vol. III F-40, <strong>[B]</strong>).",
     'K09-43a'),
    ("qui portent les limites de portée (Vol. III F-40, <strong>[B]</strong> ;",
     "qui portent les bornes de privilège (Vol. III F-40, <strong>[B]</strong> ;",
     'K09-43b'),
    ("Deux champs obligatoires portent les outils invocables et les limites de portée (F-40,",
     "Deux champs obligatoires portent les outils invocables et les bornes de privilège (F-40,",
     'K09-43c'),
    ("la liste des outils invocables et les bornes de portée (F-40, <strong>[B]</strong>)",
     "la liste des outils invocables et les bornes de privilège (<code>permissionBoundaries</code>, F-40, <strong>[B]</strong>)",
     'K09-43d'),
    ("<code>permissionBoundaries</code> — qui porte les limites de portée — parmi les",
     "<code>permissionBoundaries</code> — qui porte les bornes de privilège — parmi les",
     'K09-43e'),
    ("énumération des outils invocables, limites de portée (Vol. III <strong>F-40</strong>, [B])",
     "énumération des outils invocables, bornes de privilège (<code>permissionBoundaries</code> ; Vol. III <strong>F-40</strong>, [B])",
     'K09-43f'),
    ("énumération d'outils invocables, bornes de privilège (Vol. II <strong>F-08</strong>",
     "énumération d'outils invocables, bornes de privilège (<code>permissionBoundaries</code> ; Vol. II <strong>F-08</strong>",
     'K09-43g'),
    ("<em>l'énumération des outils invocables et les bornes de portée</em>",
     "<em>l'énumération des outils invocables et les bornes de privilège (<code>permissionBoundaries</code>)</em>",
     'K09-43h'),
    ("l'inscription au registre porte des outils invocables et des bornes de portée, la chaîne",
     "l'inscription au registre porte des outils invocables et des bornes de privilège (<code>permissionBoundaries</code>), la chaîne",
     'K09-43i'),
    ("deux champs obligatoires portant les outils invocables et les limites de portée, sur un dispositif",
     "deux champs obligatoires portant les outils invocables et les bornes de privilège, sur un dispositif",
     'K09-43j'),
    ("porte donc ses bornes de permissions : des bornes sont déclarées",
     "porte donc ses bornes de privilège : des bornes sont déclarées",
     'K09-43k'),
    ("le détail complet des bornes de permission sont exclus",
     "le détail complet des bornes de privilège sont exclus",
     'K09-43l'),
    ("champs obligatoires d'accès aux outils et de bornes de permission (F-40,",
     "champs obligatoires d'accès aux outils et de bornes de privilège (F-40,",
     'K09-43m'),

    # =========================================================================
    # CH. 46 et 48 : renvois, antécédents et état (K09-47, K09-49)
    # =========================================================================

    # K09-47 — le document IETF sur les clés de requête est identifié au § 48.5; la révision du protocole agent-outil est publiée
    ("<em>le document de l'IETF sur les clés de requête (« Idempotency-Key ») n'est nommé par aucun chapitre ni par aucune relève : son identifiant est à établir à l'ouverture de l'instruction, et cet établissement en est le premier acte</em>",
     "<em>le document de l'IETF sur les clés de requête (« Idempotency-Key »), identifié au § 48.5 (<code>draft-ietf-httpapi-idempotency-key-header</code>, révision <code>-07</code> du 15 octobre 2025, expiré le 18 avril 2026) : son état à la date de l'instruction est à relever à l'ouverture, et ce relevé en est le premier acte</em>",
     'K09-47a'),
    ("Une révision majeure du protocole agent-outil est annoncée au brouillon — dont la date n'est pas confirmée à la source — et tout constat",
     "Une révision majeure du protocole agent-outil avait été annoncée au brouillon — sa date n'était pas confirmée à la source — et tout constat",
     'K09-47b'),

    # K09-49 — antécédents et jargon : « même état », « adverse », « relève », « ce chapitre en est le siège », « elle se reconstruit »
    ("leurs trois cibles sont désormais dans le MÊME état — ce qui déplace la réserve sans la lever.",
     "leurs trois cibles sont désormais toutes trois rédigées — ce qui déplace la réserve sans la lever : la matière existe ailleurs, la confrontation reste à conduire.",
     'K09-49a'),
    ("Une préimpression adverse de mai 2026 tient la détection",
     "Une préimpression de mai 2026 tient la détection",
     'K09-49b'),
    ("(relève le § 48.2)",
     "(prolonge le § 48.2)",
     'K09-49c'),
    ("(relève le § 48.4 et la question propre de cette section)",
     "(prolonge le § 48.4 et la question propre de cette section)",
     'K09-49d'),
    ("Elle recoupe les événements de péremption du ch.\xa050 sans les reconstruire — <em>ce chapitre en est le siège.</em>",
     "Elle recoupe les événements de péremption du ch.\xa050 sans les reconstruire — <em>le ch.\xa050 en est le siège.</em>",
     'K09-49e'),
    ("jamais des sources ; <em>elle se reconstruit sur le principe hérité seul.</em>",
     "jamais des sources ; <em>la section se reconstruit sur le principe hérité seul.</em>",
     'K09-49f'),
    # =========================================================================
    # ANNEXE I : références (K11-02, K11-05, K11-21, K11-24, K11-31, K11-34, K11-39) et V2-16
    # =========================================================================

    # K11-31 — SR 11-7 : émetteurs de 2011 = Réserve fédérale et OCC; la FDIC l'a adoptée le 7 juin 2017 (FDIC, FIL-22-2017)
    ("<li>Board of Governors of the Federal Reserve System, OCC &amp; FDIC (2011). <em>Supervisory Guidance on Model Risk Management</em>. SR 11-7 / OCC Bulletin 2011-12, 4 avril 2011 ; remplacé par <em>Revised Guidance</em> (SR 26-2 / OCC Bulletin 2026-13), 17 avril 2026. https://www.occ.gov/news-issuances/news-releases/2011/nr-ia-2011-39.html — cf.\xa0§5.3, §5.4, §5.7 — cf.\xa0§5.3, §5.4, §5.7</li>",
     "<li>Board of Governors of the Federal Reserve System &amp; OCC (2011). <em>Supervisory Guidance on Model Risk Management</em>. SR 11-7 / OCC Bulletin 2011-12, 4 avril 2011 ; adoptée par la FDIC le 7 juin 2017 (FIL-22-2017, https://www.fdic.gov/news/financial-institution-letters/2017/fil17022.html) ; remplacée par <em>Revised Guidance</em> (SR 26-2 / OCC Bulletin 2026-13), 17 avril 2026. https://www.occ.gov/news-issuances/news-releases/2011/nr-ia-2011-39.html — cf.\xa0§5.3, §5.4, §5.7</li>",
     'K11-31'),

    # K11-39 — sources secondaires rangées sous l'auteur réel (Klover.ai, PYMNTS.com), à leur place alphabétique
    ("<li><strong>Fiserv (analyse Klover.ai) (2025).</strong> <em>Fiserv deploying agentic AI via UiPath partnership.</em> À recouper avec les communiqués Fiserv primaires. https://www.klover.ai/fiserv-ai-strategy-analysis-of-dominance-in-fintech-payments-ai/ — cf.\xa0§5.11, §5.12.2</li>\n",
     "",
     'K11-39a'),
    ("<li>Knublauch, H.; Kontokostas, D. (Eds.) (2017).",
     "<li><strong>Klover.ai (2025).</strong> <em>Fiserv deploying agentic AI via UiPath partnership</em> (analyse tierce portant sur Fiserv, non un document de Fiserv ; à recouper avec les communiqués primaires de Fiserv). https://www.klover.ai/fiserv-ai-strategy-analysis-of-dominance-in-fintech-payments-ai/ — cf.\xa0§5.11, §5.12.2</li>\n<li>Knublauch, H.; Kontokostas, D. (Eds.) (2017).",
     'K11-39b'),
    ("<li><strong>FS-ISAC / FIS (2026).</strong> <em>FIS and Anthropic Collaborate to Enable Agent-First Banks (analyse partenariat ; AML de jours en minutes).</em> PYMNTS.com, mai 2026 (préférer le communiqué FIS primaire). https://www.pymnts.com/artificial-intelligence-2/2026/fis-and-anthropic-collaborate-to-enable-agent-first-banks/ — cf.\xa0§5.5, §5.7, §5.11</li>\n",
     "",
     'K11-39c'),
    ("<li>Qian, C.; Liu, W.",
     "<li><strong>PYMNTS.com (2026).</strong> <em>FIS and Anthropic Collaborate to Enable Agent-First Banks</em> (analyse du partenariat ; AML de jours en minutes ; source secondaire, non de FS-ISAC ni de FIS : le communiqué primaire de FIS, du 4 mai 2026, est rangé sous FIS / Anthropic). Mai 2026. https://www.pymnts.com/artificial-intelligence-2/2026/fis-and-anthropic-collaborate-to-enable-agent-first-banks/ — cf.\xa0§5.5, §5.7, §5.11</li>\n<li>Qian, C.; Liu, W.",
     'K11-39d'),

    # K11-21 — MITRE ATLAS : la version courante est celle que dit le corps (v2026.09), non v2026.05
    ("Origine 2020 (Adversarial ML Threat Matrix) ; version courante v2026.05 (27 mai 2026). https://atlas.mitre.org/.",
     "Origine 2020 (Adversarial ML Threat Matrix) ; collection 2026.06 (modifiée le 27 mai 2026, publiée le 30 juin 2026), puis v2026.09 (15 septembre 2026), courante au 23 octobre 2026. https://atlas.mitre.org/.",
     'K11-21'),

    # K11-34 — lettres d'année : toute entrée ambiguë reçoit la première lettre libre; les renvois du corps suivent
    ("<li>Anthropic (2024). <em>Introducing the Model Context Protocol</em>",
     "<li>Anthropic (2024c). <em>Introducing the Model Context Protocol</em>",
     'K11-34a'),
    ("<li>Anthropic (2024). <em>Messages API</em>",
     "<li>Anthropic (2024d). <em>Messages API</em>",
     'K11-34b'),
    ("<li><strong>OpenAI (2024).</strong> <em>Klarna's AI assistant",
     "<li><strong>OpenAI (2024c).</strong> <em>Klarna's AI assistant",
     'K11-34c'),
    ("<li><strong>OpenAI (2024).</strong> <em>Morgan Stanley uses AI evals",
     "<li><strong>OpenAI (2024d).</strong> <em>Morgan Stanley uses AI evals",
     'K11-34d'),
    ("<li>OpenAI (2025). <em>Responses API</em>",
     "<li>OpenAI (2025g). <em>Responses API</em>",
     'K11-34e'),
    ("<li><strong>Bank of England / FPC (2025).</strong>",
     "<li><strong>Bank of England / FPC (2025a).</strong>",
     'K11-34f'),
    ("<p>Anthropic (2025) présente l'ensemble de ces opérations",
     "<p>Anthropic (2025c) présente l'ensemble de ces opérations",
     'K11-34g'),
    ("documentée par Anthropic (2025) — l'<strong>édition de contexte</strong>",
     "documentée par Anthropic (2025e) — l'<strong>édition de contexte</strong>",
     'K11-34h'),
    ("d'Anthropic (2025) instrumente ce dernier plan",
     "d'Anthropic (2025e) instrumente ce dernier plan",
     'K11-34i'),
    ("(OpenAI, 2024) — un sous-ensemble de 500 tâches",
     "(OpenAI, 2024a) — un sous-ensemble de 500 tâches",
     'K11-34j'),
    ("(dichotomie popularisée par Anthropic, 2024)",
     "(dichotomie popularisée par Anthropic, 2024a)",
     'K11-34k'),
    ("est celle d'Anthropic (2024, § 4.1.1)</em>, reprise depuis",
     "est celle d'Anthropic (2024a, § 4.1.1)</em>, reprise depuis",
     'K11-34l'),

    # K11-02 — quatre paires qui désignent le même document sont fondues (OASIS UDDI, FOCUS 1.4, OWASP NHI Top 10, communiqué Visa du 14 octobre 2025)
    ("<li>OASIS UDDI Specification TC (2004). <em>UDDI Version 3.0.2</em> (ratifié OASIS Standard fév. 2005). https://oasis-open.org/committees/uddi-spec/doc/spec/v3/uddi-v3.0.2-20041019.htm.</li>\n",
     "",
     'K11-02a'),
    ("<li>Linux Foundation / FinOps Foundation (2026). <em>FOCUS (FinOps Open Cost and Usage Specification) 1.4</em> (économie des jetons scopée pour 1.5). Ratifiée le 4 juin 2026. https://www.finops.org/insights/introducing-focus-1-4/.</li>\n",
     "",
     'K11-02b'),
    ("Ratifiée 4.6.2026. https://focus.finops.org/focus-specification/ — cf.\xa0§5.6, §5.11</li>",
     "Ratifiée 4.6.2026 (économie des jetons scopée pour 1.5 ; annonce : https://www.finops.org/insights/introducing-focus-1-4/). https://focus.finops.org/focus-specification/ — cf.\xa0§5.6, §5.11</li>",
     'K11-02c'),
    ("<li>OWASP Non-Human Identities Top 10 Project (2025). <em>OWASP Non-Human Identities Top 10 — 2025</em>. OWASP Foundation (NHI1 Improper Offboarding, NHI2 Secret Leakage, NHI5 Overprivileged NHI…). https://owasp.org/www-project-non-human-identities-top-10/2025/.</li>\n",
     "",
     'K11-02d'),
    ("<li>Visa (avec Cloudflare) (2025). <em>Visa Introduces Trusted Agent Protocol</em> (HTTP Message Signatures, aligné sur Web Bot Auth (Cloudflare) ; « Agent Intent »). Newsroom, 14 oct. 2025. https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html.</li>\n",
     "",
     'K11-02e'),
    ("<em>Visa Introduces Trusted Agent Protocol: An Ecosystem-Led Framework for AI Commerce.</em> 14.10.2025. https://investor.visa.com/",
     "<em>Visa Introduces Trusted Agent Protocol: An Ecosystem-Led Framework for AI Commerce</em> (HTTP Message Signatures, aligné sur Web Bot Auth (Cloudflare) ; « Agent Intent » ; même communiqué sur le site de presse de Visa : https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html). 14.10.2025. https://investor.visa.com/",
     'K11-02f'),
    ("<td>Doublons résiduels d’adresse ou d’intitulé fondus à la révision du 12 novembre 2026</td><td><strong>−\xa062</strong></td></tr><tr><td><strong>Entrées uniques de la présente annexe (§\xa0I.1)</strong></td><td><strong>1\xa0003</strong></td></tr>",
     "<td>Doublons résiduels d’adresse ou d’intitulé fondus à la révision du 12 novembre 2026</td><td><strong>−\xa062</strong></td></tr><tr><td>Doublons résiduels (même document sous deux adresses ou deux auteurs) fondus à la relecture du 13 novembre 2026</td><td><strong>−\xa04</strong></td></tr><tr><td><strong>Entrées uniques de la présente annexe (§\xa0I.1)</strong></td><td><strong>999</strong></td></tr>",
     'K11-02g'),
    ("(<strong>1\xa0003 entrées uniques</strong> après les passes de nettoyage et de dédoublonnage des 29 octobre et 12 novembre 2026)",
     "(<strong>999 entrées uniques</strong> après les passes de nettoyage et de dédoublonnage des 29 octobre, 12 et 13 novembre 2026)",
     'K11-02h'),
    ("— 1\xa0003 notices uniques</td>",
     "— 999 notices uniques</td>",
     'K11-02i'),
    ("conduisant aux 1\xa0003 notices uniques de la section\xa0I.1.",
     "conduisant aux 999 notices uniques de la section\xa0I.1.",
     'K11-02j'),

    # K11-05 — « une » bibliographie, « trois » et « sept » : l'annexe réunit les sept bibliographies du Vol. I
    ("le Vol. I fournit une bibliographie parce qu'il en tient une ; les deux autres n'en fournissent aucune parce qu'ils n'en tiennent pas. <em>L'annexe ne réunit donc pas trois bibliographies — elle en réunit une, et constate l'absence des deux autres. (b)</em>",
     "le Vol. I fournit ses bibliographies parce qu'il en tient ; les deux autres n'en fournissent aucune parce qu'ils n'en tiennent pas. <em>L'annexe ne réunit donc pas une bibliographie par volume : elle réunit les sept bibliographies du Vol. I, et constate que les Vol. II et III n'en tiennent aucune. (b)</em>",
     'K11-05'),

    # K11-24 — « gel » : le corps est gelé au 27 juillet, l'annexe est assemblée le 30 juillet
    ("ne rendait, au gel du 30 juillet 2026, <strong>qu'une seule adresse isolée",
     "ne rendait, à l'assemblage du 30 juillet 2026 (corps gelé au 27 juillet 2026), <strong>qu'une seule adresse isolée",
     'K11-24a'),
    ("<p><em>Annexe assemblée le 30 juillet 2026.</em></p>",
     "<p><em>Annexe assemblée le 30 juillet 2026 (corps gelé au 27 juillet 2026) ; nettoyage du 29 octobre et révisions des 12 et 13 novembre 2026 : voir le tableau I.2.</em></p>",
     'K11-24b'),

    # L11-14 — gras / romain : le régime est dit à l'entrée de la section I.1
    ("renvoient à la numérotation interne de ce volume source, non aux chapitres 1 à 50 du Compendium.</em></p>",
     "renvoient à la numérotation interne de ce volume source, non aux chapitres 1 à 50 du Compendium. En règle générale, le nom de l'auteur est en gras lorsque la notice porte un renvoi « cf. § » et en romain dans le cas contraire : c'est un reste de composition du volume source, sans valeur de classement.</em></p>",
     'L11-14'),

    # V2-16 — les deux derniers pictogrammes ⚖ (§ 49.12.2) sont remplacés par la mention textuelle
    ("⚖ vote dû, non conduit",
     "marquée <em>vote dû, non conduit</em>",
     'V2-16', '*'),
    # =========================================================================
    # LOT L (relecture du 11 novembre) : ch. 40 à 46, annexe I, coquilles
    # =========================================================================

    # L08-10 — § 40.3 : le bloc sur S-149 et S-154 reprend son antécédent (« Elles » désignait des entrées d'un paragraphe antérieur)
    ("<p>Elles situent la question ; elles ne l'établissent pas. Et leurs états de re-datation diffèrent",
     "<p>Ces deux entrées de repérage situent la question ; elles ne l'établissent pas. Et leurs états de re-datation diffèrent",
     'L08-10'),

    # L09-06 — « ramenés à six principes » : le premier principe du Vol. III n'est pas parmi les six du Tableau 45.1
    ("(ramenés à six principes au ch.\xa045), dont le premier conditionne l'admission à un artefact que personne ne délivre",
     "(ramenés à six principes au ch.\xa045), dont le premier, non retenu parmi les six, conditionne l'admission à un artefact que personne ne délivre",
     'L09-06a'),
    ("<p>Le blueprint repose sur six principes. <em>Aucun n'est un produit",
     "<p>Le blueprint repose sur six principes — le blueprint du Vol. III en énonce huit, et la somme n'en documente pas la réduction à six, sinon que le premier des huit, celui du passeport, n'en fait pas partie. <em>Aucun n'est un produit",
     'L09-06b'),
    ("<p>Et le premier principe touche un objet qui n'existe pas. <em>Le blueprint du Vol. III pose, lui, que rien",
     "<p>Et le premier principe du blueprint du Vol. III, qui n'est pas l'un des six du Tableau 45.1, touche un objet qui n'existe pas. <em>Ce blueprint pose, lui, que rien",
     'L09-06c'),

    # L09-13 — LCIM : auteur et date de l'instrument repris, comme au Tableau 24.2 et à l'annexe I
    ("<em>— Wang, Tolk et Wang, 2009 — aux agents, et la somme",
     "<em>— Tolk et Muguira, 2003, repris par Wang, Tolk et Wang, 2009 — aux agents, et la somme",
     'L09-13'),

    # L09-11 — § 44.0.4 aligné sur le § 44.7 : deux ateliers nommés par le Vol. I (en [C]), non « la quasi-totalité »
    ("À la mi-2026, la quasi-totalité des ateliers d'architecture d'entreprise n'exporte et n'importe encore que la version 3.2 nativement, ce qui rend le blueprint du ch.\xa045 non échangeable en version de référence dans la plupart d'entre eux.",
     "À la mi-2026, deux ateliers de modélisation nommés par le Vol. I (information rapportée en [C]) n'exportent et n'importent encore que la version 3.2 nativement, ce qui rend le blueprint du ch.\xa045 non échangeable en version de référence dans ces ateliers.",
     'L09-11'),

    # L09-05 — fait négatif sur l'arrêté de désignation : daté et borné (§ 43.6 et § 45.13), comme aux ch. 32 et 42
    ("Aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; <em>la candidature d'un format d'industrie relève du</em> <strong><em>commentaire d'industrie</em></strong>, attribué comme tel. La discipline qui en découle est celle du ch.\xa032",
     "Au 16 juillet 2026 (constat rejoué le 28 juillet 2026, et aucun arrêté de désignation constaté au 21 octobre 2026, annexe N), aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans la loi ni dans le règlement prépublié ; l'existence d'un arrêté non publié à la Gazette demeure au degré 3 ; <em>la candidature d'un format d'industrie relève du</em> <strong><em>commentaire d'industrie</em></strong>, attribué comme tel. La discipline qui en découle est celle du ch.\xa032",
     'L09-05a'),
    ("<p>Le fait négatif est ici du degré le plus fort — VÉRIFIÉ : <em>aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels</em> ;",
     "<p>Le fait négatif est ici du degré le plus fort — VÉRIFIÉ, borné aux chaînes cherchées au 16 juillet 2026 (rejoué le 28 juillet ; index de la Gazette du Canada balayés jusqu'au 21 octobre 2026, annexe N) : <em>aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans la loi ni dans le règlement prépublié</em>, l'existence d'un arrêté non publié à la Gazette demeurant au degré 3 ;",
     'L09-05b'),

    # L09-07 — § 45.15 : la résidence n'a pas de ligne au Tableau 45.3 (elle est au principe 4 du Tableau 45.1)
    ("<em>Les contraintes-pivots du cas — l'article 12.1, la résidence canadienne, les lignes directrices de risque de modèle et de risque technologique, la ligne directrice IA provinciale — se retrouvent une à une dans la correspondance du § 45.4, et aucune n'y reçoit un lien documenté.</em>",
     "<em>Les contraintes-pivots du cas — l'article 12.1, les lignes directrices de risque de modèle et de risque technologique, la ligne directrice IA provinciale — se retrouvent une à une dans la correspondance du § 45.4, et aucune n'y reçoit un lien documenté ; la résidence canadienne, elle, n'y a pas de ligne : le principe 4 du Tableau 45.1 la porte (§ 45.1).</em>",
     'L09-07'),

    # L09-17 — ch. 46, ouverture : balise </p> en trop après la phrase sur les ch. 42 à 45
    ("le <strong>ch.\xa045</strong> les a instanciées.</p></p>",
     "le <strong>ch.\xa045</strong> les a instanciées.</p>",
     'L09-17'),

    # L09-10 — § 48.3 : l'unicité de « sagas » était fausse; la section est la seule à traiter la saga au grain d'une action d'agent
    ("cette section est la seule occurrence de « sagas » de toute la somme, et elle l'est au grain d'une action unique.</p>",
     "cette section est la seule de la somme qui traite la saga au grain d'une action unique d'agent ; le ch.\xa01 § 1.6.2.2 pose la saga en général, et le ch.\xa031 en emploie le patron compensatoire.</p>",
     'L09-10'),

    # COQ-Com-134 — « au multi-agents » (accord) : le singulier du nom est remplacé par une tournure au pluriel, comme l'adjectif de l'ouvrage
    ("Le surcoût propre au multi-agents s'y trouve",
     "Le surcoût propre aux systèmes multi-agents s'y trouve",
     'COQ-Com-134'),

    # COQ-Com-036 — « 3,1 M » : l'unité est « partenaires EDI préexistants » (page du produit, ibm.com/products/b2b-integration-van)
    ("partenaires commerciaux à grande échelle — de l'ordre de 3,1 M)",
     "partenaires commerciaux à grande échelle — plus de 3,1 millions de partenaires EDI préexistants, selon la page du produit)",
     'COQ-Com-036'),

    # COQ-Com-172 — doubles espaces après espace insécable (annexe I et un cas au corps)
    ("cf.\xa0 §", "cf.\xa0§", 'COQ-Com-172a', '*'),
    ("p.\xa0 ", "p.\xa0", 'COQ-Com-172b', '*'),
    ("vol.\xa0 ", "vol.\xa0", 'COQ-Com-172c', '*'),
    ("al.\xa0 — ", "al.\xa0— ", 'COQ-Com-172d'),
    ("vs.\xa0 Age", "vs.\xa0Age", 'COQ-Com-172e'),
]

JOURNAL = [
    ('Ch. 43 (§ 43.3 et § 43.6), zones de compensation et points de contrôle',
     "aligner la numérotation sur le Tableau 42.2 : l'interface d'accès du cadre bancaire est la quatrième zone (Z4), la cinquième (Z5) est « le contenu et l'état »; PC1 n'a pas de ligne au Tableau 42.2",
     'K09-03'),
    ('Ch. 44 (Tableau 44.1, ligne « Substitution d\'éléments retirés »), colonne Siège',
     "retirer les sièges § 43.5.3 et § 46.1, qui n'emploient ni <<maturity-gap>> ni <<KPI>>, et renvoyer au § 44.1.1 et au § 44.4",
     'K09-18'),
    ('Ch. 43 (§ 43.6), ch. 45 (§ 45.5, Tableaux 45.1 et 45.3, § 45.9)',
     "nommer l'éditeur et écrire les dates et versions là où le texte écrivait « datée » ou « nommée » (Microsoft Agent Framework, LangGraph Platform, Confluent, IBM API Connect, IBM watsonx.governance, IBM MQ, jalons de S-043)",
     'K09-21'),
    ('Ch. 45 (Tableau 45.3, § 45.7 en tête de chapitre)',
     "remplacer le code interne « CA-8 » par « règle héritée » et retirer le terme « enveloppe dérivée », jamais définis",
     'K09-26'),
    ('Ch. 45 (§ 45.7), cas Boréalis',
     "dire que le cumul des statuts fédéral et provincial est une hypothèse de travail du cas fictif, dont le montage juridique n'est pas précisé",
     'K09-28'),
    ('Ch. 45 (§ 45.9 et synthèse), décompte des six gestes',
     "écrire que les six gestes ont un siège ailleurs (trois traités en entier, un repris ici, un outillé à moitié, un annoncé) au lieu du partage 4 + 1 + 1",
     'K09-30'),
    ('Ch. 45 (§ 45.12), flux 2',
     "dire que le positionnement de l'agent observateur reste une lecture d'auteur que la taxonomie OO1-OO4 ne tranche pas, et l'accorder à la ligne C3 du Tableau 45.2",
     'K09-31'),
    ('Ch. 45 (§ 45.14), lecture de l\'auteur',
     "restreindre la conclusion au point d'arrêt humain (PC3), seul point situé dans l'exemple",
     'K09-32'),
    ('Ch. 43 (§ 43.3) et ch. 46 (§ 46.1.3), renvoi à la lecture des quatre propriétés démontrables',
     "poser le renvoi au ch. 22 § 22.2 (siège de la lecture) au § 43.3 et unifier le renvoi au ch. 39 § 39.2.3",
     'K09-34'),
    ('Ch. 46 (§ 46.3, lecture finale et synthèse), jalons externes',
     "compter un jalon survenu (28 juillet 2026) et quatre états d'attente, et renvoyer à l'annexe N pour le rail temps réel",
     'K09-36'),
    ('Ch. 47 (§ 47.2), introduction du Tableau 47.2',
     "dire que le tableau porte, avec les réserves d'origine, les compléments datés du 30 juillet 2026",
     'K09-38'),
    ('Ch. 47, entre l\'introduction et le § 47.1',
     "ajouter l'intertitre du premier mouvement, comme pour le second",
     'K09-54'),
    ('Ch. 12 (§ 12.6), ch. 15 (§ 15.2.4 et § 15.3.1), ch. 16 (§ 16.1), ch. 18 (§ 18.2), ch. 37 (§ 37.5.4), ch. 39 (§ 39.4), ch. 43 (§ 43.1.1), ch. 45 (§ 45.8), ch. 47 (§ 47.1 et § 47.12), champ permissionBoundaries',
     "un seul terme, « bornes de privilège » (celui de la grille du ch. 14), pour « bornes de portée », « limites de portée » et « bornes de permission »; l'identifiant anglais <code>permissionBoundaries</code> donné à la première occurrence de chaque chapitre",
     'K09-43'),
    ('Ch. 48 (§ 48.2), document de l\'IETF sur les clés de requête, et révision du protocole agent-outil',
     "dire que le document est identifié au § 48.5 (draft-ietf-httpapi-idempotency-key-header, expiré) et mettre au passé l'annonce de la révision du protocole agent-outil, publiée le 28 juillet 2026",
     'K09-47'),
    ('Ch. 46 (§ 46.3), ch. 48 (§ 48.4 et § 48.5), ch. 45 (§ 45.6)',
     "nommer l'état commun des trois cibles (rédigées), retirer « adverse », écrire « prolonge » au lieu de « relève », nommer le ch. 50 comme siège et rétablir l'antécédent « la section »",
     'K09-49'),
    ('Annexe I (I.1, entrée SR 11-7 / OCC Bulletin 2011-12)',
     "retirer la FDIC des émetteurs de 2011 (Réserve fédérale et OCC) et dater son adoption au 7 juin 2017 (FDIC, FIL-22-2017); retirer le renvoi répété",
     'K11-31'),
    ('Annexe I (I.1, entrées Fiserv / Klover.ai et FS-ISAC / FIS / PYMNTS.com)',
     "ranger les deux sources secondaires sous leur auteur réel (Klover.ai, PYMNTS.com), à leur place alphabétique, avec renvoi au communiqué primaire de FIS",
     'K11-39'),
    ('Annexe I (I.1, entrée MITRE ATLAS)',
     "remplacer « version courante v2026.05 » par la collection 2026.06 et la version v2026.09 courante au 23 octobre 2026",
     'K11-21'),
    ('Annexe I (I.1, entrées OpenAI, Anthropic, Bank of England) et ch. 4',
     "lettrer les entrées ambiguës (Anthropic 2024c et 2024d, OpenAI 2024c, 2024d et 2025g, Bank of England 2025a) et aligner les renvois du ch. 4 (Anthropic 2025c et 2025e, 2024a; OpenAI 2024a)",
     'K11-34'),
    ('Annexe I (I.1 et tableaux I.1 et I.2), quasi-doublons',
     "fondre quatre paires qui désignent le même document (OASIS UDDI 3.0.2, FOCUS 1.4, OWASP NHI Top 10 2025, communiqué Visa du 14 octobre 2025) et porter le décompte de 1 003 à 999 entrées uniques",
     'K11-02'),
    ('Annexe I (§ I.2, borne b)',
     "dire que l'annexe réunit les sept bibliographies du Vol. I et que les Vol. II et III n'en tiennent aucune",
     'K11-05'),
    ('Annexe I (§ I.2)',
     "distinguer l'assemblage du 30 juillet 2026 du gel du corps au 27 juillet 2026 et renvoyer aux passes d'octobre et de novembre",
     'K11-24'),
    ("Annexe I (I.1, note d'ouverture)",
     "expliquer l'alternance gras / romain du nom de l'auteur (reste de composition du volume source)",
     'L11-14'),
    ('Ch. 49 (§ 49.12.2 et tableau 49.2), « vote dû, non conduit »',
     "remplacer le pictogramme ⚖ par la mention textuelle « marquée vote dû, non conduit » (deux occurrences restantes)",
     'V2-16'),
    ('Ch. 40 (§ 40.3), bloc sur S-149 et S-154',
     "écrire « Ces deux entrées de repérage » au lieu de « Elles », sans antécédent proche",
     'L08-10'),
    ('Ch. 43 (§ 43.3, dernier paragraphe) et ch. 45 (§ 45.1), principes directeurs',
     "dire que le premier des huit principes du Vol. III (le passeport) n'est pas l'un des six du Tableau 45.1 et que la réduction de huit à six n'est pas documentée",
     'L09-06'),
    ('Ch. 43 (§ 43.5.3), instrument LCIM',
     "écrire l'auteur et la date d'origine (Tolk et Muguira, 2003, repris par Wang, Tolk et Wang, 2009), comme au Tableau 24.2 et à l'annexe I",
     'L09-13'),
    ('Ch. 44 (§ 44.0.4), réserve d\'outillage',
     "remplacer « la quasi-totalité des ateliers » par « deux ateliers nommés par le Vol. I (en [C]) », comme au § 44.7",
     'L09-11'),
    ('Ch. 43 (§ 43.6) et ch. 45 (§ 45.13), fait négatif sur l\'arrêté de désignation',
     "dater (16 juillet 2026, rejoué le 28 juillet, index de la Gazette jusqu'au 21 octobre 2026) et borner le fait négatif, et dire que l'existence d'un arrêté non publié demeure au degré 3; sections ajoutées à la ligne correspondante de l'annexe N",
     'L09-05'),
    ('Ch. 45 (§ 45.15), contraintes-pivots',
     "retirer la résidence canadienne de l'énoncé « une à une » du § 45.4 et la renvoyer au principe 4 du Tableau 45.1",
     'L09-07'),
    ('Ch. 46 (ouverture)',
     "retirer la balise de paragraphe fermante en trop après la phrase sur les ch. 42 à 45",
     'L09-17'),
    ('Ch. 48 (§ 48.3), saga',
     "remplacer l'unicité fausse de « sagas » par « seule section à traiter la saga au grain d'une action d'agent », avec renvoi aux ch. 1 et 31",
     'L09-10'),
    ('Ch. 40 (§ 40.2), accord de « multi-agents »',
     "« propre au multi-agents » remplacé par « propre aux systèmes multi-agents »",
     'COQ-Com-134'),
    ('Annexe I (I.1, entrée IBM Sterling B2B Integration)',
     "écrire l'unité du chiffre « 3,1 M » : plus de 3,1 millions de partenaires EDI préexistants, selon la page du produit",
     'COQ-Com-036'),
    ('Annexe I (I.1), espaces',
     "retirer les doubles espaces (« cf.\u00a0 § », « p.\u00a0 », « vol.\u00a0 », « al.\u00a0 — », « vs.\u00a0 »)",
     'COQ-Com-172'),
]
