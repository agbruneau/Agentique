# Relecture adversariale — phase P4, les treize pièces restantes

| Champ | Valeur |
|---|---|
| Objet | **Les 13 pièces qui demeuraient au gabarit à la clôture de P3** — avant-propos, ch. 22 à 28 (Parties VII à IX), annexes A à E —, rédigées, relues adversarialement et corrigées les 21 et 22 juillet 2026. Ce rapport **succède** à [`relecture-P3.md`](relecture-P3.md) sans le remplacer : celui-ci demeure la trace du tronc, et ses chiffres valent à sa date |
| Relecteurs | **Un par pièce au moins, distinct du rédacteur** (CA-14) ; **six pièces en ont reçu deux**, par des relecteurs distincts entre eux — ch. 22, 23, 24, 25, 26 et 27. ⚠ **La distinction rédacteur / relecteur demeure déclarée et non constatable sur disque** — réserve 1 de R-G-19, non levée par P4 |
| Verdict | ⚠ **`A_CORRIGER` sur les 13 pièces, sans exception.** **181 réfutations journalisées**, décomptées sur les 13 en-têtes et les 13 blocs `## Notes` ; **180 ont produit une correction**, **1 a été écartée comme infondée après constat sur pièce** (ch. 22, seconde passe) |
| État des correctifs | ☑ **Appliqués dans le pipeline, non différés.** Les 13 en-têtes déclarent le point 6 de la boucle qualité ([PRDPlan](../prd/PRDPlan.md) §5.2) tenu à l'intérieur de la passe de rédaction — leçon de P3, appliquée. Constat sur pièce : **les 34 en-têtes du volume portent le statut « Rédigé et relu adversarialement »**, lu champ par champ le 22 juillet 2026 ; **aucun gabarit ne subsiste** |
| Contrôles spécifiques | **Trois**, tous déposés sous `verification/` : [CA-09](relecture-CA-09-P4.md) (périmètre, Parties VII et VIII), [CA-13](relecture-CA-13-P4.md) (traçabilité, Partie IX), [CA-12 étendue aux rapports de lot](relecture-CA-12-lots.md). ⚠ **Chacun déclare ses propres bornes, et elles sont reportées ici sans être adoucies** |
| Périmètre | **Les 13 pièces de P4 et elles seules**, plus les trois rapports de contrôle et les registres. Les 21 pièces du tronc n'ont pas été relues par la présente passe ; elles n'ont été **re-mesurées** que pour la volumétrie |

⚠ **Ce document est la trace d'un contrôle, pas un certificat de conformité.** Il n'atteste la conformité d'aucune pièce à aucun garde-fou. Les cardinaux qu'il publiait ont été re-mesurés sur leur domaine entier — les 34 fichiers de `monographie/`, les en-têtes du registre des remontées, les 68 cibles de lien du commit de renommage ; ceux qui n'ont pas pu l'être sont déclarés comme tels plutôt qu'estimés.

⚠ **Amendement du 22 juillet 2026 — les cardinaux mouvants de ce rapport avaient été retirés et remplacés par des marqueurs `##…##` ; la mesure unique a eu lieu et les a renseignés.** Motif du dispositif : **quatre passes parallèles ont publié des décomptes de volumétrie et de remontées pendant qu'une cinquième écrivait**, chacune mesurant un état vrai à son instant et faux à la fin. Treize marqueurs avaient été posés, en trois familles — **volumétrie** (total, taux, relevé par bloc, sous-totaux du tronc et de l'appareil avec leurs taux, dépassement de la projection), **remontées** (cardinal et ventilation en tranchées, sans objet, ouvertes) et **liens** (cibles `prd/`). ☑ **Ils ont été renseignés en fin de chaîne, par un porteur unique, à partir d'une seule exécution des mesures sur leur domaine entier**, et reportés au même acte à tous les porteurs — présent rapport, [registre des remontées](remontees-gouvernance.md), [registre de gel](../monographie/99-registre-gel.md), [PRDPlan](../prd/PRDPlan.md), `CLAUDE.md` du volume, avant-propos et annexe A. *Un décompte exact publié par quatre passes concurrentes produit quatre chiffres et aucune vérité.* Les cardinaux **stables** — 34 pièces, 98 entrées propres, 33 héritées, 15 lots, 22 lacunes — sont conservés et vérifiés sur pièce.

---

## 1. Ce que la phase a produit — décomptes re-mesurés

### 1.1 Le cadrage P4.0, préalable à toute rédaction

Quatre actes, chacun constaté à son siège le 22 juillet 2026 :

