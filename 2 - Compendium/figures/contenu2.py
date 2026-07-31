#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures du barème A — Livre II (chapitres 12 à 21)."""
from spec import f, NOTE  # noqa: F401

f(12, "12.1", "f-12-01-genealogie",
  "Cinq moments documentés, de 2012 à 2026 : l'hypothèse humaine quitte les définitions.",
  "Cinq moments dates de la genealogie des identites non humaines, de 2012 a 2026.",
  "§ 12.1, chapitre 12.", r"^## § 12\.2 ", "frise",
  "Chacun a sa date, son statut et sa borne. Les fondre en une continuité produirait un RÉCIT là "
  "où le socle ne porte que des jalons — et c'est exactement ce que cette figure refuse de faire.",
  dict(titre="CINQ MOMENTS, ET AUCUNE CONTINUITÉ", jalons=[
      ("2012", "RFC 6749", "le détenteur de ressource est « une entité » ; « utilisateur final » est réservé au cas où c'est une personne", "plein"),
      ("…", "L'hypothèse humaine", "elle n'est pas dans les définitions : elle est dans le flux", "creux"),
      ("…", "Identité de charge", "l'exécution reçoit une identité propre, à courte durée de vie", "plein"),
      ("2026", "L'agent", "identité stable, comportement variable — § 12.3", "plein"),
  ]))

f(12, "12.4", "f-12-04-client-ou-detenteur",
  "L'agent dans OAuth : client ou détenteur de ressource ? Les deux placements, et ce que chacun engage.",
  "Les deux placements possibles d'un agent dans les roles du RFC 6749.",
  "§ 12.4, chapitre 12, sur le RFC 6749 § 1.1.", r"^## § 12\.5 ", "paire",
  "Rien dans les deux définitions n'écarte un mandataire logiciel — et rien ne l'y installe. "
  "Le RFC ne tranche pas : il n'avait pas la question. C'est un standard étiré, non un standard "
  "qui répond.",
  dict(titre_g="L'AGENT COMME CLIENT", titre_d="L'AGENT COMME DÉTENTEUR DE RESSOURCE",
       gauche=("« Une application qui demande des ressources protégées pour le compte d'autrui »",
               ["Le client est déjà, par construction, un mandataire",
                "L'agent hérite d'un rôle qui existe",
                "Mais le mandant reste hors du jeton"],
               "le rôle existe, la chaîne n'y est pas"),
       droite=("« Une entité capable d'accorder l'accès à une ressource protégée »",
               ["Le détenteur est une ENTITÉ, non nécessairement une personne",
                "« Utilisateur final » est réservé au cas humain",
                "Un agent peut donc en tenir le rôle"],
               "la définition l'admet, l'imputabilité s'y perd")))

f(13, "13.4", "f-13-04-ancrages",
  "Deux familles qui se disputent l'ancrage de l'identité sous le niveau applicatif.",
  "L'identite de charge de travail et l'identite decentralisee, et l'ancrage que chacune propose.",
  "§ 13.4, chapitre 13.", r"^## § 13\.5 ", "bandes",
  "Le Vol. I les oppose en régime [C] — c'est une lecture reprise, non un balayage de mécanismes "
  "conduit par la somme. Aucune des deux familles ne porte l'ancrage ORGANISATIONNEL que le "
  "ch. 15 § 15.1.2 déclare renvoyé hors protocole.",
  dict(titre="TROIS ANCRAGES SOUS LE NIVEAU APPLICATIF", cols=3, items=[
      ("1", "SPIFFE / SPIRE", "Une identité d'exécution, matérialisée par un justificatif à courte durée de vie ; authentification mutuelle sans secret partagé.", "adapté aux agents éphémères"),
      ("2", "Identifiants décentralisés", "Un identifiant porté par son sujet, résolvable sans annuaire central.", "W3C — voir § 13.1 pour le stade"),
      ("3", "WIMSE", "L'extension de l'identité de charge aux échanges entre charges.", "travaux IETF"),
  ]))

