# Évaluation académique du Compendium 2027

**Ouvrage évalué :** *Interopérabilité et Orchestration en Entreprise Agentique*, édition consolidée de novembre 2026, dans son état du 14 novembre 2026 (`CompendiumMaster.pdf`, 1 090 pages; manuscrit de 59 fichiers sous `Master/manuscrit/`).

**Niveau de référence :** études supérieures, maîtrise et doctorat.

**Note globale : 74 / 100.** Lue comme un travail de synthèse de maîtrise, l'édition vaut environ 82 / 100. Lue comme une contribution doctorale, elle vaut environ 62 / 100. Les sections 3 et 6 justifient ces trois chiffres.

---

## 1. Cadre de l'évaluation

### 1.1 Ce qui a été examiné

| Élément | Étendue de l'examen |
|---|---|
| Exposés des chapitres 8, 20, 21, 22, 24, 26, 35, 37, 38 et 39 | Lus en entier |
| Exposé du chapitre 23; chapitres 4, 14, 18, 33, 34, 40, 41, 42 et 44 | Lus par sections, limites et ancres |
| Sections « Limites » des 50 chapitres | Toutes lues, par extraction |
| Partie X : méthode et synthèse du chapitre 48, calendriers et registre du chapitre 49, mesures d'adoption du chapitre 50 | Lues |
| Ouverture | Lue en partie : enjeux, parcours de lecture, statut des affirmations |
| Annexes | D lue en entier; A et E en partie; B, C, F, G et H non lues |
| Rapport d'audit du 13 novembre 2026 et registre des corrections | Lus en entier |
| Tout le manuscrit | Mesuré par script : volumes, sources, limites, tableaux, extraits |
| Volets « Mise en œuvre » (31 volets, 152 086 mots) | Non lus, sauf fragments; jugés d'après le rapport d'audit |

### 1.2 Réserves sur l'évaluateur

Trois réserves bornent la valeur de cette évaluation.

1. **Elle n'est pas indépendante.** L'évaluateur est le modèle d'IA qui a rédigé, le 14 novembre 2026, les compléments de vingt chapitres, la révision de la partie X et de l'ouverture, et la passe de cohérence. Il juge donc en partie son propre travail. Une évaluation à l'aveugle, par un tiers, reste à faire.
2. **Elle n'est pas intégrale.** Environ 36 % du texte, soit les volets, n'a pas été lu. Le jugement porté sur eux repose sur les constats d'un audit lui-même mené par des agents.
3. **Elle ne revérifie pas les sources.** Aucune des 1 018 sources n'a été relue pour cette évaluation. Les sources ajoutées le 14 novembre ont été chargées ce jour-là; les autres sont jugées d'après ce que les chapitres en disent.

### 1.3 Mesures de l'ouvrage

| Indicateur | Valeur |
|---|---|
| Mots du manuscrit | 424 036 |
| Mots des exposés de référence | 250 052 (59 %) |
| Mots des volets « Mise en œuvre » | 152 086 (36 %) |
| Sources numérotées | 1 018, dont 774 pour les chapitres 1 à 47 et 244 pour la partie X |
| Appels de source dans les volets | 0 |
| Puces de limites déclarées | 393, soit près de huit par chapitre |
| Mentions, dans ces limites, d'une synthèse ou d'une déduction propre au chapitre | 42 |
| Tableaux | 334 |
| Extraits de code | 97 |
| Décisions d'architecture (ADR) | 31 |
| Figures | 67 |
| Constats de l'audit de publication | 425 : 17 bloquants, 121 majeurs, 287 mineurs |
| Entrées du registre | 549 : 356 corrections de l'audit, 193 compléments et harmonisations postérieurs |
| Points laissés à l'auteur par l'audit | 41, dont 1 bloquant et 10 majeurs |

Nature des 1 018 sources, d'après le nom de domaine de leur adresse. Le classement est grossier, comme le chapitre 48 le dit du sien.

| Nature | Sources | Part |
|---|---|---|
| Documentation ou billet d'éditeur, de fournisseur, et non classé | 363 | 35,7 % |
| Prépublication | 255 | 25,0 % |
| Projet ouvert : spécification, dépôt, fondation | 130 | 12,8 % |
| Texte officiel ou organisme public | 94 | 9,2 % |
| Organisme de normalisation ou de référence | 89 | 8,7 % |
| Analyste, cabinet ou presse | 44 | 4,3 % |
| Éditeur scientifique | 39 | 3,8 % |
| Sans adresse | 4 | 0,4 % |