- **Le verrou du ch. 26 est levé.** Le lot complémentaire **L-14b** ([`lot-L-14b-metriques-agentops.md`](lot-L-14b-metriques-agentops.md), déposé le 21 juillet 2026 en soirée) instruit les métriques d'observabilité agentique que L-14 n'avait pas couvertes. Le [PRD](../prd/PRD.md) §7.6 porte **15 lots clos sur 15** ; le ch. 26 n'est plus interdit d'écriture par §7.0.
- **Neuf entrées versées au socle.** Le [PRD](../prd/PRD.md) **§7.11** — siège propre à P4, motivé comme l'était le §7.10 pour P3 — porte **F-90 à F-98**, comptées une à une dans le fichier. Le socle propre passe de 89 à **98 entrées** ; le socle hérité demeure à **33** (H-01 à H-33), inchangé.
- **La liste des lacunes passe de quatorze à vingt-deux.** Cardinal re-mesuré sur la liste du [PRD](../prd/PRD.md) §10 : **vingt-deux items numérotés de 1 à 22, sans discontinuité**, dont deux barrés comme instruits et clos. ⚠ **Le chiffre « quatorze » est périmé partout où il désigne le cardinal courant** — il demeure exact dans les blocs d'historique daté, et le distinguer est le travail que la passe corrective a dû faire dans huit occurrences réparties sur sept pièces du tronc.
- **Sept arbitrages de P3 sont enfin reportés au TOC.** Relevé par identifiant sur [`TOC.md`](../prd/TOC.md) v0.8 : **R-G-08, R-G-09, R-G-13, R-G-14, R-G-15, R-G-37 et R-G-38** y figurent, cinq d'entre eux sous la mention littérale « *arbitrage rendu en P3 et reporté en P4.0* ». ⚠ **Ce sont des arbitrages délégués, et ils demeurent révocables** : leur report ne les convertit pas en décisions d'auteur.

La confrontation préalable des treize thèses au socle est déposée à [`theses-P4-confrontation.md`](theses-P4-confrontation.md) — **13 pièces confrontées sur 13, 37 écarts relevés, 0 pièce sans écart**, cardinaux lus dans son en-tête. C'est la parade héritée de R-G-37, et elle a fonctionné : aucune thèse de P4 n'a été écrite avant d'avoir été confrontée.

### 1.2 Volumétrie — re-mesurée par la présente passe, et elle diffère de ce qui lui a été annoncé

Commande de référence ([PRDPlan](../prd/PRDPlan.md) §1.5, `LC_ALL=C.UTF-8`), à exécuter **sur les 34 fichiers**, non sur un échantillon ni sur les valeurs publiées en en-tête : **160 447 mots** pour **102 500** de cible cumulée, soit **+56,5 %**.

☑ **Le relevé par bloc, refait en une mesure unique le 22 juillet 2026 en fin de chaîne.** Les **cibles** par bloc sont stables et viennent du [PRD](../prd/PRD.md) §6.1 ; le réel est sommé depuis les mesures pièce par pièce, non estimé.

| Bloc | Cible | Réel | Écart |
|---|---|---|---|
| Avant-propos | 2 500 | 3 955 | +58,2 % |
| I — ch. 1 à 4 | 11 000 | 13 895 | +26,3 % |
| II — ch. 5 à 8 | 12 000 | 18 338 | +52,8 % |
| III — ch. 9 à 11 | 9 500 | 12 986 | +36,7 % |
| IV — ch. 12 à 15 | 12 000 | 16 984 | +41,5 % |
| V — ch. 16 à 18 | 9 000 | 13 104 | +45,6 % |
| VI — ch. 19 à 21 | 9 500 | 11 700 | +23,2 % |
| VII — ch. 22 et 23 | 7 000 | 11 523 | +64,6 % |
| VIII — ch. 24 à 26 | 10 000 | 16 867 | +68,7 % |
| IX — ch. 27 et 28 | 11 000 | 21 643 | +96,8 % |
| Annexes A à E | 9 000 | 19 452 | +116,1 % |
| **Total du volume** | **102 500** | **160 447** | **+56,5 %** |

: Volumétrie réelle du volume III par bloc au 22 juillet 2026, mesure unique de fin de chaîne.

⚠ **Mesure postérieure — activité P5.3, 22 juillet 2026.** Le présent tableau vaut à la clôture de P4 et est conservé à ce titre (en-tête : *ses chiffres valent à sa date*). Après lui, les retraits CA-12 de la passe P5.1 ont coupé **23 mots** — ch. 1, ch. 25, avant-propos, ch. 28 §28.3 —, et la re-mesure unique de P5.3 sur les 34 pièces donne **160 427 mots** (tronc **87 001**, appareil **73 426**), portée au [registre de gel](../monographie/99-registre-gel.md), seul porteur de la mesure courante ; les 34 en-têtes concordent avec elle, champ par champ. Les pourcentages par bloc sont inchangés, hormis VIII (**+68,6 %**) et IX (**+96,7 %**).

⚠ **Le chiffre de 159 951 mots (+56,0 %) qui a été transmis à cette passe était déjà périmé quand elle l'a reçu**, et le constat vaut plus que l'écart : il datait d'**avant** la passe corrective du 22 juillet, qui a ajouté des datations de report dans neuf pièces du tronc. La valeur que cette passe lui a substituée a été périmée à son tour, par les passes du même jour. *Un relevé de volumétrie se périme à la vitesse de la passe suivante, non à celle de la phase* — et c'est le motif du passage aux marqueurs.

### 1.3 D'où vient le creusement de l'écart

L'écart ne s'est pas creusé uniformément, et la décomposition par phase le montre. Sous-totaux **sommés**, non estimés :

| Périmètre | Cible | Réel | Écart |
|---|---|---|---|
| Les 21 pièces de P3 (ch. 1 à 21) | 63 000 | 87 007 | **+38,1 %** |
| Les 13 pièces de P4 (avant-propos, ch. 22 à 28, annexes A à E) | 39 500 | 73 440 | **+85,9 %** |
| **Volume entier** | **102 500** | **160 447** | **+56,5 %** |

