"""Corrections des relectures des 3 et 11 novembre 2026, appliquées au corps extrait.

Le corps de la Revue n'a pas de source éditable : il est relu dans l'édition d'origine
(construire_pdf.py, ORIGINE). Comme les errata du 29 octobre, les corrections des
relectures des 3 et 11 novembre sont faites à leur place, et consignées au tableau
d'errata de l'annexe (actualisation-2026-11.html, tableau 19).

Chaque correction remplace un passage qui doit figurer une fois exactement dans le corps
extrait : un passage absent ou ambigu arrête la composition au lieu de passer en silence.
"""
import re

NBSP = ' '

# (passage d'origine, passage corrigé), dans l'ordre du document
CORRECTIONS = [
    # mots-clés : trait d'union harmonisé avec le reste de la revue
    ('chorégraphie agentique ; essaim multiagents ;', 'chorégraphie agentique ; essaim multi-agents ;'),
    # 2.1 : les pièces à DOI sont citées aux fronts des processus et de la gouvernance,
    # non à la couche transactionnelle; règle de numérotation des normes
    ('sans laquelle le front transactionnel n’aurait pas de point d’appui.',
     'sans laquelle les fronts des processus d’affaires et de la gouvernance, où elles sont citées, '
     'n’auraient pas de point d’appui. Elles reçoivent un numéro parce qu’elles sont discutées comme '
     'pièces ; les normes que le texte invoque seulement comme référentiel — la RFC 8693 de l’IETF pour '
     'l’échange de jetons, le modèle PROV du W3C — sont nommées en ligne, sans entrée.'),
    # 2.1 : [43] et [47] désormais engagées en 9.3
    ('vingt-trois de ses cinquante pièces y sont engagées une à une, vingt-sept ne le sont pas',
     'vingt-cinq de ses cinquante pièces y sont engagées une à une, vingt-cinq ne le sont pas'),
    # 2.2 : règle de partage des commentaires, rendue déterministe
    ('une acceptation ou une présentation annoncée compte, une soumission annoncée ne compte pas —',
     'une acceptation ou une présentation annoncée compte, une soumission annoncée ne compte pas, et un '
     'nom de conférence ou d’atelier porté seul, sans mention de soumission ni d’évaluation en cours, '
     'vaut annonce d’acceptation —'),
    # tableau 2 : [180] est instruite aussi au front multi-agents
    ('<td>Systèmes multi-agents</td><td>[88-101], [187]</td>',
     '<td>Systèmes multi-agents</td><td>[88-101], [187] (et [180], rattachée à l’essaim)</td>'),
    # 5.1 : la séparation par capacités a déjà sa mesure hors du lot
    ('convertir la donnée non fiable en types de portée et de contenu bornés [74].</p>',
     'convertir la donnée non fiable en types de portée et de contenu bornés [74]. Hors du lot, l’idée '
     'a déjà sa mesure : CaMeL (Debenedetti <em>et al.</em>, arXiv:2503.18813, 2025) sépare flux de '
     'contrôle et flux de données par capacités et résout 77 % des tâches d’AgentDojo (Debenedetti '
     '<em>et al.</em>, NeurIPS 2024) avec une sécurité prouvable, contre 84 % sans défense, selon le '
     'résumé de sa version courante au 3 novembre 2026.</p>'),
    # 5.2
    ('revendication adossée à des études de cas non dénombrées, donc auto-évaluation et non évaluation adverse.',
     'revendication adossée à des études de cas non dénombrées, donc auto-évaluation et non évaluation '
     'adverse, quand le coût d’utilité de la séparation par capacités est chiffré ailleurs, à sept points '
     'de tâches résolues sur AgentDojo pour CaMeL (5.1).'),
    # 6.1 : [78] instruite à son front; antériorité du primitif atténuant
    ('capacités bornées par époque se fermant à l’achèvement de la tâche [87]. Le socle proposait déjà '
     'des jetons de capacité liés à l’invocation [16].',
     'capacités bornées par époque se fermant à l’achèvement de la tâche [87]. Une formalisation borne '
     'ce que la chaîne transmet de responsabilité : la délégation à deux niveaux répartit la '
     'responsabilité le long d’une chaîne à plusieurs sauts sous un plafond par agent, avec monotonie '
     'de la sûreté et convergence de la politique interne — trois résultats prouvés, la validation '
     'empirique étant annoncée pour une révision ultérieure [78]. <em>Prépublication d’un auteur unique, '
     'non révisée par les pairs : aucune mesure.</em> Le socle proposait déjà des jetons de capacité '
     'liés à l’invocation [16]. Le primitif est d’ailleurs antérieur aux agents : les Macaroons '
     '(Birgisson <em>et al.</em>, NDSS 2014) chaînent des réserves qui ne peuvent qu’atténuer '
     'l’autorité, chaque détenteur pouvant en ajouter sans l’émetteur, et Biscuit en donne une forme à '
     'clé publique, vérifiable hors ligne. Ce qui converge ici est l’adaptation d’un primitif établi aux '
     'protocoles d’agents, non son invention.'),
    # 6.1 : régime de [179]
    ('<em>Rapport d’expérience de trois auteurs : aucune mesure,',
     '<em>Prépublication non révisée par les pairs, rapport d’expérience de trois auteurs : aucune mesure,'),
    # 7.1
    ('la supervision d’exécution en récupère −29,68 % de jetons sans perte de succès sur GAIA [99].',
     'la supervision d’exécution réduit la dépense de jetons de 29,68 % sans perte de succès sur GAIA [99].'),
    # 7.2 : tableau 4, reste de l'erratum 3 du 29 octobre
    ('onze évaluent une construction de leurs auteurs et quatre annoncent un comité de lecture ; les '
     'quatre évaluations indépendantes contre ligne de base forte concluent toutes au non-avantage.',
     'onze évaluent une construction de leurs auteurs et quatre annoncent un comité de lecture ; les '
     'quatre pièces contre ligne de base forte concluent toutes au non-avantage, dont trois évaluent une '
     'architecture de tiers, [92] évaluant aussi son propre cadre et comptant des deux côtés.'),
    ('<td>Non-avantage</td><td>architecture de tiers</td>',
     '<td>Non-avantage</td><td>architecture de tiers ; des auteurs pour [92]</td>'),
    ('quand la correction bootstrap n’est qu’en O(n^−1/2).',
     'quand la correction bootstrap n’est qu’en O(n<sup>−1/2</sup>).'),
    # 8.1
    ('cache ainsi −64,3 points de dégât et +60,7 points de compensation',
     'cache ainsi 64,3 points de dégât et 60,7 points de compensation'),
    ('le prix de l’auditabilité se chiffre à son tour, <strong>8,3 ms',
     'le prix de l’auditabilité se chiffre à son tour : <strong>8,3 ms'),
    # 8.3
    ('sur-bloque massivement', 'surbloque massivement'),
    # 9.3 : [43] et [47]; portée de la lacune de responsabilité
    ('symétriquement, les deux pièces AP2 ignorent x402 [116], [117].',
     'symétriquement, les deux pièces AP2 ignorent x402 [116], [117], que le socle soumet pourtant à deux '
     'analyses d’attaque [43], [47].'),
    ('<p>Première lacune : aucune pièce ne traite la responsabilité d’une transaction non autorisée.',
     '<p>Première lacune : aucune pièce du corpus ne traite la responsabilité d’une transaction non autorisée.'),
    ('une pile assurantielle qui présuppose résolue l’allocation de responsabilité qu’elle ne traite pas [45].',
     'une pile assurantielle qui présuppose résolue l’allocation de responsabilité qu’elle ne traite pas '
     '[45]. La doctrine juridique des paiements — mandats électroniques, régimes de la DSP2 ou du '
     'règlement E américain — se publie en revues de droit, hors du périmètre d’arXiv : la lacune est '
     'celle du corpus, non celle du droit.'),
    # 10.1 : [136]; chiffre de [127] révisé
    ('la gouvernance des agents en processus [32].</p>',
     'la gouvernance des agents en processus [32]. La seule pièce du front attestée en revue mesure '
     'autre chose : la compétence des modèles de langue à produire un modèle de processus, non '
     'l’exécution d’un agent [136].</p>'),
    ('à moins de 6 % de surcoût [127].',
     'à moins de 6 % de surcoût dans la version citée, de 5,2 à 6,6 % depuis sa v3 du 31 août 2026 '
     '(tableau 10) [127].'),
    # 10.2 : [134] révisée
    ('des portes d’approbation humaine des invariants applicables [134]',
     'des portes d’approbation humaine des invariants applicables [134], doté depuis sa v3 d’une preuve '
     'et d’une mesure (tableau 10),'),
    # 10.3 : portée de la requête; conformité imposée et vérification binaire
    ('pas l’exécution d’un agent contre un modèle métier.</p>',
     'pas l’exécution d’un agent contre un modèle métier. La requête est un indicateur, non une preuve '
     'd’absence : la gestion des processus publie surtout hors d’arXiv, et nomme aussi la chose '
     'alignement de trace ou conformité d’exécution. Deux frontières bornent la lacune. Un contrôleur '
     'formel qui pilote l’agent — le graphe DCR de [137], les invariants d’approbation de [134] — '
     'impose la conformité par construction, <em>a priori</em> ; ce qui manque est le contrôle <em>a '
     'posteriori</em> d’une trace d’agent peu contrainte contre un modèle prescrit. Et la vérification '
     'de trace contre une spécification TLA+ ou LTL [171], [172] rend une acceptation binaire, non la '
     '<em>fitness</em> et la précision de la discipline.</p>'),
    # 11.1 : [192], rattachée à la gouvernance (tableau 2), instruite à son front (règle 2.1)
    ('l’énoncé d’ouverture sur l’ampleur de la délégation en finance y est argumenté, non mesuré.</p>',
     'l’énoncé d’ouverture sur l’ampleur de la délégation en finance y est argumenté, non mesuré.</p>\n'
     '<p>Une seconde étude déposée la veille, de 5 280 épisodes pré-spécifiés sur quatre familles de '
     'modèles, déplace la même question vers l’institution qui gouverne la délégation : sur le critère de '
     'sortie, une invite constitutionnelle détaillée et un garde exécutable sensible à la provenance '
     'produisent chacun zéro violation réalisée sur 384 épisodes (le second bloquant au passage 51 '
     'tentatives, dont 44 s’achèvent ensuite sans infraction) ; en scénarios appariés de blanchiment, où '
     'une transformation ordinaire modifie la politique visible sans changer l’autorité d’origine, un garde '
     'qui ne lit que l’état local admet 22 violations sur 96 contre zéro sous application par provenance '
     '[192]. <em>Le taux final ne distingue donc pas seul la règle de son point d’appui : comptent l’état '
     'd’autorité que l’institution consulte et l’issue ouverte après un refus (14.1, 15.3).</em> Régime : '
     'prépublication non révisée par les pairs, d’un auteur unique, dépôt public de reproductibilité, non '
     'répliquée.</p>'),
    # 11.2 : renvoi
    ('<em>La mise en garde de cette revue tient donc toujours :',
     '<em>La mise en garde de méthode de cette revue (3.1, 17) tient donc toujours :'),
    # 12 : registres vérifiables
    ('Ce front compte quatre mesures, dont une seule arbitrée, trois propositions d’architecture, trois '
     'positions, et aucune simulation.',
     'Ce front compte quatre mesures, dont une seule arbitrée — [151], [152], [154], [158] —, trois '
     'propositions d’architecture — [149], [150], [156] —, trois positions — [153], [155], [157] —, et '
     'aucune simulation.'),
    # 13 : erratum 1 du 1er novembre, appliqué à sa place
    ('Aucune de ses seize pièces n’est publiée en comité de lecture —',
     'Aucune de ses seize pièces n’atteste en notice une publication en comité de lecture —'),
    ('ne porte aucun signe de revue [180].</p>',
     'ne porte aucun signe de revue [180]. Crossref établit depuis trois publications, [164], [171] et '
     '[172] (annexe de novembre).</p>'),
    # 13.1 : [160] révisée
    ('+10,5 points sur SWE-bench Verified à coût par tâche réduit de moitié [160]',
     '+10,5 points sur SWE-bench Verified à coût par tâche réduit de moitié dans la version citée, '
     'chiffres changés à la v3 du 4 octobre 2026 (tableau 10) [160]'),
    ('compromet la multi-agents à 80 %', 'compromet le système multi-agents à 80 %'),
    ('tombe de 68-75 % à 6-13 %', 'tombe de 68–75 % à 6–13 %'),
    # 14.1
    ('une attaque compromettant la multi-agents à 80 %', 'une attaque compromettant le système multi-agents à 80 %'),
    # 14.3 : dénominateurs
    ('les pièces entrées à la reprise du 15 août n’y sont pas comptées, et la répartition par front, '
     'elle, les compte.</em>',
     'les pièces entrées à la reprise du 15 août n’y sont pas comptées, ni dans les fractions par front '
     'ci-dessus, quand la répartition du tableau 2, elle, les compte.</em>'),
    # tableau 6
    ('idempotent / réversible /compensable / irréversible', 'idempotent / réversible / compensable / irréversible'),
    # tableau 7 : sécurité
    ('<td>[74] sous attaque adaptative [71], coût d’utilité publié</td>',
     '<td>[74] sous attaque adaptative [71], coût d’utilité publié comme l’est celui de CaMeL sur AgentDojo</td>'),
    # 15 : numéros doublés
    ('<h3>15.1 1. « ', '<h3>15.1 « '),
    ('<h3>15.2 2. « ', '<h3>15.2 « '),
    ('<h3>15.3 3. « ', '<h3>15.3 « '),
    # 15.3 : [112] n'est attestée qu'en commentaire; publiée hors notice
    ('La seule pièce arbitrée du front étend la provenance W3C aux flux agentiques',
     'La pièce du front bâtie sur la provenance du W3C — acceptation annoncée au seul champ de '
     'commentaire, publication à eScience 2025 établie hors notice (annexe de novembre) — l’étend aux '
     'flux agentiques'),
    # références : en-tête
    ('nomment quatre entrées ainsi qualifiées dont une base de littérature arbitrée établit la publication.</em></p>',
     'nomment quatre entrées ainsi qualifiées dont une base de littérature arbitrée établit la publication. '
     'Le champ de commentaire est cité dans ses 55 premiers caractères, la coupure marquée « […] ». Les bancs '
     'que plusieurs pièces emploient sans y être discutés — AgentDojo, SWE-bench et sa sélection Verified '
     '(Jimenez <em>et al.</em>, ICLR 2024) — sont nommés comme instruments, sans entrée, comme les normes '
     'et les primitifs invoqués en référentiel.</em></p>'),
    # annexe du 29 octobre : appel du tableau 9
    ('<p>Seize notices ont bougé en soixante-quinze jours :',
     '<p>Seize notices ont bougé en soixante-quinze jours (tableau 9) :'),
]