Au moins 107 entrées portent la mention « résumé ». S'y ajoutent les 83 notices de la revue de littérature, lues par leur résumé selon le chapitre 48 lui-même. Près d'une source sur cinq n'a donc été lue que par son résumé. Vingt-huit entrées sont données pour non lues ou inaccessibles.

---

## 2. Nature de l'objet

Le compendium n'est ni une thèse ni un manuel. C'est une revue multivocale, au sens que la recherche en génie logiciel donne à ce terme : une synthèse qui mêle littérature scientifique et littérature grise, soit spécifications, documentation d'éditeurs, textes officiels et notes d'analystes. Il y ajoute deux objets d'un autre genre : des artefacts de conception (architecture de référence, grilles de décision, fiches ADR, listes de contrôle) et un cas fictif, le Groupe Boréal, qui sert de fil rouge aux volets.

L'ouvrage le dit lui-même. Sa page « À propos de cette édition » précise qu'il réunit deux éditions rédigées séparément, que le rapprochement, l'audit et les compléments ont été faits par des agents sous contrôle automatique, et qu'aucune relecture humaine intégrale n'a eu lieu. Cette franchise est une qualité, mais elle fixe aussi le plafond de la note : un texte de 424 000 mots produit sans relecture humaine ne peut pas recevoir le crédit d'un travail validé.

---

## 3. Grille de notation

| Critère | Poids | Points | Appréciation |
|---|---|---|---|
| 1. Problématique, pertinence et portée | 10 | 9,0 | Question nette, d'actualité, ancrée dans un contexte réglementé |
| 2. Cadre conceptuel et structure | 10 | 8,5 | Gabarit uniforme et thèses par chapitre; plusieurs cadres sont des propositions non éprouvées |
| 3. Méthode et reproductibilité | 15 | 9,5 | Traçabilité exemplaire de l'édition; lecture des sources fragile |
| 4. Qualité et solidité des sources | 15 | 9,0 | Corpus large et étiqueté; trop de prépublications, de documentation d'éditeurs et de résumés |
| 5. Rigueur de l'argumentation et prudence des inférences | 15 | 12,5 | Affirmations calibrées; prescriptions parfois plus fermes que leur preuve |
| 6. Contribution originale | 10 | 5,5 | Synthèses utiles; aucune donnée propre, aucune validation |
| 7. Cohérence interne et intégrité de l'ensemble | 10 | 7,0 | Audit sérieux; 41 points ouverts et des compléments non audités |
| 8. Couverture et équilibre | 5 | 4,0 | Très large; preuve de terrain et effets sur le travail restent minces |
| 9. Langue et présentation | 5 | 4,5 | Prose sobre et régulière; quelques tableaux surchargés |
| 10. Éthique de la recherche et transparence | 5 | 4,5 | Limites déclarées partout; auteur, licence et relecture humaine absents |
| **Total** | **100** | **74,0** | |

---

## 4. Appréciation critère par critère

### 4.1 Problématique, pertinence et portée (9,0 / 10)

L'ouvrage pose une question précise : qu'est-ce qui rend un parc d'agents interopérable, orchestrable et gouvernable dans une entreprise réglementée ? Chaque chapitre la décline en une question directrice d'une ligne, puis y répond par une thèse énoncée dès l'introduction. Le chapitre 26 en donne l'exemple : les plateformes sont « ouvertes sur le fil et fermées sur le plan de contrôle ». La thèse est réfutable, et le chapitre dit par quels essais la vérifier.

L'ancrage canadien et québécois distingue l'ouvrage de la littérature courante. Le chapitre 38 montre que la conformité se joue dans l'orchestration : le caractère « exclusivement » automatisé d'une décision, au sens de l'article 12.1 de la loi québécoise sur le secteur privé, dépend de l'endroit où un humain intervient. C'est un apport réel pour le lecteur visé.

Le demi-point retenu tient à la portée : le titre annonce l'entreprise en général, mais la preuve mobilisée vient surtout du logiciel et des services financiers.

### 4.2 Cadre conceptuel et structure (8,5 / 10)

