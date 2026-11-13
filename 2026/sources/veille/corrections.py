"""Corrections des relectures des 3 et 11 novembre 2026, appliquées au corps extrait.

Le corps de la Veille n'a pas de source éditable : il est relu dans l'édition d'origine
(construire_pdf.py, ORIGINE). Les errata du 29 octobre n'y corrigeaient que ce qui
tenait dans la ligne, le PDF étant retouché sur place; la recomposition lève cette
contrainte. Les corrections des relectures des 3 et 11 novembre sont donc faites à leur
place, errata du 29 octobre laissés à l'annexe compris, et consignées au tableau
d'errata de l'annexe de novembre (actualisation-2026-11.html, tableau 31). Chaque
correction s'appuie sur un fait que le document établit déjà, au corps ou dans ses
annexes.

Chaque correction remplace un passage qui doit figurer exactement le nombre de fois
indiqué (une, par défaut) : un passage absent ou ambigu arrête la composition.
"""
import re

ZWSP = '​'

# (passage d'origine, passage corrigé[, occurrences]), dans l'ordre du document
CORRECTIONS = [
    # mots-clés : MPP, ajouté à la section 4.8 le 15 août
    ('paiements agentiques ; AP2 ; x402 ;', 'paiements agentiques ; AP2 ; x402 ; MPP ;'),
    # sommaire, constat 2 (erratum 5 du 29 octobre, appliqué en entier)
    ('plus de 950 serveurs au répertoire [270] ; décompte <em>total</em> sans source primaire.',
     'plus de 950 serveurs au répertoire [270] ; décompte <em>total</em> établi par recomptage du '
     'registre officiel, 21 767 enregistrements au 15 août (6.3).'),
    # sommaire, constat 6 (erratum 8 du 29 octobre)
    ('il n’impose qu’information et observations devant un employé habilité à réviser :',
     'il impose information, observations devant un employé habilité à réviser et, sur demande, '
     'communication des raisons et des principaux facteurs et paramètres de la décision (8.4) :'),
    # sommaire, constat 7 : ligne directrice de l'AMF et NIST IR 8547 (annexes d'octobre et de novembre)
    ('E-23 et ligne directrice IA de l’AMF : 1er mai 2027 — cette dernière <strong>non vérifiée</strong> '
     '(403 sur <code>lautorite.qc.ca</code> et CanLII). Camunda 7, et la GPA classique : maintenance au '
     '13 avril 2030, soutien étendu à avril 2032. Identités d’agents post-quantiques : avant 2030 '
     '(NIST IR 8547, en brouillon).',
     'E-23 et ligne directrice IA de l’AMF : 1er mai 2027 — cette dernière <strong>non vérifiée</strong> '
     'au gel (403 sur <code>lautorite.qc.ca</code> et CanLII ; PDF lu depuis hors passe, annexe de '
     'novembre, erratum 1). Camunda 7, et la GPA classique : maintenance au 13 avril 2030, soutien étendu '
     'à avril 2032. Identités d’agents post-quantiques : avant 2030 (NIST IR 8547, en brouillon au gel, '
     'finale le 27 octobre 2026, annexe du 29 octobre).'),
    # sommaire, constat 10 (erratum 10 du 29 octobre)
    ('<p>10. Le corpus compagnon compte quatre volumes, dont deux ne sont pas écrits. Deux volumes rédigés '
     'fournissent des faits (4.12, 8.4) ; deux ne sont que des cadrages — zéro chapitre — et ne prêtent que '
     'des instruments, marqués comme constructions d’auteur.',
     '<p>10. Le corpus compagnon compte quatre volumes. Deux fournissent des faits (4.12, 8.4) ; les deux '
     'autres, cadrages sans chapitre aux passes de juillet, sont rédigés depuis, le 22 et le 29 juillet, mais '
     'à diffusion bornée à leur auteur (13.8), et ne prêtent que des instruments, marqués comme '
     'constructions d’auteur.'),
    # 1, QR4 : la septième couche
    ('sémantique, de confiance, orchestration —,', 'sémantique, de confiance, orchestration, exploitation —,'),
    # 1.1, contribution 7 : MPP; l'inactivité est celle d'AP2
    ('AP2, x402, ACP et UCP répliquent le fossé identité-autorisation ; aucun vocabulaire de capacités '
     'partagé (OASF bornée à son écosystème) ; x402 est allé plus loin qu’AP2, à la Linux Foundation [282], '
     'sans commit depuis le 29 avril 2026 ;',
     'AP2, x402, MPP, ACP et UCP répliquent le fossé identité-autorisation ; aucun vocabulaire de capacités '
     'partagé (OASF bornée à son écosystème) ; x402 est allé plus loin qu’AP2, à la Linux Foundation [282], '
     'quand le dépôt d’AP2 est sans commit depuis le 29 avril 2026 ; MPP, sans fondation, est le second '
     'règlement par HTTP 402 (4.8) ;'),
    # 1.2 : la section 4.14
    ('implémentation de référence (4.12), exploitation (4.13),',
     'implémentation de référence (4.12), exploitation (4.13), orchestration des agents (4.14),'),
    # guide de lecture : la section 4.14
    ('orchestration, 4.11.6 ;', 'orchestration des processus, 4.11.6, et des agents, 4.14 ;'),
    # tableau 1, ligne du 8 août : les six auto-citations complètent les 269 références (2.2)
    ('<td>179 confirmées, 54 corrigées, 30 non reconfirmables, 0 introuvable</td>',
     '<td>179 confirmées, 54 corrigées, 30 non reconfirmables, 6 auto-citations, 0 introuvable</td>'),
    # 2.2 : la prose suit le tableau 1
    ('Trois passes seulement — 2, 7 et 13 juillet — soumettent tout leur lot à la ronde adverse ; ailleurs, '
     'elle ne couvre que les énoncés les plus exposés, et les trois passes de veille n’en ont aucune. Les faits '
     'ne pèsent donc pas tous le même poids : les sections 4.6 à 4.13 en sont le haut,',
     'Deux passes seulement — 2 et 15 juillet — soumettent tout leur lot à la ronde adverse ; ailleurs — 7, 12 '
     'et 13 juillet, intégrale du 18 — elle ne couvre que les énoncés les plus exposés, et les quatre passes '
     'de veille, de l’édition d’août au 15 août, n’en ont aucune, pas plus que celle du 23 juillet. La colonne '
     '« Énoncés » compte des énoncés, sauf aux 12 et 18 juillet, où elle compte des agents. Les faits ne '
     'pèsent donc pas tous le même poids : les sections 4.10 et 4.11 en sont le haut, les sections 4.6, 4.8, '
     '4.9 et 4.13, vérifiées en partie individuellement, viennent ensuite, la 4.12 porte le régime de son '
     'corpus compagnon,'),
    # 3.3 : appel du tableau 2
    ('nous retenons une grille à trois niveaux, chacun porté par un protocole structurant au 15 août 2026 :</p>',
     'nous retenons une grille à trois niveaux, chacun porté par un protocole structurant au 15 août 2026 (tableau 2) :</p>'),
    # 4.1
    ('prise de contrôle de namespace d’organisation', 'prise de contrôle d’espace de nommage d’organisation'),
    # 4.3 : ANP 1.1, antérieure au gel (annexe du 29 octobre)
    ('le livre blanc reste en version unique [15].',
     'le livre blanc reste en version unique [15], quoique le dépôt canonique ait publié une version ANP 1.1 '
     'le 27 juin 2026 (annexe du 29 octobre, [351]).'),
    # tableau 3
    ('révision 2026-07-28 en <em>release candidate</em> [97])',
     'révision 2026-07-28 en <em>release candidate</em> au 12 juillet, normative depuis le 28 juillet [97])'),
    ('<td>livre blanc + brouillons W3C CG [15, 16]</td>',
     '<td>livre blanc + brouillons W3C CG [15, 16] ; ANP 1.1 au dépôt, 27 juin 2026 [351]</td>'),
    ('communauté ANP /incubation W3C (CG)', 'communauté ANP / incubation W3C (CG)'),
    # 4.4 : la variante ACP d'AGNTCY (agntcy/acp-spec) est elle aussi archivée depuis mai 2025
    ('Le dépôt n’a plus reçu de poussée depuis le 25 août 2025, jour de son archivage, et son dernier commit '
     'est l’annonce du passage à A2A (consulté le 15 août 2026) [268] : la consolidation est plus ancienne '
     'et plus complète que la revue ne le disait.</p>',
     'Le dépôt n’a plus reçu de poussée depuis le 25 août 2025, jour de son archivage, et son dernier commit '
     'est l’annonce du passage à A2A (consulté le 15 août 2026) [268] ; la variante ACP d’AGNTCY '
     '(<code>agntcy/acp-spec</code>) est elle aussi archivée, sans poussée depuis le 23 mai 2025 (annexe de '
     'novembre) : la consolidation est plus ancienne et plus complète que la revue ne le disait.</p>'),
    # 4.5, cadrage : les sept couches
    ('de confiance, portant l’identité et l’autorisation que présupposent leurs cadres OAuth (§4.10).</p>',
     'de confiance, portant l’identité et l’autorisation que présupposent leurs cadres OAuth (§4.10). '
     'L’événementiel (§4.6), le plan de contrôle (§4.7), l’orchestration des processus (§4.11) et '
     'l’exploitation (§4.13) complètent les sept couches ; la sous-section 4.12 est une épreuve par le code, '
     'non une couche.</p>'),
    # 4.8 : citation de [284] (annexe de novembre)
    ('seule la réservation de <em>handle</em> est ouverte, le reste restant « in the coming months » [284].',
     'seule la réservation de <em>handle</em> est ouverte, le reste annoncé pour plus tard [284].'),
    ('<em>Et le protocole le plus adopté de la sous-couche règlement n’a migré nulle part</em> : MPP n’a ni '
     'fondation, ni gouvernance neutre, ni version numérotée.',
     '<em>Et le protocole le plus adopté de la sous-couche règlement n’a migré nulle part</em> : MPP n’a ni '
     'fondation, ni gouvernance neutre, ni version numérotée ; son noyau est pourtant déposé à l’IETF depuis '
     'le 19 juin 2026, en soumission individuelle sans filière (annexe de novembre).'),
    # 4.9
    ('Existe-t-il ? Par examen direct des spécifications : non.',
     'Existe-t-il ? Par examen direct des spécifications des trois protocoles structurants : non.'),
    ('le billet primaire ne nomme ni AGNTCY ni OASF, et n’a reçu au 15 août 2026 ni nouvelle version,',
     'le billet primaire ne nomme ni AGNTCY ni OASF, et la spécification n’a reçu au 15 août 2026 ni nouvelle version,'),
    # 4.10 : DMSC n'est pas un groupe de travail (annexe du 29 octobre, [359])
    ('Mais trois BoF agentiques ont été approuvées en juin 2026, et deux groupes en sont issus : '
     '<strong>DAWN</strong> (découverte d’agents, de charges de travail et d’entités nommées) et '
     '<strong>DMSC</strong> (collaboration multi-agents sécurisée dynamique) [159]. <em>Au 15 août 2026, '
     'ces deux groupes portent',
     'Mais trois BoF agentiques ont été approuvées en juin 2026 : <strong>DAWN</strong> (découverte '
     'd’agents, de charges de travail et d’entités nommées) en est issu comme groupe de travail, et '
     '<strong>DMSC</strong> (collaboration multi-agents sécurisée dynamique), que cette édition donnait '
     'pour charté, figure au registre à l’état « BoF concluded » le 8 octobre (annexe du 29 octobre, [359]) '
     '[159]. <em>Au 15 août 2026, ces deux enceintes portent'),
    ('<em>DAWN et DMSC, chartés en juin, portent vingt-sept brouillons et n’en ont adopté aucun</em> [159]',
     '<em>DAWN, charté en juin, et DMSC, resté BoF, portent vingt-sept brouillons et n’en ont adopté aucun</em> [159]'),
    ('les deux groupes agentiques chartés en juin n’ont toujours rien adopté.',
     'ni DAWN, charté en juin, ni DMSC n’ont toujours rien adopté.'),
    # tableau 6
    ('<td>Google Agent Identity — identité SPIFFE par agent, GA le 22 avril 2026 [153]</td>',
     '<td>Google Agent Identity — identité SPIFFE par agent, GA le 22 avril 2026 ; Agent Identity API et '
     '<em>auth manager</em> en préversion [153]</td>'),
    # tableau 8 : la garantie de Zeebe n'est pas attestée
    ('<td><em>exactly-once</em> (état) — portée non énoncée par la page citée [183] ;',
     '<td>garantie non énoncée par la page citée [183] — l’<em>exactly-once</em> d’état lui était prêté sans source ;'),
    ('pré-version', 'préversion', 4),
    # 4.11.3 : pourquoi le décompte ne se fixe pas
    ('<em>Le décompte d’implémentations ne se laisse pas fixer : huit produits portent des résultats publiés, '
     'trois n’en portent aucun.</em>',
     '<em>Le décompte d’implémentations ne se laisse pas fixer : huit produits portent des résultats publiés, '
     'trois n’en portent aucun, et le nombre dépend de ce que l’on compte pour une implémentation (tableau 20).</em>'),
    # 4.11.5 : article 12.1, énoncé entier et partage des deux stades
    ('L’article 12.1 de la loi 25 québécoise', 'L’article 12.1 de la Loi 25 québécoise'),
    ('et n’impose alors que trois choses : informer au moment de la décision, permettre des observations '
     'devant un membre du personnel <em>en mesure de réviser</em>, communiquer sur demande les renseignements '
     'et les principaux facteurs [212].',
     'et impose alors d’informer la personne au plus tard au moment où elle l’informe de cette décision, de '
     'lui permettre de présenter ses observations à un membre du personnel <em>en mesure de réviser</em> la '
     'décision, et de lui communiquer sur demande les renseignements utilisés, les raisons et les principaux '
     'facteurs et paramètres ayant mené à la décision, ainsi que son droit de rectification [212].'),
    ('Maintenir un humain en mesure de réviser sort la décision du champ de l’article ; sinon, information et '
     'voie de recours — tâche utilisateur de BPMN ou confirmation de CUA (4.11.2), table DMN (4.11.3).',
     'Une intervention humaine dans la décision même — tâche utilisateur de BPMN ou confirmation de CUA '
     '(4.11.2) — la sort du champ de l’article ; le membre du personnel en mesure de réviser après coup ne '
     'l’en sort pas : il est le recours que l’article impose, avec l’information et la restitution des '
     'facteurs et paramètres, que porte une table DMN (4.11.3).'),
    # 4.12 : ce qui reste rejouable
    ('Une implémentation de référence qu’on ne peut plus ouvrir ne porte plus le même régime de preuve.</p>',
     'Une implémentation de référence qu’on ne peut plus ouvrir ne porte plus le même régime de preuve. '
     'Restent rejouables sur les dépôts publics les comportements des SDK amont — SDK Go de MCP v1.6.1, '
     'a2a-go v2.3.1 — ; les défauts propres au démonstrateur ne se vérifient plus.</p>'),
    # 4.13.1
    ('dans chacun des deux fichiers candidats [228].',
     'dans chacun des deux fichiers candidats, <code>gen-ai-agent-spans.md</code> et <code>gen-ai-spans.md</code> [228].'),
    # tableau 10
    ('<td>[233], [287], [330]</td>', '<td>[233], [286], [287], [330]</td>'),
    ('<strong>aucune fusionnée ni fermée</strong>', '<strong>aucune résolue ni fermée</strong>'),
    ('(QO 24)', '(question ouverte 24)'),
    # 4.14 : le registre de Google précède celui d'AWS
    ('le premier catalogue gouverné d’agents relève d’un exploitant, non de la couche commune, et il n’est '
     'toujours pas général.',
     'ce catalogue gouverné d’agents, venu après l’Agent Registry de Google, général depuis le 18 juin 2026 '
     '(tableau 12), relève d’un exploitant, non de la couche commune, et il n’est toujours pas général.'),
    ('(QO 25)', '(question ouverte 25)'),
    ('Chacune des sept couches orthogonales des sections 4.6 à 4.13 dispose',
     'Chacune des sept couches orthogonales des sections 4.6 à 4.11 et 4.13 — la 4.12 est une épreuve, non '
     'une couche — dispose'),
    # 5
    ('Le tableau 6.5 porte les statuts', 'Le tableau 11 porte les statuts'),
    ('AARP et COAZ — autorisation des appels d’outils MCP — en brouillons le 15 juin 2026 [79] ;',
     'AARP et COAZ — autorisation des appels d’outils MCP — en brouillons le 15 juin 2026 [79], dont le '
     'texte en vigueur est au dépôt du groupe [327] ;'),
    # 5.5 et 9.1 : a2a-tck, tronc immobile et dépôt actif (erratum 9 du 29 octobre)
    ('<code>a2a-tck</code> (Apache-2.0, mai 2025), sans une fusion depuis le 29 juin 2026 [264],',
     '<code>a2a-tck</code> (Apache-2.0, mai 2025), sans une fusion depuis le 29 juin 2026 mais six demandes '
     'de tirage ouvertes en août [264],'),
    # 6.5
    ('« portée par » l’agentique [82] [275].', '« portée par » l’agentique [82, 275].'),
    # 7.1 : OWASP (annexe de novembre)
    ('n’a rien publié depuis juin 2026, et aucun relevé d’incidents ne succède à celui du 14 avril [71, 109].',
     'n’a rien publié depuis juin 2026 à l’index de l’initiative, et aucun relevé d’incidents n’y succède à '
     'celui du 14 avril [71, 109] ; le projet GenAI d’OWASP date pourtant du 8 juillet un relevé du deuxième '
     'trimestre (annexe de novembre).'),
    # 7.1 et 8.4 : l'incident de juillet, d'après les primaires du 26 août (annexe de novembre)
    ('par une faille zéro-jour dans un logiciel de registre de paquets exposé sur l’internet,',
     'par des failles zéro-jour d’une instance interne de registre de paquets, devenue leur voie vers '
     'l’internet (rapport technique du 26 août, annexe de novembre),', 2),
    ('elle a été fabriquée (8.4).</p>',
     'elle a été fabriquée (8.4) — selon l’avis de la CSA ; l’enquête indépendante publiée depuis estime à '
     'environ 7 % les transcriptions falsifiées, à petite échelle, et n’a vu aucune altération réussie des '
     'journaux (annexe de novembre).</p>'),
    # 7.2
    ('l’Agent Identity API demeure en préversion depuis le 15 juin 2026 [107, 153]',
     'l’Agent Identity API demeure en préversion depuis le 18 juin 2026 [107, 153]'),
    # 7.3
    ('passé au groupe DAWN, chartré en juin,', 'passé au groupe DAWN, charté en juin,'),
    # 7.8
    ('Entrées de registre : retrait par l’exploitant', '<strong>Entrées de registre</strong> : retrait par l’exploitant'),
    ('Attestations vérifiables : mécanisme de statut spécifié', '<strong>Attestations vérifiables</strong> : mécanisme de statut spécifié'),
    # 8 : pictogrammes de correction
    ('✎ <em>Correction d’un énoncé de l’édition précédente</em>', '<em>Correction d’un énoncé de l’édition précédente</em>', 2),
    ('✎ <em>Correction</em> :', '<em>Correction</em> :'),
    ('✎ Mais il n’impose pas seulement', 'Mais il n’impose pas seulement'),
    ('[341], texte canadien primaire qui, lui, nomme', '[341], texte primaire cosigné par le Canada qui, lui, nomme'),
    # 8.3
    ('COAZ projette déjà, en brouillon, chaque appel d’outil MCP sur un point AuthZEN [149] ;',
     'COAZ projette déjà, en brouillon, chaque appel d’outil MCP sur un point AuthZEN [149, 327] ;'),
    # 8.4 : AMF, état du PDF (annexe de novembre, erratum 1, témoignage hors passe)
    ('La date de la version finale de la ligne directrice IA de l’AMF diverge — 30 mars 2026 au socle [218], '
     'contre le 7 avril ici [210] —',
     'La date de la version finale de la ligne directrice IA de l’AMF diverge — 30 mars 2026 au socle [218], '
     'contre le 7 avril ici [210] ; le PDF, lu depuis hors passe, porte « Mars 2026 » et une modification du '
     '30 mars, pour une publication en avril (annexe de novembre, erratum 1) —'),
    ('l’incident de juillet 2026 en fournit la preuve par des artefacts de journaux hallucinés (7.1) [337]',
     'l’incident de juillet 2026 en fournit un indice par des artefacts de journaux hallucinés (7.1) [337], '
     'que l’enquête indépendante ramène à des transcriptions falsifiées, sans journal altéré'),
    # 9.1
    ('kit d’A2A figé depuis juin 2026 [264]', 'kit d’A2A au tronc immobile depuis le 29 juin 2026, au dépôt actif [264]'),
    # 9.5 : MPP
    ('<strong>ni AP2, ni UCP, ni ACP</strong> [285] : souscrire à tout n’empêche pas les tiers de trancher.',
     '<strong>ni AP2, ni UCP, ni ACP</strong> [285], et documente MPP depuis le 5 août [309] : souscrire à '
     'tout n’empêche pas les tiers de trancher, entre mandats sinon entre règlements (4.8).'),
    # 9.6 : réserve de source sur l'AMF
    ('les instruments d’E-23, de l’AMF, de l’art. 12.1 et de DORA [172]',
     'les instruments d’E-23, de l’AMF — sous la réserve de source de la section 8.4 —, de l’art. 12.1 et de DORA [172]'),
    # 10 : AI Act consolidé (erratum 11 du 29 octobre)
    ('Aucune version consolidée de l’AI Act intégrant le règlement (UE) 2026/1744 n’est disponible non plus.',
     'La version consolidée de l’AI Act intégrant le règlement (UE) 2026/1744 est publiée (8.1, [254]), mais '
     'l’outillage automatisé n’en a reçu que des réponses vides.'),
    ('ses constats restent exacts et datés, mais un renvoi exact vers un fichier absent reste exact ; il cesse '
     'd’être opposable.',
     'ses constats restent exacts et datés, mais un renvoi vers un fichier absent, s’il reste exact, cesse '
     'd’être opposable.'),
    # 11, questions 15 et 25
    ('Deux implémentations d’A2A convergeront-elles sans suite de conformité, une canonicalisation libre ayant '
     'rompu l’interopérabilité (4.12 [217]) ?',
     'Deux implémentations d’A2A convergeront-elles tant que les vecteurs de canonicalisation RFC 8785 restent '
     'en demande ouverte au kit de conformité, une canonicalisation libre ayant rompu l’interopérabilité '
     '(4.12, [217]) ?'),
    ('L’orchestration hors de la couche commune ? Un format', 'L’orchestration hors de la couche commune. Un format'),
    # 12
    ('ligne directrice IA de l’AMF, finale [210] — date du 7 avril non reconfirmée en source primaire '
     '(section 13.6) ; Camunda 8.9 (MCP GA, connecteurs A2A alpha) [170]',
     'ligne directrice IA de l’AMF, finale en avril 2026, document daté de mars [210] — le 7 avril ne se '
     'cite qu’avec sa source secondaire (annexe de novembre, erratum 1) ; Camunda 8.9, 14 avril (connecteur '
     'MCP sorti de l’arbre alpha, sans disponibilité générale énoncée ; connecteurs A2A alpha) [170]'),
    # 12.1 et 10 : RTR (annexe de novembre, erratum 3)
    ('celle du règlement d’exploitation reste sous attribution secondaire [257].',
     'celle du règlement d’exploitation et des règles, tenue ici sous attribution secondaire [257], est '
     'confirmée par un communiqué de Paiements Canada du 30 juin 2026 (annexe de novembre, erratum 3).'),
    ('deux énoncés y sont sous attribution : l’entrée en vigueur du règlement d’exploitation du RTR,',
     'deux énoncés y sont sous attribution : l’entrée en vigueur du règlement d’exploitation du RTR, confirmée '
     'depuis (annexe de novembre, erratum 3),'),
    ('(2030-2032 [171])', '(2030-2032, [171])'),
    ('mais l’IETF a refusé la BoF sur la délégation en mai 2026 [159].',
     'mais l’IETF a refusé la BoF sur la délégation en mai 2026, et DAWN, seul groupe agentique charté en '
     'juin, n’a rien adopté au 15 août [159].'),
    # 13 : état de juillet, dit comme tel
    ('<h3>13.1 Quatre volumes, deux états de rédaction</h3>',
     '<h3>13.1 Quatre volumes, deux états de rédaction</h3>\n<p><em>Les sections 13.1 à 13.5 et les tableaux '
     '15 et 16 décrivent le corpus à son état des 18 et 19 juillet 2026, celui des passes de juillet. Les '
     'volumes III et IV ont été rédigés depuis, le 22 et le 29 juillet, le Vol. IV arrêté en cinq livres et '
     'cinquante chapitres ; leur régime de citation tient, pour un autre motif : la diffusion bornée à leur '
     'auteur (13.8).</em></p>'),
    (' <em>Note du 29 octobre 2026. Les tableaux 15 et 16 et les sections 13.1 à 13.5 décrivent l’état du '
     '18–19 juillet 2026 Le Compendium livré compte cinq livres et cinquante chapitres, et les volumes III et '
     'IV sont rédigés (13.8).</em></td>', '</td>'),
    ('<em>programmé / projeté /spéculatif</em>', '<em>programmé / projeté / spéculatif</em>'),
    ('et n’impose alors qu’information de la personne et possibilité d’observations devant un employé '
     '<strong>en mesure de réviser</strong> — il borne l’absence totale d’humain, sans prescrire aucun degré '
     'd’autonomie (8.2, 9.6).',
     'et impose alors information de la personne, possibilité d’observations devant un employé '
     '<strong>en mesure de réviser</strong> et, sur demande, communication des raisons et des principaux '
     'facteurs et paramètres de la décision — il borne l’absence totale d’humain, sans prescrire aucun degré '
     'd’autonomie (8.4, 9.6).'),
    # 13.6 : report de l'erratum 1 du 1er novembre sur l'AMF
    ('D’où une rétractation que la revue s’applique à elle-même : sa date du <strong>7 avril 2026</strong> '
     '(4.11.5, 8.4, tableau 14, [210]) n’a pas été reconfirmée en source primaire ; la divergence reste '
     'ouverte : signalée, non uniformisée.</p>',
     'D’où une rétractation que la revue s’appliquait au gel : sa date du <strong>7 avril 2026</strong> '
     '(8.4, tableau 14, [210] ; la section 4.11.5 écrivait déjà avril 2026) n’y était pas reconfirmée en '
     'source primaire ; la lecture du PDF hors passe tranche depuis pour une publication d’avril 2026 d’un '
     'document daté de mars (annexe de novembre, erratum 1).</p>'),
    # annexe des sigles : appels des tableaux 17 et 18
    ('<p>Sigles, puis famille processus et pile agentique — les écarts résument la section 4.11.</p>',
     '<p>Sigles (tableau 17), puis famille processus et pile agentique (tableau 18) — les écarts résument '
     'la section 4.11.</p>'),
    # tableau 18
    ('<td>confirmation avant effet ; refus remédiable (4.10)</td>',
     '<td>confirmation avant effet ; refus remédiable (4.11.2, 4.11.3, 4.11.5)</td>'),
    # tableau 19
    ('Même défaut que la ligne suivante, trouvé par le même moyen.', 'Même défaut que la ligne précédente, trouvé par le même moyen.'),
    ('state=all&amp;sort=updated', 'state=all&amp;' + ZWSP + 'sort=updated', None),
    # tableau 20 : l'issue ne décrit pas l'édition publiée
    ('<td>légendes redescendues après le tableau, dans tous les artefacts</td>',
     '<td>légendes redescendues après le tableau dans les artefacts de la passe ; l’édition publiée les place '
     'pourtant avant (relecture du 3 novembre 2026)</td>'),
    # tableau 21, ligne 1 : report de la lecture du 29 octobre et du PDF lu hors passe (erratum 1)
    ('<td>date de finalisation du 7 avril 2026, champ d’application, contenu, entrée en vigueur du 1er mai 2027</td>'
     '<td>aucun de ces faits n’est établi en source primaire. La revue rétracte la certitude de sa propre '
     'datation ; les énoncés correspondants sont au conditionnel et doivent tomber si la revalidation '
     'suivante échoue encore</td>',
     '<td>date de finalisation du 7 avril 2026, champ d’application, contenu, entrée en vigueur du 1er mai 2027</td>'
     '<td>aucun de ces faits n’est établi en source primaire par l’outillage au gel (la page de l’AMF lue le '
     '29 octobre et le PDF lu le 31 octobre hors passe attestent depuis avril 2026 sur un texte daté de mars '
     'et la prise d’effet du 1er mai 2027 : annexe du 29 octobre, [366], et annexe de novembre, erratum 1)</td>'),
    # tableaux 22 et 24 : 217 et 219 comptés deux fois
    ('<tr><td>Orchestration des processus</td><td>167, 169, 173, 174, 175, 181, 188, 189, 190, 203, 214, 217, '
     '219, 224, 226, 230, 231, 232, 287</td><td>dix-neuf numéros pour <strong>dix-sept références déclarées</strong> '
     '— l’écart n’est pas résolu</td>',
     '<tr><td>Orchestration des processus et exploitation (4.11, 4.13)</td><td>167, 169, 173, 174, 175, 181, '
     '188, 189, 190, 203, 214, 224, 226, 230, 231, 232, 287</td><td><strong>dix-sept</strong>, 217 et 219 '
     'étant comptées à la ligne précédente</td>'),
    ('dix-sept à dix-neuf références de faible volatilité', 'dix-sept références de faible volatilité'),
    # références
    ('Communiqué, 26 août 2025. https://my.idc.com/getdoc.jsp?containerId=prUS53765225',
     'Communiqué, 26 août 2025 — même pièce que [275], qui en porte la réserve de lecture. '
     'https://my.idc.com/getdoc.jsp?containerId=prUS53765225'),
    ('; exposition des flots RPA, agents, flots API et processus BPMN Maestro comme outils MCP)',
     '; l’énumération des flots RPA, agents, flots API et processus BPMN Maestro exposés comme outils MCP ne '
     'se lit pas dans la note : 4.11.2)'),
    ('dix produits aux résultats publiés, dont', 'huit produits aux résultats publiés et trois sans résultat, '
     'décompte non fixé (tableau 20), dont'),
    ('le reste annoncé « in the coming months ».', 'le reste annoncé pour plus tard.'),
    (' ( <em>adresse relevée le 17 août 2026', ' (<em>adresse relevée le 17 août 2026', 3),
    ('<li><p>Amazon Web Services. Annonces du 6 août 2026 —',
     '<li><p>Amazon Web Services. Annonces du 6 août 2026 (adresses exactes : [394], annexe de novembre, pour '
     'les instances ; [333] pour la préversion du registre) —'),
    ('; chaque cas d’usage d’un modèle sous-jacent capturé et évalué séparément)',
     '; inventaire des usages approuvés — l’évaluation séparée de chaque cas d’usage ne s’y lit pas en ces '
     'termes, 4.11.5)'),
    # réf. [210] : renvoi à l'erratum 1 sur l'AMF
    ('date de finalisation du 7 avril 2026 non reconfirmée en source primaire, corroborée par la seule '
     'analyse secondaire d’un cabinet juridique canadien (sections 8.4 et 13.6).',
     'date de finalisation du 7 avril 2026 non reconfirmée en source primaire, corroborée par la seule '
     'analyse secondaire d’un cabinet juridique canadien (sections 8.4 et 13.6 ; PDF daté de mars 2026 et '
     'publié en avril, lu depuis hors passe : annexe de novembre, erratum 1).'),
    # annexe du 29 octobre : appel du tableau 26
    ('<p>La relecture intégrale du 29 octobre relève onze erreurs internes.',
     '<p>La relecture intégrale du 29 octobre relève onze erreurs internes (tableau 26).'),
    # tableau 12 : AWS et Google (sections 4.14, 7.2; annexe de novembre)
    ('<td>Gateway MCP et Agent Registry <strong>GA le 13 octobre 2025</strong> ;',
     '<td>Gateway MCP <strong>GA le 13 octobre 2025</strong> ; Agent Registry en préversion depuis le 9 avril '
     '2026, relancé le 6 août, non général au 15 août (4.14) ;'),
    ('type de calcul <em>Instances</em> du <em>Runtime</em> annoncé le 6 août 2026 — aucune entrée n’en énonce '
     'la disponibilité générale</td>',
     'type de calcul <em>Instances</em> du <em>Runtime</em> en disponibilité générale le 6 août 2026 [290]</td>'),
    ('Agent Registry (agents et serveurs MCP), Agent Gateway et serveur MCP distant <strong>GA le 18 juin 2026</strong>',
     'Agent Registry (agents et serveurs MCP) et Agent Gateway <strong>GA le 18 juin 2026</strong>, serveur MCP '
     'distant GA dès le lancement du 22 avril (annexe de novembre)'),
    # 8.5 : la rétractation de 4.11.5 sur E-23
    ('E-23 exige que chaque cas d’usage d’un modèle soit capturé et évalué séparément,',
     'E-23 exige un inventaire des usages approuvés de chaque modèle (4.11.5),'),
]