: Décomposition de l'écart de volumétrie par phase de rédaction, au 22 juillet 2026.

**Le creusement vient presque entièrement de P4, et il a une cause structurelle nommable.** Les treize pièces de P4 sont, à une exception près, des **pièces de composition ou d'appareil** : elles ne consomment pas une passe de recherche, elles consomment d'autres chapitres. Or une affirmation qui vient d'un chapitre amont doit être **tracée vers lui** ou **marquée comme inférence** (CA-13, CA-07) — et il n'y a pas de troisième cas. Chaque affirmation coûte donc son renvoi, son niveau, son degré et sa borne, là où un chapitre de socle cite une entrée une fois. Les trois premiers rangs de l'écart au [registre de gel](../monographie/99-registre-gel.md) sont des pièces d'appareil : **annexe C (+267,6 %), annexe A (+126,9 %) et annexe D (+109,7 %)**, taux repris du registre après la mesure unique du 22 juillet 2026. ⚠ **La désignation antérieure — « annexe C, annexe A, ch. 28 » — était fausse et l'était déjà avant cette passe** : le ch. 28 sort à **+99,8 %** et occupe le **quatrième** rang, l'annexe D le devançant depuis son dépôt. *Un rang se relit sur le tableau qui le porte, il ne se retient pas.* En mots — et non en taux —, l'ordre est autre : ch. 28 (**+5 491**), ch. 27 (**+5 152**), annexe C (**+4 014**) ; les deux lectures sont vraies et ne désignent pas les mêmes pièces.

⚠ **Deux mécanismes s'y ajoutent, et ils sont l'un et l'autre des effets de contrôle, non de prose.**

- **Consigner une coupe coûte les deux tiers de ce qu'elle retire.** CA-09 a retiré **499 mots** de hors-périmètre et écrit **271 mots** de déclaration de coupe à leur place — **228 mots** de gain arithmétique. *Une passe de périmètre ne réduit pas une volumétrie ; elle la déplace du contenu vers sa traçabilité.*
- **Les correctifs allongent, et ils reprennent une part du gain.** Le bilan **mesuré** sur les cinq pièces est de **−210 mots**, non de −228 : les ch. 23 et 25 ont **grossi** de leur seconde relecture — de douze et six mots — pour la seule raison qu'ils annonçaient une relecture CA-09 « qui reste due », énoncé devenu faux le jour où elle a eu lieu. *La différence entre les deux chiffres n'est pas une erreur : c'est le coût d'une attestation qui cesse d'être vraie.*

⚠ **L'écart se documente, il ne s'ampute pas**, et le motif est le même qu'en P3 : il vient des **bornes rétablies**. **Amputer une borne et couper un hors-périmètre sont deux gestes opposés qui produisent le même chiffre** — c'est la raison pour laquelle un arbitrage de volumétrie ne se rend pas depuis un pourcentage. La cible demeure indicative et non normative (PRD §6.1) ; son arbitrage appartient à l'auteur (**R-G-47**, ouverte), et la projection de 140 800 mots que **R-G-39** avait inscrite — au **registre de gel**, seul siège qui la porte — est dépassée de **19 647 mots** — un taux calibré sur les seules pièces du tronc ne prédit pas l'appareil.

---

## 2. Le constat de méthode le plus coûteux de la phase

*Il ne porte pas sur une pièce. Il porte sur la relecture adversariale comme instrument, et il faut l'écrire sans l'adoucir.*

**Le découpage des trois vues du ch. 27 §27.2 s'écartait de la spécification du [PRD](../prd/PRD.md), Annexe B §B.2, sur trois points, sans aucune trace ni aucun marquage — et il a survécu à deux relectures adversariales et à dix-huit réfutations appliquées.** Les trois écarts, relevés par [CA-13](relecture-CA-13-P4.md) §2.4 :

| Vue | Ce que la pièce posait | Ce que le PRD §B.2 assigne | Écart |
|---|---|---|---|
| Vue 1 (E1) | émettre, **ancrer**, inscrire, vérifier, révoquer, admettre — **six** | émission, registre, vérification, révocation, **chaîne de mandat**, admission — **six** | **Substitution** : l'ancrage entre, la chaîne de mandat protocolaire sort |
| Vue 2 (E2) | point de décision, point d'application, passerelle | PEP/PDP, passerelles, politiques, **confinement** | **Dédoublement** du couple PEP/PDP ; **confinement absent** |
| Vue 3 (E3) | observer, évaluer, détecter la dérive, répondre à l'incident — **quatre** | observabilité, évaluation, dérive, incident, **cycle de vie** — **cinq** | **Cycle de vie absent** |

: Les trois écarts du §27.2 à la spécification du PRD §B.2, relevés le 22 juillet 2026.

**Ce que ce cas apprend sur la relecture adversariale, et qui n'est écrit dans aucun document amont.**

**(1) La faute était invisible à un contrôle qui compte.** La Vue 1 annonçait **six** fonctions, exactement le cardinal de la ligne E1 que le §27.1 venait de reproduire fidèlement. Un relecteur qui vérifie un cardinal voit une concordance. *Seule la confrontation de l'énumération à celle de la spécification voit la substitution* — et la confrontation d'énumérations n'est le mandat d'aucune des cinq étapes de la boucle qualité.