Le gabarit des exposés est tenu sur cinquante chapitres : question, état de référence daté, sections numérotées, grille de décision, points à retenir, sources, limites. Cette régularité rend l'ouvrage consultable et vérifiable par programme, ce que peu de documents de cette taille permettent.

Plusieurs distinctions conceptuelles sont nettes et réutilisables : les quatre opérations de la découverte au chapitre 8 (trouver, décrire, authentifier, approuver); la gouvernance par classe de décision au chapitre 22; l'opposition entre résidence et contrôle juridictionnel au chapitre 37; la séparation entre plan de contrôle et plan de données au chapitre 23.

La réserve porte sur le statut de ces cadres. Les limites recensent 42 synthèses ou déductions propres aux chapitres. L'échelle à quatre niveaux du chapitre 26, les cinq contrôles du chapitre 24, la hiérarchie des preuves du chapitre 42 et la grille de maturité du chapitre 3, que ce chapitre dit n'avoir « éprouvée sur aucun cas », sont des propositions. Elles sont présentées comme telles, mais elles structurent ensuite des grilles de décision qui se lisent comme des prescriptions.

### 4.3 Méthode et reproductibilité (9,5 / 15)

Deux méthodes coexistent, de qualité très inégale.

**La fabrication de l'édition est reproductible.** Chaque écart entre le manuscrit et ses deux éditions d'origine est inscrit dans un registre, avec le texte avant, le texte après, la catégorie et le motif. Un script recompose le PDF, un autre vérifie dix-sept propriétés du manuscrit et du PDF. Ce dispositif dépasse ce qu'on exige d'un mémoire ou d'une thèse.

**La lecture des sources ne l'est pas.** La plupart des pages ont été lues par un outil qui en restitue un résumé, sans recollationnement mot à mot; presque tous les chapitres le disent dans leurs limites. Un chiffre peut donc être celui que l'outil a rendu, non celui du texte. Les compléments du 14 novembre en donnent deux exemples, signalés dans les limites : une étude dont les décomptes restitués ne totalisent pas l'échantillon annoncé (chapitre 21), une autre dont le résumé et les tableaux se contredisent (chapitre 8).

La sélection des sources des chapitres 1 à 47 suit un « plan initial » que le lecteur ne voit pas. Elle n'est donc ni systématique ni contrôlable. Seul le chapitre 48 publie un protocole : dix requêtes, 124 notices rendues, 83 retenues, trois critères d'inclusion. Rapporté aux lignes directrices PRISMA pour les revues de cadrage, ce protocole satisfait la question, les critères, les sources d'information, la stratégie de recherche et la synthèse. Il lui manque un protocole enregistré, une seconde base, un double tri, la lecture en texte intégral et une évaluation de la qualité des travaux retenus. Le chapitre reconnaît chacun de ces manques.

Aucun humain n'a relu l'ensemble. L'audit a vérifié en ligne les seuls faits signalés comme douteux, et 95 adresses sur 790 n'ont pas pu être contrôlées depuis le poste d'audit.

### 4.4 Qualité et solidité des sources (9,0 / 15)

Le corpus est large et honnêtement étiqueté. Les textes normatifs sont cités à la source quand elle est accessible : spécifications de MCP et d'A2A, règlement européen, ligne directrice E-23, Loi 25. L'annexe E pose une échelle de preuve à trois marques et la rappelle au lecteur.

Quatre faiblesses pèsent sur la note.

- **Le poids des éditeurs.** Plus du tiers des sources est de la documentation ou des billets d'éditeurs. C'est légitime pour dire ce qu'un produit annonce; cela ne dit rien de ce qu'il fait. Le chapitre 26 en tire la conséquence, mais d'autres chapitres s'y appuient pour des affirmations de fonctionnement.
- **Le poids des prépublications.** Un quart des sources n'a pas passé d'évaluation par les pairs, et moins de 4 % viennent d'un éditeur scientifique. Plusieurs constats reposent sur une prépublication d'un seul auteur, ce que les chapitres 21 et 34 signalent.
- **Les lectures par résumé.** Près d'une source sur cinq. À ce niveau, on rapporte ce que les auteurs mettent en avant, non ce que leur méthode permet de conclure.
- **Les textes inaccessibles.** Sept textes structurants n'ont jamais pu être lus : la Directive fédérale sur la prise de décisions automatisée, l'article 12.1 codifié, la ligne directrice de l'AMF sur l'IA, le référentiel SecNumCloud, le rapport Gartner sur la gestion d'agents, la documentation de ServiceNow et le rapport McKinsey sur le maillage agentique. Pour un ouvrage destiné aux services financiers du Québec, décrire la ligne directrice de l'AMF d'après deux analyses de cabinets est une faiblesse sérieuse.

