"""Correctifs de l'audit du 11 novembre 2026, lot « comp-b » (Compendium, Livres II à IV : K04, K05, K06, K07, V1, L04 à L07, coquilles)."""

CORRECTIONS = [
    # =========================================================================
    # LIVRE II (K04, L04)
    # =========================================================================

    # K04-03 — § 18.1 : le tableau 18.1 porte des re-datations; l'échéance de septembre vise le -00
    ("<em>Un compteur affiché n'est pas un fait stable</em> — le tableau conserve le relevé du 21 juillet 2026, qui porte sa date.</p>",
     "<em>Un compteur affiché n'est pas un fait stable</em> — le tableau conserve le relevé du 21 juillet 2026 pour les décomptes de participants, et date chacune des re-datations des <em>Internet-Drafts</em> qu'il porte, jusqu'au 21 octobre 2026.</p>",
     "K04-03a"),
    ("<em>l'échéance de septembre est sans objet</em> ;",
     "<em>l'expiration du <code>-00</code>, en septembre 2026, est sans objet</em> ;",
     "K04-03b"),

    # K04-23 — § 20.10 : la jonction F-56 / F-73 est refusée au § 18.1
    ("<p>Une pièce du même mouvement est établie par deux instructions distinctes, avec des bornes différentes, et la convergence vaut d'être dite : le document de concept",
     "<p>Une pièce du même mouvement est établie par une instruction distincte de celle de l'initiative, avec une borne différente : le document de concept",
     "K04-23a"),
    ("(F-73, <strong>[B]</strong>, convergent avec l'initiative F-56 en <strong>[C]</strong>, sans fusionner les deux entrées conformément au § 18.1)",
     "(F-73, <strong>[B]</strong>). Le socle ne documente pas si cette pièce et le volet identité de l'initiative (F-56, <strong>[C]</strong>) désignent le même document : les deux entrées restent portées séparément, conformément au § 18.1",
     "K04-23b"),

    # K04-25 — § 21.0 : le ch. 18 porte des échéances PROGRAMMÉES (expirations d'Internet-Drafts)
    ("les propositions du ch.\xa018 sont <strong>sans jalon</strong>",
     "les propositions du ch.\xa018 ne portent, pour toute échéance, que l'expiration mécanique de leurs <em>Internet-Drafts</em> (PROGRAMMÉE, sans portée sur l'adoption)",
     "K04-25"),

    # =========================================================================
    # LIVRE III — PREMIER MOUVEMENT (K05)
    # =========================================================================

    # K05-27 — le ratio de 82 pour 1 vient du rapport CyberArk 2025; au ch. 24 § 24.0.2, l'attribution est déjà rétablie.
    # Reste le renvoi du Vol. I, qui l'attribue à Rubrik Zero Labs seule.
    ("un rapport de <strong>82 pour 1</strong> attribué à Rubrik Zero Labs (2025) — chiffre de fournisseur, issu d'une enquête commanditée, que le Vol. I marque",
     "un rapport de <strong>82 pour 1</strong> attribué à Rubrik Zero Labs (2025), qui le relaie d'après un rapport CyberArk de 2025 (enquête Vanson Bourne ; ch.\xa024 § 24.0.2) — chiffre de fournisseur, issu d'une enquête commanditée, que le Vol. I marque",
     "K05-27"),

    # =========================================================================
    # LIVRE III — TROISIÈME MOUVEMENT (K07)
    # =========================================================================

    # K07-33 — Tableau 36.2, Q2 : le cessionnaire est une alliance; son critère de neutralité n'est pas établi
    ("<em>la question est close pour l'annonce, ouverte pour la matérialisation du transfert et pour ce qu'il emporte</em></td></tr><tr><td><strong>Q3</strong>",
     "<em>la question est close pour l'annonce, ouverte pour la matérialisation du transfert et pour ce qu'il emporte ; le socle ne documente pas si cette alliance répond au critère de neutralité que la question vise (absence de documentation, degré 3)</em></td></tr><tr><td><strong>Q3</strong>",
     "K07-33"),

    # =========================================================================
    # LIVRE II (L04)
    # =========================================================================

    # L04-12 — § 21.1 : échéances OMB échues; la mention « voir annexe N » renvoie à une annexe qui n'en traite pas
    ("(échéances de 90 et 120 jours échues en septembre et octobre 2026 ; l'état de publication des plans d'agence correspondants n'a pas été ré-instruit au gel, voir annexe N)",
     "(échéances de 90 et 120 jours échues en septembre et octobre 2026, si elles courent des dates de signature — le point de départ des délais n'est pas précisé ici ; l'état de la directive de l'OMB et celui des plans d'agence correspondants n'ont pas été ré-instruits au gel, et l'annexe N ne les traite pas : absence de documentation dans le corpus, degré 3)",
     "L04-12"),

    # =========================================================================
    # COQUILLES (COQ-Com-…)
    # =========================================================================

    # COQ-Com-016 — § 21.8 : le sigle CFDIR est déjà développé (02_livres1_2.py), mais le développement n'est pas le bon.
    # CFDIR = Canadian Forum for Digital Infrastructure Resilience (recherche en ligne du 13 novembre 2026, pages d'ISDE et du forum).
    ("(<em>Canadian Financial Sector Post-Quantum Cryptography</em> / forum canadien de préparation post-quantique du secteur financier)",
     "(<em>Canadian Forum for Digital Infrastructure Resilience</em>, forum canadien pour la résilience des infrastructures numériques)",
     "COQ-Com-016"),

    # COQ-Com-102 — un seul terme, « préimpression » : restent deux « Préprint » à l'annexe B
    ("Feuille de route académique. <code>[A]</code> — Vol. II <code>F-06</code> §7.1. Préprint de mai 2025, non révisé par les pairs.",
     "Feuille de route académique. <code>[A]</code> — Vol. II <code>F-06</code> §7.1. Préimpression de mai 2025, non révisée par les pairs.",
     "COQ-Com-102a"),
    ("§7.2. Préprint v1 du 30 juin 2026, non révisé par les pairs.",
     "§7.2. Préimpression v1 du 30 juin 2026, non révisée par les pairs.",
     "COQ-Com-102b"),

    # COQ-Com-107 — un seul terme, « humain dans la boucle » : reste une forme à traits d'union, au titre du § 34.1.2
    ("<h4>34.1.2 Front conversationnel et le revirement humain-dans-la-boucle</h4>",
     "<h4>34.1.2 Front conversationnel et le revirement humain dans la boucle</h4>",
     "COQ-Com-107"),
]