f(13, "13.5", "f-13-05-fosse-adoption",
  "Le fossé d'adoption : ce que le corpus documente, et à quel degré d'absence.",
  "Le fosse d'adoption des accreditations verifiables en production, et le degre d'absence.",
  "§ 13.5, chapitre 13.", NOTE, "paire",
  "⚠ C'est une ABSENCE DE DOCUMENTATION, non un fait négatif vérifié (troisième degré, R-14 du "
  "Vol. III). Elle ne soutient en aucun cas l'énoncé « aucune banque n'emploie ces mécanismes » — "
  "et la figure ne doit pas laisser lire ce qu'elle ne dit pas.",
  dict(titre_g="CE QUE LE CORPUS PORTE", titre_d="CE QU'IL NE PORTE PAS",
       gauche=("Des spécifications, et leurs stades",
               ["Modèle de données d'accréditation et identifiants décentralisés du W3C",
                "Des profils d'interopérabilité, avec leur lacune de couverture déclarée",
                "Des groupes communautaires agentiques"],
               "l'appareil normatif existe"),
       droite=("Aucun établissement financier réglementé, nommément désigné",
               ["exploitant EN PRODUCTION",
                "des accréditations vérifiables ou des identifiants décentralisés",
                "au corpus consulté le 21 juillet 2026"],
               "troisième degré d'absence")))

f(14, "14.1", "f-14-01-grille-cinq-questions",
  "La grille des cinq questions, et ce que chacune exige d'un mécanisme.",
  "Les cinq questions de la grille d'identite agentique et l'exigence attachee a chacune.",
  "Tableau 14.1, § 14.1, chapitre 14.", r"^## § 14\.2 ", "bandes",
  "La grille TRIE, elle ne certifie pas : répondre aux cinq questions n'établit pas qu'un "
  "mécanisme est sûr, seulement qu'il porte ce qu'il faut pour être interrogé. Son inspiration "
  "n'autorise pas davantage (§ 14.1).",
  dict(titre="CINQ QUESTIONS, CINQ EXIGENCES", cols=1, items=[
      ("Q-A", "Qui es-tu ?", "Un identifiant stable, vérifiable, résistant à l'usurpation et révocable.", ""),
      ("Q-B", "Qui t'a créé ?", "Une chaîne de provenance jusqu'à une autorité d'émission, avec son ancrage de confiance.", ""),
      ("Q-C", "Pour qui agis-tu ?", "Une chaîne de mandat interrogeable à l'instant t, et non seulement à l'admission.", ""),
      ("Q-D", "Que peux-tu faire ?", "Des bornes de privilège explicites et opposables au point d'application.", ""),
      ("Q-E", "Qui en répond ?", "Une imputabilité traçable jusqu'à une personne ou une entité juridique.", ""),
  ]))

f(15, "15.1", "f-15-01-ancrage-signature",
  "La carte signée et la question de l'ancrage : qui signe les signataires ?",
  "La chaine de verification d'une carte d'agent signee, et le point ou l'ancrage sort du protocole.",
  "§ 15.1.1 et § 15.1.2, chapitre 15.", r"^## § 15\.2 ", "chaine",
  "⚠ L'ANCRAGE EST RENVOYÉ HORS DU PROTOCOLE. Le magasin de clés de confiance est un dispositif "
  "que les clients « MAY maintain » : le texte n'en définit ni la provenance, ni le format, ni "
  "les critères d'inscription (F-09, [B]). Le vérificateur établit l'intégrité — jamais l'appartenance.",
  dict(titre="CE QUE LA VÉRIFICATION ÉTABLIT, ET OÙ ELLE S'ARRÊTE",
       rupture=("La chaîne casse au dernier maillon : l'appartenance de la clé à une organisation n'est pas spécifiée.", 2),
       maillons=[
           ("Carte publiée", "à un emplacement bien connu, conforme à un mécanisme normalisé"),
           ("Signature", "apposition MAY, vérification SHOULD (F-04, [A])"),
           ("Intégrité", "d'un contenu canonicalisé au regard d'une clé (F-01, F-02, [A])"),
           ("Appartenance", "hors protocole : `kid`, `jku`, ou un magasin facultatif"),
       ]))