### 4.5 Rigueur de l'argumentation et prudence des inférences (12,5 / 15)

C'est le point fort des exposés. Les affirmations sont calibrées : le texte distingue ce qu'une source établit, ce qu'un éditeur déclare et ce que le chapitre déduit. Les formules de réserve sont précises plutôt que rituelles. Le chapitre 21 écrit que les remèdes publiés « déplacent ces échecs plus qu'ils ne les suppriment »; le chapitre 22, que les sources indépendantes « confirment la direction, non l'ampleur »; le chapitre 42, qu'un cas « se juge d'abord à ce qu'il tait ».

L'ouvrage sait aussi conclure contre son sujet. Le chapitre 20 soutient que le choix d'un cadriciel compte moins qu'on le croit, et le chapitre 21, qu'ajouter des agents ne fiabilise pas un système.

Deux réserves. Les grilles de décision donnent une « option par défaut » pour chaque choix, sans indiquer la force de la preuve qui la soutient : une recommandation tirée d'une norme et une autre tirée d'un billet d'éditeur y ont le même poids visuel. Et les volets, d'après l'audit, prescrivent parfois plus que l'exposé ne retient; l'ouvrage le signale par une phrase, sans toujours trancher.

### 4.6 Contribution originale (5,5 / 10)

L'ouvrage ne produit aucune donnée. Il n'y a ni entretien, ni enquête, ni expérience, ni étude de cas réelle, ni essai des produits décrits. Le chapitre 26 propose trois scénarios d'essai d'interopérabilité et n'en exécute aucun; le chapitre 24 propose trois essais de passerelle et n'en exécute aucun.

La contribution est donc de trois ordres, tous de synthèse :

- une cartographie datée d'un champ en mouvement, avec ses contradictions relevées, par exemple les versions incompatibles d'A2A d'un éditeur à l'autre;
- des cadres d'analyse, dont la valeur reste à démontrer;
- un programme de recherche : les dix questions ouvertes de la section 48.10 et les hypothèses H1 à H6 du chapitre 4, confrontées à la littérature.

Au regard de la démarche de science de la conception, les artefacts de l'ouvrage sont construits, mais ni démontrés ni évalués. C'est la raison principale de l'écart entre la lecture de maîtrise et la lecture doctorale.

### 4.7 Cohérence interne et intégrité de l'ensemble (7,0 / 10)

L'audit de publication a relevé 425 constats et en a corrigé 356. La démarche est sérieuse, mais elle laisse 41 points ouverts, dont un bloquant au chapitre 47 et dix majeurs. Deux d'entre eux touchent au cœur du sujet : le volet du chapitre 27 fait converser deux plateformes dans une version d'A2A que le chapitre 26 dit incompatible avec celle de l'une d'elles; la fiche ADR-009 impose en production un composant que la grille de décision du chapitre 12 demande de ne pas y bâtir.

La coexistence de deux éditions reste visible. Les volets représentent 36 % du texte, ne citent aucune source et s'appuient sur un cas fictif chiffré. L'ouvrage prévient que ce cas est une fiction située en 2027 et en 2028; le risque demeure qu'un lecteur pressé prenne un chiffre du Groupe Boréal pour un résultat. Les 97 extraits de code n'ont pas été exécutés, pour autant que l'audit le montre : il y relève un fragment de processus dont le graphe est rompu et un extrait qui suit une version dépassée de MCP.

Enfin, les compléments du 14 novembre, soit 193 entrées du registre, n'ont pas été audités. La passe de cohérence qui les a suivis a corrigé une erreur que ces mêmes compléments avaient introduite dans la page « À propos ». D'autres peuvent subsister.

### 4.8 Couverture et équilibre (4,0 / 5)