**(2) La faute était invisible à un contrôle qui lit.** Le contenu de chaque case des trois tables **était tracé** : c'est précisément ce que les deux relectures avaient vérifié, et elles avaient raison. Ce qui n'était tracé ni marqué, c'était le **découpage lui-même** — un objet qui n'est le contenu d'aucune case et qu'aucune lecture de case n'atteint. *Une relecture qui vérifie les éléments d'une liste ne vérifie pas la liste.*

**(3) Elle a été attrapée par un contrôle d'un autre type.** Ni un rédacteur, ni deux relecteurs adversariaux, ni dix-huit réfutations appliquées n'ont produit ce constat ; **CA-13** l'a produit à la première lecture, parce qu'il ouvre la spécification de cadrage et la confronte élément par élément. *Répéter un contrôle du même type n'augmente pas sa couverture ; il augmente sa profondeur sur ce qu'il voit déjà.* La leçon de P3 — « un échantillon qui trouve encore autant à sa dernière ligne n'a pas épuisé son gisement » — reçoit ici son pendant : **un gisement peut être entièrement hors de portée de l'instrument, quel que soit le nombre de passes.**

### 2.1 Le corollaire de CA-13, et il vaut pour tout ce qui reste à écrire

**Un chapitre qui reprend la découpe du cadrage n'a rien à marquer ; un chapitre qui la refait doit tout marquer, et c'est là que la faute se loge.**

Le **ch. 28 a été épargné par reprise, non par mérite** : son §28.1 à §28.3 reprend le découpage du PRD §B.4 sans le re-couper — trois transitions, treize gestes, ordre identique, vérifié terme à terme par CA-13 §3.1. Il n'avait donc **rien à marquer** à cet endroit, et l'absence de marquage y était correcte. Le ch. 27 re-coupe le §B.2 en trois endroits, et l'absence de marquage y était une faute bloquante. *Les deux pièces présentaient le même symptôme — pas de marquage sur un découpage — et une seule était en faute.* Un contrôle qui se serait borné à chercher le marquage aurait produit deux verdicts faux.

⚠ **La correction est opérée et constatée sur pièce** : le §27.2 porte désormais, **avant la Vue 1**, un marquage « Lecture de l'auteur » dans sa forme exacte qui nomme les trois écarts un par un, trace l'ancrage à **F-09** pour ce que le socle en documente, et renvoie les trois éléments écartés à leur siège — contrat E1 → E2 du §27.1, **ch. 25 §25.3** pour le confinement, **ch. 25** pour le cycle de vie.

---

## 3. Les trois contrôles spécifiques — résultats et bornes déclarées

*Aucun des trois ne certifie une pièce. Chacun déclare son périmètre, et les trois périmètres laissent des trous que la présente section nomme.*

### 3.1 CA-09 — test d'appartenance, Parties VII et VIII

**Résultat :** cinq pièces, **vingt sections examinées, vingt passent** au grain de la section. **Deux développements coupés** au grain du *développement* :

| Siège | Ce qui est coupé | Retiré | Déclaration écrite à la place |
|---|---|---|---|
| **ch. 22 §22.2** | le transport SLIM (`draft-mpsb-agntcy-slim-02`, `L13-A5`) — couche de messagerie et son chiffrement | **227 mots** | 164 mots |
| **ch. 25 §25.3** | le stade commercial des outils de triage (**F-58**) — trois éditeurs, trois stades de disponibilité | **272 mots** | 107 mots |
| | **Total** | **499 mots** | **271 mots** |

: Les deux coupes de périmètre opérées le 22 juillet 2026.

Le principe de discrimination est écrit dans le rapport pour être réfutable : *une réponse négative est une réponse ; un état de produit n'en est pas une.* Une entrée du socle en sort **orpheline** — **F-58** demeure mobilisée au ch. 15 §15.1, hors du champ de CA-09, avec ses trois bornes.

⚠ **La borne, et c'est celle qui coûte : le grain de CA-09 n'est pas tranché.** Le critère prescrit un contrôle **« section par section »** ; le PRD §5.1, qu'il met en œuvre, énonce le test au grain du **« développement »**. **Les deux coupes vivaient dans des sections qui passent** — au grain prescrit, aucune n'aurait été trouvée. La question est consignée au [PRD](../prd/PRD.md) §11 comme **question ouverte**, chiffrée et non arbitrée, et ouverte au registre sous **R-G-46**. *Un critère d'acceptation relève de l'auteur.* ⚠ **L'écart se reposera à l'identique sur la Partie IX et sur l'appareil, que ce contrôle n'a pas couverts.**

### 3.2 CA-13 — traçabilité de la Partie IX

**Résultat : trois cas « ni tracé ni marqué », trois corrigés ; aucune trace fausse.** Ce second membre est le résultat le plus solide de la passe et mérite d'être dit séparément : **toutes les entrées citées par les deux pièces portent ce que les pièces leur font porter**, vérifié par ouverture de chaque entrée au PRD §7.2, §7.3, §7.8 à §7.11 — soit plusieurs dizaines d'entrées propres et héritées.

Les trois cas :