JOURNAL = [
    ('Ch. 18 (§ 18.1), phrase sur le tableau 18.1 et cellule IETF',
     "préciser que le tableau conserve le relevé du 21 juillet 2026 pour les décomptes et date ses re-datations; viser l'expiration du -00 plutôt que « l'échéance de septembre »",
     'K04-03'),
    ('Ch. 20 (§ 20.10), document de concept du NCCoE',
     "retirer la « convergence » de F-73 et F-56 et reprendre la réserve du § 18.1 (le socle ne documente pas s'il s'agit du même document)",
     'K04-23'),
    ('Ch. 21 (§ 21.0), introduction',
     "nuancer « sans jalon » : les propositions du ch. 18 ne portent que des expirations mécaniques d'Internet-Drafts (PROGRAMMÉES)",
     'K04-25'),
    ('Ch. 8 à 9 (renvoi au Vol. I § 4.1.3), ratio de 82 pour 1',
     "attribuer le ratio au rapport CyberArk 2025 (enquête Vanson Bourne), relayé par Rubrik Zero Labs, et renvoyer au ch. 24 § 24.0.2",
     'K05-27'),
    ('Ch. 21 (§ 21.1), note OMB M-26-15 et décret 14412',
     "dire que le point de départ des délais de 90 et 120 jours n'est pas précisé, que l'état de la directive et des plans d'agence n'a pas été ré-instruit et que l'annexe N ne le traite pas (degré 3)",
     'L04-12'),
    ('Ch. 21 (§ 21.8), sigle CFDIR',
     "rétablir le développement exact du sigle (Canadian Forum for Digital Infrastructure Resilience)",
     'COQ-Com-016'),
    ('Ch. 36 (tableau 36.2, Q2), transfert de gouvernance du protocole de paiement',
     "dire que le socle ne documente pas si l'alliance cessionnaire répond au critère de neutralité visé par la question",
     'K07-33'),
    ('Annexe B (entrées S-006 et S-035), « préprint »',
     "« Préprint » remplacé par « Préimpression » (un seul terme dans l'ouvrage)",
     'COQ-Com-102'),
    ('Ch. 34 (§ 34.1.2), intertitre',
     "« humain-dans-la-boucle » remplacé par « humain dans la boucle » (un seul terme dans l'ouvrage)",
     'COQ-Com-107'),
]