La couverture est remarquable : protocoles, découverte, sémantique, mémoire, orchestration, plateformes, identité, sécurité, observabilité, droit, économie, organisation. Les renvois entre chapitres sont denses et résolus.

Trois zones restent minces. La preuve de terrain : au moins quatorze chapitres déclarent n'avoir aucune donnée d'adoption, et les études de cas reposent sur un seul déploiement lu en entier. Les effets sur le travail et l'emploi, traités par renvoi. Le droit des autres provinces et les régulateurs sectoriels hors du Canada, absents ou relevés d'après une seule source.

### 4.9 Langue et présentation (4,5 / 5)

La prose des exposés est sobre, régulière, sans jargon inutile, dans un français soigné qui garde en anglais les termes techniques. Les tableaux servent l'argument. Quelques-uns, au chapitre 26 notamment, concentrent trop d'information dans une cellule. La mise en page du PDF est propre, et les contrôles automatiques n'y trouvent ni débordement ni balisage apparent.

### 4.10 Éthique de la recherche et transparence (4,5 / 5)

Peu d'ouvrages déclarent leurs limites avec cette constance : 393 puces, près de huit par chapitre, qui disent ce qui n'a pas été lu, ce qui vient de la connaissance générale et ce qui est une déduction. Le mode de production par agents est déclaré dès la deuxième page.

Il manque ce qu'une publication exige : un auteur, une mention légale, une licence, et la relecture d'un expert humain qui engage sa responsabilité sur le fond.

---

## 5. Appréciation par partie

| Partie | Forces | Faiblesses principales |
|---|---|---|
| I. Fondements (ch. 1 à 4) | Hypothèses H1 à H6 explicites; statistiques officielles ajoutées | Définition de l'entreprise agentique propre à l'ouvrage; enquêtes d'analystes non lues à la source |
| II. Protocoles (ch. 5 à 11) | Lecture serrée des spécifications; mesures de l'écosystème réel au chapitre 8 | Aucune mesure d'un déploiement de MCP ou d'A2A en production |
| III. Sémantique, contexte, mémoire (ch. 12 à 15) | Risques de la mémoire bien posés | Articles lus par leur résumé; gains mesurés sur les bancs des auteurs |
| IV. Orchestration (ch. 16 à 22) | Taxonomie des échecs et gouvernance par classe de décision; partie la plus solide | Résultats de bancs d'essai transposés à l'entreprise par hypothèse |
| V. Architecture et plateformes (ch. 23 à 28) | Distinction entre interopérabilité déclarée et constatée | Dépendance à la documentation des éditeurs; aucun essai |
| VI. Confiance (ch. 29 à 34) | Exploitation fondée sur le succès vérifié | Littérature mince, simulation d'un seul auteur |
| VII. Droit et gouvernance (ch. 35 à 39) | Ancrage canadien et québécois; lignes de défense | Textes clés inaccessibles; lectures juridiques non validées par un juriste |
| VIII. Économie et organisation (ch. 40 à 43) | Hiérarchie des preuves du chapitre 42 | Un seul cas de premier niveau; valeur non mesurée |
| IX. Approfondissements (ch. 44 à 47) | Sujets d'avant-garde traités avec réserve | Volets deux fois plus longs que les exposés; le point bloquant de l'audit s'y trouve |
| X. Recherche (ch. 48 à 50) | Autocritique méthodique; protocole publié | Revue rapide, sur résumés, dans une seule base |

---

## 6. Verdict selon le niveau

**Niveau maîtrise : environ 82 / 100.** Comme essai de synthèse ou comme revue de littérature étendue, le travail satisfait largement les attentes : maîtrise du domaine, structure, esprit critique, conscience de ses limites. Un jury demanderait surtout la relecture humaine, la fermeture des points ouverts de l'audit et la lecture intégrale des sources qui portent les conclusions.

**Niveau doctorat : environ 62 / 100.** L'ouvrage vaut un excellent état de l'art, du type exigé à l'examen de synthèse, et il formule un programme de recherche crédible. Il ne constitue pas une thèse : il lui manque une question de recherche unique, une contribution originale démontrée, des données propres et une validation des artefacts proposés. Sa taille même joue contre lui à ce niveau, où l'on attend la profondeur sur une question plutôt que l'étendue sur cinquante.