1. **ch. 27 §27.2** — le découpage des trois vues (§2 ci-dessus). **Bloquant.**
2. **ch. 27 §27.3** — la **sixième** correspondance réglementaire du tableau (cadre bancaire) portait « Attente réglementaire — ne rien anticiper » **seule**, sans marquage d'inférence. ⚠ La faute est subtile et vaut d'être nommée : « attente réglementaire » qualifie **la prudence due à un texte non publié**, non le **statut du lien**. **Les deux se cumulent ; l'un ne tient pas lieu de l'autre**, et R-07 n'admet aucune exception. Une réfutation antérieure avait corrigé le **décompte** de cette même colonne sans jamais poser la question du **statut** de sa sixième ligne — *le décompte était exact ; c'est la colonne qui était incomplète.*
3. **ch. 28 §28.1 et §28.4** — la clause renforcée de **R-07**, due pour E-23, absente en deux endroits. ⚠ **Aucun motif de balayage du PRD §A.6 ne l'attrape** : elle n'existe qu'à deux endroits du garde-fou et ne se déduit d'aucune entrée. Seul un parcours des rapprochements un à un la voit manquer.

### 3.3 CA-12 étendue aux rapports de lot

**Résultat : treize rapports relus** — et non douze. L'écart n'est pas une erreur du compte rendu amont : **L-14b a été déposé après la remontée qui annonçait douze**. ⚠ *Un décompte de périmètre est un instantané, pas une clôture* — d'où la remontée qui demande de doter R-12 d'une **règle de périmètre** plutôt que d'un cardinal.

**Zéro charge utile, zéro séquence d'exploitation, zéro preuve de concept.** Contrôle préalable mécanique sur les treize fichiers : **zéro délimiteur de bloc de code**.

**Deux retraits, tous deux d'attestations auto-délivrées** — [L-09](lot-L-09-revocation-integrite.md) §E point 5 et [L-10](lot-L-10-soc-agentique.md) §E point 7. Constat sur pièce le 22 juillet 2026 : les deux formules ont **zéro occurrence** dans leurs fichiers respectifs.

**Ce que la passe a trouvé n'est pas la faute qu'elle cherchait, et c'est son résultat.** Elle cherchait les jumelles du verbatim de fiche de vulnérabilité corrigé dans L-08 le 21 juillet ; elle n'en a trouvé aucune. Elle a trouvé une faute de **troisième famille** — et le raisonnement qui la condamne mérite d'être posé une fois pour toutes :

> **Aucune des deux propositions retirées n'était matériellement fausse.** Aucun élément opératoire ne figurait dans ces rapports, et l'attestation le disait exactement. ***Ce qui est proscrit est le geste, non son résultat*** — et c'est **précisément parce qu'elle est ici exacte que la formule est dangereuse** : elle installe l'usage d'une clause que le contrôle suivant trouvera fausse ailleurs. C'est ce qui s'est produit dans L-08, où la même clause était fausse sur trois passages.

⚠ **Les deux retraits siègent dans les deux lots dont la matière est la plus proche d'un vecteur** — révocation et intégrité d'outils pour L-09, sécurité opérationnelle pour L-10. *La formule apparaît là où le rédacteur sent le risque, ce qui la rend prévisible et repérable.* Onze rapports sur treize n'en portaient aucune : la contamination est réelle et bornée.

⚠ **Cinq autres rapports portent des attestations auto-délivrées d'un autre critère** — bornage, neutralité fournisseur : L-04 §E points 2 et 6, L-06 §E point 6, L-09 §E point 2, L-11 §E point 1, L-14 §E point 4. **Signalées, non corrigées** : elles sont hors de la lentille CA-12, qui est unique. Ouvertes au registre sous **R-G-49**, avec la tension qu'elles rouvrent contre **R-G-07** — *un rapport de lot ne se réécrit pas*, et deux viennent pourtant de l'être.

⚠ **Un constat de forme, hors lentille, et il touche le socle** : **99 cellules de tableau tronquées à la génération**, sur **douze rapports de treize** (L-14b seul indemne, ayant été rédigé sans le générateur). Les blocs `**Réserve**` du §F sont **intacts partout**, ce qui est décisif au regard de la faute de P1.4 où la troncature avait coupé précisément sur les clauses de bornage. Mais plusieurs **reformulations de contrôle de bornage** — l'acte même par lequel un excès a été retiré — ne sont lisibles qu'à moitié. Ouvert sous **R-G-50**.

---

## 4. Décompte des réfutations

**181 réfutations ou correctifs journalisés sur les 13 pièces.** Décompte établi pièce par pièce sur les 13 en-têtes et les 13 blocs `## Notes`, non recopié d'un document amont.

| Bloc | Pièce | Passes | Bloquantes | Majeures | Mineures | Non ventilées | Total |
|---|---|---|---|---|---|---|---|
| — | avant-propos | 1 | — | — | — | 5 | **5** |
| VII | ch. 22 | 2 | 1 | 4 | 5 | 12 | **22** |
| VII | ch. 23 | 2 | 3 | 8 | 6 | — | **17** |
| VIII | ch. 24 | 2 | 1 | 4 | 3 | 9 | **17** |
| VIII | ch. 25 | 2 | 3 | 8 | 9 | — | **20** |
| VIII | ch. 26 | 2 | 2 | 13 | 4 | — | **19** |
| IX | ch. 27 | 2 | 4 | 10 | 4 | — | **18** |
| IX | ch. 28 | 1 | — | — | — | 9 | **9** |
| Annexes | A | 1 | — | — | — | 9 | **9** |
| Annexes | B | 1 | — | — | — | 8 | **8** |
| Annexes | C | 1 | — | — | — | 15 | **15** |
| Annexes | D | 1 | — | — | — | 9 | **9** |
| Annexes | E | 1 | 2 | 6 | 5 | — | **13** |
| | **Total** | | **16** | **53** | **36** | **76** | **181** |