# Corrections supplémentaires issues de l'audit intégral (lots VT1 à VT7, O-18..O-22, § 10.8)
CORRECTIONS_AUDIT = [
    # VT1-03, VT1-20 : Résumé, Abstract, Sommaire chapeau
    ('où chaque affirmation est confrontée aux sources primaires et soumise à contradiction',
     'où chaque affirmation est confrontée aux sources primaires et les plus exposées soumises à une ronde adverse (§2.2)'),
    ('l’audit intégral de bibliographie du 8 août — première édition ramenée à un format ferme —, au même régime déclaré',
     'l’audit intégral de bibliographie de l’édition du 8 août — la première au format arrêté —, au même régime déclaré'),
    ('in which every claim is checked against primary sources and subjected to challenge',
     'in which every claim is checked against primary sources and the most exposed ones are subjected to adversarial review (§2.2)'),
    ('the full bibliography audit of 8 August — the first edition brought down to a fixed format — under',
     'the full bibliography audit of the 8 August edition — the first in fixed format — under'),
    ('<p>Revue vérifiée : chaque affirmation factuelle est confrontée à sa source primaire et soumise à contradiction (2).',
     '<p>Veille vérifiée : chaque affirmation factuelle est confrontée à sa source primaire ; les plus exposées sont soumises à une ronde adverse (régimes en 2.2).'),
    # VT1-02 : Sommaire constat 2 (Block)
    ('Block déclare qu’en juin l’IA agentique a écrit ou révisé la quasi-totalité de son code [271]',
     'Block déclare qu’en juin l’IA agentique a aidé à écrire et à réviser la quasi-totalité de ses changements de code de production [271]'),
    # VT1-14 & Coquille VT1 p. 5 : Sommaire constat 4 (DMN et ISO/CEI 19510)
    ('seule couche au cœur normalisé <em>de jure</em> (BPMN/ISO 19510, XES/IEEE 1849-2023, DMN et son kit de conformité)',
     'seule couche au cœur normalisé <em>de jure</em> (BPMN/ISO/CEI 19510, XES/IEEE 1849-2023), plus DMN, spécification de l’OMG dotée d’un kit de conformité'),
    # VT4-17 & Erratum 7 : Sommaire constat 6 (art. 12.1 de la LPRPSP)
    ('Un raccourci tombe : l’article 12.1 de la Loi 25 n’exige aucune intervention humaine déterminante ; déclenché par la décision fondée <em>exclusivement</em> sur un traitement automatisé, il impose information, observations devant un employé habilité à réviser et, sur demande, communication des raisons et des principaux facteurs et paramètres de la décision (8.4) : il borne l’absence d’humain, non le degré d’autonomie.',
     'Un raccourci tombe : l’article 12.1 de la LPRPSP (introduit par la Loi 25) n’exige aucune intervention humaine déterminante ; déclenché par la décision fondée <em>exclusivement</em> sur un traitement automatisé, il impose information au plus tard lors de la décision, observations devant un membre du personnel en mesure de la réviser et, sur demande, communication des renseignements utilisés, des raisons et des principaux facteurs et paramètres ayant mené à la décision ainsi que du droit de rectification (4.11.5, 8.4) : il borne l’absence d’humain dans la décision même, non le degré d’autonomie.'),
    # VT1-20 : Sommaire constat 7 (Camunda 7)
    ('Camunda 7, et la GPA classique : maintenance au 13 avril 2030',
     'Camunda 7 (GPA classique) : maintenance au 13 avril 2030'),
    # VT1-15 : Sommaire constat 9 & § 9.7 (douze brouillons IETF)
    ('douze brouillons individuels IETF [162] : aucun adopté',
     'douze brouillons individuels IETF (7.7, dont [162]) : aucun adopté'),
    ('douze brouillons IETF décrivent des chaînes à N sauts, aucun n’est adopté [162].',
     'douze brouillons IETF décrivent des chaînes à N sauts, aucun n’est adopté (7.7, dont [162]).'),
    # VT1-01, VT1-12, VT1-13 : Sommaire constat 12 (AI Act art. 50(1) et art. 74/99)
    ('Le 2 août 2026 : première échéance européenne qu’un déploiement agentique puisse enfreindre, et première fois que le droit européen nomme l’agentique. Ce jour-là, la Commission range les « AI agents » parmi les systèmes à interaction directe soumis à <strong>l’article 50(1)</strong> [278], quand tous les autres régimes examinés n’accrochent l’agent que par inférence. Le même jour, le Bureau IA obtient ses pouvoirs sur les modèles à usage général, jusqu’au retrait et aux amendes (3 % du chiffre d’affaires mondial ; 15 M€ ou 3 % pour la transparence). Le règlement (UE) 2026/1744 reporte le haut risque, mais ni l’article 50, ni ce pouvoir.',
     'Le 2 août 2026 : première échéance européenne qu’un déploiement agentique puisse enfreindre, après le premier texte interprétatif européen à nommer l’agentique. Le 20 juillet 2026, les lignes directrices de la Commission sur l’article 50 (point 31) rangent les « AI agents » parmi les systèmes à interaction directe soumis à <strong>l’article 50(1)</strong> [336], lecture reprise par la FAQ officielle le 24 juillet [278] ; l’obligation s’applique depuis le 2 août, quand tous les autres régimes examinés n’accrochent l’agent que par inférence. Le même jour, le Bureau IA obtient ses pouvoirs sur les modèles à usage général, jusqu’au retrait et aux amendes (jusqu’à 15 M€ ou 3 % du chiffre d’affaires mondial, plafond identique à celui des manquements de transparence). Le règlement (UE) 2026/1744 reporte le haut risque, ne reporte pas l’article 50 — hors un délai de grâce de quatre mois pour l’article 50(2) des systèmes antérieurs —, ni ce pouvoir.'),
    # VT1-10 : § 1 et Tableau 3 (MCP gouvernance AAIF)
    ('le <em>Model Context Protocol</em> (MCP), d’Anthropic [5]',
     'le <em>Model Context Protocol</em> (MCP), d’Anthropic puis de l’Agentic AI Foundation (Linux Foundation) [5, 41]'),
    ('<td>Anthropic / projet ouvert (cf.\xa0§5)</td>',
     '<td>Anthropic / Agentic AI Foundation (Linux Foundation, depuis le 9 déc. 2025 ; cf.\xa0§5)</td>'),
    # VT1-16 : § 1.2 (corpus protocolaire 4.1 à 4.5)
    ('corpus protocolaire et couches implicites (4.6 à 4.10)',
     'corpus protocolaire (4.1 à 4.5) et couches implicites (4.6 à 4.10)'),
    # VT1-07, VT4-09, O-19 : Tableau 1 et § 2.2
    ('Camunda 8.9 (MCP Client en DG, A2A Client en accès anticipé)',
     'Camunda 8.9 (MCP Client sans disponibilité générale énoncée, A2A Client en accès anticipé)'),
    (' — régime de 12.4</td>', ' (tableau 24)</td>', 2),
    ('et les quatre passes de veille, de l’édition d’août au 15 août, n’en ont aucune, pas plus que celle du 23 juillet. La colonne « Énoncés » compte des énoncés, sauf aux 12 et 18 juillet, où elle compte des agents.',
     'et les trois passes de veille, de l’édition d’août au 15 août, n’en ont aucune, ni celles des 4 juillet (deux lignes), 13 juillet (authenticité), 18 juillet (compagnons), 19 et 23 juillet. La colonne « Énoncés » compte des énoncés, sauf aux 12 et 18 juillet (agents, et grappes au 18) et aux 13 juillet et 8 août (références).'),
    ('celui de la sous-section 12.4, non celui des sections 4.6 à 4.13',
     'intermédiaire (tableau 24), sous celui des sections 4.6 à 4.13'),
    ('et trois erreurs dans son propre texte rend surtout compte des secondes.',
     'et quatre erreurs dans son propre texte (§4.1, §4.2, §4.4, §4.12) rend surtout compte des secondes.'),
    # VT1-11 : § 3.3 et § 4.6 (point à point vs synchrone requête-réponse)
    ('les trois protocoles structurants sont synchrones, requête-réponse',
     'les trois protocoles structurants sont point à point (A2A admettant flux SSE et notifications push par webhook, mais sans courtier ni découplage producteur-consommateur)'),
    ('Les trois protocoles structurants sont <em>synchrones et orientés requête-réponse</em> [5, 10].',
     'Les trois protocoles structurants sont <em>point à point</em> : A2A admet flux et notifications push par webhook, mais aucun ne prévoit de courtier ni de découplage producteur-consommateur [5, 10].'),
    # VT1-17, VT1-18, Coquille VT1 p. 14 : § 4.1 et § 4.2
    ('Dépréciés, Roots, Sampling et Logging [252] retirent les deux voies par lesquelles un serveur sollicitait le système de fichiers du client et le modèle de l’hôte (§7.1).',
     'Dépréciés, Roots, Sampling et Logging [252] condamnent à terme — au plus tôt douze mois après dépréciation — les deux voies par lesquelles un serveur sollicitait le système de fichiers du client et le modèle de l’hôte (§7.1).'),
    ('deux de ces demandes ajoutent des scénarios pour la journalisation, que la même révision vient de déprécier.',
     'l’une de ces demandes ajoute des scénarios pour la journalisation (#449, à côté de #450 sur l’annulation et la progression), que la même révision vient de déprécier.'),
    ('intake de vulnérabilités', 'réception des signalements de vulnérabilités'),
    # VT1-08 : § 4.4 (appel [435])
    ('sans poussée depuis le 23 mai 2025 (annexe de novembre)',
     'sans poussée depuis le 23 mai 2025 [435] (annexe de novembre)'),
    # VT1-09 : § 4.5 et Tableau 3
    ('A2A immobile depuis le 28 mai', 'A2A sans publication depuis le 28 mai'),
    ('(état vérifié au 12 juillet 2026).</caption>',
     '(état vérifié au 12 juillet 2026, ligne « Maturité documentée » mise à jour au 15 août).</caption>'),
    # VT2-02, VT2-03, Coquille VT2 p. 17 : § 4.7
    ('Motif non normalisé, que concrétisent trois instances sous gouvernance ouverte.',
     'Motif non normalisé, que concrétisent deux instances sous gouvernance ouverte et une variante d’éditeur.'),
    ('et livrée en v1.4.1 avec une branche principale active jusqu’au 14 août [95]',
     'et livrée en v1.4.1 avec une branche principale active jusqu’au 14 août [95, 221, 222]'),
    ('multi-latérale', 'multilatérale', 3),
    # VT2-01, VT2-05, VT2-06, Coquille VT2 p. 19 : § 4.8, Tableau 4, Ref [125]
    ('Depuis septembre 2025, des protocoles de <em>paiement et de commerce agentiques</em> le comblent',
     'Depuis mai 2025, des protocoles de <em>paiement et de commerce agentiques</em> le comblent'),
    ('Quatre se déclarent extensions de MCP et d’A2A ; le cinquième, MPP, s’y raccorde par une trousse MCP sans s’en réclamer.',
     'Quatre se raccordent à MCP (dont trois aussi à A2A) ; le cinquième, MPP, s’y raccorde par une trousse MCP sans s’en réclamer.'),
    ('co-écrit par', 'coécrit par', 2),
    ('<td>Coinbase, 11 déc. 2025 [125]</td>',
     '<td>Coinbase, 6 mai 2025 (V2 le 11 déc. 2025) [125]</td>'),
    ('<em>Et le protocole le plus adopté de la sous-couche règlement n’a migré nulle part</em>',
     '<em>Et le second protocole de la sous-couche règlement, soutenu par Visa, Stripe et Cloudflare, n’a migré nulle part</em>'),
    ('(protocole de paiement sur HTTP 402 ; V2 publiée le 11 décembre 2025',
     '(protocole de paiement sur HTTP 402 lancé par Coinbase le 6 mai 2025 ; V2 publiée le 11 décembre 2025'),
    # Coquille VT2 p. 21 : § 4.9
    ('aucune n’a dépassé le préprint', 'aucune n’a dépassé la prépublication'),
    # VT2-07, VT2-08, VT2-09, VT2-04, VT2-11, Coquille VT2 p. 22 : § 4.10 et Tableau 6
    ('Deux des trois familles de la section 7.2 sont en production — charge de travail chez Google, où l’agent devient un principal IAM à identité SPIFFE propre [153], standard que recommandait la CNCF [56, 156] ; décentralisée chez AGNTCY, dont les « Agent Badges » sont des justificatifs vérifiables W3C [29, 152] —, la troisième (extensions OAuth/OIDC) aucune.',
     'Des trois familles de la section 7.2, une est en production — charge de travail chez Google, où l’agent devient un principal IAM à identité SPIFFE propre [153], standard que recommandait la CNCF [56, 156] —, une deuxième est publiée en préversion — décentralisée chez AGNTCY, dont les « Agent Badges » (v0.0.23) sont des justificatifs vérifiables W3C [29, 152] —, la troisième (extensions OAuth/OIDC) n’ayant aucune mise en œuvre agentique vérifiée.'),
    ('le chaînage d’identité et d’autorisation entre domaines de confiance (RFC 8693 [27], RFC 7523) est en file d’attente du RFC Editor',
     'le chaînage d’identité et d’autorisation entre domaines de confiance, bâti sur les RFC 8693 [27] et 7523, est en file d’attente du RFC Editor'),
    ('la BoF GARR, sur un registre et une résolution d’agents à portée mondiale, l’a été le 22 mai [159]. Mais trois BoF agentiques ont été approuvées en juin 2026 :',
     'la BoF GARR, sur un registre et une résolution d’agents à portée mondiale, a été refusée le 22 mai [159]. Mais trois BoF agentiques ont été approuvées en juin 2026 (avec « Agent Communication Protocols », exploratoire) :'),
    ('les sources de [95], [153], [154] et [155] n’ont pas été rouvertes dans ce tour.',
     'les sources de [153] (corrigée à la relecture, tableau 31), [154] et [155] n’ont pas été rouvertes dans ce tour ([95] étant revérifiée au 15 août en §4.7).'),
    ('trois incarnations en production sans pile commune ici.',
     'trois incarnations (deux en production chez Google et Microsoft, une en préversion chez AGNTCY) sans pile commune ici.'),
    ('Ce qui avait changé au printemps est l’étage de la délégation, où des documents <em>adoptés</em> et une spécification <em>finale</em> offrent des briques génériques',
     'Ce qui avait changé depuis l’hiver tient aux étages de la délégation (documents <em>adoptés</em>) et de l’autorisation (spécification <em>finale</em> de janvier), qui offrent des briques génériques'),
    # VT2-12, VT2-13, VT2-14, VT2-15, VT2-16, VT2-17, VT2-18, VT2-19, VT2-20, Coquilles VT2 : § 4.11 à § 4.14
    ('<em>Le moteur de processus se fait client des protocoles agentiques, jamais l’inverse.</em>',
     '<em>Le moteur de processus se fait client des protocoles agentiques ou s’y expose comme outil ; jamais il ne leur cède sa sémantique de processus.</em>'),
    ('<em>Le moteur consomme MCP et A2A comme contrats externes</em> ; la réciproque n’existe pas, et la sémantique de <em>processus</em> reste au moteur.',
     '<em>Le moteur consomme MCP et A2A comme contrats externes ou s’y expose en outil</em> ; la réciproque protocolaire n’existe pas, et la sémantique de <em>processus</em> reste au moteur.'),
    ('un <em>déploiement</em> d’ici <em>2029</em> (Gartner), ou <em>45 %</em> d’ici 2030 (IDC).',
     'un <em>déploiement</em> d’ici <em>2029</em> (Gartner) ou <em>45 %</em> d’orchestration d’ici 2030 (IDC ; voir §6.5 et §12.2).'),
    ('socle établi le 15 juillet, revérifié le 8 août',
     'socle établi le 15 juillet, revérifié les 8 et 15 août'),
    ('conception <em>et</em> exécution MCP livrées — non annoncées',
     'conception <em>et</em> exécution MCP livrées, et non seulement annoncées'),
    ('contre 72,4 % chez l’humain (AI Index, 7.5).',
     'contre 72,4 % chez l’humain (AI Index [76], §7.5).'),
    ('là où le TCK de DMN vérifie la conformité à une norme <em>de jure</em>',
     'là où le TCK de DMN vérifie la conformité à une norme formelle de consortium (OMG)'),
    ('la GDA avec DMN [165]', 'la gestion des décisions d’affaires (GDA) avec DMN [165]'),
    ('Deuxième norme <em>de jure</em> de la couche après ISO/CEI 19510, elle porte',
     'XES, deuxième norme <em>de jure</em> de la couche après ISO/CEI 19510, porte'),
    ('au registre Agent 365 (préversion privée au 1er mai, statut inchangé) [206]',
     'au registre Agent 365 (intégration Celonis en préversion privée depuis le 1er mai, statut inchangé) [206]'),
    ('seules des sources secondaires les documentent [210].',
     'seules des sources secondaires les documentent au gel [210] (PDF daté de mars 2026 et publié en avril, lu depuis hors passe : annexe de novembre, erratum 1).'),
    ('L’article 12.1 de la Loi 25 québécoise (renseignements personnels, secteur privé), en vigueur depuis le 22 septembre 2023',
     'L’article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (LPRPSP, introduit par la Loi 25), en vigueur depuis le 22 septembre 2023'),
    ('seule région normalisée <em>de jure</em> — BPMN par l’ISO à une révision près [163, 164], les journaux par l’IEEE [201], la décision par son kit de conformité [196] —',
     'seule région dotée de normes <em>de jure</em> — BPMN par l’ISO à une révision près [163, 164], les journaux par l’IEEE [201] — et d’une spécification formelle de consortium à kit de conformité public pour la décision [165, 196],'),
    ('et plus de dépôt ouvert où les rejouer.',
     'et plus de dépôt ouvert où rejouer les défauts propres au démonstrateur, les comportements des SDK amont restant rejouables.'),
    ('ce qu’exigent l’article 12.1 de la Loi 25 et la journalisation probatoire d’E-23 (sections 8.4 et 8.5).',
     'ce que supposent l’article 12.1 de la LPRPSP (restitution des raisons et facteurs) et l’inventaire des usages approuvés d’E-23 (sections 8.4 et 8.5).'),
    ('et aucune des huit propositions qui la visent n’a été fusionnée [233, 234].',
     'et aucune des huit propositions qui la visent n’a été résolue ni fermée [233, 234].'),
    ('par l’organisation du cadriciel le plus employé du domaine [262]',
     'par l’organisation de LangGraph [262]'),
    ('La documentation du SDK d’agents le plus diffusé l’énonce',
     'La documentation de l’OpenAI Agents SDK l’énonce'),
    ('bibliothèque de patron par son éditeur', 'bibliothèque de patrons par son éditeur'),
    # VT3-01 à VT3-23, Coquilles VT3 : § 5 à § 7
    ('la charte du groupe <em>Agents</em>, <strong>fusionnée le 5 août 2026</strong>, veut promouvoir <em>Tasks</em> <strong>dans le protocole de base</strong>, l’inverse de la révision <code>2026-07-28</code> [266] : en dix jours',
     'la charte du groupe <em>Agents</em>, <strong>proposée le 5 août 2026</strong> (demande de tirage n° 3200), veut promouvoir <em>Tasks</em> <strong>dans le protocole de base</strong>, l’inverse de la révision <code>2026-07-28</code> [266] : en huit jours'),
    ('aucune activité depuis juin 2025 [16]',
     'aucune activité après août 2025 [16, 138]'),
    ('révocation et cycle de vie des attestations, <strong>cryptographie post-quantique</strong>',
     '<strong>révocation et cycle de vie des attestations</strong>, <strong>cryptographie post-quantique</strong>'),
    ('La fenêtre du 8 au 15 août produit deux révisions et zéro RFC. Le groupe WIMSE verse <code>draft-ietf-wimse-http-signature-06</code> le 4 août et <code>draft-ietf-wimse-workload-identity-practices-06</code> le <strong>11 août 2026</strong>',
     'La fenêtre du 8 au 15 août produit une révision — après <code>draft-ietf-wimse-http-signature-06</code> versé le 4 août — et zéro RFC : le groupe WIMSE verse <code>draft-ietf-wimse-workload-identity-practices-06</code> le <strong>11 août 2026</strong>'),
    ('demeure au 15 août en file du RFC Editor',
     'demeure, à la vérification du 13 août, en file du RFC Editor'),
    ('en brouillons le 15 juin 2026 [79], dont le texte en vigueur est au dépôt du groupe [327] ;',
     'annoncés en brouillons le 15 juin 2026 [79], dont le texte en vigueur au dépôt du groupe est daté du 13 février 2026 pour la liaison MCP [327] ;'),
    ('Lignes W3C, IETF, OASIS, OpenID Foundation, NIST, OCDE, <em>Five Eyes</em> et FIDO Alliance rouvertes en source primaire le 15 août 2026 ; les autres lignes à l’état vérifié au 12 juillet 2026.',
     'Lignes Linux Foundation, W3C, IETF, OASIS, OpenID Foundation, NIST, OCDE, <em>Five Eyes</em>, FIDO Alliance et x402 Foundation (tentative, site non joignable) rouvertes en source primaire le 15 août 2026 ; la ligne CNCF (repère) à l’état vérifié au 12 juillet 2026.'),
    ('inactif depuis juin 2025', 'inactif depuis août 2025'),
    ('nº ', 'n° ', 3),
    ('durci le 7 août 2026 et inchangé depuis [263]',
     'durci le 7 août 2026, sans fusion depuis mais six demandes de tirage ouvertes ou remises à jour en août [263]'),
    ('L’écart entre 2 000 et « plus de 10 000 » qui traînait dans la littérature n’était pas une querelle de sources, c’était une querelle de curseur.',
     'L’écart entre 2 000 et « plus de 10 000 » qui traînait dans la littérature peut ainsi tenir en partie à ce que l’on compte (objets ou versions, registre ou parc).'),
    ('celle-ci est la seule dont la méthode le soit.',
     'celle-ci est la seule dont la méthode soit publiée et reproductible.'),
    ('la revue n’est pas l’écriture, une quinzaine n’est pas un trimestre.',
     'la révision de code n’est pas l’écriture, une quinzaine n’est pas un mois (la nouvelle mesure portant sur juin).'),
    ('documenté de bout en bout par ses trois parties, en juillet 2026',
     'documenté de bout en bout par ses deux parties et par un tiers (CSA), en juillet 2026'),
    ('dont le communiqué primaire dit la croissance « portée par » l’agentique [82, 275].',
     'dont le communiqué primaire dit la croissance « portée par » l’agentique — confusion qu’entretient le titre même du communiqué [82, 275].'),
    ('il a détecté et contenu le 16 juillet, cinq jours avant qu’OpenAI ne relie sa propre évaluation à l’intrusion. Les durées se réconcilient de même : un week-end de latéralisation <em>chez Hugging Face</em>, à l’intérieur d’une intrusion de quatre jours commencée sur le réseau du fournisseur.',
     'il a divulgué l’incident dès le 16 juillet après l’avoir détecté et contenu, cinq jours avant qu’OpenAI ne relie sa propre évaluation à l’intrusion : un week-end de latéralisation <em>chez Hugging Face</em>, que la directive de la CSA inscrit dans une séquence de quatre jours commencée sur le réseau du fournisseur.'),
    ('Contre-exemple de rigueur : l’affirmation répandue selon laquelle les premières versions de MCP n’auraient comporté <em>aucune</em> authentification est <strong>réfutée à l’unanimité</strong> par notre procédure de vérification (section 2).',
     'Nuance d’historique sur le protocole : la révision initiale de MCP (<code>2024-11-05</code>) ne spécifiait aucun mécanisme d’autorisation au niveau du protocole, mais dès la révision <code>2025-03-26</code> un cadre d’autorisation fondé sur OAuth 2.1 (facultatif et réservé aux transports HTTP) y a été introduit [5] — l’affirmation selon laquelle toutes les versions de première année auraient été dépourvues de cadre d’authentification a été écartée lors de la vérification (section 2).'),
    ('complétée en juin par deux brouillons de groupe (appels d’outils MCP, section 5.4) [78, 79].',
     'complétée par deux brouillons de groupe annoncés en juin (liaison MCP datée du 13 février 2026 au dépôt, section 5.4) [78, 79, 327].'),
    ('<em>Reconduit du gel antérieur sans revérification : la page « nouveautés » d’Entra est servie dans un état arrêté au 30 juin 2026 et ne mentionne pas Dataverse ; l’entrée [301] ne porte pas de page cible.</em>',
     '<em>Revérifié le 15 août 2026 sur la page « nouveautés » d’Entra [155], servie dans un état arrêté au 30 juin 2026 qui ne mentionne pas Dataverse ; l’annonce du 6 août est reconduite d’après [301], dont l’entrée ne porte pas de page cible.</em>'),
    ('Du 8 au 15 août 2026, l’appareil normatif <strong>produit sans franchir la ligne</strong>.',
     'Du 6 au 15 août 2026, l’appareil normatif <strong>produit sans franchir la ligne</strong>.'),
    ('passées en révision −06 le 11 août et en évaluation de direction de zone à l’IESG [144]',
     'passées en révision −06 le 11 août, toujours en évaluation de direction de zone à l’IESG (état déjà acquis en −05 au 30 juin) [144]'),
    ('ce que le mécanisme <strong>démontre</strong> [219].</p>',
     'ce que le mécanisme <strong>démontre</strong> (tableau 13) [219].</p>'),
    ('la troisième colonne est la plus vide du tableau. <em>Les cellules reportent l’état du gel antérieur : parmi les sources citées, seules celles de [10], [56], [57], [105], [107], [148] et [149] ont été rouvertes au 15 août 2026 ; [22], [29], [42], [58], [118] et [122] ne l’ont pas été.</em>',
     'la colonne <em>Pour qui agis-tu</em> est la plus vide des trois questions d’identité (la colonne <em>Qui en répond</em>, plus vide encore, relevant du contrat et de l’organisation). <em>Les cellules reportent l’état du gel antérieur : parmi les sources citées, seules celles de [10], [56], [57], [105], [107], [122] (salle de presse FIDO), [148] et [149] ont été rouvertes au 15 août 2026 ; [22], [29], [42], [58] et [118] ne l’ont pas été.</em>'),
    ('AuthZEN /points de décision', 'AuthZEN / points de décision'),
    ('<em>Pour qui agis-tu</em> est la seule colonne presque vide, et son exception est instructive',
     'Parmi les trois questions d’identité, <em>Pour qui agis-tu</em> est la seule colonne presque vide (la cinquième question relevant du droit et de l’organisation), et son exception est instructive'),
    ('la troisième colonne est désormais l’objet',
     'la colonne <em>Pour qui agis-tu</em> est désormais l’objet'),
    ('respectivement depuis les 16 et 30 septembre 2025 et le 25 mars 2026.',
     'respectivement depuis le 16 septembre 2025, le 25 mars 2026 et le 30 septembre 2025.'),
    ('<code>-01</code> du profil SCITT', '<code>−01</code> du profil SCITT'),
    ('les seuls groupes DAWN et DMSC en portent vingt-sept',
     'l’enceinte DAWN (groupe charté) et la BoF DMSC en portent vingt-sept'),
    ('eIDAS et la FIDO Alliance n’ont de travaux applicables que dans le périmètre du paiement [122].',
     'la FIDO Alliance n’a de travaux applicables que dans le périmètre du paiement [122], et eIDAS n’outille en propre que l’identité des personnes physiques et morales, même si les lignes directrices européennes y renvoient pour attester des agents (§8.3, [336]).'),
    ('et les douze brouillons de la section 7.7 signent tous en Ed25519 ou en EdDSA.',
     'et ceux des douze brouillons de la section 7.7 qui fixent un algorithme le fixent en EdDSA (Ed25519 compris) [276, 315].'),
    ('deux groupes agentiques chartés en juin, vingt-sept brouillons entre eux',
     'un groupe agentique charté en juin (DAWN), une BoF restée sans charte (DMSC), vingt-sept brouillons entre eux'),
    # VT4-01 à VT4-24, Coquilles VT4 : § 8 à § 14, annexes sigles et traçabilité
    ('avec amendes jusqu’à 3 % du chiffre d’affaires mondial ; les manquements de transparence, jusqu’à 15 millions d’euros ou 3 % [38].',
     'avec amendes jusqu’à 15 millions d’euros ou 3 % du chiffre d’affaires mondial, plafond identique à celui des manquements de transparence [38].'),
    ('Un agent qui n’annonce ni sa nature ni son commettant enfreint l’article 50',
     'Un agent qui n’annonce pas sa nature artificielle enfreint l’article 50(1), et les lignes directrices de la Commission (point 31, non contraignantes) y ajoutent la déclaration de son commettant [336]'),
    ('L’article 50 exige d’un agent qu’il déclare <em>sa nature</em> et <em>son commettant</em> [336] : ni l’un ni l’autre n’a de support protocolaire.',
     'L’article 50(1), tel que l’interprètent les lignes directrices de la Commission (point 31, non contraignantes), attend d’un agent qu’il déclare <em>sa nature</em> (obligation du règlement) et <em>son commettant</em> (lecture de la Commission) [336] : ni l’un ni l’autre n’a de support protocolaire.'),
    ('l’article 12.1 de la Loi 25, que l’édition précédente sous-lisait.',
     'l’article 12.1 de la LPRPSP (introduit par la Loi 25), que l’édition précédente sous-lisait.'),
    ('<code>legisquebec.gouv.qc.ca</code> a refusé la consultation à nos deux tentatives ; le verbatim est établi par vérification indépendante en source officielle, non par accès propre (cf.\xa0relevé de preuves).',
     '<code>legisquebec.gouv.qc.ca</code> a refusé la consultation automatisée (HTTP 403, quatre variantes d’URL testées jusqu’au 15 août 2026) ; le verbatim est établi par vérification indépendante en source officielle, non par accès propre (tableau 21).'),
    ('<em>cette date ne figure toujours pas sur la page primaire de Paiements Canada</em>.',
     '<em>cette date ne figure pas sur la page du système RTR de Paiements Canada [257], mais est établie par son communiqué du 30 juin 2026 [430] (annexe de novembre, erratum 3)</em>.'),
    ('contre le 7 avril ici [210]', 'contre le 7 avril dans l’édition du gel [210]'),
    ('<strong>Synthèse</strong> (section 12) :',
     '<strong>Synthèse</strong> (grille de la section 12 ; section 12 de la monographie [218]) :'),
    ('il est écrit trois fois, en six semaines, et jamais entièrement.',
     'il est écrit trois fois en une semaine de juillet 2026 (après la directive des <em>Five Eyes</em> du 1er mai), et jamais entièrement.'),
    ('portait sur <em>pour qui agis-tu</em> (question ouverte 13) — c’est précisément la propriété que le premier régulateur à nommer les agents leur impose de déclarer depuis le 2 août 2026, et que la couche protocolaire n’exprime toujours pas. L’écart a cessé d’être une hypothèse d’architecte ; il est devenu une non-conformité datée.',
     'portait sur <em>pour qui agis-tu</em> (7.6) — c’est précisément la propriété que les lignes directrices de la Commission sur l’article 50 (instrument interprétatif non contraignant d’une obligation applicable depuis le 2 août 2026) demandent aux agents de déclarer [336], et que la couche protocolaire n’exprime toujours pas. L’écart a cessé d’être une seule hypothèse d’architecte pour entrer dans la doctrine administrative européenne.'),
    ('Agent-outils, fait accompli — un demi-milliard de téléchargements mensuels [269]',
     'Agent-outils, fait accompli — près d’un demi-milliard de téléchargements mensuels déclarés par le projet, 400 millions selon Anthropic [269, 270]'),
    ('40 % de projets annulés d’ici fin 2027 [80]',
     'plus de 40 % de projets annulés d’ici fin 2027 [80]'),
    ('Corpus anglophone ; revue structurée et vérifiée, non systématique au sens PRISMA (section 2)',
     'Corpus anglophone ; veille structurée et vérifiée, non revue systématique au sens PRISMA (section 2)'),
    ('Son régime est celui de la sous-section 12.4, <strong>non celui des sections 4.6 à 4.13</strong> ;',
     'Leur régime est intermédiaire : sources primaires rouvertes individuellement, sans ronde adverse (tableau 24), <strong>au-dessous des sections 4.6 à 4.13</strong> mais au-dessus de la sous-section 12.4 qui descend aux seules métadonnées ;'),
    ('Trois sources publiques refusent la consultation automatisée, toutes en réponse 403 : le domaine du régulateur québécois (sept tentatives sur cinq adresses), le service législatif québécois (trois tentatives) et, ajouté le 8 août 2026, CanLII.',
     'Plusieurs sources refusent la consultation automatisée (tableau 21), dont trois sources publiques portant des énoncés réglementaires canadiens, toutes en réponse 403 : le domaine du régulateur québécois (sept tentatives sur cinq adresses), le service législatif québécois (quatre variantes d’URL testées jusqu’au 15 août 2026) et, ajouté le 8 août 2026, CanLII.'),
    ('(QO 21)', '(question ouverte 21)'),
    ('[162] [276] [277]', '[162, 276, 277]'),
    ('(QO 2)', '(question ouverte 2)'),
    ('Aucune des sept couches (4.6 à 4.13)', 'Aucune des sept couches (4.6 à 4.11 et 4.13)'),
    ('approbation de façade, déférence accrue devant une justification mieux rédigée [219] ?',
     'approbation de façade, déférence accrue devant une justification mieux rédigée (hypothèses de programme formulées en [219]) ?'),
    ('Le tableau 14 porte les deux bornes fermes : E-23 et la ligne directrice de l’AMF au 1er mai 2027 [209, 210]',
     'Le tableau 14 porte une borne ferme vérifiée au gel — E-23 au 1er mai 2027 [209] — et la ligne directrice de l’AMF à la même date, tenue au conditionnel au gel (§8.4) puis attestée hors passe sur la page primaire de l’AMF [210, 366] (annexe de novembre, erratum 1)'),
    ('<tr><td>7-14 avril 2026</td><td>ligne directrice IA de l’AMF, finale en avril 2026, document daté de mars [210] — le 7 avril ne se cite qu’avec sa source secondaire (annexe de novembre, erratum 1) ; Camunda 8.9, 14 avril (connecteur MCP sorti de l’arbre alpha, sans disponibilité générale énoncée ; connecteurs A2A alpha) [170]</td></tr>',
     '<tr><td>avril 2026</td><td>ligne directrice IA de l’AMF, finale en avril 2026, document daté de mars [210, 366] — le 7 avril ne se cite qu’avec sa source secondaire (annexe de novembre, erratum 1)</td></tr><tr><td>14 avril 2026</td><td>Camunda 8.9 (connecteur MCP sorti de l’arbre alpha, sans disponibilité générale énoncée ; connecteurs A2A alpha) [170]</td></tr>'),
    ('<tr><td>1er mai 2027</td><td>entrée en vigueur simultanée d’E-23 et de la ligne directrice IA de l’AMF [209, 210]</td></tr>',
     '<tr><td>1er mai 2027</td><td>entrée en vigueur d’E-23 [209] et prise d’effet de la ligne directrice IA de l’AMF (au conditionnel au gel, §8.4 ; attestée hors passe sur la page de l’AMF, [210, 366])</td></tr>'),
    ('La fenêtre d’août 2026 ajoute quatre échéances.',
     'La fenêtre d’août 2026 ajoute trois échéances.'),
    (' <strong>Décembre 2026</strong>, les deux interdictions nouvelles.', ''),
    ('<p>La consolidation transactionnelle.', '<p><strong>La consolidation transactionnelle.</strong>'),
    ('<p>L’interopérabilité multilatérale ouverte.', '<p><strong>L’interopérabilité multilatérale ouverte.</strong>'),
    ('<p>Septième, la sémantique de processus.', '<p><strong>La sémantique de processus.</strong>'),
    ('<p>Huitième, le plus incertain : la stabilisation d’une convention d’observabilité agentique.',
     '<p><strong>La stabilisation d’une convention d’observabilité agentique.</strong>'),
    ('sinon la journalisation probatoire (8.4, 8.5) reste satisfaite par l’enveloppe.',
     'sinon l’exigence probatoire (8.4, 8.5) reste satisfaite par l’enveloppe.'),
    ('douze préimpressions arXiv', 'douze prépublications arXiv'),
    ('rejouable dans le seul historique git.',
     'rejouable dans le seul historique git pour les défauts propres au démonstrateur (les comportements des SDK amont restant rejouables sur leurs dépôts publics).'),
    ('ne prête qu’un instrument sans autorité normative : la grille des cinq questions (7.6) [219].',
     'ne prête que deux instruments d’analyse sans autorité normative : la grille des cinq questions (7.6) et la partition des trois temps — émettre, appliquer, exploiter (9.7) [219].'),
    ('(refus HTTP 403, 18 juillet et 8 août 2026)',
     '(refus HTTP 403 les 18 juillet, 8 août et 15 août 2026)'),
    ('Quatre instruments — tri <em>programmé / projeté / spéculatif</em>, degrés d’absence, grille des cinq questions, traçabilité de fusion —',
     'Cinq instruments — tri <em>programmé / projeté / spéculatif</em>, degrés d’absence, grille des cinq questions, partition des trois temps (9.7), traçabilité de fusion —'),
    ('Deux corrections de fond sur la lecture d’un texte juridique. L’article 12.1 de la Loi 25 n’exige',
     'Deux corrections de fond sur la lecture d’un texte juridique. L’article 12.1 de la LPRPSP (introduit par la Loi 25) n’exige'),
    ('Émettre est résolu, appliquer borné, exploiter vide (4.13)',
     'Émettre est le mieux servi, appliquer borné, exploiter vide (4.13, 9.7)'),
    ('En dix jours de fenêtre, six énoncés porteurs de l’édition précédente ont été réfutés sur source primaire — dont deux sur le calendrier réglementaire, et un sur le déficit qu’elle tenait pour son résultat central : au-delà de deux sauts de délégation, la traçabilité opposable n’est plus absente des documents mais des normes. Une revue dont dix jours suffisent à réfuter six énoncés porteurs mesure moins sa faiblesse que la vitesse de son objet',
     'Lors de la passe du 29 juillet au 8 août (dix jours de fenêtre), six énoncés porteurs de l’édition précédente ont été réfutés sur source primaire — suivis de onze réfutations au tour du 15 août (tableau 19) ; au-delà de deux sauts de délégation, la traçabilité opposable n’est plus absente des documents mais des normes. Une veille dont dix jours suffisent à réfuter six énoncés porteurs mesure moins sa faiblesse que la vitesse de son objet'),
    # VT4-24 : Tableau 17 développé et trié alphabétiquement
    ('<table><caption>Tableau\xa017.\xa0– Sigles employés dans cette revue (sélection ; les sigles des sections 1 à 8 non repris ici sont définis à leur première occurrence).</caption><thead><tr><th>Sigle</th><th>Signification</th></tr></thead><tbody><tr><td>A2A</td><td><em>Agent2Agent</em></td></tr><tr><td>AAIF</td><td><em>Agentic AI Foundation</em></td></tr><tr><td>AARP / COAZ</td><td>profils agentiques d’AuthZEN</td></tr><tr><td>AGNTCY</td><td>écosystème d’agents</td></tr><tr><td>AuthZEN</td><td>Authorization API 1.0</td></tr><tr><td>ANP</td><td><em>Agent Network Protocol</em></td></tr><tr><td>ACVM</td><td>Autorités canadiennes en valeurs mobilières</td></tr><tr><td>ADS</td><td>architecture détaillée de solution</td></tr><tr><td>AP2 / ACP / UCP</td><td>couche transactionnelle</td></tr><tr><td>APA</td><td><em>Agentic Process Automation</em></td></tr><tr><td>A-BPMS</td><td><em>Agentic BPM Systems</em></td></tr><tr><td>BOAT</td><td><em>Business Orchestration and Automation Technologies</em></td></tr><tr><td>BPMN</td><td><em>Business Process Model and Notation</em></td></tr><tr><td>CMMN</td><td><em>Case Management Model and Notation</em></td></tr><tr><td>CNCF</td><td><em>Cloud Native Computing Foundation</em></td></tr><tr><td>CoSAI / CSA</td><td><em>Coalition for Secure AI</em> ; <em>Cloud Security Alliance</em></td></tr><tr><td>CUA</td><td><em>Computer-Using Agent</em></td></tr><tr><td>CVE / CNA</td><td>vulnérabilité publique ; autorité</td></tr><tr><td>DID / VC</td><td>identifiants décentralisés ; justificatifs</td></tr><tr><td>DIP</td><td><em>Decision Intelligence Platforms</em></td></tr><tr><td>DMN</td><td><em>Decision Model and Notation</em> ; FEEL</td></tr><tr><td>DORA</td><td>règlement (UE) 2022/2554</td></tr><tr><td>E-23</td><td>ligne directrice du BSIF</td></tr><tr><td>FIPA</td><td><em>Foundation for Intelligent Physical Agents</em></td></tr><tr><td>GDA</td><td>décisions d’affaires</td></tr><tr><td>LLM</td><td>grand modèle de langue</td></tr><tr><td>OPA / OCPM</td><td><em>Open Policy Agent</em> ; fouille objets</td></tr><tr><td>GPA</td><td>processus d’affaires (BPM)</td></tr><tr><td>GPAI</td><td>IA à usage général</td></tr><tr><td>IETF / IESG / BoF</td><td>normalisation de l’Internet</td></tr><tr><td>ISO 20022</td><td>messages de paiement</td></tr><tr><td>JWS</td><td><em>JSON Web Signature</em></td></tr><tr><td>LIAD</td><td>Loi sur l’IA et les données</td></tr><tr><td>Lynx / RTR</td><td>paiements canadiens</td></tr><tr><td>MCP</td><td><em>Model Context Protocol</em></td></tr><tr><td>ML-DSA</td><td>signature post-quantique (FIPS 204)</td></tr><tr><td>NIST / ENISA</td><td>cybersécurité</td></tr><tr><td>OMG</td><td><em>Object Management Group</em></td></tr><tr><td>OWASP</td><td>sécurité applicative</td></tr><tr><td>OCEL</td><td><em>Object-Centric Event Log</em></td></tr><tr><td>OASF</td><td><em>Open Agentic Schema Framework</em></td></tr><tr><td>PDP / PEP</td><td>décision / application</td></tr><tr><td>RBA</td><td>robotisation des processus (RPA)</td></tr><tr><td>RFC</td><td><em>Request for Comments</em></td></tr><tr><td>SPIFFE / WIMSE</td><td>identité de charge de travail</td></tr><tr><td>TCK</td><td><em>Technology Compatibility Kit</em></td></tr><tr><td>W3C</td><td><em>World Wide Web Consortium</em></td></tr><tr><td>WORM</td><td><em>write once, read many</em></td></tr><tr><td>XES</td><td><em>eXtensible Event Stream</em></td></tr></tbody></table>',
     '<table><caption>Tableau\xa017.\xa0– Sigles employés dans cette veille (sélection ; les sigles des sections 1 à 8 non repris ici sont définis à leur première occurrence).</caption><thead><tr><th>Sigle</th><th>Signification</th></tr></thead><tbody><tr><td>A-BPMS</td><td><em>Agentic Business Process Management Systems</em></td></tr><tr><td>A2A</td><td><em>Agent2Agent Protocol</em></td></tr><tr><td>AAIF</td><td><em>Agentic AI Foundation</em> (Linux Foundation)</td></tr><tr><td>AARP / COAZ</td><td><em>Agent Authorization Request Profile</em> / <em>Context-Aware Authorization</em> (profils d’AuthZEN)</td></tr><tr><td>ACVM</td><td>Autorités canadiennes en valeurs mobilières</td></tr><tr><td>ADS</td><td>architecture détaillée de solution</td></tr><tr><td>AGNTCY</td><td>collectif d’infrastructure d’agents (Linux Foundation)</td></tr><tr><td>ANP</td><td><em>Agent Network Protocol</em></td></tr><tr><td>AP2 / ACP / UCP</td><td><em>Agent Payments Protocol</em> / <em>Agentic Commerce Protocol</em> / <em>Universal Commerce Protocol</em></td></tr><tr><td>APA</td><td><em>Agentic Process Automation</em></td></tr><tr><td>AuthZEN</td><td><em>Authorization API 1.0</em> (OpenID Foundation)</td></tr><tr><td>BOAT</td><td><em>Business Orchestration and Automation Technologies</em></td></tr><tr><td>BPMN</td><td><em>Business Process Model and Notation</em> (ISO/CEI 19510)</td></tr><tr><td>CMMN</td><td><em>Case Management Model and Notation</em></td></tr><tr><td>CNCF</td><td><em>Cloud Native Computing Foundation</em></td></tr><tr><td>CoSAI / CSA</td><td><em>Coalition for Secure AI</em> (OASIS) ; <em>Cloud Security Alliance</em></td></tr><tr><td>CUA</td><td><em>Computer-Using Agent</em></td></tr><tr><td>CVE / CNA</td><td><em>Common Vulnerabilities and Exposures</em> / <em>CVE Numbering Authority</em></td></tr><tr><td>DID / VC</td><td><em>Decentralized Identifiers</em> / <em>Verifiable Credentials</em> (W3C)</td></tr><tr><td>DIP</td><td><em>Decision Intelligence Platforms</em></td></tr><tr><td>DMN</td><td><em>Decision Model and Notation</em> ; FEEL (<em>Friendly Enough Expression Language</em>)</td></tr><tr><td>DORA</td><td><em>Digital Operational Resilience Act</em>, règlement (UE) 2022/2554</td></tr><tr><td>E-23</td><td>ligne directrice E-23 du BSIF (gestion du risque de modélisation)</td></tr><tr><td>FIPA</td><td><em>Foundation for Intelligent Physical Agents</em> (IEEE)</td></tr><tr><td>GDA</td><td>gestion des décisions d’affaires</td></tr><tr><td>GPA</td><td>gestion des processus d’affaires (<em>Business Process Management</em>, BPM)</td></tr><tr><td>GPAI</td><td><em>General-Purpose Artificial Intelligence</em> (IA à usage général)</td></tr><tr><td>IETF / IESG / BoF</td><td><em>Internet Engineering Task Force</em> / <em>Internet Engineering Steering Group</em> / <em>Birds of a Feather</em></td></tr><tr><td>ISO 20022</td><td>norme internationale de messages financiers</td></tr><tr><td>JWS</td><td><em>JSON Web Signature</em> (RFC 7515)</td></tr><tr><td>LIAD</td><td>Loi sur l’intelligence artificielle et les données (projet de loi C-27, Canada)</td></tr><tr><td>LLM</td><td><em>large language model</em> (grand modèle de langue)</td></tr><tr><td>LPRPSP</td><td>Loi sur la protection des renseignements personnels dans le secteur privé (Québec, RLRQ c. P-39.1)</td></tr><tr><td>Lynx / RTR</td><td>système de paiement de grande valeur / <em>Real-Time Rail</em> (Paiements Canada)</td></tr><tr><td>MCP</td><td><em>Model Context Protocol</em></td></tr><tr><td>ML-DSA</td><td><em>Module-Lattice-Based Digital Signature Algorithm</em> (FIPS 204)</td></tr><tr><td>NIST / ENISA</td><td><em>National Institute of Standards and Technology</em> / Agence de l’Union européenne pour la cybersécurité</td></tr><tr><td>OASF</td><td><em>Open Agentic Schema Framework</em></td></tr><tr><td>OCEL</td><td><em>Object-Centric Event Log</em></td></tr><tr><td>OMG</td><td><em>Object Management Group</em></td></tr><tr><td>OPA / OCPM</td><td><em>Open Policy Agent</em> ; <em>Object-Centric Process Mining</em> (fouille centrée objets)</td></tr><tr><td>OWASP</td><td><em>Open Worldwide Application Security Project</em></td></tr><tr><td>PDP / PEP</td><td><em>Policy Decision Point</em> / <em>Policy Enforcement Point</em></td></tr><tr><td>RBA</td><td>robotisation des processus d’affaires (<em>Robotic Process Automation</em>, RPA)</td></tr><tr><td>RFC</td><td><em>Request for Comments</em> (IETF)</td></tr><tr><td>SPIFFE / WIMSE</td><td><em>Secure Production Identity Framework for Everyone</em> / <em>Workload Identity in Multi System Environments</em></td></tr><tr><td>TCK</td><td><em>Technology Compatibility Kit</em></td></tr><tr><td>W3C</td><td><em>World Wide Web Consortium</em></td></tr><tr><td>WORM</td><td><em>write once, read many</em> (stockage non réinscriptible)</td></tr><tr><td>XES</td><td><em>eXtensible Event Stream</em> (IEEE 1849-2023)</td></tr></tbody></table>'),
    ('(QO 4)', '(question ouverte 4)'),
    # O-19, VT4-02, VT4-18, VT3-09, VT2-04, VT3-10, VT3-01, VT4-10 : Annexe traçabilité et Divulgation
    ('et le régime de la vérification elle-même.',
     'et le régime de la vérification elle-même (tableaux 19 à 24).'),
    ('Les dix énoncés réfutés de l’édition du 15 août 2026, chacun avec l’état antérieur, l’état courant, la source rouverte et l’extrait ou le fait qui a fait basculer. Trois d’entre eux sont des réfutations que la revue s’applique à elle-même, produites entre son premier et son second tour de vérification.',
     'Les onze énoncés réfutés de l’édition du 15 août 2026, chacun avec l’état antérieur, l’état courant, la source rouverte et l’extrait ou le fait qui a fait basculer. Quatre d’entre eux sont des réfutations que la veille s’applique à elle-même, produites entre son premier et son second tour de vérification.'),
    ('<td>date de finalisation du 7 avril 2026, champ d’application, contenu, entrée en vigueur du 1er mai 2027</td>',
     '<td>date de finalisation (avril 2026, document daté de mars ; le 7 avril est de source secondaire), champ d’application, contenu, entrée en vigueur du 1er mai 2027</td>'),
    ('<td>adresse au domaine nu, <strong>sans page cible</strong> ; page « nouveautés » servie dans un état arrêté au 30 juin 2026</td><td>préversion publique du 6 août 2026</td><td><strong>énoncé non rouvert</strong> ; réserve dans le corps</td>',
     '<td>adresse au domaine nu [301], <strong>sans page cible</strong> ; page « nouveautés » [155] rouverte le 15 août 2026 mais servie dans un état arrêté au 30 juin 2026</td><td>préversion publique du 6 août 2026</td><td><strong>énoncé de [301] non rouvert</strong> (page [155] rouverte sans mention de Dataverse) ; réserve dans le corps</td>'),
    ('94, 95, 110, 118, 122, 154',
     '94, 95 (hors dépôt GitHub), 110, 118, 122 (livre blanc ; salle de presse rouverte en §5.2), 154'),
    ('deux groupes chartés en portent vingt-sept de plus dans leur voisinage',
     'le groupe charté DAWN et la BoF DMSC en portent vingt-sept de plus dans leur voisinage'),
    ('<h3>Régime de la vérification</h3>',
     '<h3>Régime de la vérification</h3>\n<p>Le tableau 24 récapitule les cinq régimes de preuve qui coexistent dans l’édition du 15 août 2026.</p>'),
    ('<td>dix réfutations, sept désaccords, deux tours de rédaction et de vérification séparés</td>',
     '<td>onze réfutations (dont quatre du premier tour), sept désaccords, deux tours de rédaction et de vérification séparés</td>'),
    ('Les divergences entre corpus sont <strong>signalées et non arbitrées</strong> (8.4, 13.6).',
     'Les divergences entre corpus sont <strong>signalées et tranchées sur pièce</strong>, l’une en source primaire (AP2), l’autre hors passe (AMF, erratum 1) (8.4, 13.6).'),
    # VT6, VT7, O-20, O-21, § 10.8 : Références [1] à [342]
    ('<em>Plusieurs références renvoient à des pages vivantes — dépôts, notes de version, documentation en ligne — sans version datée stable : leur contenu peut avoir évolué depuis la date de consultation indiquée.</em>',
     '<em>Plusieurs références renvoient à des pages vivantes — dépôts, notes de version, documentation en ligne — sans version datée stable : leur contenu peut avoir évolué depuis la date de consultation indiquée. Sauf date de consultation propre indiquée à l’entrée, les sources web ont été consultées lors des passes de juillet et d’août 2026 et revérifiées au gel du 15 août 2026.</em>'),
    ('arXiv:2505.07176v2, mai 2025. https://arxiv.org/abs/2505.07176',
     'arXiv:2505.07176v2, mai 2025 (publié dans <em>IEEE Transactions on Cognitive Communications and Networking</em>, doi:10.1109/TCCN.2025.3623369). https://arxiv.org/abs/2505.07176'),
    ('arXiv:2602.11327v2, février 2026. https://arxiv.org/abs/2602.11327',
     'arXiv:2602.11327v2, février 2026 (publié dans <em>Journal of Information Security and Applications</em>, 2026, art. 104645, doi:10.1016/j.jisa.2026.104645). https://arxiv.org/abs/2602.11327'),
    ('arXiv:2511.02841v2, novembre 2025. https://arxiv.org/abs/2511.02841',
     'arXiv:2511.02841v2, octobre 2025 (déposé le 1er octobre 2025, v2 de novembre 2025 ; publié aux actes d’ICAART 2026). https://arxiv.org/abs/2511.02841'),
    ('doi:10.6028/NIST.AI.100-1</p></li>',
     'doi:10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1</p></li>'),
    ('Blogue d’ingénierie de Block, 2025. https://engineering.block.xyz/blog/blocks-playbook-for-designing-mcp-servers</p></li>',
     'Blogue d’ingénierie de Block, 21 avril 2025. https://engineering.block.xyz/blog/blocks-playbook-for-designing-mcp-servers (consulté le 12 juillet 2026).</p></li>'),
    ('Gaowei Chang, créateur d’ANP) : livre blanc',
     'Gaowei Chang, créateur d’ANP)\u202f: livre blanc'),
    ('et al.\xa0 ', 'et al. ', 2),
    ('arXiv:2512.00520v1, 29 novembre 2025 — <em>version consultée ; une</em> <strong><em>v2 est parue le 27 avril 2026</em></strong><em>, antérieure au gel de cette édition et non reprise ici. La revue de littérature compagnonne, elle, cite la v2 (sa notice 22).</em>',
     'arXiv:2512.00520v2, 29 novembre 2025 (v2 du 27 avril 2026 ; <em>la v1 avait été consultée initialement au gel, la v2 étant citée par la revue de littérature compagnon à sa notice 22</em>).'),
    ('<li><p>IETF. « AI Agent Authentication and Authorization » (modèle AIMS).',
     '<li><p>P. Kasselman, H. Tschofenig et D. R. Lopez. « AI Agent Authentication and Authorization » (modèle AIMS).'),
    ('dépôt de spécification : https://github.com/cloudevents/spec</p></li>',
     'dépôt de spécification : https://github.com/cloudevents/spec (consulté le 12 juillet 2026).</p></li>'),
    ('https://solace.com/what-is-an-event-mesh/</p></li>',
     'https://solace.com/what-is-an-event-mesh/ (consulté le 12 juillet 2026).</p></li>'),
    ('https://github.com/SolaceLabs/solace-agent-mesh ; https://solacelabs.github.io/solace-agent-mesh/</p></li>',
     'https://github.com/SolaceLabs/solace-agent-mesh (la documentation <code>solacelabs.github.io/solace-agent-mesh/</code> renvoyant HTTP 404 au 11 novembre 2026 ; consulté le 12 juillet 2026).</p></li>'),
    ('versée à la Linux Foundation ; kagent, exécutif d’agents natif de Kubernetes (Apache 2.0, MCP et A2A), projet de bac à sable de la CNCF, bâti par les fondateurs d’Istio. https://agentgateway.dev/ ; https://kagent.dev/ ; https://www.solo.io/press-releases/solo-io-launches-agent-gateway-and-introduces-agent-mesh ; https://aaif.io/blog/use-agentgateway-to-mediate-mcp-and-llm-traffic-at-solo-io/</p></li>',
     'versée à la Linux Foundation puis à l’AAIF le 4 juin 2026 [222], version v1.4.1 et branche principale active au 14 août 2026 ; kagent, exécutif d’agents natif de Kubernetes (Apache 2.0, MCP et A2A), projet de bac à sable de la CNCF, bâti par Solo.io. https://agentgateway.dev/ ; https://kagent.dev/ ; https://www.solo.io/press-releases/solo-io-launches-agent-gateway-and-introduces-agent-mesh ; https://aaif.io/blog/use-agentgateway-to-mediate-mcp-and-llm-traffic-at-solo-io/ (consulté le 15 août 2026).</p></li>'),
    ('(signature par les présidents du Parlement et du Conseil, 8 juillet 2026 ; publication au JO non constatée) : https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=celex:52025PC0836 (consulté le 12 juillet 2026).',
     'au 12 juillet 2026 (signature par les présidents du Parlement et du Conseil le 8 juillet 2026 ; parution au JO le 24 juillet 2026, voir [254]) : https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=celex:52025PC0836 (consulté les 12 juillet et 8 août 2026).'),
    ('« Frontier models and production agents: Advancing Microsoft Foundry for the agentic era ».',
     '« Frontier models and production agents: Advancing Microsoft Foundry for the agentic era » (page retitrée « GPT-5.6 now available in Microsoft Foundry: Frontier models, pricing, and production agents »).'),
    ('arXiv:2601.14567v1, 21 janvier 2026 — <em>version consultée ; une</em> <strong><em>v2 est parue le 13 juillet 2026</em></strong><em>, antérieure au gel de cette édition et non reprise ici. La revue de littérature compagnonne, elle, cite la v2 (sa notice 27).</em>',
     'arXiv:2601.14567v2, 21 janvier 2026 (v2 du 13 juillet 2026 ; <em>la v1 avait été consultée initialement au gel, la v2 étant citée par la revue de littérature compagnon à sa notice 27</em>).'),
    ('https://openid.github.io/authzen/authzen-mcp-profile-1_0.html (consulté le 13 juillet 2026).',
     'https://openid.github.io/authzen/authzen-mcp-profile-1_0.html (consulté les 13 juillet et 15 août 2026).'),
    ('30 avril 2026. https://cloudsecurityalliance.org/research/working-groups/autonomous-action-runtime-management-aarm',
     'don annoncé par Vanta le 30 avril 2026, au lendemain du communiqué de la CSAI Foundation [111]. https://cloudsecurityalliance.org/research/working-groups/autonomous-action-runtime-management-aarm'),
    ('« BoF requests » et pages de documents des groupes chartés',
     '« BoF requests » et pages de documents de DAWN et DMSC'),
    ('DAWN et DMSC chartés dans la foulée.',
     'DAWN charté dans la foulée ; DMSC resté à l’état de BoF (« BoF concluded » au registre le 8 octobre, voir [359]).'),
    ('11 mars 2026 (réponse au RFI NIST-2025-0035 :',
     'billet du 11 mars 2026 rendant publique la réponse déposée au RFI NIST-2025-0035 (clos le 9 mars [116]) :'),
    ('https://www.cncf.io/projects/serverless-workflow/ (consulté le 15 juillet 2026).',
     'https://serverlessworkflow.io/ (la fiche <code>cncf.io/projects/serverless-workflow/</code> renvoyant HTTP 404 au 11 novembre 2026 ; consulté le 15 juillet 2026).'),
    ('https://docs.camunda.io/docs/reference/announcements-release-notes/890/890-release-notes/ (consulté le 15 juillet 2026).',
     'https://docs.camunda.io/docs/reference/announcements-release-notes/890/890-release-notes/ (consulté les 15 juillet et 8 août 2026).'),
    ('arXiv:2504.03693v2, avril 2025 (v2, juillet 2025 ; accepté à Responsible BPM 2025).',
     'arXiv:2504.03693v2, mars 2025 (déposé le 23 mars 2025, v2 de juillet 2025 ; accepté à Responsible BPM 2025).'),
    ('https://microservices.io/patterns/data/transactional-outbox.html</p></li>',
     'https://microservices.io/patterns/data/transactional-outbox.html (consulté le 15 juillet 2026).</p></li>'),
    ('arXiv:2505.20127v2, mai 2025 (v2, juillet 2025).',
     'arXiv:2505.20127v2, mai 2025 (v2, juillet 2025 ; publié aux actes de PMAI 2025, CEUR Workshop Proceedings, vol. 4087).'),
    ('date de finalisation du 7 avril 2026 non reconfirmée en source primaire',
     'date de finalisation (avril 2026, document daté de mars ; le 7 avril n’est pas reconfirmé en source primaire)'),
    ('risque-lie-aux-tiers</p></li>',
     'risque-lie-aux-tiers (tentatives des 18 juillet, 8 août et 15 août 2026).</p></li>'),
    ('<li><p>Gouvernement du Québec. « Décision fondée exclusivement sur un traitement automatisé » — art. 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (en vigueur depuis le 22 septembre 2023 : information de la personne, observations auprès d’un membre du personnel, communication sur demande des renseignements et principaux facteurs de la décision). Audit du 8 août 2026 — l’adresse citée ne résout plus, et la page qu’elle visait traitait du secteur <em>public</em> (art. 65.2 de la <em>Loi sur l’accès</em>), non de l’article 12.1 du secteur privé. La disposition est citée ici d’après son texte ; <code>legisquebec.gouv.qc.ca</code> refuse la consultation automatisée (HTTP 403), de sorte qu’elle n’a pu être reconfirmée sur sa source officielle — même obstacle qu’aux sections 8.4 et 10.</p></li>',
     '<li><p>Gouvernement du Québec. « Loi sur la protection des renseignements personnels dans le secteur privé », RLRQ c. P-39.1, art. 12.1 (décision fondée exclusivement sur un traitement automatisé, en vigueur depuis le 22 septembre 2023 : information de la personne au plus tard au moment où l’entreprise l’informe de la décision ; possibilité de présenter ses observations à un membre du personnel en mesure de réviser la décision ; communication, sur demande, des renseignements personnels utilisés, des raisons et des principaux facteurs et paramètres ayant mené à la décision, et du droit de faire rectifier ces renseignements). Audit du 8 août 2026 — l’adresse initialement citée ne résolvait plus et visait le secteur <em>public</em> (art. 65.2 de la <em>Loi sur l’accès</em>) ; <code>legisquebec.gouv.qc.ca</code> refuse la consultation automatisée (HTTP 403), de sorte que le texte a été vérifié hors outillage automatisé (sections 8.4 et 10). https://www.legisquebec.gouv.qc.ca/fr/document/lc/P-39.1</p></li>'),
    ('<strong>Aucune fusionnée à cette date</strong>',
     '<strong>Aucune résolue ni fermée à cette date</strong>'),
    ('versions finales du 13 août 2024 — <strong>errata du 31 juillet 2026</strong> ; <em>le correctif du 23 février 2026 que cette entrée portait n’existe pas (audit du 8 août 2026)</em> — :',
     'versions finales du 13 août 2024 — <strong>note de planification d’errata du 31 juillet 2026</strong> (errata annoncés, non encore publiés ; <em>le correctif du 23 février 2026 que cette entrée portait initialement n’existe pas, audit du 8 août 2026</em>) — :'),
    ('<strong>Réserve —</strong> errata publiés après parution : note de planification du 17 novembre 2025 sur FIPS 203 ; pour FIPS 204, note de planification du 31 juillet 2026 annonçant des errata non encore publiés — et non un correctif paru. https://csrc.nist.gov/pubs/fips/204/final',
     '<strong>Réserve —</strong> notes de planification d’errata après parution : 17 novembre 2025 sur FIPS 203 ; pour FIPS 204, 31 juillet 2026 annonçant des errata non encore publiés — et non un correctif paru. https://csrc.nist.gov/pubs/fips/204/final (consulté le 15 août 2026).'),
    ('arXiv:2606.25876v1, juin 2026.',
     'arXiv:2606.25876v1, juin 2026 (v2 déposée le 2 septembre 2026, après le gel : annexe de novembre).'),
    ('(Agentic AI Foundation /Anthropic)', '(Agentic AI Foundation / Anthropic)'),
    ('https://blog.modelcontextprotocol.io/posts/2026-07-28/</p></li>',
     'Consulté le 15 août 2026. https://blog.modelcontextprotocol.io/posts/2026-07-28/</p></li>'),
    ('https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=OJ:L_202601744</p></li>',
     'Consulté le 15 août 2026. https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=OJ:L_202601744</p></li>'),
    ('distinct de l’initiative de normalisation des agents du 17 février 2026 [61]. https://csrc.nist.gov/Projects/cosais/use-cases</p></li>',
     'distinct de l’initiative de normalisation des agents du 17 février 2026 [61] (la page du CSRC intitule depuis le projet « SP 800-53 Control Overlays for Super Intelligence Systems », COSIS : annexe de novembre). Consulté le 15 août 2026. https://csrc.nist.gov/Projects/cosais/use-cases</p></li>'),
    ('<strong>Réserve —</strong> l’entrée en vigueur du règlement d’exploitation et des règles au <strong>24 août 2026</strong>, ainsi que l’approbation du cadre juridique par le ministre fédéral des Finances, sont rapportées par des comptes rendus secondaires et <strong>ne figurent pas</strong> sur cette page primaire.',
     '<strong>Réserve —</strong> l’entrée en vigueur du règlement d’exploitation et des règles au <strong>24 août 2026</strong> ne figure pas sur cette page du système ; elle est établie en source primaire par le communiqué de Paiements Canada du 30 juin 2026 [430] et par le DORS/2026-133 [281] (annexe de novembre, erratum 3).'),
    ('https://blog.modelcontextprotocol.io/</p></li>',
     'https://blog.modelcontextprotocol.io/ (consulté le 15 août 2026).</p></li>'),
    ('https://claude.com/blog</p></li>',
     'https://claude.com/blog (consulté le 15 août 2026).</p></li>'),
    ('https://investors.block.xyz/financials/quarterly-results/</p></li>',
     'https://investors.block.xyz/financials/quarterly-results/ (consulté le 15 août 2026).</p></li>'),
    ('<li><p>Audit dynamique de 414 serveurs MCP publics — 68 vulnérabilités relevées (injection SQL, falsification de requête côté serveur vers les métadonnées d’infonuagique, traversée de chemin) ; 91,8 % des serveurs sans authentification OAuth. arXiv:2608.00150, 31 juillet 2026. https://arxiv.org/abs/2608.00150</p></li>',
     '<li><p>N. Padilla. « Exposed by Design: A Dynamic Security Assessment of Internet-Facing MCP Servers at Scale ». arXiv:2608.00150v1, 31 juillet 2026 — audit dynamique de 414 serveurs MCP publics : 68 vulnérabilités relevées (injection SQL, falsification de requête côté serveur vers les métadonnées d’infonuagique, traversée de chemin) ; 91,8 % des serveurs sans authentification OAuth (consulté le 15 août 2026). https://arxiv.org/abs/2608.00150</p></li>'),
    ('Préimpression non révisée par les pairs. https://arxiv.org/abs/2607.27080</p></li>',
     'Prépublication non révisée par les pairs (consulté le 15 août 2026). https://arxiv.org/abs/2607.27080</p></li>'),
    ('définition de l’IA agentique, risques de chaînage d’outils et d’accès surprivilégié, moindre privilège et points d’approbation. 13 juillet 2026. https://www.osfi-bsif.gc.ca</p></li>',
     'définition de l’IA agentique reprise de la directive conjointe des <em>Five Eyes</em> [341], risques de chaînage d’outils et d’accès surprivilégié, moindre privilège et points d’approbation. 13 juillet 2026. https://www.osfi-bsif.gc.ca (consulté le 15 août 2026).</p></li>'),
    ('https://www.idc.com/getdoc.jsp?containerId=prUS53765225</p></li>',
     'https://www.idc.com/getdoc.jsp?containerId=prUS53765225 (consulté le 15 août 2026).</p></li>'),
    ('<li><p>Internet-Draft draft-helixar-hdp-agentic-delegation-01 (soumission individuelle), 3 août 2026 — chaîne de sauts de délégation signée Ed25519, vérifiable hors ligne. Brouillon individuel, non adopté par un groupe de travail. https://datatracker.ietf.org/doc/draft-helixar-hdp-agentic-delegation/</p></li>',
     '<li><p>Helixar. « Human Delegation Provenance Protocol (HDP): Cryptographic Chain-of-Custody for Agentic AI Systems ». Internet-Draft draft-helixar-hdp-agentic-delegation-01 (soumission individuelle), 3 août 2026 — chaîne de sauts de délégation signée Ed25519, vérifiable hors ligne. Brouillon individuel, non adopté par un groupe de travail. https://datatracker.ietf.org/doc/draft-helixar-hdp-agentic-delegation/ (consulté le 15 août 2026).</p></li>'),
    ('<li><p>Internet-Draft draft-reece-wimse-cross-org-delegation-01 (soumission individuelle), 30 juillet 2026 — énoncé du problème de la délégation récursive entre organisations. Brouillon individuel, non adopté par un groupe de travail. https://datatracker.ietf.org/doc/draft-reece-wimse-cross-org-delegation/</p></li>',
     '<li><p>C. Reece <em>et al.</em> « Cross-Organizational Delegation for Workload and Agent Identity: Problem Statement and Requirements ». Internet-Draft draft-reece-wimse-cross-org-delegation-01 (soumission individuelle), 30 juillet 2026 — énoncé du problème de la délégation récursive entre organisations. Brouillon individuel, non adopté par un groupe de travail. https://datatracker.ietf.org/doc/draft-reece-wimse-cross-org-delegation/ (consulté le 15 août 2026).</p></li>'),
    ('https://digital-strategy.ec.europa.eu/en/faqs/ai-act-article-50-transparency-obligations</p></li>',
     'https://digital-strategy.ec.europa.eu/en/faqs/ai-act-article-50-transparency-obligations (consulté le 15 août 2026).</p></li>'),
    ('https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai</p></li>',
     'https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (consulté le 15 août 2026).</p></li>'),
    ('https://ec.europa.eu/commission/presscorner/</p></li>',
     'https://ec.europa.eu/commission/presscorner/ (consulté le 15 août 2026).</p></li>'),
    ('https://gazette.gc.ca/rp-pr/p2/2026/2026-07-01/html/sor-dors133-fra.html</p></li>',
     'https://gazette.gc.ca/rp-pr/p2/2026/2026-07-01/html/sor-dors133-fra.html (consulté le 15 août 2026).</p></li>'),
    ('https://x402.foundation/</p></li>',
     'https://x402.foundation/ (tentative de réouverture le 15 août 2026).</p></li>'),
    ('https://github.com/x402-foundation/x402</p></li>',
     'https://github.com/x402-foundation/x402 (consulté le 15 août 2026).</p></li>'),
    ('https://github.com/open-telemetry/semantic-conventions-genai/blob/8c1b98a/docs/registry/attributes/gen-ai.md</p></li>',
     'https://github.com/open-telemetry/semantic-conventions-genai/blob/8c1b98a/docs/registry/attributes/gen-ai.md (consulté le 15 août 2026).</p></li>'),
    ('https://github.com/open-telemetry/semantic-conventions-genai/blob/3cfb9e6/docs/registry/attributes/gen-ai.md</p></li>',
     'https://github.com/open-telemetry/semantic-conventions-genai/blob/3cfb9e6/docs/registry/attributes/gen-ai.md (consulté le 15 août 2026).</p></li>'),
    ('https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.44.0</p></li>',
     'https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.44.0 (consulté le 15 août 2026).</p></li>'),
    ('https://github.com/Arize-ai/openinference/releases</p></li>',
     'https://github.com/Arize-ai/openinference/releases (consulté le 15 août 2026).</p></li>'),
    ('https://aws.amazon.com/about-aws/whats-new/</p></li>',
     'https://aws.amazon.com/about-aws/whats-new/ (consulté le 15 août 2026).</p></li>'),
    ('connecteur <em>MCP Client</em> en disponibilité générale en 8.9 — <em>statut non énoncé par les notes de version, attesté seulement par la sortie du connecteur de l’arbre <code>/early-access/alpha/</code></em>, connecteurs',
     'connecteur <em>MCP Client</em> sans disponibilité générale énoncée en 8.9 (attesté seulement par la sortie du connecteur de l’arbre <code>/early-access/alpha/</code> [329]), connecteurs'),
    ('<li><p>Pegasystems. Communiqué du 14 juillet 2026 — Infinity 26 <strong>disponible</strong>, conception et exécution MCP comprises. https://www.pega.com/about/news/press-releases</p></li>',
     '<li><p>Pega. Communiqué du 14 juillet 2026 — Infinity 26 <strong>disponible</strong>, conception et exécution MCP comprises. https://www.pega.com/about/news/press-releases (consulté le 15 août 2026).</p></li>'),
    ('https://docs.temporal.io/cloud/release-notes</p></li>',
     'https://docs.temporal.io/cloud/release-notes (consulté le 15 août 2026).</p></li>'),
    ('https://github.com/restatedev/restate/releases/tag/v1.7.3</p></li>',
     'https://github.com/restatedev/restate/releases/tag/v1.7.3 (consulté le 15 août 2026).</p></li>'),
    ('<li><p>W3C. Note <em>Verifiable Credentials Overview</em> v1.0 (30 juillet 2026) ; <em>Recognized Entities</em> v1.0 (2 août 2026) ; <em>VC Barcodes</em> v1.0 et <em>DID Resolution</em> v1 au stade <em>Candidate Standard</em> (6 août 2026). https://www.w3.org/TR/did-resolution/</p></li>',
     '<li><p>W3C. Note <em>Verifiable Credentials Overview</em> v1.0 (30 juillet 2026 ; v1.1 le 10 août [324]) ; <em>Recognized Entities</em> v1.0 (première publication le 2 août 2026, republiée le 11 août [324]) ; <em>VC Barcodes</em> v1.0 et <em>DID Resolution</em> v1 (6 août 2026 ; voir la réserve de [324] sur les étiquettes d’index de <code>/TR</code>). https://www.w3.org/TR/did-resolution/ (consulté le 15 août 2026).</p></li>'),
    ('https://openid.net/wg/authzen</p></li>',
     'https://openid.net/wg/authzen (consulté le 15 août 2026).</p></li>'),
    ('https://openid.net/certification/</p></li>',
     'https://openid.net/certification/ (consulté le 15 août 2026).</p></li>'),
    ('https://github.com/spiffe/spiffe</p></li>',
     'https://github.com/spiffe/spiffe (consulté le 15 août 2026).</p></li>'),
    ('https://learn.microsoft.com</p></li>',
     'https://learn.microsoft.com (consulté le 8 août 2026).</p></li>'),
    ('https://developers.googleblog.com/</p></li>',
     'https://developers.googleblog.com/ (consulté le 15 août 2026).</p></li>'),
    ('https://www.gartner.com/en/newsroom</p></li>',
     'https://www.gartner.com/en/newsroom (consulté le 15 août 2026).</p></li>'),
    ('Aucune modification de <code>specification.md</code> ni de <code>a2a.proto</code>',
     'Aucune modification normative de <code>specification.md</code> ni aucune modification de <code>a2a.proto</code>'),
    ('extension du modèle d’identité de charge de travail SPIFFE (RFC 9542)',
     'extension du modèle d’identité de charge de travail SPIFFE (spécification CNCF ; le brouillon mentionne par erreur la RFC 9542, qui porte sur les paramètres IEEE 802)'),
    ('réponse chiffrant agents directs, agents en cascade et jetons révoqués',
     'réponse dénombrant les agents directs, les agents en cascade et les jetons révoqués'),
    ('<em>L’adresse citée en [294] ne résout plus (HTTP 404) au 15 août 2026 ; la page a été consultée à son adresse mensuelle.</em>',
     '<em>L’index générique <code>…/release-notes</code> cité au gel en [294] ne menait plus au mois visé au 15 août 2026 (UiPath y substituant une page de repli ; adresse remplacée par l’URL mensuelle en [294]) ; la page d’août a été consultée à son adresse mensuelle.</em>'),
    ('https://github.com/open-telemetry/semantic-conventions-genai/commit/8d3e4a0</p></li>',
     'https://github.com/open-telemetry/semantic-conventions-genai/commit/8d3e4a0 (consulté le 15 août 2026).</p></li>'),
    ('https://arize.com/blog/arize-ax-opentelemetry-genai-semantic-conventions/</p></li>',
     'https://arize.com/blog/arize-ax-opentelemetry-genai-semantic-conventions/ (consulté le 15 août 2026).</p></li>'),
    ('https://aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview</p></li>',
     'https://aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview (consulté le 15 août 2026).</p></li>'),
    ('reproduit verbatim au corps, section 8.5, et non répété ici',
     'reproduit verbatim au corps, section 8.1, et non répété ici'),
    ('<li><p>OpenAI. « Hugging Face model evaluation security incident ». Divulgation du fournisseur, <strong>21 juillet 2026</strong> —',
     '<li><p>OpenAI. « OpenAI and Hugging Face partner to address security incident during model evaluation » (slug <code>hugging-face-model-evaluation-security-incident</code>). Divulgation du fournisseur, <strong>21 juillet 2026</strong> —'),
    ('l’existence, la date et l’attribution sont établies par le communiqué primaire de la CSA du 28 juillet 2026 [337], qui date nommément la divulgation, et par convergence de comptes rendus secondaires.',
     'l’existence, la date et l’attribution sont établies au gel par le communiqué primaire de la CSA du 28 juillet 2026 [337], qui date nommément la divulgation, les éléments détaillés (GPT-5.6 Sol, ExploitGym, « unprecedented ») provenant de comptes rendus secondaires convergents au 15 août avant confirmation par le rapport technique du 26 août [424] lu en novembre.'),
    # Annexe du 29 octobre : Tableau 25 (appels [n]), prose, Tableau 26, Références [343]..[371]
    ('<td>343</td>', '<td>[343]</td>'),
    ('<td>344, 345</td>', '<td>[344, 345]</td>'),
    ('<td>346</td>', '<td>[346]</td>'),
    ('<td>347</td>', '<td>[347]</td>'),
    ('<td>348</td>', '<td>[348]</td>'),
    ('<td>349</td>', '<td>[349]</td>'),
    ('<td>351</td>', '<td>[351]</td>'),
    ('<td>119, 130</td>', '<td>[119, 130]</td>'),
    ('<td>352</td>', '<td>[352]</td>'),
    ('<td>353</td>', '<td>[353]</td>'),
    ('<td>354</td>', '<td>[354]</td>'),
    ('<td>355</td>', '<td>[355]</td>'),
    ('<td>356, 359</td>', '<td>[356, 359]</td>'),
    ('<td>357, 358</td>', '<td>[357, 358]</td>'),
    ('<td>360</td>', '<td>[360]</td>'),
    ('<td>361</td>', '<td>[361]</td>'),
    ('<td>362, 363</td>', '<td>[362, 363]</td>'),
    ('<td>364, 365</td>', '<td>[364, 365]</td>'),
    ('<td>366</td>', '<td>[366]</td>'),
    ('<td>367, 368, 369</td>', '<td>[367, 368, 369]</td>'),
    ('<td>370</td>', '<td>[370]</td>'),
    ('les douze brouillons qui signent en Ed25519 ou en EdDSA emploient un algorithme',
     'les brouillons de la section 7.7 qui signent en EdDSA (Ed25519 compris) emploient un algorithme'),
    ('« Corps » : corrigé à sa place ; « annexe » : corrigé ici seulement.',
     '« corps » : corrigé à sa place ; « corps ; annexe » : détaillé ici et reporté au corps lors des relectures de novembre (tableau 31).'),
    ('QO 2', 'question ouverte 2'),
    ('<td>annexe</td>', '<td>corps ; annexe</td>', 4),
    # VT5-15 : Références [343] à [371], dates de consultation et liens OASF / DAWN
    (' <a href="https://github.com/agntcy/dir/releases">https://github.com/agntcy/dir/releases</a>',
     ' Consulté le 29 octobre 2026. <a href="https://github.com/agntcy/oasf/tags">https://github.com/agntcy/oasf/tags</a> ; <a href="https://github.com/agntcy/dir/releases">https://github.com/agntcy/dir/releases</a>'),
    (' <a href="https://datatracker.ietf.org/group/dmsc/about/">https://datatracker.ietf.org/group/dmsc/about/</a>',
     ' Consulté le 29 octobre 2026. <a href="https://datatracker.ietf.org/group/dawn/about/">https://datatracker.ietf.org/group/dawn/about/</a> ; <a href="https://datatracker.ietf.org/group/dmsc/about/">https://datatracker.ietf.org/group/dmsc/about/</a>'),
    ('<code>docs/community/working-groups/tasks-events.mdx</code>. <a href="https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3440">',
     '<code>docs/community/working-groups/tasks-events.mdx</code>. Consulté le 29 octobre 2026. <a href="https://github.com/modelcontextprotocol/modelcontextprotocol/pull/3440">'),
    ('2026). <a href="https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/seps">',
     '2026). Consulté le 29 octobre 2026. <a href="https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/seps">'),
    ('2026. <a href="https://github.com/modelcontextprotocol/registry/releases">',
     '2026. Consulté le 29 octobre 2026. <a href="https://github.com/modelcontextprotocol/registry/releases">'),
    ('2026. <a href="https://github.com/modelcontextprotocol/conformance/commits/main">',
     '2026. Consulté le 29 octobre 2026. <a href="https://github.com/modelcontextprotocol/conformance/commits/main">'),
    ('dev-1.1. <a href="https://github.com/a2aproject/A2A/compare/v1.0.1...v1.1.0-rc">',
     'dev-1.1. Consulté le 29 octobre 2026. <a href="https://github.com/a2aproject/A2A/compare/v1.0.1...v1.1.0-rc">'),
    ('2026. <a href="https://github.com/a2aproject/a2a-tck/pulls">',
     '2026. Consulté le 29 octobre 2026. <a href="https://github.com/a2aproject/a2a-tck/pulls">'),
    ('(texte). <a href="https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards">',
     '(texte). Consulté le 29 octobre 2026. <a href="https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards">'),
    ('2026). <a href="https://github.com/agent-network-protocol/AgentNetworkProtocol/releases">',
     '2026). Consulté le 29 octobre 2026. <a href="https://github.com/agent-network-protocol/AgentNetworkProtocol/releases">'),
    ('2026. <a href="https://github.com/Universal-Commerce-Protocol/ucp/releases/tag/v2026-08-25">',
     '2026. Consulté le 29 octobre 2026. <a href="https://github.com/Universal-Commerce-Protocol/ucp/releases/tag/v2026-08-25">'),
    ('2026). <a href="https://github.com/x402-foundation/x402/security/advisories">',
     '2026). Consulté le 29 octobre 2026. <a href="https://github.com/x402-foundation/x402/security/advisories">'),
    ('#350. <a href="https://github.com/open-telemetry/semantic-conventions-genai">',
     '#350. Consulté le 29 octobre 2026. <a href="https://github.com/open-telemetry/semantic-conventions-genai">'),
    ('Informational. <a href="https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/">',
     'Informational. Consulté le 29 octobre 2026. <a href="https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/">'),
    ('arch-08. <a href="https://datatracker.ietf.org/wg/wimse/documents/">',
     'arch-08. Consulté le 29 octobre 2026. <a href="https://datatracker.ietf.org/wg/wimse/documents/">'),
    ('2026). <a href="https://datatracker.ietf.org/wg/oauth/documents/">',
     '2026). Consulté le 29 octobre 2026. <a href="https://datatracker.ietf.org/wg/oauth/documents/">'),
    ('expirés. <a href="https://datatracker.ietf.org/doc/draft-chen-oauth-agent-revocation/">',
     'expirés. Consulté le 29 octobre 2026. <a href="https://datatracker.ietf.org/doc/draft-chen-oauth-agent-revocation/">'),
    ('NIST.IR.8547. <a href="https://csrc.nist.gov/pubs/ir/8547/final">',
     'NIST.IR.8547. Consulté le 29 octobre 2026. <a href="https://csrc.nist.gov/pubs/ir/8547/final">'),
    ('2026. <a href="https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai">',
     '2026. Consultée le 29 octobre 2026. <a href="https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai">'),
    ('outillage. <a href="https://www.orrick.com/en/Insights/2026/10/First-Harmonised-Technical-Standard-Published-Under-the-EU-AI-Act">',
     'outillage. Consulté le 29 octobre 2026. <a href="https://www.orrick.com/en/Insights/2026/10/First-Harmonised-Technical-Standard-Published-Under-the-EU-AI-Act">'),
    ('ultérieure. <a href="https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027">',
     'ultérieure. Consultée le 29 octobre 2026. <a href="https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027">'),
    ('2026. <a href="https://www.parl.ca/legisinfo/en/bill/45-1/c-36">',
     '2026. Consulté le 29 octobre 2026. <a href="https://www.parl.ca/legisinfo/en/bill/45-1/c-36">'),
    ('2026. <a href="https://docs.camunda.io/docs/reference/announcements-release-notes/overview/">',
     '2026. Consulté le 29 octobre 2026. <a href="https://docs.camunda.io/docs/reference/announcements-release-notes/overview/">'),
    ('2026 ». <a href="https://openid.net/authorization-api-1-0-final-specification-approved/">',
     '2026 ». Consulté le 29 octobre 2026. <a href="https://openid.net/authorization-api-1-0-final-specification-approved/">'),
    # VT1-19, VT2-21, VT3-24, VT4-25 : remplacement de « revue » par « veille » lorsqu'elle se désigne elle-même
    ('<h3>2.1 Protocole de revue</h3>', '<h3>2.1 Protocole de veille</h3>'),
    ('<p>La revue a été ouverte le 2 juillet 2026', '<p>La veille a été ouverte le 2 juillet 2026'),
    ('<td>Revue initiale, cinq angles</td>', '<td>Veille initiale, cinq angles</td>'),
    ('<h2>10 Limites de cette revue</h2>', '<h2>10 Limites de cette veille</h2>'),
    ('<h3>13.7 Ce que le corpus prête à la revue, et ce que la revue lui renvoie</h3>',
     '<h3>13.7 Ce que le corpus prête à la veille, et ce que la veille lui renvoie</h3>'),
    ('<h3>13.9 Ce que le corpus arrêté renvoie à la revue</h3>',
     '<h3>13.9 Ce que le corpus arrêté renvoie à la veille</h3>'),
    ('l’opposition que corpus et revue construisaient', 'l’opposition que corpus et veille construisaient'),
    ('la revue des méthodologies', 'la SYNTHESE_METHODOLOGIES_KEEP'),
    ('la revue de littérature compagnon', 'la REVUE_LITTERATURE_KEEP', 2),
    ('Cette revue ', 'Cette veille ', 2),
    ('cette revue', 'cette veille', 18),
    ('présente revue', 'présente veille', 4),
    ('La revue ', 'La veille ', 4),
    ('la revue', 'la veille', 27),
    ('la SYNTHESE_METHODOLOGIES_KEEP', 'la revue des méthodologies'),
    ('la REVUE_LITTERATURE_KEEP', 'la revue de littérature compagnon', 2),
]


def corriger(s):
    for c in CORRECTIONS + CORRECTIONS_AUDIT:
        ancien, nouveau, *n = c
        attendu = n[0] if n else 1
        k = s.count(ancien)
        assert k > 0 if attendu is None else k == attendu, f'correction : passage trouvé {k} fois (attendu {attendu}) : {ancien[:80]}'
        s = s.replace(ancien, nouveau)
    return s