# Entrées de la bibliographie dont le champ de commentaire est coupé à 55 caractères
# (55 ou moins après retrait de l'espace final), vérifiées contre les notices le 3 novembre
# 2026; [131] fait exactement 55 caractères et n'est pas coupée.
COMMENTAIRES_COUPES = {7, 8, 32, 33, 61, 66, 79, 99, 103, 112, 113, 133, 135, 137, 145, 155, 156, 172, 183}


# Corrections issues de l'audit complet (lots RL1, RL2, RL3, RL4, O-19, O-23, § 10.8)
AUDIT_CORRECTIONS = [
    # RL1-01 (Majeure, 6.1 et légende Tableau 3)
    (
        "Trois travaux indépendants, qui ne se citent pas et ne partagent ni domaine d’application ni vocabulaire, obtiennent des gains d’ordre cent sur les baux temporels et sur OAuth 2.0. <em>Les trois ne les obtiennent pas au même régime, et la colonne de droite le dit : un facteur mesuré en simulation et un facteur mesuré sur essaim d’agents réels ne s’additionnent pas.</em>",
        "Trois travaux indépendants, qui ne se citent pas et ne partagent ni domaine d’application ni vocabulaire, lient la validité à un événement ; deux en chiffrent le gain, d’ordre cent, sur les baux temporels [75] et sur OAuth 2.0 [80], tandis que le troisième ferme l’accès futur sans facteur chiffré [87]. <em>Ils ne portent pas le même régime, et la colonne de droite du tableau 3 le dit : un facteur mesuré en simulation et un facteur mesuré sur essaim d’agents réels ne s’additionnent pas.</em>",
    ),
    (
        "Trois voies indépendantes vers une validité liée à un événement, chacune avec le régime où son gain a été obtenu.</caption>",
        "Trois voies indépendantes vers une validité liée à un événement, chacune avec le régime où son gain ou son effet a été obtenu.</caption>",
    ),
    # RL1-02 (2.2, 3.1) + RL2-12 (Annexe corpus arbitré)
    (
        "<em>Le premier relevé de cette revue ne retenait que le premier des deux champs et comptait sept pièces là où il y en a douze ; l’écart a été trouvé en confrontant les notices aux entrées, et il est rapporté ici plutôt que corrigé en silence.</em>",
        "<em>Le premier décompte de cette revue, sur le relevé du 9 août, ne retenait que le premier des deux champs et comptait sept pièces là où les notices en portaient déjà douze ; l’écart a été corrigé le 15 août en confrontant les notices aux entrées de la bibliographie, et il est rapporté ici plutôt qu’en silence.</em>",
    ),
    (
        "les mêmes douze qu’au relevé du 9 août :",
        "les mêmes douze que portaient les notices du 9 août, que le premier décompte réduisait à sept (corrigé le 15 août, 2.2) :",
    ),
    (
        "La liste est inchangée depuis le relevé du 9 août : en une semaine, aucune pièce n’y est entrée, aucune n’en est sortie, et les seize arrivées au corpus n’en approchent pas.",
        "Les notices de ces douze pièces sont inchangées depuis le relevé du 9 août (dont le premier décompte ne retenait que sept pièces, corrigé le 15 août, 2.2) : en une semaine, aucune pièce n’y est entrée, aucune n’en est sortie, et les seize arrivées au corpus n’en approchent pas.",
    ),
    # RL1-03 (1, p. 4)
    (
        "une littérature qui double de volume en douze mois n’a pas eu le temps d’être filtrée",
        "un corpus dont plus de six pièces sur dix ont été déposées dans les huit premiers mois de 2026 n’a pas eu le temps d’être filtré",
    ),
    # RL1-04 (CaMeL [259] en 5.1, 5.2, Tableau 7, en-tête des références) + RL2-19 (AgentDojo, SWE-bench)
    (
        "CaMeL (Debenedetti <em>et al.</em>, arXiv:2503.18813, 2025) sépare flux de contrôle et flux de données",
        "CaMeL (Debenedetti <em>et al.</em>, arXiv:2503.18813, 2025 [259]) sépare flux de contrôle et flux de données",
    ),
    (
        "à sept points de tâches résolues sur AgentDojo pour CaMeL (5.1).",
        "à sept points de tâches résolues sur AgentDojo pour CaMeL [259] (5.1).",
    ),
    (
        "<td>[74] sous attaque adaptative [71], coût d’utilité publié comme l’est celui de CaMeL sur AgentDojo</td>",
        "<td>[74] sous attaque adaptative [71], coût d’utilité publié comme l’est celui de CaMeL [259] sur AgentDojo</td>",
    ),
    (
        "Les bancs que plusieurs pièces emploient sans y être discutés — AgentDojo, SWE-bench et sa sélection Verified (Jimenez <em>et al.</em>, ICLR 2024) — sont nommés comme instruments, sans entrée, comme les normes et les primitifs invoqués en référentiel.</em></p>",
        "Les bancs que plusieurs pièces emploient sans y être discutés — SWE-bench (Jimenez <em>et al.</em>, ICLR 2024) et sa sélection Verified (OpenAI, 2024), AgentDojo (Debenedetti <em>et al.</em>, NeurIPS 2024) — sont nommés comme instruments, sans entrée, comme les normes et les primitifs invoqués en référentiel, tandis que l’architecture CaMeL, citée à la section 5.1, fait l’objet de l’entrée [259] et la veille technologique compagnon de l’entrée [260].</em></p>",
    ),
    # RL1-05 (Veille technologique [260] en 1.2, 2.1, Tableau 2, 15, 17, Annexe 29 oct.)
    (
        "Cette revue prolonge une veille technologique du même auteur, qui dresse l’état du champ sur sources primaires : spécifications, dépôts de code, communiqués de fondations, textes réglementaires.",
        "Cette revue prolonge une veille technologique du même auteur (<em>Veille technologique en entreprise — Interopérabilité et Orchestration Agentiques</em>, édition gelée au 15 août 2026, reprise du 29 octobre et actualisation du 11 novembre 2026 [260]), qui dresse l’état du champ sur sources primaires : spécifications, dépôts de code, communiqués de fondations, textes réglementaires.",
    ),
    (
        "La première est le socle hérité de la veille : ses 50 pièces académiques",
        "La première est le socle hérité de la veille [260] : ses 50 pièces académiques",
    ),
    (
        "<td>Socle hérité de la veille</td>",
        "<td>Socle hérité de la veille [260]</td>",
    ),
    (
        "Auto-citation déclarée : la veille dont trois énoncés sont ici mis à l’épreuve est du même auteur.",
        "Auto-citation déclarée : la veille dont trois énoncés sont ici mis à l’épreuve est du même auteur [260].",
    ),
    (
        "La reprise du 29 octobre de la même veille — auto-citation déclarée — les rouvre ; aucun verdict de la section 15 n’en est déplacé.",
        "La reprise du 29 octobre de la même veille [260] — auto-citation déclarée — les rouvre ; aucun verdict de la section 15 n’en est déplacé.",
    ),
    # RL1-06 (5.1, p. 10)
    (
        "<em>Le gel du 9 août écrivait « aucune » : la pièce conclut sur « presque toutes », et la correction est faite ici plutôt qu’en silence.</em>",
        "<em>Le relevé du 9 août écrivait qu’aucune n’est déployable ; la pièce dit que presque toutes sont insuffisamment sûres ou sur-défensives, et la correction est faite ici plutôt qu’en silence.</em>",
    ),
    # RL1-07 (8.2, p. 17)
    (
        "Deux pièces de la mi-août prennent le second parti et le chiffrent.",
        "Deux pièces de la mi-août prennent le second parti : [189] le chiffre ; [182] en décrit le coût sans le chiffrer.",
    ),
    # RL1-08 (6.1, p. 13)
    (
        "Le seul parc d’entreprise décrit dans le corpus est arrivé le 11 août.",
        "Le seul rapport de déploiement d’un parc de serveurs d’agents d’entreprise dans le corpus est arrivé le 11 août — la flotte infonuagique de [82] modélisant des identités non humaines générales.",
    ),
    # RL1-09 (4.1, p. 8)
    (
        "par quatre chemins indépendants.",
        "par quatre pièces indépendantes et trois voies : empirique, formelle, analytique.",
    ),
    # RL1-10 (3.1, p. 7)
    (
        "77\xa0% des énoncés retenus ici ne déclarent aucun comité à leur notice",
        "77\xa0% des pièces arXiv retenues ici ne déclarent aucun comité à leur notice",
    ),
    # RL1-11 (8.2, p. 17)
    (
        "un banc d’affaires est publié par le fournisseur du produit agentique concurrent du domaine évalué [104].",
        "un banc d’affaires est publié par l’éditeur d’un produit agentique du domaine évalué (Salesforce), qu’il mesure aux côtés des concurrents [104].",
    ),
    # Coquilles RL1 (p. 9 non archival, p. 15 sur-créditée, p. 15 ordre [94], [95])
    (
        "déclare lui-même non archival.",
        "déclare lui-même non archivé (<em>non-archival</em>).",
    ),
    (
        "est sur-créditée exactement quand",
        "est surcréditée exactement quand",
    ),
    (
        "[92], [93], [95], [94]",
        "[92], [93], [94], [95]",
    ),
    # RL2-01 (Majeure, Annexe 29 oct., p. 47)
    (
        "Quatorze révisions en dix semaines : 7\xa0% du corpus, au rythme que mesurait la section 3.1.",
        "Quatorze révisions en dix semaines : 7\xa0% du corpus (environ 2,8\xa0% par mois), soit un rythme nettement inférieur aux 15\xa0% observés sur le seul mois de juin à la section 3.1.",
    ),
    # RL2-02 (Majeure, 15.2, p. 29)
    (
        "Mais quatre formalismes conçus <em>pour</em> les agents existent depuis fin 2024 :",
        "Mais quatre formalismes conçus <em>pour</em> les agents ont paru de décembre 2024 à août 2026 :",
    ),
    # RL2-03 (15 intro et 15.1, p. 28) + RL1-05
    (
        "Ces trois énoncés proviennent d’une veille sur sources primaires — brouillons de normalisation, moteurs d’orchestration, conventions d’observabilité — arrêtée au 8 août 2026.",
        "Ces trois énoncés proviennent d’une veille sur sources primaires — brouillons de normalisation, moteurs d’orchestration, conventions d’observabilité — arrêtée au 15 août 2026 (énoncés issus de la passe du 8 août, inchangés à l’édition du 15 août) [260].",
    ),
    (
        "Qu’un brouillon de délégation ait avancé, stagné ou été adopté depuis le 8 août ne change ni le constat d’invention ni l’absence de mesure de terrain",
        "Qu’un brouillon de délégation ait avancé, stagné ou été adopté depuis le 15 août ne change ni le constat d’invention ni l’absence de mesure de terrain",
    ),
    # RL2-04 et RL2-05 (18, p. 32)
    (
        "Un corpus dont les trois quarts ne déclarent aucun comité à leur notice, dont la moitié évalue une construction de ses propres auteurs, et dont trois fronts indépendants concluent que l’instrument de mesure est faux, ne peut pas à lui seul arbitrer une décision d’architecture.",
        "Un corpus dont les trois quarts ne déclarent aucun comité à leur notice, dont plus de la moitié des pièces de front évaluent une construction de leurs propres auteurs, et dont trois fronts indépendants concluent que l’instrument de mesure est le maillon faible, ne peut pas à lui seul arbitrer une décision d’architecture.",
    ),
    # RL2-06 (14.1, p. 26)
    (
        "<p>Les dix fronts convergent sur un énoncé qu’aucun ne porte seul :",
        "<p>Neuf des dix fronts convergent sur un énoncé qu’aucun ne porte seul :",
    ),
    # RL2-07 (11.1, p. 22)
    (
        "un garde qui ne lit que l’état local admet 22 violations sur 96 contre zéro sous application par provenance [192].",
        "un garde qui ne lit que l’état local admet des violations dans 22 épisodes sur 96, contre aucun sous application par provenance [192].",
    ),
    # RL2-08 (15.3, p. 29)
    (
        "en bloquant au passage 51 tentatives sur 384, dont 44 aboutissent quand même ensuite [192].",
        "en bloquant au passage 51 tentatives sur 384, dont 44 épisodes s’achèvent ensuite sans infraction [192].",
    ),
    # RL2-09 (Tableau 8, p. 32)
    (
        "<td>Propose l’échelle d’autonomie la plus citée du champ, et la seule opérationnalisable</td>",
        "<td>Propose une échelle de niveaux d’AGI et d’autonomie conçue pour être opérationnalisable</td>",
    ),
    # RL2-10 (17, p. 31)
    (
        "aucun verdict de la section précédente n’y est suspendu.",
        "aucun verdict de la section 15 n’y est suspendu.",
    ),
    # RL2-11 (3.1 p. 7, 18 p. 32, Annexe corpus arbitré p. 33)
    (
        "et la passe de contrôle sur DBLP et Crossref rapportée aux limites trouve de la littérature arbitrée",
        "et la passe de contrôle sur DBLP, Crossref et OpenAlex rapportée aux limites trouve de la littérature arbitrée",
    ),
    (
        "La passe de contrôle sur DBLP et Crossref, rapportée aux limites, borne ce constat dans les deux sens :",
        "La passe de contrôle sur DBLP, Crossref et OpenAlex, rapportée aux limites, borne ce constat dans les deux sens :",
    ),
    (
        "DBLP et Crossref donnent de la littérature arbitrée sur quatre de ces six fronts",
        "DBLP, Crossref et OpenAlex donnent de la littérature arbitrée sur quatre de ces six fronts",
    ),
    # RL2-13 (Clarification des références au « gel » dans le corps)
    (
        "La lacune de second rang du gel s’est en revanche comblée.",
        "La lacune de second rang du relevé du 9 août s’est en revanche comblée.",
    ),
    (
        "Les quatorze pièces du front retenues au gel du 9 août :",
        "Les quatorze pièces du front retenues au relevé du 9 août :",
    ),
    (
        "le gel du 9 août les présentait comme une seule.",
        "le relevé du 9 août les présentait comme une seule.",
    ),
    (
        "Le gel du 9 août désignait à cette place l’attribution de responsabilité ;",
        "Le relevé du 9 août désignait à cette place l’attribution de responsabilité ;",
    ),
    (
        "La trace comme preuve reste hors banc, mais l’énoncé du gel était trop large.",
        "La trace comme preuve reste hors banc, mais l’énoncé du relevé du 9 août était trop large.",
    ),
    (
        "aucune des douze notices du front n’a bougé depuis le gel, et la fenêtre du 9 au 15 août n’a rien livré",
        "aucune des douze notices du front n’a bougé depuis le relevé du 9 août, et la fenêtre du 9 au 15 août n’a rien livré",
    ),
    (
        "Contrôle vérifiable, refait à l’API du dépôt le 15 août 2026 et de compte inchangé depuis le gel :",
        "Contrôle vérifiable, refait à l’API du dépôt le 15 août 2026 et de compte inchangé depuis le relevé du 9 août :",
    ),
    (
        "un mouvement de ce dernier depuis le gel déplace la date d’un fait, jamais la conclusion.",
        "un mouvement de ce dernier depuis le gel du 15 août déplace la date d’un fait, jamais la conclusion.",
    ),
    (
        "si l’un d’eux a publié depuis le gel des primitives agentiques natives",
        "si l’un d’eux a publié depuis le gel du 15 août des primitives agentiques natives",
    ),
    (
        "sept entrées classées sans revue dont l’identifiant arXiv est antérieur au gel —,",
        "sept entrées classées sans revue dont l’identifiant arXiv est antérieur au gel du 15 août —,",
    ),
    # RL2-14 (13.1 et 13.3, p. 25-26)
    (
        "des milliers d’agents produisent 45 000 déclarations Lean 4",
        "un millier d’agents produisent 45 000 déclarations Lean 4",
    ),
    (
        "[169] atteint le millier sans courbe de coût",
        "[169] atteint le millier d’agents sans courbe de coût",
    ),
    # RL2-15 (Tableau 7, p. 28)
    (
        "RIA opérationnalisable [138] ou inadéquat [139]",
        "Règlement européen sur l’IA opérationnalisable [138] ou inadéquat [139]",
    ),
    # RL2-16 (Tableau 10, p. 47)
    (
        "<td>[164] (13.2)</td><td>v2 → v3, 30 août</td><td>(F+1)-robustesse sur le graphe</td><td>résumé inchangé quant au fond ; acceptation à EMNLP 2026 annoncée</td>",
        "<td>[164] (13.2)</td><td>v2 → v3, 30 août</td><td>(F+1)-robustesse sur le graphe</td><td>formulation du résumé retouchée (borne de (F+1)-robustesse inchangée) ; acceptation à EMNLP 2026 annoncée au commentaire</td>",
    ),
    # RL2-17 / O-19 (Annexe 29 oct., p. 46)
    (
        "corrige quatre erreurs relevées à la relecture.",
        "corrige quatre erreurs relevées à la relecture (tableau 11).",
    ),
    # RL2-18 (15.1, p. 28)
    (
        "Une vérification en TLA+ sur 2,7 M d’états établit, à profondeur arbitraire, rétrécissement d’autorité",
        "Une vérification en TLA+ sur 2,7 M d’états établit rétrécissement d’autorité",
    ),
    # RL2-20 (Tableau 8, p. 33)
    (
        "<td>Actes ACM, 2026</td>",
        "<td>Actes CAIS ’26 (ACM)</td>",
    ),
    # Coquille RL2 (9.3, p. 19)
    (
        "Permit2, EIP-8004, Kite",
        "Permit2, ERC-8004, Kite",
    ),
    # RL3-12 (3.1 p. 7 et Annexe 29 oct. p. 47)
    (
        "136 pièces sur 189, soit 72\xa0%, ont été révisées pour la dernière fois en 2026",
        "136 pièces sur 189, soit 72\xa0%, ont leur version courante datée de 2026",
    ),
    (
        "137 ont été révisées pour la dernière fois en 2026",
        "137 ont leur version courante datée de 2026",
    ),
    # RL4-02 (12.3, p. 24)
    (
        "Six jours de production sur le sujet, et pas un énoncé raccordable aux échelles d’autonomie.",
        "Six jours d’intervalle (sept dates, du 9 au 15 août) de production sur le sujet, et pas un énoncé raccordable aux échelles d’autonomie.",
    ),
    # RL4-18 (Tableau 11, p. 48)
    (
        "le champ <code>journal_ref</code> porte « MSR “26 »",
        "le champ <code>journal_ref</code> porte <code>MSR '26</code>",
    ),
    # § 10.8 et audit-references.md ([103], [127], [134])
    (
        "https://github.com/All-Han […]",
        "https://github.com/All-Hands-AI/OpenHands",
    ),
    (
        "Edward Y. Chang, Longling Geng <em>et al.</em> « Mnemosyne:",
        "Edward Y. Chang et Longling Geng. « Mnemosyne:",
    ),
    (
        "Ylli Prifti. « Specifying AI-SDLC Processes:",
        "Ylli Prifti <em>et al.</em> « Specifying AI-SDLC Processes:",
    ),
    # RL1-05 (1.2, p. 4) : le signalement est le renvoi [260], non un signalement « à chaque renvoi »
    (
        "L’auto-citation est déclarée ici et signalée à chaque renvoi.",
        "L’auto-citation est déclarée ici ; le renvoi [260] la signale aux sections 2.1, 3.2, 15 et 17 et dans les annexes.",
    ),
    # COQ-Vei-251 (suite, 1.2) : le titre de la veille est cité comme sa page de titre le porte
    (
        "Interopérabilité et Orchestration Agentiques</em>, édition gelée au 15 août 2026",
        "Interopérabilité et orchestration agentiques</em>, édition gelée au 15 août 2026",
    ),
]