f(15, "15.3", "f-15-03-chemin-magasin",
  "Deux moitiés d'un même mécanisme : le protocole normalise le chemin, l'infrastructure spécifie le magasin.",
  "La repartition entre la normalisation du chemin de decouverte et la specification du magasin.",
  "§ 15.3.2, chapitre 15.", NOTE, "paire",
  "Ce paragraphe est le versant IDENTITÉ ET CONFORMITÉ d'une matière partagée : le versant "
  "protocolaire — les trois moments de la découverte, les catalogues fédérés, les modes d'échec "
  "des registres — est au ch. 9, et n'est pas reconstruit ici.",
  dict(titre_g="LE CHEMIN", titre_d="LE MAGASIN",
       gauche=("Ce que le protocole agent-agent normalise",
               ["L'emplacement bien connu où se publie la carte",
                "La forme de l'auto-description",
                "Le chemin par lequel on trouve"],
               "normalisé, et le registre décliné"),
       droite=("Ce que la couche d'infrastructure spécifie",
               ["Le magasin où les descriptions sont tenues",
                "Ses champs d'accès aux outils et de bornes",
                "Ce qui décide de la confiance"],
               "spécifié, et à statut déclaré")))

f(16, "16.1a", "f-16-01a-quatre-pieces",
  "Les quatre pièces du passeport d'agent : ce que le socle établit de chacune, et ce qu'il n'établit pas.",
  "Les quatre pieces du passeport d'agent, avec leur siege et la borne de chacune.",
  "Tableau 16.1, § 16.1, chapitre 16, au 21 juillet 2026.", r"^### 16\.1\.1 ", "bandes",
  "⚠ Le passeport est un OBJET DE SYNTHÈSE CONSTRUIT PAR LA SOMME : aucune spécification ne le "
  "nomme, aucune organisation ne l'émet. Les quatre pièces existent séparément ; leur assemblage "
  "est un énoncé d'auteur, pas un mécanisme.",
  dict(titre="QUATRE PIÈCES, QUATRE SIÈGES", cols=2, items=[
      ("1", "Carte signée", "Intégrité d'un contenu canonicalisé au regard d'une clé.", "ch. 15 § 15.1 — n'établit pas l'appartenance de la clé"),
      ("2", "Inscription au registre", "Champs obligatoires d'accès aux outils et de bornes de permission.", "ch. 15 § 15.3 — n'établit pas leur opposabilité"),
      ("3", "Chaîne de mandat", "Format versionné, attributs temporels, expression de la délégation.", "ch. 17 — n'établit pas l'interrogeabilité à l'instant t"),
      ("4", "Attestations de conformité", "Un nom de champ facultatif, hors socle.", "ch. 15 § 15.3.3 et ch. 25 § 25.5 — ni format, ni contenu, ni émetteur"),
  ]))

f(16, "16.1b", "f-16-01b-substituts",
  "Ce qui tient lieu de chaque pièce aujourd'hui, et l'écart que le substitut laisse ouvert.",
  "Les substituts actuels des quatre pieces du passeport, et l'ecart que chacun laisse ouvert.",
  "Tableau 16.2, § 16.1.1, chapitre 16, au 30 juillet 2026.", r"^## § 16\.2 ", "bandes",
  "Aucun substitut n'est une pièce : chacun règle le problème CHEZ SOI et le laisse entier à la "
  "frontière. La quatrième n'a même pas de substitut protocolaire — ce qui en tient lieu est "
  "documentaire, tenu hors du maillage et lu par des humains.",
  dict(titre="QUATRE SUBSTITUTS, QUATRE ÉCARTS", cols=2, items=[
      ("1", "Carte signée", "La carte d'agent, signée et vérifiée hors bande — le mécanisme existe et il est spécifié.", "ne fournit pas l'ancrage organisationnel de la clé"),
      ("2", "Inscription", "Un registre interne, tenu par l'exploitant du maillage, avec ses propres champs.", "ne fournit pas l'opposabilité inter-organisationnelle"),
      ("3", "Chaîne de mandat", "L'échange de jeton RFC 8693 et son attribut d'acteur — à un saut, dans un domaine unique.", "ne fournit ni la composition au-delà du premier saut, ni l'interrogeabilité"),
      ("4", "Attestations", "Rien de protocolaire : un inventaire documentaire, lu par des humains.", "ne fournit rien de ce qui en ferait une pièce"),
  ]))