**Note globale : 74 / 100.** Elle traduit un travail de synthèse de grande qualité formelle, dont la valeur de preuve est bornée par sa méthode de lecture, par son corpus et par l'absence de validation.

Ce qui ferait passer la note au-delà de 85 : une relecture humaine experte par partie, la lecture intégrale des sources connues par leur résumé, la fermeture des 41 points de l'audit, et au moins une validation empirique d'un artefact central.

---

## 7. Critique de fond

### 7.1 La validité de la lecture

Le risque premier n'est pas l'erreur de raisonnement, mais l'erreur de relevé. Un outil qui résume une page peut inverser une condition, arrondir un chiffre ou attribuer une phrase à la mauvaise section. L'ouvrage s'en protège par l'aveu, non par le contrôle. Tant qu'un échantillon de citations n'aura pas été recollationné à la source par un humain, le taux d'erreur de relevé reste inconnu.

### 7.2 La validité externe

Presque toute la preuve empirique vient de bancs d'essai, de cadriciels à code ouvert ou de déclarations d'éditeurs. Le passage à l'entreprise réglementée est une hypothèse, que les chapitres 21 et 42 énoncent comme telle. Les statistiques officielles ajoutées au chapitre 4 bornent l'adoption de l'IA, sans rien dire des agents.

### 7.3 Le mélange des genres

Un exposé sourcé et un volet prescriptif non sourcé se suivent dans le même chapitre, sous la même numérotation. La règle d'arbitrage est saine : l'exposé prime. Mais un lecteur qui consulte une section de volet isolée n'a aucun moyen de savoir quelle part en est appuyée.

### 7.4 La périssabilité

L'état de référence est daté au jour près, et beaucoup d'objets décrits sont en préversion ou à l'état de brouillon. L'annexe D le reconnaît : une chronologie de ce domaine vieillit vite. Sans dispositif de mise à jour, la moitié des constats sur les produits sera caduque en un an.

### 7.5 L'autorité

Un ouvrage produit par des agents, audité par des agents et complété par un agent pose une question d'autorité que la transparence ne résout pas. La régularité du texte peut inspirer une confiance que sa méthode ne justifie pas encore.

---

## 8. Programme de travaux pour 2027

Les travaux sont classés par ordre de priorité. Chacun a un livrable vérifiable.

### 8.1 Assainir l'édition (premier trimestre)

| Travail | Livrable |
|---|---|
| Fermer les 41 points laissés à l'auteur, en commençant par le point bloquant du chapitre 47 et les dix majeurs | Registre mis à jour; zéro point bloquant, cinq majeurs au plus |
| Soumettre les 193 compléments du 14 novembre à un second audit, mené par un lecteur qui ne les a pas écrits | Rapport d'audit complémentaire |
| Recollationner à la source un échantillon aléatoire de 200 citations chiffrées | Taux d'erreur de relevé, publié dans l'annexe E |
| Lire en texte intégral les sources connues par leur résumé qui portent une conclusion | Mention « résumé seulement » ramenée sous 5 % des sources |
| Obtenir les sept textes inaccessibles, par un accès humain | Chapitres 22, 23, 26, 37 et 38 révisés |
| Faire relire chaque partie par un expert humain du domaine, et les chapitres 35 à 38 par un juriste | Attestation de relecture par partie |
| Fixer l'auteur, la mention légale, la licence et l'ISBN | Page de titre et métadonnées complètes |

### 8.2 Produire une preuve propre (premier au troisième trimestre)

| Travail | Livrable |
|---|---|
| Étude de cas multiple dans trois à cinq organisations canadiennes réglementées, par entretiens et analyse documentaire | Mise à l'épreuve des hypothèses H1 à H6; chapitre 42 refondu |
| Essai d'interopérabilité : les trois scénarios du chapitre 26, la trousse de compatibilité d'A2A et les essais de conformité de MCP, sur trois plateformes | Tableau « constaté » en regard du tableau « documenté » |
| Essai de passerelles : les trois essais du chapitre 24 sur des produits que l'ouvrage décrit | Latence ajoutée, taux d'arrêt des descriptions piégées, contournement |
| Mesure de la supervision dans un déploiement réel : taux de modification, temps de révision, tâches témoins | Première mesure indépendante de la fatigue d'approbation |
| Mise à l'épreuve de la grille de maturité du chapitre 3 et de l'échelle du chapitre 26 sur des cas | Cadres validés, amendés ou retirés |

