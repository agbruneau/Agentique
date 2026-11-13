"""Intégration des correctifs de l'audit du 11 novembre 2026 : reprises transversales, après les lots 09 à 12."""

CORRECTIONS = [
    # V1-40 : texte de remplacement de la figure 22.1, aligné sur le titre retouché (PATCHS_FIGURES[50])
    ('alt="DEUX AXES : QUI SAIT, ET QUI COMMANDE OO1',
     'alt="DEUX AXES : QUI SAIT, ET QUI COMMANDE — EN HAUT, LES AGENTS COMMANDENT ; EN BAS, LE CADRE OO1',
     'V1-40'),
    # COQ-Com-067 / -082 (contradictoires) : « 1ᵉʳ », graphie majoritaire du corps (84 contre 12)
    (' 1er ', ' 1ᵉʳ ', 'COQ-Com-067/082', '*'),
    ('>1er ', '>1ᵉʳ ', 'COQ-Com-067/082', '*'),
    ('(1er ', '(1ᵉʳ ', 'COQ-Com-067/082', '*'),
    # COQ-Com-069 / -079 (contradictoires) : « revérif- », graphie majoritaire (46 contre 32) et des dictionnaires
    (' re-vérif', ' revérif', 'COQ-Com-069/079', '*'),
]

JOURNAL = [
    ('ch. 22, figure 22.1', 'Rangées de la grille nommées par l’axe « qui commande » (titre et texte de remplacement)',
     'V1-40'),
    ('corps', 'Harmonisation : « 1ᵉʳ » partout (12 « 1er »), « revérif- » partout (31 « re-vérif- »)',
     'COQ-Com-067, 069, 079, 082'),
]