: Réfutations journalisées par les treize pièces de P4, décomptées sur pièce le 22 juillet 2026.

⚠ **Soixante-seize réfutations ne sont pas ventilées par gravité, et ce rapport ne les invente pas** — huit pièces journalisent leurs correctifs sans les graduer, et deux ne graduent que leur seconde passe. *Une gravité qu'on ne peut pas constater ne se déduit pas du libellé du correctif.* La proportion est plus forte qu'en P3 (76 sur 181 contre 26 sur 175) et elle se concentre sur l'**appareil** : les cinq annexes et l'avant-propos ne graduent rien.

**Issue.** **180 des 181 ont produit une correction. Une seule a été écartée**, comme infondée après constat sur pièce — ch. 22, seconde passe.

### 4.1 Six pièces ont reçu deux relectures, et la seconde n'a pas rendu moins que la première

Ch. 22, 23, 24, 25, 26 et 27. Le résultat contredit l'intuition qu'une seconde passe racle un fond :

| Pièce | Première passe | Seconde passe |
|---|---|---|
| ch. 22 | 12 | 10 |
| ch. 23 | 9 | 8 |
| ch. 24 | 9 | 8 |
| ch. 25 | 9 | 11 |
| ch. 26 | 12 | 7 |
| ch. 27 | 11 | 7 |

: Rendement comparé des deux passes de relecture, sur les six pièces qui en ont reçu deux.

**Le ch. 25 en a rendu davantage à la seconde qu'à la première**, et les cinq autres ont rendu entre 58 % et 89 % du rendement initial. ⚠ **Deux pièces déclarent en outre que leur seconde passe a trouvé une faute de la classe même que la première avait corrigée ailleurs** — le ch. 23 le nomme en toutes lettres : la première passe avait rendu à F-29 sa portée et laissé passer la même faute sur F-71, F-72 et F-73 ; le ch. 27, une faute **bloquante** de libellé d'entrée débordé, classe déjà corrigée par la première. *Une passe de relecture corrige les occurrences qu'elle voit d'une classe, non la classe.* C'est le même mécanisme qu'au §2, à un cran d'abstraction en dessous.

---

## 5. Le constat d'arborescence — soixante-huit cibles cassées en un seul `git mv`

Le 22 juillet 2026, l'auteur a renommé `doc/` en `prd/` au commit **fd8f1be** (« Phase 4 en cours »), un **`git mv` pur** — les trois documents de gouvernance sont déplacés sans une ligne modifiée.

**Mesure propre à cette passe**, exécutée sur l'état du dépôt à ce commit et **figée à ce commit**, en excluant les chaînes `doc/` internes à des URL : **68 cibles de lien relatives visaient `doc/`, réparties sur 45 fichiers.** État après repointage, mesuré sur l'arbre de travail : **zéro cible `doc/` subsistante** — cardinal qui tient —, et **82 cibles `prd/` réparties sur 46 fichiers**, relevées en fin de chaîne le 22 juillet 2026 sur un total de **393 cibles relatives, 388 résolues**. ⚠ **Ce couple se refait à chaque passe qui écrit un renvoi, et la présente passe l'a démontré contre elle-même** : la mesure du même jour, prise avant les substitutions de marqueurs, donnait 387 / 382 et 81 cibles `prd/`. La **convention de comptage** — retrait du code entre accents graves et des blocs délimités avant résolution — est posée au PRDPlan §1.3, comme R-G-51 le réclamait.

⚠ **Ce que cette section écrivait des `doc/` résiduels était faux, au cardinal comme au siège — re-mesuré et corrigé le 22 juillet 2026** sur la racine du volume, domaine entier (`grep -ro "datatracker\.ietf\.org/doc/"`). Le motif compte **19 occurrences sur 9 fichiers**, toutes des URL réelles : **17 sous `verification/`** — L-01 × 3, L-05 × 6, L-06 × 2, L-07 × 2, L-09 × 2, L-13 × 1, revalidation × 1 — **et 2 sous `monographie/`**, aux ch. 9 §9.2 et ch. 10 §10.2, l'une et l'autre citant `draft-ietf-oauth-identity-chaining`. L'énoncé antérieur — « deux occurrences, dans deux fichiers de `verification/` » — **excluait explicitement le répertoire qui en porte deux**. ⚠ *Un énoncé qui sert d'instruction — « ne pas les corriger » — n'a pas le droit de se tromper de siège : le cardinal se relit, le siège se suit.*

⚠ **Ce que ce chiffre dit, et il ne dit pas ce qu'on croit.** Le volume s'était **prémuni de ce gisement une fois déjà** : la décision **P0.3** du 18 juillet 2026 avait tranché `doc/` **avant la première pièce**, au prix de deux renvois cassés dont l'un vivait dans le **gabarit** que les 34 pièces recopient — non corrigé, il aurait produit mécaniquement 34 renvois cassés, reproduction exacte du gisement du Vol. II et de ses 48 renvois. La parade a fonctionné : **deux renvois avant la première pièce, soixante-huit après la trente-quatrième.**

