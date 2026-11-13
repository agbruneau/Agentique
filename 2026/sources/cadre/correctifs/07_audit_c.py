"""Correctifs de l'audit du 10 novembre 2026, lot cadre-c (chapitres 9 à 15, tableaux et figures du lot).

Appliqué après les modules 01 à 04 : chaque passage d'origine est cherché dans le corps déjà corrigé.
"""

CORRECTIONS = [
    # --- Chapitre 9 : identité, passerelle, sécurité -------------------------------------------
    # R04-06 : le tableau 35 aligné sur l'EXIG-IAM-13 (aucun octroi implicite)
    ('Octroi implicite à éviter, octroi par mot de passe interdit, PKCE pour tous les clients (choix du cadre, EXIG-IAM-13)',
     'Octroi implicite interdit (la RFC 9700 le déconseille seulement, SHOULD NOT; choix du cadre, EXIG-IAM-13), octroi par mot de passe interdit, PKCE pour tous les clients (choix du cadre, EXIG-IAM-13)',
     'R04-06'),

    # R04-54 : négations universelles remplacées par des constats sur les textes consultés
    ('Aucune norme IETF, OpenID ou NIST ne fixe de durée de vie chiffrée',
     'Parmi les textes consultés (IETF, OpenID, NIST), aucun ne fixe de durée de vie chiffrée',
     'R04-54'),
    ('Aucune norme ne fixe ces délais.',
     'Les textes consultés ne fixent pas ces délais.',
     'R04-54'),
    ('Aucune norme ne fixe les seuils\xa0: le cadre alerte à 80\xa0% et arrête à 100\xa0%.',
     'Les textes consultés ne fixent pas les seuils\xa0: le cadre alerte à 80\xa0% et arrête à 100\xa0%.',
     'R04-54'),
    ('Aucune source vérifiable ne chiffre le gain d’un coupe-circuit;',
     'Les sources consultées ne chiffrent pas le gain d’un coupe-circuit;',
     'R04-54'),

    # R04-05 : les neuf contrôles de la passerelle deviennent normatifs par la section 1.4
    ('<li>le tableau 58, pour les seules phases d’exigibilité de l’EXIG-GOV-21.</li>',
     '<li>la liste des neuf contrôles de la passerelle d’agents (section 9.4, «\xa0Fonctions obligatoires\xa0»), à laquelle renvoie l’EXIG-IAM-17; la figure 18 l’illustre;</li>\n'
     '<li>le tableau 58, pour les seules phases d’exigibilité de l’EXIG-GOV-21.</li>',
     'R04-05'),
    ('qui applique au minimum les neuf contrôles de la figure 18, chacun lorsqu’il s’applique.',
     'qui applique au minimum les neuf contrôles de la liste «\xa0Fonctions obligatoires\xa0» de la présente section (illustrés par la figure 18), chacun lorsqu’il s’applique\xa0: le contrôle 5 lorsque l’EXIG-AUT-10 exige une approbation, le contrôle 7 lorsqu’une injection de justificatifs est prévue (EXIG-IAM-19).',
     'R04-05'),

    # R04-56 : la dispense des fonctions locales ne remplace pas la décision par appel
    ('la décision par appel (EXIG-IAM-02) y est appliquée par le serveur de ressources et par l’authentification mutuelle du maillage de services.',
     'la décision par appel y est rendue par le service de politiques (EXIG-IAM-02), interrogé par le serveur de ressources ou par une bibliothèque d’application inscrite au catalogue, et non par la seule authentification mutuelle du maillage de services; ce point d’application écrit aussi l’enregistrement d’audit d’un appel P1 portant sur des RP (EXIG-OBS-11).',
     'R04-56'),

    # R04-57 : « point d'application unique » -> commun à tous les appels d'outils et d'agents
    ('un point d’application unique est le seul endroit où une politique',
     'un point d’application commun à tous les appels d’outils et d’agents est le seul endroit où une politique',
     'R04-57'),

    # R04-27 : le coupe-circuit désactive l'identité seulement lorsqu'il vise un agent
    ('par le canal de suspension de l’EXIG-IAM-18, désactive l’identité de l’agent auprès du fournisseur d’identité et diffuse',
     'par le canal de suspension de l’EXIG-IAM-18, désactive, lorsqu’il vise un agent, son identité auprès du fournisseur d’identité et diffuse',
     'R04-27'),
    ('sur toutes les passerelles, désactive l’identité de l’agent et diffuse la révocation',
     'sur toutes les passerelles, désactive, lorsqu’il vise un agent, son identité et diffuse la révocation',
     'R04-27'),

    # R04-59 : décomptes d'ATLAS postérieurs à la version citée, signalés sur place
    ('et 73 études de cas<strong><sup>[352]</sup></strong></td>',
     'et 73 études de cas<strong><sup>[352]</sup></strong>; depuis le 28 octobre 2026, la version 2026.10 compte 129 techniques, 92 sous-techniques, 44 mesures et 77 études de cas<strong><sup>[487]</sup></strong> (annexe H)</td>',
     'R04-59'),
    ('Tableau 36 — Mécanismes d’identité en normalisation : état au 27 octobre 2026</caption>',
     'Tableau 36 — Mécanismes d’identité en normalisation : état au 27 octobre 2026, révisions postérieures signalées</caption>',
     'R04-59'),

    # R04-23 : seuls les risques ASI sont obligatoires, comme l'indique le tableau 37
    ('tenir une matrice qui relie chaque risque ASI, chaque menace T1 à T17 pertinente et chaque technique MITRE ATLAS retenue aux exigences du cadre et aux tests qui les vérifient,',
     'tenir une matrice qui relie chaque risque ASI aux exigences du cadre et aux tests qui les vérifient, et <strong>DEVRAIT</strong> y relier de même les menaces T1 à T17 et les techniques MITRE ATLAS que la modélisation de l’EXIG-SEC-01 a retenues,',
     'R04-23'),

    # R04-36 : un seul terme, « injection d'instructions »
    ('Le NIST classe l’injection d’invite indirecte (NISTAML.015)',
     'Le NIST classe l’injection d’instructions indirecte (NISTAML.015)',
     'R04-36'),
    ('LLM01:2025 (injection d’invite)',
     'LLM01:2025 (injection d’instructions)',
     'R04-36'),

    # R04-61 : quatre niveaux complémentaires, non ordonnés par force
    ('puis échelonne les contrôles du plus faible au plus fort.',
     'puis présente quatre niveaux de contrôle complémentaires.',
     'R04-61'),
    ('Les contrôles ne se valent pas. Le cadre les classe en quatre niveaux, du plus faible au plus fort (bande inférieure de la figure 19), et un agent exposé à du contenu non fiable en combine toujours plusieurs.',
     'Les contrôles ne s’équivalent pas et ne se remplacent pas. Le cadre les présente en quatre niveaux complémentaires, du signalement à l’approbation (bande inférieure de la figure 19)\xa0: l’approbation est le dernier rempart, non le contrôle le plus fort, et elle ne compense pas une conception faible. Un agent exposé à du contenu non fiable en combine toujours plusieurs.',
     'R04-61'),
    ('la bande inférieure classe les contrôles du cadre du plus faible (signaler) au plus fort (approuver).',
     'la bande inférieure présente les quatre niveaux de contrôle du cadre, du signalement à l’approbation, qui se complètent sans se remplacer.',
     'R04-61'),

    # R04-34 : chaque exposé en un seul endroit (courtage : 9.7; AIMS : 9.2; arrêt : 9.4)
    ('Selon la documentation de Vercel Sandbox, le patron a des limites lorsqu’il s’applique au trafic sortant d’un bac à sable\xa0: il dépend de l’indication du nom de serveur TLS (SNI) et exige la terminaison TLS par le mandataire, et une règle générique laisse passer sans transformation le trafic dont le domaine n’est pas détecté<strong><sup>[342]</sup></strong> (section 9.7).',
     'Le patron a des limites lorsqu’il s’applique au trafic sortant d’un bac à sable; elles sont exposées à la section 9.7.',
     'R04-34'),
    ('Le brouillon WIMSE AIMS interdit par ailleurs au modèle d’accéder aux justificatifs de l’agent<strong><sup>[93]</sup></strong>.',
     'Le modèle n’a par ailleurs jamais accès aux justificatifs de l’agent (EXIG-IAM-06, section 9.2).',
     'R04-34'),
    ('Le règlement européen sur l’IA exige que les personnes chargées de la supervision puissent interrompre un système à haut risque au moyen d’un bouton d’arrêt ou d’une procédure analogue qui l’amène à un état sûr (art. 14, par. 4, al. e))<strong><sup>[290]</sup></strong>, et le NIST AI RMF (MANAGE 2.4) demande des mécanismes et des responsabilités pour désactiver un système qui s’écarte de l’usage prévu<strong><sup>[99]</sup></strong>. Au Québec,',
     'Les sources de l’exigence d’arrêt (règlement européen sur l’IA, art. 14, par. 4, al. e); NIST AI RMF, MANAGE 2.4) sont données à la section 9.4. Au Québec,',
     'R04-34'),

    # R04-66 : le journal d'exécution du bac à sable a un statut défini
    ('dans un journal inaltérable rattaché à la trace de la tâche (section 10.3).',
     'dans un journal d’exécution distinct des traces et du journal d’audit, tenu en ajout seul sur un stockage qui interdit modification et effacement avant échéance (EXIG-OBS-13), et rattaché à la trace de la tâche par son identifiant (section 10.1).',
     'R04-66'),
    ('journal d’audit, 24 mois (EXIG-OBS-13); dossier de décision',
     'journal d’audit, 24 mois (EXIG-OBS-13); journal d’exécution des bacs à sable, 24 mois (EXIG-SEC-16, choix du cadre); dossier de décision',
     'R04-66'),

    # R04-33 : EXIG-SEC-21, la « surveillance des flux » devient une mesure constatable
    ('interdiction qu’un serveur référence ou modifie les outils d’un autre, et surveillance des flux de données entre serveurs.',
     'interdiction qu’un serveur référence ou modifie les outils d’un autre, et, pour tout résultat d’un serveur passé en argument à un outil d’un autre serveur, enregistrement au journal d’audit et alerte selon une règle inscrite au catalogue.',
     'R04-33'),

    # --- Chapitre 10 : observabilité, évaluation, FinOps ---------------------------------------
    # R04-39 : identifiants A2A et référence de contenu au tableau 41
    ('pour un appel A2A, le <code>taskId</code> et le <code>contextId</code>. Une déduplication',
     'pour un appel A2A, le <code>taskId</code> et le <code>contextId</code> (attributs <code>ca.entreprise.a2a.task_id</code> et <code>ca.entreprise.a2a.context_id</code>, tableau 41). Une déduplication',
     'R04-39'),
    ('joint par l’identifiant du jeton d’approbation</td></tr></tbody></table>',
     'joint par l’identifiant du jeton d’approbation</td></tr>'
     '<tr><td>A2A</td><td><code>ca.entreprise.a2a.task_id</code>; <code>ca.entreprise.a2a.context_id</code></td><td>Hors convention</td><td>Obligatoires sur un appel A2A (EXIG-OBS-03)</td></tr>'
     '<tr><td>Contenu de débogage</td><td><code>ca.entreprise.content_ref</code></td><td>Hors convention</td><td>Obligatoire lorsqu’une capture de contenu est activée (EXIG-OBS-08)</td></tr></tbody></table>',
     'R04-39'),

    # R04-73 : appels de références en exposant dans les lignes « Sources » (celle du tableau 41 est déjà traitée par 05_audit_a)
    ('(EUR-Lex)<strong>[58, 61]</strong>',
     '(EUR-Lex)<strong><sup>[58, 61]</sup></strong>',
     'R04-73'),
    ('Future of Life Institute<strong>[444, 445, 446]</strong>',
     'Future of Life Institute<strong><sup>[444, 445, 446]</sup></strong>',
     'R04-73'),
    ('Commissariat à la protection de la vie privée; BSIF; RIA<strong>[56, 61, 426, 427, 434, 460]</strong>',
     'Commissariat à la protection de la vie privée; BSIF; RIA<strong><sup>[56, 61, 426, 427, 434, 460]</sup></strong>',
     'R04-73'),
    ('<strong>[61, 318, 413, 432, 452]</strong>',
     '<strong><sup>[61, 318, 413, 432, 452]</sup></strong>',
     'R04-73'),

    # R04-21 : l'extrait reprend la structure de l'annexe C.8 (tableau « approbations », identite, tâche distincte)
    ('l’exemple complet figure à l’annexe C.</p>',
     'l’exemple complet, d’une autre tâche, figure à l’annexe C.8.</p>',
     'R04-21'),
    ('    "agent":       { "id": "agent-risque-credit", "version": "2.3.0", "invite_systeme": "sha256:…" },',
     '    "agent":       { "id": "agent-risque-credit", "identite": "spiffe://…", "invite_systeme": "sha256:…",\n'
     '                     "version": "2.3.0" },',
     'R04-21'),
    ('    "autorite":    { "approbation_jti": "…", "approbateur": "a-91c0…", "controle": "…",\n'
     '                     "empreinte_approbation": "…", "version_politique": "…" },',
     '    "autorite":    { "approbations": [ { "approbateur": "apb-91c0…", "jti": "…", "role": "…" } ],\n'
     '                     "classe_risque": "…", "controle": "…", "empreinte_approbation": "…",\n'
     '                     "niveau_autonomie": "…", "version_politique": "…" },',
     'R04-21'),
    ('"trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "tache": "tache-7f3c2a",',
     '"trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "tache": "tache-2b9d41",',
     'R04-21'),

    # R04-42 : indisponibilité du service d'audit et appels P1 portant sur des RP
    ('s’il est indisponible, les appels P2 et P3 sont refusés.',
     's’il est indisponible, les appels P2 et P3 sont refusés; les appels P1 portant sur des RP ou des données classifiées le sont aussi, sauf si la passerelle met leurs enregistrements en file durable pour les verser au journal au retour du service; les refus sont consignés de la même façon.',
     'R04-42'),

    # R04-49 / R04-50 : le facteur de prix est daté, relatif aux modèles comparés, et sorti du bloc d'exigence
    ('contre 10\xa0$\xa0US et 50\xa0$\xa0US pour Claude Fable 5.1, soit un facteur 100.',
     'contre 10\xa0$\xa0US et 50\xa0$\xa0US pour Claude Fable 5.1, soit, entre ces deux modèles, un facteur 100; l’écart varie selon les modèles comparés et la grille change souvent.',
     'R04-49'),
    ('dans la grille d’octobre 2026, à titre illustratif, l’écart de prix atteint un facteur 100 chez un même fournisseur (Claude Fable 5.1 contre Claude Haiku 5.5, pour des invites d’au plus 100 000 jetons; facteur 20 au-delà, si le prix de Claude Fable 5.1 ne varie pas avec la longueur de l’invite)<strong><sup>[399]</sup></strong>;',
     'l’écart de prix entre le plus petit et le plus grand modèle d’un même fournisseur peut atteindre deux ordres de grandeur (section 10.5)<strong><sup>[399]</sup></strong>;',
     'R04-50'),

    # R04-51 : le segmenteur donne une fourchette, non un écart typique
    ('produit en outre environ 30\xa0% plus de jetons pour un même texte que le segmenteur précédent (celui de Claude Sonnet 4.6 et des modèles antérieurs), l’écart variant selon le contenu',
     'produit en outre jusqu’à 35\xa0% plus de jetons pour un même texte que le segmenteur précédent (celui de Claude Sonnet 4.6 et des modèles antérieurs), soit de 1 à 1,35 fois selon le contenu',
     'R04-51'),

    # R04-71 : l'AI Index 2025 est présenté comme un repère historique
    ('Selon l’AI Index 2025 de Stanford (l’édition 2026 est parue depuis; le chiffre n’a pas été revérifié dans celle-ci), le coût',
     'Selon l’AI Index 2025 de Stanford, repère historique antérieur à octobre 2024, le coût',
     'R04-71'),

    # R04-47 : l'agent sans processus de référence entre en revue de valeur; la définition des trois indicateurs fait foi
    ('<li>le tableau 58, pour les seules phases d’exigibilité de l’EXIG-GOV-21.</li>',
     '<li>la définition des trois indicateurs d’économie unitaire (section 10.6, «\xa0Imputation et économie unitaire\xa0»), à laquelle renvoie l’EXIG-FIN-10;</li>\n'
     '<li>le tableau 58, pour les seules phases d’exigibilité de l’EXIG-GOV-21.</li>',
     'R04-47'),
    ('pour chaque agent en production, les trois indicateurs ci-dessus,',
     'pour chaque agent en production, les trois indicateurs définis à la section 10.6,',
     'R04-47'),
    ('Un agent dont le coût par tâche réussie dépasse celui du processus de référence deux mois de suite (choix du cadre) passe en revue de valeur',
     'Un agent dont le coût par tâche réussie dépasse celui du processus de référence ou, à défaut de processus de référence, la valeur attendue inscrite à la fiche (tableau 42), deux mois de suite (choix du cadre) passe en revue de valeur',
     'R04-47'),

    # --- Chapitre 11 : gouvernance -------------------------------------------------------------
    # R05-01 : l'architecture d'entreprise approuve la revue (A au tableau 44), la sécurité la réalise (R)
    ('Tient le cadre et le catalogue des protocoles; conduit les revues d’architecture; instruit les dérogations.',
     'Tient le cadre et le catalogue des protocoles; approuve les revues d’architecture, que la sécurité réalise (tableau 44); instruit les dérogations.',
     'R05-01'),

    # R05-03 : un seul A par activité et par cas
    ('Chaque activité du tableau 44 <strong>DOIT</strong> avoir un et un seul rôle A.',
     'Chaque activité du tableau 44 <strong>DOIT</strong> avoir un et un seul rôle A dans chaque cas que le tableau et les règles qui le complètent distinguent (classe de risque élevée ou niveau N4, retrait anticipé, délégation de la dérogation, incident de confidentialité).',
     'R05-03'),

    # --- Chapitre 12 : risques, conformité, réglementation -------------------------------------
    # R05-18 : mention de travail retirée; provenance des articles déclarée (la relecture des textes consolidés reste à faire)
    ('dans la lecture qu’en fait le cadre (texte consolidé à relire), exige',
     'dans la lecture qu’en fait le cadre d’après la loi modificative (sans relecture du texte consolidé), exige',
     'R05-18'),
    ('Source des obligations\xa0: L.Q. 2021, c. 25<strong><sup>[56]</sup></strong>. La colonne',
     'Source des obligations\xa0: Loi sur le privé (RLRQ, c. P-39.1), modifiée par la L.Q. 2021, c. 25<strong><sup>[56]</sup></strong>; les obligations sont relevées dans la loi modificative, et le texte consolidé n’a pas été relu pour le présent cadre. La colonne',
     'R05-18/COQ-Cad-225'),

    # R05-60 : l'analyse des biais n'est exigée qu'une fois (volet impact algorithmique de l'EXIG-CON-26, joint à l'EFVP)
    ('et <strong>DOIT</strong> comprendre une analyse des biais lorsque l’agent décide ou recommande à l’égard d’une personne (exigence propre au cadre).',
     'et, lorsque l’agent décide ou recommande à l’égard d’une personne, <strong>DOIT</strong> y joindre le volet impact algorithmique de l’EXIG-CON-26, dont l’analyse des biais tient lieu d’analyse des biais de l’EFVP (exigence propre au cadre).',
     'R05-60'),
    ('non une obligation légale<strong>[56, 413, 415]</strong>.',
     'non une obligation légale<strong><sup>[56, 413, 415]</sup></strong>.',
     'R05-60'),

    # R05-20 : « dès que possible » n'est pas le texte de la LPRPDE (« le plus tôt possible »)
    ('avis aux personnes «\xa0dès que possible\xa0» (LPRPDE, par. 10.1(2) et (6)); toutes les atteintes sont consignées, registre conservé 24 mois<strong>[426, 427]</strong>.',
     'avis aux personnes «\xa0le plus tôt possible\xa0» (LPRPDE, par. 10.1(2) et (6)); toutes les atteintes sont consignées, registre conservé 24 mois<strong><sup>[426, 427]</sup></strong>.',
     'R05-20'),
    ('«\xa0Dès que possible\xa0»; registre de toutes les atteintes conservé 24 mois',
     '«\xa0Le plus tôt possible\xa0»; registre de toutes les atteintes conservé 24 mois',
     'R05-20'),

    # R05-22 / X1-27 : mention de l'AMF sourcée (relais de la Note AMF IA) et datée; veille réglementaire complétée
    ('Ligne directrice sur l’utilisation de l’intelligence artificielle (version d’avril 2026, en vigueur le 1<sup>er</sup> mai 2027), que le présent cadre ne reprend pas.',
     'Ligne directrice sur l’utilisation de l’intelligence artificielle (document daté de mars 2026, publié en avril 2026, en vigueur le 1<sup>er</sup> mai 2027)<strong><sup>[491]</sup></strong>, que le présent cadre ne reprend pas.',
     'R05-22/X1-27'),
    ('veille réglementaire (CAI, BSIF, AMF, Parlement du Canada et Assemblée nationale, Commission européenne)',
     'veille réglementaire (CAI, Commissariat à la protection de la vie privée du Canada, BSIF, AMF, Autorités canadiennes en valeurs mobilières (ACVM), Parlement du Canada et Assemblée nationale, Commission européenne)',
     'R05-22'),

    # R05-68 : régime de l'inventaire E-23 après la date butoir
    ('la version et l’état de validation. E-23 ne fixe aucune échéance',
     'la version et l’état de validation. Elle <strong>DOIT</strong> ensuite inscrire tout agent ou modèle nouveau avant sa mise en production. L’inventaire est le registre d’entreprise (section 11.4), que l’équipe plateforme opère et où le parrain inscrit l’agent (tableau 44). E-23 ne fixe aucune échéance',
     'R05-68'),

    # X1-17 : E-23 « attend » un inventaire (et non « exige »), comme ailleurs dans le cadre
    ('la ligne directrice E-23 du BSIF, en vigueur le 1<sup>er</sup> mai 2027, exige un inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs, et une cote',
     'la ligne directrice E-23 du BSIF, en vigueur le 1<sup>er</sup> mai 2027, attend un inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs, et une cote',
     'X1-17'),
    ('dans ses principes de surveillance et exige un inventaire d’entreprise',
     'dans ses principes de surveillance et attend un inventaire d’entreprise',
     'X1-17'),
    ('applicable aux institutions financières fédérales, exige un inventaire d’entreprise des modèles à risque non négligeable',
     'applicable aux institutions financières fédérales, attend un inventaire d’entreprise des modèles à risque non négligeable',
     'X1-17'),

    # C4-23 : intitulé d'E-23 unique (la référence [8] est alignée sur le tableau 48 et sur le texte : « risque de modèle »)
    ('Ligne directrice E-23 – Gestion du risque de modélisation (2027).',
     'Ligne directrice E-23 – Gestion du risque de modèle (2027).',
     'C4-23'),

    # --- Chapitre 13 : approvisionnement et clauses --------------------------------------------
    # R05-32 : un destinataire interne (architecture d'entreprise) pour les exigences adressées au fournisseur
    ('Le fournisseur <strong>DOIT</strong> démontrer la prise en charge de MCP 2026-07-28 et,',
     'L’architecture d’entreprise <strong>DOIT</strong> exiger du fournisseur qu’il démontre la prise en charge de MCP 2026-07-28 et,',
     'R05-32'),
    ('La solution <strong>DOIT</strong> exporter traces, métriques et journaux par OTLP',
     'L’architecture d’entreprise <strong>DOIT</strong> exiger que la solution exporte traces, métriques et journaux par OTLP',
     'R05-32'),
    ('propager le contexte W3C Trace Context sur chaque saut qu’elle contrôle et fournir ses données de facturation',
     'qu’elle propage le contexte W3C Trace Context sur chaque saut qu’elle contrôle et qu’elle fournisse ses données de facturation',
     'R05-32'),
    ('La solution <strong>DOIT</strong> attribuer à chaque agent une identité non humaine distincte, fédérable au fournisseur d’identité de l’entreprise et sans clé statique partagée, et permettre à l’entreprise',
     'L’architecture d’entreprise <strong>DOIT</strong> exiger que la solution attribue à chaque agent une identité non humaine distincte, fédérable au fournisseur d’identité de l’entreprise et sans clé statique partagée, et permette à l’entreprise',
     'R05-32'),

    # R05-33 : le « Pourquoi » de l'EXIG-APP-07 dit ce qu'il veut dire
    ('sans A2A 1.0 natif ni extension imposée, l’entreprise change de fournisseur sans réécrire ses délégations;',
     'avec A2A 1.0 natif et sans extension imposée, l’entreprise change de fournisseur sans réécrire ses délégations;',
     'R05-33'),

    # R05-49 : écart contractuel pour les engagements qui durent le temps du contrat
    ('Les délais marqués « cible du cadre » sont des choix internes, ajustables par dérogation (section 11.6).',
     'Les délais marqués « cible du cadre » sont des choix internes, ajustables par dérogation (section 11.6). Une dérogation qui porte sur un engagement contractuel (délai négocié sous la cible, extension obligatoire admise par l’EXIG-APP-02, offre retenue malgré un échec éliminatoire selon l’EXIG-APP-17) prend la forme d’un écart contractuel : le comité le décide; il vaut jusqu’à l’échéance du contrat, sans la limite de six mois de l’EXIG-GOV-16; il est inscrit au registre et revu à chaque renouvellement. Aucune dérogation ni aucun écart contractuel ne peut porter sur ce que les clauses 4 à 6 reprennent d’une obligation légale (art. 17 et 18.3 de la Loi sur le privé; EXIG-GOV-17).',
     'R05-49'),
    ('sauf dérogation approuvée (section 11.6). La grille remplie',
     'sauf dérogation approuvée, sous la forme d’un écart contractuel (section 13.3). La grille remplie',
     'R05-49'),

    # R05-34 : cible distincte pour les institutions soumises à un signalement en 24 heures
    ('tant que dure le gel notifié par l’entreprise (EXIG-CON-23).</p>\n<div id="pourquoi-1253">',
     'tant que dure le gel notifié par l’entreprise (EXIG-CON-23). Pour une institution financière fédérale, que l’avis au BSIF astreint à 24 heures ou moins, le contrat <strong>DEVRAIT</strong> fixer un délai plus court (cible du cadre : quatre heures).</p>\n<div id="pourquoi-1253">',
     'R05-34'),
    ('et une institution financière fédérale devrait exiger un délai plus court<strong><sup>[434]</sup></strong> (section 12.8).',
     'd’où le délai plus court que le contrat d’une institution financière fédérale devrait fixer<strong><sup>[434]</sup></strong> (section 12.8).',
     'R05-34'),

    # R05-36 : le seuil de 2,0 ne peut jamais jouer; le score sert à classer les offres admissibles
    ('Le cadre fixe le seuil d’admissibilité à 2,0, sans aucun échec à un critère éliminatoire.',
     'Une offre est admissible si elle n’échoue à aucun critère éliminatoire; le cadre ne fixe pas de seuil de score, puisqu’une offre sans échec éliminatoire dépasse toujours 2,0, et le score sert à classer les offres admissibles.',
     'R05-36'),

    # R05-63 : doublon [311]/[466] déclaré à l'annexe G (473 entrées, 25 doublons); seule la désignation des auteurs est alignée
    ('<code>[466]</code></strong> South, T. (dir.) (2025, octobre).',
     '<code>[466]</code></strong> South, T. et al. (2025, octobre).',
     'R05-63'),

    # --- Chapitres 14 et 15 : maturité et feuille de route --------------------------------------
    # R05-38 : qui arrête l'évaluation initiale
    ('recalibrée au jalon 1. Une évaluation a lieu ensuite',
     'recalibrée au jalon 1. Avant la constitution du comité (tableau 60, semaines 1 et 2), le parrain de direction de la feuille de route (section 15.4) arrête cette évaluation initiale, et le comité la ratifie à sa première séance. Une évaluation a lieu ensuite',
     'R05-38'),

    # R05-54 : la date de migration MCP au jalon 1, l'absence de révision antérieure au jalon 2
    ('comité en fonction; aucune clé partagée entre agents et tous les appels de modèles par la passerelle de modèles (tableau 61).',
     'comité en fonction; chaque serveur et client MCP antérieur à la révision de référence inscrit au catalogue avec sa date de migration (EXIG-MCP-22); aucune clé partagée entre agents et tous les appels de modèles par la passerelle de modèles (tableau 61).',
     'R05-54'),
    ('chaque serveur et client MCP en production sur une révision antérieure a une date de migration au plus tard le 28\xa0juillet 2027, et aucun ne reste en production après cette date.',
     'aucun serveur ni client MCP d’une révision antérieure à la révision de référence n’est en production (échéance du 28\xa0juillet 2027 au plus tard, EXIG-MCP-22).',
     'R05-54'),

    # R05-55 : critère constatable au jalon 5
    ('niveau 5 visé en interopérabilité et en gouvernance',
     'niveau 5 atteint en interopérabilité et en gouvernance',
     'R05-55'),

    # R05-43 : les règles de progression, l'encadré du jalon 2a, les règles de mesure des indicateurs et le recul de maturité sont normatifs
    ('<li>le tableau 58, pour les seules phases d’exigibilité de l’EXIG-GOV-21.</li>',
     '<li>le tableau 58, pour ses phases d’exigibilité (EXIG-GOV-21) et pour les critères de ses jalons;</li>\n'
     '<li>les règles de progression et l’encadré «\xa0Jalon 2a\xa0» de la section 15.1, les règles de mesure des indicateurs de la section 15.3 et la règle de recul de maturité de la section 14.2, dont les «\xa0doit\xa0» et les «\xa0ne doit pas\xa0» ont la force du tableau 3, sans bloc d’exigence propre.</li>',
     'R05-43'),

    # R05-54 (suite) / V3-31 : la cible interne du jalon 2a est distinguée de l'échéance légale au tableau 59
    ('<strong>J2a</strong></td><td>RIA, annexe III, le 2\xa0décembre 2027</td>',
     '<strong>J2a</strong> (cible interne du cadre)</td><td>RIA, annexe III, le 2\xa0décembre 2027</td>',
     'V3-31'),

    # V3-28 : la légende de la figure 25 parle de jalons, comme le texte (section 11.5) et le bandeau de la figure
    ('Figure 25 — Cycle de vie d’un agent et points de contrôle.',
     'Figure 25 — Cycle de vie d’un agent et jalons.',
     'V3-28'),

    # C4-02 : l'obligation d'informer de l'art. 12.1 s'applique dès l'adoption; repérage des décisions dès les semaines 3 et 4
    ('recenser les clés d’API et les comptes de service utilisés par des agents. Pour une institution financière fédérale,',
     'recenser les clés d’API et les comptes de service utilisés par des agents; repérer les décisions fondées exclusivement sur un traitement automatisé (art. 12.1 de la Loi sur le privé), dont l’obligation d’informer s’applique déjà, par des moyens manuels au besoin, sans attendre l’outillage de la phase Plateforme. Pour une institution financière fédérale,',
     'C4-02'),
    ('ropriétaire métier; inventaire des secrets</td><td>Propriétaires métier, équipe plateforme</td>',
     'ropriétaire métier; inventaire des secrets; liste des décisions visées par l’article 12.1</td><td>Propriétaires métier, équipe plateforme</td>',
     'C4-02'),

    # C3-20 : le texte précise déjà que l'environnement Wasm tourne dans un processus distinct de l'agent; la force du mot-clé est rétablie
    ('Il ne doit pas s’exécuter dans un conteneur à noyau partagé, dans le processus de l’agent ni sur l’hôte de la passerelle.',
     'Il <strong>NE DOIT PAS</strong> s’exécuter dans un conteneur à noyau partagé, dans le processus de l’agent ni sur l’hôte de la passerelle.',
     'C3-20'),

    # C4-05 : la séparation des fonctions vise toute action soumise à approbation
    ('n’approuve pas les actions P3 de cet agent;',
     'n’approuve aucune action de cet agent soumise à approbation (EXIG-AUT-10);',
     'C4-05'),

    # C4-17 : lettres RACI cohérentes avec la section 11.2 (R pour les actions de réalisation)
    ('<td>I\xa0: instancie</td>',
     '<td>R\xa0: instancie</td>',
     'C4-17'),
    ('<td>C\xa0: inscrit au catalogue</td><td>R\xa0: propose</td>',
     '<td>R\xa0: inscrit au catalogue</td><td>R\xa0: propose</td>',
     'C4-17'),

    # C4-20 : règles hors bloc du § 13.2 reformulées (règle rattachée à l'EXIG-APP-03; grille informative, comme au § 9.4)
    ('ses résultats sont utiles, mais l’entreprise doit les compléter par ses propres scénarios',
     'ses résultats sont utiles, mais l’entreprise les complète par ses propres scénarios (EXIG-APP-03)',
     'C4-20'),
    ('Le cadre retient en outre, comme critères d’acceptation d’une passerelle d’agents (section 9.4), sept portes',
     'Le cadre retient en outre, comme grille informative d’évaluation d’une passerelle d’agents (section 9.4), sept portes',
     'C4-20'),

    # --- Coquilles et typographie --------------------------------------------------------------
    ('Plafonds repris d’EXIG-CON-02, qui fait foi.',
     'Plafonds repris de l’EXIG-CON-02, qui fait foi.',
     'COQ-Cad-059'),
    ('à la découverte des actifs d’IA déployés par 30 nouvelles intégrations',
     'à la découverte des actifs d’IA déployés, au moyen de 30 nouvelles intégrations',
     'COQ-Cad-222'),
    ('de la fonction risques et, s’il y a des RP, du RPRP',
     'de la fonction risques et conformité et, s’il y a des RP, du RPRP',
     'COQ-Cad-223'),
    ('Les quatre critères d’analyse du cadre (rayon d’impact, réversibilité, délai de détection et de récupération, observabilité reconstructive) sont décrits à la section 8.2.',
     'Les quatre critères d’analyse du cadre qui fixent le niveau d’autonomie sous le plafond de la classe (rayon d’impact, réversibilité, délai de détection et de récupération, observabilité reconstructive) sont décrits à la section 8.2; ce ne sont pas les critères du tableau 46.',
     'COQ-Cad-224'),
    ('des centres de données sous juridiction québécoise',
     'des centres de données relevant de la compétence du Québec',
     'COQ-Cad-226'),
    ('si ses sorties sont, ou sont prévues pour être, utilisées dans l’Union européenne',
     'si ses sorties sont utilisées dans l’Union européenne, ou destinées à l’être',
     'COQ-Cad-227'),
    ('vise le niveau 3, «\xa0Défini\xa0», en 18 mois (durée indicative',
     'vise le niveau 3, «\xa0Défini\xa0», en 18 mois environ (durée indicative',
     'COQ-Cad-228'),
    ('Ces 13 semaines sont des semaines travaillées\xa0: une période de congés collectifs s’y ajoute (section 15.1, tableau 60).',
     'Une période de congés collectifs s’ajoute à ces 13 semaines (section 15.1, tableau 60).',
     'COQ-Cad-230'),
]