f(17, "17.2", "f-17-02-rang-de-la-chaine",
  "Trois mécanismes, et le rang que chacun accorde à la chaîne de délégation.",
  "Les trois mecanismes de delegation, distingues par le rang qu'ils accordent a la chaine.",
  "§ 17.2, chapitre 17.", r"^## § 17\.3 ", "bandes",
  "⚠ La mise en rang est une CONSTRUCTION DE LA SOMME. Le socle établit trois faits séparés, un "
  "par mécanisme ; il n'établit aucun classement entre eux — aucun lot n'a balayé de corpus, et "
  "« énoncer la chaîne comme structure propre » est un critère d'auteur.",
  dict(titre="TROIS MÉCANISMES, TROIS RANGS", cols=3, items=[
      ("1", "Document d'autorisation d'agent", "Décrit la chaîne comme l'objet qu'il spécifie.", "F-46, [B] — format versionné, attributs temporels"),
      ("2", "Échange de jeton", "Exprime la délégation, et laisse la sécurité du jeton hors périmètre.", "F-47, [A]"),
      ("3", "Carte d'agent", "Porte l'identité, non la chaîne.", "F-29, [A]"),
  ]))

f(17, "17.6", "f-17-06-deux-sauts",
  "Le problème des deux sauts : où chaque mécanisme perd le fil.",
  "La chaine de delegation a deux sauts, et le point ou les mecanismes cessent de la porter.",
  "§ 17.6.1, chapitre 17.", r"^### 17\.6\.2 ", "chaine",
  "⚠ « Deux sauts » N'EST PAS UNE MESURE : c'est la formulation d'un front ouvert (H-28, [C]). "
  "Aucune entrée du socle propre ne compte de sauts, n'en fixe le seuil, ni ne définit le terme — "
  "la définition employée par le chapitre est déclarée par lui.",
  dict(titre="UN SAUT PORTÉ, LE SECOND NON",
       rupture=("Au-delà du premier saut : degré 3 — absence de documentation, non fait négatif vérifié.", 2),
       maillons=[
           ("Mandant", "l'humain qui délègue, premier et dernier maillon (§ 17.4)"),
           ("Agent", "détient le mandat, l'exerce — premier saut"),
           ("Sous-agent", "reçoit un mandat dérivé — second saut"),
           ("Service", "applique, sans pouvoir remonter la chaîne à l'instant t"),
       ]))

f(18, "18.1", "f-18-01-neuf-chantiers",
  "Neuf chantiers, six organisations, zéro texte ratifié.",
  "Les neuf chantiers de verification d'agent tiers, repartis en six organisations, aucun ratifie.",
  "Tableau 18.1, § 18.1, chapitre 18, au 21 juillet 2026.", r"^## § 18\.2 ", "bandes",
  "⚠ ZÉRO TEXTE RATIFIÉ. Un chantier ouvert n'est pas une norme en cours d'adoption : deux "
  "brouillons de l'IETF sont des soumissions individuelles non adoptées, une charte place la "
  "normalisation HORS de son périmètre, et l'un des neuf est un cadre commercial.",
  dict(titre="SIX ORGANISATIONS, NEUF CHANTIERS, AUCUN TEXTE", cols=3, items=[
      ("W3C", "Deux groupes communautaires", "« Agent Identity Registry Protocol » (22 avr. 2026) et « AI Agent Protocol » (8 mai 2025).", "ni voie des normes, ni Recommandation"),
      ("OIDF", "Gestion d'identité pour l'IA", "Sa charte place hors périmètre le développement de protocoles de normalisation mondiaux.", "renvoie le travail ailleurs"),
      ("DIF", "Connaissance de l'agent", "Version 1 encore soumise à relecture et à approbation au 22 juin 2026.", "F-50 [B, degré 2] — non ratifiée"),
      ("IETF", "Deux brouillons individuels", "Identité d'agent (26 mars 2026) et registre d'identité (23 mai 2026).", "non adoptés par un groupe de travail"),
      ("NIST", "Deux initiatives", "Document de concept (5 févr. 2026) et initiative de normalisation (17 févr. 2026).", "projet public initial ; volet identité à l'état de concept"),
      ("Éditeur", "Cadre commercial", "« Know Your Agent », annoncé le 15 juin 2026.", "F-49 [B, degré 3] — une offre, pas une norme"),
  ]))