*Un gabarit protège de ce que les pièces recopient ; il ne protège pas d'un déplacement postérieur.* La leçon consignée au `CLAUDE.md` du volume — le chemin relatif se vérifie à la création de chaque pièce, en l'ouvrant — **vaut d'abord pour celui qui déplace le répertoire**, et c'est le seul moment où elle ne s'applique à personne.

⚠ **Le récit de P0.3 ne se réécrit pas.** Le renommage est consigné comme un **fait daté du 22 juillet 2026** au PRD, au TOC, au PRDPlan §1.3 et sous **R-G-51** ; aucun de ces sièges n'efface que P0.3 avait choisi `doc/` le 18 juillet. *Une décision antérieure qu'un fait postérieur périme n'est pas une décision fautive ; l'effacer serait la faute.*

---

## 6. Ce que P4 n'a pas fait, et qu'aucune de ses sorties ne doit laisser croire

*Section décisive. Chaque point est constaté à son siège, non repris d'une déclaration de passe.*

1. **Le vote adversarial dû sur F-92 et F-96 n'a pas été conduit.** Le [PRD](../prd/PRD.md) §7.11 le déclare en toutes lettres — « dette déclarée, non résorbée » —, et §A.4 réserve le vote aux affirmations qui portent à elles seules la thèse d'un chapitre. **Les deux entrées sont dans ce cas, et elles fondent le ch. 26.** La parade tenue est un **marqueur ⚖ à chaque mobilisation** : douze occurrences constatées au ch. 26. *Une parade n'est pas une résorption* — si le vote fait tomber le niveau, la thèse du chapitre est en cause. Ouvert sous **R-G-44**.
2. **Le §24.4 demeure sans socle.** Le volet de corrélation de `docs/gen-ai/mcp.md` n'est instruit **ni par L-14, ni par L-14b** ; le déblocage du ch. 24 est **partiel**, et le PRD §7.6 l'écrit comme tel. La section porte un encadré de lacune renvoyant à la **lacune 21**, constaté sur pièce. ⚠ *Un déblocage partiel écrit n'est pas un arbitrage rendu.* Ouvert sous **R-G-45**.
3. **Le grain de CA-09 n'est pas tranché** (§3.1). La question est consignée au PRD §11 ; elle n'y est pas arbitrée.
4. **La Partie IX et l'appareil n'ont pas subi CA-09.** Le périmètre du contrôle est **cinq pièces**, Parties VII et VIII, et il le déclare. **Huit pièces sur treize — ch. 27, ch. 28, l'avant-propos et les cinq annexes — n'ont reçu aucun test d'appartenance.** ⚠ Ce sont, à l'exception de l'avant-propos, celles dont l'écart de volumétrie est le plus fort.
5. **La relecture dédiée CA-12 n'a été conduite sur aucune pièce de P4.** Constat sur les treize fichiers : **douze la déclarent non tenue** — neuf en en-tête, trois aux Notes ou sous la forme « n'a pas eu lieu ». ⚠ **L'annexe D n'en dit rien : zéro occurrence de « CA-12 » dans le fichier entier.** La couverture de `monographie/` par CA-12 est donc **inchangée depuis P3** — quatre pièces lues intégralement et quatre sections nommées —, et **treize pièces neuves s'y ajoutent sans contrôle**. R-12 demeure le seul garde-fou du volume sans motif de balayage : aucun décompte ne le supplée.
6. **Le rejeu des motifs de balayage du PRD §A.6 sur les 34 pièces n'a pas eu lieu.** Le PRD §A.6 déclare lui-même que les bilans publiés dans les pièces du tronc ont été **mesurés à l'instrument défectueux** et qu'aucun ne vaut attestation ; le rejeu est **ordonnancé en P5.2**. Les décomptes re-mesurés par CA-09 portent sur les seuls motifs que les coupes ont déplacés, sur les seules pièces coupées.
7. **Les remontées relevant de l'auteur demeurent, et elles se sont multipliées.** Cardinal à relever **marqueur par marqueur** sur les en-têtes de [`remontees-gouvernance.md`](remontees-gouvernance.md), en une passe unique, faite en fin de chaîne le 22 juillet 2026 : **52 remontées — R-G-01 à R-G-52, en-têtes contigus et sans doublon —, 39 tranchées, 3 sans objet (R-G-18, R-G-19, R-G-36), 10 ouvertes (R-G-43 à R-G-52)**. ⚠ S'y ajoutent les **douze arbitrages délégués de P3, révocables**, dont le report au TOC ne change pas le régime. ⚠ **Et la lacune que P3 avait nommée n'est pas réparée** : le plan n'a toujours désigné aucune instance capable de trancher la classe de remontées que §5.3 réserve à l'auteur. *P3 avait écrit qu'elle se reposerait à l'identique en J-5 ; elle s'y est reposée.*
8. **La revalidation temporelle finale (P5.1) reste due dans sa totalité.** Les sept lignes de faits chauds du PRD §8.3 n'ont pas été reprises depuis le 21 juillet 2026. Les **34 pièces portent la même date de gel — 21 juillet 2026** —, y compris celles dont les correctifs datent du 22 : le champ n'a pas été inventé, il a été conservé, et l'écart d'un jour entre le gel déclaré et le dernier correctif est consigné ici plutôt que lissé.
9. **Aucun lot n'a été rouvert, aucune divergence n'a été arbitrée.** Les deux divergences non arbitrées du PRD §7.5 — gouvernance d'AP2, date de la ligne directrice IA de l'AMF — demeurent signalées et non tranchées.