JOURNAL = [
    # --- Chapitre 9 ---
    ('Tableau 35 (profil OAuth), ligne « Pratiques de sécurité courantes »',
     'Octroi implicite interdit et non plus « à éviter », conformément à l’EXIG-IAM-13; la RFC 9700 ne le déconseille que (SHOULD NOT), l’interdiction est un choix du cadre.',
     ['R04-06']),
    ('§ 9.3 (durée de vie des jetons), § 9.4 (coupe-circuit), § 9.7 (verrou 3), § 10.6 (enveloppe et quotas)',
     'Négations universelles (« aucune norme ne fixe… », « aucune source vérifiable ne chiffre… ») remplacées par un constat sur les textes et sources consultés.',
     ['R04-54']),
    ('§ 1.4; § 9.4 (EXIG-IAM-17)',
     'Les neuf contrôles de la passerelle d’agents font foi par la liste « Fonctions obligatoires » (ajoutée à la liste normative de la section 1.4), la figure 18 restant informative; conditions d’application des contrôles 5 et 7 énoncées dans l’exigence.',
     ['R04-05']),
    ('§ 9.4, EXIG-IAM-17',
     'La fonction locale P0-P1 dispensée de la passerelle reste soumise à la décision par appel du service de politiques, interrogé par le serveur de ressources ou une bibliothèque inscrite au catalogue; l’appel P1 portant sur des RP est journalisé (EXIG-OBS-11).',
     ['R04-56']),
    ('§ 9.4, EXIG-IAM-17 (Pourquoi)',
     '« Point d’application unique » remplacé par « point d’application commun à tous les appels d’outils et d’agents », la passerelle de modèles et le courtier d’événements restant d’autres points d’application.',
     ['R04-57']),
    ('§ 9.4, EXIG-IAM-20; glossaire (Coupe-circuit)',
     'Le coupe-circuit ne désactive l’identité que lorsqu’il vise un agent; il suspend aussi un outil, un serveur MCP ou une catégorie d’actions. Bandeau de la figure 18 : voir le rapport de lot.',
     ['R04-27']),
    ('§ 9.5, tableaux 36 et 37 (MITRE ATLAS)',
     'Décomptes de la version 2026.10 d’ATLAS (28 octobre 2026) signalés sur place avec renvoi à l’annexe H; titre du tableau 36 complété (« révisions postérieures signalées »). Décomptes non revérifiés à la source.',
     ['R04-59']),
    ('§ 9.5, EXIG-SEC-02',
     'La matrice DOIT relier les risques ASI (obligatoires au tableau 37) et DEVRAIT relier les menaces T1 à T17 et les techniques ATLAS retenues par la modélisation de l’EXIG-SEC-01 (référentiels « Recommandé »).',
     ['R04-23']),
    ('§ 9.5 (correspondance ASI-LLM), § 9.6 (Présumer l’injection)',
     '« Injection d’invite » remplacée par « injection d’instructions », terme du titre et de la définition de la section 9.6.',
     ['R04-36']),
    ('§ 9.6 (introduction, « Quatre niveaux de contrôle »); légende de la figure 19',
     'Les quatre niveaux sont présentés comme complémentaires et non ordonnés par force; l’approbation est le dernier rempart, non le contrôle le plus fort. Texte intégré à la figure 19 : voir le rapport de lot.',
     ['R04-61']),
    ('§ 9.4 (modèle sans clés), § 9.7 (verrou 2), § 9.9 (exercices)',
     'Redites réduites : limites du courtage d’identifiants exposées en 9.7 seulement, interdiction faite au modèle d’accéder aux justificatifs renvoyée à l’EXIG-IAM-06 (9.2), sources de l’arrêt (RIA art. 14(4)e, NIST MANAGE 2.4) données en 9.4 seulement.',
     ['R04-34']),
    ('§ 9.7, EXIG-SEC-16; EXIG-CON-10',
     'Journal d’exécution du bac à sable défini : magasin distinct, en ajout seul (EXIG-OBS-13), rattaché à la trace par son identifiant, conservé 24 mois au moins (choix du cadre, ajouté aux minimums de l’EXIG-CON-10).',
     ['R04-66']),
    ('§ 9.8, EXIG-SEC-21',
     'La « surveillance des flux de données » devient une mesure constatable : enregistrement d’audit et alerte, selon une règle inscrite au catalogue, pour tout résultat d’un serveur passé en argument à un outil d’un autre serveur.',
     ['R04-33']),
    ('§ 9.7, EXIG-SEC-08',
     'Le texte précise déjà que l’environnement Wasm tourne dans un processus distinct de l’agent (corrigé antérieurement); mot-clé « NE DOIT PAS » rétabli en majuscules et en gras.',
     ['C3-20']),

    # --- Chapitre 10 ---
    ('§ 10.1, EXIG-OBS-03; tableau 41',
     'Attributs des identifiants A2A (ca.entreprise.a2a.task_id et .context_id) et de la référence de contenu (ca.entreprise.content_ref) ajoutés au tableau 41 et à l’EXIG-OBS-03.',
     ['R04-39']),
    ('§ 12.4 à 12.9 (lignes « Sources »)',
     'Appels de références des lignes « Sources » mis en exposant, comme dans le texte courant. Les espaces distendus des paragraphes justifiés relèvent de la composition (construire_pdf.py) : voir le rapport de lot.',
     ['R04-73']),
    ('§ 10.3, extrait « Enregistrement d’audit à cinq éléments »',
     'Extrait aligné sur la structure de l’annexe C.8 (tableau « approbations », classe de risque, niveau d’autonomie, identité de l’agent) avec un identifiant de tâche distinct; l’exemple complet est dit d’une autre tâche.',
     ['R04-21']),
    ('§ 10.3, EXIG-OBS-11',
     'Service d’audit indisponible : les appels P1 portant sur des RP ou des données classifiées sont refusés, sauf mise en file durable de leurs enregistrements versés au retour du service; les refus sont consignés de la même façon.',
     ['R04-42']),
    ('§ 10.5 (« Une facture qui dépend de la configuration »); EXIG-FIN-06 (Pourquoi)',
     'Facteur de prix 100 daté et relatif aux deux modèles comparés; rapport de prix et noms de modèles retirés du bloc d’exigence (« deux ordres de grandeur », renvoi à la section 10.5).',
     ['R04-49', 'R04-50']),
    ('§ 10.5 (segmenteur des modèles Claude 4.7 et suivants)',
     '« Environ 30 % » remplacé par la fourchette documentée (jusqu’à 35 %, soit de 1 à 1,35 fois selon le contenu); valeur relevée par l’audit dans la documentation de l’API, la page [399] n’ayant pas été rouverte.',
     ['R04-51']),
    ('§ 10.5 (AI Index 2025 de Stanford)',
     'Repère présenté comme historique (antérieur à octobre 2024); parenthèse sur l’édition 2026 retirée.',
     ['R04-71']),
    ('§ 1.4; § 10.6, EXIG-FIN-10',
     'L’agent sans processus de référence entre en revue de valeur (comparaison à la valeur attendue de la fiche, tableau 42); la définition des trois indicateurs d’économie unitaire (section 10.6) est ajoutée à la liste normative de la section 1.4.',
     ['R04-47']),

    # --- Chapitre 11 ---
    ('§ 11.1, tableau 43 (Architecture d’entreprise)',
     'L’architecture d’entreprise approuve les revues d’architecture que la sécurité réalise, comme au tableau 44 (A et R).',
     ['R05-01']),
    ('§ 11.2, EXIG-GOV-04',
     'Un seul rôle A par activité et par cas (classe élevée ou N4, retrait anticipé, délégation de la dérogation, incident de confidentialité), conformément au tableau 44 et à ses règles complémentaires.',
     ['R05-03']),
    ('§ 11.2, EXIG-GOV-03',
     'Le responsable technique n’approuve aucune action de son agent soumise à approbation (EXIG-AUT-10), et non plus les seules actions P3.',
     ['C4-05']),
    ('§ 11.3, tableau 45',
     '« I : instancie » et « C : inscrit au catalogue » remplacés par « R : … », les lettres I et C ayant le sens de la section 11.2.',
     ['C4-17']),
    ('§ 11.4; § 12.3 (EXIG-CON-12, Pourquoi); § 15.1 (encadré « Attention »)',
     'E-23 « attend » (et non « exige ») un inventaire d’entreprise des modèles, comme ailleurs dans le cadre.',
     ['X1-17']),

    # --- Chapitre 12 ---
    ('§ 12.2, EXIG-CON-09 (Pourquoi); note du tableau 47',
     'Mention de travail « texte consolidé à relire » retirée : la provenance (loi modificative, L.Q. 2021, c. 25) et l’absence de relecture du texte consolidé sont déclarées; la relecture du RLRQ c. P-39.1 reste à faire.',
     ['R05-18', 'COQ-Cad-225']),
    ('§ 12.2, EXIG-CON-04',
     'L’analyse des biais n’est plus exigée deux fois : l’EFVP y joint le volet impact algorithmique de l’EXIG-CON-26, dont l’analyse des biais tient lieu.',
     ['R05-60']),
    ('§ 12.3, tableaux 48 et 51 (LPRPDE)',
     '« Dès que possible » (entre guillemets) remplacé par « le plus tôt possible », libellé des paragraphes 10.1(2) et 10.1(6).',
     ['R05-20']),
    ('§ 12.3 (« Trois conséquences pratiques »); EXIG-GOV-20',
     'Mention de la ligne directrice de l’AMF datée (document de mars 2026, publié en avril 2026) et sourcée par la Note AMF IA [491]; veille réglementaire complétée (Commissariat à la protection de la vie privée du Canada, ACVM). Lignes AMF et ACVM du tableau 48 non ajoutées (voir le rapport de lot).',
     ['R05-22', 'X1-27']),
    ('§ 12.3, EXIG-CON-12',
     'Après le 1er mai 2027, tout agent ou modèle nouveau est inscrit à l’inventaire avant sa mise en production; l’inventaire est le registre d’entreprise (section 11.4), opéré par l’équipe plateforme, où le parrain inscrit l’agent.',
     ['R05-68']),
    ('Annexe G, référence [8]',
     'Intitulé de la ligne directrice E-23 aligné sur le tableau 48 et le texte : « Gestion du risque de modèle ».',
     ['C4-23']),
    ('§ 11.6, § 12.1 (note du tableau 46), § 12.3 (Énoncé de politique de souveraineté numérique), § 12.4 (EXIG-CON-13)',
     'Coquilles : « de l’EXIG-CON-02 », « au moyen de 30 nouvelles intégrations », « fonction risques et conformité », précision que les quatre critères d’analyse (§ 8.2) ne sont pas ceux du tableau 46, « relevant de la compétence du Québec », « utilisées dans l’Union européenne, ou destinées à l’être ».',
     ['COQ-Cad-059', 'COQ-Cad-222', 'COQ-Cad-223', 'COQ-Cad-224', 'COQ-Cad-226', 'COQ-Cad-227']),

    # --- Chapitre 13 ---
    ('§ 13.2, EXIG-APP-03, EXIG-APP-05, EXIG-APP-06',
     'Destinataire interne ajouté aux exigences adressées au fournisseur : l’architecture d’entreprise exige du fournisseur ou de la solution la démonstration ou la fonction visée.',
     ['R05-32']),
    ('§ 13.2 (interopérabilité, passerelle d’agents)',
     'Règles hors bloc reformulées : la complémentarité des essais est rattachée à l’EXIG-APP-03, et les sept portes de MuleSoft sont une grille informative, comme à la section 9.4.',
     ['C4-20']),
    ('§ 13.3, EXIG-APP-07 (Pourquoi)',
     '« Sans A2A 1.0 natif ni extension imposée » remplacé par « avec A2A 1.0 natif et sans extension imposée ».',
     ['R05-33']),
    ('§ 13.3 (chapeau); EXIG-APP-17',
     'Écart contractuel pour les engagements qui durent le temps du contrat (décidé par le comité, valable jusqu’à l’échéance, inscrit au registre, revu au renouvellement, sans la limite de six mois); clauses 4 à 6 non négociables pour ce qu’elles reprennent d’une obligation légale (EXIG-GOV-17).',
     ['R05-49']),
    ('§ 13.3, EXIG-APP-12',
     'Cible distincte pour une institution financière fédérale (DEVRAIT : quatre heures, cible du cadre), le délai de 24 heures du BSIF n’étant pas tenable avec la cible générale.',
     ['R05-34']),
    ('§ 13.4 (grille d’évaluation)',
     'Seuil d’admissibilité de 2,0 retiré (il ne pouvait jamais jouer) : l’admissibilité dépend de l’absence d’échec éliminatoire, et le score classe les offres admissibles.',
     ['R05-36']),
    ('Annexe G, référence [466]',
     'Désignation des auteurs alignée sur [311] (« et al. »). Fusion des doublons non faite : l’annexe G les déclare (473 entrées, 25 doublons) et ne réattribue jamais un numéro.',
     ['R05-63']),

    # --- Chapitres 14 et 15 ---
    ('§ 14.2 (Calendrier et conduite)',
     'L’évaluation initiale, antérieure au mandat du comité, est arrêtée par le parrain de direction de la feuille de route, puis ratifiée par le comité à sa première séance.',
     ['R05-38']),
    ('§ 15.1, tableau 58 (jalons 1, 2 et 5); tableau 59',
     'Jalon 1 : date de migration de chaque serveur et client MCP antérieur; jalon 2 : aucun serveur ni client MCP d’une révision antérieure en production; jalon 5 : « niveau 5 atteint » (et non « visé »); jalon 2a désigné comme cible interne au tableau 59. Figure 28 : voir le rapport de lot.',
     ['R05-54', 'R05-55', 'V3-31']),
    ('§ 1.4; § 14.2, § 15.1, § 15.3',
     'Les règles de progression, l’encadré « Jalon 2a », les règles de mesure des indicateurs, le recul de maturité et les critères des jalons du tableau 58 sont ajoutés à la liste normative de la section 1.4 (ils ont la force du tableau 3, sans bloc d’exigence propre).',
     ['R05-43']),
    ('§ 15.2, tableau 60 (semaines 3 et 4); § 15.1, tableau 58 (Plateforme)',
     'L’obligation d’informer de l’art. 12.1 s’applique dès l’adoption : repérage des décisions exclusivement automatisées ajouté aux semaines 3 et 4 (livrable : liste des décisions visées). Tableau 58 et figure 28 déjà corrigés.',
     ['C4-02']),
    ('§ 11.5 (légende de la figure 25)',
     'Titre de la légende : « points de contrôle » remplacé par « jalons ». Libellés et flèche de la figure 25 : voir le rapport de lot.',
     ['V3-28']),
    ('§ 14.1 (légende de la figure 27), § 15.2',
     '« 18 mois environ » dans la légende de la figure 27 (le calage du tableau 59 place J3 à 19 mois); redite supprimée au début de la section 15.2. Figures 27 et 28 : voir le rapport de lot.',
     ['COQ-Cad-228', 'COQ-Cad-230']),
]
