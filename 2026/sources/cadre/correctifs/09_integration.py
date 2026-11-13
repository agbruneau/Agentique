"""Intégration des correctifs de l'audit du 11 novembre 2026 : reprises transversales, après les lots 05 à 08.

L'EXIG-GOV-21 de la v1.2 (régime transitoire des agents existants) n'existe pas dans la v1.1 : son contenu y est le
paragraphe « Régime transitoire et exigibilité » de la section 11.6, rattaché aux EXIG-GOV-16 et EXIG-GOV-17. Les
renvois ajoutés à l'EXIG-GOV-21 par la reprise du 12 novembre visaient donc une exigence absente du registre D.
"""

RT = 'régime transitoire de la section 11.6 (EXIG-GOV-16 et EXIG-GOV-17)'

CORRECTIONS = [
    ('y sont ramenés selon le régime transitoire de l’EXIG-GOV-21 (chapitre 5, chapitre 9).</li>',
     f'y sont ramenés selon le {RT}.</li>', 'Intégration GOV-21'),
    ('(état cible; agents existants\xa0: EXIG-GOV-21)',
     '(état cible; agents existants\xa0: régime transitoire de la section 11.6)', 'Intégration GOV-21'),
    ('les niveaux et les topologies qu’il exerce (EXIG-GOV-21).</p>',
     'les niveaux et les topologies qu’il exerce (régime transitoire de la section 11.6).</p>', 'Intégration GOV-21'),
    ('le tableau 58, pour ses phases d’exigibilité (EXIG-GOV-21) et',
     'le tableau 58, pour ses phases d’exigibilité (régime transitoire de la section 11.6) et', 'Intégration GOV-21'),
    ('suit le régime transitoire de l’EXIG-GOV-21;', f'suit le {RT};', 'Intégration GOV-21'),
    ('<caption>Tableau 50 — Matrice de correspondance : NIST AI RMF, ISO/IEC 42001, Loi 25, RIA et artefacts du cadre',
     '<caption>Tableau 50 — Matrice de correspondance : NIST AI RMF, ISO/IEC 42001, Loi 25, BSIF, RIA et artefacts du cadre',
     'COQ-Cad-189'),
]

JOURNAL = [
    ('Sommaire (décisions 2 et 5, « Par où commencer »); § 1.4; § 1.6',
     'Renvois à une EXIG-GOV-21 absente du registre ramenés au régime transitoire de la section 11.6 '
     '(EXIG-GOV-16 et EXIG-GOV-17)', 'Intégration'),
    ('Tableau 50 (légende et liste des tableaux)', 'BSIF ajouté au titre : le tableau a une colonne BSIF', 'COQ-Cad-189'),
]