f(18, "18.2", "f-18-02-admettre",
  "Admettre un agent tiers : ce que la frontière reçoit, et ce qu'elle doit produire elle-même.",
  "La repartition entre ce que le protocole specifie a l'admission et ce qu'il laisse a l'organisation.",
  "§ 18.2, chapitre 18.", r"^## § 18\.3 ", "paire",
  "⚠ La grille du ch. 14 N'EST PAS APPLIQUÉE ici : ce chapitre instruit Q-C, il ne rend pas de "
  "verdict mécanisme par mécanisme (ch. 17 § 17.0). La découverte est spécifiée ; l'admission "
  "ne l'est pas — et l'écart entre les deux est tout entier à la charge de celui qui décide.",
  dict(titre_g="CE QUE LA FRONTIÈRE REÇOIT", titre_d="CE QU'ELLE DOIT PRODUIRE ELLE-MÊME",
       gauche=("Spécifié",
               ["Une carte d'agent, publiée et signée",
                "Un chemin de découverte normalisé",
                "Des capacités déclarées par l'agent lui-même"],
               "la découverte est spécifiée"),
       droite=("Non spécifié",
               ["Le critère d'admission",
                "L'ancrage de la clé dans une organisation",
                "La vérification de ce que l'agent déclare",
                "Le verdict, et sa durée de validité"],
               "l'admission ne l'est pas")))

f(19, "19.2", "f-19-02-triade-letale",
  "La triade létale : trois propriétés dont la conjonction suffit.",
  "La triade letale : acces a des donnees privees, exposition a du contenu non fiable, canal de sortie.",
  "§ 19.2, chapitre 19 — siège de la triade létale pour toute la somme.", r"^## § 19\.3 ", "venn",
  "⚠ C'est une CONJONCTION, non une somme de risques : retirer l'une des trois suffit à sortir "
  "de la zone, et les trois réunies suffisent à y entrer. Le ch. 11 § 11.1.2 n'en traite que "
  "l'amplification par la composabilité, et le ch. 20 s'y adosse — le siège est ici.",
  dict(titre="TROIS PROPRIÉTÉS, UNE CONJONCTION", centre="exploitable",
       ensembles=[("Données privées", "l'agent y a accès"),
                  ("Contenu non fiable", "courriel, page web, document, sortie d'outil"),
                  ("Canal de sortie", "vers l'extérieur")]))

f(19, "19.4", "f-19-04-maillon-qui-cede",
  "Le tri des attaques par le maillon qui cède, et la question de la grille en défaut.",
  "Les attaques du socle triees par le maillon de la chaine d'identite qui cede.",
  "Tableau 19.1, § 19.4, chapitre 19, au 21 juillet 2026.", r"^## § 19\.5 ", "bandes",
  "Chaque cellule du tableau source porte LA BORNE DE SON ENTRÉE, et la figure ne la reprend pas : "
  "une attaque documentée par une préimpression non revue et un incident daté ne s'opposent pas au "
  "même régime de preuve. Se reporter au tableau pour la borne.",
  dict(titre="CINQ MAILLONS, CINQ QUESTIONS EN DÉFAUT", cols=1, items=[
      ("Q-A", "L'identifiant", "Jeton porteur non lié à l'appelant, à l'appareil ni à la session — compromission de jetons d'application tierce, août 2025.", "l'identifiant n'est pas résistant à la détention par un tiers"),
      ("Q-B", "La provenance", "Empoisonnement à la publication, en amont de toute vérification ; entrée de mémoire ou document récupéré sans origine vérifiable.", "extension de la grille aux sources"),
      ("Q-C", "Le mandat", "L'instruction inter-agents fait agir le mandataire hors du mandat qu'il détient.", "chaîne de mandat non interrogeable à l'exécution"),
      ("Q-D", "Les bornes", "Absence de réduction de portée entre mandant et mandataire ; invocation d'outils inaccessibles à l'utilisateur.", "bornes de privilège non opposables"),
      ("—", "La composition", "Le détournement réussit même lorsque les agents pris isolément ne sont pas vulnérables.", "aucune question de la grille ne porte sur l'assemblage"),
  ]))

f(20, "20.0", "f-20-00-le-moment",
  "La classe d'attaques dont la particularité n'est pas le maillon mais le moment.",
  "La sequence d'une attaque par retournement : l'admission reussit, et l'objet verifie change ensuite.",
  "§ 20.0 et § 20.1, chapitre 20.", r"^## § 20\.1 ", "frise",
  "L'attaque NE DÉFAIT PAS la vérification : elle attend qu'elle soit faite. La question qu'elle "
  "pose n'est donc pas celle de la robustesse du mécanisme d'admission, mais celle de la DURÉE "
  "DE VALIDITÉ d'un verdict que rien ne borne.",
  dict(titre="L'ADMISSION RÉUSSIT, PUIS L'OBJET CHANGE", jalons=[
      ("t₀", "Publication", "un serveur d'outils est publié, décrit, référencé", "plein"),
      ("t₁", "Admission", "le mécanisme fonctionne, le verdict est rendu", "plein"),
      ("t₂", "Usage", "l'agent l'invoque sur la foi du verdict de t₁", "plein"),
      ("t₃", "Retournement", "l'objet vérifié change — et rien ne re-pose la question", "creux"),
  ]))