---

## 7. Ce que ce rapport ne dit pas

*Les bornes de la présente lecture. Elles sont larges, et les taire serait la faute que ce volume prend pour objet.*

1. **Ce rapport n'a relu aucune pièce.** Il porte sur les **en-têtes**, les **blocs `## Notes`**, les **trois rapports de contrôle**, les **registres** et les **documents de gouvernance**. Il n'a pas lu le corps des treize pièces de P4, et encore moins celui des vingt et une du tronc. **Il ne peut donc pas dire qu'un correctif appliqué est juste** ; il peut dire qu'il est journalisé, et que le journal est cohérent avec ce que le contrôle qui l'a produit déclare.
2. **Il n'a vérifié aucune affirmation contre sa source primaire.** Aucune spécification, aucun RFC, aucune ligne directrice, aucun rapport de lot n'a été ouvert au titre de son contenu. Les vérifications conduites portent sur des **cardinaux**, des **champs d'en-tête**, des **cibles de lien** et des **présences ou absences de chaînes** — pas sur la vérité de ce que les pièces avancent.
3. **Ce qu'il a vérifié directement, et ce que cela a produit.** Quatre contrôles ont été exécutés sur les fichiers plutôt que lus dans un rapport : la volumétrie des 34 pièces, le statut et la date de gel des 34 en-têtes, le cardinal des remontées sur les en-têtes du registre, et le gisement de liens du commit de renommage. **Trois ont démenti un chiffre qui lui avait été transmis** — dont la volumétrie du volume, et **douze pièces sur treize déclarant CA-12 non tenue là où une passe amont écrivait « les treize sans exception »**. *Le rendement d'un contrôle direct sur un chiffre transmis n'a pas décru non plus.* ⚠ **Et le chiffre que ce contrôle a substitué a été démenti à son tour** par les passes du même jour : d'où les marqueurs, et non un troisième chiffre.
4. **Deux constats de la passe corrective n'ont pas été re-vérifiés ici**, faute de porter sur un objet mesurable en l'état : que les sept reports d'arbitrage soient **fidèles à la formulation** que l'arbitrage avait écrite — seule la **présence** des sept identifiants au TOC v0.8 et **quatre libellés sur pièce** ont été constatés —, et que les onze passages d'arborescence corrigés dans dix pièces le soient **correctement**. Le second est plus exposé : *un passage qui décrit l'état d'un autre fichier se périme au premier mouvement de ce fichier, et aucun contrôle ne le signale.*
5. **La distinction rédacteur / relecteur n'est pas constatable sur disque**, non plus qu'en P3. Réserve 1 de **R-G-19**, non levée. Les six secondes passes sont déclarées confiées à des relecteurs distincts des premiers ; **ce rapport le consigne, il ne l'atteste pas.** Il en va de même du fait que les treize pièces aient tenu les points 1 à 6 de la boucle qualité : c'est une déclaration d'en-tête, lue et reportée.
6. **Aucun contrôle de propagation inter-pièces n'a été conduit, en P4 pas plus qu'en P3.** La question « la même formule, la même borne, la même entrée traitées différemment dans deux pièces » n'a été posée par personne — ni par les rédacteurs, ni par les relecteurs, ni par les trois contrôles spécifiques, ni ici. **C'est le contrôle qui avait le meilleur rendement en P3**, et il n'existe toujours dans aucun document de gouvernance.
7. **Aucun contrôle de migration entre `verification/` et `monographie/` n'a été conduit.** La question que CA-12 pose et laisse ouverte — *un élément retiré d'un rapport de lot a-t-il été recopié dans une pièce ?* — exige la lecture conjointe des deux répertoires. Elle se pose en particulier pour L-09 et L-10, dont la matière nourrit les ch. 13, 14 et 15.
8. **Les rapports L-03 et L-08 n'ont été relus par personne depuis le 21 juillet 2026**, et CA-12 le déclare : rien n'établit que les correctifs de P1.4 y tiennent toujours.
9. **Un défaut d'en-tête signalé par la présente passe a été corrigé depuis, le 22 juillet 2026** : [`theses-P4-confrontation.md`](theses-P4-confrontation.md) portait deux renvois dont le **libellé** disait `doc/TOC.md` et `doc/PRD.md` alors que la **cible** pointait correctement vers `../prd/`. Le lien résolvait ; l'étiquette mentait. C'était hors mandat de cette passe-ci ; les deux libellés sont rectifiés.
10. **Ce rapport ne clôt rien.** Il ne verse aucune entrée de socle, n'amende ni le PRD, ni le TOC, ni le plan, n'arbitre aucune remontée et ne renseigne aucun registre. **Dix remontées sont ouvertes — R-G-43 à R-G-52 —, douze arbitrages délégués demeurent révocables, deux entrées portent une dette de vote, une section demeure sans socle, un critère d'acceptation attend son grain, et le rejeu exhaustif des motifs de balayage n'a pas eu lieu.** *Trente-quatre pièces rédigées, relues et corrigées ne font pas un ouvrage publiable — elles font un ouvrage complet, ce qui est autre chose.*