def corriger(s):
    for ancien, nouveau in CORRECTIONS:
        n = s.count(ancien)
        assert n == 1, f'correction : passage trouvé {n} fois : {ancien[:80]}'
        s = s.replace(ancien, nouveau)
    # appels groupés : séparés par une virgule, comme dans le reste du texte
    s = re.sub(r'(\[\d+\]) (?=\[\d+\])', r'\1, ', s)
    # pas de « % » rejeté en début de ligne
    s = re.sub(r'(?<=\d) %', NBSP + '%', s)
    # commentaires coupés : la coupure est marquée
    debut = s.index('<h2>Références</h2>')
    fin = s.index('</ol>', debut)
    entrees = s[debut:fin].split('<li>')
    for n in COMMENTAIRES_COUPES:
        e, k = re.subn(r'(<em>Comments</em> \(« .*?)( »\))', r'\1 […]\2', entrees[n], count=1)
        assert k == 1, f'commentaire de [{n}] introuvable'
        entrees[n] = e
    s = s[:debut] + '<li>'.join(entrees) + s[fin:]
    # corrections issues de l'audit
    for ancien, nouveau in AUDIT_CORRECTIONS:
        n = s.count(ancien)
        assert n == 1, f'audit_correction : passage trouvé {n} fois : {ancien[:80]}'
        s = s.replace(ancien, nouveau)
    # O-23 : « le 1 <mois> » / « du 1 <mois> » -> « 1er »
    s = re.sub(
        r'\b(le|du) 1 (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\b',
        r'\1 1er \2',
        s,
    )
    # Coquille RL1 : harmoniser « auto-déclaré(e)(s) » en « autodéclaré(e)(s) » dans tout le document
    s = s.replace('auto-déclaré', 'autodéclaré')
    return s
