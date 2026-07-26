# TOC — Table des matières commentée du Volume IV (compendium intégral)

| Champ                                       | Valeur                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Version                                     | **0.18 — reformatage markdown : les tables détaillées passent en titres** (26 juill. 2026). Passe de **forme**, sans objet éditorial : **aucun chapitre, aucun livre, aucune enveloppe, aucune thèse, aucune ligne Fusion, aucun renvoi de provenance** — 57 chapitres, dix livres I-X, fourchette ≈ 369 000–394 000 mots strictement inchangés. Les **309 entrées de section** des 57 tables détaillées, jusque-là des puces en gras, deviennent des **titres markdown `####`**, enfants directs du `### Chapitre N` : le plan du fichier expose désormais la hiérarchie **livre → chapitre → section** dans tout afficheur de plan — éditeur, forge, table des matières Pandoc —, ce que des puces ne permettaient pas. Trois gestes mécaniques l'accompagnent : la glose qui suivait le titre passe en **paragraphe** (257 cas, le séparateur « — » devenant redondant), les **sous-sections** restent en liste, dés-indentées d'un niveau (230 cas), et l'en-tête « Table des matières détaillée du chapitre N » devient un **paragraphe gras** — même forme que « Table de couverture (décision 6) » — pour ne pas s'interposer entre le chapitre et ses sections. ⚠ **Aucun mot n'est ajouté, retiré ni déplacé**, et la passe le prouve plutôt que de l'affirmer : comparaison du flux de mots avant/après, **72 764 mots, séquence identique**. Un seul titre est normalisé — celui du § 36.4, dont le gras imbriqué est irrécupérable par découpe : l'emphase y passe en italique, forme employée partout ailleurs dans le fichier. ⚠ **Ce que la passe ne fait pas** : elle ne touche ni le bandeau, ni les décisions, ni les annexes, ni les journaux gelés, et n'ajoute **aucun index de tête** — un index serait un cardinal de plus à tenir à jour (risque 1), alors que les titres se dérivent d'eux-mêmes. `check-toc.py` (C1-C14, sortie 0) constaté avant et après. Détail au journal v0.18 |
| Historique v0.17                            | **0.17 — révision de finalisation : les écarts de la v0.16 sont résolus** (25 juill. 2026). Passe de **résolution**, non d'ajout : **aucun chapitre, aucun livre, aucune enveloppe, aucune thèse** — 57 chapitres, dix livres I-X, fourchette ≈ 369 000–394 000 mots strictement inchangés. Elle solde les écarts que la v0.16 avait relevés sans les arbitrer, chacun par la règle que le fichier porte déjà, **jamais par un choix de contenu neuf**. **Le plus lourd — une source vide — est corrigé par la décision 8** (*le plan s'aligne sur le chapitre rédigé*) : le « volet RGPD » que les ch. 31 et 34 se partageaient n'existe plus au ch. 20 du Vol. III, retiré le 22 juillet 2026 par l'arbitrage **R-G-38** ; le ch. 31 reçoit ce chapitre **en entier**, le ch. 34 garde sa matière RGPD par le **Vol. I** (§4.8.4, §5.3) qui est intact, et la **lacune 16 du Vol. III entre au registre de l'Annexe C** — dans une **seconde table**, distincte des onze du Vol. II, mélanger les séries périmant un cardinal contrôlé. **Trois doubles revendications tranchées par partage déclaré** (ACP entre ch. 8 et ch. 10 ; §3.4 du Vol. II, siège au ch. 7 ; §7.4 du Vol. III, « hors §7.4 » porté au ch. 16). **Cinq listes de sections réalignées** sur leur ligne Fusion (§1.2 et « exécution durable » au ch. 1 ; §2.8.5 au ch. 4 ; menace et vecteurs au ch. 6 ; ANP au ch. 8). **Un renvoi nommé** (« PRDPlan §4.4 » → « PRDPlan Vol. II §4.4 », décision 7) et **une section sans source marquée construction d'auteur** (ch. 28, décision 8). ⚠ **Les risques 13, 14 et 15 ne sont pas touchés** : ils portent sur du **contenu manquant**, dont l'arbitrage est une décision d'auteur (D-7 du PRD) — une passe de cohérence ne comble pas un angle mort. `check-toc.py` (C1-C14, sortie 0) et 955 renvois de provenance vérifiés. Détail au journal v0.17 |
| Historique v0.16                            | **0.16 — les tables des matières détaillées : le plan déplié chapitre par chapitre** (25 juill. 2026). Passe d'expansion, non de restructuration : **aucun chapitre, aucun livre, aucune enveloppe, aucune thèse, aucune ligne Fusion ne bouge** — 57 chapitres, dix livres I-X, fourchette ≈ 369 000–394 000 mots strictement inchangés. Elle ajoute, sous chaque entrée de chapitre, une **table des matières détaillée dérivée du texte rédigé des sources** — Vol. I *Monographie* ch. 1-7 et Annexe B, Vol. II *Monographie* ch. 1-24 et Annexe B, Vol. III *Monographie* ch. 1-28 et Annexe B — où chaque sous-section porte sa provenance et chaque chapitre sa **table de couverture** (décision 6). Les **57 chapitres** en sont pourvus. ⚠ **Ces tables sont subordonnées** : en cas d'écart, la ligne Fusion prime — elles la déplient, elles ne la re-décident pas (décision 8). ⚠ **Les ch. 52-54 n'ont aucune provenance externe, et c'est un fait, non un manque** : « Fusion : aucune » (décision 9) — appuis internes seuls, tout énoncé au mieux repérage [C]. **Treize écarts relevés et non arbitrés**, dont une **source vide** (le « volet RGPD » du ch. 20 du Vol. III, retiré de la source le 22 juill. 2026 par l'arbitrage R-G-38 — ch. 34) et une **collision de renvoi** (un « PRDPlan §N » nu est indécidable entre les PRDPlan des Vol. II et III). **Trois défauts introduits par la passe elle-même ont été détectés par `check-toc.py` et corrigés** : deux « R-5 » nus au ch. 36, devenus indécidables parce que la table y introduisait une mention du Vol. III, et un « R-8 » nu au ch. 47. `check-toc.py` (C1-C14, sortie 0) constaté après correction ; 955 renvois de section vérifiés contre les sources, aucun pendant. Détail au journal v0.16 |
| Historique v0.15                            | **0.15 — la coordination sous défaillance : un second angle mort déclaré** (24 juill. 2026). Passe de déclaration, du genre de la v0.10 : **aucun chapitre, aucun livre, aucune enveloppe ne bouge**. Elle consomme un audit de couverture externe daté du 24 juillet 2026 (`audit.md`, à la racine du dossier — un rapport sans autorité, ni source ni décision), dont un seul constat résiste à la vérification : le plan décrit la communication entre agents (Livre II, ch. 41-42) et les effets d'une action isolée (ch. 54), mais **nulle part l'accord entre agents sous asynchronie et défaillance partielle** — partitions, division du plan de contrôle, pair vivant qui répond faux. Mesure du 24 juillet 2026 sur la **zone des chapitres** (de `### Chapitre 1` à `# Annexes`) : zéro occurrence de « consensus », « byzantin », « quorum », « BFT », « split-brain » ; une seule de « sagas », au ch. 54, au grain d'une action unique. ⚠ **La zone est la bonne unité de mesure, pas le fichier** : depuis cette passe, ces termes figurent dans la *déclaration* elle-même — bandeau, risque 15, journal v0.15 —, et une mesure sur le fichier entier ne distinguerait plus l'objet décrit de son constat d'absence. Le constat est **déclaré au risque 15, non comblé** — l'arbitrage est une décision d'auteur (D-7 du PRD), comme pour le risque 14. Les autres constats de l'audit sont soit déjà portés par le plan (risques 11, 13, 14 ; portes G-1 et G-3 à G-6 du PRD), soit fautifs — ancrages de ligne périmés, risque mal numéroté, recommandation déjà planifiée — et corrigés dans le rapport lui-même. `check-toc.py` (C1-C14, sortie 0) constaté avant et après édition. Détail au journal v0.15 |
| Historique v0.14                            | **0.14 — collation d'appui structurelle contre les trois monographies rédigées** (23 juill. 2026). Passe de collation, non d'ajout : elle confronte la **carte des chapitres du plan** au **texte rédigé** des trois volumes sources — Vol. I (7 chapitres, Conclusion, ADS en Annexe B), Vol. II (24 chapitres, 7 parties), Vol. III (28 chapitres, 9 parties), ce dernier collationné pour la première fois contre sa monographie et non contre son plan. **Bilan structurel : sain.** Couverture complète — chaque chapitre des trois volumes est affecté à un chapitre d'arrivée, aucun abandon silencieux ; et les **onze renvois de section au Vol. III** (le seul volume dont le plan précédait le texte) résolvent tous contre sa monographie rédigée, à numérotation et titre concordants (§6.3, §7.4, §9.3, §18.2, §19.1, §19.3, §20.2, §27.2, §10.3, §28.6). ⚠ **Ce que cette passe ne fait pas** : la **collation de fond** — confrontation adversariale de chaque glose et de chaque thèse au texte rédigé, l'homologue de la v0.6 pour les Vol. I-II — reste le préalable déclaré aux Livres III et VII (porte G-4 du PRD, risque 11) ; cette passe n'en lève que le volet **structurel** (couverture et résolution des renvois), pas le volet de fond. **Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes et fourchette ≈ 369 000–394 000 mots intactes. `check-toc.py` (C1-C14, sortie 0) exécuté avant et après ; harnais de mutation rejoué après réancrage de M14 (le conspectus passe à v0.14). Détail au journal v0.14 |
| Historique v0.13                            | **0.13 — collation d'état contre le Vol. III rédigé : la filiation change de régime** (23 juill. 2026). Passe de faits de dépôt, du genre de la v0.12 — constats pris sur pièces dans les en-têtes du PRD v1.3, du TOC v0.8 et du CLAUDE.md du Vol. III, non relèves externes. **Le Vol. III n'est plus une proposition : il est rédigé** — 34 pièces sur 34 au statut « Rédigé et relu adversarialement » (22 juill. 2026), socle propre **F-01…F-98** plus 33 entrées héritées H-01…H-33, 15 lots d'instruction clos, gel des pièces au 21 juillet 2026, volumétrie mesurée **160 427 mots** (contre 102 500 planifiés), rendu FESP de 428 p. le 23 juillet 2026 ; ⚠ son propre cadrage impose « **rédigé ne vaut pas publiable** » — quinze remontées R-G-43…R-G-57 ouvertes, douze arbitrages délégués révocables, dette de vote sur F-92 et F-96. **La décision P0.2 est tranchée depuis le 21 juillet 2026 : filiation livresque retirée**, L-15 close par échec documenté, réversible par dépôt ultérieur. **Dix sites normatifs amendés** : Filiation, bloc Corpus d'appui, Volumétrie, décision 7 (⚠ **collision neuve des deux séries F-xx** — le Vol. III a désormais la sienne), Annexe B, risques 3, 9 et 11, ch. 47 et ch. 49 (« sous réserve de P0.2 » caduc). **Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes et fourchette ≈ 369 000–394 000 mots intactes. ⚠ La **collation de fond** contre le texte rédigé du Vol. III (l'homologue de la v0.6 pour les Vol. I-II) **n'est pas menée ici** : préalable déclaré à la rédaction des Livres III et VII, remis au PRD du Vol. IV. Détail au journal v0.13 |
| Historique v0.12                            | **0.12 — l'exécutable de contrôle reconstruit : le préalable de publication est levé** (23 juill. 2026). Passe d'appareil, sans objet éditorial : **aucun chapitre, aucun livre, aucune enveloppe, aucune relève** — 57 chapitres, dix livres I-X, fourchette ≈ 369 000–394 000 mots strictement inchangés. Trois objets. **(1) `check-toc.py` reconstruit et versionné au dossier** (quatorze contrôles C1-C14, domaine : chapitres 1-57, dix livres), **validé par mutation** — passage constaté sur le document intact, puis dix-sept mutations couvrant chaque classe de faute, toutes détectées ; trois avaient échappé à la première version du script, qui a été durcie avant publication (détail au journal). Reconstruction d'après la spécification du champ Contrôles, **non** restauration de l'exécutable perdu des passes v0.3-v0.6. **(2) Un fait de dépôt re-vérifié et corrigé en ses deux sites** : le README racine annonce désormais la somme (titre, table des livrables, section dédiée) — la Filiation et le risque 8 sont amendés. **(3) Cardinal C12 re-mesuré** : onze renvois nommés « Vol. III *TOC* §N.x » en zone normative — le « onze » de la décision 7 reste exact. Première passe depuis la v0.6 contrôlée par exécutable versionné. Détail au journal v0.12 |
| Historique v0.11                            | **0.11 — l'après-agentique : quatre trajectoires relevées sur dépôt de prépublications** (23 juill. 2026). Passe du genre des v0.7 et v0.10 — actualisation de faits vivants, non collation —, menée sur instruction d'auteur du 23 juillet 2026 et instruite **sur pièces écrites relevées sur arXiv exclusivement**, métadonnées (identifiant, titre, auteurs, dates de dépôt et de révision) vérifiées à l'API d'exportation du dépôt le jour de la passe. **Six relèves, toutes marquées « à instruire à la source primaire »** : aucune n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune (décision 8). Objet : ce qui se dessine **après** l'agentique telle que la somme la traite — la généralisation de la pile en « web agentique » (ch. 9), l'économie machine-à-machine déjà mesurable sur des rails que le plan n'instruit pas (ch. 40), l'agent mutable qui sape la réputation (ch. 19), l'auto-évolution qui fait de la dérive une fonctionnalité (ch. 44), l'assurabilité et les échelles d'autonomie au-delà de l'agentique (ch. 55). Chapitres marqués : ch. 9, 19, 40, 44 et 55. **Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes de tête et fourchette ≈ 369 000–394 000 mots identiques. ⚠ **Toutes les pièces sont des préimpressions non révisées par les pairs, résumés seuls consultés** : repérages [C], jamais des faits. Détail au journal v0.11 |
| Historique v0.10                            | **0.10 — la couche d'exécution : le harnais** (21 juill. 2026). Passe du genre de la v0.7 — actualisation de faits vivants, non collation —, déclenchée par une conférence datée du 21 juillet 2026 et instruite **sur pièces écrites**. **Huit relèves, toutes marquées « à instruire à la source primaire »** : aucune n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune (décision 8). Objet : le **harnais** — le programme qui héberge la boucle de l'agent et porte en propre la persistance de session, les modes, les sous-agents, la politique d'approbation d'outils, l'admission d'extensions et la compression de contexte — **n'est traité par aucun des 57 chapitres** ; le constat entre en **risque 14** et **n'est pas comblé** (ouvrir un chapitre créerait un second livre sans socle avant que le Livre IX ait le sien — risque 13). Chapitres marqués : ch. 20, 21, 22, 26, 43, 44, 52, 53, 54, 55 et 57. **Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes de tête et fourchette ≈ 369 000–394 000 mots identiques. ⚠ **La vidéo déclencheuse est sans transcription disponible** (piste de sous-titres automatiques déclarée mais vide au 21 juillet 2026) : elle est traitée comme **déclencheur daté, jamais comme source**, et les relèves s'appuient sur des pièces écrites datées, toutes [C]. Détail au journal v0.10 |
| Historique v0.9                             | **0.9 — condensation à dix livres** (20 juill. 2026). Sur instruction d'auteur : les treize livres de la v0.8 deviennent **dix**, sans toucher aux chapitres — la numérotation continue des chapitres (décision 1) est indépendante des livres, les 57 chapitres et tous les renvois « ch. N » sont **strictement inchangés**. Fusions : anciens Livres III+IV+V → **Livre III** (ch. 12-24, ~50 000 mots — émettre, versant hostile, horloge post-quantique : un seul arc issu des Parties I-V du Vol. III) ; anciens Livres IX+X → **Livre VII** (ch. 41-45, ~27 000 mots — appliquer et exploiter) ; décalage mécanique des autres (VI→IV, VII→V, VIII→VI, XI→VIII, XII→IX, XIII→X). Corps inchangé (301 000), total inchangé (≈ 369 000–394 000). La triade des capacités tient désormais en deux livres (III, VII) — risque 12 réduit ; risques 11 et 13, décision 9 et Nature re-libellés ou annotés. Règle et correspondance en **décision 10** ; **les journaux v0.3-v0.8, gelés, citent l'ancienne numérotation de livres**. Balayage exécutable rejoué après édition (voir Contrôles). Détail au journal v0.9 |
| Historique v0.8 | **0.8 — validation de cohérence et réouverture du périmètre** (20 juill. 2026). Deux objets. **(1) Validation de cohérence des douze livres hérités** : balayage exécutable ad hoc sur le fichier v0.7 — chapitres 1-54 contigus et uniques, douze livres, somme des enveloppes de tête conforme (287 000 de corps + 4 000 d'avant-propos, total annoncé 380 000 avec les 89 000 d'annexes), ventilation des annexes sommant à ≈ 89 000, aucun renvoi « ch. N » hors de 1-54. **Structure saine, aucun défaut nouveau** ; les sept relèves v0.7 restent « à instruire à la source primaire », aucune n'est consommée ici. **(2) Réouverture de la décision de périmètre v0.3, sur instruction d'auteur du 20 juillet 2026** : les trois fronts écartés (provenance des composants, mise en service, sémantique d'effet) entrent comme **Livre XII — L'agent comme livrable logiciel** (ch. 52-54, ~14 000 mots — l'estimation même de l'audit v0.3), inséré **avant** le livre de clôture, devenu **Livre XIII** (ch. 55-57). La somme passe à **57 chapitres en 13 livres, ≈ 369 000–394 000 mots**. Livre sans aucun socle hérité — déclaré tel (décision 9, risque 13), rédaction en dernier. Renumérotation bornée aux trois chapitres de clôture ; **les journaux v0.3-v0.7 et les rangées d'historique de ce bandeau, gelés, citent l'ancienne numérotation** (correspondance au journal v0.8). Détail au journal v0.8 |
| Historique v0.7 | **0.7 — actualisation à l'état de l'art de juillet 2026** (19 juill. 2026). Passe d'un autre genre que les collations v0.3-v0.6 : confrontation des **faits vivants** du plan à l'état du monde de juillet 2026, par balayage de sources ouvertes. **Sept actualisations, toutes marquées « à instruire à la source primaire »** — aucune n'entre au socle par cette passe (décision 8). **(1) AP2 — la divergence tranchée a un fait nouveau candidat** : des annonces publiques d'avril-mai 2026 font état du don d'AP2 (v0.2) à la **FIDO Alliance** le 28 avril 2026, sous deux groupes de travail ; c'est la « source primaire nouvelle datée » que l'Annexe C exige pour rouvrir — réouverture **déclenchée, non consommée** (ch. 10, Annexe C). **(2) MCP 2026-07-28** : la RC (gelée le 21 mai 2026) porte un cœur **sans état**, des extensions (Tasks, MCP Apps), un durcissement d'autorisation et une politique de dépréciation — rupture annoncée qui périme l'anatomie du ch. 8 **neuf jours après la date de ce fichier**. **(3) Filière IETF de l'identité d'agent** : le brouillon SCIM-agents expiré a des successeurs actifs à mi-2026 (ch. 13). **(4) IR 8547** : toujours brouillon à mi-2026, mais des instruments fédéraux américains de juin 2026 en opposabilisent les jalons (ch. 23). **(5) OTel GenAI/MCP** : toujours « Development » à la mi-2026 (ch. 43). **(6) ArchiMate 4** : ampleur de C260 confirmée (réduction d'environ 30 % du nombre d'éléments, couches remplacées par des domaines) — la re-vérification du mécanisme d'extension en v4 devient un préalable du ch. 48. **(7) Incidents d'identité agentique** : divulgations du 1ᵉʳ semestre 2026, candidats à l'événement de péremption du ch. 54 et corpus candidat au dénombrement qu'exige la thèse du ch. 20. S'y ajoutent **deux constats de dépôt** : `check-toc.py`, que le champ Contrôles invoque, est **introuvable au dépôt** ; et les chemins `Tocs/…` du journal v0.5 ne résolvent pas — les trois TOC sources vivent sous leurs volumes. Détail au journal v0.7 |
| Historique v0.6 | **0.6 — collation contre les volumes sources complets** (19 juill. 2026). Les passes antérieures collationnaient ce fichier contre les *plans* des volumes ; celle-ci l'a confronté au **texte rédigé** du Vol. I (233 000 mots) et du Vol. II (29 pièces), ainsi qu'au **PRD** du Vol. II. **Bilan structurel : sain** — les 91 sections du corps du Vol. I sont toutes affectées, les 24 chapitres du Vol. II tous cités, les 48 entrées F-xx toutes résolues, et les 181 renvois de section résolvent tous. **Bilan de fond : quinze écarts**, dont trois graves. **(1) Une lacune héritée manquait** : le PRD du Vol. II en porte **onze**, pas dix — la §10.11 (datation du Budget 2025) a été ouverte le 17 juillet, après la table de couverture du TOC du Vol. II sur laquelle la v0.5 s'était bâtie. Le registre passe à onze ; **c'est le PRD qui fait autorité, pas le TOC**. **(2) Deux formulations proscrites par la source** : « la supervision humaine **exigée** » au ch. 29, alors que le PRD impose « attendu par E-23 » et proscrit « exigé » ; et « art. 12.1 **outillé** » au ch. 50, alors que le ch. 23 du Vol. II écrit que « le blueprint ne doit pas prétendre le contraire ». **(3) Un renvoi structurellement ambigu** : le Vol. II porte **deux** « Annexe B » sans rapport — la matrice de sa Monographie et le blueprint de son PRD — et les ch. 46, ch. 49 et ch. 50 les citaient toutes trois sans nommer le document. Décision 7 étendue aux annexes, sous contrôle. S'y ajoutent quatre thèses plus fortes que le chapitre rédigé (ch. 5, ch. 7, ch. 10 et ch. 27 — décision 8), une section jamais affectée (**§2.8.5**, seule perte silencieuse du fichier), une chronologie inversée (ch. 7), une scission attribuée au mauvais chapitre (ch. 49-50), une plage de socle trop large (ch. 50), une double affectation du §5.3 et deux en-têtes de livre sur-inclusifs. Détail au journal v0.6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Historique v0.5                             | **0.5 — collation contre les trois TOC sources, et re-mesure de la volumétrie** (19 juill. 2026). Passe menée en confrontant ce fichier aux trois tables des matières sources (`Tocs/`), et non plus aux seuls volumes. Cinq classes de défauts corrigées. **(1) Volumétrie fausse sur une mesure** : « ADS Boréalis ≈ 90 000 mots » est démenti par mesure — l'ADS en fait **20 655** ; et l'enveloppe des neuf annexes (35 000) est **inférieure à la seule bibliographie du Vol. I** (37 104 mots mesurés), alors que le compendium doit porter les trois. Enveloppe et fourchette re-basées sur mesure. **(2) Renvoi pendant** : « Vol. III §10.4 » (ch. 53) ne résout pas — le ch. 10 du Vol. III s'arrête à §10.3. **(3) Couverture perdue** : Q4 de la série d'agenda du Vol. II (que le Vol. III déclare prolonger) n'était nommée nulle part ; les lacunes **§10.7 et §10.10** du PRD Vol. II avaient disparu, trois autres survivaient sans leur identifiant — un registre des **onze** lacunes héritées entre à l'Annexe C. **(4) Doctrine incomplète** : l'invariant était énoncé à **trois** termes alors que le Vol. I en pose un quatrième — l'*exploitation* (§4.12.4, élargi §7.0), « legs explicite au Vol. III » et fondement du Livre X, que le ch. 44 invoquait sans qu'il ait été posé ; et les trois capacités du Vol. III (émettre / appliquer / exploiter), qui sont ce qui sépare les Livres III, IX et X, n'étaient pas énoncées. **(5) Règles de gouvernance non héritées** : « une thèse de TOC n'est pas une entrée du socle » et la contrepartie du socle « construit par la rédaction » — les deux acquis les plus transférables du Vol. II — entrent en décision 8 et à l'Annexe A. S'y ajoutent l'ancrage de version du ch. 48 (ArchiMate 4 / C260) et la collision de numérotation que la fusion crée à l'Annexe H. Décision 7 étendue au Vol. III. **Seconde passe de cohérence sur l'ensemble** : trois en-têtes de livre revendiquaient une Partie qu'un autre livre entame (Livres III, VI et XI — double affectation jamais vérifiée au niveau des livres) ; le registre des lacunes ajouté ci-dessus était **creux**, huit des dix chapitres désignés ne nommant pas leur lacune ; le ch. 24 définissait encore l'invariant à trois termes ; le cardinal des renvois de série était périmé par l'ajout de Q4. Cinq contrôles exécutables nouveaux (12 à 16), tous validés par mutation. Détail au journal v0.5 en fin de fichier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Historique                                  | **v0.4** (19 juill. 2026) — cohérence interne et discipline épistémique : quatre garde-fous R-N du Vol. II laissés **nus** dans des chapitres consommant le Vol. III (ch. 16, ch. 34, ch. 41 et ch. 54) nommés, sous contrôle exécutable (contrôle 11, validé par mutation) ; « refonte pure — aucun contenu neuf » qualifié, le journal v0.3 consignant quatre enrichissements intra-chapitres ; titre du ch. 37 aligné sur sa réserve (« RTR visé ») ; révisions d'A2A ajoutées aux événements de péremption. **v0.3** (19 juill. 2026) — rebalancement structurel et audit de couverture : trois audits indépendants ont collationné chaque ligne « Fusion » contre les sources (Vol. I : 91 sections relevées sur les sept chapitres ; Vol. II : 29 pièces, socle de 46 entrées, R-1…R-8 ; Vol. III : plan v0.4) ; structure rééquilibrée à 54 chapitres en 12 livres, plus de livre à chapitre unique ; contrôles exécutables ajoutés (`check-toc.py`). **v0.2** (18 juill. 2026) — révision des renvois : §3.5 réacheminé, Annexe B du Vol. II rattachée, double affectation du §5.12 tranchée, sections orphelines réaffectées, convention du renvoi nommé posée (décision 7), corpus d'appui du Vol. III intégré avec ses réserves, Annexe I ajoutée. **v0.1** — cadrage initial : première fusion des trois volumes en une somme à numérotation continue, décisions de déduplication posées, deux divergences héritées tranchées, méthode et gel unifiés                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Date                                        | 26 juillet 2026 (reformatage markdown)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Statut                                      | Proposition de compilation — se substitue à la lecture des trois volumes une fois rédigée ; jusque-là, les trois volumes sources font foi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Nature                                      | **Compendium intégral** : omnibus qui absorbe Vol. I, II et III en un seul ouvrage réordonné, dédoublonné, à lecture autonome. Ce n'est ni un panneau du triptyque ni un méta-index — c'est la *somme* qui les remplace. ⚠ **Depuis la v0.8, l'absorption ne couvre plus tout l'ouvrage** : le Livre IX (l'agent comme livrable logiciel ; Livre XII à son entrée en v0.8) est de la matière neuve sans volume source, admise sur décision d'auteur et déclarée telle (décision 9, risque 13)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Filiation                                   | Quatrième opus, terminal. Absorbe :**Vol. I — Interopérabilité agentique** (cadre mondial et théorique, méthode ArchiMate/ADS Boréalis, gel juin 2026) ; **Vol. II — L'autonomie encadrée** (cas canadien réglementé, socle F-01…F-48 + F-23b, niveaux [A]/[B]/[C], gel 16-17 juillet 2026) ; **Vol. III — L'entreprise agentique** (identité, délégation, maillage, AgentOps, PQC — **rédigé, constat v0.13 sur pièces** : 34 pièces sur 34 au statut « Rédigé et relu adversarialement » au 22 juillet 2026, gel des pièces au 21 juillet 2026, socle propre **F-01…F-98** plus 33 entrées héritées H-01…H-33, 15 lots d'instruction clos, gouvernance PRD v1.3 / TOC v0.8 / PRDPlan v0.5, rendu FESP de 428 p. au 23 juillet 2026 ; ⚠ **« rédigé ne vaut pas publiable »**, régime que le Vol. III déclare lui-même — quinze remontées R-G-43…R-G-57 ouvertes, douze arbitrages délégués révocables, dette de vote sur F-92 et F-96 : voir le risque 11). Ce fichier consomme abondamment son PRD et son PRDPlan (garde-fous R-01…R-14, motifs de balayage §A.6, règle d'escalade §5.3, lacune L-15 close par la décision P0.2). ⚠ La mention « proposition v0.4, sans aucun socle F-xx » des versions antérieures à la v0.13 est **périmée depuis le 22 juillet 2026** ; la hiérarchie d'autorité du Vol. III demeure, et il la consigne lui-même : en cas d'écart entre son TOC et son PRD, **c'est le PRD qui fait foi** (le TOC conservant l'autorité sur le découpage), et le document doit être nommé à chaque renvoi (décision 7). Le README racine, réécrit depuis, annonce la somme — re-vérification du 23 juill. 2026 : titre, table des livrables et section Vol. IV dédiée (risque 8 amendé en v0.12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Décisions structurantes de la fusion       | (1)**Numérotation continue** des chapitres (1→57 depuis la v0.8 ; 1→54 avant elle) et des figures/tableaux/faits — un compendium n'a qu'une seule table. (2) **Déduplication** : tout sujet traité par ≥2 volumes est fusionné en un chapitre unique, la provenance et l'arbitrage de fusion étant tracés sous chaque entrée (ligne « Fusion »). (3) **Divergences tranchées** (voir Annexe C). (4) **Méthode unifiée** (voir Annexe A). (5) **Gel unique** à fixer au lancement de la rédaction, avec re-datation de tout fait périssable hérité des trois gels distincts. (6) **Couverture totale tracée** : chaque section des trois sources est affectée à un chapitre d'arrivée ou coupée explicitement (mention « coupe assumée ») — aucune perte silencieuse ; les **annexes et l'avant-propos** des volumes sources sont soumis à la même règle que leurs chapitres. (7) **Renvoi nommé, série nommée, identifiant nommé** : tout renvoi vers un document source nomme ce document — *Monographie*, *Synthèse* ou *PRD* — car le Vol. I vit en numérotation **triple** et non double (Monographie §1-§7 ; *Synthèse* **§1-§12**, et non §3-§12 comme l'écrivaient les v0.1-v0.2 ; Annexe B §0-§17) et les §8.x/§10.x du Vol. II existent à la fois dans sa Monographie et dans son PRD. **Tout renvoi vers une série d'identifiants internes nomme aussi sa série** : le Vol. II porte deux séries « Q n » indépendantes (*Monographie* ch. 16 §16.3, cinq questions AP2/RTR ; ch. 21 §21.2, six questions d'agenda). **Et tout garde-fou nomme son volume** : le Vol. II numérote **R-1…R-8**, le Vol. III **R-01…R-14** — deux séries distinctes portant sur des objets différents, dont les libellés courts se confondent à l'œil. Un « R-7 » nu est indécidable dans un chapitre qui consomme les deux volumes. ⚠ **La règle vaut aussi pour le Vol. III, et la v0.4 ne l'y appliquait pas** : ce volume vit lui aussi en numérotation multiple — son `TOC.md` (ch. 1-28, sections §N.x), son **PRD** et son **PRDPlan**, tous trois porteurs de §N.x —, et ce fichier cite les trois (« Vol. III §7.4 » = TOC ch. 7 ; « PRD du Vol. III §7.7 » ; « PRDPlan §1.5 »). Un « Vol. III §7.x » nu est donc indécidable exactement comme l'était un « R-7 » nu. **Convention retenue et appliquée en v0.5** : les onze renvois de section au Vol. III portent désormais leur document — `Vol. III *TOC* §N.x` pour le plan, `PRD du Vol. III §N` et `PRDPlan §N` pour les deux pièces de gouvernance. ⚠ **Précision défensive sur la *Synthèse* du Vol. I** : sa numérotation est **§1-§12** — vérifié le 19 juillet 2026 par relevé des titres de `Synthese Monographie.md` (§1 Introduction … §12 Conclusion). Les **TOC des Vol. I et III portent tous deux, encore, l'intervalle faux « §3-§12 »** (Vol. I, champ *Filiation* et table des livrables associés ; Vol. III, champ *Filiation* et risque 9c). Ce sont eux qui sont à corriger, non ce fichier : un futur éditeur qui collationnerait le compendium contre ces deux TOC réintroduirait l'erreur en croyant la corriger. ⚠ **Collision neuve, constat v0.13 — les F-xx sont devenus une série double.** Depuis la constitution du socle propre du Vol. III (F-01…F-98, versées du 21 au 22 juillet 2026 à quatre sièges datés de son PRD), un « F-36 » nu est indécidable entre le socle du Vol. II (F-01…F-48 + F-23b) et celui du Vol. III — exactement comme l'était un « R-7 » nu. **Convention transitoire de ce fichier** : les « F-xx » nus des lignes Socle désignent la série du **Vol. II**, seule existante à leur rédaction ; toute citation du socle du Vol. III s'écrit « **F-xx du Vol. III** ». Le règlement définitif appartient à la refonte de l'Annexe B (numérotation unique), dont le périmètre s'élargit d'autant. |
| Décision 8 — le plan n'est pas une source | **Une thèse de TOC n'est pas une entrée du socle et ne peut pas en tenir lieu** — règle établie par le Vol. II, qui a dû corriger quatre thèses de son propre TOC (ch. 2 « structure **toute** architecture », ch. 4 « dès l'origine », ch. 7 « support MCP **généralisé** », ch. 13 « **chaque** exigence… **est indéfendable** ») et la thèse de son ch. 15 (« le RTR **naîtra** », futur catégorique non attribué). Trois corollaires, tous opposables à ce fichier : (a) **le plan s'aligne sur le chapitre, jamais l'inverse** — dans les quatre cas, « la rédaction avait lu le socle mieux que le plan » ; (b) **une déviation fondée se déclare** — la déviation du ch. 16 du Vol. II était juste mais silencieuse, donc « indiscernable d'un oubli » ; (c) un conflit en-tête/corps non remonté **survit dans la pièce publiée**, les chapitres recopiant fidèlement le bandeau fautif. ⚠ Ce fichier porte au moins un énoncé exposé à cette règle : la thèse du **ch. 20** (« une part majoritaire des attaques… sont des attaques d'identité »), maintenue en forme forte avec son avertissement d'instruction — dispositif délibéré, à trancher par dénombrement avant rédaction, non à recopier tel quel dans le bandeau du chapitre. |
| Décision 9 — la matière neuve se déclare (v0.8) | La décision de périmètre v0.3 — trois fronts écartés (provenance des composants, mise en service, sémantique d'effet) — est **rouverte sur instruction d'auteur du 20 juillet 2026**, ce que le journal v0.3 prévoyait expressément, dans l'ordre d'instruction qu'il suggérait. Trois règles. **(a) La matière neuve se déclare** : le Livre XII (Livre IX depuis la v0.9) porte en tête son statut « aucun socle hérité », chaque ligne « Fusion » y écrit « aucune » plutôt que d'inventer une filiation, et chaque thèse y est marquée construction d'auteur — la décision 6 (couverture tracée) est sans objet pour un livre qui n'a pas de source, la décision 8 s'y applique doublement. **(b) Le livre de clôture reste terminal** : le Livre XII s'insère avant l'ancien Livre XII (horizon, frontière, péremption), devenu Livre XIII (Livre X depuis la v0.9), ses chapitres passant de 52-54 à **55-57** — la renumérotation est bornée à ces trois-là ; les journaux v0.3-v0.7 et les rangées d'historique de ce bandeau, gelés, citent l'ancienne numérotation (correspondance au journal v0.8). **(c) Rédaction en dernier** : après même les cinq livres du risque 11 — leur socle est à refondre ou à constituer depuis des repérages, celui du livre de matière neuve est à constituer depuis rien (risque 13). |
| Décision 10 — condensation à dix livres (v0.9) | Sur instruction d'auteur du 20 juillet 2026, les treize livres de la v0.8 sont condensés en **dix**, à chapitres strictement inchangés (1-57 — aucun renvoi « ch. N » touché, aucune annexe, aucun registre). Les anciens Livres III-IV-V fusionnent en **Livre III** (ch. 12-24, trois mouvements : émettre, ch. 12-19 ; versant hostile, ch. 20-22 ; horloge post-quantique, ch. 23-24) ; les anciens Livres IX-X fusionnent en **Livre VII** (ch. 41-45, deux mouvements : appliquer, ch. 41-42 ; exploiter, ch. 43-45) ; les autres se renumérotent sans changer de contenu (VI→IV, VII→V, VIII→VI, XI→VIII, XII→IX, XIII→X). Les en-têtes des livres fusionnés **combinent les lignes de provenance de leurs constituants sans perte** (décision 6), et l'emplacement de chaque ancien en-tête porte un marqueur de mouvement. Aucune enveloppe ne change en somme : 50 000 = 30+10+10, 27 000 = 15+12, corps à 301 000. ⚠ **Les journaux v0.3-v0.8 et les rangées d'historique de ce bandeau, gelés, citent l'ancienne numérotation de livres** (correspondance au journal v0.9) : un « Livre IX » de journal gelé désigne l'AgentMesh, non le livre de matière neuve ; un « Livre X » gelé désigne l'AgentOps, non la clôture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Contrôles                                  | `python check-toc.py` — numérotation continue, contiguïté des livres, renvois internes pendants, décomptes annoncés, arithmétique du budget, mention du corpus d'appui, traçabilité de chaque chapitre, garde-fous R-N nus dans les chapitres consommant le Vol. III, **renvois « Vol. III §N.x » laissés sans document nommé** (décision 7), **complétude du registre des onze lacunes héritées du PRD Vol. II** (Annexe C), **portage effectif de chaque lacune par le chapitre que le registre désigne** (un registre qui pointe vers un chapitre muet est creux), **cardinal en toutes lettres des renvois nommés au Vol. III** et **double revendication d'une Partie d'un volume source entre deux livres** (décision 6). À exécuter avant toute publication de ce fichier. ⚠ **Ce que le script ne couvre pas, et qui reste une collation manuelle** : le recouvrement entre un en-tête de livre qui revendique une Partie entière et un autre livre qui en prend un chapitre nommé — l'automatiser supposerait d'encoder ici la carte Partie → chapitres des volumes sources, or le Vol. III est une proposition volatile et une carte périmée ferait « détecter » des fautes inexistantes. À refaire à chaque révision d'un en-tête de livre. ⚠ Le contrôle du budget lie l'enveloppe de chaque livre à la fourchette annoncée : elles ne se modifient pas séparément, et **la forme `~N 000 mots` est réservée aux enveloppes de tête** — l'employer dans une ventilation de détail la ferait entrer dans la somme contrôlée. ⚠ **Constat v0.7 : `check-toc.py` est introuvable au dépôt** (balayage du 19 juill. 2026 — `**/check-toc.py`, zéro résultat), alors que les journaux v0.3 à v0.6 déclarent des contrôles « validés par mutation » jusqu'au contrôle 17. Les contrôles décrits ici sont donc une **spécification sans exécutable versionné** ; tant que le script n'est pas restauré ou reconstruit — et re-validé par mutation sur le document intact —, aucune passe ne peut se déclarer contrôlée, et le rétablir est un **préalable à toute publication** de ce fichier. ⚠ **Constat reconduit en v0.8** : le script demeure introuvable ; la passe v0.8 a été vérifiée par balayage exécutable ad hoc (contiguïté des chapitres 1-57, treize livres, sommes d'enveloppes 301 000 + 4 000 + 89 000 = 394 000, aucun renvoi « ch. N » hors de 1-57), non par `check-toc.py` — dont le domaine, à sa reconstruction, est la numérotation 1-57 (et, depuis la v0.9, dix livres). ⚠ **Constat reconduit en v0.9** : script toujours introuvable ; la condensation a été vérifiée par le même balayage exécutable ad hoc — chapitres 1-57 inchangés, contigus et uniques, **dix livres I-X**, enveloppes de tête inchangées en somme (301 000 de corps + 4 000 d'avant-propos ; 394 000 avec les 89 000 d'annexes), aucun renvoi « ch. N » pendant, aucune occurrence normative des anciens numéraux de livres hors zones gelées. ⚠ **Constat reconduit en v0.10 — quatrième passe consécutive sans exécutable** : le script demeure introuvable. La v0.10 n'ajoutant ni chapitre, ni livre, ni enveloppe, le balayage ad hoc a porté sur l'invariance — chapitres 1-57 contigus et uniques, dix livres I-X, somme des enveloppes de tête inchangée (301 000 + 4 000 ; 394 000 avec les annexes), aucun renvoi « ch. N » pendant, aucun cardinal en toutes lettres du fichier modifié —, plus la cohérence propre de la passe : les onze chapitres annoncés comme marqués au bandeau portent effectivement une marque « relève v0.10 », et le journal porte bien **huit** relèves numérotées. ⚠ **Constat reconduit en v0.11 — cinquième passe consécutive sans exécutable** : le script demeure introuvable. La v0.11 n'ajoutant ni chapitre, ni livre, ni enveloppe, le balayage ad hoc a porté sur l'invariance — chapitres 1-57 contigus et uniques, dix livres I-X, somme des enveloppes de tête inchangée (301 000 + 4 000 ; 394 000 avec les annexes), aucun renvoi « ch. N » pendant, cardinaux en toutes lettres de la passe re-mesurés —, plus la cohérence propre de la passe : les cinq chapitres annoncés comme marqués au bandeau (ch. 9, 19, 40, 44, 55) portent effectivement une marque « relève v0.11 », le journal porte bien **six** relèves numérotées, et chaque identifiant arXiv cité a été résolu à l'API du dépôt le 23 juillet 2026. ⚠ **Constat v0.12 — le préalable est levé** : `check-toc.py` a été **reconstruit le 23 juillet 2026** et versionné dans ce dossier (contrôles C1-C14 ; zones gelées — rangées Historique du bandeau et journaux — exemptées des contrôles de motifs, qui y citeraient des formes fautives à dessein ; spans « … » et `…` retirés avant contrôle, la décision 7 citant ses exemples entre guillemets), **validé par mutation** via `check-toc-mutations.py` versionné au même dossier — dix-sept mutations couvrant chaque classe de faute, toutes détectées, après passage constaté sur le document intact. Reconstruction d'après la présente spécification, non restauration : les journaux gelés qui citent « contrôle N » (jusqu'à 17) se lisent dans leur numérotation d'origine, les correspondances établies étant consignées dans le script (C7 ≈ contrôle 17, C8 ≈ contrôle 11). **Toute modification du script se re-valide par mutation avant publication.** ⚠ **Constat v0.13** : `check-toc.py` exécuté avant et après édition (C1-C14, sortie 0) ; harnais de mutation rejoué après le réancrage de son motif M14 (le conspectus passe à v0.13) — dix-sept mutations, toutes détectées ; aucun cardinal contrôlé ne bouge (57 chapitres, dix livres, 305 + 89, onze renvois nommés au Vol. III). ⚠ **Constat v0.17 — une classe de double revendication qu'aucun contrôle n'attrape.** Le contrôle de double revendication compare des **Parties** ; il ne voit pas le cas où une ligne Fusion absorbe un **intervalle de chapitres** (« Vol. III ch. 5-7 ») pendant qu'un autre chapitre en prélève **une section** nommée (« §7.4 ») — les deux renvois vivent à des grains différents, et chacun est valide isolément. Le défaut a été trouvé à la main, à la dérivation des tables détaillées. **Automatiser supposerait d'encoder ici la carte chapitre → sections de chaque volume source**, ce que le champ ci-dessus refuse déjà pour la carte Partie → chapitres, et pour le même motif. **Collation manuelle, à refaire à chaque révision d'une ligne Fusion citant un intervalle de chapitres.** ⚠ **Constat v0.17 — le contrôle des renvois de provenance est externe et non versionné** : les 955 renvois `← Vol. N` *document* `§N.M` des 57 tables détaillées ont été résolus contre les six documents sources (trois monographies, deux PRD, deux PRDPlan), validés par mutation (huit classes de faute), mais le script ne vit pas au dépôt — **cette vérification n'est pas reproductible en l'état**, et son versement dans `PRD/` est la dette d'appareil du fichier. ⚠ **Constat v0.18 — un reformatage ne relève d'aucun des quatorze contrôles, et c'est à savoir avant d'en tenter un autre.** Les contrôles portent sur des **motifs de ligne** — titre de chapitre, titre de livre, rangées du bandeau, enveloppes de tête, rangées du registre des lacunes : aucun ne connaît la forme des tables des matières détaillées, de sorte qu'une promotion de puces en titres passe sans être vue, donc sans être validée. Le contrôle propre à cette passe est **externe et jetable** : comparaison du flux de mots avant/après reformatage (**72 764 mots, séquence identique**), qui établit qu'aucun mot n'a été ajouté, retiré ni déplacé. L'exécution de `check-toc.py` avant et après (C1-C14, sortie 0) prouve que la forme reste **conforme à ce que le script sait lire**, jamais que la transformation est fidèle — ne pas confondre les deux. |

---

## Titre

### La somme agentique

#### Interopérabilité, autonomie encadrée et fabrique de confiance : déployer des agents en services financiers réglementés (2024-2032)

*Justification du titre : les trois volumes portaient chacun une thèse partielle — « autonomie graduée sous contrôle de finalité » (I), « autonomie encadrée / framed autonomy » (II), « la confiance se fabrique » (III). Le compendium ne les juxtapose pas : il montre qu'elles sont trois coupes d'un même objet. « La somme agentique » revendique le genre — une* summa*, non une anthologie — et le sous-titre énumère les trois plans (interopérabilité, encadrement, confiance) et borne le domaine (services financiers réglementés) et l'horloge (2024-2032, des premiers protocoles ouverts aux jalons PQC).*

## Thèse d'ensemble

Déployer des agents non humains qui engagent la responsabilité d'une institution financière réglementée est **un seul problème d'ingénierie continu**, non trois — et c'est la démonstration de cette continuité qui justifie de refondre trois volumes en une somme. Le problème se lit sur trois plans qui ne sont pas des sujets séparés mais des coupes du même objet : **faire coopérer** les agents (l'interopérabilité — protocoles, sémantique, maillage), **les encadrer** sous un contrôle de finalité que la réglementation impose (l'autonomie encadrée — orchestration déterministe, frames normatifs), et **fonder la confiance** que cette coopération encadrée présuppose sans jamais la produire elle-même (la fabrique — identité non humaine, délégation vérifiable, exploitation dans la durée).

Les trois volumes sources le prouvaient chacun à demi : le Vol. I posait la théorie mais s'arrêtait au seuil du droit applicable ; le Vol. II instruisait le droit canadien mais présupposait la théorie du Vol. I sans la reconstruire ; le Vol. III isolait le verrou commun — l'identité — mais le traitait comme un ouvrage à part. Le compendium tient les trois ensemble : l'invariant du Vol. I — **découplage, contrat, évolution, et un quatrième terme, l'*exploitation*** — devient le fil qui traverse l'orchestration encadrée (II) et la crypto-agilité (III) ; le « pont » du Vol. II (des contraintes réglementaires aux frames déterministes) devient l'articulation centrale entre les plans I et III ; le « passeport d'agent » du Vol. III redevient ce qu'il est — une pièce d'une architecture de référence unique, formalisée en ArchiMate (méthode-signature du Vol. I) et instanciée sur un cas financier canadien (continuité Boréalis → portefeuille IBM). L'ensemble est tendu par une horloge datée : la convergence protocolaire (2024-2026), les entrées en vigueur réglementaires (1ᵉʳ mai 2027) et la migration post-quantique (jalons NIST 2030/2035).

**Ajout v0.8 — le quatrième plan.** Les trois plans tiennent l'agent pour un *interlocuteur* : à faire coopérer, à encadrer, à accréditer. Or il est aussi un *livrable logiciel* — un artefact qui se compose, se met en service et produit des effets — et l'audit v0.3 a établi qu'aucun des trois volumes ne le traite ainsi. Le Livre IX (entré en v0.8 comme Livre XII), matière neuve admise sur décision d'auteur (décision 9), porte ce quatrième plan : provenance des composants, mise en service, sémantique d'effet. Il **complète** la démonstration de continuité, il ne la fonde pas — et il est le seul livre de la somme sans socle hérité, ce qui se déclare (risque 13).

## Les deux armatures héritées — à énoncer avant d'être invoquées

Le compendium reprend deux ossatures conceptuelles de ses sources. Aucune des deux n'était énoncée dans les v0.1-v0.4, alors que toutes deux y étaient **invoquées** — défaut de la même famille qu'un renvoi pendant, et corrigé en v0.5.

**L'invariant à quatre termes.** Le Vol. I énonce **découplage / contrat / évolution**, puis lui adjoint au ch. 4 (*Monographie* §4.12.4) un quatrième terme — l'**exploitation** —, repris et élargi au ch. 7 (§7.0) : *un parc d'agents doit rester non seulement interopérable, mais opérable*. Le Vol. I qualifie ce quatrième terme de **legs explicite au Vol. III**, dont la Partie VIII (AgentOps) le prend pour fondement. Dans la somme, il est le fondement du **Livre VII**, et le ch. 44 l'invoque nommément (« réalisation opérationnelle du quatrième terme de l'invariant ») : l'énoncer à trois termes, comme le faisaient les versions antérieures, rendait cette invocation sans antécédent. Le terme est posé à l'avant-propos, éprouvé au ch. 1 (découplage/contrat), au ch. 24 (crypto-agilité comme application de l'invariant à la couche cryptographique) et refermé au Livre VII.

**Les trois capacités.** Le Vol. III ordonne son propos par trois capacités de l'organisation — **émettre** une identité opposable, **appliquer** cette identité là où elle est vérifiée, **exploiter** le comportement dans la durée. Cette triade est ce qui explique la structure de la somme sur son plan « confiance » : **Livre III = émettre** (avec ses versants hostile et post-quantique, ch. 20-24), **Livre VII = appliquer et exploiter** (le maillage est à l'identité ce que le tribunal est à la loi ; l'exploitation referme l'invariant). La v0.8 les séparait de six livres ; la condensation v0.9 (décision 10) les resserre en deux livres — le risque de dilution que le Vol. III avait identifié (son risque 6) en est réduit sans être éteint, deux capacités cohabitant désormais dans un même livre, et sa parade est reconduite : tout contenu de maillage ou d'exploitation sans lien à l'identité ou à la délégation est hors périmètre.

## Publics visés

Architectes d'entreprise et directions technologiques des institutions financières canadiennes ; responsables IAM/CIAM, RSSI et équipes de sécurité offensive/défensive ; responsables risque, conformité et audit (E-23, AMF, Loi 25, ACVM) ; équipes plateforme, SRE et exploitation (AgentOps/MLOps/FinOps) ; dirigeants instruisant la trajectoire de maturité agentique de leur organisation ; chercheurs en interopérabilité, identité décentralisée et sécurité des systèmes multi-agents. *Un lecteur pressé côté canadien peut entrer directement au Livre V (réglementaire) ou au Livre VIII (blueprint), en remontant aux Livres I-III au besoin — le compendium conserve les parcours différenciés des sources.* **Les deux dispositifs du Vol. I sont reconduits** (précision v0.5, parade concrète du risque 1) : les encadrés ***Perspective recherche***, qui isolent les apports théoriques, et les encadrés ***Mise en œuvre***, qui isolent les normes datées et les considérations de déploiement. Ils sont ce qui permet au double lectorat — recherche et praticien-architecte — d'être servi sans cloisonner le propos, et à 394 000 mots ils cessent d'être un confort de mise en page pour devenir un instrument de navigation.

## Corpus d'appui hérité du Vol. III — ⚠ filiation retirée (P0.2, 21 juillet 2026), réversible

Le Vol. III adossait plusieurs de ses chapitres à trois ouvrages de **littérature secondaire de cadrage** : Arsanjani & Bustos, *Agentic Architectural Patterns for Building Multi-Agent Systems* (Packt — discipline des patrons, trois modèles de maturité, cas fil rouge *loan processing*) ; Nagasubramanian, *Agentic AI for Engineers* (Apress, 2026 — progression automatisation → autonomie, test-évaluation-déploiement) ; Ranjan, Chembachere & Lobo, *Agentic AI in Enterprise* (Apress, 2025 — préparation organisationnelle).

⚠ **Ce corpus n'a jamais été un acquis, et la décision est maintenant prise (constat v0.13).** La vérification du 18 juillet 2026 consignée au PRD du Vol. III (§7.7) avait établi que **les trois ouvrages sont introuvables au dépôt** — inventaire exhaustif des formats, recherche par auteur, titre et ISBN, balayage de l'historique Git : aucun n'y a jamais existé. **La décision d'auteur P0.2 a été tranchée le 21 juillet 2026 : la filiation livresque est retirée.** Le rejeu de la vérification l'a confirmé jusque dans l'historique Git ; **L-15 est close par échec documenté** — un résultat, non une lacune non instruite —, et les sept sections et l'annexe E du Vol. III qui en dépendaient sont **réaffectées à son socle** (table de réaffectation au TOC v0.8 du Vol. III). L'issue que ce bloc prévoyait est advenue : le croisement grille × maturité se rebâtit sur l'autonomie graduée et la grille des cinq questions, et le catalogue de patrons sur le seul héritage GoF/EIP (Annexe G). ⚠ **La décision est réversible** — un dépôt ultérieur rouvre L-15, réserve que le Vol. III consigne lui-même : les mentions « corpus d'appui » ci-dessous sont **conservées comme marqueurs conditionnels** de cette réouverture éventuelle, jamais comme des sources disponibles, et aucun chapitre du compendium ne se rédige en s'appuyant sur ces ouvrages sans dépôt effectif. ⚠ **Vigilance héritée, changée de nature** : le Vol. III rédigé a comblé ses huit emplacements par **construction d'auteur sous CA-07** (« Lecture de l'auteur » en tête d'énoncé) — la fusion reprend ces passages avec leur marquage, jamais comme des faits de corpus.

**Réserves reconduites, si un dépôt ultérieur rouvre L-15** : statut [C] à l'entrée avec élévation [B] par extraction citée ; règle du « jamais seul » (aucune affirmation centrale portée par le corpus sans source primaire concordante) ; datation au bouclage éditorial du livre et revalidation de tout fait périssable à la source primaire ; antériorité à la stabilisation protocolaire de 2025 (Ranjan et al.) ; **biais d'écosystème attaché au seul Arsanjani & Bustos** — la formule « deux ouvrages d'auteurs Google Cloud », reprise de la v0.2, est une incohérence que le Vol. III a lui-même relevée dans ce fichier (J-1) : elle avance un second ouvrage que sa source ne nomme pas, et elle est retirée ; « manuel généraliste, profondeur inégale sur l'identité » (Nagasubramanian) ; « traiter les patrons comme cadre, **vérifier chaque affirmation protocolaire à la source primaire** » (Arsanjani & Bustos).

Chapitres consommateurs : 15 (grille × maturité), 18 (patrons d'interaction humain-agent), 44 (cycle de vie), 47 (modèles de maturité), 49 (préparation organisationnelle) et 50 (cas fil rouge), **plus l'Annexe G** (catalogue de patrons). Les deux derniers rattachements manquaient à la v0.2.

## Volumétrie indicative

Somme naïve des trois volumes (décomptes bruts `wc`, non comparables entre eux — voir la mise en garde) : **Vol. I ≈ 233 000 mots** (`wc -w` sur `Monographie.md`, 19 juill. 2026 : 233 257, dont **bibliographie générale 37 104** et **Annexe B / ADS Boréalis 20 655**), **Vol. II ≈ 92 000 mots** (décompte de référence PRDPlan §4.2 ; ≈ 200 000 en brut avec pièces de gouvernance), **Vol. III ≈ 160 000 mots** (**mesuré : 160 427**, commande de référence du volume — `LC_ALL=C.UTF-8`, PRDPlan §1.5 —, 34 pièces, relevé du 22 juillet 2026 porté à son registre de gel ; la cible planifiée était de 102 500 mots, et le Vol. III attribue l'écart de +56,5 % aux bornes rétablies par ses garde-fous, non à un ajout de matière — chiffre de la v0.4 à v0.12 de ce fichier : « ≈ 102 500, planifié, non écrit », périmé par la mesure). Le compendium est projeté à **≈ 369 000–394 000 mots**, 57 chapitres en 10 livres, avant-propos, 9 annexes. La borne haute est la **somme exacte des enveloppes déclarées ci-dessous** (394 000 = 301 000 de corps — dont 14 000 de matière neuve au Livre IX, v0.8 — + 4 000 d'avant-propos + 89 000 d'annexes) ; la borne basse suppose la déduplication des recouvrements de corps (protocoles, identité, blueprint, réglementaire — estimés à 25-35 % du matériau) effectivement réalisée. **Fourchette indicative, non normative** (leçon du Vol. II : un écart se documente, il ne se corrige pas par amputation). ⚠ **Conséquence v0.13** : les enveloppes des Livres III et VII (77 000 mots à elles deux) avaient été calibrées sur un Vol. III planifié à 102 500 mots ; contre la mesure (160 427), le même périmètre suppose une condensation d'environ 52 % au lieu d'environ 25 %. La fourchette reste inchangée — indicative —, et le re-calibrage éventuel des enveloppes est une décision d'auteur, remise au gel unique.

⚠ **Deux chiffres de la v0.4 étaient faux, et la mesure les tranche.** (1) « Vol. I ≈ 241 000 mots, **dont l'ADS Boréalis en annexe, ≈ 90 000** » : l'ADS mesure **20 655 mots**, soit un facteur 4,4. Le TOC du Vol. I déclarait de son côté « ≈ 17 500 mots » d'après le décompte porté en tête d'ADS — sous-estimé de ~18 % par rapport à la mesure sur le fichier consolidé, mais du bon ordre de grandeur ; c'est la valeur de 90 000 qui n'a aucune source, et elle est retirée. (2) L'enveloppe des **neuf** annexes était portée à 35 000 mots alors que **la seule bibliographie du Vol. I en fait 37 104** et que l'Annexe I doit porter celles des *trois* volumes : deux annexes sur neuf dépassaient à elles seules l'enveloppe entière. Ventilation indicative reconstruite (non normative, et **délibérément écrite hors de la forme `~N 000 mots`** pour ne pas entrer dans la somme contrôlée) :

| Annexe | Contenu                               |    Mots (indicatif) | Origine du chiffre                                                                                             |
| ------ | ------------------------------------- | ------------------: | -------------------------------------------------------------------------------------------------------------- |
| A      | Méthode unifiée                     |               4 000 | estimation (Vol. II Annexe A mesurée à 2 046, élargie aux trois méthodes)                                  |
| B      | Socle factuel consolidé              |               8 000 | estimation (46 entrées du Vol. II + faits du Vol. I + repérages [C] du Vol. III)                             |
| C      | Faits partagés, divergences, lacunes |               3 000 | estimation                                                                                                     |
| D      | Chronologie fusionnée 2023-2032      |               4 000 | Vol. II Annexe C mesurée à 1 884, étendue à 2032 et aux trois volumes                                      |
| E      | Glossaire bilingue unifié            |               4 000 | Vol. II Annexe D mesurée à 2 901, fusionnée avec celle du Vol. III                                          |
| F      | Matrice des mécanismes               |               3 000 | Vol. II*Monographie* Annexe B (matrice) mesurée à 1 930, élargie                                          |
| G      | Catalogue de patrons                  |               2 500 | budget déclaré par le Vol. III (son Annexe E)                                                                |
| H      | ADS Boréalis intégrale              |    **20 655** | **mesuré** (`wc -w`, `Monographie.md` § Annexe B, 19 juill. 2026)                                  |
| I      | Bibliographie générale consolidée  |    **40 000** | **plancher mesuré 37 104** (Vol. I seul, 1 270 entrées) + corpus Vol. II et III, après dédoublonnage |
|        | **Total**                       | **≈ 89 000** |                                                                                                                |

*⚠ Ces chiffres agrègent des décomptes pris par des commandes différentes ; aucun n'est une mesure unifiée, et les mesures nouvelles ci-dessus sont des `wc -w` bruts sur fichier consolidé — balisage Markdown, tables et sources Mermaid compris. La première tâche de la rédaction reste de re-mesurer les trois corpus par une commande de référence unique (héritage direct de l'incident de décompte du Vol. II). Ce que ces mesures établissent n'est pas le chiffre juste : c'est que deux chiffres publiés étaient faux d'un facteur, ce qui est un fait suffisant pour les retirer.*

⚠ **Conséquence à ne pas taire : la somme est plus lourde que ne l'annonçait la v0.4, non par ajout de contenu mais par correction d'un budget d'annexes sous-évalué.** Les livres hérités des trois volumes restent à 287 000 mots — inchangés ; le Livre IX (matière neuve, v0.8) y ajoute 14 000 mots de matière neuve — l'estimation même de l'audit v0.3 —, portant le corps à 301 000 mots. Le risque 1 (explosion volumétrique et non-lecture) en est aggravé, pas atténué : à 394 000 mots, la somme est sans ambiguïté un ouvrage de référence, et ses parades — parcours différenciés, renvois internes denses, Annexe F comme table de navigation — cessent d'être un confort pour devenir la condition de son utilité.

---

## Avant-propos et note méthodologique unifiée *(~4 000 mots)*

Origine : la refonte des trois volumes en une somme, motivée par leur continuité démontrée. Définition de travail posée d'entrée : l'**agent d'entreprise** est un système non humain à qui une organisation délègue des tâches qui engagent sa responsabilité, et qu'elle doit rendre interopérable, encadrer et rendre digne de confiance. Reprise du **mode d'emploi de lecture** hérité du Vol. I *Monographie* §5.0.1 (ce qui est acquis des livres amont, ce qui est ajouté) et du patron directeur **« autonomie graduée sous contrôle de finalité »** (§5.0.2, avec les quatre durcisseurs financiers), que la thèse d'ensemble revendique et qui doit donc être posé avant d'être invoqué. **Même exigence pour les deux armatures héritées** (voir la section dédiée en tête de fichier) : l'**invariant à quatre termes** — découplage, contrat, évolution, **exploitation** (Vol. I *Monographie* §4.12.4, élargi §7.0) — est posé ici en entier, faute de quoi l'invocation du « quatrième terme » au ch. 44 serait sans antécédent ; et les **trois capacités** du Vol. III — émettre, appliquer, exploiter — sont énoncées ici comme principe d'ordre des Livres III et VII — émettre au premier, appliquer et exploiter au second —, que la v0.8 séparait de six livres et que la condensation v0.9 resserre. **Méthode unifiée** (détail Annexe A) : socle factuel daté et cité ; niveaux de preuve [A]/[B]/[C] (héritage Vol. II) ; tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF pour tout énoncé prospectif (héritage Vol. I) ; vote adversarial multi-juges sur les affirmations centrales ; attribution systématique des métriques auto-déclarées (**PRD Vol. II §7.5**, à chaque occurrence) ; distinction stricte entre lien documenté et inférence d'auteur ; corpus d'appui mobilisé en cadrage, jamais en preuve (règle du « jamais seul », héritage Vol. III) ; **convention de qualification cryptographique** (héritage Vol. III, garde-fou R-02) — un mécanisme est qualifié par ce que sa spécification *démontre*, jamais par ce qu'elle *promet* : c'est cette règle, et non un jugement d'humeur, qui fait du ch. 16 le chapitre « à plus haut risque de surinterprétation » ; **échelle des trois degrés d'absence** (héritage Vol. III, R-14) — *fait négatif vérifié* (établi par balayage documenté) > *fait négatif établi* > *absence de documentation*, jamais interchangeables, le troisième n'autorisant aucune conclusion. **Convention de datation** : gel unique de l'ouvrage + date de gel par chapitre pour les faits périssables. **Décompte** : commande de référence unique à fixer au lancement — le Vol. III en a déjà une (`LC_ALL=C.UTF-8`, PRDPlan §1.5), le Vol. II a assumé un sous-compte de 1,3 % en locale `C` qu'il ne pouvait plus corriger sans invalider ses chiffres publiés ; la somme n'a pas cette contrainte et doit choisir avant de mesurer. ⚠ **Et la commande de référence est elle-même du contenu, qui se vérifie sur son domaine entier.** Le Vol. II a publié la sienne après l'avoir *testée sur deux fichiers pour vingt-neuf* : elle s'arrêtait à « ## Notes », que trois pièces ne portent pas, et comptait leur bloc de gouvernance en commentaire (son annexe C : 2 897 annoncés pour 1 656 réels). Le défaut a été relevé par une relecture adversariale, non par la passe qui avait fixé la commande, et il a fallu **quatre mesures successives** (89 757 → 88 021 → 90 362 → 92 059) pour arrêter un chiffre — chacune vraie à sa date et fausse à la suivante. La somme fixe sa commande, la valide sur les trois corpus entiers, puis mesure : dans cet ordre. **La v0.5 de ce fichier illustre le coût de l'ordre inverse** — deux chiffres publiés (ADS, enveloppe des annexes) étaient faux d'un facteur, et seule une mesure les a montrés. **Escalade** : règle d'arbitrage posée *avant* la première rédaction et non apprise en cours de route (héritage Vol. III, PRDPlan §5.3 — au Vol. II, un chapitre pivot a dû trancher seul une remontée non arbitrée). **Motifs de balayage** : les critères d'acceptation et les motifs qui les contrôlent ne se séparent pas (Vol. III, PRD Annexe A §A.6) ; la somme doit se doter des siens, faute de quoi sa méthode n'est pas vérifiable. **Socle des chapitres de synthèse — règle et contrepartie** (héritage Vol. II, arbitrage de clôture P3) : un chapitre de synthèse ne mobilise pas un socle *choisi à l'avance*, mais celui des chapitres qu'il croise ; sa liste ne peut donc être arrêtée qu'à la rédaction. La contrepartie est **obligatoire et non négociable** : le chapitre **énumère dans son en-tête** les entrées effectivement mobilisées et les garde-fous effectivement balayés, **y compris ceux dont il constate zéro occurrence**. C'est ce dispositif, et non une relecture, qui a permis au Vol. II de contrôler la traçabilité de son ch. 18 — et c'est ce même chapitre qui y a détecté une erreur de marquage du socle. La somme compte bien plus de chapitres de synthèse que le Vol. II (ch. 46, ch. 47, ch. 51, ch. 55, ch. 56 et ch. 57) et six annexes de méthode ou de table (A, B, C, D, E, F) : la règle s'applique aux douze. Avertissements : pas de conseil juridique ni d'investissement ; neutralité fournisseur (Entra Agent ID, watsonx, Boréalis traités comme cas documentés, non comme recommandations). Note sur la fusion : ce qui, dans les trois volumes, était renvoi inter-volumes devient renvoi interne ; les deux divergences factuelles héritées sont tranchées et non plus signalées comme ouvertes — **sans que la clôture d'une divergence vaille clôture d'une lacune** (Annexe C).

*Fusion : Vol. II avant-propos + Vol. I* Monographie *§5.0.1/§5.0.3 (mode d'emploi, convention de sourçage) et §5.0.2 (patron directeur et quatre durcisseurs).*

---

## LIVRE I — Fondements : interopérabilité et ingénierie agentique

*(absorbe Vol. I ch. 1-2 ; ~40 000 mots)*

### Chapitre 1 — L'interopérabilité comme problème d'intégration d'entreprise

**Thèse** : l'interopérabilité n'est pas un attribut mais une propriété à maintenir dans le temps ; la dette d'intégration et le coût de la non-interopérabilité en font un problème économique avant d'être technique.
Sections : définition et taxonomie des niveaux (LCIM) ; couplage, découplage, conception orientée contrat ; **cadres de référence et modèles de maturité** (dimensions canoniques et ISO 11354 ; LISI, EIMM, IMM/IMAPS et les limites des modèles à niveaux ; EIF/EIRA et l'*Interoperable Europe Act*) ; SOA → ESB → microservices → maillage de services et d'événements ; styles et contrats d'API ; MOM, courtiers et architecture événementielle ; patrons d'intégration d'entreprise (EIP), orchestration/chorégraphie.
*Fusion : Vol. I* Monographie *§1.0-1.6, condensé. Le §1.3.4 (maillage de services/événements) est **scindé** — le socle transposable y reste, la déclinaison agentique part au Livre VII (ch. 41). Le §1.6.3 — dont le titre exact est **« Exécution durable, pipelines et orchestration agentique »**, et non « orchestration agentique » seule — part **en entier** au Livre IV (ch. 25) : l'exécution durable et les pipelines le suivent, et ne sont donc **pas** traités ici malgré ce que la liste de sections des v0.1-v0.5 laissait entendre. Coupes assumées : §1.11 (tendances agentiques 2024-2026 — matériau daté, remplacé par les Livres II et X) et §1.12 (synthèse du chapitre source, absorbée ici).*

**Table des matières détaillée du chapitre 1**

*Dérivée de `Monographie.md` §1.0-1.6 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 1.0 — Introduction : l'interopérabilité comme problème d'intégration d'entreprise

- 1.0.1 Coût de la non-interopérabilité et dette d'intégration : l'enjeu économique et le périmètre du chapitre — *← §1.0.1*
- 1.0.2 L'invariant transversal — découplage, contrat, évolution : les deux premiers termes sont éprouvés ici, l'invariant complet (quatre termes, dont l'exploitation) étant posé à l'avant-propos et refermé au Livre VII — *← §1.0.2.1*
- 1.0.3 Parcours différenciés : lecture recherche et lecture praticien-architecte ; reconduction des encadrés *Perspective recherche* et *Mise en œuvre* — *← §1.0.2.2*

#### § 1.1 — Fondements et théorie de l'interopérabilité

- 1.1.1 Définir l'interopérabilité : définition de travail (échanger **et** utiliser) ; interopérabilité / intégration / compatibilité / portabilité ; exigence qualité ISO/IEC 25010:2023 — *← §1.1.1.1-1.1.1.3*
- 1.1.2 Taxonomie des niveaux : pile canonique (technique, syntaxique, sémantique, organisationnel) et LCIM — *← §1.1.2.1-1.1.2.2*
- 1.1.3 Couplage, découplage et conception orientée contrat : facettes du couplage (Hohpe) ; le contrat comme support formel ; hétérogénéité, autonomie, distribution — *← §1.1.3.1-1.1.3.3*
- 1.1.4 L'interopérabilité dans le temps : évolution et versionnement ; formalismes de la compatibilité comportementale — *← §1.1.4.1-1.1.4.2*

#### § 1.2 — Cadres de référence et modèles de maturité

⚠ *absente de la liste de sections ci-dessus (voir écart n° 1 plus bas)*

- 1.2.1 Dimensions canoniques (juridique, organisationnelle, sémantique, technique) et ISO 11354 / Framework for Enterprise Interoperability — *← §1.2.1.1-1.2.1.2*
- 1.2.2 Modèles de maturité : LISI, OIM et la lignée C4ISR/DoD ; EIMM, IMM/IMAPS ; limites des modèles à niveaux face aux architectures dynamiques — *← §1.2.2.1-1.2.2.3*
- 1.2.3 Le cadre européen : EIF et EIRA ; Interoperable Europe Act (évaluation obligatoire, solutions labellisées) — *← §1.2.3.1-1.2.3.2*

#### § 1.3 — Architectures d'intégration : de la SOA aux maillages

- 1.3.1 Architecture orientée services : principes, SOAP/WSDL/WS-\*, granularité et gouvernance — *← §1.3.1.1-1.3.1.3*
- 1.3.2 Bus de services d'entreprise et intégration B2B : médiation ESB, iPaaS et low-code, EDI/EDIFACT-X12, AS2/AS4 — *← §1.3.2.1-1.3.2.3*
- 1.3.3 Microservices et communication inter-services : continuité et rupture avec la SOA ; styles synchrone / asynchrone / événementiel ; résilience, cohérence, anti-patrons distribués — *← §1.3.3.1-1.3.3.3*
- 1.3.4 Maillages — socle transposable seulement : plan de contrôle et plan de données (sidecar, ambiant/eBPF), Gateway API, *event mesh* — *← §1.3.4.1-1.3.4.4, scindé : la déclinaison agentique part au ch. 41 (Livre VII)*

#### § 1.4 — Styles d'API, conception et gestion

- 1.4.1 Panorama et critères de choix : REST et modèle de Richardson ; RPC/gRPC ; GraphQL et fédération ; webhooks — *← §1.4.1.1-1.4.1.4*
- 1.4.2 Contrats d'API : OpenAPI et JSON Schema ; AsyncAPI ; *contract-first* vs *code-first*, versionnement et compatibilité — *← §1.4.2.1-1.4.2.3*
- 1.4.3 Gestion d'API : passerelle et plan de trafic ; portails et *API-as-a-Product* ; orchestration de parcours (Arazzo) et surcharges (Overlay) — *← §1.4.3.1-1.4.3.3*

#### § 1.5 — Messagerie, middleware orienté message et architecture événementielle

- 1.5.1 Modèle du MOM : message, canal, producteur/consommateur ; files, publication-abonnement, flux persistants — *← §1.5.1.1-1.5.1.2*
- 1.5.2 Courtiers, protocoles et garanties : Kafka, RabbitMQ, Pulsar, NATS ; AMQP, MQTT, STOMP ; sémantique de livraison, idempotence, ordre — *← §1.5.2.1-1.5.2.3*
- 1.5.3 Architecture événementielle et fiabilité : *event sourcing* et CQRS sous l'angle intégration ; Outbox transactionnel et CDC ; CloudEvents et registres de schémas — *← §1.5.3.1-1.5.3.3*

#### § 1.6 — Patrons d'intégration et coordination de processus

- 1.6.1 Le langage des patrons d'intégration d'entreprise (EIP) : canaux, routage, transformation, points d'extrémité ; modèle de données canonique — *← §1.6.1.1-1.6.1.2*
- 1.6.2 Coordination : orchestration vs chorégraphie ; saga, 2PC, cohérence éventuelle ; BPMN, DMN, CMMN — *← §1.6.2.1-1.6.2.3*

⚠ *Le §1.6.3 (« Exécution durable, pipelines et orchestration agentique ») n'est pas repris ici : il part en entier au ch. 25 (Livre IV) — voir écart n° 2.*

#### § 1.7 — Synthèse : ce que le chapitre lègue à la somme

reprise du §1.12 source, réorientée vers les renvois internes (IAM → ch. 3 ; sémantique → ch. 2 ; orchestration déterministe → ch. 25 ; maillage agentique → ch. 41). *Section de sortie sans homologue direct dans la source — construction d'éditeur.*

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §1.0 | § 1.0 | condensé |
| §1.1 | § 1.1 | condensé |
| §1.2 | § 1.2 | condensé — non nommé dans la liste de sections |
| §1.3.1-1.3.3 | § 1.3.1-1.3.3 | condensé |
| §1.3.4 | § 1.3.4 (socle) + ch. 41 (agentique) | scindé, déclaré |
| §1.4 | § 1.4 | condensé |
| §1.5 | § 1.5 | condensé |
| §1.6.1-1.6.2 | § 1.6 | condensé |
| §1.6.3 | ch. 25 (Livre IV) | déplacé en entier |
| §1.7-1.8 | ch. 2 | hors périmètre |
| §1.9-1.10 | ch. 3 | hors périmètre |
| §1.11 | — | coupe assumée |
| §1.12 | § 1.7 | absorbée |

**Deux écarts constatés dans la liste de sections ci-dessus, signalés et non corrigés ici** (relèvent d'une passe de `PRD/TOC.md`, hors mandat de ce fichier) :
1. **§1.2 orphelin de glose** — cadres de référence et modèles de maturité (ISO 11354, EIF/EIRA, LISI, EIMM) sont couverts par l'intervalle « §1.0-1.6 » de la ligne Fusion mais absents de la phrase « Sections : … » ci-dessus.
2. **« exécution durable » reste nommée dans la phrase « Sections : … »** alors que la ligne Fusion la retire explicitement (le journal v0.6 déclare l'écart déjà corrigé côté ch. 1 — la liste de sections n'a pas été réalignée en conséquence).

### Chapitre 2 — Données, sémantique et ontologies

**Thèse** : l'interopérabilité sémantique — accord sur le sens, pas seulement sur le format — est le niveau que les protocoles agentiques présupposent et que peu savent établir.
Sections : formats, sérialisation, schémas et registres ; transformation, modèle canonique, contrats de données, formats de table ; pile du Web sémantique, médiation ontologique, graphe de connaissances d'entreprise ; LLM et automatisation de l'interopérabilité sémantique.
*Fusion : Vol. I* Monographie *§1.7-1.8. Aval agentique (§3.5) consolidé au Livre II (ch. 9).*

**Table des matières détaillée du chapitre 2**

*Dérivée de `Monographie.md` §1.7-1.8 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 2.1 — Formats d'échange, sérialisation, schémas et registres

- 2.1.1 Taxonomie des formats : texte vs binaire, document vs flux, *schema-on-read* / *schema-on-write* — *← §1.7.1.1*
- 2.1.2 Formats textuels et binaires : XML, JSON, YAML ; Protobuf, Avro — *← §1.7.1.2*
- 2.1.3 Formats analytiques et protocoles de connexion : Parquet, ORC, Arrow ; Flight SQL, ADBC — *← §1.7.1.3*
- 2.1.4 Schémas et validation : XSD, JSON Schema, IDL — *← §1.7.2.1*
- 2.1.5 Évolution et compatibilité : *backward*, *forward*, *full*, *transitive* — *← §1.7.2.2*
- 2.1.6 Registres de schémas dans l'architecture événementielle — *← §1.7.2.3*

#### § 2.2 — Transformation, modèle canonique, contrats de données et formats de table

- 2.2.1 Transformation et ponts inter-formats — *← §1.7.3.1*
- 2.2.2 Contrats de données et produits de données (*data mesh*) — *← §1.7.3.2*
- 2.2.3 Formats de table et catalogues interopérables : Iceberg, Delta, REST Catalog — *← §1.7.3.3*

#### § 2.3 — Pile du Web sémantique, médiation ontologique et graphe de connaissances d'entreprise

- 2.3.1 RDF, RDFS, OWL et JSON-LD — *← §1.8.1.1*
- 2.3.2 SPARQL et la fédération de sources — *← §1.8.1.2*
- 2.3.3 Validation et contrats sémantiques : SHACL et ShEx — *← §1.8.1.3*
- 2.3.4 Alignement ontologique et architectures de médiation — *← §1.8.2.1*
- 2.3.5 Graphe de connaissances, OBDA et MDM — *← §1.8.2.2*

#### § 2.4 — LLM et automatisation de l'interopérabilité sémantique

- 2.4.1 LLM pour la construction d'ontologies et l'appariement de schémas — *← §1.8.3.1*
- 2.4.2 GraphRAG : graphes au service de l'IA générative d'entreprise — *← §1.8.3.2*

⚠ *Le versant agentique de la sémantique (§3.5 du Vol. I : écart accord-de-protocole / compréhension, sémantique lue-par-le-modèle, ontologies de capacités, modes d'échec sémantiques) n'est pas repris ici — il est consolidé au ch. 9.*

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §1.7.1 | § 2.1.1-2.1.3 | condensé |
| §1.7.2 | § 2.1.4-2.1.6 | condensé |
| §1.7.3 | § 2.2 | condensé |
| §1.8.1 | § 2.3.1-2.3.3 | condensé |
| §1.8.2 | § 2.3.4-2.3.5 | condensé |
| §1.8.3 | § 2.4 | condensé |
| §3.5 | ch. 9 | hors périmètre (aval agentique) |

### Chapitre 3 — Sécurité, identité et gouvernance de l'interopérabilité

**Thèse** : le passage du périmètre réseau à la confiance par échange, et l'identité fédérée à autorisation déléguée, sont l'héritage IAM que la fabrique de confiance agentique (Livre III) étire jusqu'à rupture.
Sections : du périmètre à la confiance par échange ; identité fédérée, OAuth/OIDC, autorisation déléguée (**socle pré-agentique** — sa transposition aux agents est au ch. 13) ; zero-trust, identité de charge de travail (SPIFFE/SPIRE), confiance décentralisée ; gouvernance de l'intégration, cycle de vie des contrats, test/certification, observabilité comme condition opérationnelle.
*Fusion : Vol. I* Monographie *§1.9-1.10. **Chapitre-charnière dédoublonné** : pose le socle IAM classique une seule fois. Les ch. 13 (Livre III) et ch. 42 (Livre VII) **y renvoient sans le reconstruire** — ils n'héritent donc pas de §1.9.2 ni de §1.9.3, qui restent ici en entier. C'est la principale économie de la fusion côté identité, et elle n'a lieu que si ces deux chapitres s'y tiennent.*

**Table des matières détaillée du chapitre 3**

*Dérivée de `Monographie.md` §1.9-1.10 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 3.1 — Du périmètre réseau à la confiance par échange

- 3.1.1 Modèle de menace de l'intégration — *← §1.9.1.1*
- 3.1.2 OWASP API Security Top 10 et contrôles — *← §1.9.1.2*

#### § 3.2 — Identité fédérée et autorisation déléguée

**socle pré-agentique, posé ici une seule fois**

- 3.2.1 SAML, OAuth 2.x/2.1 et OpenID Connect — *← §1.9.2.1*
- 3.2.2 Jetons, anti-rejeu et profils à haute sécurité — *← §1.9.2.2*
- 3.2.3 Provisionnement et propagation de contexte — *← §1.9.2.3*

#### § 3.3 — Zero-trust, identité de charge de travail et confiance décentralisée

**socle pré-agentique, posé ici une seule fois**

- 3.3.1 Zero-trust et identité de charge de travail : SPIFFE/SPIRE, WIMSE — *← §1.9.3.1*
- 3.3.2 Identité décentralisée, eIDAS 2.0 et cryptographie post-quantique — *← §1.9.3.2*

#### § 3.4 — Gouvernance, test et observabilité de l'interopérabilité

- 3.4.1 Modèles de gouvernance et *policy-as-code* — *← §1.10.1.1*
- 3.4.2 Cycle de vie des contrats, SLA/SLO/SLI et application à l'exécution — *← §1.10.1.2*
- 3.4.3 Conformité vs interopérabilité ; *contract testing* piloté par le consommateur — *← §1.10.2.1*
- 3.4.4 Suites de certification et organismes de normalisation — *← §1.10.2.2*
- 3.4.5 Traçage distribué : OpenTelemetry et W3C Trace Context — *← §1.10.3.1*
- 3.4.6 Auditabilité et conformité réglementaire des intégrations — *← §1.10.3.2*

⚠ **L'économie de fusion tient à ce que les §3.2 et §3.3 ne soient reconstruits nulle part ailleurs.** Renvois entrants attendus, sans reprise : ch. 13 (transposition d'OAuth/OIDC/SCIM aux agents), ch. 14 (identité décentralisée agentique : VC, DID), ch. 42 (zero-trust au grain de l'infrastructure), ch. 23-24 (horloge post-quantique — le §3.3.2 n'en pose que le socle pré-agentique), ch. 43 (observabilité agentique, OTel GenAI).

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §1.9.1 | § 3.1 | condensé |
| §1.9.2 | § 3.2 | **en entier — non hérité par les ch. 13 et 42** |
| §1.9.3 | § 3.3 | **en entier — non hérité par les ch. 13 et 42** |
| §1.10.1 | § 3.4.1-3.4.2 | condensé |
| §1.10.2 | § 3.4.3-3.4.4 | condensé |
| §1.10.3 | § 3.4.5-3.4.6 | condensé |

### Chapitre 4 — L'ingénierie des systèmes agentiques : anatomie, raisonnement, outils

**Thèse** : l'agent est un LLM augmenté d'une boucle perception-raisonnement-action-observation ; son ingénierie est une discipline distincte du prompt, gouvernée par des régimes de contrôle et des niveaux d'autonomie.
Sections : de l'agent conversationnel à l'agent qui agit ; cadre de l'agent rationnel (PEAS, BDI, MAS) ; architectures de boucle mono-agent, séparation contrôleur/exécuteur ; raisonnement, planification, test-time compute ; utilisation d'outils et **MCP comme protocole agent-outil** (anatomie détaillée reportée au ch. 8) ; **choix et service du modèle comme décision d'ingénierie** (§2.8.5, reçu du ch. 6).
*Fusion : Vol. I* Monographie *§2.1-2.5. L'anatomie protocolaire de MCP (§2.5.4) est **consolidée au ch. 8** ; ici, seul l'usage d'outils au niveau ingénierie.*

**Table des matières détaillée du chapitre 4**

*Dérivée de `Monographie.md` §2.1-2.5 et §2.8.5 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 4.0 — Introduction : de l'agent conversationnel à l'agent qui agit

- 4.0.1 Du LLM conversationnel à l'agent qui agit sur le monde — *← §2.1.1*
- 4.0.2 Le double public et l'angle d'ingénierie dominant — *← §2.1.2 ; les encadrés* Perspective recherche *et* Mise en œuvre *sont l'instrument de ce double public (avant-propos)*
- *§2.1.3 (carte du chapitre source) : apparat de navigation, refondu à l'échelle de la somme — pas de section propre.*

#### § 4.1 — Fondements et définitions de l'IA agentique

- 4.1.1 Qu'est-ce qu'un agent ? Définition canonique, boucle perception-action-but ; agent vs IA agentique — *← §2.2.1.1-2.2.1.2*
- 4.1.2 Le cadre de l'agent rationnel : PEAS et typologies — *← §2.2.2*
- 4.1.3 Héritages théoriques : BDI ; MAS classiques, MDP/POMDP et lignée RL — *← §2.2.3.1-2.2.3.2*
- 4.1.4 Agent, workflow, automatisation : régimes de contrôle et niveaux d'autonomie — *← §2.2.4* ⚠ **garde-fou R-13 du Vol. III** : c'est le **continuum 0-5**, l'une des trois échelles distinctes du Vol. I — ne jamais écrire « l'autonomie graduée du Vol. I » sans préciser laquelle
- 4.1.5 La frontière des capacités 2024-2026 : cadrage qualitatif — *← §2.2.5*

#### § 4.2 — Architectures d'agent et boucle agentique

- 4.2.1 Le LLM augmenté et la boucle perception-raisonnement-action-observation — *← §2.3.1*
- 4.2.2 Architectures cognitives en héritage : SOAR, ACT-R, CoALA — *← §2.3.2*
- 4.2.3 Patrons de boucle mono-agent : ReAct ; Plan-and-Execute et ReWOO ; Reflexion ; CodeAct — *← §2.3.3.1-2.3.3.4*
- 4.2.4 Séparation contrôleur/exécuteur et critères de choix d'architecture — *← §2.3.4*

#### § 4.3 — Raisonnement, planification et calcul à l'inférence

- 4.3.1 Du raisonnement linéaire à la recherche structurée — *← §2.4.1*
- 4.3.2 Recherche guidée et vérificateurs à l'inférence — *← §2.4.2*
- 4.3.3 Décomposition et planification : PDDL et limites des LLM planificateurs ; approches hybrides — *← §2.4.3.1-2.4.3.2*
- 4.3.4 Modèles de raisonnement et *test-time compute* : contrôler le budget ; fidélité et monitorabilité de la chaîne — *← §2.4.4.1-2.4.4.2*
- 4.3.5 Entraînement et auto-amélioration des agents — *← §2.4.5*

#### § 4.4 — Utilisation d'outils et accès aux outils

- 4.4.1 Appel de fonctions et apprentissage de l'usage d'outils — *← §2.5.1*
- 4.4.2 Sélection, orchestration et conception d'outils fiables — *← §2.5.2*
- 4.4.3 Outils universels : exécution de code, *computer use* et agents GUI ; ancrage visuel ; agents de navigateur — *← §2.5.3.1-2.5.3.2*
- 4.4.4 Robustesse de la boucle d'outillage et évaluation — *← §2.5.5*

#### § 4.5 — Choix et service du modèle comme décision d'ingénierie

*← §2.8.5, **arrivée depuis le ch. 6** (seule perte silencieuse trouvée à la collation v0.5)*

⚠ *Le §2.5.4 (protocole agent-outil : primitives, transports, révisions ; registres, passerelles et découverte d'entreprise) n'est **pas** traité ici — il part en entier au ch. 8. Ce chapitre s'arrête à l'usage d'outils au niveau ingénierie.*

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §2.1 | § 4.0 | condensé ; §2.1.3 refondu en apparat |
| §2.2 | § 4.1 | condensé |
| §2.3 | § 4.2 | condensé |
| §2.4 | § 4.3 | condensé |
| §2.5.1-2.5.3, §2.5.5 | § 4.4 | condensé |
| §2.5.4 | ch. 8 | déplacé en entier |
| §2.8.5 | § 4.5 | **arrivée**, déclarée au ch. 6 |

⚠ **Écart résolu en v0.17** — l'arrivée du §2.8.5 n'était déclarée qu'à son **départ** (ligne Fusion du ch. 6) : la phrase « Sections : … » de ce chapitre la porte désormais. Un chapitre rédigé sur la seule liste de sections aurait sinon perdu la section que la v0.5 avait précisément sauvée — **une arrivée se déclare aux deux bouts**.

### Chapitre 5 — Ancrage informationnel : mémoire, contexte, RAG agentique

**Thèse** : l'agent persistant se construit par l'ingénierie du contexte et une pile de récupération gouvernée. ⚠ **L'empoisonnement de la mémoire et des sources n'est pas traité ici** : les §2.6-2.7 du Vol. I n'en portent aucune occurrence — la matière vit au §2.10.2, déjà affectée au ch. 20, qui la relit comme un risque d'identité des *sources*. Ce chapitre pose l'ancrage ; le ch. 20 en pose le versant hostile.
Sections : taxonomie de la mémoire, ingénierie du contexte ; architectures de mémoire long terme ; RAG agentique (planifier-récupérer-critiquer-itérer) ; données structurées, accès d'entreprise, gouvernance d'ancrage.
*Fusion : Vol. I* Monographie *§2.6-2.7. Le versant sécurité (empoisonnement) renvoie au ch. 20 (Livre III, versant hostile).*

**Table des matières détaillée du chapitre 5**

*Dérivée de `Monographie.md` §2.6-2.7 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 5.1 — Du LLM sans état à l'agent persistant : mémoire et ingénierie du contexte

- 5.1.1 Taxonomie de la mémoire — *← §2.6.1*
- 5.1.2 L'ingénierie du contexte comme discipline — *← §2.6.2*
- 5.1.3 Compaction réversible, résumé et oubli actif — *← §2.6.2.1*
- 5.1.4 Mémoire procédurale et fichiers de configuration d'agent — *← §2.6.2.2*

#### § 5.2 — Architectures de mémoire long terme et pile de récupération

- 5.2.1 Architectures de mémoire long terme et pile de récupération — *← §2.6.3*
- 5.2.2 Consolidation, ancrage et évaluation de la mémoire — *← §2.6.4*

#### § 5.3 — RAG agentique : planifier-récupérer-critiquer-itérer

- 5.3.1 Du RAG statique au RAG agentique — *← §2.7.1*
- 5.3.2 Stratégies de récupération, ingestion et structures — *← §2.7.2*

#### § 5.4 — Données structurées, accès d'entreprise et gouvernance d'ancrage

- 5.4.1 Données structurées et accès d'entreprise — *← §2.7.3*
- 5.4.2 Gouvernance d'accès, ancrage et évaluation — *← §2.7.4*

⚠ **Aucune sous-section d'empoisonnement ici, et c'est un constat de source, non un oubli.** Les §2.6-2.7 du Vol. I n'en portent aucune occurrence ; la matière vit au §2.10.2.2 (empoisonnement d'outils, de données et de mémoire), déjà affecté au ch. 20, qui la relit comme un risque d'identité des *sources*. Ce chapitre pose l'ancrage ; le ch. 20 en pose le versant hostile.

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §2.6.1-2.6.2 | § 5.1 | condensé |
| §2.6.3-2.6.4 | § 5.2 | condensé |
| §2.7.1-2.7.2 | § 5.3 | condensé |
| §2.7.3-2.7.4 | § 5.4 | condensé |
| §2.10.2.2 | ch. 20 | hors périmètre (versant hostile) |

### Chapitre 6 — Systèmes multi-agents, évaluation et sûreté

**Thèse** : le multi-agent a un surcoût que seuls certains gains justifient ; son évaluation (succès de tâche vs trajectoire) et sa sûreté (triade létale, vecteurs d'attaque) sont les deux fronts encore ouverts.
Sections : pourquoi le multi-agent, topologies, raisonnement collectif ; communication inter-agents (A2A/ACP — anatomie au ch. 8) ; frameworks d'orchestration et frontière déterministe/agentique (**consolidé au ch. 27**) ; évaluation, LLM-comme-juge, bancs d'essai, red-teaming (la mise en œuvre en production est au ch. 44) ; défense architecturale, garde-fous d'exécution et alignement (**le modèle de menace et les vecteurs d'attaque sont consolidés au ch. 20** — §2.10.1-2.10.2 ; ce chapitre pose la défense, pas la menace).
*Fusion : Vol. I* Monographie *§2.8-2.10, **partagé explicitement** : §2.8.1-2.8.3 et §2.9.1-2.9.5 restent ici ; §2.8.4 (frameworks) fusionne au ch. 27 ; **§2.8.5 (choix et service du modèle comme décision d'ingénierie) part au ch. 4** — section restée sans destination ni coupe assumée jusqu'à la v0.5, seule perte silencieuse trouvée à la collation contre les volumes complets ; §2.9.6 (observabilité, OTel GenAI) part au ch. 43 ; §2.10.1-2.10.2 (modèle de menace, vecteurs) partent au ch. 20 ; §2.10.3-2.10.5 (défense architecturale, garde-fous d'exécution, alignement) restent ici, le ch. 42 les reprenant au grain de l'infrastructure. Le §2.11.3 (gouvernance par les normes) part au ch. 34, les §2.11.4-2.11.5 (HITL opérationnel, réponse aux incidents, AIOps agentique) au ch. 44, le §2.13.1 (grille « quand agentifier ») au ch. 47 et le §2.13.2 (questions ouvertes) au ch. 56. Coupe assumée : §2.12 (applications et tendances 2024-2026 — remplacé par les Livres VI et X).*

**Table des matières détaillée du chapitre 6**

*Dérivée de `Monographie.md` §2.8-2.10 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 6.1 — Pourquoi le multi-agent : gains, surcoût, topologies

- 6.1.1 Gains, surcoût et fondements classiques — *← §2.8.1*
- 6.1.2 Topologies, rôles et raisonnement collectif — *← §2.8.2*

#### § 6.2 — Communication inter-agents : A2A, ACP et pile d'interopérabilité

*← §2.8.3 ; l'anatomie protocolaire est au ch. 8, la pile au ch. 9*

#### § 6.3 — Évaluation et bancs d'essai

- 6.3.1 Pourquoi évaluer un agent est difficile : succès de tâche vs trajectoire — *← §2.9.1*
- 6.3.2 LLM-comme-juge : principes, biais et *reward hacking* — *← §2.9.2*
- 6.3.3 Bancs d'essai de capacité : codage, web et bureautique ; raisonnement général, outils et tâches d'entreprise — *← §2.9.3.1-2.9.3.2*

#### § 6.4 — Sûreté, red-teaming et taxonomie d'échecs

- 6.4.1 Évaluation de la sûreté et red-teaming agentique — *← §2.9.4*
- 6.4.2 Fiabilité, coût et taxonomie d'échecs — *← §2.9.5*

#### § 6.5 — Défense architecturale, garde-fous et alignement

- 6.5.1 Référentiels et patrons de défense architecturale — *← §2.10.3 ; **posés ici**, appliqués au grain de l'infrastructure au ch. 42*
- 6.5.2 Garde-fous d'exécution et chaîne d'approvisionnement — *← §2.10.4 ; même partage déclaré avec le ch. 42*
- 6.5.3 Alignement, comportement déviant et asymétrie attaquant/défenseur — *← §2.10.5*

**Table de couverture (décision 6)** — ce chapitre est le dernier à consommer le ch. 2 du Vol. I ; sa ligne Fusion porte la ventilation de tout le reste du chapitre source.

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §2.8.1-2.8.2 | § 6.1 | condensé |
| §2.8.3 | § 6.2 | condensé |
| §2.8.4 | ch. 27 | déplacé (frameworks d'orchestration) |
| §2.8.5 | ch. 4 | déplacé (§ 4.5) |
| §2.9.1-2.9.3 | § 6.3 | condensé |
| §2.9.4-2.9.5 | § 6.4 | condensé |
| §2.9.6 | ch. 43 | déplacé — **seule affectation**, non conservé ici |
| §2.10.1-2.10.2 | ch. 20 | déplacé (modèle de menace, vecteurs) |
| §2.10.3-2.10.4 | § 6.5.1-6.5.2 + ch. 42 | **partagé déclaré** : posés ici, appliqués là |
| §2.10.5 | § 6.5.3 | condensé |
| §2.11.1 | Livre VII | hors périmètre (modèle de coût) |
| §2.11.2 | ch. 18 | hors périmètre (chaînes multi-saut) |
| §2.11.3 | ch. 34 | hors périmètre (gouvernance par les normes) |
| §2.11.4-2.11.5 | ch. 44 | hors périmètre (HITL, incidents, AIOps) |
| §2.12 | — | coupe assumée (Livres VI et X) |
| §2.13.1 | ch. 47 | hors périmètre (grille « quand agentifier ») |
| §2.13.2 | ch. 56 | hors périmètre (questions ouvertes) |

⚠ **Écart résolu en v0.17** — la phrase « Sections : … » annonçait « modèle de menace, vecteurs d'attaque » alors que la ligne Fusion les envoie au ch. 20 (§2.10.1-2.10.2) ; elle est réalignée et porte le renvoi. Même classe que « exécution durable » au ch. 1, résolu de même : **quand une ligne Fusion est corrigée, la liste de sections se réaligne dans la même passe**.

---

## LIVRE II — Couche protocolaire agentique

*(fusionne Vol. I ch. 3 — hors §3.6, consolidé au Livre III — + Vol. II Partie I ; ~25 000 mots)*

### Chapitre 7 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts

**Thèse** : en dix-sept mois, la couche protocolaire agentique s'est consolidée sous gouvernance neutre (Linux Foundation) — condition **nécessaire et non suffisante** de sa crédibilité en entreprise réglementée (formulation du ch. 1 du Vol. II, que les v0.1-v0.5 amputaient de sa restriction) ; mais « soutien ≠ production » et AP2 n'a aucun transfert de gouvernance documenté (⚠ relève v0.7 : fait nouveau candidat, don à la FIDO Alliance annoncé au 28 avril 2026 — instruit au ch. 10, thèse à réviser si la source primaire se confirme).
Sections : définition et niveaux de l'interopérabilité agentique (LCIM appliqué aux agents, taxonomie des quatre axes) ; chronologie 2024-2026 (⚠ **par protocole, non par date** : MCP nov. 2024 ; **AGNTCY mars 2025, antérieur à A2A avril 2025** ; passages sous fondation dans l'ordre inverse — A2A juin 2025, AGNTCY 29 juill. 2025, MCP déc. 2025. La flèche « MCP → A2A → AGNTCY » des v0.1-v0.5 était fausse dans les deux lectures) ; gouvernance comparée des fondations ; **encadré de désambiguïsation R-8** (collision « (agentic) control plane » à quatre branches) ; lecture critique des métriques d'adoption (**PRD Vol. II §8.2.1** : « soutien ≠ production »).
*Fusion : Vol. II ch. 1 (charpente) + Vol. I* Monographie *§3.0-3.1 (fondements et quatre axes — socle amont de la grille du ch. 15) + §3.13.1 (fondations neutres : AAIF, FIDO). ⚠ Le reste du §3.13 (coexistence/souveraineté, programme de recherche sémantique, synthèse) et le §7.3 (bifurcation de la gouvernance par couche : AAIF, FIDO, W3C, IETF, DIF) vont au **ch. 55** — ne pas les traiter deux fois. Socle : F-01, F-02, F-04, F-05, F-43. Garde-fous : R-1, R-8. **Lacune héritée portée : PRD Vol. II §10.7** — la quatrième branche de R-8 (composante ACP d'AGNTCY) n'est établie par le socle ni dans son intitulé complet ni dans son identité avec l'ACP d'IBM Research : encadré, sans la combler ; renvoi ch. 56.*

**Table des matières détaillée du chapitre 7**

*Dérivée de `Monographie.md` §3.0-3.1 et §3.13.1 (Vol. I) et de `Monographie.md` ch. 1 (Vol. II) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 7.0 — Introduction : de l'échange de données à l'échange d'intentions

*← Vol. I §3.0.1 (positionnement et proposition directrice). Les §3.0.2 (mode d'emploi, conventions, nomenclature) et §3.0.3 (double public, fil analytique) sont absorbés à l'avant-propos de la somme — apparat de chapitre source, sans section propre ici.*

#### § 7.1 — Définir l'interopérabilité agentique et ses niveaux

- 7.1.1 Définition de travail — *← Vol. I §3.1.1*
- 7.1.2 Les niveaux LCIM appliqués aux agents : technique, syntaxique, sémantique, pragmatique, dynamique — *← Vol. I §3.1.2*
- 7.1.3 Pragmatique (L4) et dynamique (L5) : niveaux existants devenus verrous opérationnels — *← Vol. I §3.1.2.1*
- 7.1.4 Ce qui change quand les acteurs sont autonomes, non déterministes et pilotés par LLM — *← Vol. I §3.1.3*
- 7.1.5 Reformuler la triade contrat / découplage / évolution pour des acteurs probabilistes — *← Vol. I §3.1.4 ; l'invariant est posé à l'avant-propos et éprouvé au ch. 1*
- 7.1.6 Pourquoi l'interop classique (RPC/API/ESB) ne suffit pas : l'argument de l'étagement — *← Vol. I §3.1.5 ; le socle classique est aux ch. 1 et 3*

#### § 7.2 — Filiation historique et taxonomie des quatre axes

- 7.2.1 KQML, FIPA-ACL, actes de langage et protocoles à engagements — *← Vol. I §3.1.6*
- 7.2.2 Taxonomie structurante des quatre axes d'interopérabilité — *← Vol. I §3.1.7 ; **socle amont de la grille des cinq questions du ch. 15***
- 7.2.3 Panorama introductif des modes d'échec — *← Vol. I §3.1.8 ; la taxonomie complète est au ch. 11*

#### § 7.3 — Chronologie 2024-2026 : dix-sept mois de consolidation

*← Vol. II §1.1.* ⚠ **Ordonner par protocole, non par date de lancement** : MCP nov. 2024 ; **AGNTCY mars 2025, antérieur à A2A avril 2025** ; passages sous fondation dans l'ordre inverse (A2A juin 2025, AGNTCY 29 juill. 2025, MCP déc. 2025). La flèche « MCP → A2A → AGNTCY » des v0.1-v0.5 était fausse dans les deux lectures.

#### § 7.4 — Gouvernance comparée : ce que « neutre » veut dire

- 7.4.1 Gouvernance comparée des fondations — *← Vol. II §1.2*
- 7.4.2 Les fondations neutres : AAIF (Linux Foundation) et FIDO Alliance — *← Vol. I §3.13.1 — **seule part du §3.13 reçue ici** ; §3.13.2-3.13.4 vont au ch. 55*

#### § 7.5 — Encadré de désambiguïsation R-8 : la collision « (agentic) control plane » à quatre branches

*← Vol. II ch. 3 §3.4 (versant protocolaire).* ⚠ **Lacune héritée portée (PRD Vol. II §10.7)** : la quatrième branche (composante ACP d'AGNTCY) n'est établie par le socle ni dans son intitulé complet ni dans son identité avec l'ACP d'IBM Research — encadrer sans combler ; renvoi ch. 56.

#### § 7.6 — Lecture critique des métriques d'adoption : « soutien » n'est pas « production »

*← Vol. II §1.3 + son bloc « Ce que ce chapitre établit, et ce qu'il ne dit pas » (PRD Vol. II §8.2.1).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. I §3.0 | § 7.0 | condensé ; §3.0.2-3.0.3 absorbés à l'avant-propos |
| Vol. I §3.1.1-3.1.5 | § 7.1 | condensé |
| Vol. I §3.1.6-3.1.8 | § 7.2 | condensé |
| Vol. I §3.13.1 | § 7.4.2 | seule part du §3.13 reçue ici |
| Vol. I §3.13.2-3.13.4 | ch. 55 | hors périmètre |
| Vol. I §7.3 | ch. 55 | hors périmètre (bifurcation de la gouvernance par couche) |
| Vol. II §1.1 | § 7.3 | condensé |
| Vol. II §1.2 | § 7.4.1 | condensé |
| Vol. II §1.3 + clôture | § 7.6 | condensé |
| Vol. II §3.4 | § 7.5 | **siège de l'encadré R-8** (voir écart) |

⚠ **Écart résolu en v0.17** — le §3.4 du ch. 3 du Vol. II (*Le versant protocolaire de la désambiguïsation (R-8)*) était revendiqué implicitement par **deux** chapitres, le ch. 10 absorbant « Vol. II ch. 3 » en bloc. **Le siège est ici**, et la liste de sections du ch. 10 porte désormais son renvoi explicite au § 7.5 sans reconstruire l'encadré (décision 6).

### Chapitre 8 — Anatomie : MCP (agent-outil) et A2A (agent-agent)

**Thèse** : « MCP dans les agents, A2A entre les agents » — doctrine de complémentarité **déclarée par le projet A2A** (non un accord des deux projets) qui fournit le premier critère de découpage architectural, sans le contraindre.
Sections : MCP (JSON-RPC 2.0, cadre d'autorisation OAuth — « cadre », jamais « sécurisé » ; révision 2025-11-25 ; ⚠ **RC 2026-07-28, relève v0.7** : gelée le 21 mai 2026, ratification annoncée pour le 28 juillet 2026 — cœur **sans état** (fin de la poignée de main et de l'en-tête de session), extensions (Tasks, MCP Apps), durcissement de l'autorisation aligné OAuth/OIDC, politique de dépréciation à cycle de vie (Active/Deprecated/Removed, ≥ 12 mois entre dépréciation et retrait) ; rupture **annoncée** portant des changements cassants — l'anatomie décrite ici est celle de 2025-11-25, à revalider en bloc au gel, sources primaires à extraire) ; A2A v1.0 (Agent Cards signées, multi-protocole, multi-location) ; **ANP** (identité décentralisée, sémantique web, négociation méta-protocole) et **ACP-agent : la mécanique de sa fusion dans A2A** — ⚠ **partage déclaré avec le ch. 10** (décision 2) : la *mécanique* de la convergence se traite ici, sur le Vol. I *Monographie* §3.3.4 ; la *portée de risque* de cette fusion (R-1 du Vol. II, séquencement périmé) se traite au ch. 10, sur le Vol. II ch. 3 §3.3 — ni l'un ni l'autre ne reconstruit ce que porte son voisin ; intégrations infonuagiques (Azure/AWS/Google Cloud).
*Fusion : Vol. I* Monographie *§3.2-3.3 + §2.5.4 + Vol. II ch. 2. Socle : F-01, F-02, F-03, F-16. Garde-fous : réserve F-01. **Lacune héritée portée : PRD Vol. II §10.9** — ancrage de confiance des *Signed Agent Cards*, date de la v1.0, multi-location et inventaire infonuagique de MCP ne sont pas au socle ; renvoi ch. 56.*

**Table des matières détaillée du chapitre 8**

*Dérivée de `Monographie.md` §3.2-3.3 et §2.5.4 (Vol. I) et de `Monographie.md` ch. 2 (Vol. II) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 8.1 — MCP comme couche de contrat : problème N×M, primitives, transports

- 8.1.1 Le problème N×M et la critique du slogan « USB-C » — *← Vol. I §3.2.1*
- 8.1.2 Architecture et primitives, sous l'angle de la bidirectionnalité négociée — *← Vol. I §3.2.2 + §2.5.4.1*
- 8.1.3 Transports et trajectoire du couplage vers le découplage : de stdio au cœur sans état — *← Vol. I §3.2.3*
- 8.1.4 Une interface d'outillage assortie d'un **cadre** d'autorisation — *← Vol. II §2.1 ; **réserve F-01** : « cadre d'autorisation », jamais « sécurisé »*

#### § 8.2 — MCP : jalons datés, autorisation et sémantique des résultats

- 8.2.1 Les cinq jalons datés : trajectoire de maturation d'un standard — *← Vol. I §3.2.4*
- 8.2.2 Autorisation et identité : OAuth 2.1 et le serveur MCP comme *Resource Server* — *← Vol. I §3.2.5*
- 8.2.3 Vers une sémantique des résultats : sorties structurées, schémas et *Tasks* (expérimental) — *← Vol. I §3.2.6*

⚠ **Relève v0.7 — la RC 2026-07-28 périme cette anatomie** : gelée le 21 mai 2026, ratification annoncée pour le 28 juillet 2026 — cœur **sans état**, extensions (Tasks, MCP Apps), durcissement de l'autorisation, politique de dépréciation à cycle de vie. L'anatomie décrite ici est celle de **2025-11-25**, à revalider en bloc au gel, sources primaires à extraire.

#### § 8.3 — MCP : conformité, registre, dépréciation et gouvernance

- 8.3.1 Du projet Anthropic à l'AAIF : conformité, registre, dépréciation — *← Vol. I §3.2.7*
- 8.3.2 Registres, passerelles et découverte d'entreprise — *← Vol. I §2.5.4.2 ; **versant outillage seul** — la pile protocolaire est au ch. 9, les registres gouvernés au ch. 16*

#### § 8.4 — A2A v1.0 : la délégation entre pairs

- 8.4.1 Du Contract Net à FIPA-ACL : patrons d'interaction transposés aux agents LLM — *← Vol. I §3.3.1*
- 8.4.2 A2A v1.0 : Agent Card signée, modèle de tâche et structure des messages — *← Vol. I §3.3.2 + Vol. II §2.2*
- 8.4.3 Délégation de tâches et collaboration inter-cadriciels ; multi-protocole et multi-location — *← Vol. I §3.3.3*

#### § 8.5 — ACP-agent, ANP et l'état de la standardisation

- 8.5.1 ACP-agent (IBM/BeeAI) et sa fusion dans A2A : la convergence par fusion — *← Vol. I §3.3.4* ⚠ voir écart
- 8.5.2 ANP : identité décentralisée, sémantique web et négociation méta-protocole — *← Vol. I §3.3.5* ⚠ voir écart
- 8.5.3 Comparaison, convergence et état de la standardisation (juin 2026) — *← Vol. I §3.3.6*

#### § 8.6 — La frontière MCP/A2A : une complémentarité déclarée, et par qui

- 8.6.1 Limites de MCP et frontière avec A2A ; modes d'échec de MCP — *← Vol. I §3.2.8*
- 8.6.2 Négociation, coordination et modes d'échec propres à l'agent-agent — *← Vol. I §3.3.7 ; taxonomie complète au ch. 11*
- 8.6.3 « MCP dans les agents, A2A entre les agents » : doctrine **déclarée par le projet A2A**, non accord des deux projets — *← Vol. II §2.4*

#### § 8.7 — Les intégrations infonuagiques : lire le statut, pas la présence

*← Vol. II §2.3 (Azure, AWS, Google Cloud) + le bloc « Ce que ce chapitre établit, et ce qu'il ne dit pas ».*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. I §3.2.1-3.2.3 | § 8.1 | condensé |
| Vol. I §3.2.4-3.2.6 | § 8.2 | condensé |
| Vol. I §3.2.7 | § 8.3.1 | condensé |
| Vol. I §3.2.8 | § 8.6.1 | condensé |
| Vol. I §3.3.1-3.3.3 | § 8.4 | condensé |
| Vol. I §3.3.4-3.3.6 | § 8.5 | condensé |
| Vol. I §3.3.7 | § 8.6.2 | condensé |
| Vol. I §2.5.4 | § 8.1.2 et § 8.3.2 | **arrivée** depuis le ch. 4 |
| Vol. II §2.1 | § 8.1.4 | condensé |
| Vol. II §2.2 | § 8.4.2 | condensé |
| Vol. II §2.3 | § 8.7 | condensé |
| Vol. II §2.4 | § 8.6.3 | condensé |
| Vol. I §3.6 | Livre III | hors périmètre (en-tête du Livre II : « hors §3.6 ») |

⚠ **Deux écarts résolus en v0.17.**
1. **La fusion d'ACP était revendiquée par deux chapitres.** Le ch. 8 reçoit Vol. I §3.3.4 (« ACP-agent et sa fusion dans A2A ») et l'annonce dans sa liste de sections ; le ch. 10 reçoit Vol. II §3.3 (« Le destin de l'ACP protocolaire ») et l'annonce aussi (« le destin d'ACP — plus haut risque R-1 »). Même objet, deux sources, deux chapitres : c'est exactement ce que la **décision 2 (déduplication)** proscrit. Le partage doit être déclaré (p. ex. mécanique de la fusion ici, portée de risque au ch. 10) ou l'un des deux doit renvoyer à l'autre.
2. **ANP n'était nommé ni au titre ni à la liste de sections** du ch. 8, alors que le §3.3.5 y arrive par l'intervalle « §3.2-3.3 » de la ligne Fusion — même classe que le §1.2 au ch. 1, couvert sans être glosé. **La liste de sections le porte désormais.** ⚠ *Le **titre** du chapitre reste « MCP (agent-outil) et A2A (agent-agent) » : le retoucher déplacerait un renvoi cité en clair dans huit chapitres, et ANP y est traité comme un tiers comparé, non comme un objet du même rang — l'écart de titre est **assumé et déclaré**, non oublié.*

### Chapitre 9 — Découverte, registres, portabilité et pile protocolaire

**Thèse** : la découverte et le nommage des agents, et la portabilité inter-modèles/inter-cadriciels, sont les propriétés que l'étagement de la pile protocolaire rend possibles — ou trahit.
Sections : découverte, registres et nommage (pont vers ch. 16) ; la pile de protocoles agentiques et son étagement ; portabilité inter-modèles et inter-cadriciels ; interopérabilité sémantique des agents (de l'accord-de-protocole à la compréhension) ; test de conformité et certification des protocoles ; ⚠ **relève v0.11 — la généralisation de la pile a un nom de scène et un programme normatif** : une préimpression de juillet 2025 nomme « web agentique » le régime où l'interaction machine-à-machine devient le cas nominal du web et l'ordonne en trois dimensions — intelligence, interaction, économie (arXiv 2507.21206) ; une préimpression de juin 2026 soutient que ce régime exige une infrastructure **normative** neuve, l'accès des agents aux plateformes pour le compte d'utilisateurs n'étant réglé ni par le droit ni par les mécanismes de gouvernance existants (arXiv 2606.10711). Préimpressions non révisées par les pairs, résumés seuls consultés : cadre de nommage candidat pour la trajectoire du ch. 55, jamais un fait d'adoption.
*Fusion : Vol. I* Monographie *§3.4, §3.5, §3.7-3.8 + §3.12 (conformité protocolaire ; la propagation de trace inter-agents §3.12.3 part au ch. 43). Les registres gouvernés (versant identité/conformité) sont **consolidés au ch. 16** ; ici, le versant protocolaire seul.*

**Table des matières détaillée du chapitre 9**

*Dérivée de `Monographie.md` §3.4, §3.5, §3.7-3.8 et §3.12 (Vol. I) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 9.1 — Découverte, registres et nommage des agents et des outils

**versant protocolaire seul**

- 9.1.1 La leçon d'UDDI : la récurrence annuaire → registre de services → registre d'agents — *← §3.4.1*
- 9.1.2 Le problème de découverte propre aux agents : trois moments — *← §3.4.2*
- 9.1.3 Auto-description et catalogues fédérés : Agent Card, OASF, MCP Registry — *← §3.4.3*
- 9.1.4 Annuaires, services de noms et registres d'identité : AGNTCY ADS, ANS, W3C Agent Identity Registry — *← §3.4.4*
- 9.1.5 Marketplaces, gouvernance et modes d'échec des registres — *← §3.4.5*

⚠ *Le §3.4 est **partagé déclaré** avec le ch. 16, qui prend le versant identité/conformité (registres gouvernés). Pont, pas reprise.*

#### § 9.2 — La pile de protocoles agentiques et son étagement

- 9.2.1 Pourquoi une « pile » : du protocole isolé au modèle en couches — *← §3.7.1*
- 9.2.2 Analogie OSI/TCP-IP et ses limites : propositions Agent-OSI — *← §3.7.2*
- 9.2.3 Les couches transversales : positionnement par renvoi (anti-catalogue) — *← §3.7.3*
- 9.2.4 Composition de la pile : comment MCP, A2A, agent-humain et règlement s'emboîtent — *← §3.7.4*
- 9.2.5 Matrice de maturité et de décision (livrable praticien, juin 2026) — *← §3.7.5*

#### § 9.3 — Portabilité inter-modèles et inter-cadriciels

- 9.3.1 L'API « compatible OpenAI » comme standard de fait et le paradoxe du *lock-in* inverse — *← §3.8.1*
- 9.3.2 Fragmentation des formats et passerelles de médiation (LiteLLM, gateways) — *← §3.8.2*
- 9.3.3 Interopérabilité des cadriciels par protocoles partagés — *← §3.8.3*
- 9.3.4 Portabilité de la configuration et de la définition d'agent : AGENTS.md, Agent Spec — *← §3.8.4*
- 9.3.5 Neutralité par fondation : l'AAIF comme mécanisme anti-fragmentation — *← §3.8.5 ; la gouvernance comparée est au ch. 7*

#### § 9.4 — Interopérabilité sémantique des agents : de l'accord-de-protocole à la compréhension

- 9.4.1 L'écart accord-de-protocole vs compréhension-sémantique — *← §3.5.1*
- 9.4.2 La sémantique lue-par-le-modèle : descriptions d'outils et écart description/comportement — *← §3.5.2*
- 9.4.3 Ontologies de capacités, d'intentions et de tâches ; ancrage (*grounding*) — *← §3.5.3*
- 9.4.4 Le LLM comme couche de médiation sémantique : appariement d'ontologies — *← §3.5.4 ; le socle pré-agentique est au ch. 2*
- 9.4.5 Modes d'échec d'origine sémantique — *← §3.5.5 ; taxonomie complète au ch. 11*

#### § 9.5 — Test de conformité et certification des protocoles

- 9.5.1 Du test de conformité d'API à la conformité des protocoles d'agents : définir « interopérable » — *← §3.12.1*
- 9.5.2 Suites de conformité MCP, validation d'Agent Cards et test de la négociation — *← §3.12.2*
- 9.5.3 Bancs inter-agents et vers une certification des protocoles — *← §3.12.4*

⚠ **Relève v0.11, à instruire à la source primaire** — la généralisation de la pile a un nom de scène et un programme normatif : « web agentique » comme régime où l'interaction machine-à-machine devient le cas nominal (arXiv 2507.21206, trois dimensions : intelligence, interaction, économie) ; exigence d'une infrastructure **normative** neuve (arXiv 2606.10711). **Préimpressions non révisées par les pairs, résumés seuls consultés** : cadre de nommage candidat pour la trajectoire du ch. 55, jamais un fait d'adoption.

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §3.4 | § 9.1 + ch. 16 | **partagé déclaré** : protocolaire ici, gouverné là |
| §3.5 | § 9.4 | condensé |
| §3.7 | § 9.2 | condensé |
| §3.8 | § 9.3 | condensé |
| §3.12.1-3.12.2, §3.12.4 | § 9.5 | condensé |
| §3.12.3 | ch. 43 | déplacé (propagation W3C Trace Context) |

### Chapitre 10 — Transaction et infrastructure : AP2 et AGNTCY

**Thèse** *(deux énoncés de statut inégal, à ne pas fondre)* : que la transaction pilotée par agents (AP2) soit l'**aboutissement financier** de la pile est une **lecture d'auteur** — le socle établit qu'AP2 est un protocole compagnon d'A2A, rien de plus sur sa centralité ; qu'AGNTCY soit une couche d'infrastructure **et non un concurrent** est le **positionnement officiel déclaré du projet**, une déclaration et non un fait vérifié, que des analyses tierces nuancent.
Sections : AP2 (60+ organisations financières — endossement, pas production ; anatomie non documentée au socle, lacune assumée) ; AGNTCY (annuaires, transport SLIM) ; interopérabilité du commerce et des paiements agentiques ; le destin d'ACP — **portée de risque seule** (plus haut risque R-1 du Vol. II ; ⚠ **partage déclaré avec le ch. 8**, décision 2 : la mécanique de la fusion y siège, sur le Vol. I *Monographie* §3.3.4, et n'est pas reconstruite ici) ; **le versant protocolaire de la désambiguïsation R-8 du Vol. II** — ⚠ **renvoi au ch. 7 § 7.5, siège de l'encadré des quatre branches** : ne pas le reconstruire ; **les feuilles de route de séquencement protocolaire comme jalon historiographique, jamais comme prescription** (réserve F-06 : la séquence MCP → ACP → A2A → ANP est périmée du fait même de la fusion d'ACP).
*Fusion : Vol. I* Monographie *§3.9 + Vol. II ch. 3. **Divergence tranchée** : gouvernance d'AP2 — aucun transfert documenté à date de gel ; **cette absence ne vaut pas fait négatif vérifié** (PRD Vol. II §10.9e), et la lacune reste ouverte au registre de l'Annexe C. ⚠ **Fait nouveau candidat, relève v0.7** : des annonces publiques d'avril-mai 2026 font état du don d'AP2 (v0.2, 28 avril 2026) à la **FIDO Alliance**, sous deux groupes de travail (authentification agentique ; paiements) — si la source primaire (annonce FIDO/Google) est extraite et datée, c'est la « source primaire nouvelle datée » que l'Annexe C exige, et la lacune §10.9e s'instruit du même mouvement. Statut à date : **annoncé**, non vérifié au socle — le chapitre ne s'écrit pas comme si le transfert était acquis. Socle : F-04, F-05, F-43 ; **réserve F-06**. Garde-fous : R-1, R-8.*

**Table des matières détaillée du chapitre 10**

*Dérivée de `Monographie.md` §3.9 (Vol. I) et de `Monographie.md` ch. 3 (Vol. II) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 10.1 — AP2 : la transaction pilotée par agents

*← Vol. II §3.1 + Vol. I §3.9.2 (volet AP2).* ⚠ **Thèse à statut déclaré** : qu'AP2 soit l'« aboutissement financier » de la pile est une **lecture d'auteur** — le socle établit qu'AP2 est un protocole compagnon d'A2A, rien de plus sur sa centralité. Les 60+ organisations financières sont un **endossement**, pas une mise en production ; l'anatomie du protocole n'est pas documentée au socle (lacune assumée).

⚠ **Divergence tranchée + fait nouveau candidat (relève v0.7)** : aucun transfert de gouvernance documenté à la date de gel — **et cette absence ne vaut pas fait négatif vérifié** (PRD Vol. II §10.9e) ; des annonces d'avril-mai 2026 font état du don d'AP2 (v0.2, 28 avril 2026) à la **FIDO Alliance**. Statut : **annoncé**, non vérifié au socle.

#### § 10.2 — AGNTCY : la couche d'infrastructure

*← Vol. II §3.2 (annuaires, transport SLIM).* ⚠ Le positionnement « couche d'infrastructure et non concurrent » est le **positionnement officiel déclaré du projet** — une déclaration, non un fait vérifié, que des analyses tierces nuancent.

#### § 10.3 — Interopérabilité du commerce et des paiements agentiques

- 10.3.1 Le problème d'interop propre au commerce agentique — *← Vol. I §3.9.1*
- 10.3.2 Checkout et mandats : ACP-commerce (OpenAI/Stripe), UCP (Google) — *← Vol. I §3.9.2, hors volet AP2 (§ 10.1)*
- 10.3.3 Rails de cartes et authentification d'agent (tableau daté) — *← Vol. I §3.9.3*
- 10.3.4 Paiements machine-natifs : x402, MPP, KYA — *← Vol. I §3.9.4 ; le **siège du KYA** est au ch. 19*

#### § 10.4 — Responsabilité, litiges et non-répudiation : l'interop organisationnelle

*← Vol. I §3.9.5.*

#### § 10.5 — Le destin de l'ACP protocolaire : une fusion, non un abandon

*← Vol. II §3.3 ; **plus haut risque R-1**.* ⚠ voir écart

#### § 10.6 — Les feuilles de route de séquencement protocolaire : jalon historiographique, jamais prescription

*← **réserve F-06** : la séquence MCP → ACP → A2A → ANP est périmée du fait même de la fusion d'ACP + le bloc « Ce que ce chapitre établit, et ce qu'il ne dit pas » du Vol. II.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. I §3.9.1 | § 10.3.1 | condensé |
| Vol. I §3.9.2 | § 10.1 et § 10.3.2 | scindé (volet AP2 / autres mandats) |
| Vol. I §3.9.3-3.9.4 | § 10.3.3-10.3.4 | condensé |
| Vol. I §3.9.5 | § 10.4 | condensé |
| Vol. II §3.1 | § 10.1 | condensé |
| Vol. II §3.2 | § 10.2 | condensé |
| Vol. II §3.3 | § 10.5 | condensé (voir écart) |
| Vol. II §3.4 | ch. 7 § 7.5 | **siège de l'encadré R-8** — renvoi, pas reprise |

⚠ **Écart résolu en v0.17 (contrepartie de celui du ch. 8)** — la fusion d'ACP était annoncée par les deux chapitres sans partage déclaré. **Partage posé** (décision 2) : la *mécanique* de la convergence au ch. 8, sur le Vol. I *Monographie* §3.3.4 ; la *portée de risque* ici, sur le Vol. II §3.3. Le §3.4 du Vol. II est réglé de même : son siège est le ch. 7 § 7.5, auquel ce chapitre renvoie.

### Chapitre 11 — Modes d'échec et taxonomie des risques protocolaires

**Thèse** : la sécurité des protocoles dépend de l'implémentation ; empoisonnement d'outils et injection d'invites sont **nommés par les protocoles comme risques attachés**, sans que le socle en date la documentation ni en établisse la mécanique.
Sections : surface d'attaque (outils, invites, mémoire) ; modes d'échec propres à l'interopérabilité agentique ; réponses protocolaires (Signed Agent Cards, autorisation) ; ce que les protocoles ne couvrent pas (renvoi passerelles ch. 42, taxonomie d'identité ch. 20).
*Fusion : Vol. I* Monographie *§3.10-3.11 + Vol. II ch. 4. Socle : F-01, F-02, F-36. Garde-fou : réserve F-01 (« cadre d'autorisation », jamais « sécurisé »). **Lacune héritée portée : PRD Vol. II §10.8** — les risques sont nommés par les protocoles, jamais datés ni outillés d'une source dédiée, et aucune attaque propre à A2A n'est au socle ; renvoi ch. 56.*

**Table des matières détaillée du chapitre 11**

*Dérivée de `Monographie.md` §3.10-3.11 (Vol. I) et de `Monographie.md` ch. 4 (Vol. II) le 25 juillet 2026 — chaque section porte sa provenance. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 11.1 — La surface d'attaque : outils, invites, mémoire

- 11.1.1 Cadrage : l'interopérabilité crée une surface d'attaque **non composable** — *← Vol. I §3.10.1*
- 11.1.2 Modèle de menace de la pile (MCP/A2A/ANP) et triade létale amplifiée — *← Vol. I §3.10.2 ; la triade est posée au ch. 20*
- 11.1.3 Attaques sur les frontières : empoisonnement d'outils, *rug-pull*, injection inter-agents — *← Vol. I §3.10.3 + Vol. II §4.1*

⚠ **Garde-fou** : empoisonnement d'outils et injection d'invites sont **nommés par les protocoles comme risques attachés**, sans que le socle en date la documentation ni en établisse la mécanique.

#### § 11.2 — Modes d'échec propres à l'interopérabilité agentique

- 11.2.1 Taxonomie des échecs émergents (non réductibles à un agent) — *← Vol. I §3.11.1*
- 11.2.2 Défaillances en cascade, incidents de production et *compounding* à long horizon — *← Vol. I §3.11.2*

#### § 11.3 — Les réponses protocolaires : ce que les spécifications apportent

- 11.3.1 Signed Agent Cards et autorisation — *← Vol. II §4.2 ; **réserve F-01** : « cadre d'autorisation », jamais « sécurisé »*
- 11.3.2 Durcissement par couche et intégrité/provenance des registres — *← Vol. I §3.10.4*
- 11.3.3 Défenses par conception et red-teaming inter-agents — *← Vol. I §3.10.5*

#### § 11.4 — Ce que les protocoles ne couvrent pas

*← Vol. II §4.3 + le bloc « Ce que ce chapitre établit, et ce qu'il ne dit pas ».* Renvois : passerelles et durcissement d'infrastructure au **ch. 42** ; taxonomie des risques d'identité au **ch. 20**.

⚠ **Lacune héritée portée (PRD Vol. II §10.8)** : les risques sont nommés par les protocoles, jamais datés ni outillés d'une source dédiée, et **aucune attaque propre à A2A n'est au socle** ; renvoi ch. 56.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. I §3.10.1-3.10.3 | § 11.1 | condensé |
| Vol. I §3.10.4-3.10.5 | § 11.3.2-11.3.3 | condensé |
| Vol. I §3.11 | § 11.2 | condensé |
| Vol. II §4.1 | § 11.1.3 | condensé |
| Vol. II §4.2 | § 11.3.1 | condensé |
| Vol. II §4.3 + clôture | § 11.4 | condensé |

---

## LIVRE III — Identité, délégation et fabrique de confiance : émission, confiance hostile, horloge post-quantique

*(fusionne Vol. III Parties I-V + Vol. I §2.11.2/§3.6/§5.5.4/§7.4.2 + §2.10.1-2.10.2/§7.5 + §7.4.1/§7.4.4 + Vol. II ch. 8 — condensation v0.9 : absorbe les anciens Livres IV et V, décision 10 ; trois mouvements — émettre, ch. 12-19 ; le versant hostile, ch. 20-22 ; l'horloge post-quantique, ch. 23-24 ; ~50 000 mots)*

**Premier mouvement — émettre (ch. 12-19).**

### Chapitre 12 — L'héritage : un demi-siècle d'identités non humaines

**Thèse** : l'identité machine n'est pas née avec les agents — comptes de service, X.509, clés d'API forment un passif mal gouverné dont l'entreprise agentique hérite avant d'y ajouter le sien.
Sections : généalogie (comptes de service → workload identity) ; l'écart de gouvernance NHI (ratio machines/humains, prolifération des secrets — illustration, jamais preuve) ; pourquoi l'agent casse le modèle (identité stable vs comportement non déterministe).
*Fusion : Vol. III ch. 1, adossé au ch. 3 (socle IAM déjà posé, non repris). Garde-fou : chiffres de prolifération auto-déclarés.*

**Table des matières détaillée du chapitre 12**

*Dérivée du **texte rédigé** de `Monographie.md` ch. 1 (Vol. III) le 25 juillet 2026. ⚠ **Convention de renvoi propre à ce livre** (décision 7) : le Vol. III vit en numérotation multiple — un renvoi au texte s'écrit `Vol. III `*Monographie*` §N.M`, un renvoi au plan `Vol. III `*TOC*` §N.x`. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 12.1 — Généalogie : de l'hypothèse humaine à l'identité de charge de travail

*← Vol. III* Monographie *§1.1 (comptes de service, X.509, clés d'API → workload identity).*

#### § 12.2 — L'écart de gouvernance des identités non humaines

*← Vol. III* Monographie *§1.2.* ⚠ **Garde-fou** : ratio machines/humains et prolifération des secrets sont des chiffres **auto-déclarés** — illustration, jamais preuve.

#### § 12.3 — Pourquoi l'agent casse le modèle : identité stable et comportement variable

*← Vol. III* Monographie *§1.3.*

⚠ *Le socle IAM pré-agentique (Vol. I §1.9.2-§1.9.3) est **posé au ch. 3** et n'est pas repris ici : ce chapitre s'y adosse. C'est la contrepartie de l'économie de fusion déclarée au ch. 3.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §1.1 | § 12.1 | condensé |
| Vol. III *Monographie* §1.2 | § 12.2 | condensé |
| Vol. III *Monographie* §1.3 | § 12.3 | condensé |

### Chapitre 13 — Les standards étirés : OAuth, OIDC, SCIM face à l'agent

**Thèse** : la première vague de l'identité agentique est une extension des RFC existantes, non une rupture — et chaque extension révèle une hypothèse implicite (un humain au bout du flux) qui cesse de tenir.
Sections : OAuth 2.x et l'agent (client ou resource owner ?) ; drafts IETF (délégation, transaction tokens, identité de charge de travail appliquée aux agents) ; SCIM et provisionnement d'agents ; Entra Agent ID **comme extension des RFC** (GA, licences — son traitement comme annuaire commercial est au ch. 16, et n'est pas repris ici) ; ce que les RFC ne disent pas.
*Fusion : Vol. III ch. 2 + Vol. II ch. 8 §8.1/§8.3 + Vol. I* Monographie *§3.6.1-3.6.2 (OAuth 2.1/OIDC appliqués aux agents, Token Exchange). ⚠ Le socle IAM pré-agentique (§1.9.2) **reste au ch. 3** et n'est pas repris ici. Socle : F-07, F-08. Garde-fou : **PRD Vol. II §8.2.5** — statuts pré-normatifs : un brouillon IETF n'est pas une norme, et celui de SCIM-agents est **expiré depuis le 19 avril 2026**. ⚠ **Relève v0.7 — la filière ne s'est pas éteinte** : brouillons successeurs actifs à mi-2026 (applicabilité de WIMSE aux agents d'IA, expirant le 1ᵉʳ septembre 2026 ; cadre composant WIMSE, SPIFFE et OAuth 2.0, version du 1ᵉʳ juin 2026 ; extension SCIM d'éditeur pour le provisionnement d'agents), tous **pré-normatifs** — à recenser au gel, le garde-fou §8.2.5 demeurant inchangé, sources primaires (datatracker) à extraire. (R-2 et R-3 ne sont pas portés ici : ils vivent au §8.4 et au §8.2 du Vol. II, donc aux ch. 17 et ch. 16.)*

**Table des matières détaillée du chapitre 13**

*Dérivée du texte rédigé de `Monographie.md` ch. 2 (Vol. III), ch. 8 (Vol. II) et §3.6 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 13.1 — OAuth 2.x et l'agent : *client* ou détenteur de ressource ?

*← Vol. III* Monographie *§2.1 + Vol. I* Monographie *§3.6.1 (pourquoi NHI et OAuth ne suffisent plus).*

#### § 13.2 — Les brouillons de l'IETF : quatre statuts, et ce que leurs dates disent ou ne disent pas

*← Vol. III* Monographie *§2.2 + Vol. II §8.3 (un ancrage dont le point d'ancrage a expiré) + Vol. I* Monographie *§3.6.2 (délégation multi-saut, Token Exchange).*

⚠ **Garde-fou (PRD Vol. II §8.2.5)** : un brouillon IETF n'est pas une norme ; celui de SCIM-agents est **expiré depuis le 19 avril 2026**.

⚠ **Relève v0.7, à instruire à la source primaire** : brouillons successeurs actifs à mi-2026 (applicabilité de WIMSE aux agents d'IA, expirant le 1ᵉʳ septembre 2026 ; cadre composant WIMSE/SPIFFE/OAuth 2.0, version du 1ᵉʳ juin 2026 ; extension SCIM d'éditeur), tous **pré-normatifs**.

#### § 13.3 — SCIM et le provisionnement d'agents

*← Vol. III* Monographie *§2.3.*

#### § 13.4 — Entra Agent ID comme extension des RFC

*← Vol. II §8.1 (GA, licences).* ⚠ **Son traitement comme annuaire commercial est au ch. 16** et n'est pas repris ici.

#### § 13.5 — Ce que les RFC ne disent pas — et à quel degré

*← Vol. III* Monographie *§2.4 ; l'échelle des trois degrés d'absence (R-14 du Vol. III) s'applique.*

⚠ *Le socle IAM pré-agentique (Vol. I §1.9.2) **reste au ch. 3**. R-2 et R-3 ne sont pas portés ici : leurs sièges sont le §8.4 (ch. 17) et le §8.2 (ch. 16) du Vol. II.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §2.1 | § 13.1 | condensé |
| Vol. III *Monographie* §2.2 | § 13.2 | condensé |
| Vol. III *Monographie* §2.3 | § 13.3 | condensé |
| Vol. III *Monographie* §2.4 | § 13.5 | condensé |
| Vol. II §8.1 | § 13.4 | condensé (volet RFC seul) |
| Vol. II §8.3 | § 13.2 | condensé |
| Vol. I *Monographie* §3.6.1-3.6.2 | § 13.1-13.2 | condensé |

### Chapitre 14 — L'identité décentralisée : VC, DID et la promesse du portable

**Thèse** : le corpus W3C (VC, DID) fournit le vocabulaire du « passeport d'agent », mais son adoption en entreprise financière reste à démontrer — la distinction promesse/production est le fil.
Sections : VC Data Model et DID Core ; DIF et profils d'interopérabilité ; Community Groups agentiques du W3C (signal faible, état 2026) ; le fossé adoption (qui vérifie quoi, en production).
*Fusion : Vol. III ch. 3 + Vol. I* Monographie *§3.6.4 (SPIFFE/SPIRE, DID, WIMSE) et **§7.4.3** (identité vérifiable inter-domaines — le §7.4 est partagé : §7.4.1 et §7.4.4 vont aux ch. 23-24, §7.4.2 au ch. 17, §7.4.3 se partage entre ici et le ch. 19). Garde-fou : une charte de groupe n'est pas un standard.*

**Table des matières détaillée du chapitre 14**

*Dérivée du texte rédigé de `Monographie.md` ch. 3 (Vol. III) et §3.6.4/§7.4.3 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 14.1 — VC Data Model et DID Core : à quel stade en sont les recommandations

*← Vol. III* Monographie *§3.1.*

#### § 14.2 — Les profils d'interopérabilité : une lacune de couverture assumée

*← Vol. III* Monographie *§3.2 (DIF).*

#### § 14.3 — Les Community Groups agentiques du W3C

*← Vol. III* Monographie *§3.3 (signal faible, état 2026).* ⚠ **Garde-fou** : une charte de groupe n'est pas un standard.

#### § 14.4 — Identité de charge et identité décentralisée : SPIFFE/SPIRE, DID, WIMSE

*← Vol. I* Monographie *§3.6.4 ; le socle zero-trust pré-agentique (§1.9.3) reste au ch. 3.*

#### § 14.5 — Le fossé d'adoption : qui vérifie quoi, en production, à date

*← Vol. III* Monographie *§3.4 + Vol. I* Monographie *§7.4.3 (identité vérifiable inter-domaines — **partagé déclaré avec le ch. 19**, qui en prend le versant* trust fabric*).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §3.1-3.3 | § 14.1-14.3 | condensé |
| Vol. III *Monographie* §3.4 | § 14.5 | condensé |
| Vol. I *Monographie* §3.6.4 | § 14.4 | condensé |
| Vol. I *Monographie* §7.4.3 | § 14.5 + ch. 19 | **partagé déclaré** |
| Vol. I *Monographie* §7.4.1, §7.4.4 | ch. 23-24 | hors périmètre (horloge PQC) |
| Vol. I *Monographie* §7.4.2 | ch. 17 | hors périmètre (passeport) |

### Chapitre 15 — La grille des cinq questions

**Thèse** : cinq questions — *qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond* — forment la grille de lecture de tout mécanisme d'identité agentique ; aucun mécanisme de 2026 ne répond aux cinq.
Sections : dérivation depuis les axes du Vol. I (*Monographie* §3.1.7, repris au ch. 7) ; application-témoin à trois mécanismes ; la grille comme critère de structure des chapitres suivants ; croisement grille × maturité (corpus d'appui — construction d'auteur).
*Fusion : Vol. III ch. 4 (chapitre de méthode transversal, homologue de la matrice du ch. 46).*

**Table des matières détaillée du chapitre 15**

*Dérivée du texte rédigé de `Monographie.md` ch. 4 (Vol. III) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 15.1 — L'inspiration de la grille — et ce qu'elle n'autorise pas

*← Vol. III* Monographie *§4.1 ; dérivation depuis les quatre axes du Vol. I (*Monographie* §3.1.7, repris au ch. 7 § 7.2.2).*

#### § 15.2 — Application-témoin à trois mécanismes

*← Vol. III* Monographie *§4.2.*

#### § 15.3 — La grille comme critère de structure des chapitres suivants

*← Vol. III* Monographie *§4.3 (Parties II-IV de la source = ch. 16-24 ici).*

#### § 15.4 — Grille et maturité

*← Vol. III* Monographie *§4.4.* ⚠ **Corpus d'appui : filiation retirée** (P0.2, 21 juill. 2026, L-15 close par échec documenté, **réversible**) — le croisement grille × maturité se rebâtit sur l'autonomie graduée et la grille elle-même ; le Vol. III rédigé a comblé cet emplacement par **construction d'auteur sous CA-07** (« Lecture de l'auteur » en tête d'énoncé), à reprendre avec son marquage, jamais comme un fait de corpus.

⚠ *Les cinq questions — **qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond** — structurent les verdicts des ch. 16 à 24 ; le ch. 17 est le seul endroit où les cinq reçoivent une réponse, et elle est sur le papier.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §4.1-4.4 | § 15.1-15.4 | condensé |
| Vol. I *Monographie* §3.1.7 | ch. 7 § 7.2.2 | socle amont, non repris ici |

### Chapitre 16 — Émettre : Agent Card signée, annuaires, registres gouvernés

**Thèse** *(instruit Q3 de la série d'agenda du Vol. II — Monographie ch. 21 §21.2)* : la signature d'une Agent Card vaut ce que valent son ancrage de confiance, sa révocation et sa gouvernance des clés ; le registre gouverné devient la pièce de conformité maîtresse, mais trois modèles concurrents répondent à des questions différentes de la grille.
Sections : Agent Card signée (format, chaîne, ancrage, révocation, valeur probante) ; annuaires commerciaux (Entra Agent ID et pairs — GA/annonce/feuille de route) ; registres gouvernés (spécification CSA `toolAccessList`/`permissionBoundaries`, registres A2A/AGNTCY) ; **le risque de standard de fait** (Vol. III *TOC* §6.3 : un annuaire commercial dominant fixe la norme sans passer par une norme) ; le registre comme objet réglementaire (pont vers Livre V).
*Fusion : Vol. III ch. 5-7 **hors §7.4** (« Ce qui n'existe toujours pas » — prélevé par le ch. 17, qui le nomme : le bloc « ch. 5-7 » et ce prélèvement se contredisaient à la lettre, décision 6) + Vol. II ch. 8 §8.2 + Vol. I* Monographie *§3.4 (découverte) et §3.6.3 (preuve cryptographique : Agent Cards signées et VC). Chapitre à plus haut risque de surinterprétation — relecture adversariale prioritaire. Socle : F-07, F-08 + spécifications A2A/CSA/AGNTCY. Garde-fous : **R-3 du Vol. II** (la spécification CSA s'appuie sur SPIFFE/SPIRE comme fondation ; l'exigence stricte n'est pas établie) et **PRD Vol. II §8.2.5** (la spécification CSA est un brouillon de laboratoires, pas une norme).*

**Table des matières détaillée du chapitre 16**

*Dérivée du texte rédigé de `Monographie.md` ch. 5-7 (Vol. III), ch. 8 §8.2 (Vol. II) et §3.4/§3.6.3 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 16.1 — L'Agent Card signée : anatomie et valeur probante

- 16.1.1 Le format et la chaîne de signature — *← Vol. III* Monographie *§5.1 + Vol. I* Monographie *§3.6.3 (preuve cryptographique : Agent Cards signées et VC)*
- 16.1.2 Ancrage : qui signe les signataires ? — *← Vol. III* Monographie *§5.2*
- 16.1.3 Révocation et durée de vie — *← Vol. III* Monographie *§5.3 ; l'inventaire complet de la révocation est au ch. 21*
- 16.1.4 Verdict par la grille du ch. 15 : ce que la carte prouve, ce qu'elle affirme, ce qu'elle tait — *← Vol. III* Monographie *§5.4*

#### § 16.2 — Les annuaires commerciaux : Entra Agent ID et ses pairs

- 16.2.1 Ce que la disponibilité générale couvre, et ce qu'elle ne couvre pas — *← Vol. III* Monographie *§6.1 ; **le versant « extension des RFC » est au ch. 13** et n'est pas repris ici*
- 16.2.2 Les mécanismes documentés chez les autres fournisseurs infonuagiques : un état daté — *← Vol. III* Monographie *§6.2*
- 16.2.3 **Le risque de standard de fait** : un annuaire commercial dominant fixe la norme sans passer par une norme — *← Vol. III* Monographie *§6.3*
- 16.2.4 La grille du ch. 15 appliquée — *← Vol. III* Monographie *§6.4*

#### § 16.3 — Les registres gouvernés : de la spécification CSA aux registres A2A

- 16.3.1 La spécification CSA (`toolAccessList`, `permissionBoundaries`) : ce qu'un brouillon de laboratoire prescrit, et ce qu'il traîne — *← Vol. III* Monographie *§7.1 + Vol. II §8.2*
- 16.3.2 Registres et découverte : A2A normalise le chemin, AGNTCY spécifie le magasin — *← Vol. III* Monographie *§7.2 + Vol. I* Monographie *§3.4 (**partagé déclaré avec le ch. 9**, qui en prend le versant protocolaire)*
- 16.3.3 Le registre comme objet réglementaire — et la quatrième pièce du passeport — *← Vol. III* Monographie *§7.3 ; pont vers le Livre V (ch. 29)*

⚠ **Garde-fous** : **R-3 du Vol. II** — la spécification CSA s'appuie sur SPIFFE/SPIRE comme *fondation* ; l'exigence stricte n'est pas établie. **PRD Vol. II §8.2.5** — la spécification CSA est un brouillon de laboratoires, pas une norme. **Chapitre à plus haut risque de surinterprétation : relecture adversariale prioritaire.**

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §5.1-5.4 | § 16.1 | condensé |
| Vol. III *Monographie* §6.1-6.4 | § 16.2 | condensé |
| Vol. III *Monographie* §7.1-7.3 | § 16.3 | condensé |
| Vol. III *Monographie* §7.4 | **ch. 17** | prélevé — « hors §7.4 » porté à la ligne Fusion (v0.17) |
| Vol. II §8.2 | § 16.3.1 | condensé |
| Vol. I *Monographie* §3.4 | § 16.3.2 + ch. 9 | **partagé déclaré** |
| Vol. I *Monographie* §3.6.3 | § 16.1.1 | condensé |

⚠ **Écart résolu en v0.17** — la ligne Fusion absorbait « Vol. III ch. 5-**7** » en bloc alors que le §7.4 de la source est **nommément prélevé par le ch. 17** : elle porte désormais son « **hors §7.4** ». ⚠ **Le contrôle exécutable ne voit pas cette classe** — la double revendication y est à deux grains différents, l'un au chapitre, l'autre à la section : elle reste une **collation manuelle**, à refaire à chaque révision d'une ligne Fusion citant un intervalle de chapitres.

### Chapitre 17 — Le passeport d'agent : synthèse d'un objet encore virtuel

**Thèse** : le « passeport d'agent » n'existe dans aucune spécification de 2026 — objet de synthèse assemblant carte signée, inscription au registre, chaîne de mandat et attestations ; sa normalisation 2027-2028 est projetée en statut PROJETÉ. Pour l'entreprise, rien n'entre au maillage sans lui.
Sections : les quatre pièces du passeport ; **ce qui n'existe toujours pas** (Vol. III *TOC* §7.4 — inventaire des manques côté émission, prolongé ici par le §8.4 du Vol. II) ; qui l'émettrait, qui le vérifierait ; trois scénarios de normalisation (PROGRAMMÉ/PROJETÉ/SPÉCULATIF) ; le passeport par la grille du ch. 15 — la seule construction qui répond aux cinq questions, sur le papier.
*Fusion : Vol. III ch. 8 (chapitre-pivot) + Vol. III *TOC* §7.4 + Vol. II ch. 8 §8.4 (« ce qui n'existe pas encore ») + Vol. I* Monographie *§7.4.2 (de l'identité au passeport : la normalisation 2027-2028 — siège du statut PROJETÉ ici repris). Garde-fous : **R-2 et R-3**, dont le §8.4 du Vol. II est le siège (encadré « Affirmations écartées »). Inférences d'auteur marquées systématiquement.*

**Table des matières détaillée du chapitre 17**

*Dérivée du texte rédigé de `Monographie.md` ch. 8 et §7.4 (Vol. III), ch. 8 §8.4 (Vol. II) et §7.4.2 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 17.1 — Assemblage : les quatre pièces du passeport

*← Vol. III* Monographie *§8.1 (carte signée, inscription au registre, chaîne de mandat, attestations).*

#### § 17.2 — Ce qui n'existe toujours pas — et à quel degré

*← Vol. III* Monographie *§7.4 (inventaire des manques côté émission) **prolongé par** Vol. II §8.4 (« Ce qui n'existe pas encore »).* ⚠ **Siège des garde-fous R-2 et R-3** (encadré « Affirmations écartées » du Vol. II) ; l'échelle des trois degrés d'absence (R-14 du Vol. III) s'applique — *fait négatif vérifié* > *fait négatif établi* > *absence de documentation*, jamais interchangeables.

#### § 17.3 — Qui l'émettrait, qui le vérifierait

*← Vol. III* Monographie *§8.2.*

#### § 17.4 — Trois scénarios de normalisation, et ce que leur tri prospectif interdit d'écrire

*← Vol. III* Monographie *§8.3 + Vol. I* Monographie *§7.4.2 (de l'identité au passeport : la normalisation 2027-2028, **siège du statut PROJETÉ** ici repris).* Tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF obligatoire.

#### § 17.5 — Le passeport par la grille du ch. 15

*← Vol. III* Monographie *§8.4 : **le seul endroit de l'ouvrage où les cinq questions reçoivent une réponse, et elle est sur le papier**.*

⚠ *Le « passeport d'agent » **n'existe dans aucune spécification de 2026** : objet de synthèse, pas mécanisme documenté. Inférences d'auteur marquées systématiquement (décision 8).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §8.1-8.4 | § 17.1, 17.3-17.5 | condensé |
| Vol. III *Monographie* §7.4 | § 17.2 | **prélevé au ch. 16**, qui porte son « hors §7.4 » (v0.17) |
| Vol. II §8.4 | § 17.2 | condensé — siège de R-2 et R-3 |
| Vol. I *Monographie* §7.4.2 | § 17.4 | condensé — siège du statut PROJETÉ |

### Chapitre 18 — La chaîne de mandat et le problème des deux sauts

**Thèse** *(instruit le front ouvert du Vol. I,* Synthèse *§11.5)* : la délégation est le maillon faible — les mécanismes de 2026 prouvent qu'un agent *a* une identité, presque aucun ne prouve *au nom de qui* il agit ; au-delà de deux sauts, aucun mécanisme documenté ne maintient une traçabilité opposable de bout en bout.
Sections : le mandat dans les protocoles (AP2, on-behalf-of OAuth, transaction tokens) ; **ce que le droit civil du mandat éclaire — et où l'analogie casse** (Vol. III *TOC* §9.3, seule occurrence : le versant québécois du mandat est au ch. 31, l'analyse de la limite de l'analogie est ici) ; chaîne de délégation comme objet de première classe ; l'humain premier et dernier maillon (approbation/escalade/HITL relus comme actes de délégation datés ; **patrons d'interaction humain-agent — corpus d'appui, cadrage et non preuve**) ; **le biais d'automatisation et la supervision de façade** — le tamponnage comme mode d'échec documenté de la révision humaine, et le paradoxe de l'explicabilité (une justification mieux rédigée augmente la déférence, pas le discernement) : c'est la limite empirique de la parade sur laquelle reposent l'art. 12.1 (ch. 31) et la supervision E-23 (ch. 29) ; le problème des deux sauts (où chaque mécanisme perd le fil, pistes et limites, question de recherche).
*Fusion : Vol. III ch. 9-10 + Vol. I* Monographie *§2.11.2 (chaînes multi-saut) et §3.6.6 (l'axe agent-humain : HITL négocié). Socle : spécification AP2 (**divergence de gouvernance déjà tranchée au ch. 10**) ; **le versant biais d'automatisation est un front neuf — aucun des trois volumes ne le porte, sources primaires à établir.** Frontière de la connaissance vérifiable exposée, non comblée.*

**Table des matières détaillée du chapitre 18**

*Dérivée du texte rédigé de `Monographie.md` ch. 9-10 (Vol. III) et §2.11.2/§3.6.6 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 18.1 — Le mandat dans les protocoles

*← Vol. III* Monographie *§9.1 (AP2, on-behalf-of OAuth, transaction tokens).* ⚠ La divergence de gouvernance d'AP2 est **déjà tranchée au ch. 10** — ne pas la rouvrir ici.

#### § 18.2 — La chaîne de délégation comme objet de première classe

*← Vol. III* Monographie *§9.2 + Vol. I* Monographie *§2.11.2 (chaînes multi-saut).*

#### § 18.3 — Ce que le droit civil du mandat éclaire — et où l'analogie casse

*← Vol. III* Monographie *§9.3, **seule occurrence** : le versant québécois du mandat est au ch. 31 (Vol. III* Monographie *§20.2), l'analyse de la limite de l'analogie est ici.*

#### § 18.4 — L'humain, premier et dernier maillon

*← Vol. III* Monographie *§9.4 + Vol. I* Monographie *§3.6.6 (l'axe agent-humain : HITL négocié, modalités,* elicitation *MCP, MCP Apps, AG-UI).* Approbation, escalade et HITL relus comme **actes de délégation datés**. ⚠ **Patrons d'interaction humain-agent : corpus d'appui, cadrage et non preuve** (filiation retirée par P0.2, réversible).

#### § 18.5 — Le biais d'automatisation et la supervision de façade

le tamponnage comme mode d'échec documenté de la révision humaine ; le **paradoxe de l'explicabilité** (une justification mieux rédigée augmente la déférence, pas le discernement).

⚠ **Front neuf — aucun des trois volumes ne le porte** : sources primaires à établir avant rédaction. C'est la **limite empirique de la parade** sur laquelle reposent l'art. 12.1 (ch. 31) et la supervision attendue par E-23 (ch. 29) : la section est structurante pour le Livre V, et son socle est à constituer depuis rien.

#### § 18.6 — Le problème des deux sauts

- 18.6.1 Pourquoi deux sauts : où chaque mécanisme perd le fil — *← Vol. III* Monographie *§10.1*
- 18.6.2 Trois pistes, et ce que le socle établit de chacune — *← Vol. III* Monographie *§10.2*
- 18.6.3 Question de recherche formulée pour instruction — *← Vol. III* Monographie *§10.3*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §9.1-9.4 | § 18.1-18.4 | condensé |
| Vol. III *Monographie* §10.1-10.3 | § 18.6 | condensé |
| Vol. I *Monographie* §2.11.2 | § 18.2 | condensé |
| Vol. I *Monographie* §3.6.6 | § 18.4 | condensé |
| — (front neuf) | § 18.5 | **socle à constituer**, déclaré |

### Chapitre 19 — Know Your Agent : la vérification d'agent tiers inter-domaines

**Thèse** : le KYA transpose la logique du KYC — vérifier avant d'admettre — sans l'infrastructure institutionnelle qui rend le KYC possible ; la *trust fabric* inter-entreprises reste privée et fragmentée, et c'est elle qui décide si l'entreprise agentique s'arrête à ses murs.
Sections : état des propositions KYA ; admission d'un agent tiers (point de contact identité/frontières) ; fédérations de confiance (eIDAS, FIDO) et transposabilité ; ⚠ **relève v0.11 — l'agent mutable prive la réputation de son ancrage** : une préimpression révisée en mai 2026 (arXiv 2605.30169) soutient que les architectures d'agents à poids, invites et mémoire mutables n'offrent pas la persistance d'identité que tout mécanisme de réputation présuppose — l'objet vérifié à l'admission peut cesser d'être l'objet admis. À instruire ; si la thèse tient, elle pèse sur la cinquième question de la grille (ch. 15) et sur la révocation (ch. 21) autant que sur l'admission.
*Fusion : Vol. III ch. 11 + Vol. I* Monographie *§5.5.4 (SIÈGE du KYA), §3.6.5 et §7.4.3 (trust fabric inter-domaines, partagé avec le ch. 14). Garde-fou : « KYA » est un terme de marché avant d'être un terme de norme.*

**Table des matières détaillée du chapitre 19**

*Dérivée du texte rédigé de `Monographie.md` ch. 11 (Vol. III) et §5.5.4/§3.6.5/§7.4.3 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 19.1 — État des propositions KYA

*← Vol. III* Monographie *§11.1 (neuf chantiers, six organisations, **zéro texte ratifié**) + Vol. I* Monographie *§5.5.4 (**SIÈGE unique du KYA** : KYA, NHI et jetons de paiement agentiques).* ⚠ **Garde-fou** : « KYA » est un terme de **marché** avant d'être un terme de norme.

#### § 19.2 — Admettre un agent tiers : ce que les protocoles remettent à celui qui décide

*← Vol. III* Monographie *§11.2 (point de contact identité/frontières).*

#### § 19.3 — Fédérations de confiance : ce que trois précédents portent d'institutionnel

*← Vol. III* Monographie *§11.3 (eIDAS, FIDO) + Vol. I* Monographie *§3.6.5 (trust fabric inter-domaines, profils d'interop et angles morts) et §7.4.3 (**partagé déclaré avec le ch. 14**).* Le KYA transpose la logique du KYC **sans l'infrastructure institutionnelle qui rend le KYC possible**.

#### § 19.4 — ⚠ Relève v0.11, à instruire : l'agent mutable prive la réputation de son ancrage

une préimpression révisée en mai 2026 (arXiv 2605.30169) soutient que les architectures à poids, invites et mémoire **mutables** n'offrent pas la persistance d'identité que tout mécanisme de réputation présuppose : *l'objet vérifié à l'admission peut cesser d'être l'objet admis*. **Préimpression non révisée par les pairs, résumé seul consulté — repérage [C], jamais un fait.** Si la thèse tient, elle pèse sur la cinquième question de la grille (ch. 15) et sur la révocation (ch. 21) autant que sur l'admission.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §11.1-11.3 | § 19.1-19.3 | condensé |
| Vol. I *Monographie* §5.5.4 | § 19.1 | **siège unique du KYA** |
| Vol. I *Monographie* §3.6.5 | § 19.3 | condensé |
| Vol. I *Monographie* §7.4.3 | § 19.3 + ch. 14 | **partagé déclaré** |

**Deuxième mouvement — la confiance hostile (ch. 20-22)** *(anciennement Livre IV ; provenance intégrée à l'en-tête du livre)*

### Chapitre 20 — Taxonomie des attaques d'identité et de délégation

**Thèse** *(instruit Q2 de la série d'agenda du Vol. II — Monographie ch. 21 §21.2)* : une part majoritaire des attaques propres aux systèmes multi-agents documentées à date sont des attaques d'identité (usurpation, confusion de délégué) ou de délégation (élévation par chaîne de mandat) — ce qui justifie d'absorber la sécurité dans le cadre identitaire.
Sections : recension (identifiants de vulnérabilité, incidents datés — dont les divulgations du 1ᵉʳ semestre 2026 relevées en v0.7, corpus candidat du dénombrement exigé par la décision 8, à qualifier pièce par pièce avant usage —, littérature ; ⚠ **relève v0.10** : une classe dont le vecteur est le **harnais** — extension tierce admise par simple configuration — et non le protocole ni le mécanisme d'identité (voir ch. 52) ; si elle s'instruit, elle entre au dénombrement **contre** la thèse d'absorption de ce chapitre, non à son appui) ; taxonomie par la grille du ch. 15 ; empoisonnement de la mémoire et des sources (provenance RAG comme problème d'identité des sources — reprend le ch. 5) ; ce que la recension ne trouve pas.
*Fusion : Vol. III ch. 12 + Vol. I* Monographie *§2.10.1-2.10.2. ⚠ **La thèse de ce chapitre est le premier énoncé à instruire avant rédaction** : le Vol. II pose Q2 précisément parce que son socle ne porte **aucune** attaque propre à A2A (PRD §10.8 — absence de documentation, non fait négatif vérifié). La proportion affirmée doit être établie par dénombrement sur un corpus déclaré, ou l'énoncé retombe à « une part notable » sans quantificateur. Traitement défensif exclusif : mécanique au niveau architectural, sans recette d'exploitation.*

**Table des matières détaillée du chapitre 20**

*Dérivée du texte rédigé de `Monographie.md` ch. 12 (Vol. III) et §2.10.1-2.10.2 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 20.1 — Recension : identifiants, incidents datés, littérature

*← Vol. III* Monographie *§12.1.*

⚠ **Relève v0.7** : les divulgations du 1ᵉʳ semestre 2026 forment le **corpus candidat** du dénombrement qu'exige la décision 8 — à qualifier pièce par pièce avant usage.

⚠ **Relève v0.10** : une classe d'attaques dont le vecteur est le **harnais** (extension tierce admise par simple configuration), et non le protocole ni le mécanisme d'identité — voir ch. 52. Si elle s'instruit, elle entre au dénombrement **contre** la thèse d'absorption de ce chapitre, non à son appui.

#### § 20.2 — Modèle de menace agentique, triade létale et impossibilité architecturale

*← Vol. I* Monographie *§2.10.1 ; **siège de la triade létale**, que le ch. 11 § 11.1.2 invoque sans la reconstruire.*

#### § 20.3 — Vecteurs d'attaque

*← Vol. I* Monographie *§2.10.2 : injection d'invite directe et indirecte (§2.10.2.1) ; exfiltration, egress et agence excessive (§2.10.2.3).*

#### § 20.4 — Taxonomie par la grille du ch. 15

*← Vol. III* Monographie *§12.2.*

#### § 20.5 — L'empoisonnement de la mémoire et des sources

*← Vol. III* Monographie *§12.3 + Vol. I* Monographie *§2.10.2.2.* La provenance RAG relue comme **problème d'identité des sources** : c'est le versant hostile de l'ancrage posé au ch. 5, qui n'en porte aucune occurrence.

#### § 20.6 — Ce que la recension ne trouve pas

*← Vol. III* Monographie *§12.4 ; échelle des trois degrés d'absence (R-14 du Vol. III).*

⚠ **La thèse de ce chapitre est le premier énoncé à instruire avant rédaction.** Le Vol. II pose Q2 précisément parce que son socle ne porte **aucune** attaque propre à A2A (PRD Vol. II §10.8 — *absence de documentation*, non fait négatif vérifié). La proportion affirmée (« une part majoritaire ») doit être établie **par dénombrement sur un corpus déclaré**, ou l'énoncé retombe à « une part notable » sans quantificateur (décision 8). **Traitement défensif exclusif** : mécanique au niveau architectural, sans recette d'exploitation.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §12.1-12.4 | § 20.1, 20.4-20.6 | condensé |
| Vol. I *Monographie* §2.10.1 | § 20.2 | **arrivée** depuis le ch. 6 |
| Vol. I *Monographie* §2.10.2 | § 20.3, § 20.5 | **arrivée** depuis le ch. 6 |
| Vol. I *Monographie* §2.10.3-2.10.5 | ch. 6 (+ ch. 42) | hors périmètre — défense et alignement |

### Chapitre 21 — Usurpation, rug-pull et révocation

**Thèse** : la vérification à l'admission ne protège pas contre la dérive après admission (rug-pull d'un serveur d'outils ou d'un agent tiers) ; et chaque mécanisme spécifie l'émission avec soin et la révocation avec négligence — asymétrie qui reproduit l'histoire des PKI.
Sections : le rug-pull documenté ; vérification continue vs à l'admission ; attestation d'intégrité à l'exécution ; inventaire de la révocation par mécanisme ; précédent PKI (CRL, OCSP) ; révocation en cascade dans une chaîne de délégation (problème ouvert).
*Fusion : Vol. III ch. 13-14. Renvoi ch. 44 (dérive en exploitation) et ch. 50 (révocation dans le cycle de vie). ⚠ **Relève v0.10** : le rug-pull a un grain de plus fin que le serveur d'outils — l'**extension déclarative** du harnais (fichier d'instructions, serveur ajouté par configuration), dont l'installation n'est pas un acte de compilation et dont la révocation n'a, à cette date, aucun mécanisme relevé. À instruire à la source primaire ; l'incident public candidat est décrit au ch. 52.*

**Table des matières détaillée du chapitre 21**

*Dérivée du texte rédigé de `Monographie.md` ch. 13-14 (Vol. III) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 21.1 — Le *rug-pull* documenté : ce que le corpus nomme, et à quel niveau de preuve

*← Vol. III* Monographie *§13.1.*

⚠ **Relève v0.10, à instruire** : le *rug-pull* a un grain plus fin que le serveur d'outils — l'**extension déclarative** du harnais (fichier d'instructions, serveur ajouté par configuration), dont l'installation n'est pas un acte de compilation et dont la révocation n'a, à cette date, **aucun mécanisme relevé**. Incident public candidat décrit au ch. 52.

#### § 21.2 — Vérification continue et vérification à l'admission

*← Vol. III* Monographie *§13.2.* La vérification à l'admission ne protège pas contre la **dérive après admission** ; renvoi ch. 44 (dérive en exploitation).

#### § 21.3 — L'attestation d'intégrité à l'exécution : état des mécanismes

*← Vol. III* Monographie *§13.3.*

#### § 21.4 — L'inventaire de la révocation, mécanisme par mécanisme

*← Vol. III* Monographie *§14.1.* Chaque mécanisme spécifie **l'émission avec soin et la révocation avec négligence**.

#### § 21.5 — Le précédent PKI : ce que les listes de révocation et le statut en ligne ont déjà appris

*← Vol. III* Monographie *§14.2 (CRL, OCSP).*

#### § 21.6 — La révocation en cascade dans une chaîne de délégation

*← Vol. III* Monographie *§14.3 ; **problème ouvert**, adossé au ch. 18 ; renvoi ch. 50 (révocation dans le cycle de vie).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §13.1-13.3 | § 21.1-21.3 | condensé |
| Vol. III *Monographie* §14.1-14.3 | § 21.4-21.6 | condensé |

### Chapitre 22 — L'agentic SOC et la boucle défensive

**Thèse** : la défense s'agentifie elle-même, et l'identité distingue un SOC agentique gouvernable d'un système auto-organisé ingouvernable — les agents défensifs sont les premiers à devoir porter le passeport du ch. 17.
Sections : état de l'agentic SOC (offres datées, périmètres réels) ; symétrie attaque/défense relue par l'identité ; référentiels de sécurité agentique en mouvement (état 2026 ; ⚠ **relève v0.10** : une préimpression adverse de mai 2026 propose un durcissement structurel du runtime agentique — barrière d'admission des extensions, journal d'audit chaîné, garde de sortie, racine de confiance de signature de modules —, matériau candidat pour ce chapitre, à instruire et à ne pas confondre avec un référentiel adopté).
*Fusion : Vol. III ch. 15 + Vol. I* Monographie *§7.5 (trajectoire de la menace).*

**Table des matières détaillée du chapitre 22**

*Dérivée du texte rédigé de `Monographie.md` ch. 15 (Vol. III) et §7.5 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 22.1 — Le seuil franchi : l'attaque largement autonome est démontrée

*← Vol. I* Monographie *§7.5.1.* Tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF obligatoire — un seuil démontré n'est pas une généralisation.

#### § 22.2 — État de l'*agentic SOC* : offres datées, périmètres réels

*← Vol. III* Monographie *§15.1 + Vol. I* Monographie *§7.5.2.*

#### § 22.3 — La symétrie attaque/défense relue par l'identité

*← Vol. III* Monographie *§15.2 + Vol. I* Monographie *§7.5.2.* L'identité distingue un SOC agentique **gouvernable** d'un système auto-organisé ingouvernable : les agents défensifs sont les premiers à devoir porter le passeport du ch. 17.

#### § 22.4 — Référentiels de sécurité agentique en mouvement (état 2026)

*← Vol. III* Monographie *§15.3 + Vol. I* Monographie *§7.5.3.*

⚠ **Relève v0.10, à instruire** : une préimpression adverse de mai 2026 propose un durcissement structurel du *runtime* agentique — barrière d'admission des extensions, journal d'audit chaîné, garde de sortie, racine de confiance de signature de modules. **Matériau candidat, à ne pas confondre avec un référentiel adopté.**

#### § 22.5 — Vérification d'intégrité continue et confiance composable : l'agenda de recherche

*← Vol. I* Monographie *§7.5.4 ; prolonge le § 21.3.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §15.1-15.3 | § 22.2-22.4 | condensé |
| Vol. I *Monographie* §7.5.1-7.5.4 | § 22.1-22.5 | condensé |

**Troisième mouvement — l'horloge post-quantique (ch. 23-24)** *(anciennement Livre V ; provenance intégrée à l'en-tête du livre)*

### Chapitre 23 — La menace quantique appliquée à la pile identitaire agentique

**Thèse** : toute la fabrique d'émission (ch. 12-19) repose sur des signatures classiques ; les jalons du NIST IR 8547 — dépréciation **visée** pour 2030, retrait **visé** pour 2035 — tombent dans la durée de vie des architectures conçues aujourd'hui, la PQC est donc une contrainte de conception et non une annexe.
Sections : échéances et sources (⚠ **garde-fou R-11 du Vol. III** : écrire « visée », jamais « fixée » ni « ~2030 » ; et porter le **statut du document** — IR 8547 est au socle hérité un *Initial Public Draft*, avec réserve « dates à re-vérifier ». Les quatre statuts de l'Annexe D — annoncé / visé / attendu / incertain — s'appliquent ici comme ailleurs ; ⚠ **relève v0.7** : IR 8547 demeure un brouillon à mi-2026, mais des instruments fédéraux américains de juin 2026 — décret exécutif et directive OMB alignant les systèmes fédéraux sur les jalons 2030/2035 — en font une échéance **opposable** outre-frontière : enrichissement déclaré, sources primaires à extraire, qui durcit la contrainte de conception sans changer le statut du document ni la formulation « visée ») ; *harvest now, decrypt later* appliqué aux artefacts d'identité longue durée ; inventaire (quels artefacts cassent, et quand).
*Fusion : Vol. III ch. 16 + Vol. I* Monographie *§7.4.1.*

**Table des matières détaillée du chapitre 23**

*Dérivée du texte rédigé de `Monographie.md` ch. 16 (Vol. III) et §7.4.1 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 23.1 — Les échéances exactes et leurs sources

*← Vol. III* Monographie *§16.1 + Vol. I* Monographie *§7.4.1 (**SIÈGE de l'horloge** : la migration post-quantique comme contrainte de conception).*

⚠ **Garde-fou R-11 du Vol. III** : écrire « **visée** », jamais « fixée » ni « ~2030 » — dépréciation **visée** pour 2030, retrait **visé** pour 2035. Porter le **statut du document** : NIST IR 8547 est au socle hérité un *Initial Public Draft*, avec réserve « dates à re-vérifier ». Les quatre statuts de l'Annexe D — *annoncé / visé / attendu / incertain* — s'appliquent ici comme ailleurs.

⚠ **Relève v0.7, à instruire à la source primaire** : IR 8547 demeure un brouillon à mi-2026, mais des instruments fédéraux américains de juin 2026 (décret exécutif, directive OMB) alignent les systèmes fédéraux sur les jalons 2030/2035 — l'échéance devient **opposable outre-frontière**. Cela **durcit la contrainte de conception sans changer le statut du document ni la formulation « visée »**.

#### § 23.2 — *Harvest now, decrypt later* appliqué aux artefacts d'identité longue durée

*← Vol. III* Monographie *§16.2.*

#### § 23.3 — Inventaire : quels artefacts de la pile agentique cassent, et quand

*← Vol. III* Monographie *§16.3 ; porte sur la fabrique d'émission des ch. 12-19, qui repose entièrement sur des signatures classiques.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §16.1-16.3 | § 23.1-23.3 | condensé |
| Vol. I *Monographie* §7.4.1 | § 23.1 | **siège de l'horloge** |

### Chapitre 24 — Crypto-agilité et dette de migration

**Thèse** : la crypto-agilité est l'application des **trois premiers termes de l'invariant** (découplage, contrat, évolution — le quatrième, l'exploitation, est refermé au Livre VII) à la couche cryptographique ; la dette de migration PQC est réelle mais largement non chiffrée — méthode d'estimation plutôt que chiffre.
Sections : définition opérationnelle, état des recommandations NIST ; audit de crypto-agilité des mécanismes d'émission du présent livre (ch. 12-19) ; **méthode d'inventaire pour une institution** (Vol. III *TOC* §18.2 — la section qui porte la « méthode d'estimation plutôt que chiffre » annoncée à la thèse) ; patrons de migration sans rupture de chaîne de confiance ; ce que les études de coût couvrent (et pas) ; fenêtre d'action 2026-2029.
*Fusion : Vol. III ch. 17-18 + Vol. I* Monographie *§7.4.4 (l'horloge de l'horizon ; §7.4.2 et §7.4.3 sont aux ch. 17, ch. 14 et ch. 19). Garde-fou : refus d'extrapoler un chiffre non porté par le socle.*

**Table des matières détaillée du chapitre 24**

*Dérivée du texte rédigé de `Monographie.md` ch. 17-18 (Vol. III) et §7.4.4 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 24.1 — Définition opérationnelle et état des recommandations NIST

*← Vol. III* Monographie *§17.1.* La crypto-agilité est l'application des **trois premiers termes de l'invariant** — découplage, contrat, évolution — à la couche cryptographique ; **le quatrième, l'exploitation, est refermé au Livre VII** et n'est pas invoqué ici.

#### § 24.2 — Audit de crypto-agilité des mécanismes d'émission et du mandat

*← Vol. III* Monographie *§17.2 ; porte sur les ch. 12-19 du présent livre.*

#### § 24.3 — Patrons de migration sans rupture de la chaîne de confiance

*← Vol. III* Monographie *§17.3.*

#### § 24.4 — Ce que les études de coût publiées couvrent (et ne couvrent pas)

*← Vol. III* Monographie *§18.1 + Vol. I* Monographie *§7.4.4 (crypto-agilité et coût : la dette de migration de la couche agentique).* ⚠ **Garde-fou** : refus d'extrapoler un chiffre non porté par le socle — la dette est **réelle mais largement non chiffrée**.

#### § 24.5 — Méthode d'inventaire pour une institution

*← Vol. III* Monographie *§18.2 : c'est la section qui porte la « **méthode d'estimation plutôt que chiffre** » annoncée à la thèse.*

#### § 24.6 — Fenêtre d'action 2026-2029 : le calendrier inverse

*← Vol. III* Monographie *§18.3.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §17.1-17.3 | § 24.1-24.3 | condensé |
| Vol. III *Monographie* §18.1-18.3 | § 24.4-24.6 | condensé |
| Vol. I *Monographie* §7.4.4 | § 24.4 | condensé |

---

## LIVRE IV — Autonomie encadrée : orchestration en entreprise

*(fusionne Vol. II Partie II **hors ch. 8** — scindé au Livre III — + Vol. I ch. 4 **hors §4.8, §4.9 et §4.12** — partis aux Livres V, VII et VIII — + §1.6.3/§2.8.4 ; ~30 000 mots)*

### Chapitre 25 — Les options d'orchestration : la taxonomie OO1-OO4

**Thèse** : le choix d'architecture agentique est un choix de position sur un continuum d'encadrement, objectivable par cinq propriétés et sept critères.
Sections : OO1-OO4 ; cinq propriétés (autonomie, spécificité, réactivité, correction, traçabilité) ; critères de sélection ; métriques quantitatives (illustration — préprint) ; exécution durable et pipelines (du ch. 1).
*Fusion : Vol. II ch. 5 + Vol. I* Monographie *§1.6.3. Socle : F-37. Garde-fou : source unique (préprint v1). **Lacune héritée portée : PRD Vol. II §10.10** — OO1-OO4 repose sur une source unique et le *frame* opérationnel n'est pas caractérisé ; renvoi ch. 56.*

**Table des matières détaillée du chapitre 25**

*Dérivée du texte rédigé de `Monographie.md` ch. 5 (Vol. II) et §1.6.3 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 25.1 — Les quatre options d'orchestration (OO1-OO4)

*← Vol. II §5.1.*

#### § 25.2 — Les cinq propriétés d'évaluation

*← Vol. II §5.2 (autonomie, spécificité, réactivité, correction, traçabilité).*

#### § 25.3 — Les sept critères de sélection

*← Vol. II §5.3.*

#### § 25.4 — Les métriques quantitatives et les résultats expérimentaux

*← Vol. II §5.4.* ⚠ **Garde-fou : source unique (préprint v1)** — illustration, jamais preuve.

#### § 25.5 — Exécution durable, pipelines et orchestration agentique

*← Vol. I* Monographie *§1.6.3, **reçu en entier du ch. 1** :*

- 25.5.1 Moteurs BPMN et *workflow-as-code* à exécution durable — *← §1.6.3.1*
- 25.5.2 Continuum batch/streaming et orchestration de pipelines — *← §1.6.3.2*
- 25.5.3 Orchestration déterministe vs orchestration agentique — *← §1.6.3.3 ; charnière avec le § 25.1*

⚠ **Lacune héritée portée (PRD Vol. II §10.10)** : OO1-OO4 repose sur une **source unique** et le *frame* opérationnel n'est pas caractérisé ; renvoi ch. 56. La relève v0.10 signalée au ch. 26 (chaîne de règles à premier appariement gagnant) est un **cas**, jamais un fondement de cette taxonomie.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §5.1-5.4 | § 25.1-25.4 | condensé |
| Vol. I *Monographie* §1.6.3 | § 25.5 | **arrivée en entier** depuis le ch. 1 |

### Chapitre 26 — Le paradigme APM : l'autonomie encadrée

**Thèse** : l'autonomie n'est pas l'automatisation ; elle se gouverne par des frames normatifs et opérationnels et quatre capacités (encadrement, explicabilité, actionnabilité conversationnelle, auto-modification).
Sections : système APM, distinction autonomie/automatisation ; frames normatifs vs opérationnels ; quatre capacités ; frames locaux comme frontière de sécurité ; « responsibility gap » (préparé ici, exploité au ch. 33).
*Fusion : Vol. II ch. 6. Socle : F-36. Garde-fou : R-1 (mention ACP du manifeste antérieure à la fusion). ⚠ **Relève v0.10** : les harnais documentés en 2026 résolvent les permissions par une **chaîne ordonnée de règles à premier appariement gagnant** (refus par outil, auto-approbation globale, politique par outil, octrois de session par outil puis par catégorie, politique par catégorie, défaut : demander), avec des octrois **persistant d'une session à l'autre**. C'est la première réalisation concrète et datée d'un frame opérationnel — à instruire comme **cas**, jamais comme fondement de la taxonomie du ch. 25, dont le socle est déjà sous lacune §10.10 ; deux points à verser au ch. 18 et au ch. 29 : un octroi de catégorie qui survit à la session est un élargissement de mandat sans acte de délégation, et un mode d'auto-approbation globale n'est pas un contrôle au sens de la supervision attendue par E-23.*

**Table des matières détaillée du chapitre 26**

*Dérivée du texte rédigé de `Monographie.md` ch. 6 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 26.1 — Le système APM et la ligne de partage entre autonomie et automatisation

*← Vol. II §6.1.* ⚠ **Garde-fou R-1** : la mention ACP du manifeste est **antérieure à la fusion** — ne pas l'agréger aux autres emplois du sigle (encadré R-8, ch. 7).

#### § 26.2 — Frames normatifs, frames opérationnels, trois scénarios

*← Vol. II §6.2.*

⚠ **Relève v0.10, à instruire comme cas** : les harnais documentés en 2026 résolvent les permissions par une **chaîne ordonnée de règles à premier appariement gagnant** (refus par outil, auto-approbation globale, politique par outil, octrois de session par outil puis par catégorie, politique par catégorie, défaut : demander), avec des octrois **persistant d'une session à l'autre**. Première réalisation concrète et datée d'un *frame* opérationnel — **jamais un fondement de la taxonomie du ch. 25**, dont le socle est déjà sous lacune §10.10. Deux points à verser ailleurs : un **octroi de catégorie qui survit à la session est un élargissement de mandat sans acte de délégation** (ch. 18) ; un **mode d'auto-approbation globale n'est pas un contrôle** au sens de la supervision attendue par E-23 (ch. 29).

#### § 26.3 — Les quatre capacités requises

*← Vol. II §6.3 (encadrement, explicabilité, actionnabilité conversationnelle, auto-modification).*

#### § 26.4 — Les frames locaux comme frontière de sécurité

*← Vol. II §6.4.*

#### § 26.5 — L'écart de responsabilité, ou qui répond de ce que personne n'a décidé

*← Vol. II §6.5 ; **préparé ici, exploité au ch. 33** (imputabilité du comportement émergent).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §6.1-6.5 | § 26.1-26.5 | condensé |

### Chapitre 27 — Les frameworks d'orchestration d'entreprise

**Thèse** : l'offre s'est industrialisée en 2025-2026 (Agent Framework, LangGraph, orchestration événementielle Kafka/Confluent) avec un support MCP **répandu et inégalement établi** et un support A2A de périmètre inégal.
Sections : Microsoft Agent Framework ; LangGraph Platform (A2A pour la plateforme commerciale seulement) ; orchestration événementielle (Streaming Agents, A2A sur Kafka ; Confluent acquise par IBM, clôture 17 mars 2026) ; encadrés Temporal [C] et **CrewAI, à trois niveaux de preuve tenus séparés** (A2A élevé [B] sur source primaire extraite ; **MCP au repérage [C]** ; métriques d'adoption auto-déclarées) — ⚠ l'étiquette unique « CrewAI [B] » des v0.1-v0.5 écrase la distinction dont dépend le décompte « deux offres sur cinq de première main » qui fonde la thèse ; grille OO1-OO4 des patrons.
*Fusion : Vol. II ch. 7 + Vol. I* Monographie *§2.8.4. Socle : F-15, F-16, F-32, F-33, F-41. Garde-fou : PRD Vol. II §8.2.3 (chiffres d'éditeurs auto-déclarés). **Lacune héritée portée : PRD Vol. II §10.3** — réduite en P0, ne subsiste que Temporal, maintenu en [C].*

**Table des matières détaillée du chapitre 27**

*Dérivée du texte rédigé de `Monographie.md` ch. 7 (Vol. II) et §2.8.4 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 27.1 — Microsoft Agent Framework : la succession assumée

*← Vol. II §7.1 + Vol. I* Monographie *§2.8.4.2 (frameworks des grands fournisseurs : couplage, exécution, interop).*

#### § 27.2 — LangGraph Platform : la GA la plus ancienne, la frontière plateforme/bibliothèque

*← Vol. II §7.2 + Vol. I* Monographie *§2.8.4.1 (LangGraph et le graphe d'états).* ⚠ **A2A pour la plateforme commerciale seulement** — périmètre à ne pas élargir.

#### § 27.3 — L'orchestration événementielle : le journal avant le cadre

*← Vol. II §7.3 + Vol. I* Monographie *§2.8.4.3 (CrewAI Flows, LlamaIndex Workflows).* *Streaming Agents*, A2A sur Kafka ; **Confluent acquise par IBM, clôture le 17 mars 2026**.

#### § 27.4 — Deux cas en encadré : Temporal et CrewAI

*← Vol. II §7.4 + Vol. I* Monographie *§2.8.4.4 (exécution durable, garde-fous structurels, observabilité native).*

⚠ **CrewAI se tient à trois niveaux de preuve séparés** : A2A élevé **[B]** sur source primaire extraite ; **MCP au repérage [C]** ; métriques d'adoption **auto-déclarées**. L'étiquette unique « CrewAI [B] » des v0.1-v0.5 écrase la distinction dont dépend le décompte « **deux offres sur cinq de première main** » qui fonde la thèse. Temporal reste **[C]** (lacune PRD Vol. II §10.3, réduite en P0).

#### § 27.5 — Grille de lecture : ce que les patrons livrés positionnent, et ce qu'ils ne positionnent pas

*← Vol. II §7.5 ; grille OO1-OO4 du ch. 25 appliquée aux patrons.*

⚠ **Garde-fou (PRD Vol. II §8.2.3)** : chiffres d'éditeurs **auto-déclarés** — attribution à chaque occurrence. Le support MCP est **répandu et inégalement établi**, le support A2A **de périmètre inégal** : la thèse tient à cette double nuance.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §7.1-7.5 | § 27.1-27.5 | condensé |
| Vol. I *Monographie* §2.8.4 | § 27.1-27.4 | **arrivée** depuis le ch. 6 |

### Chapitre 28 — Le passage à l'échelle de l'entreprise

**Thèse** : de la dette d'intégration à la prolifération d'agents, l'entreprise doit intégrer les agents à son tissu existant, gouverner le parc à l'échelle et instruire sa maturité — sans dupliquer l'IAM et l'observabilité en place.
Sections : intégrer les agents au tissu d'intégration existant ; plateformes d'agents d'entreprise et stratégie de standards ouverts ; **identité et accès des agents à l'échelle du parc** (application du Livre III au grain de la plateforme, sans reconstruire leur doctrine) ; accès aux données d'entreprise et ancrage gouverné ; orchestration/collaboration humain-agent inter-équipes et B2B ; sécurité du parc à l'échelle ; capacité d'inférence, budget de latence et contention comme contraintes de dimensionnement ; adoption organisationnelle, modèle opérationnel, maturité.
*Fusion : Vol. I* Monographie *ch. 4 (§4.1-4.7, §4.10-4.11), le §4.4 (identité et accès à l'échelle) recevant enfin une section d'accueil. Le §4.8 (gouvernance/conformité) part au Livre V ; le §4.9 (observabilité/FinOps) au Livre VII ; le §4.12 (architectures de référence) au Livre VIII.*

**Table des matières détaillée du chapitre 28**

*Dérivée du texte rédigé de `Monographie.md` ch. 4 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 28.0 — L'enjeu d'entreprise : de la dette d'intégration à la prolifération d'agents

*← §4.1.1-4.1.4 (continuité et rupture de la dette ;* agent sprawl *et explosion des identités non humaines ; pilotes d'affaires et coût du statu quo).* ⚠ *L'encadré méthodologique §4.1.6 (« comment lire les chiffres de ce chapitre ») passe à la méthode unifiée (Annexe A) ; le mode d'emploi §4.1.5 est refondu en apparat.*

#### § 28.1 — Intégrer les agents au tissu d'intégration existant

*← §4.2.1-4.2.6 : modèle de référence de l'intégration agentique ; iPaaS comme fabrique de serveurs MCP ; API management, AI gateway et passerelle LLM (**domicile mécanique**) ; encapsuler le* legacy *par MCP ; event mesh et EDI agentiques ; catalogue et coexistence des serveurs MCP à l'échelle.*

#### § 28.2 — Plateformes d'agents d'entreprise et stratégie de standards ouverts

*← §4.3.1-4.3.5 : modèle de référence ; plateformes infusées dans la suite métier ; plateformes cloud horizontales ; jardins clos vs standards ouverts et anti-*lock-in* ; portabilité du modèle, TCO et ROI.*

#### § 28.3 — Identité et accès des agents à l'échelle du parc

*← §4.4.1-4.4.4 : cycle de vie de l'identité à l'échelle ; délégation multi-saut, autorisation fine, gestion des secrets ; plateformes d'identité d'agents et zero-trust ; **OWASP Non-Human Identities Top 10 (2025) comme grille de risque — domicile**.*

⚠ **Application du Livre III au grain de la plateforme, sans reconstruire sa doctrine** : la chaîne de mandat est au ch. 18, l'émission aux ch. 16-17. Le §4.4 **reçoit enfin une section d'accueil** — il n'en avait aucune avant la v0.5.

#### § 28.4 — Accès aux données d'entreprise et ancrage gouverné

*← §4.5.1-4.5.5 : du RAG-jouet à la connaissance d'entreprise gouvernée ; récupération consciente des permissions et mémoire de flotte (**domicile permissions**) ; couche sémantique, graphe de connaissances,* text-to-SQL *gouverné ; MCP gouverné et contrats de données pour agents ; observabilité de l'ancrage.*

#### § 28.5 — Orchestration et collaboration humain-agent inter-équipes et B2B

*← §4.6.1-4.6.4 : quand le multi-agent aide ou nuit à l'échelle ; trois échelles d'orchestration ; collaboration inter-organisations via A2A ; exécution durable et gestion des exceptions.*

#### § 28.6 — Sécurité du parc d'agents à l'échelle

*← §4.7.1-4.7.3 : modèle de menace du parc ; injection indirecte via les données d'entreprise et fuites zéro-clic ; DLP/egress, chaîne d'approvisionnement MCP et confinement.*

#### § 28.7 — Interopérabilité inter-entreprises (B2B), commerce agentique et écosystème

*← §4.10.1-4.10.4 : confiance inter-organisationnelle (KYA) et registres inter-firmes (**le siège du KYA est au ch. 19**) ; commerce et paiement agentiques B2B (**la pile est au ch. 10**) ;* data spaces *souverains et marketplaces ; responsabilité et modes d'échec à la frontière.*

#### § 28.8 — Capacité d'inférence, budget de latence et contention

contraintes de dimensionnement du parc. ⚠ **Construction d'auteur, marquée telle (décision 8, posé en v0.17)** : aucune sous-section du ch. 4 du Vol. I ne porte cet objet — les appuis les plus proches sont le §4.3.5 (TCO et ROI) et le §4.6.1 (quand le multi-agent aide ou nuit à l'échelle), qui l'abordent par le coût et non par le dimensionnement. **Sources primaires à établir avant rédaction** ; à défaut, la section se replie sur ces deux appuis et cesse d'être autonome.

#### § 28.9 — Adoption organisationnelle, modèle opérationnel et maturité

*← §4.11.1-4.11.4 : CdE agentique et* hub-and-spoke *; transposition LCIM → agents (**propriétaire**) ; conduite du changement, compétences, droit social ; gouvernance socio-technique, redevabilité et déqualification.*

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §4.1 | § 28.0 | condensé ; §4.1.5-4.1.6 refondus en apparat |
| §4.2 | § 28.1 | condensé |
| §4.3 | § 28.2 | condensé |
| §4.4 | § 28.3 | condensé — **section d'accueil obtenue en v0.5** |
| §4.5 | § 28.4 | condensé |
| §4.6 | § 28.5 | condensé |
| §4.7 | § 28.6 | condensé |
| §4.8 | ch. 34 (Livre V) | hors périmètre |
| §4.9 | Livre VII | hors périmètre (observabilité, FinOps) |
| §4.10 | § 28.7 | condensé |
| §4.11 | § 28.9 | condensé |
| §4.12 | Livre VIII | hors périmètre (architectures de référence) |

⚠ **Écart résolu en v0.17** — le § 28.8 ne correspondant à aucune sous-section nommée du ch. 4 du Vol. I, il est **marqué construction d'auteur** (décision 8) plutôt que rattaché de force à une source qui ne le porte pas. C'est le seul emplacement de ce chapitre sans provenance.

---

## LIVRE V — Cadre réglementaire canadien

*(fusionne Vol. II Partie III + Vol. III Partie VI + Vol. I §4.8/§5.3 ; ~25 000 mots)*

### Chapitre 29 — E-23 : le risque de modèle à l'ère de l'IA

**Thèse** : E-23 couvre l'IA agentique *implicitement*, par sa définition de « modèle » — couverture par inférence que les institutions doivent traiter comme acquise d'ici le 1ᵉʳ mai 2027 ; l'identité agentique est le prérequis technique d'obligations qui ne la mentionnent pas.
Sections : genèse et calendrier ; définition de « modèle » et anticipation des systèmes autonomes ; l'inférence agentique ; le registre du ch. 16 comme condition d'inventaire ; la surveillance continue **attendue** par E-23 et la limite empirique de la supervision humaine (ch. 18) — ⚠ **formulation imposée, PRD Vol. II §7.3 et PRDPlan Vol. II §4.4** : écrire « attendu par E-23 », **jamais** « exigé par E-23 » ni « E-23 impose » (ligne fondée sur des principes, rédigée au conditionnel) ; et les cinq attentes au socle sont cycle de vie, inventaire, cotation, documentation et surveillance continue — **la « supervision humaine » n'en est pas une** ; **ce que les cadres n'exigent pas — ne pas leur faire dire plus** (Vol. III *TOC* §19.3) ; rapport BSIF-ACFC (risque de causalité indéterminable).
*Fusion : Vol. II ch. 9 + Vol. III ch. 19, **volet E-23 seul** — la relecture de la ligne directrice AMF par la grille des cinq questions (§19.1, seconde moitié) va au ch. 31, qui est son siège. Socle : F-09 (les deux strates), F-10. Garde-fous : PRD Vol. II §8.2.4 (couverture E-23 = inférence d'analystes) et PRD Vol. II §8.2.6 (projections).*

**Table des matières détaillée du chapitre 29**

*Dérivée du texte rédigé de `Monographie.md` ch. 9 (Vol. II) et ch. 19 (Vol. III) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 29.1 — Genèse et calendrier

*← Vol. II §9.1 ; entrée en vigueur au 1ᵉʳ mai 2027.*

#### § 29.2 — La définition de « modèle » et l'anticipation des systèmes autonomes

*← Vol. II §9.2.*

#### § 29.3 — L'inférence agentique

*← Vol. II §9.3.* ⚠ **Garde-fou (PRD Vol. II §8.2.4)** : la couverture agentique d'E-23 est une **inférence d'analystes juridiques** — écrire « couverture implicite via la définition de modèle », **jamais** « le BSIF exige pour l'IA agentique ».

#### § 29.4 — Relecture d'E-23 par la grille des cinq questions

*← Vol. III* Monographie *§19.1, **moitié E-23 seule** — la moitié AMF va au ch. 31, qui en est le siège.*

#### § 29.5 — Le registre du ch. 16 comme pièce de conformité

*← Vol. III* Monographie *§19.2 ; l'identité agentique est le **prérequis technique d'obligations qui ne la mentionnent pas**.*

#### § 29.6 — La surveillance continue attendue par E-23, et la limite empirique de la supervision humaine

renvoi au ch. 18 § 18.5 (biais d'automatisation).

⚠ **Formulation imposée (PRD Vol. II §7.3 et PRDPlan Vol. II §4.4)** : écrire « **attendu** par E-23 », **jamais** « exigé par E-23 » ni « E-23 impose » — ligne fondée sur des principes, rédigée au conditionnel.

⚠ **Les cinq attentes au socle sont : cycle de vie, inventaire, cotation, documentation, surveillance continue. La « supervision humaine » n'en est pas une** — ne pas l'ajouter à la liste.

#### § 29.7 — Ce que les cadres n'exigent pas — ne pas leur faire dire plus

*← Vol. III* Monographie *§19.3.*

#### § 29.8 — Le rapport BSIF-ACFC : une trajectoire déclarée et une causalité indéterminable

*← Vol. II §9.4.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §9.1-9.4 | § 29.1-29.3, § 29.8 | condensé |
| Vol. III *Monographie* §19.1 | § 29.4 | **moitié E-23** — moitié AMF au ch. 31 |
| Vol. III *Monographie* §19.2-19.3 | § 29.5, § 29.7 | condensé |

### Chapitre 30 — Le vide fédéral : de C-27 à C-36

**Thèse** : la mort de la LIAD laisse le Canada sans régulation fédérale spécifique de l'IA ; C-36 (loi sur la vie privée, non loi IA autonome) ne comble pas ce vide — la couverture effective passe par les régulateurs sectoriels.
Sections : prorogation du 6 janvier 2025, mort de C-27 ; ministre de l'IA et C-36 (réforme LPRPDE, *Digital Safety and Data Protection Commission*) ; conséquences pour les institutions financières.
*Fusion : Vol. II ch. 10. Socle : F-24 [B, revalidé].*

**Table des matières détaillée du chapitre 30**

*Dérivée du texte rédigé de `Monographie.md` ch. 10 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 30.1 — La prorogation du 6 janvier 2025 et la mort de C-27

*← Vol. II §10.1 ; fin de la LIAD.*

#### § 30.2 — Le ministre de l'IA et le projet de loi C-36

*← Vol. II §10.2 : réforme de la LPRPDE,* Digital Safety and Data Protection Commission. ⚠ **C-36 est une loi sur la vie privée, non une loi IA autonome** — elle ne comble pas le vide.

#### § 30.3 — Conséquences : le vide persiste, la charge est sectorielle

*← Vol. II §10.3 ; la couverture effective passe par les régulateurs sectoriels (ch. 29, 31, 32).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §10.1-10.3 | § 30.1-30.3 | condensé |

### Chapitre 31 — Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25

**Thèse** *(prolonge Q4 de la série d'agenda du Vol. II — Monographie ch. 21 §21.2 — **sans la trancher**)* : le Québec dispose du cadre le plus explicite ; l'art. 12.1 (révision humaine sur demande) entre en friction directe avec la décision agentique autonome, et son imputabilité pèse sur l'assujetti.
Sections : ligne directrice AMF (**finale le 30 mars 2026** — divergence tranchée, voir Annexe C ; en vigueur 1ᵉʳ mai 2027 ; ⚠ **seules ses dates sont au socle, jamais son contenu** — lacune PRD Vol. II §10.4, la plus coûteuse du volume, à rouvrir par extraction de la source primaire avant rédaction ; ne jamais écrire « en attente », réserve F-25) ; art. 12.1 (trois obligations, texte officiel) ; critère « exclusivement » et HITL (nuance Fasken vs CAI ; le biais d'automatisation du ch. 18 comme limite empirique de la parade) ; la ligne directrice AMF relue par la grille des cinq questions (Vol. III *TOC* §19.1) ; le mandat en droit civil québécois (Vol. III *TOC* §20.2 ; la limite de l'analogie est au ch. 18) ; le droit des renseignements personnels et la chaîne de délégation (qui traite, qui décide, qui répond).
*Fusion : Vol. II ch. 11 + Vol. III ch. 20 (**en entier** — ⚠ **corrigé en v0.17** : les v0.1-v0.16 écrivaient « volet Loi 25 seul, le volet RGPD va au ch. 34 », partage devenu sans objet depuis que le Vol. III rédigé a **retiré le RGPD de son ch. 20** le 22 juillet 2026, arbitrage **R-G-38** ; le plan s'aligne sur le chapitre rédigé, décision 8) + Vol. III ch. 19 §19.1 (moitié AMF). ⚠ **Siège de Q4** : le Vol. III déclare que son ch. 20 « prolonge Q4 du Vol. II — l'applicabilité de l'art. 12.1 à la décision multi-agents avec humain-dans-la-boucle — sans la trancher » ; les v0.1-v0.4 nommaient Q2, Q3 et Q5 de la même série et **laissaient Q4 sans chapitre d'accueil**, alors que sa matière arrivait ici avec le ch. 20 du Vol. III. La question est instruite, non tranchée : le §20.3 du Vol. III est une « cartographie des lectures, sans verdict », et cette forme est reconduite. Socle : F-25, F-27. Garde-fou renforcé : aucun avis juridique ; ⚠ la position « finale le 30 mars 2026 » porte une **dette de vérification déclarée** au Vol. II (source primaire renvoyant 403 aux outils employés le 17 juillet 2026) — la divergence est tranchée, la vérification reste due.*

**Table des matières détaillée du chapitre 31**

*Dérivée du texte rédigé de `Monographie.md` ch. 11 (Vol. II) et ch. 19-20 (Vol. III) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 31.1 — La ligne directrice IA de l'AMF : chronologie et convergence

*← Vol. II §11.1.*

⚠ **Divergence tranchée (Annexe C)** : **finale le 30 mars 2026**, en vigueur le 1ᵉʳ mai 2027 — ne **jamais** écrire « en attente » (réserve F-25). ⚠ **Dette de vérification déclarée** : la source primaire renvoyait 403 aux outils employés le 17 juillet 2026 — la divergence est tranchée, la vérification reste **due**.

⚠ **Seules ses dates sont au socle, jamais son contenu** — lacune **PRD Vol. II §10.4**, la plus coûteuse du volume, à rouvrir par extraction de la source primaire **avant rédaction**.

#### § 31.2 — L'article 12.1 : trois obligations, un texte

*← Vol. II §11.2 (texte officiel).*

#### § 31.3 — Le critère « exclusivement » et l'humain-dans-la-boucle

*← Vol. II §11.3 (nuance Fasken vs CAI) ; le biais d'automatisation du ch. 18 § 18.5 en est la **limite empirique**.*

#### § 31.4 — L'article 12.1 et la décision automatisée multi-agents : état des positions

*← Vol. III* Monographie *§20.1.*

#### § 31.5 — La ligne directrice AMF relue par la grille des cinq questions

*← Vol. III* Monographie *§19.1, **moitié AMF — ce chapitre en est le siège** ; la moitié E-23 est au ch. 29. Le Vol. III désigne le §19.1 comme **seul siège d'application de la grille pour sa Partie VI**.*

#### § 31.6 — Le mandat agentique en droit civil québécois : ce que l'analogie porte

*← Vol. III* Monographie *§20.2 ; **la limite de l'analogie est au ch. 18** § 18.3.*

#### § 31.7 — Cartographie des lectures, sans verdict

*← Vol. III* Monographie *§20.3.* ⚠ **Siège de Q4** de la série d'agenda du Vol. II (*Monographie* ch. 21 §21.2) : la question est **instruite, non tranchée**, et cette forme est reconduite.

#### § 31.8 — Conséquences d'architecture

*← Vol. II §11.4 ; qui traite, qui décide, qui répond.*

⚠ **Garde-fou renforcé : aucun avis juridique.** ⚠ **Thèse du Vol. III amendée le 22 juillet 2026 (R-G-37)** : le droit des renseignements personnels **raisonne par exploitant d'entreprise** (F-89 du Vol. III, [B]) — la dichotomie « responsable / mandataire » n'est portée par aucune entrée du socle et se traite comme **construction à instruire**, non comme acquis.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §11.1-11.4 | § 31.1-31.3, § 31.8 | condensé |
| Vol. III *Monographie* §19.1 | § 31.5 | **moitié AMF** — siège de la grille |
| Vol. III *Monographie* §20.1-20.3 | § 31.4, § 31.6-31.7 | condensé — **chapitre 20 en entier** (voir écart au ch. 34) |

### Chapitre 32 — Valeurs mobilières : l'avis ACVM 11-348

**Thèse** : les lois existantes s'appliquent — la définition retenue des systèmes d'IA (autonomie et adaptativité variables) capture nativement l'agentique.
Sections : portée et doctrine (« ne crée ni ne modifie aucune exigence ») ; attentes (gouvernance, explicabilité, supervision) ; suites de la consultation.
*Fusion : Vol. II ch. 12. Socle : F-26.*

**Table des matières détaillée du chapitre 32**

*Dérivée du texte rédigé de `Monographie.md` ch. 12 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 32.1 — Portée et doctrine : ce que l'avis dit qu'il ne fait pas

*← Vol. II §12.1.* L'avis « **ne crée ni ne modifie aucune exigence** » : les lois existantes s'appliquent.

#### § 32.2 — La définition comme accroche : autonomie et adaptativité

*← Vol. II §12.2 ; la définition retenue (autonomie et adaptativité **variables**) capture nativement l'agentique.*

#### § 32.3 — Les suites de la consultation

*← Vol. II §12.3 ; attentes de gouvernance, explicabilité et supervision.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §12.1-12.3 | § 32.1-32.3 | condensé |

### Chapitre 33 — Le pont : des contraintes réglementaires aux frames déterministes

**Thèse** *(pivot)* : la plupart des exigences canadiennes lues se traduisent en frame d'architecture ; l'encadrement déterministe des processus réglementés est le principe sur lequel convergent trois sources **non indépendantes**, dont le socle n'établit l'application ni au Canada ni à la finance canadienne — la portée de la convergence, pas son autorité majorée.
Sections : table de traduction exigences → frames (**onze entrées au Vol. II, dont neuf produisent une contrainte** ; ⚠ la ligne AMF y est la seule qui n'en produit **aucune**, faute de contenu au socle — l'écrire, ne pas la combler ; ⚠ **ces deux cardinaux sont ceux du Vol. II et ne se recopient pas** : la refonte du socle à l'Annexe B peut en changer, et le chapitre pose lui-même que « la densité de contraintes dérivables d'un texte mesure ce que le socle en a extrait, non son exigence propre » — le compte se re-mesure à la rédaction) ; verdict empirique (F-37) et convergence à trois sources (F-36, F-37, F-46) ; imputabilité (qui répond du comportement émergent) ; énoncé du principe directeur repris aux Livres VIII et X.
*Fusion : Vol. II ch. 13 (chapitre-pivot conservé intact). Socle : F-09 (deux strates), F-25, F-26, F-27, F-36, F-37, F-46 ; F-10, F-35 en renvoi.*

**Table des matières détaillée du chapitre 33**

*Dérivée du texte rédigé de `Monographie.md` ch. 13 (Vol. II) le 25 juillet 2026. **Chapitre-pivot conservé intact** — la structure du Vol. II est reprise sans redécoupage. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 33.1 — La table de traduction : ce que les exigences imposent aux frames

*← Vol. II §13.1.*

⚠ **Onze entrées au Vol. II, dont neuf produisent une contrainte** ; **la ligne AMF est la seule qui n'en produit aucune**, faute de contenu au socle — l'écrire, **ne pas la combler**.

⚠ **Ces deux cardinaux sont ceux du Vol. II et ne se recopient pas** : la refonte du socle à l'Annexe B peut en changer, et le chapitre pose lui-même que « la densité de contraintes dérivables d'un texte mesure ce que le socle en a extrait, non son exigence propre ». **Le compte se re-mesure à la rédaction.**

#### § 33.2 — Le verdict empirique et la convergence à trois sources

*← Vol. II §13.2 (F-37 ; convergence F-36, F-37, F-46).* ⚠ **Trois sources non indépendantes** — le socle n'établit l'application ni au Canada ni à la finance canadienne : c'est la **portée** de la convergence, pas son autorité majorée.

#### § 33.3 — L'imputabilité : qui répond du comportement émergent ?

*← Vol. II §13.3 ; exploite l'écart de responsabilité préparé au ch. 26 § 26.5.*

#### § 33.4 — Le principe directeur

*← Vol. II §13.4 ; énoncé repris aux Livres VIII et X.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §13.1-13.4 | § 33.1-33.4 | **intact** (chapitre-pivot) |

### Chapitre 34 — Le maillage réglementaire international et la normalisation institutionnelle

**Thèse** : hors Canada, l'AI Act, ISO 42001, le RGPD et les cadres sectoriels dessinent le maillage transversal que l'agent en finance régulée doit satisfaire ; et la désignation de l'organisme de normalisation technique du cadre bancaire canadien fixera qui écrit les règles d'identité des agents financiers.
Sections : gouvernance et conformité d'entreprise (AI Act, ISO 42001, RGPD, sectoriel — du Vol. I *Monographie* §4.8) ; maillage réglementaire UE/US/Canada-Québec et double-qualification agent = modèle + tiers TIC (Vol. I *Monographie* §5.3) ; normalisation institutionnelle du cadre bancaire (Q5 de la série d'agenda du Vol. II — *Monographie* ch. 21 §21.2) ; normalisation internationale (ISO/IEC SC 42, CEN-CENELEC, NIST) appliquée à l'identité d'agent.
*Fusion : Vol. III ch. 21 + Vol. I* Monographie *§4.8/§5.3/§2.11.3 (gouvernance par les normes) + Vol. II ch. 21 §21.2 (Q5). ⚠ **Corrigé en v0.17 — le « volet RGPD » du ch. 20 du Vol. III est retiré de cette ligne : il n'existe plus.** Les v0.1-v0.16 l'y portaient ; le Vol. III rédigé a retiré le RGPD de son ch. 20 le 22 juillet 2026 (arbitrage **R-G-38**), son socle « ne documentant pas le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation*, degré 3, **non** fait négatif vérifié — et « aucun rapprochement entre le régime québécois et le régime européen n'y est opéré ». **Le chapitre ne perd aucune matière** : son RGPD est porté par le Vol. I (§4.8.4 et §5.3), intact. La lacune correspondante du Vol. III (**sa lacune 16**) entre au registre de l'Annexe C.* Instruit la lacune PRD Vol. II §10.1 (aucun arrêté au 16 juill. 2026). Garde-fou : R-5 du Vol. II.*

**Table des matières détaillée du chapitre 34**

*Dérivée du texte rédigé de `Monographie.md` ch. 21 (Vol. III), §4.8/§5.3/§2.11.3 (Vol. I) et ch. 21 §21.2 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 34.1 — Gouvernance et conformité d'entreprise

*← Vol. I* Monographie *§4.8 + §2.11.3 (gouvernance par les normes et réglementation) :*

- 34.1.1 Qualification des agents sous l'AI Act et calendrier d'application — *← §4.8.1*
- 34.1.2 Normes volontaires : ISO/IEC 42001, famille 42000, NIST AI RMF — *← §4.8.2*
- 34.1.3 Inventaire/registre d'agents et *policy-as-code* — *← §4.8.3 ; le registre comme pièce de conformité est au ch. 29 § 29.5*
- 34.1.4 **RGPD pour agents autonomes** et réglementation sectorielle — *← §4.8.4* ⚠ voir écart
- 34.1.5 Résidence/souveraineté, responsabilité, *e-discovery* et modèle opérationnel de gouvernance — *← §4.8.5*

#### § 34.2 — Maillage réglementaire transversal UE / US / Canada-Québec

*← Vol. I* Monographie *§5.3 :*

- 34.2.1 La grille de qualification multiple : système TIC / modèle / décision automatisée — *← §5.3.1.* ⚠ **Le SIÈGE de la double-qualification est le §5.1.4, au ch. 35** ; le §5.3 déclare lui-même ne faire que l'**instancier** — ne pas la reposer ici.
- 34.2.2 DORA et la résilience opérationnelle : l'agent comme service TIC — *← §5.3.2*
- 34.2.3 AI Act Annexe III : haut-risque ciblé et report adopté — *← §5.3.3*
- 34.2.4 Risque-modèle : la divergence transatlantique — *← §5.3.4 ; à lire contre le ch. 29 (E-23)*
- 34.2.5 Conduite et marchés : MiFID II, *suitability*, MiCA — *← §5.3.5*
- 34.2.6 AML/CTF et capital : *single rulebook* 2027, AMLA, Bâle III — *← §5.3.6*
- 34.2.7 L'axe Canada / Québec (couverture explicite imposée) — *← §5.3.7 ; renvois ch. 29-32*

#### § 34.3 — La normalisation institutionnelle et le cadre bancaire canadien

- 34.3.1 État de la désignation — *← Vol. III* Monographie *§21.1 + **Q5** de la série d'agenda du Vol. II (*Monographie* ch. 21 §21.2).* ⚠ **Instruit la lacune PRD Vol. II §10.1** : aucun arrêté ministériel au 16 juillet 2026 — l'écrire, ne pas la combler. **Garde-fou R-5 du Vol. II.**
- 34.3.2 Scénarios et leurs conséquences sur la pile identitaire — *← Vol. III* Monographie *§21.2.* La désignation fixera **qui écrit les règles d'identité des agents financiers**.
- 34.3.3 Normalisation internationale appliquée à l'identité d'agent — *← Vol. III* Monographie *§21.3 (ISO/IEC SC 42, CEN-CENELEC, NIST).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §21.1-21.3 | § 34.3 | condensé |
| Vol. III *Monographie* ch. 20 | **ch. 31 en entier** | voir écart — le « volet RGPD » n'existe plus |
| Vol. I *Monographie* §4.8 | § 34.1 | condensé |
| Vol. I *Monographie* §5.3 | § 34.2 | condensé ; siège de la double-qualification au ch. 35 |
| Vol. I *Monographie* §2.11.3 | § 34.1 | **arrivée** depuis le ch. 6 |
| Vol. II ch. 21 §21.2 (Q5) | § 34.3.1 | condensé |

⚠ **Écart résolu en v0.17, et c'était le plus lourd de ce livre — le « volet RGPD » du ch. 20 du Vol. III n'existe plus.** La ligne Fusion répartit le ch. 20 du Vol. III entre le ch. 31 (« volet Loi 25 seul ») et ce chapitre (« volet RGPD »). Or le Vol. III **rédigé** a retiré le RGPD de ce chapitre le **22 juillet 2026**, par l'arbitrage **R-G-38** : son titre nommait le RGPD jusqu'à cette date, et l'avertissement de portée du §20 pose désormais que « **le socle ne documente pas le règlement général sur la protection des données ni aucun de ses articles** » — *absence de documentation* (degré 3), **non** fait négatif vérifié —, que « **aucun rapprochement entre le régime québécois et le régime européen n'est donc opéré ici** », et que la lacune est portée au PRD du Vol. III **sous le numéro 16** (« non instruite — absent du socle et du programme de constitution »).

**Conséquences — *(a)* et *(c)* appliquées en v0.17, *(b)* est un constat :** *(a)* le ch. 31 reçoit le ch. 20 du Vol. III **en entier**, sa mention « volet Loi 25 **seul** » étant sans objet — **ligne Fusion corrigée** ; *(b)* la matière RGPD de ce chapitre est portée par le **Vol. I** (§4.8.4 et §5.3), qui est intact — **le chapitre ne perd rien**, seule sa ligne de provenance désignait une source vide, et elle est corrigée ; *(c)* la **lacune 16 du Vol. III** est **entrée au registre de l'Annexe C**, dans une seconde table distincte de celle des onze lacunes du Vol. II — mélanger les deux séries périmerait un cardinal contrôlé (décision 7). C'est la classe d'écart que la **collation de fond** contre le Vol. III rédigé — préalable déclaré, dont la v0.14 n'a levé que le volet structurel — a précisément pour objet de trouver.

---

## LIVRE VI — Terrain canadien : interopérabilité financière et adoption

*(fusionne Vol. II Parties IV-V + Vol. I ch. 5 **hors §5.0, §5.3, §5.5.4 et §5.12.1-5.12.3** — partis à l'avant-propos et aux ch. 34, ch. 19 et ch. 47 ; ~35 000 mots)*

### Chapitre 35 — Le vertical financier : pourquoi l'agentique y est durcie

**Thèse** : la finance durcit l'agentique par des contraintes transverses (standards de données, maillage réglementaire, risque-modèle, sécurité/AML-KYC/KYA, résidence/souveraineté) qui préexistent à l'agent et le contraignent.
Sections : positionnement du vertical et rappel des quatre durcisseurs (posés à l'avant-propos) ; standards de données financières (substrat sémantique) ; risque-modèle, auditabilité, explicabilité ; sécurité, fraude, AML-KYC et identité d'agent ; données, résidence et souveraineté.
*Fusion : Vol. I* Monographie *§5.1-5.6 **hors §5.3** (maillage réglementaire transversal), consolidé au ch. 34 — double affectation relevée à la collation contre les volumes complets. ⚠ Le **§5.1.4 est le SIÈGE déclaré** de la double-qualification (l'agent comme modèle *et* comme tiers TIC) : il se traite ici en entier, le ch. 34 ne faisant que l'instancier, comme le §5.3 lui-même le pose. Le §5.0 (orientation, durcisseurs, convention de sourçage) est **acheminé à l'avant-propos**, dont il fournit le mode d'emploi de lecture. Le §5.5.4 (KYA) est déjà consolidé au ch. 19 — les §5.5.1-5.5.3 (triade létale, fraude, AML-KYC) restent ici ; cadrage financier transverse.*

**Table des matières détaillée du chapitre 35**

*Dérivée du texte rédigé de `Monographie.md` §5.1-5.6 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 35.1 — Le vertical financier : positionnement

- 35.1.1 Irréversibilité et finalité du règlement comme contrainte de conception — *← §5.1.1 (**SIÈGE du patron**)*
- 35.1.2 Capital, risque systémique et agents corrélés — *← §5.1.2 (**SIÈGE du risque systémique**)*
- 35.1.3 Confiance, responsabilité et conduite — *← §5.1.3*
- 35.1.4 **La double-qualification : l'agent comme MODÈLE et comme TIERS TIC** — *← §5.1.4 (**SIÈGE du patron-signature**).* ⚠ **Se traite ici en entier** : le ch. 34 ne fait que l'instancier, comme le §5.3 le pose lui-même.

#### § 35.2 — Standards de données financières : le substrat sémantique

- 35.2.1 Le découpage en trois couches : messagerie / modèle-capacité / ontologie — *← §5.2.1*
- 35.2.2 ISO 20022 : la bascule de novembre 2025 comme événement structurant — *← §5.2.2 ; détail au ch. 37*
- 35.2.3 BIAN, FIBO et l'ontologie comme garde-fou déterministe — *← §5.2.3*
- 35.2.4 CDM/DRR et FIX Orchestra : du standard de donnée au standard de **logique exécutable** — *← §5.2.4*
- 35.2.5 ACORD, FDX et MISMO — *← §5.2.5 ; le cadre bancaire est au ch. 36*
- 35.2.6 État réel des serveurs MCP et connecteurs sectoriels — *← §5.2.6 (**SIÈGE du critère anti-hype**)*

#### § 35.3 — Risque-modèle, auditabilité et explicabilité appliqués aux agents

- 35.3.1 « Si l'agent décide, c'est un modèle » : l'inventaire comme premier contrôle — *← §5.4.1 ; pont vers E-23, ch. 29*
- 35.3.2 Piste d'audit infalsifiable et *e-discovery* réglementaire — *← §5.4.2*
- 35.3.3 Le standard ouvert de référence : FINOS AI Governance Framework v2.0 — *← §5.4.3*
- 35.3.4 Ségrégation des tâches, *four-eyes* et indépendance anti-collusion — *← §5.4.4 (**SIÈGE du four-eyes**)*

#### § 35.4 — Sécurité, fraude, AML-KYC et identité d'agent

- 35.4.1 La triade létale rencontre l'irréversibilité financière — *← §5.5.1 ; la triade est posée au ch. 20*
- 35.4.2 Fraude amplifiée par l'IA : *deepfakes*, *APP fraud* et rails instantanés — *← §5.5.2*
- 35.4.3 AML/KYC exécutés par des agents : le cas d'usage tête de pont — *← §5.5.3 (**SIÈGE du patron AML**)*

⚠ *Le §5.5.4 (**SIÈGE unique du KYA**) est **déjà consolidé au ch. 19** et n'est pas repris ici.*

#### § 35.5 — Données, résidence et souveraineté en finance régulée

- 35.5.1 La résidence doit couvrir l'inférence, les *embeddings*, les traces **et** les journaux d'audit — *← §5.6.1*
- 35.5.2 Offres de cloud souverain et risque de concentration — *← §5.6.2*

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §5.0 | **avant-propos** | acheminé (durcisseurs, patron directeur, sourçage) |
| §5.1 | § 35.1 | condensé — §5.1.4 en entier, siège |
| §5.2 | § 35.2 | condensé |
| §5.3 | ch. 34 | hors périmètre (maillage réglementaire) |
| §5.4 | § 35.3 | condensé |
| §5.5.1-5.5.3 | § 35.4 | condensé |
| §5.5.4 | ch. 19 | hors périmètre (siège du KYA) |
| §5.6 | § 35.5 | condensé |

### Chapitre 36 — Le cadre des services bancaires axés sur le consommateur

**Thèse** : le cadre est légiféré (C-15), supervisé par la Banque du Canada, réglementairement en cours — et son standard technique n'est **pas** désigné (fait négatif vérifié).
Sections : de 2024 à C-15 (mobilité des données) ; supervision Banque du Canada, accréditation, registre ; règlement prépublié (27 juin 2026, entrée échelonnée) ; le standard technique (organisme à désigner par arrêté — FDX = anticipation d'industrie).
*Fusion : Vol. II ch. 14. Socle : F-11, F-23, F-34, F-35. Garde-fou : R-5 du Vol. II. **Lacune héritée portée : PRD Vol. II §10.11** — F-11 attribue au Budget fédéral 2025 un fait structurant du cadre sans le dater ; lacune ouverte le 17 juillet 2026 à la construction de la frise, donc **après** la table de couverture du TOC du Vol. II, ce qui explique qu'elle en soit absente ; renvoi Annexe D.*

**Table des matières détaillée du chapitre 36**

*Dérivée du texte rédigé de `Monographie.md` ch. 14 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 36.1 — De la loi partielle de 2024 à C-15 : abrogation, remplacement, mobilité des données

*← Vol. II §14.1.*

#### § 36.2 — La Banque du Canada, l'accréditation et le registre

*← Vol. II §14.2 ; le registre d'agents du ch. 16 en est distinct — ne pas les confondre.*

#### § 36.3 — Le règlement prépublié : ce qui est écrit, ce qui peut encore changer

*← Vol. II §14.3 (prépublication du 27 juin 2026, entrée échelonnée).*

#### § 36.4 — Le standard technique : un fait négatif, *vérifié*

*← Vol. II §14.4.* ⚠ L'organisme reste **à désigner par arrêté** ; **FDX est une anticipation d'industrie**, non une désignation. **Garde-fou R-5 du Vol. II.** Distinguer ce *fait négatif vérifié* de la simple absence de documentation (échelle R-14 du Vol. III).

⚠ **Lacune héritée portée (PRD Vol. II §10.11)** : F-11 attribue au **Budget fédéral 2025** un fait structurant du cadre **sans le dater**. Lacune ouverte le 17 juillet 2026 à la construction de la frise — donc **après** la table de couverture du TOC du Vol. II, ce qui explique qu'elle en soit absente ; renvoi Annexe D.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §14.1-14.4 | § 36.1-36.4 | condensé |

### Chapitre 37 — ISO 20022 : Lynx accompli, RTR visé

**Thèse** : la couche sémantique commune des paiements canadiens est en place — Lynx a achevé sa bascule ; Paiements Canada annonce un RTR nativement ISO 20022 dès son lancement, **visé** au T4 2026 (cible plusieurs fois repoussée — attribuer, ne pas affirmer au futur catégorique).
Sections : Lynx (fin de coexistence MT/MX, 22 nov. 2025, alignée CBPR+) ; RTR (chronologie vérifiée, partenaires, cible T4 2026 ; ⚠ **formulation imposée — « la cible a été successivement reportée : 2019, puis 2022, puis 2023, puis 2026 » : ce sont quatre *cibles successives*, non quatre reports ni les dates auxquelles les reports ont été décidés** — PRDPlan Vol. II §4.4) ; By-law no 10 ; ce que la couche sémantique change — et ce que le socle n'en dit pas.
*Fusion : Vol. II ch. 15. Socle : F-28, F-29, F-45. Garde-fous : R-4 (la cible T4 2026 *est* officiellement annoncée) et réserve F-29 (ne jamais écrire « lancé » ni « en production »).*

**Table des matières détaillée du chapitre 37**

*Dérivée du texte rédigé de `Monographie.md` ch. 15 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 37.1 — Lynx : une migration achevée, et ce que cela veut dire

*← Vol. II §15.1 ; fin de coexistence MT/MX le 22 novembre 2025, alignée CBPR+.*

#### § 37.2 — RTR : une chronologie vérifiée, une cible annoncée, une cible reportée

*← Vol. II §15.2.*

⚠ **Formulation imposée (PRDPlan Vol. II §4.4)** : écrire « la cible a été successivement reportée : 2019, puis 2022, puis 2023, puis 2026 » — ce sont **quatre cibles successives**, ni quatre reports, ni les dates auxquelles les reports ont été décidés.

⚠ **Garde-fou R-4** : la cible T4 2026 *est* officiellement annoncée — l'attribuer, ne pas l'affirmer au futur catégorique. ⚠ **Réserve F-29** : ne **jamais** écrire « lancé » ni « en production ».

#### § 37.3 — By-law no 10 : l'instrument juridique précède le rail

*← Vol. II §15.3.*

#### § 37.4 — Ce que la couche sémantique commune change — et ce que le socle n'en dit pas

*← Vol. II §15.4 ; le substrat sémantique est au ch. 35 § 35.2, le flux instancié au ch. 50.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §15.1-15.4 | § 37.1-37.4 | condensé |

### Chapitre 38 — Les sous-domaines financiers : banque, assurance, patrimoine

**Thèse** : l'agentique se décline différemment selon le sous-domaine — bancaire, IARD, assurance de personne, gestion de patrimoine, services TI financiers — chacun avec sa maturité et ses points de durcissement propres.
Sections : bancaire (détail, gros, paiements, crédit, core banking) ; assurance dommage (IARD/P&C) ; assurance de personne (vie & santé) ; gestion de patrimoine & d'actifs ; services TI dans le domaine financier ; synthèse par sous-domaine (études de cas datées, bancs d'essai sectoriels, questions ouvertes, bacs à sable réglementaires) ; **synthèse et transition du bloc financier** (Vol. I *Monographie* §5.14).
*Fusion : Vol. I* Monographie *§5.7-5.11 + §5.12.4-5.12.7 + §5.14 (synthèse de chapitre — **rattachement corrigé en v0.3** : le §5.14 est la clôture du ch. 5, non un développement sur les paiements agentiques). Les §5.12.1-5.12.3 (architecture de référence, maturité, grille de décision) sont consolidés au ch. 47 ; le §5.13 (interop B2B, commerce et paiements agentiques) au ch. 40.*

**Table des matières détaillée du chapitre 38**

*Dérivée du texte rédigé de `Monographie.md` §5.7-5.12 et §5.14 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 38.1 — Bancaire : détail, gros, paiements, crédit, *core banking

* — *← §5.7.1-5.7.7 : tri « productivité assistée » vs « autonomie transactionnelle » ; copilotes employés et revirement HITL ; KYC/AML et crime financier ; crédit et octroi (haut-risque AI Act 5(b), origination hypothécaire) ; paiements temps réel et irréversibilité ; encapsulation du core et du mainframe COBOL ; banque ouverte — l'agent comme destinataire accrédité (cadre au ch. 36).*

#### § 38.2 — Assurance dommage (IARD / P&C)

*← §5.8.1-5.8.4 : le tournant ACORD-MCP ; les PAS/core comme plateformes d'agents — « agent-dans-le-cœur » vs « cœur-comme-outil » (**SIÈGE des plateformes P&C**) ; sinistres et fraude, chaîne FNOL → règlement → subrogation ; souscription, tarification, distribution, télématique.*

#### § 38.3 — Assurance de personne (vie & santé)

*← §5.9.1-5.9.5 : souscription accélérée comme chaîne d'orchestration régulée ; « donnée de santé comme contexte d'agent » (FHIR/HL7 + MCP) ; prestations et* prior authorization *; distribution, conseil, rentes ; régime propre — haut-risque, équité/biais, donnée sensible.*

#### § 38.4 — Gestion de patrimoine et d'actifs

*← §5.10.1-5.10.7 : copilote du conseiller comme orchestrateur d'interop ; architecture fédérée à registre de plugins ; plateformes wealthtech ;* robo-advisor *classique vs agent LLM (**désambiguïsation impérative**) ; cadre fiduciaire,* suitability *et explicabilité ; trading et recherche augmentée ; opérations* buy-side.

#### § 38.5 — Services TI dans le domaine financier

*← §5.11.1-5.11.6 : résilience opérationnelle (*exit-by-design*, concentration) ; modernisation du core, le serveur MCP comme façade gouvernée du* legacy *; AI gateway et iPaaS régulés ; identité des agents et NHI en finance (doctrine au Livre III) ; cloud souverain et résidence ; observabilité et FinOps réglementaire (discipline au Livre VII).*

#### § 38.6 — Synthèse par sous-domaine

*← §5.12.4-5.12.7 : études de cas datées (tableau-synthèse) ; bancs d'essai sectoriels — la fiabilité de* workflow *prime sur le raisonnement ; questions ouvertes propres à la finance ; bacs à sable réglementaires.*

#### § 38.7 — Synthèse et transition du bloc financier

*← §5.14.1-5.14.4 : le patron directeur ; la signature du vertical (double-qualification, **siège au ch. 35 § 35.1.4**) ; les standards de données comme garde-fou déterministe ; l'horizon réglementaire 2026-2027.*

⚠ **Rattachement corrigé en v0.3** : le §5.14 est la **clôture du ch. 5**, non un développement sur les paiements agentiques — les v0.1-v0.2 l'acheminaient au chapitre prospectif AP2.

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §5.7-5.11 | § 38.1-38.5 | condensé |
| §5.12.1-5.12.3 | ch. 47 | hors périmètre (architecture, maturité, grille) |
| §5.12.4-5.12.7 | § 38.6 | condensé |
| §5.13 | ch. 40 | hors périmètre (interop B2B, commerce) |
| §5.14 | § 38.7 | condensé — rattachement corrigé en v0.3 |

### Chapitre 39 — Études de cas : la production agentique canadienne (2025-2026)

**Thèse** : l'agentique canadienne est en production, documentée par sources primaires, gouvernée au niveau C-suite — et inégalement documentable selon les institutions.
Sections : TD (Layer 6, pré-adjudication RESL) ; Scotiabank (AIDox ; consortium Agentic Control Plane) ; RBC (AI Group, FINOS) ; Manuvie (runtime Akka, Global CAIO) ; Desjardins (plan 2026-2029) ; CIBC (assistive — ne pas surqualifier) ; Intact (~600 modèles, sans terminologie agentique) ; BMO et Sun Life (élevés en P0) ; gouvernances comparées et code de conduite volontaire.
*Fusion : Vol. II ch. 17 (conservé intact). Socle : F-17 à F-23b (F-18, F-19, F-20, F-21 et F-22 à nommer un à un à la rédaction, la plage seule ne les désignant pas), F-30, F-31, F-47, F-48. Garde-fous : **PRD Vol. II §7.5** (métriques institutionnelles auto-déclarées, attribution à chaque occurrence), R-8. **Lacune héritée portée : PRD Vol. II §10.2** — réduite après P0, mais résidus [C] et absence documentée de sources primaires pour la BNC subsistent, en encadrés.*

**Table des matières détaillée du chapitre 39**

*Dérivée du texte rédigé de `Monographie.md` ch. 17 (Vol. II) le 25 juillet 2026 — **chapitre conservé intact**. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 39.1 — TD : la pré-adjudication hypothécaire, ou l'agentique dans la chaîne d'octroi

*← Vol. II §17.1 (Layer 6).*

#### § 39.2 — Scotiabank : AIDox, ou le volume comme terrain d'expérimentation

*← Vol. II §17.2.* ⚠ Le consortium *Agentic Control Plane* relève de la **branche (b) de R-8** — ne jamais l'agréger aux trois autres emplois du sigle (encadré au ch. 7).

#### § 39.3 — RBC : la structure avant l'application

*← Vol. II §17.3 (AI Group, FINOS).*

#### § 39.4 — Manuvie : le *runtime* nommé, la cible chiffrée

*← Vol. II §17.4 (Akka, Global CAIO).*

#### § 39.5 — Desjardins : la stratégie avant le système

*← Vol. II §17.5 (plan 2026-2029).*

#### § 39.6 — CIBC : ce que le communiqué ne dit pas

*← Vol. II §17.6.* ⚠ **Assistif — ne pas surqualifier.**

#### § 39.7 — Intact : l'industrialisation sans le vocabulaire

*← Vol. II §17.7 (~600 modèles, sans terminologie agentique).*

#### § 39.8 — BMO, Sun Life, Banque Nationale : la frontière du documentable

*← Vol. II §17.8 ; BMO et Sun Life élevés en P0 (F-47, F-48).* ⚠ **Lacune héritée portée (PRD Vol. II §10.2)** : réduite après P0, mais **résidus [C] et absence documentée de sources primaires pour la BNC** subsistent — en encadrés, non comblés.

#### § 39.9 — Gouvernances comparées : ce que cinq dispositifs ont en commun

*← Vol. II §17.9 ; code de conduite volontaire.*

⚠ **Garde-fou (PRD Vol. II §7.5)** : les métriques institutionnelles sont **auto-déclarées et non auditées indépendamment** — attribution obligatoire **à chaque occurrence**. **Socle** : F-17 à F-23b — **F-18, F-19, F-20, F-21 et F-22 à nommer un à un à la rédaction, la plage seule ne les désignant pas** —, F-30, F-31, F-47, F-48.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §17.1-17.9 | § 39.1-39.9 | **intact** |

### Chapitre 40 — Prospective : AP2 sur les rails canadiens ?

**Thèse** *(explicitement prospectif)* : aucune source ne documente l'articulation AP2 ↔ rails canadiens — le chapitre pose le cadre d'analyse et les conditions de possibilité, sans affirmer (énumérer des conditions n'est pas prédire).
Sections : état de la question (lacune assumée) ; interopérabilité B2B, commerce et paiements agentiques en finance (Vol. I *Monographie* §5.13) ; conditions de possibilité ; questions de recherche (série AP2/RTR — Vol. II *Monographie* ch. 16 §16.3, Q1-Q5) ; ⚠ **relève v0.11 — l'économie d'agents existe déjà, sur d'autres rails que ceux qu'instruit ce chapitre** : une étude empirique de juin 2026 (arXiv 2606.25876) mesure des millions de transactions machine-à-machine quotidiennes sur des rails de micropaiement natifs du web (x402) et d'enregistrement sur chaîne (ERC-8004), et en établit la fragilité — identité, autorisation et paiement non interopérables ; deux analyses datées relèvent des vulnérabilités du rail de paiement (arXiv 2605.30998) et la manipulabilité de la réputation du registre (arXiv 2606.26028) ; un cadre d'encadrement — l'« économie bac à sable », axes de perméabilité et d'intentionnalité — est proposé par des chercheurs d'un laboratoire industriel (arXiv 2509.10147). Préimpressions, à instruire : ces rails parallèles sont un contre-scénario aux conditions de possibilité du chapitre, pas un fait canadien.
*Fusion : Vol. II ch. 16 + Vol. I* Monographie *§5.13. Socle : F-04, F-29. **Lacune héritée portée : PRD Vol. II §10.5** (AP2 ↔ rails canadiens, ouverte) — c'est le sujet même du chapitre ; renvoi ch. 56. Garde-fou : ne pas combler la lacune par de la fiction.*

**Table des matières détaillée du chapitre 40**

*Dérivée du texte rédigé de `Monographie.md` ch. 16 (Vol. II) et §5.13 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 40.1 — État de la question

*← Vol. II §16.1.* ⚠ **Lacune héritée portée (PRD Vol. II §10.5)** : aucune source ne documente l'articulation AP2 ↔ rails canadiens — **c'est le sujet même du chapitre** ; renvoi ch. 56. **Garde-fou : ne pas combler la lacune par de la fiction.**

#### § 40.2 — Interopérabilité B2B, commerce et paiements agentiques en finance

*← Vol. I* Monographie *§5.13.1-5.13.7 :*

- 40.2.1 La pile à trois couches : intention/orchestration vs autorisation/règlement — *← §5.13.1*
- 40.2.2 Le mandat vérifiable comme exigence issue de l'irréversibilité — *← §5.13.2 ; la chaîne de mandat est au ch. 18*
- 40.2.3 Rails réseaux de cartes : l'insertion de la banque émettrice via les *agentic tokens* — *← §5.13.3*
- 40.2.4 Protocoles ouverts de mandat et de commerce : AP2/FIDO, ACP, UCP, x402 — *← §5.13.4 ; anatomie au ch. 10*
- 40.2.5 Règlement M2M, stablecoins régulés et dépôts tokenisés — *← §5.13.5*
- 40.2.6 Litige, *chargeback* et réconciliation : le trou de responsabilité — *← §5.13.6 ; la sémantique d'effet est au ch. 54*
- 40.2.7 Angle Canada/Québec : RTR, stablecoins CAD, insertion des institutions — *← §5.13.7*

#### § 40.3 — Conditions de possibilité

*← Vol. II §16.2.* ⚠ **Énumérer des conditions n'est pas prédire** — le chapitre pose le cadre d'analyse, il n'affirme pas.

#### § 40.4 — Questions de recherche (série AP2/RTR, Q1-Q5)

*← Vol. II §16.3.* ⚠ **Décision 7** : le Vol. II porte **deux** séries « Q n » indépendantes — celle-ci (*Monographie* ch. 16 §16.3, cinq questions AP2/RTR) et celle d'agenda (ch. 21 §21.2, six questions). Nommer la série à chaque renvoi.

#### § 40.5 — ⚠ Relève v0.11, à instruire : l'économie d'agents existe déjà, sur d'autres rails

une étude empirique de juin 2026 (arXiv 2606.25876) mesure des millions de transactions machine-à-machine quotidiennes sur des rails de micropaiement natifs du web (x402) et d'enregistrement sur chaîne (ERC-8004), et en établit la **fragilité** — identité, autorisation et paiement non interopérables ; deux analyses datées relèvent des vulnérabilités du rail de paiement (arXiv 2605.30998) et la manipulabilité de la réputation du registre (arXiv 2606.26028) ; un cadre d'encadrement — l'« économie bac à sable », axes de perméabilité et d'intentionnalité — est proposé par des chercheurs d'un laboratoire industriel (arXiv 2509.10147). **Préimpressions, résumés seuls consultés** : ces rails parallèles sont un **contre-scénario** aux conditions de possibilité du § 40.3, **pas un fait canadien**.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §16.1-16.3 | § 40.1, § 40.3-40.4 | condensé |
| Vol. I *Monographie* §5.13 | § 40.2 | **arrivée** depuis le ch. 38 |

---

## LIVRE VII — AgentMesh et AgentOps : appliquer et exploiter la confiance

*(fusionne Vol. III Parties VII-VIII + Vol. I §1.3.4 + §2.9.6/§2.11.1/§2.11.4-2.11.5/§4.9 — condensation v0.9 : absorbe l'ancien Livre X, décision 10 ; deux mouvements — appliquer, ch. 41-42 ; exploiter, ch. 43-45 ; ~27 000 mots)*

⚠ **Désambiguïsation obligatoire, garde-fou R-04 du Vol. III, branche (f).** « AgentMesh » désigne ici — et partout dans la somme — le **patron d'infrastructure** (plan de données médiatisant chaque arête, plan de contrôle centralisant la politique). Le terme sert ailleurs dans l'industrie à nommer une **équipe plateforme**, un **produit commercial** et une **couche de courtage** ; la branche (f) de R-04 a précisément été ouverte parce que la v0.1 de ce fichier employait le mot dans deux sens incompatibles à trente lignes d'écart. Le glossaire (Annexe E) porte les six emplois ; aucun chapitre n'emploie le terme sans que le sens visé soit déterminable de sa phrase.

**Premier mouvement — appliquer (ch. 41-42).**

### Chapitre 41 — Du service mesh à l'agent mesh : généalogie et anatomie

**Thèse** : le maillage d'agents est la réinstanciation, au niveau agentique, du patron *service mesh* — un plan de données qui médiatise chaque arête, un plan de contrôle qui centralise la politique ; cette filiation trie ce que le terme recouvre réellement de ce qu'il recouvre en marketing.
Sections : généalogie (sidecar, passerelle, plan de contrôle/données ; mTLS, SPIFFE/SPIRE transposables — repris du ch. 1) ; anatomie du maillage agentique (passerelles d'outils, courtage A2A, transport SLIM, routage sémantique) ; ce que l'arête change (la sûreté n'est pas compositionnelle) ; grille du ch. 15 appliquée.
*Fusion : Vol. III ch. 22 + Vol. I* Monographie *§1.3.4. Garde-fous : « agent mesh » terme de fournisseur ; désambiguïsation R-8 du Vol. II (« control plane » — le patron décrit ici comporte un plan de contrôle, terme dont les quatre branches de la collision sont le siège de ce garde-fou) ; la désambiguïsation d'« AgentMesh » lui-même relève de R-04 du Vol. III, branche (f), imposée en tête de livre.*

**Table des matières détaillée du chapitre 41**

*Dérivée du texte rédigé de `Monographie.md` ch. 22 (Vol. III) et §1.3.4 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 41.1 — Généalogie et définition : ce que la filiation apporte, ce que le socle en porte

*← Vol. III* Monographie *§22.1 + Vol. I* Monographie *§1.3.4 (sidecar, plan de contrôle/données, maillage sans sidecar et eBPF, Gateway API,* event mesh*) — **socle transposable repris du ch. 1**, avec mTLS et SPIFFE/SPIRE.* ⚠ **Garde-fou** : « agent mesh » est un **terme de fournisseur** avant d'être un terme d'architecture.

#### § 41.2 — Anatomie du maillage agentique, à l'état daté

*← Vol. III* Monographie *§22.2 : passerelles d'outils, courtage A2A, transport SLIM, routage sémantique.* ⚠ **Désambiguïsation R-8 du Vol. II** : le patron décrit ici **comporte un plan de contrôle** — terme dont les quatre branches de la collision siègent au ch. 7 § 7.5.

#### § 41.3 — Ce que l'arête change : la non-compositionnalité de la sûreté

*← Vol. III* Monographie *§22.3.*

#### § 41.4 — La grille du ch. 15 appliquée au maillage : ce qu'il vérifie, ce qu'il transporte, ce qu'il ignore

*← Vol. III* Monographie *§22.4.*

⚠ **Rappel du garde-fou R-04 du Vol. III, branche (f)** (imposé en tête de livre) : « AgentMesh » désigne ici le **patron d'infrastructure**, jamais une équipe plateforme, un produit commercial ou une couche de courtage. Le glossaire (Annexe E) porte les six emplois.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §22.1-22.4 | § 41.1-41.4 | condensé |
| Vol. I *Monographie* §1.3.4 | § 41.1 | **arrivée** (déclinaison agentique, scindée au ch. 1) |

### Chapitre 42 — Le maillage comme point d'application : PEP/PDP et zero trust agentique

**Thèse** : le maillage est le lieu où le passeport du ch. 17 devient opposable — PEP adossé à un PDP, transposition du zero trust au graphe d'agents : vérifier chaque arête, sans confiance héritée de la topologie.
Sections : PEP/PDP agentiques (langages de politique, état des mécanismes) ; garde-fous d'exécution au grain de l'arête (application des principes de défense architecturale du ch. 6) ; zero trust transposé (« jamais confiance au graphe ») ; le maillage et la chaîne de mandat (ce qu'il trace du problème des deux sauts, ch. 18 — et ce qu'il ne résout pas) ; coûts (latence, complexité, point de défaillance — conditions qui renversent la recommandation).
*Fusion : Vol. III ch. 23 + Vol. I* Monographie *§2.10.3-2.10.4 (défense architecturale et garde-fous, appliqués ici, posés au ch. 6). ⚠ Le socle zero-trust pré-agentique (§1.9.3) **reste au ch. 3** et n'est pas reconstruit ici. Socle : NIST SP 800-207. Prolonge les points de contrôle obligatoires (Vol. II ch. 19 §19.3) au grain de l'infrastructure.*

**Table des matières détaillée du chapitre 42**

*Dérivée du texte rédigé de `Monographie.md` ch. 23 (Vol. III) et §2.10.3-2.10.4 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 42.1 — PEP et PDP agentiques : où se prend et où s'applique la décision d'autorisation

*← Vol. III* Monographie *§23.1 (langages de politique, état des mécanismes).* Le maillage est **le lieu où le passeport du ch. 17 devient opposable**.

#### § 42.2 — Garde-fous d'exécution au grain de l'arête

*← Vol. I* Monographie *§2.10.3-2.10.4 (référentiels et patrons de défense architecturale ; garde-fous d'exécution et chaîne d'approvisionnement) — **appliqués ici, posés au ch. 6** : partage déclaré, sans reconstruction.*

#### § 42.3 — *Zero trust* transposé : de « jamais confiance au réseau » à « jamais confiance au graphe »

*← Vol. III* Monographie *§23.2 ; socle NIST SP 800-207.* ⚠ Le **socle zero-trust pré-agentique (Vol. I §1.9.3) reste au ch. 3** et n'est pas reconstruit ici.

#### § 42.4 — Le maillage et la chaîne de mandat protocolaire

*← Vol. III* Monographie *§23.3 : ce que le point d'application **peut tracer** du problème des deux sauts (ch. 18), **et ce qu'il ne résout pas**.*

#### § 42.5 — Coûts, latence, complexité, point de défaillance

*← Vol. III* Monographie *§23.4 : **les conditions qui renverseraient ce que ce chapitre avance** — à écrire comme telles, non comme réserves de style.*

⚠ *Prolonge les **points de contrôle obligatoires** (Vol. II ch. 19 §19.3, repris au ch. 47) au grain de l'infrastructure.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §23.1-23.4 | § 42.1, § 42.3-42.5 | condensé |
| Vol. I *Monographie* §2.10.3-2.10.4 | § 42.2 | **partagé déclaré** avec le ch. 6 |

**Second mouvement — exploiter (ch. 43-45)** *(anciennement Livre X ; provenance intégrée à l'en-tête du livre)*

### Chapitre 43 — L'observabilité agentique

**Thèse** : l'AgentOps commence par l'observabilité, dont le socle de standardisation est les conventions sémantiques GenAI/agents d'OpenTelemetry — mais tracer un *appel* n'est pas tracer une *délégation* : la corrélation trace ↔ chaîne de mandat est le chaînon manquant.
Sections : de l'APM à l'AgentOps (non-déterminisme, coût par jeton, horizon de tâche) ; état des conventions OTel (stable/expérimental — **daté en v0.7** : à la mi-2026, les conventions GenAI et MCP restent au statut *Development* — semconv 1.40.0, avril 2026 —, seuls des attributs d'exécution de base étant tenus pour stables ; leur migration vers un dépôt dédié est une ressource vivante, à re-dater au gel) ; journalisation probatoire (pont vers E-23, ch. 29 ; ⚠ **relève v0.10** : une préimpression adverse de mai 2026 pose que la propriété porteuse d'un runtime agentique n'est pas la richesse de la trace mais la **détection de la divergence entre l'action effectuée et son enregistrement d'audit**, et propose le journal chaîné par empreintes comme parade — matériau candidat, à instruire ; le versant *effet* est au ch. 54) ; corréler la trace au passeport (l'identité comme clé de jointure).
*Fusion : Vol. III ch. 24 + Vol. I* Monographie *§2.9.6 (observabilité, OTel GenAI — **seule affectation**, le ch. 6 ne la conserve pas), §3.12.3 (propagation de trace inter-agents) et §4.9.1-4.9.2 (OTel étagé, journal d'audit probatoire). Garde-fou : « AgentOps » désigne la discipline, non un produit homonyme.*

**Table des matières détaillée du chapitre 43**

*Dérivée du texte rédigé de `Monographie.md` ch. 24 (Vol. III) et §2.9.6/§3.12.3/§4.9.1-4.9.2 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 43.1 — De l'APM à l'AgentOps : ce que l'observabilité classique couvre et où l'agent la déborde

*← Vol. III* Monographie *§24.1 (non-déterminisme, coût par jeton, horizon de tâche).* ⚠ **Garde-fou** : « AgentOps » désigne **la discipline**, non un produit homonyme.

#### § 43.2 — État des conventions sémantiques OpenTelemetry pour l'IA générative et les agents

*← Vol. III* Monographie *§24.2 + Vol. I* Monographie *§2.9.6 (**seule affectation** — le ch. 6 ne la conserve pas) et §4.9.1 (OTel étagé, traces inter-agents/inter-org).*

⚠ **Daté en v0.7** : à la mi-2026, les conventions GenAI **et MCP** restent au statut *Development* (semconv 1.40.0, avril 2026), seuls des attributs d'exécution de base étant tenus pour stables. Leur migration vers un dépôt dédié est une **ressource vivante**, à re-dater au gel.

#### § 43.3 — Propagation de trace à travers les frontières d'agents

*← Vol. I* Monographie *§3.12.3 (W3C Trace Context) — **prélevé au ch. 9**, qui garde le reste du §3.12.*

#### § 43.4 — La journalisation probatoire : quand la trace devient pièce de conformité

*← Vol. III* Monographie *§24.3 + Vol. I* Monographie *§4.9.2 (journal d'audit réglementaire, conservation probante, admissibilité) ; pont vers E-23 (ch. 29).*

⚠ **Relève v0.10, à instruire** : une préimpression adverse de mai 2026 pose que la propriété porteuse d'un *runtime* agentique n'est pas la richesse de la trace mais la **détection de la divergence entre l'action effectuée et son enregistrement d'audit**, et propose le journal chaîné par empreintes comme parade. **Matériau candidat** ; le versant *effet* est au ch. 54.

#### § 43.5 — Corréler la trace au passeport : l'identité comme clé de jointure

*← Vol. III* Monographie *§24.4.* **Tracer un *appel* n'est pas tracer une *délégation*** : la corrélation trace ↔ chaîne de mandat (ch. 18) est le **chaînon manquant**.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §24.1-24.4 | § 43.1-43.2, § 43.4-43.5 | condensé |
| Vol. I *Monographie* §2.9.6 | § 43.2 | **seule affectation** |
| Vol. I *Monographie* §3.12.3 | § 43.3 | prélevé au ch. 9 |
| Vol. I *Monographie* §4.9.1-4.9.2 | § 43.2, § 43.4 | condensé |

### Chapitre 44 — Le cycle de vie opérationnel : évaluation continue, dérive et incident

**Thèse** : l'exploitation d'un parc d'agents est une boucle — évaluer, détecter la dérive, répondre à l'incident, réviser le mandat — réalisation opérationnelle du quatrième terme de l'invariant ; sans elle, le passeport certifie un comportement passé, jamais le comportement courant.
Sections : évaluation en production (des jeux d'essai à l'évaluation continue) ; dérive agentique (modèle, outil — rug-pull du ch. 21 relu en signal —, autonomie ; ⚠ **relève v0.10** : une quatrième source de dérive, **la mémoire**, quand le contexte de travail est continûment réécrit par des modèles auxiliaires — un observateur qui extrait des observations structurées, un réflecteur qui les compresse, déclenchés à seuil de jetons et à l'inactivité. Le dispositif est décrit par son éditeur comme parade au pourrissement de contexte ; **aucune propriété de conservation n'est publiquement établie**, et un état de mémoire produit par un autre modèle est un artefact dérivé et daté — à instruire, avec le ch. 5) ; réponse à incident (révocation d'urgence ch. 21, confinement par le maillage ch. 42, agentic SOC ch. 22) ; GitOps du parc ; l'agent qui apprend (revalidation après apprentissage) ; **cycle de vie et modèles de maturité — corpus d'appui, cadrage et non preuve** ; ⚠ **relève v0.11 — l'auto-évolution fait de la dérive une fonctionnalité** : deux relevés de synthèse de 2025, tenus à jour en 2026 (arXiv 2508.07407 ; arXiv 2507.21046), décrivent des agents qui optimisent en production leurs invites, outils et mémoires — la dérive que ce chapitre veut détecter y devient un comportement recherché, et la revalidation après apprentissage cesse d'être un cas limite pour devenir le régime nominal ; une préimpression de juillet 2026 propose d'encadrer l'auto-modification par des certificats à garanties d'erreur auditables (arXiv 2607.00871). À instruire ; la distinction adaptation éphémère / évolution persistante du ch. 26 est le point d'ancrage, et le versant versionnement est au ch. 53 — un artefact qui se modifie en production n'a plus d'horloge fixe du tout.
*Fusion : Vol. III ch. 25 + Vol. I* Monographie *§2.11.4-2.11.5 (HITL opérationnel, réponse aux incidents, AIOps agentique). ⚠ Le §2.9 n'est **pas** repris ici : ses fondements restent au ch. 6, son versant observabilité va au ch. 43. **Le « quatrième terme de l'invariant » que la thèse invoque est posé à l'avant-propos** et vient du Vol. I* Monographie *§4.12.4 (élargi §7.0) — que le Vol. I qualifie de legs explicite au Vol. III, lequel en fait le fondement de sa Partie VIII : c'est la filiation exacte de ce livre, et elle se nomme plutôt qu'elle ne s'invoque. La section « l'agent qui apprend » **renvoie au ch. 26** (capacité d'auto-modification du paradigme APM, Vol. II ch. 6 §6.3) pour la distinction adaptation éphémère / évolution persistante, sans la reconstruire. Chapitre de synthèse refermant les fils du Livre III.*

**Table des matières détaillée du chapitre 44**

*Dérivée du texte rédigé de `Monographie.md` ch. 25 (Vol. III) et §2.11.4-2.11.5 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 44.1 — L'évaluation en production : des jeux d'essai à l'évaluation continue

*← Vol. III* Monographie *§25.1.* ⚠ Les **fondements** de l'évaluation restent au ch. 6 (le §2.9 du Vol. I n'est pas repris ici) ; la barrière d'évaluation au déploiement est au ch. 53.

#### § 44.2 — La dérive agentique : modèle, outil, autonomie

*← Vol. III* Monographie *§25.2 ; le rug-pull du ch. 21 relu en **signal**.*

⚠ **Relève v0.10, à instruire** — une **quatrième source de dérive : la mémoire**, quand le contexte de travail est continûment réécrit par des modèles auxiliaires (un observateur qui extrait des observations structurées, un réflecteur qui les compresse, déclenchés à seuil de jetons et à l'inactivité). Le dispositif est décrit par son éditeur comme parade au pourrissement de contexte ; **aucune propriété de conservation n'est publiquement établie**, et un état de mémoire produit par un autre modèle est un **artefact dérivé et daté**. À instruire avec le ch. 5.

#### § 44.3 — La réponse à incident agentique : révoquer, confiner, imputer

*← Vol. III* Monographie *§25.3 + Vol. I* Monographie *§2.11.4 (fiabilité opérationnelle, HITL, réponse aux incidents) ; révocation d'urgence ch. 21, confinement par le maillage ch. 42,* agentic SOC *ch. 22.*

#### § 44.4 — GitOps du parc d'agents : versionner le mandat protocolaire, promouvoir, revenir en arrière

*← Vol. III* Monographie *§25.4 + Vol. I* Monographie *§2.11.5 (AIOps agentique) ; le grain du déploiement est au ch. 53.*

#### § 44.5 — L'agent qui apprend : ce que le passeport date, et ce qu'il ne date pas

*← Vol. III* Monographie *§25.5.* ⚠ **Renvoie au ch. 26** (capacité d'auto-modification du paradigme APM, Vol. II ch. 6 §6.3) pour la distinction **adaptation éphémère / évolution persistante**, sans la reconstruire.

⚠ **Relève v0.11, à instruire — l'auto-évolution fait de la dérive une fonctionnalité** : deux relevés de synthèse de 2025 tenus à jour en 2026 (arXiv 2508.07407 ; arXiv 2507.21046) décrivent des agents qui optimisent **en production** leurs invites, outils et mémoires — la dérive que le § 44.2 veut détecter y devient un comportement **recherché**, et la revalidation après apprentissage cesse d'être un cas limite pour devenir le régime nominal ; une préimpression de juillet 2026 propose d'encadrer l'auto-modification par des certificats à garanties d'erreur auditables (arXiv 2607.00871). Le versant versionnement est au ch. 53 — **un artefact qui se modifie en production n'a plus d'horloge fixe du tout**.

#### § 44.6 — Cycle de vie et modèles de maturité

⚠ **corpus d'appui, cadrage et non preuve** (filiation retirée par P0.2 le 21 juill. 2026, réversible).

⚠ **Le « quatrième terme de l'invariant » que la thèse invoque est posé à l'avant-propos** et vient du Vol. I *Monographie* §4.12.4 (élargi §7.0) — que le Vol. I qualifie de **legs explicite au Vol. III**, lequel en fait le fondement de sa Partie VIII. C'est la filiation exacte de ce livre : **elle se nomme plutôt qu'elle ne s'invoque**. Chapitre de synthèse refermant les fils du Livre III.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §25.1-25.5 | § 44.1-44.5 | condensé |
| Vol. I *Monographie* §2.11.4-2.11.5 | § 44.3-44.4 | **arrivée** depuis le ch. 6 |
| Vol. I *Monographie* §2.9 | ch. 6 / ch. 43 | hors périmètre — non repris ici |

### Chapitre 45 — Les indicateurs de l'AgentOps et le FinOps des agents

**Thèse** : la discipline naissante n'a pas ses indicateurs de référence ; les métriques publiées sont hétérogènes et auto-déclarées — grille minimale dérivée des obligations des Livres V-VII, présentée comme construction d'auteur ; le modèle de coût agentique est une contrainte d'ingénierie de premier ordre.
Sections : recension critique des métriques publiées ; grille minimale (disponibilité du parc, couverture de traçabilité, délai de révocation, fraîcheur des évaluations) ; métrique d'horizon de tâche déléguée ; **indicateurs de la supervision humaine** (délai médian de révision, taux de renversement — proxies imparfaits du tamponnage, ch. 18) ; FinOps des agents (coût par résolution, budget par jeton, routage de modèles et mise en cache comme leviers, latence comme contrainte d'usage).
*Fusion : Vol. III ch. 26 + Vol. I* Monographie *§4.9.3-4.9.5 et **§2.11.1** (modèle de coût agentique — **seule affectation**, le ch. 43 ne la revendique plus). Garde-fou : chaque indicateur marqué construction d'auteur, chaque chiffre attribué.*

**Table des matières détaillée du chapitre 45**

*Dérivée du texte rédigé de `Monographie.md` ch. 26 (Vol. III) et §2.11.1/§4.9.3-4.9.5 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 45.1 — Recension critique des métriques relevées : ce qui a été ouvert, et ce que cela compte

*← Vol. III* Monographie *§26.1.* La discipline naissante **n'a pas ses indicateurs de référence** ; les métriques publiées sont **hétérogènes et auto-déclarées**.

#### § 45.2 — La grille minimale : ce que l'architecte doit pouvoir répondre à l'auditeur

*← Vol. III* Monographie *§26.2 : disponibilité du parc, couverture de traçabilité, délai de révocation, fraîcheur des évaluations.* ⚠ **Construction d'auteur**, dérivée des obligations des Livres V-VII — marquée telle.

#### § 45.3 — La métrique d'horizon de tâche déléguée

*← Vol. III* Monographie *§26.3 (front ouvert hérité du Vol. I).* ⚠ **Partage déclaré avec le ch. 56** (décision 6, posé en v0.17) : **la métrique et son état se traitent ici** ; **l'énoncé de recherche qui en sort** est transmis au ch. 56 § 56.2, qui ne la reconstruit pas.

#### § 45.4 — Indicateurs de la supervision humaine

délai médian de révision, taux de renversement. ⚠ **Proxies imparfaits du tamponnage** (ch. 18 § 18.5) : mesurer la révision n'est pas mesurer le discernement.

#### § 45.5 — Le modèle de coût agentique comme contrainte d'ingénierie de premier ordre

*← Vol. I* Monographie *§2.11.1 (**seule affectation** — le ch. 43 ne la revendique plus).*

#### § 45.6 — FinOps des agents

*← Vol. I* Monographie *§4.9.3-4.9.5 : évaluation en production à l'échelle de flotte, SLO/SLI, fiabilité et dérive (§4.9.3) ; allocation, showback, chargeback et coût par résultat (§4.9.4) ; pré-production gouvernée — staging, shadow deployment, non-régression (§4.9.5, pont vers le ch. 53).* Coût par résolution, budget par jeton, routage de modèles et mise en cache comme leviers, latence comme contrainte d'usage.

⚠ **Garde-fou** : chaque indicateur marqué **construction d'auteur**, chaque chiffre **attribué**.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §26.1-26.3 | § 45.1-45.3 | condensé ; §26.3 **partagé déclaré** avec le ch. 56 |
| Vol. I *Monographie* §2.11.1 | § 45.5 | **seule affectation** |
| Vol. I *Monographie* §4.9.3-4.9.5 | § 45.6 | condensé |

---

## LIVRE VIII — Synthèse architecturale et blueprint

*(fusionne Vol. I ch. 6 + Annexe B ADS + Vol. II Partie VI **hors ch. 21** + ch. 22-23 — le ch. 21 et le ch. 24 du Vol. II vont au Livre X — + Vol. III Partie IX ; ~35 000 mots)*

### Chapitre 46 — La matrice protocoles × exigences réglementaires

**Thèse** : croiser la pile protocolaire (MCP/A2A/AP2) avec les exigences canadiennes (E-23, AMF, art. 12.1, 11-348, cadre bancaire) et la grille des cinq questions révèle où les standards suffisent et où l'architecture doit compenser — et, à date, quinze croisements sans lien documenté.
Sections : construction de la matrice ; lecture par protocole ; lecture par exigence ; zones de compensation architecturale.
*Fusion : Vol. II ch. 18 + Vol. II ***Monographie*** Annexe B (matrice détaillée protocoles × réglementation — source des quinze croisements) + Vol. III Annexe B (matrice des mécanismes). Socle **transversal** (Livres II-VIII), **construit par la rédaction avec sa contrepartie obligatoire** : l'en-tête énumère les entrées effectivement mobilisées et les garde-fous effectivement balayés, y compris à zéro occurrence (règle de l'avant-propos, héritée du Vol. II). C'est ce dispositif — et non une relecture — qui a permis au Vol. II de contrôler la traçabilité de son ch. 18, et c'est ce chapitre qui y a détecté une erreur de marquage de son socle.*

**Table des matières détaillée du chapitre 46**

*Dérivée du texte rédigé de `Monographie.md` ch. 18 et Annexe B (Vol. II) et de l'Annexe B (Vol. III) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 46.1 — Construction de la matrice

*← Vol. II §18.1 + Vol. II* Monographie *Annexe B (matrice détaillée protocoles × réglementation — **source des quinze croisements**) + Vol. III Annexe B (matrice des mécanismes).* Croise la pile protocolaire (MCP/A2A/AP2), les exigences canadiennes (E-23, AMF, art. 12.1, 11-348, cadre bancaire) et la **grille des cinq questions** (ch. 15).

#### § 46.2 — Lecture par protocole

*← Vol. II §18.2.*

#### § 46.3 — Lecture par exigence

*← Vol. II §18.3.*

#### § 46.4 — Les zones de compensation architecturale

*← Vol. II §18.4 : où les standards suffisent, où l'architecture doit compenser.* ⚠ **Quinze croisements sans lien documenté** à date — cardinal du Vol. II, **à re-mesurer** contre la matrice consolidée (Annexe F), non à recopier.

⚠ **Socle transversal (Livres II-VIII), construit par la rédaction — avec sa contrepartie obligatoire et non négociable** : l'en-tête du chapitre **énumère les entrées effectivement mobilisées et les garde-fous effectivement balayés, y compris ceux à zéro occurrence** (règle de l'avant-propos, héritée du Vol. II). C'est ce dispositif — **et non une relecture** — qui a permis au Vol. II de contrôler la traçabilité de son ch. 18, et c'est ce chapitre qui y a détecté une erreur de marquage de son socle. Homologue de méthode du ch. 15.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §18.1-18.4 | § 46.1-46.4 | condensé |
| Vol. II *Monographie* Annexe B | § 46.1 | source des quinze croisements |
| Vol. III Annexe B | § 46.1 | matrice des mécanismes |

### Chapitre 47 — L'architecture de référence unifiée par couches

**Thèse** : les Livres I-VII se composent en une architecture cible neutre à couches (protocoles, identité/registre, orchestration, maillage, exploitation, gouvernance), structurée par OO1-OO4, avec OO3/OO4 et la fabrique d'identité imposés sous exigence réglementaire stricte.
Sections : couches et responsabilités (fabrique d'identité, maillage, AgentOps — les trois étages) ; positionnement OO par cas d'usage et grille « quand agentifier » ; points de contrôle obligatoires ; le plan de contrôle d'agents comme architecture de référence ; le modèle de maturité de l'entreprise agentique (confrontation des trois modèles de maturité — **corpus d'appui**, cadrage et non preuve, filiation retirée par P0.2 le 21 juill. 2026, réversible : voir le bloc Corpus d'appui — et de l'échelle **assistance → copilote → orchestration sous revue → autonomie bornée** ; ⚠ **garde-fou R-13 du Vol. III** : ne jamais écrire « l'autonomie graduée du Vol. I » sans autre précision, ce volume portant trois échelles distinctes — celle-ci, le continuum 0-5 du *Monographie* §2.2.4 et la graduation L0-L3 de son Annexe B §1.3) ; alternatives et variantes.
*Fusion : Vol. II ch. 19 + Vol. III ch. 27 §27.1/§27.4 + Vol. I* Monographie *§5.12.1-5.12.3, §6.10 (maturité et feuille de route par plateaux — **prélevé au ch. 6 du Vol. I, que le ch. 48 traite par ailleurs en bloc**), §4.12 (plan de contrôle d'agents) et §2.13.1 (grille « quand agentifier »). Socle : F-36, F-37, F-46 + Livre IV.*

**Table des matières détaillée du chapitre 47**

*Dérivée du texte rédigé de `Monographie.md` ch. 19 (Vol. II), ch. 27 (Vol. III) et §5.12.1-5.12.3/§6.10/§4.12/§2.13.1 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 47.1 — Les couches et leurs responsabilités

*← Vol. II §19.1 + Vol. III* Monographie *§27.1 (les trois étages et leurs contrats mutuels : fabrique d'identité, maillage, AgentOps) ; protocoles, identité/registre, orchestration, maillage, exploitation, gouvernance.*

#### § 47.2 — Le positionnement des options d'orchestration par cas d'usage

*← Vol. II §19.2 + Vol. I* Monographie *§2.13.1 (grille « **quand agentifier, quand s'abstenir** » — **prélevée au ch. 6**).* OO3/OO4 et la fabrique d'identité **imposés sous exigence réglementaire stricte**.

#### § 47.3 — Les points de contrôle obligatoires

*← Vol. II §19.3 ; prolongés au grain de l'infrastructure au ch. 42.*

#### § 47.4 — Le plan de contrôle d'agents comme architecture de référence

*← Vol. I* Monographie *§4.12.1 + §5.12.1 (architecture de référence en finance régulée).* ⚠ **Désambiguïsation R-8 du Vol. II** : « plan de contrôle d'agents » au sens du patron — l'encadré des quatre branches siège au ch. 7 § 7.5.

#### § 47.5 — Le modèle de maturité de l'entreprise agentique

*← Vol. III* Monographie *§27.4 + Vol. I* Monographie *§5.12.2 et §6.10 (maturité et feuille de route par plateaux — **prélevé au ch. 6 du Vol. I, que le ch. 48 traite par ailleurs en bloc**).*

Confrontation des trois modèles de maturité (⚠ **corpus d'appui**, cadrage et non preuve — filiation retirée par P0.2 le 21 juill. 2026, réversible) et de l'échelle **assistance → copilote → orchestration sous revue → autonomie bornée**.

⚠ **Garde-fou R-13 du Vol. III** : ne jamais écrire « l'autonomie graduée du Vol. I » sans autre précision — ce volume porte **trois échelles distinctes** : celle-ci, le **continuum 0-5** (*Monographie* §2.2.4, au ch. 4 § 4.1.4) et la **graduation L0-L3** (son Annexe B §1.3, à l'Annexe H).

#### § 47.6 — Alternatives, variantes et frontières d'abstraction

*← Vol. II §19.4 + Vol. I* Monographie *§5.12.3 (grille de décision / RFP de l'architecte FS).*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §19.1-19.4 | § 47.1-47.3, § 47.6 | condensé |
| Vol. III *Monographie* §27.1, §27.4 | § 47.1, § 47.5 | condensé ; §27.2 au ch. 48, §27.3/§27.5 au ch. 49 |
| Vol. I *Monographie* §5.12.1-5.12.3 | § 47.4-47.6 | **arrivée** depuis le ch. 38 |
| Vol. I *Monographie* §6.10 | § 47.5 | **prélevé au ch. 48** |
| Vol. I *Monographie* §4.12 | § 47.4 | **arrivée** depuis le ch. 28 |
| Vol. I *Monographie* §2.13.1 | § 47.2 | **arrivée** depuis le ch. 6 |

### Chapitre 48 — La formalisation ArchiMate

**Thèse** *(le verrou est méthodologique et se nomme d'emblée)* : **ArchiMate n'a aucun élément natif** pour l'agent autonome, l'appel d'outil MCP, l'interaction A2A, l'identité non humaine ou le plan de contrôle ; la seule extension défendable est le mécanisme officiel **Specialization + stéréotype `<<…>>` + Profiles**, sur le modèle du *Risk & Security Overlay*. Ce que le chapitre apporte est une **traduction structurelle**, jamais une reprise du fond conceptuel des livres amont.
Sections : primer ArchiMate et patrons pour concepts agentiques ; **registre des stéréotypes** (Vol. I *Monographie* §6.1.9 — point d'appui aval dont dépendent les ch. 49-50 et l'Annexe H : il se tient ici, en un seul lieu) ; Motivation (exigences réglementaires traçables) ; Strategy (capacités, chaînes de valeur financières) ; Business (rôles, collaborations, objets financiers) ; Application & Technology (agents, protocoles, runtime, résidence) ; points de vue transverses ; gouvernance des vues ; bibliothèque de patrons et anti-patrons.
*Fusion : Vol. I* Monographie *ch. 6 **hors §6.8 et §6.10**, prélevés respectivement par les ch. 50 et ch. 47. Consolide les fonctions d'identité, points d'application du maillage et boucle d'exploitation (Vol. III *TOC* §27.2) dans le formalisme ArchiMate.*
*⚠ **Ancrage de version, absent des v0.1-v0.4 alors que le Vol. I le porte** : version de référence **ArchiMate 4** (The Open Group, doc **C260**, 27 avr. 2026), équivalents **3.2** (oct. 2022) en notes de transition. **Ressources vivantes à recouper au gel** : la liste définitive des éléments retirés ou renommés de C260 — ⚠ **relève v0.7 : l'ampleur est confirmée par l'éditeur de la norme** (réduction d'environ 30 % du nombre d'éléments, de plus de soixante à une quarantaine ; les couches remplacées par des **domaines**, dont un domaine commun ; multiplicité sur les relations), soit la refonte de métamodèle la plus profonde depuis la création du langage : la re-vérification du mécanisme Specialization + stéréotype + Profiles **tel que C260 le porte** est un préalable au registre des stéréotypes, non une note de transition ; l'état du support outils — à la mi-2026, la quasi-totalité des outils d'architecture d'entreprise n'exporte et n'importe encore que 3.2 nativement, ce qui rend le blueprint des ch. 49-50 non échangeable en v4 dans la plupart des ateliers ; le format d'échange v4 ; les programmes de certification en cours de mise à jour.*
*⚠ **Garde-fou de non-redondance, hérité du Vol. I §6.0.1 et plus nécessaire ici qu'à sa source** : « si l'on retire le mot ArchiMate et que la phrase tient encore comme un exposé des chapitres amont, c'est une redondance à renvoyer ». Au Vol. I, ce chapitre en suivait cinq ; ici il en suit quarante-sept.*

**Table des matières détaillée du chapitre 48**

*Dérivée du texte rédigé de `Monographie.md` ch. 6 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 48.0 — Primer ArchiMate et convention de version

*← §6.0.2-6.0.8 : pourquoi un blueprint et pourquoi ArchiMate ; langage / méthode / cadre / outil / modèle de référence ; cadre, domaines et aspects ; éléments et relations ; vues, points de vue et mécanismes d'extension ; relation ArchiMate ↔ TOGAF ADM.* Le §6.0.1 (contrat de lecture) est refondu en apparat.

#### § 48.1 — Le problème de modélisation : patrons pour concepts agentiques

*← §6.1.1-6.1.9 :*

- 48.1.1 Le verrou méthodologique : **aucun élément natif**, le recours à la spécialisation — *← §6.1.1*
- 48.1.2 Patron « agent » : Application Component vs Role vs Collaboration — *← §6.1.2*
- 48.1.3 Patron « appel d'outil MCP » : Application Service + Interface + Serving — *← §6.1.3*
- 48.1.4 Patron « interaction A2A » : Collaboration + Flow + Triggering — *← §6.1.4*
- 48.1.5 Patron « identité non humaine » : Role + Active Structure + overlay sécurité — *← §6.1.5*
- 48.1.6 Patron « plan de contrôle d'agents » et limite « découverte dynamique » — *← §6.1.6*
- 48.1.7 Patron « humain-agent » : HITL, *four-eyes*, autonomie graduée — *← §6.1.7*
- 48.1.8 Patron « mémoire, RAG et *grounding* gouverné » — *← §6.1.8*
- 48.1.9 **Registre des stéréotypes du blueprint** — *← §6.1.9.* ⚠ **Point d'appui aval dont dépendent les ch. 49-50 et l'Annexe H : il se tient ici, en un seul lieu.**

#### § 48.2 — Motivation : exigences réglementaires traçables

*← §6.2.1-6.2.5 (Stakeholder, Driver, Assessment, Goal/Outcome, Principle/Requirement ; amorce de la conformité traçable, dont le **siège est au §6.6.3**).*

#### § 48.3 — Strategy : capacités agentiques et chaînes de valeur financières

*← §6.3.1-6.3.4.*

#### § 48.4 — Business : rôles, collaborations humain-agent et objets financiers

*← §6.4.1-6.4.5.*

#### § 48.5 — Application et Technology : agents, protocoles, runtime, résidence

*← §6.5.x.*

#### § 48.6 — Points de vue transverses

*← §6.6.1-6.6.4 : Sécurité/Risque (RSO appliqué au parc) ; zéro-trust, NHI et segmentation ; **conformité traçable exigence → contrôle → élément (SIÈGE)** ; audit/observabilité et ségrégation des tâches.*

#### § 48.7 — Gouvernance des vues et organisation du blueprint

*← §6.7.1-6.7.4.*

#### § 48.8 — Bibliothèque de patrons et anti-patrons

*← §6.9.1-6.9.2.*

#### § 48.9 — Questions ouvertes : ArchiMate face aux systèmes autonomes

*← §6.11.1-6.11.4 (adéquation aux systèmes non déterministes ; modèles vivants et synchronisation ; overlay vs extension de langage).*

⚠ **Consolide** les fonctions d'identité, points d'application du maillage et boucle d'exploitation — *← Vol. III* Monographie *§27.2* — **dans le formalisme ArchiMate**, sans reprendre leur fond (posé aux Livres III et VII). *La ligne Fusion ci-dessus cite ce renvoi au plan (`Vol. III `*TOC*` §27.2`) ; la présente table cite le **texte rédigé**, où il résout à numérotation et titre concordants (collation v0.14).*

⚠ **Ancrage de version** : **ArchiMate 4** (The Open Group, doc **C260**, 27 avr. 2026), équivalents **3.2** (oct. 2022) en notes de transition. **Relève v0.7 — ampleur confirmée par l'éditeur** : réduction d'environ 30 % du nombre d'éléments (de plus de soixante à une quarantaine), couches remplacées par des **domaines**, multiplicité sur les relations — la refonte de métamodèle la plus profonde depuis la création du langage. **La re-vérification du mécanisme Specialization + stéréotype + Profiles tel que C260 le porte est un préalable au registre des stéréotypes**, non une note de transition. À la mi-2026, la quasi-totalité des outils n'exporte et n'importe encore que **3.2** nativement — le blueprint des ch. 49-50 n'est donc **pas échangeable en v4** dans la plupart des ateliers.

⚠ **Garde-fou de non-redondance (hérité du Vol. I §6.0.1, plus nécessaire ici qu'à sa source)** : « si l'on retire le mot ArchiMate et que la phrase tient encore comme un exposé des chapitres amont, c'est une redondance à renvoyer ». **Au Vol. I ce chapitre en suivait cinq ; ici il en suit quarante-sept.** Ce que le chapitre apporte est une **traduction structurelle**, jamais une reprise du fond conceptuel.

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §6.0 | § 48.0 | condensé ; §6.0.1 refondu en apparat |
| §6.1-6.7 | § 48.1-48.7 | condensé |
| §6.8 | **ch. 50** | prélevé (exemple de bout en bout) |
| §6.9 | § 48.8 | condensé |
| §6.10 | **ch. 47** | prélevé (maturité par plateaux) |
| §6.11 | § 48.9 | condensé |
| Vol. III *Monographie* §27.2 | § 48 (transverse) | formalisation seule |

### Chapitre 49 — Le blueprint instancié : de Boréalis au portefeuille IBM à la fabrique de confiance

**Thèse** : le blueprint applique les principes directeurs à un portefeuille réel documenté ; chaque couche porte son positionnement OO, son statut de preuve et son point d'intégration avec l'IAM et l'observabilité en place — étendre, jamais dupliquer.
Sections : principes directeurs (dont « aucune interaction IA non gouvernée ») ; C1-C8 avec composants IBM datés (GA/préversion/déprécié ; pivot Confluent clôturé le 17 mars 2026 — écrire au passé) ; correspondance réglementaire (statuts explicites — **aucune conformité E-23/B-13 revendiquée par IBM : fait négatif *établi*, non *vérifié***, garde-fou R-07 du Vol. III et échelle des trois degrés d'absence) ; l'organisation de la fabrique (rôles entre plateforme, IAM, sécurité, exploitation ; préparation organisationnelle — **corpus d'appui**, cadrage et non preuve, filiation retirée par P0.2 le 21 juill. 2026, réversible : voir le bloc Corpus d'appui ; facteur humain et conduite du changement).
*Fusion : Vol. II ch. 22 (**repris en entier** : principes, couches C1-C8 et neutralité fournisseur — ce chapitre ne porte aucun flux) + Vol. II ch. 23 **§23.1 seul** (le tableau B.3 développé : quatre statuts, sept liens) + Vol. III ch. 27 §27.3/§27.5 + Vol. I Annexe B (ADS Boréalis, résumée ici, complète en Annexe H). **Décision de fusion** : les deux instanciations (Boréalis du Vol. I, portefeuille IBM du Vol. II) sont présentées comme deux réalisations de la même architecture de référence, non comme deux blueprints concurrents. Socle : F-38 à F-46 (F-39, F-40 et F-42 à nommer un à un, la plage seule ne les désignant pas) ; **PRD** Vol. II Annexe B §B.1-B.2 (blueprint d'architecture). Garde-fous : **CA-8** (chaque composant tracé au socle, chaque lien réglementaire marqué « documenté » ou « inférence »), PRD Vol. II §8.4 (neutralité fournisseur), **lacune héritée portée : PRD Vol. II §10.6** (portefeuille IBM — Gartner MQ iPaaS sous R-6 du Vol. II, FTM/ISO 20022 en [C] après élévation tentée et échouée, annonces canadiennes ouvertes ; renvoi ch. 57), **R-5, R-6, R-7 et R-8 du Vol. II** — nommés par volume, ce chapitre consommant aussi du Vol. III, dont les R-05…R-08 portent sur d'autres objets (décision 7).*

**Table des matières détaillée du chapitre 49**

*Dérivée du texte rédigé de `Monographie.md` ch. 22 et ch. 23 §23.1 (Vol. II), ch. 27 (Vol. III) et Annexe B (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 49.1 — Les principes directeurs

*← Vol. II §22.1 (les six principes, dont « **aucune interaction IA non gouvernée** »).*

#### § 49.2 — La vue en couches C1-C8, avec statuts datés

*← Vol. II §22.2 ; composants IBM datés GA / préversion / déprécié.* ⚠ **Pivot Confluent clôturé le 17 mars 2026 — écrire au passé.**

#### § 49.3 — La neutralité fournisseur en pratique

*← Vol. II §22.3 + PRD Vol. II §8.4.*

#### § 49.4 — Correspondance réglementaire : le tableau B.3 développé

*← Vol. II §23.1 (**§23.1 seul** : quatre statuts, sept liens).*

⚠ **Aucune conformité E-23/B-13 revendiquée par IBM : fait négatif *établi*, non *vérifié*** — garde-fou **R-07 du Vol. III** et échelle des trois degrés d'absence (R-14). **CA-8** : chaque lien réglementaire marqué « documenté » ou « inférence ».

#### § 49.5 — Points d'intégration avec l'existant : étendre, ne pas dupliquer

*← Vol. III* Monographie *§27.3 ; IAM et observabilité en place (Livres III et VII).*

#### § 49.6 — L'organisation de la fabrique : qui opère quoi

*← Vol. III* Monographie *§27.5 ; rôles entre plateforme, IAM, sécurité, exploitation.* ⚠ **Préparation organisationnelle : corpus d'appui, cadrage et non preuve** (filiation retirée par P0.2, réversible). Facteur humain et conduite du changement.

#### § 49.7 — L'ADS Boréalis, résumée

*← Vol. I Annexe B ; **intégrale à l'Annexe H**.* ⚠ **Décision de fusion** : les deux instanciations — Boréalis (Vol. I) et portefeuille IBM (Vol. II) — sont présentées comme **deux réalisations de la même architecture de référence**, non comme deux blueprints concurrents.

⚠ **Ce chapitre ne porte aucun flux** : le ch. 22 du Vol. II est repris **en entier** (principes, couches, neutralité) ; les trois flux sont au ch. 50. ⚠ **Socle** : F-38 à F-46 — **F-39, F-40 et F-42 à nommer un à un, la plage seule ne les désignant pas** ; **PRD** Vol. II Annexe B §B.1-B.2. **Lacune héritée portée (PRD Vol. II §10.6)** : portefeuille IBM — Gartner MQ iPaaS sous **R-6**, FTM/ISO 20022 en [C] après élévation tentée et échouée, annonces canadiennes ouvertes ; renvoi ch. 57. **Garde-fous R-5, R-6, R-7 et R-8 du Vol. II** — nommés par volume (décision 7), ce chapitre consommant aussi du Vol. III, dont les R-05…R-08 portent sur d'autres objets.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §22.1-22.3 | § 49.1-49.3 | **repris en entier** |
| Vol. II §23.1 | § 49.4 | **§23.1 seul** — §23.2-23.4 au ch. 50 |
| Vol. III *Monographie* §27.3, §27.5 | § 49.5-49.6 | condensé |
| Vol. I Annexe B (ADS) | § 49.7 | résumée ; intégrale à l'Annexe H |

### Chapitre 50 — Instanciation : le cycle de vie complet d'un agent d'entreprise

**Thèse** : le blueprint se prouve par le parcours — de l'enregistrement à la révocation, chaque transition est jouée contre l'architecture, au grain d'un cas financier canadien (continuité Boréalis).
Sections : naissance (enregistrement, émission du passeport, admission au maillage) ; vie (délégations, vérifications par arête, traces d'exploitation, évaluations continues, migration PQC) ; mort (révocation, cascade dans la chaîne de mandat, retrait, archivage probatoire) ; trois flux de bout en bout (décision de crédit, **OO3 ou OO4 — le positionnement est une inférence d'auteur, le socle n'établissant pas la conscience du processus qui les sépare** ; ⚠ le flux outille un **point d'arrêt humain**, **jamais la révision de l'article 12.1** — le ch. 23 du Vol. II écrit que « le blueprint ne doit pas prétendre le contraire » ; paiement ISO 20022 vers Lynx ; accès cadre bancaire sous passerelle d'outils) ; confrontation externe (cas fil rouge *loan processing* — **corpus d'appui**, cadrage et non preuve).
*Fusion : Vol. III ch. 28 (**hors §28.5 et §28.6**, prélevés par les ch. 56 et ch. 57) + Vol. II ch. 23 **§23.2-23.4** (les trois flux ; son §23.1 va au ch. 49 — ⚠ **c'est le ch. 23 qui est scindé, non le ch. 22** : les v0.1-v0.5 attribuaient la scission au mauvais chapitre, le ch. 22 ne portant aucun flux) + Vol. I* Monographie *§6.8 (exemple de bout en bout : souscription vie augmentée et variante FNOL — **prélevé au ch. 6**). Socle : **F-39 à F-42 et F-44 à F-46** (plage relevée sur l'en-tête du ch. 23 du Vol. II : ni F-38 ni F-43 n'y figurent, contrairement à ce qu'annonçaient les v0.1-v0.5), F-27, F-28, F-34, F-35 ; **PRD** Vol. II Annexe B §B.3-B.4 (blueprint d'architecture). Garde-fou : **CA-8**.*

**Table des matières détaillée du chapitre 50**

*Dérivée du texte rédigé de `Monographie.md` ch. 28 (Vol. III), ch. 23 §23.2-23.4 (Vol. II) et §6.8 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 50.1 — Naissance : enregistrement, émission du passeport, admission au maillage

*← Vol. III* Monographie *§28.1 ; ch. 16-17 et ch. 41-42 joués contre l'architecture.*

#### § 50.2 — Vie : délégations, vérifications par arête, traces, évaluations continues, renouvellements, migration post-quantique

*← Vol. III* Monographie *§28.2 ; ch. 18, 42, 43, 44 et 23-24.*

#### § 50.3 — Mort : révocation, cascade dans la chaîne de mandat, retrait du maillage, archivage probatoire

*← Vol. III* Monographie *§28.3 ; la révocation en cascade reste un **problème ouvert** (ch. 21 § 21.6).*

#### § 50.4 — Flux 1 — la décision de crédit assistée par agents : le processus commande, OO3 ou OO4

*← Vol. II §23.2.*

⚠ **Le positionnement OO3/OO4 est une inférence d'auteur** — le socle n'établit pas la conscience du processus qui les sépare. ⚠ **Le flux outille un point d'arrêt humain, jamais la révision de l'article 12.1** : le ch. 23 du Vol. II écrit que « le blueprint ne doit pas prétendre le contraire ».

#### § 50.5 — Flux 2 — le paiement ISO 20022 vers Lynx : l'agent observe, le rail exécute

*← Vol. II §23.3 ; ch. 37.*

#### § 50.6 — Flux 3 — l'accès au cadre bancaire : concevoir contre une norme qui n'existe pas encore

*← Vol. II §23.4 ; ch. 36 (standard technique non désigné, fait négatif vérifié).*

#### § 50.7 — Exemple de bout en bout : souscription vie augmentée (et variante FNOL P&C)

*← Vol. I* Monographie *§6.8.1-6.8.5 (**prélevé au ch. 6**) : Motivation, Strategy, Business (point HITL sur l'irréversible), Application (agent orchestrateur, serveurs MCP-FHIR), Technology & Implementation.*

#### § 50.8 — Confrontation externe

*← Vol. III* Monographie *§28.4 (confrontation interne au corpus).* ⚠ Cas fil rouge *loan processing* : **corpus d'appui, cadrage et non preuve**.

⚠ **C'est le ch. 23 du Vol. II qui est scindé, non le ch. 22** : les v0.1-v0.5 attribuaient la scission au mauvais chapitre, le ch. 22 ne portant aucun flux. ⚠ **Socle : F-39 à F-42 et F-44 à F-46** — plage relevée sur l'en-tête du ch. 23 du Vol. II : **ni F-38 ni F-43 n'y figurent**, contrairement à ce qu'annonçaient les v0.1-v0.5 —, plus F-27, F-28, F-34, F-35 ; **PRD** Vol. II Annexe B §B.3-B.4. **Garde-fou CA-8.**

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. III *Monographie* §28.1-28.4 | § 50.1-50.3, § 50.8 | condensé |
| Vol. III *Monographie* §28.5 | ch. 56 | prélevé (questions transmises) |
| Vol. III *Monographie* §28.6 | ch. 57 | prélevé (péremption) |
| Vol. II §23.2-23.4 | § 50.4-50.6 | condensé ; §23.1 au ch. 49 |
| Vol. I *Monographie* §6.8 | § 50.7 | **prélevé au ch. 48** |

### Chapitre 51 — Instrumentation et feuille de route vers le 1ᵉʳ mai 2027

**Thèse** : les métriques d'évaluation des orchestrations (correction, réactivité, traçabilité) sont l'instrumentation candidate des programmes E-23/AMF ; la feuille de route se séquence sur l'entrée en vigueur commune (inventaire → encadrement → surveillance).
Sections : des métriques académiques aux indicateurs de risque de modèle ; feuille de route type par plateaux ; jalons externes à surveiller.
*Fusion : Vol. II ch. 20. Socle : F-09, F-25, F-37, F-44. Garde-fou : **R-7 du Vol. II** (instrumentation d'E-23 par watsonx.governance = inférence d'auteur) — à ne pas confondre avec le R-07 du Vol. III, qui porte lui aussi sur l'inférence produit ↔ réglementation : le renvoi nu était plausible dans les deux lectures, donc indécidable (décision 7).*

**Table des matières détaillée du chapitre 51**

*Dérivée du texte rédigé de `Monographie.md` ch. 20 (Vol. II) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 51.1 — Des métriques académiques aux indicateurs de risque de modèle

*← Vol. II §20.1 ; correction, réactivité, traçabilité (ch. 25 § 25.2) comme **instrumentation candidate** des programmes E-23/AMF.*

⚠ **Garde-fou R-7 du Vol. II** : l'instrumentation d'E-23 par watsonx.governance est une **inférence d'auteur**. **Ne pas confondre avec le R-07 du Vol. III**, qui porte lui aussi sur l'inférence produit ↔ réglementation — le renvoi nu était plausible dans les deux lectures, donc **indécidable** (décision 7).

#### § 51.2 — Feuille de route type : inventaire, encadrement, surveillance

*← Vol. II §20.2 ; séquencée sur l'entrée en vigueur commune du 1ᵉʳ mai 2027 (ch. 29 et ch. 31).*

#### § 51.3 — Les jalons externes à surveiller

*← Vol. II §20.3 ; recoupe les événements de péremption du ch. 57, sans les reconstruire.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §20.1-20.3 | § 51.1-51.3 | condensé |

---

## LIVRE IX — L'agent comme livrable logiciel : provenance, mise en service, sémantique d'effet

*(matière neuve — aucun volume source ; réouverture v0.8 de la décision de périmètre v0.3, sur instruction d'auteur du 20 juillet 2026 ; ~14 000 mots)*

⚠ **Statut singulier, déclaré avant tout contenu (décision 9, risque 13).** Ce livre ne fusionne rien. Les trois volumes traitent l'agent comme un *interlocuteur* — qui parle à quoi, sous quelle autorité — et l'audit v0.3 a établi qu'aucun ne le traite comme un *livrable logiciel qui produit des effets* ; les trois fronts qui en découlent avaient été écartés sur décision d'auteur, avec un ordre d'instruction suggéré pour leur réouverture — c'est cet ordre qui fait l'ordre des chapitres. **Aucun socle hérité, aucune entrée F-xx, aucun garde-fou source** : tout énoncé de ce livre est au mieux un repérage [C] à instruire, ses sources primaires sont à constituer intégralement, et sa rédaction vient **en dernier** — après même les Livres III et VII (risque 11), qui disposent au moins des repérages du Vol. III. Si le socle ne se constitue pas au lancement de la rédaction, le retrait du livre est l'issue prévue : les trois fronts retombent au statut v0.7, consignés au journal v0.3 comme choix de périmètre. **Critère d'exclusion propre** : tout contenu sans rattachement aux livres amont — identité (III), encadrement (IV), exploitation (VII), blueprint (VIII) — est hors périmètre ; ce livre complète la somme, il n'ouvre pas une thèse indépendante.

### Chapitre 52 — La provenance des composants : de quoi un agent est fait

**Thèse** *(construction d'auteur, socle à constituer)* : l'identité du Livre III certifie le *porteur* d'un agent, jamais sa *composition* — poids de modèle, serveurs d'outils, bibliothèques, invites ; la provenance des composants (nomenclatures logicielles et d'IA, signature et attestation d'artefacts) est le chaînon entre le passeport du ch. 17 et l'intégrité en exécution du ch. 21 — et le front le plus mûr des trois (jugement v0.3, que les relèves 2 et 7 de la v0.7 confirment : politique de dépréciation protocolaire, compromissions de chaîne d'approvisionnement d'agents).
Sections : l'agent comme artefact composé (inventaire des composants et de leurs horloges) ; nomenclatures logicielles et d'IA — état des normes et de l'outillage ; signature et attestation d'artefacts (modèles, serveurs d'outils, invites) ; le rug-pull du ch. 21 relu comme défaut de provenance ; la provenance comme pièce candidate du passeport du ch. 17 (construction d'auteur, marquée telle) ; les divulgations de chaîne d'approvisionnement du 1ᵉʳ semestre 2026 (relève 7 de la v0.7 — candidates, à instruire à sources primaires) ; ⚠ **relève v0.10 — l'extension déclarative, composant que la nomenclature ne voit pas** : les harnais admettent des extensions par simple configuration — fichiers d'instructions réutilisables, serveurs d'outils déclarés en JSON —, dont l'installation n'est ni une compilation ni un déploiement et échappe donc aux nomenclatures logicielles classiques ; des chercheurs d'un éditeur de sécurité ont relevé fin janvier 2026 une extension tierce d'un runtime largement déployé pratiquant exfiltration de données et injection d'invite à l'insu de l'utilisateur. **Incident candidat, relevé en sources ouvertes, aucune source primaire extraite** : il ne fonde rien tant qu'il n'est pas instruit, et il confirme sans le prouver le jugement « front le plus mûr ».
*Fusion : aucune — front neuf, sans socle hérité (journal v0.3, rouvert en v0.8). Adossements internes : ch. 17, ch. 21, ch. 22, Livre VII. Sources primaires à constituer avant rédaction (risque 13).*

**Table des matières détaillée du chapitre 52**

*⚠ **Table sans provenance externe, et c'est le fait à retenir.** Les ch. 52-54 sont de la **matière neuve** : « Fusion : aucune » (décision 9). Aucune sous-section ci-dessous ne peut porter de renvoi `←` vers un volume source — il n'y en a pas. Les seuls appuis sont **internes** (chapitres de la somme) et tout énoncé est **au mieux un repérage [C] à instruire**. Table de travail dérivée de la liste de sections du TOC, non d'un texte rédigé.*

#### § 52.1 — L'agent comme artefact composé

inventaire des composants et de leurs horloges (poids de modèle, serveurs d'outils, bibliothèques, invites). *Construction d'auteur.*

#### § 52.2 — Nomenclatures logicielles et d'IA : état des normes et de l'outillage

*sources primaires à constituer.*

#### § 52.3 — Signature et attestation d'artefacts

modèles, serveurs d'outils, invites ; adossement ch. 21 § 21.3 (attestation d'intégrité à l'exécution), sans le reconstruire.

#### § 52.4 — Le *rug-pull* du ch. 21 relu comme défaut de provenance

adossement ch. 21 § 21.1.

#### § 52.5 — La provenance comme pièce candidate du passeport du ch. 17

⚠ **construction d'auteur, marquée telle** : le passeport n'existe dans aucune spécification de 2026, et lui ajouter une cinquième pièce est un geste d'auteur sur un objet déjà virtuel.

#### § 52.6 — Les divulgations de chaîne d'approvisionnement du 1ᵉʳ semestre 2026

*relève 7 de la v0.7 : **candidates, à instruire à sources primaires**.*

#### § 52.7 — ⚠ Relève v0.10 : l'extension déclarative, composant que la nomenclature ne voit pas

les harnais admettent des extensions par **simple configuration** (fichiers d'instructions réutilisables, serveurs d'outils déclarés en JSON), dont l'installation n'est **ni une compilation ni un déploiement** et échappe donc aux nomenclatures logicielles classiques. Des chercheurs d'un éditeur de sécurité ont relevé fin janvier 2026 une extension tierce d'un *runtime* largement déployé pratiquant exfiltration de données et injection d'invite à l'insu de l'utilisateur.

⚠ **Incident candidat, relevé en sources ouvertes, aucune source primaire extraite** : il **ne fonde rien** tant qu'il n'est pas instruit, et il **confirme sans le prouver** le jugement « front le plus mûr ».

**Table de couverture (décision 6)** — *sans objet : la décision 6 (couverture tracée) ne s'applique pas à un chapitre sans source. La **décision 8 s'y applique doublement** : aucune thèse ne peut se recopier telle quelle dans le bandeau du chapitre rédigé.*

| Appui | Nature |
| --- | --- |
| ch. 17, ch. 21, ch. 22, Livre VII | **adossements internes** — renvois, jamais sources |
| relèves v0.7 (relève 7) et v0.10 | repérages [C] à instruire |
| — | **aucun volume source, aucune entrée F-xx, aucun garde-fou hérité** |

### Chapitre 53 — La mise en service d'un artefact non reproductible

**Thèse** *(construction d'auteur, socle à constituer)* : mettre en service un agent dont le comportement n'est pas reproductible à l'identique exige une discipline propre — jeux d'essai de référence, barrière d'évaluation au déploiement, versionnement à quatre horloges (modèle, invites, outils, politique) — sans laquelle l'évaluation continue du ch. 44 mesure un artefact que l'organisation ne sait pas même désigner.
Sections : le versionnement à quatre horloges (ce que « version d'un agent » veut dire) ; jeux d'essai de référence et barrière d'évaluation au déploiement (pont : évaluation du ch. 6, évaluation continue du ch. 44) ; promotion par environnements et GitOps du parc (le ch. 44 au grain du déploiement, sans le reconstruire) ; retour arrière d'un artefact à état (ce que le rollback ne restaure pas — mémoire, délégations en cours) ; l'enregistrement de version au registre du ch. 16 (construction d'auteur).
*Fusion : aucune — front neuf, sans socle hérité (journal v0.3, rouvert en v0.8). Adossements internes : ch. 6, ch. 16, ch. 44, ch. 50. Sources primaires à constituer avant rédaction (risque 13). ⚠ **Relève v0.10 — la thèse compte peut-être une horloge de trop peu.** Les pièces écrites de 2026 exhibent un cinquième porteur de version, autonome des quatre : le **harnais lui-même**, versionné par son éditeur, et dont le changement modifie le comportement observable à modèle, invites, outils et politique constants (modes, seuils de compression de contexte, ordre des règles d'approbation, format d'événements). Si la relève s'instruit, la thèse est **sous-spécifiée, non fausse** ; elle n'est **pas réécrite ici** — la décision 8 veut que le chapitre corrige le plan, non que le plan anticipe sur l'instruction.*

**Table des matières détaillée du chapitre 53**

*⚠ Matière neuve — « Fusion : aucune ». Aucun renvoi `←` vers un volume source : il n'y en a pas. Appuis internes seulement ; tout énoncé est un repérage [C] à instruire. Table dérivée de la liste de sections du TOC.*

#### § 53.1 — Le versionnement à quatre horloges

ce que « version d'un agent » veut dire : modèle, invites, outils, politique. *Construction d'auteur.*

⚠ **Relève v0.10 — la thèse compte peut-être une horloge de trop peu.** Les pièces écrites de 2026 exhibent un **cinquième porteur de version, autonome des quatre : le harnais lui-même**, versionné par son éditeur, dont le changement modifie le comportement observable **à modèle, invites, outils et politique constants** (modes, seuils de compression de contexte, ordre des règles d'approbation, format d'événements). Si la relève s'instruit, la thèse est **sous-spécifiée, non fausse** ; elle **n'est pas réécrite ici** — la décision 8 veut que le chapitre corrige le plan, non que le plan anticipe sur l'instruction.

#### § 53.2 — Jeux d'essai de référence et barrière d'évaluation au déploiement

ponts : évaluation du ch. 6 (fondements), évaluation continue du ch. 44 § 44.1.

#### § 53.3 — Promotion par environnements et GitOps du parc

le ch. 44 § 44.4 **au grain du déploiement**, sans le reconstruire ; pré-production gouvernée au ch. 45 § 45.6.

#### § 53.4 — Retour arrière d'un artefact à état

**ce que le *rollback* ne restaure pas** : mémoire, délégations en cours. Adossement ch. 18 (chaîne de mandat) et ch. 44 § 44.2 (dérive de mémoire).

#### § 53.5 — L'enregistrement de version au registre du ch. 16

⚠ **construction d'auteur** : le registre gouverné n'enregistre pas de version dans les spécifications relevées.

**Table de couverture (décision 6)** — *sans objet (chapitre sans source). Décision 8 applicable doublement.*

| Appui | Nature |
| --- | --- |
| ch. 6, ch. 16, ch. 44, ch. 50 | **adossements internes** — renvois, jamais sources |
| relève v0.10 (cinquième horloge) | repérage [C] à instruire ; thèse **sous-spécifiée, non fausse** |
| — | **aucun volume source, aucune entrée F-xx, aucun garde-fou hérité** |

### Chapitre 54 — La sémantique d'effet : idempotence, compensation, réconciliation

**Thèse** *(construction d'auteur, socle à constituer)* : une action d'agent produit des effets dans des systèmes d'enregistrement, et ce qui advient quand elle réussit à moitié — idempotence, compensation, réconciliation — n'est spécifié ni par les protocoles (Livre II) ni par l'encadrement (Livre VI) ; c'est en finance que le coût de ce silence est maximal (un virement à moitié réussi n'est pas un incident d'observabilité, c'est un écart comptable).
Sections : taxonomie des effets d'une action d'agent (lecture, écriture, engagement) ; idempotence et rejouabilité des appels d'outils (ce que les spécifications protocolaires en disent — à instruire, jamais présumé) ; compensation et sagas au grain de l'agent (héritage EIP du ch. 1 et exécution durable du ch. 25, appliqués, non reconstruits) ; réconciliation des flux financiers (pont : flux ISO 20022 des ch. 37 et ch. 50) ; tracer l'effet, pas seulement l'appel (prolonge le chaînon manquant du ch. 43 ; ⚠ **relève v0.10 — une taxonomie candidate existe déjà, en vocabulaire de sûreté** : une préimpression adverse de mai 2026 tient la détection des divergences entre l'action effectuée et son enregistrement d'audit pour la propriété porteuse d'un runtime agentique, et en énumère quatre — contournement de garde, falsification du journal, échec silencieux de l'hôte, cible erronée. C'est, dit autrement, la question de ce chapitre. **Deux réserves** : la préimpression n'est pas révisée par les pairs, et elle propose une implémentation concurrente de l'objet qu'elle mesure — son intérêt est inverse de celui de l'éditeur, ce qui ne le neutralise pas. Taxonomie à instruire ; aucun de ses résultats chiffrés n'est repris).
*Fusion : aucune — front neuf, sans socle hérité (journal v0.3, rouvert en v0.8). Adossements internes : ch. 1, ch. 25, ch. 37, ch. 43, ch. 50. Sources primaires à constituer avant rédaction (risque 13).*

**Table des matières détaillée du chapitre 54**

*⚠ Matière neuve — « Fusion : aucune ». Aucun renvoi `←` vers un volume source : il n'y en a pas. Appuis internes seulement ; tout énoncé est un repérage [C] à instruire. Table dérivée de la liste de sections du TOC.*

#### § 54.1 — Taxonomie des effets d'une action d'agent

lecture, écriture, engagement. *Construction d'auteur.*

#### § 54.2 — Idempotence et rejouabilité des appels d'outils

ce que les spécifications protocolaires en disent : **à instruire, jamais présumé** (Livre II).

#### § 54.3 — Compensation et sagas au grain de l'agent

héritage EIP du ch. 1 § 1.6.2 et exécution durable du ch. 25 § 25.5, **appliqués, non reconstruits**.

⚠ *C'est la **seule occurrence de « sagas »** de toute la zone des chapitres, au grain d'une action unique — le constat qui fonde le **risque 15** (accord entre agents sous asynchronie et défaillance partielle : angle mort déclaré, non comblé).*

#### § 54.4 — Réconciliation des flux financiers

ponts : flux ISO 20022 des ch. 37 et ch. 50 § 50.5 ; le trou de responsabilité du ch. 40 § 40.2.6.

#### § 54.5 — Tracer l'effet, pas seulement l'appel

prolonge le **chaînon manquant** du ch. 43 § 43.5.

⚠ **Relève v0.10 — une taxonomie candidate existe déjà, en vocabulaire de sûreté** : une préimpression adverse de mai 2026 tient la **détection des divergences entre l'action effectuée et son enregistrement d'audit** pour la propriété porteuse d'un *runtime* agentique, et en énumère quatre — contournement de garde, falsification du journal, échec silencieux de l'hôte, cible erronée. **C'est, dit autrement, la question de ce chapitre.**

⚠ **Deux réserves** : la préimpression **n'est pas révisée par les pairs**, et elle **propose une implémentation concurrente de l'objet qu'elle mesure** — son intérêt est inverse de celui de l'éditeur, *ce qui ne le neutralise pas*. Taxonomie à instruire ; **aucun de ses résultats chiffrés n'est repris**.

⚠ *Thèse à retenir pour le vertical : **un virement à moitié réussi n'est pas un incident d'observabilité, c'est un écart comptable** — c'est en finance que le coût du silence des protocoles (Livre II) et de l'encadrement (Livre IV) est maximal.*

**Table de couverture (décision 6)** — *sans objet (chapitre sans source). Décision 8 applicable doublement.*

| Appui | Nature |
| --- | --- |
| ch. 1, ch. 25, ch. 37, ch. 43, ch. 50 | **adossements internes** — renvois, jamais sources |
| relève v0.10 (quatre divergences) | repérage [C] à instruire ; chiffres non repris |
| — | **aucun volume source, aucune entrée F-xx, aucun garde-fou hérité** |

---

## LIVRE X — Horizon et frontière de la connaissance vérifiable

*(fusionne Vol. I ch. 7 + §3.13.2-3.13.4 + Vol. II ch. 21/24 + Vol. III clôture ; ~20 000 mots)*

### Chapitre 55 — L'horizon 2027-2032

**Thèse** *(prospectif, sans céder à la prédiction)* : une grappe d'échéances datées (PROGRAMMÉ) structure l'horizon ; au-delà, la trajectoire des protocoles, de la gouvernance par couche, de l'identité vérifiable/PQC, de la menace et de la recherche se lit en PROJETÉ, jamais en SPÉCULATIF déguisé en certitude.
Sections : la grappe d'échéances 2027-2032 (squelette daté) ; trajectoire des protocoles (coexistence stratifiée gouvernée, souveraineté) ; bifurcation de la gouvernance par couche (AAIF, FIDO, W3C, IETF, DIF) ; identité vérifiable et PQC (l'horloge — renvoi ch. 23-24) ; trajectoire de la menace (agentic SOC — renvoi ch. 22) ; programme de recherche (sémantique, garanties composables, science de l'évaluation) ; trajectoire macro (capacité, coût, soutenabilité, souveraineté) ; prospective d'entreprise et finance ; responsabilité, assurabilité, gouvernance de l'émergence ; scénarios 2027-2032.
*Fusion : Vol. I* Monographie *ch. 7 (**hors §7.4.1-§7.4.4, prélevés par le Livre III — §7.4.2/§7.4.3 côté émission, §7.4.1/§7.4.4 côté horloge post-quantique**) + §3.13.2-3.13.4 (coexistence et souveraineté, programme de recherche sémantique, synthèse — **seule affectation du reste de §3.13**, le ch. 7 ne recevant que §3.13.1). Garde-fou : tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF systématique. ⚠ **Relève v0.10** : une thèse de trajectoire sur la couche d'exécution est candidate à ce chapitre — « tout harnais s'étend jusqu'à devenir un *claw* », décalque de la loi de Zawinski, énoncée en conférence le 21 juillet 2026. Si elle y entre, elle y entre en **PROJETÉ**, attribuée nommément à son auteur, jamais en PROGRAMMÉ ; sa forme d'origine est une loi d'humour d'ingénierie — ce qui n'en fait pas une prédiction fausse, mais interdit de la citer comme une régularité établie. Le régime qu'elle décrit — agent hors session, déclenché par événement, sollicitant l'humain sur ses propres canaux — touche aussi les ch. 42, 44 et 45 (journal v0.10, relève 7). ⚠ **Relèves v0.11 — deux objets pour deux sections.** (1) *Responsabilité, assurabilité* : une préimpression de juillet 2026 (arXiv 2607.11999) propose une pile d'assurance des agents à huit composantes, à l'horizon 2030 — première architecture candidate pour une section jusqu'ici sans objet instruit ; à l'entrée, en PROJETÉ, l'horizon 2030 étant celui des auteurs, pas un jalon. (2) *Trajectoire macro* : la littérature de prépublication 2025-2026 se donne des échelles au-delà de l'agentique — niveaux croisant performance, généralité et autonomie (arXiv 2311.02462) et « chemin vers la superintelligence artificielle » assumé jusque dans les titres (arXiv 2507.21046). Si ces échelles entrent au chapitre, la trajectoire d'infrastructure s'écrit en PROJETÉ et la visée superintelligence en **SPÉCULATIF** — le tri du chapitre existe pour ce cas exact ; l'autonomie graduée du plan (ch. 26) y trouve un vis-à-vis publié, jamais une validation.*

**Table des matières détaillée du chapitre 55**

*Dérivée du texte rédigé de `Monographie.md` ch. 7 et §3.13.2-3.13.4 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 55.0 — Orientation : lire un chapitre prospectif sans céder à la prédiction

*← §7.0.2 (**SIÈGE de la discipline** : les trois statuts PROGRAMMÉ / PROJETÉ / SPÉCULATIF), §7.0.3 (cône d'incertitude, frise) et §7.0.4 (ni feuille de route produit, ni prédiction d'AGI). Le §7.0.1 est refondu en apparat.*

#### § 55.1 — La grappe d'échéances 2027-2032 : le squelette daté (PROGRAMMÉ)

*← §7.1.1-7.1.4 : la concentration de 2027 ; échéances d'identité et de standards ; échéances financières et de règlement ; **le caractère mouvant du « programmé » — discipline de re-datation**.*

#### § 55.2 — Trajectoire des protocoles : vers la coexistence stratifiée gouvernée

*← §7.2.1-7.2.4 + §3.13.2 (coexistence vs convergence, agentic web, souveraineté — **seule affectation du reste de §3.13**, le ch. 7 ne recevant que §3.13.1).*

#### § 55.3 — La bifurcation de la gouvernance par couche : AAIF, FIDO, W3C, IETF, DIF

*← §7.3.1-7.3.4 : cartographie de la fragmentation ; Community Groups du W3C comme signal faible ; **neutralité contestée — la « standardisation » peut renforcer les dominants** ; normalisation institutionnelle (ISO/IEC SC 42, CEN-CENELEC JTC 21, NIST CAISI).* ⚠ Le §7.3 est **prélevé au ch. 7**, qui ne reçoit que §3.13.1.

#### § 55.4 — Identité vérifiable et PQC : l'horloge

renvoi ch. 23-24. ⚠ **Les §7.4.1-§7.4.4 sont prélevés par le Livre III** (§7.4.2/§7.4.3 côté émission, §7.4.1/§7.4.4 côté horloge) : **ce chapitre y renvoie sans les reconstruire**.

#### § 55.5 — Trajectoire de la menace

renvoi ch. 22. ⚠ Le §7.5 est **prélevé par le ch. 22** : renvoi, pas reprise.

#### § 55.6 — Le programme de recherche

*← §7.6.1-7.6.6 : le **verrou sémantique et pragmatique (SIÈGE)** + §3.13.3 (programme de recherche sémantique) ; garanties composables sur acteurs probabilistes ; renaissance critique de l'héritage AAMAS ; science de l'évaluation et certification inter-fournisseurs ; sécurité formelle des frontières ; visions « Internet of Agents » / « Agentic Web ».*

#### § 55.7 — Trajectoire technologique et macro

*← §7.7.1-7.7.x : courbe de capacité d'autonomie (ce que mesurent et ne mesurent pas les horizons de tâche) ; économie de l'inférence et viabilité des flottes ; coût, soutenabilité, souveraineté.*

⚠ **Relève v0.11** : la littérature de prépublication 2025-2026 se donne des échelles **au-delà de l'agentique** — niveaux croisant performance, généralité et autonomie (arXiv 2311.02462) ; « chemin vers la superintelligence artificielle » assumé jusque dans les titres (arXiv 2507.21046). Si ces échelles entrent, la trajectoire d'infrastructure s'écrit en **PROJETÉ** et la visée superintelligence en **SPÉCULATIF** — le tri existe pour ce cas exact ; l'autonomie graduée du ch. 26 y trouve **un vis-à-vis publié, jamais une validation**.

#### § 55.8 — Prospective d'entreprise

*← §7.8.1-7.8.6 : sortie du « pilot purgatory » ; assainissement du marché et « agent washing » ; **lecture critique des projections de taille de marché** ; l'organisation agentique à maturité ; recomposition du travail ; **N×M → N+M comme moteur de marché : un pari, pas un chiffre**.*

#### § 55.9 — La finance à l'horizon

*← §7.9.1-7.9.6 : fenêtre où les exigences deviennent contraignantes ; course aux rails de mandat ; monnaie programmable et règlement agentique ; **risque systémique des agents corrélés — monoculture, herding, « AI monitoring AI »** ; migration des standards de données vers le code exécutable ; maturation de l'autonomie bornée.*

#### § 55.10 — Responsabilité, assurabilité et gouvernance de l'émergence

*← §7.10.1-7.10.5 : vide de responsabilité (retrait de l'AILD, PLD 2024) ; la piste d'audit comme substitut ; **l'assurabilité comme régulateur de fait** ; gouvernance de l'émergence ; risques de second ordre.*

⚠ **Relève v0.11** : une préimpression de juillet 2026 (arXiv 2607.11999) propose une **pile d'assurance des agents à huit composantes** à l'horizon 2030 — première architecture candidate pour une section jusqu'ici sans objet instruit ; à l'entrée, en **PROJETÉ**, l'horizon 2030 étant celui des auteurs, **pas un jalon**.

#### § 55.11 — Scénarios 2027-2032 et synthèse

*← §7.11.1-7.11.6 + §3.13.4 (synthèse) : tenir le cône d'incertitude ; scénarios croisés (convergence/fragmentation × régulé/dérégulé × souverain/ouvert) ; **wildcards** ; conditions pour que l'interop agentique tienne ses promesses ; questions ouvertes consolidées.*

⚠ **Relève v0.10** : « tout harnais s'étend jusqu'à devenir un *claw* » — décalque de la loi de Zawinski, énoncée en conférence le 21 juillet 2026. Si elle entre, **en PROJETÉ, attribuée nommément**, jamais en PROGRAMMÉ : sa forme d'origine est une **loi d'humour d'ingénierie** — ce qui n'en fait pas une prédiction fausse, mais interdit de la citer comme une régularité établie. Le régime décrit touche aussi les ch. 42, 44 et 45.

**Table de couverture (décision 6)**

| Source Vol. I *Monographie* | Destination | Régime |
| --- | --- | --- |
| §7.0 | § 55.0 | condensé ; §7.0.1 refondu en apparat |
| §7.1-7.3 | § 55.1-55.3 | condensé |
| §7.4 | ch. 14, 17, 19, 23, 24 | **prélevé par le Livre III** — renvoi seul ici |
| §7.5 | ch. 22 | prélevé — renvoi seul ici |
| §7.6-7.11 | § 55.6-55.11 | condensé |
| §3.13.2-3.13.4 | § 55.2, § 55.6, § 55.11 | **seule affectation du reste de §3.13** |

### Chapitre 56 — La frontière de la connaissance vérifiable

**Thèse** : ce que l'on ne sait pas encore, dit honnêtement — lacunes du socle consolidé, questions ouvertes, agenda de recherche, dont le problème des deux sauts (ch. 18) et les indicateurs manquants (ch. 45).
Sections : lacunes résiduelles du socle unifié — **les onze du PRD Vol. II reprises une à une, par leur identifiant** (registre à l'Annexe C), dont §10.4 (contenu de la ligne AMF), §10.7 (composante ACP d'AGNTCY, **quatrième branche de R-8 du Vol. II**), §10.8 (absence d'attaque documentée propre à A2A), §10.9 (anatomie et gouvernance d'AP2) et §10.10 (sous-caractérisation de F-36 et F-37) ; questions de recherche transmises (les deux séries du Vol. II, nommées — *Monographie* ch. 16 §16.3 et ch. 21 §21.2) ; frontières de la fabrique de confiance.
*Fusion : Vol. II ch. 21 (Socle : PRD Vol. II §10, §8.3 ; **garde-fou R-8 du Vol. II, branche (d)** — le Vol. II assigne cette branche à son ch. 21, et les v0.1-v0.4 la perdaient avec la lacune §10.7) + Vol. III *TOC* §10.3, §26.3 et §28.5 (**questions transmises seules** — la mécanique du problème des deux sauts reste au ch. 18, qui reçoit les ch. 9-10 **du Vol. III** ; ici, l'énoncé de recherche qui en sort) + Vol. I* Monographie *§2.13.2 (questions ouvertes : horizon long, fiabilité, sécurité, apprentissage continu). ⚠ **Renvoi corrigé en v0.5** : les versions antérieures citaient « Vol. III §10.4 », qui ne résout pas — le ch. 10 du Vol. III s'arrête à §10.3 (*Question de recherche formulée pour instruction*), qui est bien la section visée par la glose. Regroupe en un seul lieu les lacunes des trois volumes ; **socle construit par la rédaction, avec la contrepartie d'énumération de l'avant-propos.***

**Table des matières détaillée du chapitre 56**

*Dérivée du texte rédigé de `Monographie.md` ch. 21 (Vol. II), §10.3/§26.3/§28.5 (Vol. III) et §2.13.2 (Vol. I) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 56.1 — Les lacunes résiduelles du socle unifié

*← Vol. II §21.1 ; **les onze du PRD Vol. II reprises une à une, par leur identifiant** (registre à l'Annexe C) :* §10.1 (organisme de normalisation, ch. 34), §10.2 (institutions sans socle complet, ch. 39), §10.3 (frameworks, ch. 27), §10.4 (**contenu de la ligne AMF — la plus coûteuse**, ch. 31), §10.5 (AP2 ↔ rails canadiens, ch. 40), §10.6 (portefeuille IBM, ch. 49), §10.7 (**composante ACP d'AGNTCY, quatrième branche de R-8**, ch. 7), §10.8 (**aucune attaque documentée propre à A2A**, ch. 11 et ch. 20), §10.9 (anatomie et gouvernance d'AP2, ch. 8 et ch. 10), §10.10 (sous-caractérisation de F-36 et F-37, ch. 25), §10.11 (datation du Budget 2025, ch. 36).

⚠ **Garde-fou R-8 du Vol. II, branche (d)** : le Vol. II assigne cette branche à son ch. 21 — les v0.1-v0.4 la perdaient avec la lacune §10.7.

⚠ **À compléter des lacunes du Vol. III**, dont la **lacune 16 (RGPD)**, non enregistrée au registre — voir l'écart signalé au ch. 34.

#### § 56.2 — Les questions de recherche transmises

*← Vol. II §21.2 + Vol. III* Monographie *§10.3 (question de recherche formulée pour instruction), §26.3 (horizon de tâche déléguée — **partagé avec le ch. 45**) et §28.5 (questions transmises) + Vol. I* Monographie *§2.13.2 (horizon long, fiabilité, sécurité, apprentissage continu).*

⚠ **Décision 7** : les **deux séries « Q n » du Vol. II** se nomment — *Monographie* ch. 16 §16.3 (cinq questions AP2/RTR, ch. 40) et ch. 21 §21.2 (six questions d'agenda, dont Q2 au ch. 20, Q3 au ch. 16, Q4 au ch. 31, Q5 au ch. 34).

⚠ **Questions transmises seules** : la **mécanique** du problème des deux sauts reste au **ch. 18**, qui reçoit les ch. 9-10 du Vol. III ; ici, **l'énoncé de recherche qui en sort**.

⚠ **Renvoi corrigé en v0.5** : les versions antérieures citaient « Vol. III §10.4 », qui **ne résout pas** — le ch. 10 du Vol. III s'arrête à **§10.3**, qui est bien la section visée par la glose.

#### § 56.3 — Les frontières de la fabrique de confiance

*← Vol. II §21.3 en partie ; dont le problème des deux sauts (ch. 18) et les **indicateurs manquants** (ch. 45 § 45.1).*

⚠ **Socle construit par la rédaction, avec la contrepartie d'énumération de l'avant-propos** : l'en-tête énumère les entrées mobilisées et les garde-fous balayés, **y compris à zéro occurrence**. Regroupe en un seul lieu les lacunes des **trois** volumes.

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §21.1-21.2 | § 56.1-56.2 | condensé |
| Vol. II §21.3 | ch. 57 + § 56.3 | **partagé** : péremption au ch. 57 |
| Vol. III *Monographie* §10.3, §26.3, §28.5 | § 56.2 | questions transmises seules ; §26.3 **partagé déclaré** avec le ch. 45 |
| Vol. I *Monographie* §2.13.2 | § 56.2 | **arrivée** depuis le ch. 6 |

### Chapitre 57 — Péremption et protocole de revalidation

**Thèse** : le compendium est daté et le dit — événements qui le périment, protocole de revalidation, conditions de gel des chapitres périssables.
Sections : événements de péremption (désignation du standard technique par arrêté, lancement effectif du RTR, révisions de MCP et d'A2A — la couche protocolaire entière du Livre II se périme au rythme de ses deux spécifications, non de la seule première ; ⚠ relève v0.7 : la ratification MCP annoncée pour le **28 juillet 2026** est le premier de ces événements à porter une date, neuf jours après ce fichier —, transfert de gouvernance d'AP2 (⚠ relève v0.7 : **candidat survenu**, don à la FIDO Alliance annoncé au 28 avril 2026 — voir ch. 10), normalisation du passeport, stabilisation OTel, premier incident public d'identité agentique (⚠ relève v0.7 : des candidats du 1ᵉʳ semestre 2026 existent — compromissions de plateformes d'agents, divulgations en conférence de sécurité — à instruire à sources primaires avant de déclarer l'événement survenu), jalons PQC 2030/2035, entrées en vigueur du 1ᵉʳ mai 2027 ; ⚠ **relève v0.10** : la **couche d'exécution** — le harnais — n'a aucun événement dans cette liste, alors qu'elle se révise au rythme d'un produit d'éditeur (versions, politique d'approbation, admission d'extensions), soit une horloge plus rapide que celle des protocoles ; l'y inscrire suppose d'avoir tranché le risque 14) ; protocole de revalidation ; registre de gel par chapitre.
*Fusion : Vol. II ch. 24 + Vol. III *TOC* §28.6. Garde-fous : R-4, R-5 et R-6 du Vol. II et réserve F-29 (balayés ensemble à chaque revalidation). Clôt l'ouvrage par la discipline évidentiaire du Vol. II.*

**Table des matières détaillée du chapitre 57**

*Dérivée du texte rédigé de `Monographie.md` ch. 24 (Vol. II) et §28.6 (Vol. III) le 25 juillet 2026. Table **dérivée**, subordonnée : en cas d'écart, la ligne Fusion ci-dessus prime — elle porte l'arbitrage de provenance, la table n'en est que le dépliage.*

#### § 57.1 — Les lacunes propres au blueprint

*← Vol. II §24.1 ; renvoi ch. 49 (lacune PRD Vol. II §10.6).*

#### § 57.2 — Les événements de péremption

*← Vol. II §24.2 + Vol. III* Monographie *§28.6 :*

- désignation du standard technique par arrêté (ch. 36) ;
- lancement effectif du RTR (ch. 37 — ⚠ **réserve F-29** : ne jamais écrire « lancé » avant) ;
- **révisions de MCP *et* d'A2A** — ⚠ *la couche protocolaire entière du Livre II se périme au rythme de **ses deux** spécifications, non de la seule première* ; ⚠ **relève v0.7** : la ratification MCP annoncée pour le **28 juillet 2026** est le premier de ces événements à porter une date, **neuf jours après la date du fichier** ;
- transfert de gouvernance d'AP2 — ⚠ **relève v0.7 : candidat survenu**, don à la FIDO Alliance annoncé au 28 avril 2026 (ch. 10) ;
- normalisation du passeport (ch. 17) ; stabilisation OTel (ch. 43) ;
- **premier incident public d'identité agentique** — ⚠ **relève v0.7** : des candidats du 1ᵉʳ semestre 2026 existent (compromissions de plateformes d'agents, divulgations en conférence), **à instruire à sources primaires avant de déclarer l'événement survenu** ;
- jalons PQC 2030/2035 (ch. 23 — ⚠ **R-11 : « visés »**, jamais « fixés ») ; entrées en vigueur du 1ᵉʳ mai 2027 (ch. 29, ch. 31).

⚠ **Relève v0.10 — un angle mort de cette liste même** : la **couche d'exécution (le harnais)** n'y a **aucun événement**, alors qu'elle se révise au rythme d'un produit d'éditeur (versions, politique d'approbation, admission d'extensions) — une horloge **plus rapide que celle des protocoles**. L'y inscrire suppose d'avoir tranché le **risque 14**, qui est une décision d'auteur.

#### § 57.3 — Le protocole de revalidation

*← Vol. II §24.3 ; **garde-fous R-4, R-5 et R-6 du Vol. II et réserve F-29 balayés ensemble à chaque revalidation**.*

#### § 57.4 — Le registre de gel par chapitre

convention de datation de l'avant-propos : **gel unique de l'ouvrage + date de gel par chapitre** pour les faits périssables.

⚠ *Clôt l'ouvrage par la **discipline évidentiaire du Vol. II**. Le compendium est daté **et le dit**.*

**Table de couverture (décision 6)**

| Source | Destination | Régime |
| --- | --- | --- |
| Vol. II §24.1-24.3 | § 57.1-57.3 | condensé |
| Vol. III *Monographie* §28.6 | § 57.2 | prélevé au ch. 50 |

---

## Annexes *(~89 000 mots, dont l'ADS Boréalis et la bibliographie consolidée — ventilation à la Volumétrie)*

- **Annexe A — Méthode unifiée** : la fusion des trois systèmes de preuve en un seul — niveaux [A]/[B]/[C] (Vol. II), tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF (Vol. I), vote adversarial multi-juges, attribution des métriques auto-déclarées, distinction lien documenté/inférence. Table de correspondance des trois méthodes d'origine. Porte aussi ce que la v0.2 laissait hors méthode : la convention de qualification cryptographique (R-02 du Vol. III), l'échelle des trois degrés d'absence (R-14), la commande de décompte de référence, la règle d'escalade et les **motifs de balayage** propres à la somme — un critère d'acceptation sans motif qui le contrôle n'est pas vérifiable. **Ajouts de la v0.5, tous hérités du Vol. II et jusque-là non repris** : (a) **le socle des chapitres de synthèse est construit par la rédaction**, avec sa contrepartie obligatoire d'énumération en en-tête, garde-fous à zéro occurrence compris (règle posée à l'avant-propos, applicable aux ch. 46, ch. 47, ch. 51, ch. 55, ch. 56 et ch. 57 et aux annexes de méthode ou de table) ; (b) **une thèse de plan n'est pas une entrée de socle** et le plan s'aligne sur le chapitre, jamais l'inverse (décision 8) ; (c) **une déviation fondée se déclare**, faute de quoi elle est indiscernable d'un oubli ; (d) la **commande de décompte se valide sur son domaine entier** avant d'être publiée comme référence. Les deux dispositifs (a) et (b) sont ceux qui ont permis au Vol. II de détecter ses propres erreurs de marquage et de thèse : ils ne sont pas de la prose de méthode, ce sont les instruments qui rendent le reste vérifiable. *Fusion : Vol. II Annexe A (méthodologie de constitution du socle) + **Vol. III Annexe A** (méthodologie, dont PRD Annexe A §A.6 pour les motifs) + méthode déclarée du Vol. I.*
- **Annexe B — Socle factuel consolidé** : refonte de F-01…F-48 + F-23b (Vol. II) enrichie des faits datés du Vol. I et **du socle propre du Vol. III — F-01…F-98 constituées du 21 au 22 juillet 2026, plus H-01…H-33 héritées — qui a remplacé les « repérages [C] » que les versions antérieures à la v0.13 lui prêtaient**, sous une numérotation unique. *La refonte du socle est la tâche technique centrale du compendium — sans elle, les renvois F-xx des trois volumes ne résolvent pas. Livrable inclus : table de correspondance ancienne numérotation → numérotation unique. ⚠ Le Vol. II n'attribue pas F-12 à F-14 : la renumérotation ne doit pas combler ce trou en décalant les suivants sans table. ⚠ **La renumérotation ne vise que les F-xx.** Le Vol. III pose que ses identifiants ne sont **jamais** renumérotés (PRD §7.1) parce qu'ils vivent en références croisées — les R-xx, CA-xx, L-xx et H-xx des deux volumes sont donc **cités tels quels, préfixés de leur volume** (décision 7), jamais fondus dans une série unique. Les quatorze garde-fous R-01…R-14 du Vol. III, absents de la v0.2, entrent ici au même titre que les R-1…R-8 du Vol. II. ⚠ **Extension v0.13** : la refonte résout aussi la **collision des deux séries F-xx** (Vol. II : F-01…F-48 + F-23b ; Vol. III : F-01…F-98) — deux tables de correspondance, une par volume source — ; et les deux entrées du Vol. III à dette de vote déclarée (F-92 et F-96 du Vol. III, PRD du Vol. III §7.11) n'entrent pas au socle consolidé avant résorption de la dette ou reprise de la parade ⚖ que le Vol. III leur attache.*
- **Annexe C — Faits partagés, divergences tranchées et lacunes ouvertes** *(⚠ **réouverture d'une décision prise**, non résorption d'un fichier pendant : le Vol. III a décidé de **ne pas** créer `commun/faits-partages.md`, ses divergences vivant au PRD §7.5 — décision qu'il autorise expressément le Vol. IV à rouvrir s'il entre en rédaction. C'est ce que fait cette annexe, et il faut l'écrire ainsi)* : source unique des faits datés cités par plusieurs livres, et **résolution des deux divergences héritées** — (1) date de finalisation de la ligne directrice IA de l'AMF : **30 mars 2026** (position du Vol. II, la plus récente) ; (2) gouvernance d'AP2 : **aucun transfert documenté** à date de gel. Toute réouverture exige une source primaire nouvelle datée. ⚠ **Réouverture déclenchée en v0.7** : le don d'AP2 à la FIDO Alliance (annoncé au 28 avril 2026, deux groupes de travail — voir ch. 10) est le fait nouveau candidat ; la divergence ne se re-tranche qu'après extraction de la source primaire, et le socle du Vol. II, gelé, n'est **pas** corrigé rétroactivement — si le fait se confirme, il s'écrit comme un fait **postérieur à l'instruction du Vol. II**, ou antérieur mais non capté par elle, ce qui se dit et ne se lisse pas. ⚠ **Une divergence tranchée n'est pas une lacune comblée** : l'annexe tient un **registre distinct des absences héritées**, avec la règle du Vol. II en toutes lettres — *aucune de ces absences n'établit un fait négatif*. Trois entrées seulement sont des faits négatifs vérifiés par balayage documenté (F-09, F-35, F-46).

  ⚠ **Registre des onze lacunes héritées du PRD Vol. II — repris par identifiant.** Le Vol. II tient dans son propre TOC une table d'assignation de ses lacunes, et en fait son contrôle de couverture. ⚠ **Mais cette table en compte dix, et le PRD — qui fait autorité sur le socle et les lacunes — en compte onze** : la §10.11 (datation du Budget 2025) a été ouverte le 17 juillet 2026 à la construction de l'annexe C, après la rédaction de la table. Le ch. 21 du Vol. II le dit en toutes lettres : « onze lacunes ouvertes à la date de gel ». **C'est le PRD qui est repris ici, pas le TOC** — une v0.5 bâtie sur le seul TOC du Vol. II reproduisait la faute qu'elle reprochait aux versions antérieures. Les v0.1-v0.4 du compendium n'en reprenaient que cinq par leur nom : **§10.7 et §10.10 avaient disparu du fichier**, et §10.2, §10.3 et §10.6 ne survivaient qu'en substance, sans identifiant — donc introuvables et non contrôlables. Une lacune qui perd son identifiant en changeant d'ouvrage est une lacune qui se referme sans preuve, ce que le risque 5 interdit explicitement. Le registre est désormais complet et couvert par un contrôle exécutable :

  | Lacune (PRD Vol. II) | Objet                                                                                                                        | Chapitre(s) porteur(s) dans la somme   |
  | -------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
  | §10.1               | Désignation de l'organisme de normalisation technique (aucun arrêté au 16 juill. 2026)                                    | ch. 34 (instruit), ch. 36 (R-5)        |
  | §10.2               | Institutions sans socle complet — résidus [C] et BNC                                                                       | ch. 39                                 |
  | §10.3               | Frameworks — réduite en P0, ne subsiste que Temporal                                                                       | ch. 27                                 |
  | §10.4               | Réglementaire fin : contenu de la ligne AMF article par article, positions CAI, suites 11-348 —**la plus coûteuse** | ch. 31, ch. 32, ch. 33 ; renvoi ch. 56 |
  | §10.5               | AP2 ↔ rails canadiens                                                                                                       | ch. 40 (prospectif) ; renvoi ch. 56    |
  | §10.6               | Portefeuille IBM — Gartner MQ iPaaS (R-6), FTM/ISO 20022 [C], annonces canadiennes                                          | ch. 49, ch. 57                         |
  | §10.7               | Composante ACP d'AGNTCY —**quatrième branche de R-8 du Vol. II**                                                     | ch. 7 ; renvoi ch. 56                  |
  | §10.8               | Mécanique et attestation des risques protocolaires ; aucune attaque propre à A2A au socle                                  | ch. 11, ch. 20 ; renvoi ch. 56         |
  | §10.9               | Anatomie technique non documentée (A2A, MCP, AP2) — dont §10.9e, gouvernance d'AP2                                        | ch. 8, ch. 10 ; renvoi ch. 56          |
  | §10.10              | Sous-caractérisation du socle académique (F-36, F-37) — OO1-OO4 sur source unique                                         | ch. 25, ch. 26 ; renvoi ch. 56         |
  | §10.11              | Datation du Budget 2025 (F-11) — un fait structurant du cadre bancaire attribué au Budget fédéral 2025 sans être daté  | ch. 36 ; renvoi Annexe D               |

  ⚠ **Le registre est hérité, pas soldé.** Le Vol. II donne l'état de ses lacunes **à son gel (16-17 juillet 2026)** ; certaines étaient déjà « réduites » et non fermées. Aucune ne se déclare close dans la somme sans source primaire nouvelle datée, et le simple fait de figurer dans cette table ne vaut ni instruction ni clôture.

  ⚠ **Les lacunes du Vol. III forment une seconde série, et la somme ne l'a pas inventoriée — constat v0.17.** Le registre ci-dessus est celui du **PRD du Vol. II** ; son cardinal « onze » lui appartient et ne doit pas absorber d'entrées d'un autre volume (même logique que la collision des deux séries F-xx, décision 7). Or le Vol. III, rédigé depuis le 22 juillet 2026, tient au §10 de son propre PRD une série de lacunes numérotées **en clair, sans préfixe** — dont la **lacune 16** que la v0.17 a rencontrée :

  | Lacune (PRD Vol. III) | Objet                                                                                                                                                        | Chapitre(s) porteur(s) dans la somme |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
  | 16                    | **RGPD — non instruite** : « absent du socle et du programme de constitution » ; aucun rapprochement entre régime québécois et régime européen n'est opéré | ch. 34 ; renvoi ch. 56               |

  **Comment elle est arrivée ici.** Le ch. 20 du Vol. III nommait le RGPD dans son titre jusqu'au **22 juillet 2026** ; l'arbitrage **R-G-38** l'a retiré, le socle ne documentant « ni le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation* (degré 3 de l'échelle R-14 du Vol. III), **non** fait négatif vérifié. Les v0.1-v0.16 de ce fichier faisaient hériter au ch. 34 un « volet RGPD » de ce chapitre : la ligne Fusion est corrigée en v0.17, et la lacune entre ici pour que la correction **consigne le trou au lieu de le déplacer**.

  ⚠ **Cette table est incomplète et se déclare telle** : elle porte **une** entrée, celle que la passe a rencontrée, non l'inventaire des lacunes du Vol. III. Cet inventaire est un **préalable déclaré** de la collation de fond contre le Vol. III rédigé (porte G-4 du PRD, risque 11) — le mener ici, sur une seule rencontre, produirait un registre faussement complet, ce que le risque 5 interdit. **Aucun cardinal en toutes lettres n'est annoncé pour cette série tant qu'elle n'est pas inventoriée.**
- **Annexe D — Chronologie fusionnée 2023-2032** : frise unique intégrant la trajectoire protocolaire (F-01…F-05, F-43), réglementaire et d'interopérabilité financière (F-09…F-35), et les jalons PQC — quatre statuts (annoncé / visé / attendu / incertain), **appliqués à chaque entrée sans exception**, y compris aux jalons NIST du ch. 23. *Fusion : Vol. II Annexe C (chronologie réglementaire 2023-2027, 37 événements) + **Vol. III Annexe C** (chronologie 2024-2030), étendues à l'horizon 2032.*
- **Annexe E — Glossaire bilingue unifié** : terminologie français/anglais des trois volumes, avec statut épistémique de chaque terme (norme / marché / construction d'auteur), les quatre branches de **R-8 du Vol. II** (« agentic control plane ») et les six emplois de **R-04 du Vol. III** (« agent mesh »), dont la branche (f) a été ouverte à cause de ce fichier. Fusionne les glossaires des trois sources ; déduplique les entrées. *Fusion : Vol. II Annexe D, dont **§D.1 et §D.7 font autorité** sur R-8 et sur les termes proscrits — cette autorité est reconduite, non réinterprétée — + **Vol. III Annexe D**.*
- **Annexe F — Matrice des mécanismes** : les mécanismes des Livres II-III et les composants de maillage/exploitation (Livre VII) croisés avec la grille des cinq questions, l'état PQC et la couverture d'observabilité — la table de référence de l'ouvrage. *Fusion : **Vol. III Annexe B**, dont cette annexe est le prolongement. ⚠ **Partage à tenir** : le ch. 46 en tire la lecture croisée protocoles × exigences réglementaires ; l'annexe porte la table complète. La v0.2 les revendiquait toutes deux sans arbitrer — une matrice recopiée en deux endroits diverge à la première correction.*
- **Annexe G — Catalogue de patrons de la confiance agentique** : émission, vérification, révocation, chaîne de mandat, points d'application du maillage, boucles d'exploitation, formalisés au gabarit des patrons (contexte, problème, forces, solution, conséquences, patrons liés). *Fusion : **Vol. III Annexe E**. ⚠ **Filiation à ne pas réattribuer** : le Vol. III revendique explicitement la discipline des patrons d'Arsanjani & Bustos — **corpus d'appui**, donc suspendue à la décision P0.2 ; la filiation GoF/EIP du Vol. I est l'héritage de second rang, et devient le seul socle si P0.2 conclut au retrait. La v0.2 avait substitué le second au premier sans le dire.*
- **Annexe H — ADS Boréalis** *(**20 655 mots mesurés**, 19 juill. 2026 — et non les « ≈ 90 000 » que portaient les v0.1-v0.4)* : l'architecture détaillée de solution du Vol. I (Annexe B de sa Monographie), conservée intégralement comme instanciation de référence du blueprint (ch. 49-50) — inventaire produit, matrice de traçabilité, catalogue de diagrammes, configurations illustratives. Nature distincte du corps doctrinal : livrable d'ingénierie *prêt au déploiement*, dont l'insight directeur (plan de contrôle obligatoire + dorsale d'intégration tri-plan non interchangeable) et le revers assumé (*vendor lock-in*, dépendance à un tiers TIC critique, tranché en ADR-001) sont repris tels quels.
  ⚠ **Trois collisions de numérotation, dont deux que la fusion crée elle-même — décision 7 étendue, ajout de la v0.5.** Le Vol. I déclare un « piège de numérotation à ne jamais confondre » à trois branches ; en devenant l'Annexe H d'un ouvrage à 57 chapitres et 9 annexes, ce piège **change de forme et s'aggrave**, et aucune des v0.1-v0.4 ne le traitait. (a) L'ADS porte sa propre numérotation **§0-§17**, qui coexiste désormais avec les §N.x des chapitres de la somme : tout renvoi vers elle s'écrit `Annexe H §N`, jamais `§N` nu. (b) L'ADS porte ses **propres sous-annexes A-F**, dont une « Annexe B » (matrice de traçabilité) qui **entre en collision frontale avec l'Annexe B de la somme** (socle factuel consolidé) — collision nouvelle, absente du Vol. I où l'Annexe B *était* l'ADS : les sous-annexes de l'ADS s'écrivent `Annexe H, sous-annexe B`. (c) Les renvois **internes** de l'ADS vers le corps doctrinal sont explicites et **tous périmés par la fusion** : ils sont de la forme `cf. Monographie ch.6 §6.1.3` et visent le chapitre ArchiMate du Vol. I, devenu le **ch. 48** de la somme — le rebasage de ces renvois est une tâche de fusion à part entière, à mener avec la refonte du socle (Annexe B) et non après. *Conventions propres reconduites : diagrammes **Mermaid inline** légendés, devant passer `mmdc` ; vues en **ArchiMate 4**, équivalent 3.2 noté si requis (ancrage au ch. 48) ; extraits de configuration illustratifs, jamais de secret réel ; valeurs chiffrées (SLO, RPO/RTO, débits) = hypothèses à calibrer.*
- **Annexe I — Bibliographie générale consolidée** *(**plancher mesuré : 37 104 mots pour le seul Vol. I**, 1 270 entrées)* : fusion des bibliographies par chapitre du Vol. I (son Annexe A, plans détaillés et bibliographies), du corpus de sources du Vol. II (PRD §9) et du corpus d'appui du Vol. III ; entrées dédoublonnées et datées, sources primaires distinguées de la littérature secondaire. Une somme qui se substitue à ses sources doit porter leur appareil bibliographique complet. Le Vol. I regroupe ses 1 270 entrées **par chapitre puis par catégorie** (six catégories) et déclare chacune passée en **vérification adverse** — existence, auteurs, année, numéro de norme, de RFC ou de recommandation ; ce régime est reconduit, et une entrée héritée sans vérification adverse tracée y est traitée comme neuve.
  ⚠ **Deux réserves de forme héritées, à conserver telles quelles** (Vol. I, en tête de sa bibliographie) : les renvois « référence → section » ne sont **pas** reportés dans la version consolidée, chaque agent de recherche ayant numéroté selon sa propre vue ; et les accents des noms de mois dans les chaînes de citation sont préservés **verbatim**, même fautifs (« fevrier »), pour ne pas altérer les métadonnées sources. ⚠ **Un écart hérité, signalé et non arbitré** : les bilans de vérification portés en tête des fichiers de bibliographie par chapitre du Vol. I annoncent des totaux **inférieurs** pour ses chapitres 1, 4 et 7 (228, 173 et 140 entrées) à ceux de l'ouvrage consolidé — bilans non reportés après les révisions v3/v4. Le Vol. I constate l'écart sans le corriger ; la somme **en hérite tel quel** et ne le solde pas en recopiant l'un des deux chiffres. Le rapprochement relève d'une passe de vérification propre, à mener avant que le total consolidé de la somme ne soit annoncé où que ce soit.

---

### Corrections apportées en v0.3

Trois audits de couverture, un par volume source, ont collationné chaque ligne « Fusion » contre les documents réels. Ce qu'ils ont trouvé, et ce que cette version en fait :

**Structure.** Le Livre X de la v0.2 ne comptait qu'un chapitre (études de cas) — il est absorbé par le Livre VIII, désormais « Le terrain canadien ». Le Livre III comptait onze chapitres pour un seul thème apparent : sa moitié hostile (attaques, rug-pull, SOC) devient le Livre IV. La somme des enveloppes par livre (326 000 mots en v0.2) dépassait la fourchette annoncée (260 000-320 000) : les deux sont recalculées et concordent.

**Couverture (décision 6).** Vol. I : §5.0 n'était affecté nulle part — il portait le patron directeur « autonomie graduée sous contrôle de finalité » que la thèse d'ensemble revendique ; il alimente l'avant-propos. §4.4 était couvert par une plage sans section d'accueil (ch. 28) ; §2.13.2 et §7.4.2 étaient acheminés sous une glose qui ne les décrivait pas. Vol. II : quatre pièces sur vingt-neuf — avant-propos et annexes A, C, D — n'étaient ni affectées ni coupées ; elles le sont maintenant, à l'avant-propos et aux Annexes A, D et E. La réserve F-06 (feuille de route de séquencement périmée) était tombée à la fusion ; elle revient au ch. 10.

**Gloses inexactes.** Quatre renvois décrivaient une section autrement que ce qu'elle est. Le plus conséquent : §5.14 du Vol. I, *Synthèse du chapitre et transition*, était glosé « commerce/paiements agentiques » et acheminé vers le chapitre prospectif AP2 — il rejoint le ch. 38, et le §5.13 seul va au ch. 40. Également corrigés : §2.13 (dont seule la première sous-section est la grille « quand agentifier »), §3.13 (glosé avec le titre du §7.3) et §1.9.2 (section IAM **pré-agentique**, glosée « appliqués aux agents »).

**Renvoi nommé (décision 7).** Le risque 10 de la v0.2 déclarait la convention « appliquée à ce TOC » ; elle ne l'était que sur un renvoi sur quarante et un. Tous les renvois au Vol. I nomment désormais leur document. La décision est de plus étendue aux **séries d'identifiants** : les trois renvois « Q n du Vol. II » résolvaient contre deux séries homonymes distinctes, et un lecteur ouvrant la mauvaise obtenait trois fois une autre question.

**Double affectation silencieuse.** Sept sections du Vol. I étaient revendiquées par deux chapitres sans partage déclaré (§7.3, §7.4, §2.9, §2.9.6, §2.11.1, §6.10, §6.8) ; chacune porte maintenant son partage explicite. Côté Vol. II, le ch. 22 était affecté deux fois sans mention de scission. Et le ch. 3 annonçait une économie de fusion — poser le socle IAM une seule fois — que les ch. 13 et ch. 42 défaisaient en héritant de §1.9.2 et §1.9.3 : ils y renvoient désormais sans les reprendre.

**Garde-fous mal attachés ou perdus.** R-2 et R-3 étaient cités au ch. 13, qui ne reçoit pas leur matière ; ils vont aux ch. 17 et ch. 16 — ce dernier étant le chapitre déclaré « à plus haut risque de surinterprétation » et jusqu'ici sans aucun garde-fou. Quatre garde-fous du PRD Vol. II sans identifiant R-x n'étaient pas repris : §8.2.5 (statuts pré-normatifs — la spécification CSA est un brouillon de laboratoires et le brouillon SCIM-agents a expiré le 19 avril 2026), §7.5, §8.2.1 et CA-8. Trois chapitres d'arrivée n'avaient ni socle ni garde-fous là où leur source en portait (ch. 49, ch. 53 et ch. 54).

**Faits.** La formulation « cible reportée quatre fois » (RTR) reproduisait une erreur du plan v1.5 du Vol. II que son chapitre publié corrige explicitement : 2019, 2022, 2023 et 2026 sont quatre *cibles successives*. La thèse du ch. 20 (« la majorité des attaques… sont des attaques d'identité ») n'est portée par aucun socle et le Vol. II pose une question ouverte précisément là — elle est signalée comme le premier énoncé à instruire. La lacune la plus coûteuse du Vol. II — seules les *dates* de la ligne directrice AMF sont au socle, jamais son *contenu* — n'était signalée nulle part ; elle l'est aux ch. 31 et ch. 33 et à l'Annexe C.

**Statut épistémique.** L'Annexe C rangeait sous « divergences tranchées » ce que le Vol. II tient pour des lacunes ouvertes. Une divergence arbitrée et une absence de documentation ne sont pas le même objet : l'annexe tient désormais les deux registres, avec la règle du Vol. II en toutes lettres — *aucune de ces absences n'établit un fait négatif*.

**Corpus d'appui — le constat le plus lourd.** La v0.2 écrivait « le compendium hérite de ce corpus et de ses réserves » et bâtissait six chapitres et une annexe dessus. Or les trois ouvrages sont **introuvables au dépôt** et n'y ont jamais figuré (vérification du 18 juillet 2026, lacune L-15 déclarée bloquante, décision P0.2 en attente dont une issue est le retrait de la filiation livresque). Le bloc porte désormais ce statut en tête, la liste des chapitres consommateurs est complétée (ch. 49 et Annexe G manquaient), la réserve « deux ouvrages d'auteurs Google Cloud » — que le Vol. III a relevée comme incohérence en visant nommément ce fichier — est ramenée au seul ouvrage qui la porte, et deux réserves perdues sont rétablies.

**Appareil du Vol. III.** Ses quatorze garde-fous R-01…R-14 avaient purement disparu de la v0.2, qui n'employait que la série R-1…R-8 du Vol. II — au point que les « R-5, R-6, R-7, R-8 » du blueprint et le « R-7 » de l'instrumentation devenaient indécidables dans des chapitres consommant les deux volumes. Quatre de ces garde-fous sont maintenant appliqués là où ils manquaient : R-02 (qualification par ce que la spécification démontre) et R-14 (les trois degrés d'absence) entrent à la méthode ; R-11 corrige les jalons NIST (« visée », et le statut du document) ; R-13 interdit « l'autonomie graduée » nue, le Vol. I portant trois échelles ; R-04 branche (f) impose la désambiguïsation d'« AgentMesh » — branche ouverte, précisément, à cause de ce fichier. L'Annexe B acte de plus que les identifiants R/CA/L/H ne se renumérotent **jamais**, contrairement aux F-xx.

**Sections du Vol. III sans destination.** Sept étaient perdues sans mention de coupe : §9.3 (limite de l'analogie du mandat) va au ch. 18 ; §19.3 au ch. 29 ; la moitié AMF de §19.1 au ch. 31 ; le volet RGPD du ch. 20 au ch. 34 ; §18.2 (méthode d'inventaire) au ch. 24 ; §6.3 (risque de standard de fait) au ch. 16 ; §7.4 (ce qui n'existe toujours pas) au ch. 17. Ses annexes A, C, D et E, jamais citées, sont rattachées aux Annexes A, D, E et G. Deux doubles affectations sont arbitrées : Entra Agent ID (ch. 13 pour l'extension des RFC, ch. 16 pour l'annuaire) et la matrice des mécanismes (ch. 46 pour la lecture croisée, Annexe F pour la table).

**Deux reproches périmés.** La v0.2 faisait de l'arborescence README une précondition à la fusion : le Vol. III a vérifié qu'elle est correcte, le reproche est retiré. Et elle présentait `commun/faits-partages.md` comme « à créer » alors que la décision de ne pas le créer était prise — l'Annexe C la rouvre, ce qui est permis, à condition de le dire.

**Périmètre — trois fronts identifiés puis écartés, délibérément.** L'audit a relevé un angle mort commun aux trois volumes : ils traitent l'agent comme un *interlocuteur* — qui parle à quoi, sous quelle autorité — et rarement comme un *livrable logiciel qui produit des effets*. Trois sujets en découlent, qu'aucun des trois volumes ne porte : la **provenance des composants** dont un agent est fait (serveurs d'outils, poids de modèle, bibliothèques ; nomenclatures logicielles et d'IA, signature d'artefacts) ; la **sémantique d'effet** d'une action d'agent (idempotence, compensation, réconciliation — ce qui advient quand un virement réussit à moitié) ; la **mise en service** d'un artefact au comportement non reproductible (jeux d'essai de référence, barrière d'évaluation, versionnement à quatre horloges). Une version intermédiaire de ce plan en faisait trois chapitres. **Ils sont retirés sur décision d'auteur** : la somme est une refonte de trois volumes, non une thèse nouvelle, et ces trois fronts n'ont aucun socle hérité — les instruire aurait obligé à constituer des sources primaires dans les domaines où la littérature est la plus jeune, tout en alourdissant l'ouvrage de 14 000 mots contre le risque 1. Ils sont consignés ici pour qu'un futur éditeur les retrouve comme un **choix de périmètre**, et non comme une lacune passée inaperçue. *Si ce choix est rouvert, l'ordre d'instruction suggéré — construction d'auteur, à re-vérifier à la réouverture — suit la maturité de la littérature au moment du gel : la provenance des composants d'abord (nomenclatures logicielles et d'IA, signature d'artefacts — le front où normes et outillage ont le plus progressé), la mise en service ensuite, la sémantique d'effet enfin.* Les enrichissements de moindre ampleur issus du même audit sont, eux, conservés à l'intérieur de chapitres existants : le biais d'automatisation et le paradoxe de l'explicabilité au ch. 18, les indicateurs de supervision humaine au ch. 45, la capacité d'inférence et le budget de latence au ch. 28.

---

### Corrections apportées en v0.4

Passe de cohérence interne sur le fichier v0.3, pilotée par contrôle : chaque défaut a d'abord été couvert par un contrôle exécutable qui échoue sur le document fautif, puis corrigé, puis le contrôle a été validé par mutation.

**Garde-fous nus dans des chapitres mixtes — la parade du risque 10 était incomplète.** La v0.3 déclarait la décision 7 « appliquée aux garde-fous des chapitres mixtes » ; quatre chapitres consommant le Vol. III citaient pourtant encore un R-N à un chiffre sans nommer son volume : ch. 16 (« R-3 », dans le chapitre déclaré à plus haut risque de surinterprétation), ch. 34 (« R-5 »), ch. 41 (« R-8 », le cas le plus indécidable — chapitre dont la seule source non-Vol. I est le Vol. III, où un lecteur résout naturellement « R-8 » contre R-08) et ch. 54 (« R-4, R-5, R-6 »). Les quatre sont nommés « du Vol. II » ; au ch. 41, la répartition est explicitée (R-8 du Vol. II pour « control plane », R-04 du Vol. III branche (f) pour « AgentMesh », déjà imposée en tête de livre). Le contrôle 11 de `check-toc.py` couvre désormais la classe entière : tout R-N à un chiffre sans « Vol. II » à portée de phrase, dans un chapitre dont le corps touche le Vol. III, échoue.

**« Refonte pure » qualifiée.** L'en-tête v0.3 affirmait « aucun contenu neuf n'y est introduit » alors que son propre journal consigne quatre enrichissements intra-chapitres issus de l'audit — dont le biais d'automatisation au ch. 18, déclaré « front neuf — aucun des trois volumes ne le porte, sources primaires à établir ». Les deux énoncés ne peuvent être vrais ensemble ; c'est le premier qui cède, et l'en-tête v0.4 porte la qualification.

**Discipline épistémique au titre.** Le ch. 37 s'intitulait « RTR imminent » alors que son propre corps impose « visé au T4 2026 », attribue la cible et rappelle quatre cibles successives ; « imminent » affirmait au titre ce que le chapitre s'interdit d'affirmer au texte. Titre aligné : « RTR visé ».

**Péremption protocolaire complétée.** Les événements de péremption du ch. 54 citaient les révisions de MCP mais pas celles d'A2A, alors que le Livre II repose sur les deux spécifications (A2A v1.0 au ch. 8, fusion d'ACP au ch. 10 — le plus haut risque R-1 du Vol. II). A2A entre dans la liste.

**Périmètre.** Les trois fronts écartés (provenance des composants, sémantique d'effet, mise en service) reçoivent un ordre d'instruction suggéré pour une réouverture éventuelle, marqué construction d'auteur et daté du gel.

**Forme.** Deux défauts : renvoi mal fermé au ch. 43 (« pont vers E-23 ch. 29, ) ») ; virgule manquante à l'Annexe E après « (norme / marché / construction d'auteur) ».

**Non traité, à dessein.** Le dernier commit du dépôt touchant ce fichier s'intitule « TOC v0.4 » alors qu'il livrait la v0.3 — le fichier fait foi ; la présente version est la v0.4 réelle et l'écart est consigné ici plutôt que réécrit dans l'historique Git. La thèse du ch. 20 reste volontairement en forme forte avec son avertissement d'instruction : c'est un dispositif délibéré de la v0.3, non un défaut.

---

### Corrections apportées en v0.5

Passe de **collation contre les trois tables des matières sources** (`Tocs/1 - TOC IDEA.md`, `2 - TOC BPA.md`, `3 - TOC IA.md`). Les audits de la v0.3 collationnaient ce fichier contre les *volumes* ; celui-ci le collationne contre les *plans* de ces volumes, ce qui expose une classe distincte de défauts — les règles de gouvernance que les plans sources ont apprises et que la fusion n'avait pas reprises.

**Volumétrie — deux chiffres publiés étaient faux d'un facteur.** « ADS Boréalis ≈ 90 000 mots » : mesure à **20 655** (`wc -w` sur `Monographie.md`, § Annexe B, 19 juill. 2026), soit un facteur 4,4 ; le TOC du Vol. I déclarait de son côté ≈ 17 500 d'après le décompte en tête d'ADS, du bon ordre de grandeur — c'est la valeur de 90 000 qui n'a aucune source. Et l'enveloppe des **neuf** annexes était fixée à 35 000 mots alors que **la seule bibliographie du Vol. I en fait 37 104** (1 270 entrées) et que l'Annexe I doit porter celles des trois volumes : deux annexes sur neuf dépassaient à elles seules l'enveloppe entière. Ventilation reconstruite (89 000), fourchette re-basée de 300 000-326 000 à **355 000-380 000**, risque 1 aggravé en conséquence. *Les douze livres sont inchangés à 287 000 mots : ce n'est pas une inflation de contenu, c'est un budget d'annexes qui n'avait jamais été confronté à une mesure.*

**Renvoi pendant.** « Vol. III §10.4 » (ch. 53) ne résout pas : le ch. 10 du Vol. III s'arrête à §10.3, qui est précisément la section décrite par la glose (*Question de recherche formulée pour instruction*). Corrigé.

**Couverture perdue — trois trous, tous dans des séries que la somme prétend tenir.** (1) **Q4** de la série d'agenda du Vol. II n'avait aucun chapitre d'accueil, alors que Q2, Q3 et Q5 en avaient un et que le Vol. III déclare explicitement que son ch. 20 la prolonge : elle entre au ch. 31, siège de sa matière. (2) Les lacunes **§10.7 et §10.10** du PRD Vol. II avaient **disparu du fichier**, et §10.2, §10.3 et §10.6 n'y survivaient qu'en substance, sans identifiant — donc introuvables. Le Vol. II fait de la table de ses lacunes son contrôle de couverture ; la somme en tient désormais le registre complet à l'Annexe C, sous contrôle exécutable. (3) La **branche (d) de R-8** (composante ACP d'AGNTCY), que le Vol. II assigne à son ch. 21, tombait avec §10.7 ; elle est rattachée au ch. 53.

**Doctrine incomplète — deux armatures invoquées sans avoir été posées.** (1) L'**invariant** était énoncé à trois termes (découplage, contrat, évolution) alors que le Vol. I en pose un quatrième — l'**exploitation** (*Monographie* §4.12.4, élargi §7.0) —, qu'il qualifie de « legs explicite au Vol. III » et dont le Vol. III fait le fondement de sa Partie VIII ; or le ch. 44 de la somme invoque nommément « le quatrième terme de l'invariant », qui n'existait nulle part en amont. Le terme est posé en tête de fichier et à l'avant-propos, sa filiation tracée au ch. 44. (2) Les **trois capacités** du Vol. III — émettre, appliquer, exploiter — sont ce qui explique la séparation des Livres III, IX et X ; elles n'étaient énoncées nulle part, et le risque de dilution que le Vol. III y attachait n'était pas hérité. Les deux manques sont de la même famille qu'un renvoi pendant : une notion invoquée sans antécédent.

**Règles de gouvernance non héritées — les deux acquis les plus transférables du Vol. II.** (1) *« Une thèse de TOC n'est pas une entrée du socle et ne peut pas en tenir lieu »* — règle que le Vol. II a payée de cinq corrections de thèses de son propre plan, avec ses corollaires (le plan s'aligne sur le chapitre ; une déviation fondée se déclare ; un conflit en-tête/corps non remonté survit dans la pièce publiée). Elle entre en **décision 8**, et vise nommément la thèse du ch. 20 de ce fichier. (2) Le **socle « construit par la rédaction »** des chapitres de synthèse, avec sa contrepartie obligatoire — énumérer en en-tête les entrées mobilisées et les garde-fous balayés, **y compris à zéro occurrence**. C'est ce dispositif qui a permis au Vol. II de contrôler la traçabilité de son ch. 18 et d'y détecter une erreur de marquage de socle. La somme compte six chapitres de synthèse et six annexes de méthode ou de table contre quatre et trois au Vol. II : la règle y est plus nécessaire, pas moins. S'y ajoute la validation de la **commande de décompte sur son domaine entier** — le Vol. II avait publié la sienne après l'avoir testée sur deux fichiers pour vingt-neuf, et il a fallu quatre mesures successives pour arrêter un chiffre.

**Décision 7 étendue au Vol. III, et appliquée.** Le Vol. III vit lui aussi en numérotation multiple — `TOC.md`, PRD, PRDPlan, tous trois porteurs de §N.x — et ce fichier cite les trois. Les **onze** renvois de section au Vol. III portent désormais leur document. *La v0.3 reprochait à la v0.2 d'avoir déclaré cette convention « appliquée » alors qu'un renvoi sur quarante et un la respectait ; la déclarer une troisième fois sans l'appliquer aurait été le même défaut.*

**Ch. 48 — un chapitre de méthode sans ancrage.** Le chapitre ArchiMate ne portait ni version de référence, ni garde-fou, ni ressource vivante, alors que le Vol. I en porte quatre. Ajoutés : le **verrou** (ArchiMate n'a aucun élément natif pour les concepts agentiques ; seule extension défendable, Specialization + stéréotype + Profiles) ; la version **ArchiMate 4, doc C260 du 27 avr. 2026**, équivalents 3.2 en notes ; les ressources vivantes, dont l'état du support outils — à la mi-2026, la quasi-totalité des ateliers n'échange encore que 3.2, ce qui rend le blueprint des ch. 49-50 non échangeable en v4 ; le **registre des stéréotypes** (§6.1.9), dont dépendent les ch. 49-50 et l'Annexe H ; et la **phrase-test de non-redondance** du §6.0.1, plus nécessaire ici — le chapitre en suit quarante-sept, contre cinq au Vol. I.

**Annexe H — trois collisions de numérotation, dont deux créées par la fusion.** Le Vol. I déclare un « piège à ne jamais confondre » à trois branches ; en devenant l'Annexe H, l'ADS le transforme. Sa numérotation propre **§0-§17** coexiste avec les §N.x des chapitres ; sa **sous-annexe B** (matrice de traçabilité) entre en collision frontale avec l'**Annexe B** de la somme (socle consolidé) — collision inexistante au Vol. I, où l'Annexe B *était* l'ADS ; et ses renvois internes explicites (`cf. Monographie ch.6 §6.1.3`) visent tous le chapitre ArchiMate du Vol. I, devenu le **ch. 48** : **ils sont périmés en bloc par la fusion**, et leur rebasage est une tâche à mener avec la refonte du socle, non après.

**Annexe I — l'appareil bibliographique et ses réserves.** Volume établi (1 270 entrées, 37 104 mots pour le seul Vol. I), régime de vérification adverse reconduit, deux réserves de forme héritées conservées verbatim (renvois « référence → section » non reportés ; accents de mois préservés même fautifs), et un **écart hérité signalé et non arbitré** — les bilans par chapitre du Vol. I annoncent 228, 173 et 140 entrées pour ses chapitres 1, 4 et 7, en deçà du consolidé. La somme en hérite tel quel et ne le solde pas en recopiant l'un des deux chiffres.

**Deux risques ajoutés.** Le **risque 11** nomme ce que la fusion masque : cinq livres (III, IV, V, IX, X — 77 000 mots, ~27 % du corps) dérivent d'un volume **non rédigé, sans aucun socle F-xx**, et la somme les présente au même rang que ceux des deux volumes vérifiés. Le **risque 12** reprend le risque de dilution du Vol. III, que la séparation des trois capacités sur six livres aggrave.

**Défauts constatés dans les fichiers sources — signalés, non corrigés ici.** (1) Les TOC des **Vol. I et III** déclarent tous deux la *Synthèse* du Vol. I en numérotation « §3-§12 » ; le relevé des titres de `Synthese Monographie.md` donne **§1-§12** (§1 Introduction … §12 Conclusion). Ce fichier avait raison depuis la v0.3 ; ce sont les deux TOC sources qui restent à corriger, et une note défensive est ajoutée en décision 7 et au risque 10 pour qu'une collation future ne réintroduise pas l'erreur. (2) Le TOC du **Vol. III** titre son corpus d'appui « déposé au dépôt, 18 juillet 2026 » alors que le PRD du même volume établit à la même date qu'aucun des trois ouvrages n'est au dépôt — contradiction déjà portée au bloc « Corpus d'appui » de ce fichier, et que le Vol. III doit corriger (J-1). (3) Le TOC du **Vol. II** porte trois écarts internes entre son tableau de volumétrie et sa prose de commentaire (avant-propos −7 % / −13 % ; annexes +46 % / +41 % ; Partie III +17 % / +16 %) — sans effet sur la somme, qui ne reprend que le total mesuré de 92 059.

**Seconde passe — relecture de cohérence sur l'ensemble du fichier, après application de tout ce qui précède.** Quatre défauts, dont trois préexistants et un introduit par cette même version.

- **Trois en-têtes de livre revendiquaient une Partie qu'un autre livre entame** — défaut de la classe « double affectation silencieuse » que la v0.3 avait traquée au niveau des *sections* du Vol. I sans jamais la vérifier au niveau des **livres**. (a) Le Livre III annonçait « Vol. III Parties I-IV » alors que la Partie IV **est** le Livre IV ; ses chapitres ne couvrent que les Parties I-III. (b) Le Livre VI annonçait « Vol. II Partie II » alors que le ch. 8 de cette partie part au Livre III (ch. 13, ch. 16 et ch. 17) — et l'en-tête du Livre III le revendiquait déjà explicitement. (c) Le Livre XI annonçait « Partie VI + ch. 21-22 » alors que le ch. 21 du Vol. II va au Livre XII et que les chapitres de la Partie VII effectivement repris sont les ch. 22-23. Les trois portent désormais leur mention « hors … ». Le contrôle 16 couvre le cas (a) ; **les cas (b) et (c) restent une collation manuelle, et le script le dit** plutôt que de laisser croire à une couverture complète.
- **Le registre des dix lacunes, ajouté plus haut dans cette même version, était creux** : huit des dix chapitres qu'il désigne comme porteurs ne nommaient pas leur lacune. Un registre qui déclare une couverture qu'aucun chapitre n'assure est pire qu'aucun registre — il donne à la lacune l'apparence d'être suivie. Les ch. 7, ch. 8, ch. 11, ch. 25, ch. 27, ch. 39, ch. 40 et ch. 49 portent maintenant l'identifiant et ce que la lacune recouvre ; le contrôle 15 interdit la régression. *Le contrôle 13, qui vérifiait la complétude de la table, ne pouvait pas voir ce défaut : une table complète peut pointer entièrement à vide.*
- **Le ch. 24 définissait l'invariant à trois termes** (« l'application de l'invariant du Vol. I — découplage, contrat, évolution — à la couche cryptographique ») après que cette version l'eut déclaré à quatre : la parenthèse se lisait comme une définition concurrente. Reformulé en « les **trois premiers termes** de l'invariant », le quatrième étant refermé au Livre X. La crypto-agilité applique bien trois termes sur quatre — la correction porte sur ce que la phrase *définit*, pas sur ce qu'elle affirme.
- **Le cardinal des renvois de série était périmé par cette version même** : le risque 10 déclarait la décision 7 appliquée « aux trois renvois de série », or Q4 vient d'en ajouter un quatrième au ch. 31. Corrigé et daté.

**Non traité, à dessein.** La thèse du ch. 20 reste en forme forte : la décision 8 la vise nommément et impose son instruction par dénombrement avant rédaction, ce qui est la parade — la retirer maintenant reviendrait à trancher sans le corpus. Les trois fronts écartés au périmètre (provenance des composants, sémantique d'effet, mise en service) ne sont pas rouverts.

---

### Corrections apportées en v0.6

Passe de **collation contre les volumes sources complets** — le texte rédigé du Vol. I (`Monographie.md`, 233 257 mots, y compris son Annexe B/ADS) et du Vol. II (29 pièces sous `monographie/`), plus son `PRD.md`. Les v0.3 à v0.5 collationnaient contre des *plans* ; celle-ci confronte au *texte*. Trois lectures adverses indépendantes, chacune chargée de **réfuter** les affirmations de ce fichier, puis vérification directe de chaque écart à la source avant reprise.

**Ce qui tient — et qu'il faut dire avant les écarts.** La charpente est saine, et c'est un résultat, pas une formalité : les **91 sections** du corps du Vol. I sont toutes affectées à un chapitre (13 + 13 + 14 + 12 + 15 + 12 + 12, décompte re-mesuré et concordant avec celui du Vol. I) ; les **24 chapitres** du Vol. II sont tous cités par au moins une ligne « Fusion » ; les **48 entrées F-xx** citées existent toutes au PRD, et aucune entrée du socle n'est laissée sans citation ; les **181 renvois de section** des lignes « Fusion » résolvent tous contre une section réelle. La discipline de couverture posée en décision 6 est donc effectivement tenue au niveau des sections de premier rang.

**Écart grave 1 — une lacune héritée manquait, et la v0.5 avait bâti son registre sur la mauvaise source.** Le PRD du Vol. II liste **onze** lacunes ; sa §10.11 (*Datation du Budget 2025*, F-11) a été ouverte le 17 juillet 2026 à la construction de sa frise chronologique — donc **après** la table de couverture de son TOC, qui n'en tabule que dix. Le ch. 21 du Vol. II le dit en toutes lettres : « onze lacunes ouvertes à la date de gel ». La v0.5 avait construit son registre sur le TOC du Vol. II et reproduisait ainsi, d'un cran, la faute qu'elle reprochait aux v0.1-v0.4. Le registre passe à onze, la §10.11 est portée par le ch. 36 (siège de F-11) avec renvoi à l'Annexe D, et **la règle est posée : sur le socle et les lacunes, c'est le PRD qui fait autorité, jamais le TOC**.

**Écart grave 2 — deux formulations que la source proscrit en toutes lettres.** (a) Le ch. 29 écrivait « la supervision humaine **exigée** » : le PRD Vol. II §7.3 impose « écrire *attendu par E-23*, jamais *exigé par E-23* » — E-23 est une ligne fondée sur des principes, rédigée au conditionnel, et le PRDPlan §4.4 range « l'exigence d'inventaire d'E-23 » parmi les tournures proscrites, au motif que « la nuance décide de ce qu'une institution peut opposer à son régulateur ». De surcroît, les cinq attentes au socle sont cycle de vie, inventaire, cotation, documentation et **surveillance continue** — la « supervision humaine » n'en est pas une. (b) Le ch. 50 écrivait « décision de crédit OO4 **art. 12.1 outillé** » : le ch. 23 du Vol. II établit que l'humain-dans-la-boucle et la révision de l'article 12.1 ne sont pas la même chose, que le flux « n'outille pas la révision de l'article 12.1 » et que « **le blueprint ne doit pas prétendre le contraire** ». Le « OO4 » nu est corrigé du même mouvement : la source pose « OO3 **ou** OO4 » et qualifie le positionnement d'inférence, le socle n'établissant pas la conscience du processus qui les sépare.

**Écart grave 3 — « Vol. II Annexe B » désigne deux documents sans rapport.** La Monographie du Vol. II porte une Annexe B *Matrice détaillée protocoles × réglementation* (§B.1-B.4) ; son PRD porte une Annexe B *Blueprint d'architecture* (§B.1-B.5). Le ch. 46 visait la première, les ch. 49 et ch. 50 la seconde, et **aucun des trois ne le disait** — un « Vol. II Annexe B §B.1-B.2 » nu résout contre « les règles héritées du chapitre 18 » aussi bien que contre « les principes directeurs du blueprint ». Le Vol. II, lui, nomme (« PRD Annexe B.1-B.2 »). La décision 7 est étendue aux **annexes** des volumes sources, appliquée aux quatre renvois concernés — dont un que la v0.5 avait elle-même introduit dans son tableau de ventilation — et mise sous contrôle 17.

**Quatre thèses plus fortes que le chapitre rédigé — décision 8, appliquée à ce fichier.** Chacune est un cas où « la rédaction avait lu le socle mieux que le plan », et le plan du compendium avait recopié le bandeau du plan source plutôt que le chapitre. **Ch. 10** : « AP2 est l'aboutissement financier de la pile ; AGNTCY en est la couche d'infrastructure, non un concurrent » — le ch. 3 du Vol. II qualifie le premier de « **lecture de l'auteur** » et le second de « **positionnement officiel déclaré** du projet, une déclaration et non un fait vérifié, que des analyses tierces nuancent ». **Ch. 7** : « condition de sa crédibilité » — le ch. 1 du Vol. II conclut « condition *nécessaire*, **non une condition *suffisante***  ». **Ch. 5** : la thèse attribuait l'empoisonnement de la mémoire et des sources aux §2.6-2.7 du Vol. I, qui n'en portent **aucune occurrence** (balayage sur les 30 000 caractères de l'intervalle) — la matière vit au §2.10.2, déjà affectée au ch. 20. **Ch. 27** : « CrewAI [B] » écrase trois niveaux de preuve que le ch. 7 du Vol. II impose de tenir séparés — A2A élevé [B] sur source primaire, **MCP au repérage [C]**, métriques auto-déclarées — or c'est le classement [C] de MCP qui fonde le décompte « deux offres sur cinq de première main », lequel fonde à son tour le « répandu et inégalement établi » de la thèse.

**Une perte silencieuse, et une seule.** Le **§2.8.5 du Vol. I** (*Choix et service du modèle comme décision d'ingénierie*) n'avait aucun chapitre d'arrivée ni mention « coupe assumée », alors même que le ch. 6 déclare partager le §2.8 « **explicitement** » en énumérant .1 à .4. Il est affecté au ch. 4. *C'est le seul manquement à la décision 6 trouvé sur les 91 sections — la couverture annoncée était vraie au rang des sections, fausse d'une unité au rang des sous-sections.*

**Écarts de moindre portée, corrigés.** *Ch. 7* : la flèche « MCP → A2A → AGNTCY », présentée comme une chronologie, est fausse dans les deux lectures — par lancement, AGNTCY (mars 2025) précède A2A (avril 2025) ; par passage sous fondation, MCP est le dernier (déc. 2025) et non le premier. *Ch. 49-50* : la scission était attribuée au ch. 22 du Vol. II, qui ne porte aucun flux (§22.1 principes, §22.2 couches C1-C8, §22.3 neutralité) ; le chapitre réellement scindé est le **ch. 23** (§23.1 au ch. 49, §23.2-23.4 au ch. 50). La correction de la v0.3 avait été posée sur le mauvais numéro. *Ch. 50* : « Socle : F-38 à F-46 » excède ce que l'en-tête du ch. 23 déclare (« F-39 à F-42, F-44 à F-46 ») — ni F-38 ni F-43 ; le ch. 49 posait lui-même la règle enfreinte ici (« la plage seule ne les désignant pas »). *Ch. 1* : le §1.6.3 était glosé « orchestration agentique » alors qu'il s'intitule « **Exécution durable, pipelines** et orchestration agentique » — et le ch. 1 revendiquait « exécution durable » dans sa liste de sections tout en envoyant la section entière au ch. 25. *Ch. 34 et ch. 35* : le §5.3 du Vol. I était revendiqué deux fois, l'intervalle « §5.1-5.6 » du ch. 35 recouvrant le §5.3 que le ch. 34 traite ; le ch. 35 porte désormais son « hors §5.3 », et le **§5.1.4 est nommé comme SIÈGE** de la double-qualification, que le §5.3 déclare ne faire qu'instancier. *En-têtes des Livres VI et VIII* : ils revendiquaient « Vol. I ch. 4 » et « Vol. I ch. 5 » en bloc alors que leurs propres lignes « Fusion » en distribuent des sections à quatre autres livres — même classe que les trois en-têtes corrigés en v0.5, mais au rang des **chapitres** du Vol. I et non des Parties, ce que la passe précédente n'avait pas couvert.

**Contrôles.** Le contrôle 13 passe à onze lacunes et porte en commentaire la raison (le TOC du Vol. II en tabule dix, son PRD en liste onze) ; le contrôle 15 vérifie que le ch. 36 porte la §10.11 ; le **contrôle 17** interdit un « Vol. II Annexe B » sans document nommé. Les trois sont validés par mutation, après constat que le script passe sur le document intact.

**Non traité, à dessein.** Le « volet RGPD » que le ch. 34 hérite du ch. 20 du Vol. III reste déclaré tel quel : les trois sections de ce chapitre source sont québécoises et le RGPD n'apparaît qu'à son titre, mais le Vol. III n'étant pas rédigé, l'écart relève de son cadrage et non de la fusion — il est signalé au Vol. III, pas arbitré ici. De même, la section « capacité d'inférence, budget de latence et contention » du ch. 28 n'a aucun appui dans le ch. 4 du Vol. I : c'est un **enrichissement déclaré** de l'audit v0.3, non une glose de section, et il reste à sources primaires à établir — au même titre que le biais d'automatisation du ch. 18.

---

### Actualisation v0.7 — l'état de l'art de juillet 2026

Passe d'un genre distinct des collations v0.3-v0.6 : celles-ci confrontaient ce fichier à ses **sources** (plans, puis textes) ; celle-ci confronte ses **faits vivants** à l'état du monde de juillet 2026, par balayage de sources ouvertes (presse spécialisée, annonces d'éditeurs et de fondations, dépôts de normalisation). **Règle de la passe, opposée à elle-même avant tout autre usage** : un balayage de sources ouvertes n'est pas une instruction au socle — aucun des faits relevés ici n'entre en F-xx, aucun ne re-tranche une divergence, aucun ne clôt une lacune. Chaque relève est marquée « à instruire à la source primaire » et désigne son point d'atterrissage. Sept relèves, deux constats de dépôt.

**1. AP2 — le fait nouveau que l'Annexe C attendait.** Des annonces publiques d'avril-mai 2026 font état du don d'AP2 (v0.2) par Google à la **FIDO Alliance** le 28 avril 2026, avec deux groupes de travail (authentification agentique ; paiements) et une liste de soixante organisations contributrices. Si la source primaire se confirme, trois pièces du plan sont touchées d'un coup : la divergence tranchée « aucun transfert documenté » (Annexe C — réouverture déclenchée, non consommée), la lacune §10.9e du PRD Vol. II (gouvernance d'AP2), et la thèse du ch. 7 (« AP2 n'a aucun transfert de gouvernance documenté » — vraie au socle hérité, périmée si le fait s'instruit). La bifurcation de la gouvernance par couche (ch. 52) en sort renforcée : la branche FIDO cesse d'être une projection. ⚠ Le fait est **antérieur au gel du Vol. II** (28 avril contre 16-17 juillet) : s'il se confirme, l'écart avec le socle du Vol. II se **déclare** (fait non capté par son instruction), il ne se lisse pas — le Vol. II reste gelé et n'est pas corrigé rétroactivement.

**2. MCP 2026-07-28 — la péremption du Livre II a désormais une date.** La RC, gelée le 21 mai 2026 pour ratification annoncée le 28 juillet 2026, porte un cœur **sans état** (suppression de la poignée de main et de l'en-tête de session), un cadre d'extensions (Tasks pour le travail de longue durée, MCP Apps), un durcissement de l'autorisation aligné OAuth/OIDC et une politique de dépréciation à cycle de vie (≥ 12 mois entre dépréciation et retrait). Ce sont des changements **cassants** : l'anatomie du ch. 8 (révision 2025-11-25) et, par ricochet, tout ce que le Livre II dit du transport et de la session sont à revalider en bloc au gel. Le ch. 54 note que c'est le premier événement de péremption à guichet daté.

**3. Filière IETF de l'identité d'agent — l'expiration n'était pas une extinction.** Le ch. 13 portait l'expiration du brouillon SCIM-agents (19 avril 2026) sans dire ce qui suit ; à mi-2026, la filière est active : applicabilité de WIMSE aux agents d'IA (brouillon expirant le 1ᵉʳ septembre 2026), cadre composant WIMSE, SPIFFE et OAuth 2.0 (version du 1ᵉʳ juin 2026), extension SCIM d'éditeur pour le provisionnement d'agents. Tous **pré-normatifs** — le garde-fou §8.2.5 est inchangé ; la relève empêche seulement d'écrire « la voie IETF s'est éteinte », ce que l'expiration seule aurait laissé croire.

**4. IR 8547 — le statut n'a pas bougé, l'opposabilité si.** Le document demeure un brouillon à mi-2026 (R-11 du Vol. III maintenu : « visée », jamais « fixée »), mais des instruments fédéraux américains de juin 2026 — décret exécutif et directive OMB alignant les plans de migration fédéraux sur les jalons 2030/2035 — transforment une feuille de route en échéance opposable pour un périmètre fédéral américain. Enrichissement du ch. 23, sources primaires (décret, directive) à extraire ; la contrainte de conception se durcit, le statut du document ne change pas.

**5. OTel GenAI/MCP — « à dater » est daté.** Le ch. 43 demandait de dater le statut des conventions : à la mi-2026 (semconv 1.40.0, avril 2026), GenAI et MCP restent au statut *Development*, seuls des attributs d'exécution de base étant tenus pour stables ; les conventions GenAI migrent vers un dépôt dédié (ressource vivante). L'événement de péremption « stabilisation OTel » du ch. 54 n'est **pas** survenu.

**6. ArchiMate 4 — l'ampleur de C260 est confirmée, et elle élève le verrou du ch. 48.** La v4 est la refonte de métamodèle la plus profonde du langage : réduction d'environ 30 % du nombre d'éléments (de plus de soixante à une quarantaine), couches remplacées par des **domaines** dont un domaine commun, comportements fusionnés entre domaines, multiplicité sur les relations. Conséquence pour le ch. 48 : la re-vérification du mécanisme Specialization + stéréotype + Profiles **tel que C260 le porte** passe de note de transition à préalable du registre des stéréotypes — un registre bâti sur le mécanisme 3.2 pourrait ne pas se transposer.

**7. Incidents d'identité agentique — des candidats, pas encore un fait.** Le 1ᵉʳ semestre 2026 fournit des divulgations publiques (compromissions de plateformes d'hébergement d'agents, moissonnage d'identifiants d'agents en chaîne d'approvisionnement, divulgations en conférence de sécurité) et des enquêtes d'éditeurs attribuant une majorité d'incidents aux identifiants sur-provisionnés. Double atterrissage : l'événement de péremption « premier incident public d'identité agentique » (ch. 54) a des **candidats survenus**, à instruire à sources primaires avant d'être déclaré ; et la thèse du ch. 20 — que la décision 8 impose de trancher par dénombrement — a désormais un **corpus candidat**, dont chaque pièce est à qualifier (les enquêtes d'éditeurs sont des métriques auto-déclarées, PRD Vol. II §7.5 : attribution à chaque occurrence, jamais en preuve).

**Deux constats de dépôt.** (1) **`check-toc.py` est introuvable au dépôt** (balayage `**/check-toc.py` du 19 juillet 2026, zéro résultat), alors que les journaux v0.3 à v0.6 déclarent des contrôles « validés par mutation », numérotés jusqu'au contrôle 17. La leçon est celle que ce fichier applique déjà aux commandes de décompte : une attestation est du contenu, et un contrôle dont l'exécutable n'est pas versionné n'est pas un contrôle — c'est une spécification. Le champ Contrôles porte le constat ; restaurer ou reconstruire le script, puis le re-valider par mutation, est un préalable à toute publication. **Conséquence assumée : la présente passe n'a pas pu exécuter les contrôles** ; ses modifications ont été relues manuellement contre les décomptes annoncés (aucun cardinal en toutes lettres du fichier n'est modifié par la v0.7). (2) **Les chemins `Tocs/…` du journal v0.5 ne résolvent pas** : les trois TOC sources vivent sous leurs volumes (`1 - Corpus Agentique/…/Chapitres/TOC.md`, `…/2 - OrchestrationAgentique/doc/TOC.md`, `…/3 - EntrepriseAgentique/doc/TOC.md`). Soit le dossier `Tocs/` a existé puis a été supprimé, soit le journal a nommé un chemin de travail local — dans les deux cas, un futur éditeur qui voudrait rejouer la collation v0.5 ne le peut pas depuis le dépôt : l'écart est consigné, le journal v0.5 n'est pas réécrit.

**Non traité, à dessein.** Les trois fronts écartés au périmètre (provenance des composants, sémantique d'effet, mise en service) ne sont pas rouverts — les relèves 2 et 7 (chaîne d'approvisionnement d'agents, politique de dépréciation) frôlent le premier front et le confirment comme le plus mûr des trois si le choix est rouvert un jour, mais elles n'y suffisent pas. Aucun chapitre ni aucune section n'est ajouté : la somme reste une refonte de trois volumes, et les tendances de juillet 2026 y entrent comme actualisations de faits vivants, non comme matière neuve. Le socle du Vol. II n'est arbitré nulle part. Les thèses touchées par les relèves (ch. 7 sur AP2, ch. 20 sur les attaques d'identité) ne sont **pas** réécrites : la décision 8 impose que le chapitre s'aligne sur l'instruction, pas que le plan anticipe sur elle.

---

### Révision v0.8 — validation de cohérence et réouverture du périmètre

Passe menée sur instruction d'auteur du 20 juillet 2026 : analyser les douze livres, en valider la cohérence, et identifier s'il y a lieu les livres supplémentaires qui couvriraient le domaine agentique holistiquement.

**Validation de cohérence — ce qui a été vérifié, et comment.** `check-toc.py` demeurant introuvable (constat v0.7 reconduit), la vérification a été faite par balayage exécutable ad hoc sur le fichier v0.7 : chapitres 1-54 contigus et uniques ; douze livres I-XII ; somme des enveloppes de tête égale à 287 000 mots de corps plus 4 000 d'avant-propos, conforme au total annoncé de 380 000 avec les 89 000 d'annexes ; ventilation des annexes sommant à ≈ 89 000 ; aucune référence « ch. N » hors de l'intervalle 1-54. **Aucun défaut structurel nouveau.** Les défauts connus restent ouverts et ne sont pas soldés ici : script de contrôle à reconstruire, sept relèves v0.7 à instruire à la source primaire, décision P0.2 non tranchée, thèse du ch. 20 à instruire par dénombrement.

**Réouverture du périmètre — la seule lacune de couverture du domaine était déjà consignée.** L'analyse de couverture holistique n'a pas trouvé d'angle mort nouveau : le seul identifié — l'agent traité en interlocuteur, jamais en livrable logiciel — est celui que l'audit v0.3 avait nommé, chiffré (14 000 mots, trois fronts) et écarté sur décision d'auteur, en prévoyant expressément sa réouverture et son ordre d'instruction. L'instruction d'auteur du 20 juillet 2026 la déclenche. Les trois fronts entrent comme **Livre XII — L'agent comme livrable logiciel**, trois chapitres dans l'ordre d'instruction v0.3 : provenance des composants (ch. 52 — le front le plus mûr, que les relèves 2 et 7 de la v0.7 confirment), mise en service (ch. 53), sémantique d'effet (ch. 54). **Aucun autre livre n'est ajouté** : les autres candidats évalués à cette passe — économie et FinOps des agents, facteur humain et conduite du changement, souveraineté et trajectoire macro, éthique et alignement — sont déjà portés par des sections existantes (ch. 45, ch. 49, ch. 55, ch. 6) ; en faire des livres dupliquerait sans socle, contre la décision 2.

**Insertion et renumérotation — bornées à la clôture.** Le livre de clôture (horizon, frontière, péremption) doit rester terminal : le Livre XII s'insère donc avant lui, qui devient le **Livre XIII**, ses trois chapitres passant de 52-54 à **55-57**. C'est la même règle que le dépôt applique à la veille technologique — une insertion de tête se fait juste avant la clôture, et les renvois se corrigent. Renvois normatifs mis à jour : les deux listes de chapitres de synthèse (avant-propos, Annexe A), les lignes « Fusion » et renvois de lacunes des ch. 1, 6, 7, 8, 11, 25, 33, 40, 49 et 50, l'en-tête du Livre XI, le registre de l'Annexe C, l'Annexe H (« 57 chapitres »), la décision 1 (« 1→57 ») et les risques. **Les journaux v0.3-v0.7 et les rangées d'historique du bandeau sont gelés et citent l'ancienne numérotation** ; correspondance : ancien ch. 52 = ch. 55 (horizon), ancien ch. 53 = ch. 56 (frontière), ancien ch. 54 = ch. 57 (péremption). Le « ch. 52 » et suivants d'un journal gelé se lisent donc dans la numérotation de leur passe, jamais dans celle-ci.

**Régime du livre neuf.** Décision 9 (la matière neuve se déclare) et risque 13 (un livre sans aucun socle) posent le régime : lignes « Fusion : aucune », thèses marquées construction d'auteur, rédaction en dernier, socle propre à constituer avant rédaction, issue de retrait prévue. La thèse d'ensemble gagne son quatrième plan (*livrer*) en ajout daté ; Nature, risque 1 (fourchette **369 000-394 000**), risque 6 (quatrième plan) et risque 11 (part du Vol. III re-mesurée à 26 % d'un corps de 301 000) sont amendés en conséquence.

**Vérification après édition.** Le même balayage, rejoué sur le fichier v0.8 : chapitres 1-57 contigus et uniques, treize livres I-XIII, enveloppes de tête sommant à 301 000 de corps plus 4 000 d'avant-propos (total 394 000 avec les annexes), aucun renvoi « ch. N » hors de 1-57, aucune occurrence normative résiduelle de l'ancienne numérotation de clôture.

**Non traité, à dessein.** Aucune relève v0.7 n'est consommée ; le socle du Vol. II n'est arbitré nulle part ; les thèses des ch. 7 et ch. 20 ne sont pas réécrites ; la décision P0.2 reste en attente ; `check-toc.py` reste à reconstruire — préalable à toute publication, avec pour domaine la numérotation 1-57 et treize livres.

---

### Révision v0.9 — condensation à dix livres

Passe menée sur instruction d'auteur du 20 juillet 2026 : « condenser les 13 livres en 10 livres total ».

**Le principe : les chapitres ne bougent pas.** La numérotation continue des chapitres (décision 1) est indépendante des livres : condenser les livres ne renumérote aucun chapitre. Les 57 chapitres, tous les renvois « ch. N », l'avant-propos, les annexes et le registre des lacunes sont strictement inchangés ; seuls changent les numéros de livres, les en-têtes des livres fusionnés et les renvois « Livre N » du texte normatif.

**Les fusions retenues, et pourquoi celles-là.** (1) **Anciens Livres III+IV+V → Livre III** (ch. 12-24, ~50 000 mots = 30 + 10 + 10) : les trois dérivaient des Parties I-V du Vol. III et forment un seul arc — émettre l'identité (ch. 12-19), son versant hostile (ch. 20-22), son horloge post-quantique (ch. 23-24) ; les deux livres de 10 000 mots, les plus courts de la somme, disparaissent. (2) **Anciens Livres IX+X → Livre VII** (ch. 41-45, ~27 000 mots = 15 + 12) : les deux capacités d'aval du Vol. III (appliquer, exploiter — ses Parties VII-VIII) réunies. **Alternative évaluée et écartée** : fusionner plutôt les anciens Livres VII+VIII (réglementaire + terrain, ch. 29-40) aurait produit un livre de 60 000 mots — déséquilibré — sans réduire la dispersion des capacités ; la solution retenue réduit le risque 12 au lieu de l'aggraver. Décalage mécanique des autres : VI→IV, VII→V, VIII→VI, XI→VIII, XII→IX, XIII→X.

**Traçabilité des en-têtes (décision 6).** Les en-têtes des deux livres fusionnés combinent les lignes de provenance de leurs constituants sans perte ; l'emplacement de chaque ancien en-tête porte un marqueur de mouvement (« anciennement Livre N ; provenance intégrée à l'en-tête du livre »). Trois renvois du nouveau Livre III sont passés du niveau livre au niveau chapitre, un renvoi de livre devenant auto-référent après fusion : « la fabrique d'émission (ch. 12-19) » au ch. 23, « les mécanismes d'émission du présent livre (ch. 12-19) » au ch. 24, et les renvois §7.4.x des ch. 14 et 55 re-adressés en « ch. N ».

**Correspondance des livres — les journaux v0.3-v0.8 citent l'ancienne numérotation.** Anciens I et II = I et II • anciens III, IV, V = III • ancien VI = IV • ancien VII = V • ancien VIII = VI • anciens IX, X = VII • ancien XI = VIII • ancien XII = IX • ancien XIII = X. ⚠ Un « Livre IX » de journal gelé désigne donc l'AgentMesh, non le livre de matière neuve ; un « Livre X » gelé désigne l'AgentOps, non la clôture. La double correspondance active est désormais : chapitres 52-57 (journaux ≤ v0.7, correspondance au journal v0.8) et livres (journaux ≤ v0.8, correspondance ci-dessus).

**Amendements induits.** L'armature des trois capacités (tête de fichier, avant-propos) tient désormais en deux livres — III (émettre) et VII (appliquer, exploiter). Risque 12 re-libellé (réduit, non éteint : deux capacités cohabitent dans un même livre) ; risque 11 re-libellé (les cinq anciens livres dérivés du Vol. III deviennent deux, mêmes 77 000 mots, même part de 26 %) ; risques 1, 6 et 13, décision 9 et Nature annotés (Livre XII → IX, Livre XIII → X) ; Annexe F et parcours de lecture des Publics visés re-adressés. Décision 10 pose la règle et la correspondance.

**Vérification.** Balayage exécutable rejoué après édition : chapitres 1-57 contigus et uniques ; dix livres I-X ; enveloppes de tête 40 + 25 + 50 + 30 + 25 + 35 + 27 + 35 + 14 + 20 = 301 000 de corps, plus 4 000 d'avant-propos (394 000 avec les 89 000 d'annexes) ; aucun renvoi « ch. N » hors de 1-57 ; aucune occurrence normative des anciens numéraux de livres hors zones gelées. `check-toc.py` demeure introuvable : la passe le déclare, comme les deux précédentes.

**Non traité, à dessein.** Aucun chapitre fusionné ni coupé — la demande porte sur les livres ; fusionner des chapitres changerait la couverture tracée (décision 6) et exigerait une passe propre. Les relèves v0.7 restent à instruire ; la décision P0.2 reste en attente ; les journaux antérieurs ne sont pas réécrits.

---

### Actualisation v0.10 — la couche d'exécution : le harnais

Passe du genre de la v0.7 — confrontation des **faits vivants** du plan à l'état du monde —, déclenchée par une conférence datée du 21 juillet 2026 et instruite sur pièces écrites. **Règle de la passe, opposée à elle-même avant tout autre usage** : aucune des huit relèves n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune ; chacune est marquée « à instruire à la source primaire » et désigne son point d'atterrissage. Aucun chapitre, aucun livre, aucune enveloppe n'est ajouté.

**Le déclencheur, et pourquoi il n'est pas une source.** « *Every Harness Will Become A Claw* », Sam Bhagwat (fondateur et chef de la direction, Mastra), chaîne *AI Engineer*, mise en ligne le **21 juillet 2026**, 15 min 35 s. ⚠ **Aucune transcription n'était disponible au moment de la passe** : la piste de sous-titres automatiques est déclarée par la plateforme mais retourne vide, et le panneau de transcription n'existe pas encore. **Seul le résumé éditorial de la vidéo a été lu.** Une conférence non transcrite, tenue par un dirigeant d'éditeur sur la catégorie de produit qu'il vend, est un **déclencheur daté** — jamais une source : la traiter autrement serait exactement la faute que la décision 8 et le risque 11 prennent pour objet. Les relèves ci-dessous s'appuient donc sur des **pièces écrites**, toutes qualifiées **[C]** à l'entrée :

- **Écrits du même auteur** : *Anatomy of a harness* (5 juin 2026) et *Announcing Mastra Harness* (18 juin 2026, version d'éditeur `@mastra/core@1.45.0`) — éditeur décrivant son propre produit ; toute métrique y est auto-déclarée et s'attribue à chaque occurrence (PRD Vol. II §7.5).
- **Préimpression adverse** : A. Metere, *Architectural Obsolescence of Unhardened Agentic-AI Runtimes*, arXiv 2605.01740v1, 3 mai 2026 — non révisée par les pairs, et proposant une implémentation concurrente de l'objet qu'elle mesure. Son intérêt est **inverse** de celui de l'éditeur, ce qui ne l'annule pas.
- **Chronologie et incidents d'un runtime largement déployé** : relevés en **sources ouvertes** (encyclopédie collaborative, presse spécialisée) — publication initiale le 24 novembre 2025, deux renommages les 27 et 30 janvier 2026, extraction de données et injection d'invite par une extension tierce relevées par des chercheurs d'un éditeur de sécurité les 28-29 janvier 2026, incident d'action hors mandat en février 2026. **Aucune source primaire n'a été extraite** : au sens de l'échelle héritée de R-14 du Vol. III, on est au troisième degré d'absence — absence de documentation à cette passe —, dont rien ne se conclut.

**1. Le harnais est un objet que la somme ne nomme nulle part.** Le compendium traite la boucle de l'agent (ch. 4), les protocoles qui la relient (Livre II), les cadriciels qui la composent (ch. 27), l'encadrement qui la gouverne (Livre IV), le maillage qui l'applique (ch. 41-42), son exploitation (ch. 43-45) et l'artefact qu'elle livre (Livre IX). Il ne traite nulle part le **harnais** — le programme qui héberge la boucle et porte *en propre* la persistance de session et de fil, les modes d'exécution à modèle et outillage distincts, les sous-agents isolés ou forkés, la chaîne d'approbation d'outils, l'admission d'extensions et la compression de contexte. Ce n'est pas le protocole (un harnais est un client MCP, pas une spécification) ; ce n'est pas le cadriciel du ch. 27 (celui-ci compose des graphes d'exécution, il ne tient pas une session interactive) ; ce n'est pas le maillage (le harnais est **en deçà** de l'arête que le maillage médiatise). **Constat déclaré, non comblé** — voir le risque 14 : ouvrir un chapitre ici créerait un second livre sans socle au moment même où le premier (Livre IX) n'a pas le sien, et l'arbitrage est une décision d'auteur, non une décision de passe.

**2. La chaîne d'approbation d'outils : l'autonomie graduée a une implémentation datée — et un mode qui l'annule.** Les pièces écrites décrivent une résolution des permissions par **chaîne ordonnée à premier appariement gagnant** : refus par outil, auto-approbation globale, politique par outil, octroi de session par outil, octroi de session par catégorie, politique par catégorie, défaut — demander. Les octrois **persistent d'une session à l'autre**. Trois atterrissages. (a) Ch. 25-26 : c'est la première réalisation concrète et datée d'un *frame* opérationnel au sens du paradigme APM — à instruire comme **cas**, jamais comme fondement de la taxonomie OO1-OO4, dont le socle est déjà sous lacune (PRD Vol. II §10.10, source unique). (b) Ch. 18 : un octroi **par catégorie** qui survit à la session est un élargissement de mandat sans acte de délégation correspondant — précisément l'angle mort que le chapitre instruit. (c) Ch. 29 et ch. 45 : un mode d'auto-approbation globale n'est pas un contrôle au sens de la supervision **attendue** par E-23, et le distinguer d'une approbation effective est une condition de validité des indicateurs de supervision du ch. 45 (délai médian de révision, taux de renversement).

**3. Le versionnement à quatre horloges en compte une cinquième.** La thèse du ch. 53 pose quatre horloges — modèle, invites, outils, politique. Les pièces écrites en exhibent une cinquième, autonome des quatre : le **harnais lui-même**, versionné par son éditeur, et dont le changement modifie le comportement observable à modèle, invites, outils et politique constants (jeu de modes, seuils de compression, ordre des règles d'approbation, format d'événements). Si la relève s'instruit, la thèse est **sous-spécifiée, non fausse**. Elle n'est pas réécrite : la décision 8 veut que le chapitre corrige le plan, non l'inverse — et une thèse retouchée par anticipation serait indiscernable d'une thèse instruite.

**4. Divergence entre l'action et son journal — une taxonomie candidate pour le ch. 54.** La préimpression adverse pose que la propriété de sûreté porteuse d'un runtime agentique n'est pas la richesse de la trace mais la **détection de l'écart entre l'action réellement effectuée et son enregistrement d'audit**, et en énumère quatre formes : contournement de garde, falsification du journal, échec silencieux de l'hôte, cible erronée. C'est, dans un autre vocabulaire, la question du ch. 54 (« tracer l'effet, pas seulement l'appel ») et le chaînon manquant du ch. 43 (trace ↔ chaîne de mandat). La taxonomie est reprise comme **candidate** ; ses résultats chiffrés ne le sont pas — une mesure produite par l'auteur de l'implémentation concurrente se qualifie avant de se citer.

**5. L'extension déclarative : un composant que les nomenclatures ne voient pas, et un incident daté candidat.** Les harnais admettent des extensions par simple configuration — fichiers d'instructions réutilisables, serveurs d'outils déclarés en JSON — dont l'installation n'est ni une compilation ni un déploiement : une nomenclature logicielle d'artefact ne les capte pas. Fin janvier 2026, des chercheurs d'un éditeur de sécurité ont relevé une extension tierce d'un runtime largement déployé pratiquant exfiltration de données et injection d'invite à l'insu de l'utilisateur. Trois atterrissages : **ch. 52** (l'extension est un composant, et le front « provenance » gagne une pièce — sans que cela vaille preuve du jugement « front le plus mûr ») ; **ch. 21** (c'est un rug-pull, au grain de l'extension plutôt que du serveur d'outils, et sans mécanisme de révocation relevé) ; **ch. 20** (une classe d'attaque dont le vecteur est le harnais, ni le protocole ni le mécanisme d'identité — elle entre au dénombrement exigé par la décision 8 **contre** la thèse d'absorption, non à son appui ; c'est la seule relève de cette passe qui pèse contre une thèse du plan, et elle se déclare comme telle).

**6. Mémoire observationnelle : une quatrième source de dérive.** Les pièces de l'éditeur décrivent une compression de contexte par modèles auxiliaires — un observateur extrayant des observations structurées (décisions, faits, changements d'état), un réflecteur compressant périodiquement le journal d'observations —, déclenchée à seuil de jetons et à l'inactivité, et présentée comme parade au *pourrissement de contexte* et à la compaction destructrice. Deux atterrissages : **ch. 5** (l'ancrage informationnel cesse d'être une mémoire lue pour devenir un artefact **dérivé et daté**, produit par un autre modèle que l'agent) et **ch. 44** (aux trois sources de dérive que le chapitre énumère — modèle, outil, autonomie — s'en ajoute une quatrième, la mémoire réécrite). ⚠ Dispositif auto-déclaré : **aucune propriété de conservation n'est publiquement établie**, et « préserve l'information plutôt que de résumer » est une affirmation d'éditeur, pas une mesure.

**7. Le régime « claw » : permanence, événement, canal.** Le glissement que le résumé de la conférence annonce — mettre le harnais en boîte, le brancher sur des événements externes, lui donner des canaux pour interpeller l'utilisateur et un battement de cœur — décrit un agent **hors session** : il n'attend plus une invite, il s'exécute sur événement et sollicite l'humain de sa propre initiative, sur les canaux de messagerie de l'organisation. Quatre objets du plan s'en trouvent déplacés : l'arête que le maillage médiatise (**ch. 42**) n'est plus initiée par un humain ; l'horizon de tâche déléguée (**ch. 45**) cesse d'être borné par la session ; la révision du mandat (**ch. 44**) devient continue plutôt qu'événementielle ; et la supervision humaine (**ch. 29**) change de sens quand c'est l'agent qui convoque l'humain — un renversement que la ligne E-23 n'anticipe pas. **Relevé comme forme, jamais comme fait d'adoption** : aucune source primaire n'établit ce régime comme majoritaire, et les chiffres de popularité disponibles sont des indicateurs de dépôt public, non de déploiement en entreprise réglementée.

**8. La « loi de Steinberger » est une thèse de trajectoire.** Le résumé de la conférence énonce, par décalque de la loi de Zawinski, que *tout harnais s'étend jusqu'à devenir un claw*. À supposer qu'elle entre au **ch. 55**, elle y entre en **PROJETÉ**, attribuée nommément à son auteur et datée du 21 juillet 2026 — jamais en PROGRAMMÉ : le tri du ch. 55 existe pour ce cas exact. Sa forme d'origine est une loi d'humour d'ingénierie, ce qui n'en fait pas une prédiction fausse mais interdit de la citer comme une régularité établie. Le **ch. 57** en tire un constat distinct : la couche d'exécution n'a aucun événement de péremption dans sa liste, alors qu'elle se révise plus vite que les protocoles.

**Vérification.** `check-toc.py` demeure introuvable — **quatrième passe consécutive sans exécutable**, et la passe le déclare comme les trois précédentes. Balayage ad hoc rejoué après édition, orienté sur l'invariance puisque la passe n'ajoute aucune structure : chapitres 1-57 contigus et uniques ; dix livres I-X ; enveloppes de tête inchangées (301 000 de corps + 4 000 d'avant-propos ; 394 000 avec les 89 000 d'annexes) ; aucun renvoi « ch. N » hors de 1-57 ; **aucun cardinal en toutes lettres du fichier modifié** ; les onze chapitres annoncés comme marqués au bandeau (ch. 20, 21, 22, 26, 43, 44, 52, 53, 54, 55, 57) portent chacun une marque « relève v0.10 », et le journal porte **huit** relèves numérotées, conformément au bandeau.

**Non traité, à dessein.** Aucun chapitre, aucun livre, aucune annexe n'est ajouté : l'angle mort du harnais est **déclaré au risque 14, non comblé** — la somme porte déjà un livre sans socle (risque 13), et lui en adjoindre un second avant que le premier ait le sien aggraverait le défaut qu'elle déclare. Les thèses touchées (ch. 20, ch. 53) ne sont pas réécrites (décision 8). Aucune relève v0.7 n'est consommée ; la décision P0.2 reste en attente ; le socle du Vol. II n'est arbitré nulle part ; les journaux antérieurs ne sont pas réécrits. **Et la relation entre cette passe et le Livre IX n'est pas tranchée ici** : les relèves 3, 4 et 5 atterrissent toutes trois dans ce livre, ce qui plaide soit pour un quatrième front en son sein, soit pour un chapitre propre — l'arbitrage appartient au risque 14.

---

### Actualisation v0.11 — l'après-agentique : quatre trajectoires relevées sur dépôt de prépublications

Passe du genre des v0.7 et v0.10 — confrontation des **faits vivants** du plan à l'état du monde —, menée sur instruction d'auteur du 23 juillet 2026 : instruire ce qui se dessine **après** l'agentique telle que la somme la traite, sur sources vérifiables exclusivement, dépôt de prépublications arXiv en tête. **Règle de la passe, opposée à elle-même avant tout autre usage** : aucune des six relèves n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune ; chacune est marquée « à instruire à la source primaire » et désigne son point d'atterrissage. Aucun chapitre, aucun livre, aucune enveloppe n'est ajouté.

**Le régime des sources — uniforme, et déclaré une fois pour toutes.** Toutes les pièces de cette passe sont des **préimpressions arXiv non révisées par les pairs**. Leurs métadonnées — identifiant, titre, auteurs, dates de dépôt et de révision — ont été vérifiées le 23 juillet 2026 à l'API d'exportation du dépôt (`export.arxiv.org`), et leurs **résumés** consultés ; **aucun texte intégral n'a été extrait**. Au sens de la méthode héritée (Annexe A), ce sont des repérages **[C]** : une préimpression vérifiée existe et dit ce que son résumé dit — rien de plus n'est établi. Les intérêts connus s'attribuent : le cadre de l'« économie bac à sable » est proposé par des chercheurs d'un laboratoire industriel dont l'employeur édite des agents ; les études empiriques des rails sur chaîne mesurent des écosystèmes auxquels leur communauté d'auteurs participe. Et aucun cadrage — pas plus celui de ce fichier que ceux des préimpressions — n'est élevé au rang de source de fait.

**1. Le web agentique : la généralisation de la pile a un nom de scène et un programme normatif (ch. 9).** Yingxuan Yang et al., *Agentic Web: Weaving the Next Web with AI Agents* (arXiv 2507.21206, 28 juillet 2025) nomme « web agentique » le régime où l'interaction machine-à-machine devient le cas nominal du web, et l'ordonne en trois dimensions — intelligence, interaction, économie. Cameron Pattison, Matthew Boulos et Noam Kolt, *The Agentic Web Requires New Normative Infrastructure* (arXiv 2606.10711, v2, juin 2026) soutiennent que ce régime exige une infrastructure **normative** neuve : l'accès des agents aux plateformes pour le compte d'utilisateurs n'est réglé ni par le droit ni par les mécanismes de gouvernance existants. Atterrissages : ch. 9 (l'étagement de la pile du plan a une trajectoire de généralisation nommée) ; ch. 55, trajectoire des protocoles, en PROJETÉ. La somme traite la pile comme un objet d'entreprise ; ces pièces la traitent comme le successeur du web — l'écart d'échelle est la relève, pas une contradiction.

**2. L'économie machine-à-machine : déjà mesurable, sur d'autres rails que ceux que le plan instruit (ch. 40).** Yuhan Jin, Shuohan Wu, Chong Chen et al., *The Web4 Agent Economy: A Large-Scale Empirical Study of the Landscape, Challenges, and Opportunities* (arXiv 2606.25876, juin 2026) mesurent des millions de transactions machine-à-machine quotidiennes sur des rails de micropaiement natifs du web (x402) et d'enregistrement sur chaîne (ERC-8004), et en établissent la fragilité — identité, autorisation et paiement non interopérables. Deux analyses datées la précisent : vulnérabilités du rail de paiement (Ling et al., arXiv 2605.30998, mai 2026) ; réputation manipulable et comportement Sybil répandu au registre (Xiong et al., arXiv 2606.26028, juin 2026). Nenad Tomasev, Matija Franklin, Joel Z. Leibo et al., *Virtual Agent Economies* (arXiv 2509.10147, septembre 2025) proposent le cadre d'encadrement — l'« économie bac à sable », deux axes (origine émergente ou intentionnelle ; perméabilité), instruments (enchères, économies de mission, infrastructure de confiance). Atterrissage : ch. 40 — le chapitre instruit AP2 ↔ rails canadiens pendant qu'une économie d'agents se constitue sur des rails que ni le plan ni le socle ne couvrent ; renvois ch. 16 (un registre d'identité d'agents sur chaîne existe, et ses défauts sont mesurés) et ch. 19. La relève ne déplace pas la lacune §10.5 du PRD Vol. II : elle établit que le silence du chapitre sur les rails non réglementés serait désormais un choix, non une absence de matière.

**3. L'agent mutable prive la réputation de son ancrage (ch. 19).** Botao Amber Hu, Helena Rong et Max Van Kleek, *Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms* (arXiv 2605.30169, v3, mai 2026) : les architectures d'agents à poids, invites et mémoire mutables n'offrent pas la persistance d'identité que tout mécanisme de réputation présuppose. Atterrissages : ch. 19 (le KYA vérifie à l'admission un objet qui peut cesser d'être l'objet admis) ; renvois ch. 15 (« qui en répond » suppose un *qui* stable) et ch. 21 (la révocation présuppose que l'identité révoquée est celle qui a fauté). La relève pèse dans le même sens que la relève 6 de la v0.10 (la mémoire réécrite) : deuxième pièce en deux passes qui attaque la stabilité de l'objet identifié — sans qu'aucune des deux ne soit instruite.

**4. L'auto-évolution fait de la dérive une fonctionnalité (ch. 44).** Deux relevés de synthèse : Fang et al., *A Comprehensive Survey of Self-Evolving AI Agents* (arXiv 2508.07407, v2, août 2025) — cadre unifié entrées / système d'agent / environnement / optimiseurs ; Gao et al., *A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve* (arXiv 2507.21046, v4, révisée janvier 2026). S'y ajoute Sengupta, *Self-Evolving Agents with Anytime-Valid Certificates* (arXiv 2607.00871, juillet 2026) — l'auto-modification bornée par des certificats à garanties d'erreur auditables. Atterrissages : ch. 44 — la dérive que la boucle veut détecter devient un comportement recherché, et la revalidation après apprentissage cesse d'être un cas limite pour devenir le régime nominal ; renvois ch. 26 (distinction adaptation éphémère / évolution persistante — le point d'ancrage), ch. 53 (un artefact qui se modifie en production n'a plus d'horloge fixe — après la cinquième horloge de la v0.10, c'est la fixité même qui tombe) et ch. 6 (évaluer un objet qui change sous la mesure).

**5. L'assurabilité a une architecture candidate (ch. 55).** Cristian Trout, Sanmi Koyejo et Sasha Romanosky, *Underwriting the Agent Economy: The Blueprint for an AI Insurance Stack* (arXiv 2607.11999, v2, juillet 2026) : huit composantes d'infrastructure pour assurer les risques d'agents à l'échelle, à l'horizon 2030. Atterrissage : ch. 55, section « responsabilité, assurabilité, gouvernance de l'émergence » — première architecture candidate pour une section jusqu'ici sans objet instruit. À l'entrée, en PROJETÉ : l'horizon 2030 est celui des auteurs, pas un jalon.

**6. L'après-agentique se donne des échelles — à tenir en SPÉCULATIF (ch. 55).** Meredith Ringel Morris et al., *Levels of AGI for Operationalizing Progress on the Path to AGI* (arXiv 2311.02462, v5, septembre 2025) croisent performance, généralité et autonomie en niveaux ; Gao et al. (déjà cités, arXiv 2507.21046) assument le « chemin vers la superintelligence artificielle » jusque dans le titre. Atterrissage : ch. 55 — le tri du chapitre existe pour ce cas exact : trajectoire d'infrastructure en PROJETÉ, visée superintelligence en **SPÉCULATIF**, jamais l'inverse ; renvoi ch. 26 — l'autonomie graduée du plan trouve dans ces niveaux un vis-à-vis publié, ce qui n'en fait ni une validation ni une source : le socle de l'autonomie graduée reste sous sa lacune propre (PRD Vol. II §10.10, source unique).

**Vérification.** `check-toc.py` demeure introuvable — **cinquième passe consécutive sans exécutable**, déclarée comme les quatre précédentes. Balayage ad hoc rejoué après édition, orienté sur l'invariance puisque la passe n'ajoute aucune structure : chapitres 1-57 contigus et uniques ; dix livres I-X ; enveloppes de tête inchangées (301 000 de corps + 4 000 d'avant-propos ; 394 000 avec les 89 000 d'annexes) ; aucun renvoi « ch. N » hors de 1-57 ; les cinq chapitres annoncés au bandeau (ch. 9, 19, 40, 44, 55) portent chacun une marque « relève v0.11 » ; le journal porte **six** relèves numérotées, conformément au bandeau ; chaque identifiant arXiv cité dans le fichier a été résolu à l'API du dépôt le 23 juillet 2026.

**Non traité, à dessein.** Aucun chapitre, aucun livre, aucune annexe n'est ajouté — les quatre trajectoires relevées atterrissent dans des chapitres existants, et l'arbitrage d'un traitement propre, s'il devait venir, serait une décision d'auteur comme celui du risque 14. Aucune relève v0.7 ou v0.10 n'est consommée ; la décision P0.2 reste en attente ; le risque 14 n'est pas arbitré ; les thèses touchées ne sont pas réécrites (décision 8) ; les journaux antérieurs ne sont pas réécrits. Le rapprochement entre les rails sur chaîne (relève 2) et l'événement de péremption « transfert de gouvernance d'AP2 » (ch. 57) n'est pas fait ici : établir qu'un rail concurrent périme un chapitre exigerait l'instruction que cette passe s'interdit.

---

### Révision v0.12 — l'exécutable de contrôle reconstruit, le préalable levé

Passe d'appareil menée le 23 juillet 2026, en préparation du PRD du Vol. IV (gouvernance de la rédaction des chapitres). Aucun chapitre, aucun livre, aucune enveloppe, aucune relève : la structure est strictement inchangée, et la passe ne touche que le champ Contrôles, la Filiation et le risque 8.

**1. `check-toc.py` reconstruit — cinq passes sans exécutable prennent fin.** Le script est versionné dans ce dossier, aux côtés de `TOC.md`. Domaine conforme au protocole du `CLAUDE.md` (chapitres 1-57, dix livres I-X) ; quatorze contrôles : contiguïté et unicité des chapitres (C1) ; dix livres I-X dans l'ordre (C2) ; enveloppes de tête — somme 305 (301 corps + 4 avant-propos), forme `~N 000 mots` réservée aux en-têtes, fourchette 369 000–394 000 présente (C3) ; aucun renvoi « ch. N » hors de 1-57 (C4) ; aucun numéral de livre hors I-X en zone normative sans marqueur de correspondance (C5) ; aucun « Vol. III § » nu (C6, décision 7) ; aucun « Vol. II Annexe B » sans document nommé (C7 ≈ contrôle 17 historique) ; aucun R-N à un chiffre sans « Vol. II » à portée de phrase dans un chapitre consommant le Vol. III (C8 ≈ contrôle 11 historique) ; registre des onze lacunes complet et effectivement porté par les chapitres désignés (C9) ; mention « corpus d'appui » chez les six chapitres consommateurs et à l'Annexe G (C10) ; marques et décomptes des relèves v0.10 et v0.11 (C11) ; cardinal des renvois nommés au Vol. III (C12) ; « 57 chapitres » cohérent en zone normative (C13) ; alignement du conspectus (C14). **Zones gelées exemptées des contrôles de motifs** : rangées Historique du bandeau et journaux, qui citent formes fautives et anciennes numérotations à dessein ; les spans « … » et `…` sont retirés avant contrôle, la décision 7 citant ses exemples entre guillemets et ses formes de référence en apostrophes inverses.

**2. Validation par mutation — et ce qu'elle a attrapé.** Constat préalable : le script passe sur le document intact. Puis dix-sept mutations, une par classe de faute, chacune devant faire échouer le contrôle qui la vise : toutes détectées au bilan final. **Trois avaient échappé à la première version du script**, durcie en conséquence avant publication : une plage « Livres V-XII » dont seul le premier numéral était lu ; une occurrence à moins de quarante caractères d'un début de ligne, invisible à un ancrage de contexte qui ne franchit pas la ligne ; et le mot « retard » de la rangée Régénération du conspectus, qui neutralisait le contrôle d'alignement — le marqueur exigé est désormais « retard déclaré » en toutes lettres. La leçon du `CLAUDE.md` racine se confirme sur pièce : sans les mutations, un script qui passe sur l'intact reste aveugle sur des classes entières de fautes sans que rien ne le signale. Le harnais de mutation est versionné (`check-toc-mutations.py`) pour que la validation soit rejouable depuis le dépôt — leçon des chemins `Tocs/…` du journal v0.5, qu'un futur éditeur ne pouvait pas rejouer.

**3. Reconstruction, non restauration.** L'exécutable des passes v0.3-v0.6 (contrôles numérotés jusqu'à 17) demeure perdu ; le script reconstruit suit la spécification du champ Contrôles et les balayages ad hoc des journaux v0.8-v0.11. Les journaux gelés qui citent « contrôle N » ne sont pas réécrits et se lisent dans leur numérotation d'origine ; les deux correspondances établies avec certitude sont consignées en commentaire du script.

**4. Fait de dépôt corrigé — le README racine annonce la somme.** Re-vérification du 23 juillet 2026 : le README racine porte la somme dès son titre (« un triptyque, sa veille et sa somme »), à sa table des livrables (colonne Vol. IV) et dans une section dédiée, à l'état v0.11 de ce fichier. La Filiation — qui portait « état du 18 juill. 2026 : le README ne mentionne pas encore le compendium » — et le risque 8 — qui rangeait cette réécriture dans son « reste vrai et non résolu » — sont amendés. Le reproche retiré rejoint les deux reproches périmés déjà consignés à ce risque, par la même mécanique : un fait de dépôt vérifié à une date se re-vérifie avant d'être reconduit.

**5. Cardinal re-mesuré.** Les renvois nommés « Vol. III *TOC* §N.x » comptent onze occurrences en zone normative (mesure du 23 juillet 2026, au sens du préfixe nommé — c'est la règle de décompte du contrôle C12, désormais explicite) : le « onze » de la décision 7 reste exact, et il est sous contrôle exécutable.

**Vérification.** `python check-toc.py` exécuté après édition : C1-C14 passent, sortie 0. Première passe depuis la v0.6 à se déclarer contrôlée par un exécutable versionné.

**Non traité, à dessein.** Aucune relève v0.7, v0.10 ou v0.11 n'est consommée ; la décision P0.2 reste en attente ; le risque 14 n'est pas arbitré ; les thèses des ch. 20 et ch. 53 ne sont pas réécrites (décision 8) ; les journaux antérieurs ne sont pas réécrits. La gouvernance de la rédaction — gel unique, commande de décompte, seuil de vote adversarial, règle d'escalade, motifs de balayage, ordre de rédaction — relève du PRD du Vol. IV, pièce distincte à venir : un plan de contenu et une pièce de gouvernance ne se confondent pas (périmètre des fichiers de doc, `CLAUDE.md` racine).

---

### Révision v0.13 — collation d'état contre le Vol. III rédigé : la filiation change de régime

Passe de faits de dépôt, du genre de la v0.12 — constats pris sur pièces du dépôt et vérifiés à leur siège, non relèves externes. Déclencheur : la préparation du PRD du Vol. IV a confronté la Filiation de ce fichier à l'état réel du dossier `3 - EntrepriseAgentique`, et l'écart est massif — le bandeau décrivait un Vol. III que trois jours de son exécution ont périmé. Constats pris le 23 juillet 2026 dans les en-têtes du PRD v1.3 (champs Version, Statut, Corpus), du TOC v0.8 et du `CLAUDE.md` du volume, chacun ouvert et lu ; les cardinaux cités (34 pièces, 98 entrées, 15 lots, 160 427 mots) sont ceux que ces pièces portent, recoupés entre elles, jamais recopiés d'un seul site.

**1. Le Vol. III est rédigé — la Filiation et le risque 11 étaient périmés.** PRD v1.3 (22 juillet 2026), champ Statut : « les 34 pièces sont rédigées, relues adversarialement et corrigées » ; socle propre de **98 entrées F-01…F-98** à quatre sièges datés (§7.8-§7.11) plus 33 héritées H-01…H-33 ; **15 lots d'instruction clos sur 15** ; gel des pièces au 21 juillet 2026 ; volumétrie réelle **160 427 mots** (commande PRDPlan §1.5, registre de gel du volume) ; rendu FESP de 428 p. le 23 juillet 2026 (P5.4, troisième copie du pipeline — consignée au `CLAUDE.md` racine). ⚠ Le même cadrage impose « **rédigé ne vaut pas publiable** » : quinze remontées ouvertes (R-G-43…R-G-57), douze arbitrages délégués révocables, dette de vote sur F-92 et F-96 du Vol. III, rejeu exhaustif des motifs de balayage dû. La Filiation et le risque 11 sont réécrits — le corollaire de calendrier du risque 11 **s'inverse** : le socle des Livres III et VII est désormais à refondre comme les autres, non à constituer.

**2. P0.2 est tranchée depuis le 21 juillet 2026 — filiation livresque retirée.** Le PRD du Vol. III (historique v0.2 ; champ Corpus : « 3 ouvrages annoncés, 0 déposé, filiation retirée le 21 juillet 2026 ») consigne la décision : L-15 close **par échec documenté** — un résultat, non une lacune non instruite —, les sept sections et l'annexe E réaffectées au socle du volume, décision **réversible** par dépôt ultérieur. ⚠ **Écart de la v0.12, consigné ici conformément au protocole** : son journal et son bandeau, publiés quelques heures avant cette passe, reconduisaient encore « la décision P0.2 reste en attente » — reconduction d'un état périmé depuis deux jours, faute de re-vérification au dossier du Vol. III ; le journal v0.12 ne se réécrit pas, et la présente passe est née de ce constat. Le bloc Corpus d'appui (titre et paragraphe de tête), le risque 9 (re-libellé : tranché en amont, réversible) et les deux « sous réserve de la décision P0.2 » (ch. 47, ch. 49) sont amendés. Les mentions « corpus d'appui » des six chapitres consommateurs et de l'Annexe G sont **conservées comme marqueurs conditionnels** de réouverture — le contrôle C10 continue de les exiger — et une vigilance neuve est posée : le Vol. III a comblé ces emplacements par construction d'auteur sous CA-07, et la fusion reprendra ces passages avec leur marquage, jamais comme des faits de corpus.

**3. Collision neuve des séries F-xx — la décision 7 s'étend une troisième fois.** Le Vol. III ayant constitué F-01…F-98, un « F-36 » nu est devenu indécidable entre deux socles — exactement comme l'était un « R-7 » nu (v0.4) ou un « Vol. III §7.4 » nu (v0.5). Convention transitoire posée en décision 7 : les « F-xx » nus des lignes Socle de ce fichier désignent la série du **Vol. II**, seule existante à leur rédaction ; toute citation du socle du Vol. III s'écrit « F-xx du Vol. III ». Le règlement définitif appartient à la refonte de l'Annexe B, dont le périmètre s'élargit (deux tables de correspondance, une par volume source) et dont l'entrée exclut, jusqu'à résorption, les deux entrées à dette de vote du Vol. III (F-92, F-96 — parade ⚖ du Vol. III sinon).

**4. Volumétrie — le chiffre planifié cède au chiffre mesuré.** « Vol. III ≈ 102 500 mots (planifié, non écrit) » est remplacé par la mesure : **160 427 mots** (22 juillet 2026, commande de référence du volume, 34 pièces, registre de gel). Conséquence déclarée à la Volumétrie : les enveloppes des Livres III et VII (77 000 mots à elles deux) avaient été calibrées sur le chiffre planifié ; contre la mesure, le même périmètre suppose une condensation d'environ 52 % au lieu d'environ 25 %. Fourchette et enveloppes strictement inchangées — le re-calibrage éventuel est une décision d'auteur, remise au gel unique (risque 1 inchangé dans sa lettre, aggravé dans son arithmétique).

**5. Ce que cette passe ne fait pas — et que le PRD devra ordonnancer.** La **collation de fond** contre le texte rédigé du Vol. III — l'homologue, pour lui, de ce que la v0.6 a fait pour les Vol. I et II : confronter chaque ligne « Fusion », chaque glose et chaque thèse au texte final des 34 pièces — **n'est pas menée ici** ; elle est déclarée **préalable à la rédaction des Livres III et VII** et remise au PRD du Vol. IV. De même : l'intégration des 22 lacunes documentées du Vol. III (PRD du Vol. III §10) au registre de l'Annexe C — qui ne porte à ce jour que les onze du Vol. II — est **à instruire, non exécutée d'office** ; et l'état des quinze remontées ouvertes se revérifie au gel unique, pas à chaque passe de ce fichier.

**Vérification.** `check-toc.py` exécuté avant édition (C1-C14, sortie 0) et après (idem) ; harnais de mutation rejoué après le réancrage de son motif M14 (le conspectus passe à v0.13) — dix-sept mutations, toutes détectées. Aucun cardinal contrôlé ne bouge : 57 chapitres contigus et uniques, dix livres I-X, enveloppes 305 + 89, onze renvois nommés « Vol. III *TOC* §N.x » (C12).

**Non traité, à dessein.** Aucune relève v0.7, v0.10 ou v0.11 n'est consommée ; le risque 14 n'est pas arbitré ; les thèses ne sont pas réécrites (décision 8) ; les journaux antérieurs — y compris leurs mentions « P0.2 non tranchée » et « proposition v0.4 », vraies à leur date — ne sont pas réécrits ; le socle du Vol. II n'est arbitré nulle part ; enveloppes et fourchette sont intactes. Le `CLAUDE.md` racine, qui étiquette encore le Vol. III « cadrage » dans sa table d'autorité, est hors de la charge éditoriale de ce dossier : **signalé, non corrigé**. Le README racine, lui, est déjà à jour (section Vol. III à l'état PRD v1.3 / TOC v0.8, constat du 23 juillet 2026).

---

### Révision v0.14 — collation d'appui structurelle contre les trois monographies rédigées

**Genre.** Passe de collation, de la famille de la v0.6 (confrontation au texte rédigé), mais bornée à son **volet structurel** — couverture et résolution des renvois. Elle **n'est pas** la collation de fond que le PRD réserve en porte G-4 : aucune glose, aucune thèse n'a été confrontée adversarialement au texte. Ce que cette passe établit, c'est que la *carte* du plan tient contre le texte rédigé des trois sources ; ce qu'elle laisse à G-4, c'est que chaque *lecture* que le plan fait de ces sections est fidèle.

**Méthode.** Extraction des en-têtes (`# Chapitre`, `## N.M`, `# Partie`) des trois `Monographie.md` rédigées, puis confrontation, chapitre par chapitre et renvoi par renvoi, de chaque ligne « Fusion » du présent fichier à cette structure. Le Vol. III est collationné **pour la première fois contre sa monographie** (160 427 mots, 28 chapitres, gel du 21 juillet 2026) et non plus contre son plan : les passes antérieures — dont la v0.13 — ne portaient que sur des faits de dépôt.

**Bilan — sain, aucun défaut structurel relevé.**

**1. Couverture complète, aucun abandon silencieux.** Les 7 chapitres du Vol. I (plus Conclusion et ADS en Annexe B), les 24 chapitres du Vol. II (7 parties, annexes A-D) et les 28 chapitres du Vol. III (9 parties, annexes A-E) sont tous affectés à un chapitre d'arrivée. Le mappage du Vol. III, nouvellement vérifié contre son texte rédigé : Partie I (ch. 1 à 4) → ch. 12 à 15 ; Partie II (ch. 5 à 8) → ch. 16 et 17 ; Partie III (ch. 9 à 11) → ch. 18 et 19 ; Partie IV (ch. 12 à 15) → ch. 20 à 22 ; Partie V (ch. 16 à 18) → ch. 23 et 24 ; Partie VI (ch. 19 à 21, le droit) → ch. 29, ch. 31, ch. 34 ; Partie VII (ch. 22 et 23) → ch. 41 et 42 ; Partie VIII (ch. 24 à 26) → ch. 43 à 45 ; Partie IX (ch. 27 et 28, le blueprint) → ch. 47 à 50, ch. 56 et ch. 57.

**2. Les onze renvois de section au Vol. III résolvent contre le texte rédigé.** Chacun des onze renvois nommés `Vol. III *TOC* §N.x` (cardinal du contrôle C12) désigne, dans la monographie rédigée du Vol. III, une section de **même numéro et de titre concordant** : §6.3 « Le risque de standard de fait » (ch. 16) ; §7.4 « Ce qui n'existe toujours pas » (ch. 17) ; §9.3 « Ce que le droit civil du mandat éclaire — et où l'analogie casse » (ch. 18) ; §18.2 « Méthode d'inventaire pour une institution » (ch. 24) ; §19.3 « Ce que les cadres n'exigent pas » (ch. 29) ; §19.1 « Relecture ciblée d'E-23 et de la ligne directrice AMF » et §20.2 « Le mandat agentique en droit civil québécois » (ch. 31) ; §27.2 « Formalisation : fonctions d'identité, points d'application, boucle d'exploitation » (ch. 48) ; §10.3 « Question de recherche formulée pour instruction » et §28.6 « Événements de péremption et protocole de revalidation » (ch. 56 et ch. 57). Les renvois nommés « Vol. III ch. N §N.x » des ch. 47, 49 et 50 (§27.1/§27.4, §27.3/§27.5, §28.x) résolvent de même. **Constat de régime** : le label « *TOC* » de ces onze renvois n'est **pas** re-libellé en « *Monographie* » — ce serait anticiper la porte G-4 et toucher un cardinal contrôlé (C12) ; il demeure le marqueur honnête que la collation de fond est due.

**3. Vol. I et Vol. II — reconfirmés.** Les renvois de section §N.M au Vol. I (dont §1.6.3, §3.6.x, §4.8/§4.9/§4.12, §5.12.1-3, §6.1.9/§6.8/§6.10, §7.4.x, §2.11.x) et au Vol. II (dont §8.1 à §8.4, §16.3, §19.3, §21.2, §23.1 à §23.4) résolvent contre leur texte rédigé — reconduction du bilan sain de la v0.6, ces deux textes étant inchangés depuis leurs gels.

**Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes de tête et fourchette ≈ 369 000–394 000 mots identiques ; aucun cardinal contrôlé ne bouge (57 chapitres, dix livres, 305 + 89, onze renvois nommés au Vol. III).

**Contrôles.** `check-toc.py` (C1-C14, sortie 0) constaté sur le document intact avant édition, puis après ; `check-toc-mutations.py` rejoué après réancrage du motif M14 sur la version courante du conspectus (v0.14) — dix-sept mutations, toutes détectées, après passage constaté sur le document intact.

---

### Révision v0.15 — la coordination sous défaillance : un audit externe consommé, un angle mort déclaré

**Genre.** Passe de déclaration, de la famille de la v0.10 (le harnais) : elle **n'ajoute ni chapitre, ni livre, ni enveloppe**, et ne re-tranche rien. Elle consomme un audit de couverture externe daté du 24 juillet 2026 — `audit.md`, à la racine du dossier, un rapport sans autorité au sens du `CLAUDE.md` du dossier : ni source, ni décision, ni socle.

**Méthode.** Chaque constat de l'audit confronté au fichier, jamais à son résumé : mesure par motif sur la **zone des chapitres**, de `### Chapitre 1` à `# Annexes` (`consensus`, `byzantin`, `quorum`, `BFT`, `split-brain`, `saga`, `partition`, `idempot`, insensible à la casse) — la zone, et non le fichier : une mesure d'absence menée sur un fichier qui *déclare* l'absence se détruit elle-même dès la passe suivante ; et vérification des renvois de chapitre, des numéros de risque et des portes cités.

**Bilan — un constat retenu sur quatre, trois défauts renvoyés au rapport.**

**1. Constat retenu : l'accord sous défaillance.** Zéro occurrence, en zone des chapitres, de « consensus », « byzantin », « quorum », « BFT » et « split-brain ». « Sagas » y figure une fois — ch. 54, « compensation et sagas au grain de l'agent » —, c'est-à-dire au grain d'une **action unique**, non de l'accord entre pairs. Le plan couvre la communication (Livre II, ch. 41-42), la sûreté du collectif (ch. 6), les modes d'échec protocolaires (ch. 11) et l'effet à moitié réussi (ch. 54) ; il ne couvre pas ce que deux agents de deux institutions tiennent pour vrai sous partition, division du plan de contrôle ou pair vivant qui répond faux. Déclaré au **risque 15**, arbitrage remonté à l'auteur (**D-7** du PRD) — même régime que le risque 14, économie différente : la matière est ici primaire et stable, l'objection est le périmètre et la volumétrie, non le socle.

**2. Constat déjà porté : le harnais d'exécution.** L'audit le relève comme angle mort — c'est le risque 14 depuis la v0.10, avec sa porte (G-5) et sa décision d'auteur (D-2). Rien à ajouter.

**3. Constat déjà porté : le Livre IX sans socle, et le Vol. III « rédigé non publiable ».** Risques 13 et 11, portes G-6 et G-4, décisions D-3. Rien à ajouter.

**4. Constat écarté : la profondeur des cadres européens et américains.** Le déséquilibre relevé par l'audit (DORA, NIS2, SEC/FINRA/OCC traités à plus haut niveau que le cadre canadien, ch. 34) est un **choix de périmètre déclaré au titre même de l'ouvrage** — *services financiers réglementés*, terrain canadien — et non une lacune. Aucune modification.

**Défauts renvoyés au rapport, corrigés chez lui.** (i) Ses ancrages de ligne vers ce fichier étaient périmés — sur six ancrages, un seul (ch. 6) résolvait vers le chapitre annoncé, un deuxième tombait dans le premier des deux chapitres qu'il annonçait (ch. 20 pour « ch. 20-21 », le même ancrage servant ailleurs à désigner le ch. 34), et les quatre autres tombaient dans des chapitres sans rapport (ch. 14, 19, 22, 26) ; ils sont remplacés par des renvois nommés, une ligne de fichier n'étant pas un point d'ancrage stable pour un document qui change de version à chaque passe. (ii) Il attribuait la péremption des protocoles au « risque 5 » ; le risque 5 porte sur les divergences rouvertes par inadvertance, la péremption étant le risque 3 (trois horloges) et une rangée du §13 du PRD. (iii) Sa recommandation d'étendre l'idempotence aux sagas distribuées est **déjà au plan** (ch. 54) ; seule son extension à l'accord entre agents est neuve.

**Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes de tête et fourchette ≈ 369 000–394 000 mots intactes ; aucun renvoi déplacé.

**Contrôles.** `check-toc.py` (C1-C14, sortie 0) constaté sur le document intact avant édition, puis après. Script non modifié par cette passe — le harnais de mutation n'avait donc pas à être rejoué.

---

### Révision v0.16 — les tables des matières détaillées : le plan déplié chapitre par chapitre

**Genre.** Passe d'**expansion**, d'un genre neuf dans ce fichier : ni collation (v0.6, v0.13, v0.14), ni relève de faits vivants (v0.7, v0.10, v0.11), ni déclaration d'angle mort (v0.10, v0.15), ni appareil (v0.12). Elle ne re-tranche rien et n'ajoute aucune matière : elle **déplie** ce que les lignes Fusion décidaient déjà, au grain de la sous-section.

**Origine.** Le travail a été mené du 25 juillet 2026 dans un fichier séparé (`TOCAll.md`), copie de travail de ce document, puis **renommé sur lui** sur instruction d'auteur. Les quatre commits de sa constitution restent à l'historique ; le fichier de travail n'existe plus.

**Objet.** Sous chaque entrée de chapitre, une **table des matières détaillée** portant : les sections et sous-sections du chapitre à écrire, la **provenance de chacune** (`← Vol. N` *document* `§N.M`), les garde-fous et réserves à l'endroit exact où ils s'appliquent, et une **table de couverture** par chapitre (décision 6). **Les 57 chapitres en sont pourvus.**

**Sources.** Le **texte rédigé**, jamais les plans : Vol. I *Monographie* ch. 1-7 et Annexe B ; Vol. II *Monographie* ch. 1-24 et Annexe B ; Vol. III *Monographie* ch. 1-28 et Annexe B. C'est la première passe à consommer le Vol. III **rédigé** au grain de la section — les précédentes travaillaient contre son `TOC.md`.

**Subordination des tables — règle posée par cette passe.** Une table détaillée est **dérivée** : elle déplie une ligne Fusion, elle ne la re-décide pas. En cas d'écart, **la ligne Fusion prime**. Corollaire de la décision 8 : quand le chapitre sera rédigé, c'est **lui** qui corrigera la table, et non l'inverse.

**Le Livre IX ne porte aucune provenance, et c'est un fait.** Les ch. 52-54 sont de la matière neuve (« Fusion : aucune », décision 9) : aucun renvoi `←` n'y est possible, les appuis y sont **internes** (chapitres de la somme) et tout énoncé y est au mieux un repérage [C]. Leurs tables le déclarent en tête plutôt que de simuler une filiation ; la décision 6 y est sans objet, la décision 8 s'y applique doublement.

**Trois défauts introduits par la passe, détectés par le contrôle, corrigés.** Ils valent d'être consignés, parce qu'aucun n'était visible à la relecture. (i) et (ii) **Deux « R-5 » nus au ch. 36** : le chapitre ne consommait que le Vol. II, et son garde-fou nu était donc décidable ; la table détaillée y a introduit une mention de l'**échelle R-14 du Vol. III**, ce qui en a fait un **chapitre mixte** et a rendu le « R-5 » préexistant indécidable (C8). Le défaut n'est pas dans la ligne ancienne mais dans son **voisinage neuf** — les deux occurrences portent désormais « du Vol. II ». (iii) **Un « R-8 » nu au ch. 47**, même classe, même correction. **Leçon** : ajouter du contenu à un chapitre peut périmer un identifiant qu'on n'a pas touché.

**Un cardinal préservé plutôt que réécrit.** La table du ch. 48 citait d'abord `Vol. III `*TOC*` §27.2`, ce qui portait à douze le cardinal des renvois nommés au plan du Vol. III (« onze », décision 7) et déclenchait C12. Plutôt que de reporter le cardinal, le renvoi a été réaligné sur `Vol. III `*Monographie*` §27.2` — **plus exact** (le texte est rédigé, et la collation v0.14 y a établi la concordance de numérotation et de titre) et **cohérent** avec les 56 autres tables. Le cardinal onze reste donc exact, et la ligne Fusion du ch. 48, qui cite le plan, est inchangée.

**Treize écarts relevés, aucun arbitré.** Ils sont consignés dans les blocs des chapitres concernés. Le plus lourd : le ch. 34 tire un « **volet RGPD** » du ch. 20 du Vol. III, et le ch. 31 se déclare « volet Loi 25 **seul** » en conséquence — or le Vol. III rédigé a **retiré le RGPD de ce chapitre le 22 juillet 2026** (arbitrage **R-G-38**), son socle « ne documentant pas le règlement général sur la protection des données ni aucun de ses articles » (*absence de documentation*, degré 3), avec la lacune portée à son PRD **sous le numéro 16**. Trois conséquences : le ch. 31 reçoit le ch. 20 **en entier** ; la matière RGPD du ch. 34 est portée par le Vol. I (§4.8.4, §5.3), intact ; la **lacune 16 n'est pas enregistrée** au registre de l'Annexe C. S'y ajoutent : trois **doubles revendications** (fusion d'ACP entre ch. 8 et ch. 10 ; §3.4 du Vol. II entre ch. 7 et ch. 10 ; **§7.4 du Vol. III** entre ch. 16, qui l'absorbe en bloc, et ch. 17, qui le prélève nommément) ; trois **sections couvertes sans être glosées** (§1.2 du Vol. I au ch. 1 — zéro occurrence dans tout le fichier ; §2.8.5 au ch. 4 ; ANP au ch. 8) ; deux **listes de sections non réalignées** sur une ligne Fusion corrigée (ch. 1, « exécution durable » ; ch. 6, « modèle de menace, vecteurs d'attaque ») ; une **section sans source nommée** (ch. 28, budget de latence) ; un **partage non déclaré** (§26.3 du Vol. III entre ch. 45 et ch. 56) ; et une **collision de renvoi** — un « **PRDPlan §N** » nu est indécidable entre les PRDPlan des Vol. II (§4.2, §4.4) et III (§1.5, §5.3), exactement la classe que la décision 7 proscrit. **Aucun n'est corrigé ici** : l'arbitrage est une décision d'auteur, comme pour les risques 14 et 15.

**Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes de tête et fourchette ≈ 369 000–394 000 mots intactes ; aucune thèse, aucune ligne Fusion, aucun renvoi « ch. N » touché.

**Contrôles.** `check-toc.py` : **échec constaté après renommage** (quatre défauts, C8 ×3 et C12 ×1), correction, puis **sortie 0 (C1-C14)** — l'échec est consigné parce qu'il est le rendement du contrôle, non un incident. Script non modifié : harnais de mutation non rejoué. S'y ajoute un contrôle **externe et non versionné** des renvois de provenance : **955 renvois de section** de la zone des chapitres résolus contre les six documents sources (trois monographies, deux PRD, deux PRDPlan), **aucun pendant** ; validé par mutation (huit classes de faute, huit détectées, après constat de passage sur le document intact). ⚠ **Ce contrôle n'est pas au dépôt** — la vérification n'est donc pas reproductible en l'état, et son versionnement reste à décider.

---

### Révision v0.17 — finalisation : les écarts de la v0.16 soldés par les règles du fichier

**Genre.** Passe de **résolution**. La v0.16 avait déplié le plan et relevé treize écarts sans les arbitrer ; celle-ci les solde. **Aucun n'a été tranché par un choix de contenu neuf** : chacun l'a été par une règle que le fichier porte déjà — décision 2 (déduplication), décision 6 (couverture tracée), décision 7 (renvoi nommé), décision 8 (le plan s'aligne sur le chapitre rédigé). C'est la condition pour qu'une passe de cohérence ne devienne pas une passe d'auteur.

**1. La source vide — le plus lourd, corrigé par la décision 8.** Les ch. 31 et 34 se partageaient le ch. 20 du Vol. III en « volet Loi 25 » et « volet RGPD ». Ce second volet **n'existe plus** : le Vol. III rédigé l'a retiré le **22 juillet 2026** (arbitrage **R-G-38**), son socle « ne documentant pas le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation*, degré 3 de son échelle R-14, **non** fait négatif vérifié. Trois gestes : *(a)* la ligne Fusion du **ch. 31** reçoit le ch. 20 **en entier** ; *(b)* celle du **ch. 34** perd la mention — **le chapitre ne perd aucune matière**, son RGPD étant porté par le Vol. I (§4.8.4 et §5.3), intact : seule sa *provenance* désignait un vide ; *(c)* la **lacune 16 du Vol. III** entre au registre de l'Annexe C. ⚠ **Dans une seconde table**, distincte de celle des onze lacunes du Vol. II : les deux séries de lacunes se confondent comme se confondaient les deux séries F-xx, et fondre l'une dans l'autre aurait périmé un cardinal contrôlé (décision 7). Cette seconde table **se déclare incomplète** — une entrée, celle que la passe a rencontrée ; l'inventaire des lacunes du Vol. III reste un préalable de la collation de fond (porte G-4, risque 11), et le mener sur une seule rencontre produirait un registre faussement complet.

**2. Trois doubles revendications, tranchées par partage déclaré (décisions 2 et 6).** *(a)* **La fusion d'ACP** était annoncée par le ch. 8 (Vol. I *Monographie* §3.3.4) **et** le ch. 10 (Vol. II ch. 3 §3.3) : la **mécanique** de la convergence reste au ch. 8, la **portée de risque** (R-1 du Vol. II, séquencement périmé par la réserve F-06) au ch. 10, chacun renvoyant à l'autre. *(b)* **Le §3.4 du Vol. II** (versant protocolaire de R-8) était absorbé en bloc par le ch. 10 alors que l'encadré siège au ch. 7 : le ch. 10 y renvoie désormais sans le reconstruire. *(c)* **Le §7.4 du Vol. III** était pris en bloc par le ch. 16 (« Vol. III ch. 5-7 ») **et** prélevé nommément par le ch. 17 : le ch. 16 porte son « **hors §7.4** ». ⚠ **Cette troisième classe échappe au contrôle exécutable** — la double revendication y vit à deux grains différents, l'un au chapitre, l'autre à la section : elle reste une **collation manuelle**, à refaire à chaque révision d'une ligne Fusion citant un intervalle de chapitres. Le constat est porté au champ Contrôles.

**3. Cinq listes de sections réalignées sur leur ligne Fusion.** Toutes de la même famille : la ligne Fusion décidait, la phrase « Sections : … » ne suivait pas. **Ch. 1** — le §1.2 du Vol. I (cadres de référence, ISO 11354, EIF/EIRA, modèles de maturité) était couvert par l'intervalle « §1.0-1.6 » mais **glosé nulle part dans le fichier**, et « exécution durable » y figurait alors que le §1.6.3 part en entier au ch. 25. **Ch. 4** — l'arrivée du §2.8.5 n'était déclarée qu'à son départ (ch. 6) : *une arrivée se déclare aux deux bouts*, faute de quoi un chapitre rédigé sur sa seule liste de sections perd la section que la v0.5 avait sauvée. **Ch. 6** — « modèle de menace, vecteurs d'attaque » y était annoncé alors que les §2.10.1-2.10.2 partent au ch. 20. **Ch. 8** — ANP arrivait par l'intervalle « §3.2-3.3 » sans être nommé. ⚠ *Le **titre** du ch. 8 n'est pas retouché : il est cité en clair dans huit chapitres, et ANP y est un tiers comparé, non un objet de même rang que MCP et A2A — l'écart de titre est **assumé et déclaré**, non oublié.*

**4. Deux corrections de convention.** **Deux** « PRDPlan §4.4 » nus au ch. 29 — la liste de sections et le bloc de formulation imposée — deviennent « **PRDPlan Vol. II §4.4** » : la forme nue est indécidable entre les PRDPlan du Vol. II (§4.2, §4.4) et du Vol. III (§1.5, §5.3) — exactement la collision que la décision 7 proscrit, et que la v0.16 avait relevée sans la corriger. Et le **§26.3 du Vol. III**, cité par les ch. 45 et 56, porte désormais son **partage déclaré** : la métrique et son état au ch. 45, l'énoncé de recherche qui en sort au ch. 56.

**5. Une section sans source, marquée plutôt que rattachée.** Le § 28.8 (capacité d'inférence, budget de latence, contention) ne correspond à aucune sous-section du ch. 4 du Vol. I. Il est **marqué construction d'auteur** (décision 8), avec ses deux appuis les plus proches nommés (§4.3.5, §4.6.1) et ses sources primaires déclarées à établir — **le rattacher de force à une source qui ne le porte pas aurait été la faute que la décision 8 vise**.

**Ce que la passe n'a pas touché, et pourquoi.** Les **risques 13, 14 et 15** — le Livre IX sans socle, la couche d'exécution sans chapitre, l'accord entre agents sous défaillance — portent sur du **contenu manquant**, non sur une incohérence : leur arbitrage est une décision d'auteur (**D-7** du PRD), et une passe de cohérence qui comblerait un angle mort ferait exactement ce que la v0.15 s'était interdit. De même, la thèse du **ch. 20** reste en forme forte, à instruire par dénombrement. ⚠ **Les journaux antérieurs ne sont pas réécrits** : celui de la v0.14 porte « **Non traité, à dessein** — le volet RGPD reste déclaré tel quel », énoncé vrai à sa date et **périmé par la présente passe** ; il se lit dans sa numérotation et sa date d'origine, la correction vivant ici (journaux en ajout seul).

**Structure strictement inchangée** — 57 chapitres, dix livres I-X, enveloppes de tête et fourchette ≈ 369 000–394 000 mots intactes ; aucune thèse, aucun renvoi « ch. N » touché. Les 57 tables détaillées de la v0.16 sont conservées et complétées, jamais réduites.

**Contrôles.** `check-toc.py` (C1-C14, **sortie 0**) constaté avant et après édition ; le cardinal « onze » des renvois nommés au Vol. III reste exact, et celui des onze lacunes du Vol. II est préservé par la seconde table. Balayage de la **zone normative** (du Livre I au premier journal) : **zéro « Écart constaté » résiduel**, huit blocs convertis en « Écart résolu », **aucun marqueur d'action** (« à trancher », « à déclarer », « à rattacher ») laissé pendant. Contrôle externe des renvois de provenance rejoué : **955 renvois** résolus contre les six documents sources, aucun pendant. ⚠ **Ce contrôle n'est toujours pas versionné** — la vérification reste non reproductible en l'état, et son versement dans `PRD/` est la dette d'appareil de ce fichier.

---

### Révision v0.18 — reformatage markdown : les tables détaillées passent en titres

**Genre.** Passe de **forme**, la première du fichier. Aucun objet éditorial : ni collation, ni relève, ni arbitrage. Elle ne répond qu'à un défaut d'affichage — les tables des matières détaillées ajoutées par la v0.16 étaient **invisibles à tout afficheur de plan**. Un éditeur, une forge ou une table des matières Pandoc ne lisent que les titres ; les 309 entrées de section vivaient en puces en gras, sous un titre unique par chapitre. Le plan du fichier s'arrêtait donc au chapitre, alors que le contenu, lui, descendait deux niveaux plus bas.

**1. Les 309 entrées de section deviennent des titres `####`.** La forme `- **§ N.M — Titre**` devient `#### § N.M — Titre`. Le niveau 4 est celui qui fait des sections les **enfants directs** du `### Chapitre N` : la hiérarchie exposée est `## LIVRE` → `### Chapitre` → `#### § N.M`, sans niveau intercalaire.

**2. La glose passe en paragraphe (257 cas).** Ce qui suivait le titre sur la même ligne — provenance `← Vol. N`, réserves, garde-fous — devient un paragraphe sous le titre. Le séparateur « — » qui articulait titre et glose est **le seul caractère retiré par la passe** : le passage à la ligne le rend redondant.

**3. Les sous-sections restent en liste (230 cas), dés-indentées d'un niveau.** Elles ne sont **pas** promues en titres, et c'est un choix : ce sont des phrases descriptives portant leur provenance, non des intitulés. Les promouvoir aurait produit un plan de plus de mille entrées dont la plupart sont des phrases complètes — un plan illisible n'expose rien de plus qu'une absence de plan.

**4. L'en-tête de table devient un paragraphe gras.** `#### Table des matières détaillée du chapitre N` devient `**Table des matières détaillée du chapitre N**` — la forme que « **Table de couverture (décision 6)** » emploie déjà dans le même bloc. Sans ce geste, l'en-tête occuperait le niveau 4 et s'interposerait entre le chapitre et ses sections.

**Un titre normalisé, un seul.** Celui du **§ 36.4** (« Le standard technique : un fait négatif, *vérifié* ») portait un gras **imbriqué** dans un gras, forme qu'aucune découpe sur `**` ne rend : l'emphase sur « vérifié » passe en italique — forme employée partout ailleurs dans le fichier pour *fait négatif vérifié*. Le mot, sa place et son emphase sont conservés ; seul le balisage change.

**Ce que la passe ne fait pas.** Elle ne touche **ni le bandeau, ni les décisions, ni la volumétrie, ni les annexes, ni les journaux gelés** — le reformatage s'arrête aux 57 blocs de table détaillée. Elle n'ajoute **aucun index de tête** : un index serait un cardinal de plus à tenir à jour (risque 1) là où les titres se dérivent d'eux-mêmes, et le fichier porte déjà assez de décomptes multi-sites. Elle ne re-décide **aucune** ligne Fusion, aucune provenance, aucune table de couverture : les tables restent **subordonnées** (décision 8), et les renvois de provenance de la v0.17 sont inchangés — mesure : les **451 spans `← …`** de la zone des chapitres sont identiques **à l'octet** avant et après, et ce sont eux qui portent les 955 renvois résolus par cette passe.

**Contrôles.** Deux, de portées distinctes, à ne pas confondre. *(a)* **`check-toc.py` (C1-C14, sortie 0) constaté avant et après édition** : il établit que la forme reste conforme à ce que le script sait lire — les motifs de chapitre, de livre, de bandeau et d'enveloppe sont intacts, aucun renvoi ne pend, aucun cardinal ne bouge. *(b)* **Un contrôle externe propre à la passe** : comparaison du **flux de mots** du fichier avant et après reformatage — **72 764 mots, séquence identique**, donc aucun mot ajouté, retiré ni déplacé. ⚠ **Le second est le seul qui prouve la fidélité de la transformation**, et il est **jetable** : aucun des quatorze contrôles ne connaît la forme des tables détaillées, de sorte qu'un reformatage passe sans être vu par l'appareil versionné. Le constat est porté au champ Contrôles.

**Trois mutations périmées, constatées et non corrigées.** Le harnais `check-toc-mutations.py` a été rejoué, non parce que cette passe touche au script — elle n'y touche pas — mais pour établir qu'elle ne le périme pas. **Trois de ses dix-sept mutations échouent, et les trois échouaient déjà avant le reformatage** : constaté par exécution du harnais sur l'état v0.17 du fichier, mêmes trois identifiants. *(a)* **M14** est **inapplicable** — son motif (`**v0.14** (23 juillet 2026)`) n'existe plus au conspectus, réancrage dû dont le harnais avertit lui-même en tête. *(b)* **M9b** et **M11a** s'appliquent mais ne sont plus **détectées** : elles retirent une mention unique (la lacune §10.2 au ch. 27, la marque « relève v0.11 » au ch. 9) que la v0.16 a **dupliquée dans les tables détaillées** — le contrôle trouve la seconde occurrence et passe. ⚠ **C'est le harnais qui est périmé, pas les contrôles** : C9 et C11 fonctionnent, leurs mutations ne les mettent plus à l'épreuve. Le réancrage des trois motifs est une **passe d'appareil à part** — modifier le harnais dans une passe de forme reviendrait à valider un script avec un script qu'on vient de changer.

**Fichiers réalignés.** Le conspectus ([`README.md`](../README.md)) passe à v0.18 — contrôle C14 —, et le [`CLAUDE.md`](../CLAUDE.md) du dossier consigne la convention de niveaux de titres, sans quoi une passe ultérieure rétablirait les puces en croyant corriger une anomalie.

---

### Risques de cadrage propres au compendium

1. **Explosion volumétrique et non-lecture** *(aggravé en v0.5 : la re-mesure porte la projection de 300 000-326 000 à **355 000-380 000 mots**, non par ajout de contenu mais par correction d'un budget d'annexes sous-évalué de moitié ; re-aggravé en v0.8 : l'ajout du Livre XII (aujourd'hui Livre IX) — 14 000 mots de matière neuve — porte la projection à **369 000-394 000 mots**, cette fois par ajout de contenu, assumé en décision 9)* : une somme de cette taille est un ouvrage de référence, pas un ouvrage de lecture linéaire. Parade obligatoire : parcours différenciés annoncés (les « contrats de lecture » des trois volumes conservés), renvois internes denses, et l'Annexe F comme table de navigation. Sans cela, le compendium est moins utile que les trois volumes séparés — ce qui invaliderait sa raison d'être.
2. **Déduplication infidèle** : fusionner deux traitements d'un même sujet (ex. identité au ch. 3 vs Livre III ; blueprint Boréalis vs IBM au ch. 49) risque d'effacer une nuance que la séparation préservait. Parade : la ligne « Fusion » de chaque chapitre trace la décision ; toute coupe de contenu est un acte documenté, pas un silence.
3. **Péremption à trois horloges** : les trois gels (juin 2026, 16-17 juillet 2026, et — depuis la v0.13 — 21 juillet 2026 pour les 34 pièces du Vol. III) ne sont pas synchrones ; un fait vrai au gel du Vol. I peut être faux au gel du Vol. III. Parade : gel unique de l'ouvrage + re-datation systématique de tout fait périssable au socle consolidé (Annexe B), avant toute rédaction.
4. **Socle à refondre, pas à concaténer** : accoler F-01…F-48 (Vol. II), les faits du Vol. I et les repérages [C] du Vol. III produit des collisions d'identifiants et des doublons. Parade : renumérotation unique et dédoublonnage du socle (Annexe B) comme préalable technique — c'est le chemin critique du projet.
5. **Divergences rouvertes par inadvertance — et lacunes fermées par inadvertance** : les deux divergences sont tranchées à l'Annexe C, mais un chapitre repris d'un volume qui portait l'autre position peut les rouvrir silencieusement ; symétriquement, une lacune déclarée peut se refermer sans preuve du seul fait d'être rangée sous « tranché ». Parade : audit de cohérence sur les deux faits (date AMF, gouvernance AP2) à chaque gel de chapitre, et registre distinct des lacunes à l'Annexe C.
6. **Perte de la thèse dans la masse** : trois thèses partielles fondues risquent de diluer la thèse unifiante (le problème d'ingénierie continu). Parade : chaque livre rappelle en ouverture sa place dans les trois plans (coopérer / encadrer / faire confiance — auxquels la v0.8 adjoint un quatrième, *livrer*, porté par le seul Livre IX et muni de son critère d'exclusion propre en tête de livre) ; tout contenu sans rattachement à l'un de ces plans est hors périmètre.
7. **Statut du compendium vs volumes sources** : tant que la somme n'est pas rédigée, ce sont les trois volumes qui font foi ; publier un compendium partiel créerait une quatrième source de vérité concurrente des trois autres. Parade : le compendium ne se substitue aux volumes qu'à sa complétion ; jusque-là, il est un plan, et le dit (Statut, en-tête).
8. **Hygiène de dépôt héritée — dont deux reproches périmés que la v0.2 propageait** : la v0.2 reprenait tel quel le risque d'hygiène du Vol. III, alors que son PRD en avait déjà réglé deux volets. (i) *Arborescence README désynchronisée* : **reproche retiré** — vérification du Vol. III, zéro occurrence des chemins fautifs dans le README et le CLAUDE.md racine, le bloc d'arborescence reproduit les dossiers réels ; en faire une précondition à la fusion, comme le faisait la v0.2, retardait le projet sur un défaut inexistant. (ii) *`commun/faits-partages.md` à créer* : la décision de **ne pas** le créer a été prise ; l'Annexe C rouvre cette décision, ce qui est permis, mais doit se dire ainsi (voir Annexe C). Reste vrai et non résolu : la numérotation multiple du Vol. I (risque 10). Le volet README est clos en v0.12 — re-vérification du 23 juill. 2026 : le README racine annonce la somme dès son titre, à sa table des livrables et dans une section dédiée ; troisième reproche périmé retiré de ce risque, par la même mécanique que les deux premiers (un fait de dépôt vérifié à une date se re-vérifie avant d'être reconduit).
9. **Corpus d'appui hérité — tranché en amont, réversible** *(re-libellé v0.13 ; l'aggravation constatée en v0.3 est close)* : le Vol. III adossait sept sections et son Annexe E à trois ouvrages de littérature secondaire ; la vérification du 18 juillet 2026 a établi qu'**aucun n'a jamais été au dépôt** (lacune L-15), et **la décision d'auteur P0.2, tranchée le 21 juillet 2026, a retiré la filiation livresque** — L-15 close par échec documenté, les emplacements du Vol. III réaffectés à son socle. L'exigence que ce risque portait (« P0.2 doit être tranchée avant la rédaction ») est satisfaite, dans le sens prévu : l'Annexe G retombe sur GoF/EIP, le ch. 47 sur la grille des cinq questions. **Le risque résiduel est double** : (a) la décision est **réversible** — un dépôt ultérieur rouvre L-15, et les mentions « corpus d'appui » des chapitres consommateurs (contrôlées par `check-toc.py`, C10) restent les marqueurs de cette réouverture ; (b) le Vol. III rédigé a comblé ces emplacements par **construction d'auteur sous CA-07** — la fusion reprend ces passages avec leur marquage « Lecture de l'auteur », jamais comme des faits de corpus.
10. **Ambiguïté des renvois non nommés** : le Vol. I vit en numérotation **triple** — *Monographie* §1-§7, *Synthèse* **§1-§12** et Annexe B §0-§17 —, les §8.x/§10.x du Vol. II existent dans sa Monographie comme dans son PRD, le Vol. II porte deux séries « Q n » homonymes, et les deux volumes numérotent leurs garde-fous différemment (R-1…R-8 contre R-01…R-14). Un renvoi nu peut résoudre contre le mauvais document, la mauvaise série ou le mauvais volume. Parade : décision structurante (7), **appliquée en v0.3 aux quarante et un renvois du Vol. I, aux trois renvois de série — **quatre depuis la v0.5**, Q4 s'étant ajoutée au ch. 31 — et aux garde-fous des chapitres mixtes** (la v0.2 la déclarait appliquée alors qu'un seul renvoi la respectait — et la décrivait elle-même en s'appuyant sur un intervalle faux, « Synthèse §3-§12 », répété quatre fois). ⚠ **Et l'intervalle correct est §1-§12** : vérifié le 19 juillet 2026 sur `Synthese Monographie.md`. **Les TOC des Vol. I et III portent encore, tous deux, l'intervalle faux** — ce sont eux qui restent à corriger. Un futur éditeur qui collationnerait ce fichier contre eux réintroduirait l'erreur en croyant la corriger : c'est le motif pour lequel la vérification est datée et sa source nommée ici.
11. **Trois volumes absorbés, deux régimes de preuve réels — l'écart s'est réduit sans se fermer** *(ajout v0.5, hérité du risque 1 du Vol. III ; re-libellé v0.13 : le Vol. III est rédigé depuis le 22 juillet 2026)* : les Vol. I et II sont **rédigés, vérifiés et gelés** ; le Vol. III est désormais **rédigé et doté d'un socle propre** — 98 entrées F-01…F-98, 33 héritées, 15 lots clos, gel du 21 juillet 2026 — mais son propre cadrage impose « **rédigé ne vaut pas publiable** » : quinze remontées R-G-43…R-G-57 ouvertes, douze arbitrages délégués révocables (l'option écartée y est conservée), dette de vote sur F-92 et F-96, rejeu exhaustif des motifs de balayage dû. Deux livres de la somme en dérivent principalement — les Livres III et VII, **77 000 mots des 301 000 de corps, environ 26 %** — et portent son matériau le plus neuf : identité non humaine, attaques, PQC, maillage, AgentOps. Le risque n'est plus de présenter un *plan* au rang d'un volume vérifié : c'est de présenter un volume **rédigé mais non publiable** au même rang que deux volumes achevés, et de fusionner des passages que ses remontées ouvertes peuvent encore faire bouger. Parades : la **collation de fond contre le texte rédigé du Vol. III** (l'homologue de la v0.6) est un préalable déclaré à la rédaction des Livres III et VII ; les entrées à dette de vote n'entrent pas au socle consolidé sans résorption (Annexe B) ; l'état des remontées ouvertes se revérifie au gel unique ; tout arbitrage délégué révocable se relit avant reprise du passage qu'il a fixé. **Corollaire de calendrier, inversé par la v0.13** : le socle de ces deux livres est désormais **à refondre comme les autres, non à constituer** — mais leur fusion attend la collation.
12. **Dilution des trois capacités** *(ajout v0.5, reprise directe du risque 6 du Vol. III, aggravé par la fusion, réduit par la condensation v0.9)* : le Vol. III tenait ensemble trois objets — identité, maillage, exploitation — au moyen d'une ligne de défense unique : ce sont les trois capacités de l'entreprise agentique (émettre, appliquer, exploiter), et tout contenu sans lien à l'identité ou à la délégation est hors périmètre. La v0.8 les **séparait de six livres** (III, IX, X) là où le Vol. III les tenait en Parties II-III, VII et VIII ; la condensation v0.9 les resserre en **deux livres** — III (émettre) et VII (appliquer et exploiter) — séparés par trois livres : le risque diminue sans s'éteindre, deux capacités cohabitant désormais dans un même livre. Parades : la triade est énoncée en tête de fichier et à l'avant-propos ; les ouvertures des Livres III et VII nomment leurs capacités et renvoient l'une à l'autre ; le critère d'exclusion du Vol. III est reconduit mot pour mot.
13. **Un livre sans aucun socle — même pas celui d'un plan** *(ajout v0.8)* : le risque 11 distingue deux régimes de preuve ; le Livre IX (entré en v0.8 comme Livre XII) en crée un troisième, plus faible encore — il ne dérive d'aucun volume, pas même d'une proposition, et ses trois chapitres n'ont ni entrée F-xx, ni repérage [C] hérité, ni garde-fou source. Le risque est double : rédiger sur du vide en donnant au lecteur l'apparence du même régime de preuve que le reste de la somme ; ou, à l'inverse, laisser ce livre geler la publication en attendant un socle qui ne se constitue pas. Parades : statut déclaré en tête de livre et à chaque thèse (décision 9a) ; rédaction en dernier (décision 9c) ; constitution d'un socle propre — sources primaires, jamais de littérature secondaire seule — comme préalable à toute rédaction du livre ; et issue de retrait prévue — si le socle ne se constitue pas au lancement de la rédaction, le livre est retiré et les trois fronts retombent au statut v0.7, consignés comme choix de périmètre. Le retrait re-déclencherait la renumérotation inverse (55-57 → 52-54) : c'est le coût assumé de l'insertion avant clôture, préféré à un livre terminal qui aurait détrôné le chapitre de péremption.
14. **La couche d'exécution n'a de lieu nulle part dans la somme** *(ajout v0.10)* : les dix livres couvrent la boucle de l'agent (ch. 4), les protocoles (Livre II), les cadriciels de composition (ch. 27), l'encadrement (Livre IV), le maillage (ch. 41-42), l'exploitation (ch. 43-45) et l'artefact livré (Livre IX) — mais **aucun ne traite le harnais**, le programme qui héberge la boucle et porte en propre la persistance de session, les modes, les sous-agents, la chaîne d'approbation d'outils, l'admission d'extensions et la compression de contexte. Le risque est double et symétrique de celui du Livre IX. **Combler** l'angle mort ouvrirait un second livre sans socle avant que le premier ait le sien (risque 13), et sur un matériau plus volatil encore — versions d'éditeur, produits nés en novembre 2025 et renommés deux fois en janvier 2026. **Le taire** laisserait la somme décrire une architecture de confiance dont la couche où les décisions d'autorisation sont **effectivement rendues** — chaîne d'approbation, mode d'auto-approbation globale, admission d'extensions — n'est nommée nulle part, alors que c'est celle que les incidents publics de 2026 atteignent : une architecture qui certifie le porteur (Livre III), l'encadre (Livre IV), l'applique à l'arête (ch. 42) et l'exploite (ch. 43-45), sans jamais décrire le programme qui décide, en dernier ressort, d'exécuter l'appel. Parades : le constat est déclaré ici plutôt que comblé ; les huit relèves de la v0.10 sont rattachées à leurs chapitres d'accueil, où elles sont instructibles séparément ; et **l'arbitrage — chapitre neuf, sections dans les chapitres existants, ou périmètre assumé et déclaré — est une décision d'auteur, non une décision de passe**. Il se prend **avant** la rédaction des Livres VII et IX, dont trois chapitres (ch. 43, 52, 53) accueillent déjà les relèves qui en dépendent.

15. **L'accord entre agents sous défaillance n'a de lieu nulle part** *(ajout v0.15, sur audit de couverture externe du 24 juillet 2026)* : la somme décrit la communication entre agents — protocoles (Livre II), courtage et arête (ch. 41-42) —, la sûreté du collectif au grain du modèle de menace (ch. 6), les modes d'échec protocolaires (ch. 11) et les effets d'une action isolée qui réussit à moitié (ch. 54) ; **aucun chapitre ne traite l'accord** — ce que deux agents de deux institutions tiennent pour vrai quand le réseau se partitionne, quand le plan de contrôle se divise, ou quand un pair reste vivant et répond faux. Mesure du 24 juillet 2026 sur la **zone des chapitres** (de `### Chapitre 1` à `# Annexes`) : zéro occurrence de « consensus », « byzantin », « quorum », « BFT », « split-brain » ; une seule de « sagas », au ch. 54, au grain d'une action unique. ⚠ **La zone est la bonne unité de mesure, pas le fichier** : depuis cette passe, ces termes figurent dans la *déclaration* elle-même — bandeau, risque 15, journal v0.15 —, et une mesure sur le fichier entier ne distinguerait plus l'objet décrit de son constat d'absence. ⚠ **Le compendium traite déjà l'agent compromis — mais comme un problème d'identité** : le *rug-pull* du ch. 21 est une question d'admission et de révocation, non d'accord ; révoquer un porteur ne dit pas ce que le système tient pour vrai pendant la fenêtre où il répondait encore. **Le risque est double, et son économie diffère de celle du risque 14.** *Combler* n'ouvrirait pas ici un front sans socle : la matière est ancienne, primaire et stable (impossibilité FLP, tolérance aux fautes byzantines, théorème CAP et ses raffinements) — l'objection n'est pas le socle, c'est le **périmètre** (une théorie des systèmes répartis se rattache-t-elle aux quatre plans ?) et la **volumétrie** (risque 1). *Taire* laisse la somme prescrire des architectures inter-institutions — maillage inter-domaines (ch. 42), KYA (ch. 19), rails de paiement (ch. 37 et ch. 40) — sans nommer le régime de défaillance sous lequel elles opèrent, alors que c'est en finance que la divergence d'état se paie en écart comptable (thèse même du ch. 54). Parades : le constat est **déclaré ici plutôt que comblé** ; ses points d'atterrissage possibles sont nommés — ch. 6 (théorie du collectif), ch. 42 (partition et division du plan de contrôle), ch. 54 (extension des sagas à l'accord entre agents) — et **l'arbitrage — sections dans les chapitres existants, ou périmètre assumé et déclaré — est une décision d'auteur, non une décision de passe** (D-7 du PRD). Il se prend avant la rédaction du Livre I, dont le ch. 6 est le premier point d'atterrissage. ⚠ **Aucun chapitre neuf n'est proposé ici** : toute insertion resterait une décision d'auteur (décisions 9 et 10), et un livre de plus aggraverait le risque 1.