f(20, "20.6", "f-20-06-cascade",
  "La révocation en cascade : ce qui tombe quand le mandat d'origine est retiré.",
  "La question de la revocation en cascade dans une chaine de delegation a plusieurs sauts.",
  "§ 20.6, chapitre 20.", r"^## § 20\.7 ", "chaine",
  "⚠ Le socle NE DOCUMENTE PAS de mécanisme de révocation en cascade dans une chaîne de "
  "délégation — absence de documentation, non fait négatif vérifié (degré 3). La distinction "
  "décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable.",
  dict(titre="LE MANDAT D'ORIGINE EST RETIRÉ — ET CE QUI EN A ÉTÉ DÉRIVÉ ?",
       rupture=("Aucun balayage documenté ne répond de ce qui se propage, ni de la vitesse à laquelle il se propage.", 1),
       maillons=[
           ("Mandant", "retire l'autorisation qu'il avait accordée"),
           ("Agent", "détenait le mandat, l'avait transmis"),
           ("Second agent", "l'exerce encore auprès d'un service"),
       ]))

f(21, "21.2", "f-21-02-moisson",
  "Récolter maintenant, déchiffrer plus tard : ce que le socle établit, et où le raisonnement le quitte.",
  "La longevite d'un artefact d'identite comparee a l'horloge de la menace post-quantique.",
  "§ 21.2, chapitre 21.", r"^## § 21\.3 ", "paire",
  "⚠ Le socle NE DOCUMENTE PAS la collecte anticipée en vue d'un déchiffrement ultérieur — "
  "degré 3. Cette section ne s'écrit pas comme un chapitre de fait mais comme un RAISONNEMENT "
  "D'ARCHITECTURE appuyé sur des faits établis, et elle dit où le raisonnement quitte le socle.",
  dict(titre_g="CE QUE LE SOCLE ÉTABLIT", titre_d="CE QUE LE RAISONNEMENT AJOUTE",
       gauche=("La longévité des artefacts",
               ["Un artefact d'identité de longue durée survit à l'horloge",
                "Les échéances publiées sont datées et sourcées (§ 21.1)",
                "L'inventaire par artefact est dressé (§ 21.3)"],
               "faits établis, avec leurs bornes"),
       droite=("La collecte anticipée",
               ["Ce qui est chiffré aujourd'hui peut être conservé",
                "et déchiffré quand l'horloge aura tourné",
                "ni mécanique ni faisabilité datée au socle"],
               "degré 3 — le raisonnement quitte le socle ici")))

f(21, "21.9", "f-21-09-calendrier-inverse",
  "La fenêtre d'action lue à rebours, depuis l'échéance la plus contraignante.",
  "Le calendrier de migration post-quantique lu a rebours, de l'echeance vers le present.",
  "§ 21.9, chapitre 21.", NOTE, "frise",
  "⚠ La fenêtre est une CONSTRUCTION DE LA SOMME. Le socle porte des échéances datées ; il ne "
  "porte AUCUN délai de mise en œuvre applicable à une institution — et encore faut-il savoir "
  "laquelle des dates publiées s'applique.",
  dict(titre="SE LIT À REBOURS, NON DANS LE SENS DE LA LECTURE", rebours=True, jalons=[
      ("Échéance", "La date la plus contraignante", "celle qui s'applique réellement à l'institution — et le socle établit qu'elles ne sont pas une", "plein"),
      ("−1", "Migration exécutée", "les artefacts de longue durée sont réémis", "creux"),
      ("−2", "Patrons de migration", "sans rupture de la chaîne de confiance (§ 21.6)", "creux"),
      ("Aujourd'hui", "Inventaire", "la méthode est au § 21.8 ; sans inventaire, aucune des dates ne se calcule", "plein"),
  ]))