### 8.3 Durcir la méthode (deuxième trimestre)

| Travail | Livrable |
|---|---|
| Convertir la revue du chapitre 48 en revue multivocale à protocole enregistré : deux bases au moins, double tri, lecture intégrale, évaluation de la qualité des travaux et des sources grises | Protocole public; diagramme de flux; chapitre 48 refondu |
| Publier le « plan initial » et les critères de sélection des sources des chapitres 1 à 47 | Annexe méthodologique |
| Indiquer, dans chaque grille de décision, la force de la preuve derrière l'option par défaut | Colonne « niveau de preuve » dans les 50 grilles |
| Recalculer le profil du corpus sur l'ensemble des sources, par un classement manuel | Section 48.2 à jour |

### 8.4 Rendre les volets vérifiables (deuxième et troisième trimestres)

| Travail | Livrable |
|---|---|
| Exécuter les 97 extraits de code dans une chaîne d'intégration | Dépôt compagnon; extraits marqués « exécuté » ou « illustratif » |
| Marquer visuellement tout chiffre du cas fictif | Convention typographique dans les volets |
| Relier chaque prescription d'un volet à la section d'exposé qui l'appuie, ou la déclarer sans appui | Renvois systématiques |

### 8.5 Tenir l'ouvrage à jour (toute l'année)

| Échéance | Mise à jour attendue |
|---|---|
| Premier trimestre | Annonces des conférences de la fin de 2026; jalons de l'IETF de mars 2027 |
| 1er mai 2027 | Entrée en vigueur de E-23 et de la ligne directrice de l'AMF : chapitres 38 et 39 |
| Février à août 2027 | Prochaine révision de MCP; versions d'A2A : chapitres 5, 6, 8 et 20 |
| Tout au long de l'année | Projet de loi C-36; proposition européenne sur le nuage et l'IA; schéma EUCS; nouvelle série statistique sur l'adoption |
| Décembre 2027 | Règles européennes sur le haut risque : chapitre 35 |
| Chaque trimestre | Les dix requêtes du chapitre 48 et le registre de veille du chapitre 49 |

L'ouvrage devrait adopter un versionnage explicite, un journal des changements par chapitre et une règle de retrait pour les sections dont les sources n'ont pas été relues depuis deux cycles.

### 8.6 Valoriser (second semestre)

Quatre apports se prêtent à une soumission à une conférence ou à une revue, une fois validés : les quatre opérations de la découverte et le registre comme point de gouvernance; l'écart entre interopérabilité déclarée et constatée; la gouvernance de l'autonomie par classe de décision; les acceptions du maillage agentique. Pour une thèse, il faudrait retenir une seule de ces questions, la doter d'un protocole et de données, et traiter le reste comme état de l'art.

### 8.7 Indicateurs de réussite pour l'édition 2027

| Indicateur | État au 14 novembre 2026 | Cible |
|---|---|---|
| Sources lues au-delà de leur résumé | Environ 80 % | 95 % |
| Citations chiffrées recollationnées à la source par un humain | 0 | Échantillon de 200 |
| Sources d'éditeurs scientifiques ou évaluées par les pairs | Moins de 4 % par l'adresse | 15 % |
| Points bloquants ouverts | 1 | 0 |
| Points majeurs ouverts | 10 | 5 au plus |
| Études de cas réelles | 0 | 3 |
| Artefacts validés empiriquement | 0 | 2 |
| Extraits de code exécutés | Inconnu | 100 % |
| Parties relues par un expert humain | 0 sur 10 | 10 sur 10 |

---

## 9. Conclusion

Le Compendium 2027 est un travail de synthèse d'une ampleur et d'une tenue rares, qui a le mérite de dire à chaque page ce qu'il ne sait pas. Sa faiblesse est le revers de sa force : il sait décrire avec précision l'état de sa preuve, mais cette preuve reste empruntée, lue trop souvent de seconde main et jamais mise à l'essai. La note de 74 sur 100 récompense la qualité de l'analyse et de l'appareil critique; elle retient ce qu'un ouvrage de référence doit encore à ses lecteurs : une relecture humaine, des sources lues en entier et des résultats qui lui soient propres. Le programme de la section 8 dit comment y parvenir en 2027.
