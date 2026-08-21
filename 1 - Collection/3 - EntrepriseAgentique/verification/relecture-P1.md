# Relecture adversariale de la clôture P1 — 21 juillet 2026

| Champ | Valeur |
|---|---|
| Activité | **P1.4** du [PRDPlan](../prd/PRDPlan.md) — relecture adversariale de la clôture de phase |
| Objet relu | Les deux rapports de lot ([L-03](lot-L-03-agent-card.md), [L-08](lot-L-08-attaques.md)), le [registre des remontées](remontees-gouvernance.md), et les sections du PRD qui en dérivent (§3 O6, §7.8, §8.1, §8.5, §10, §11) |
| Relecteurs | **Trois, indépendants et distincts du rédacteur** (CA-14), à lentilles disjointes : **(1) socle** — une entrée dit-elle plus que le rapport n'établit ? ; **(2) gouvernance** — les arbitrages sont-ils justifiés et complets ? ; **(3) dualité d'usage** — relecture dédiée au titre de **CA-12**, distincte de la relecture de conformité |
| Consigne | **Réfuter, non valider.** Une relecture qui ne trouve rien n'a probablement pas été faite ; une réfutation inventée est pire que rien. Chaque constat cite le passage fautif verbatim et se classe BLOQUANT / MAJEUR / MINEUR |
| Verdict | **`CLÔTURE_À_CORRIGER` — unanime sur les trois lentilles.** **7 constats bloquants**, 17 majeurs, 2 mineurs |
| Suite donnée | **Les sept bloquants sont corrigés**, ainsi que les majeurs de fond. Correctifs appliqués le jour même, avant clôture de P1 |

---

## 1. Ce que cette relecture a trouvé, et que le rédacteur n'avait pas vu

**Trois familles de fautes, et elles se ressemblent.**

**(a) Le débordement du socle par sa propre synthèse.** Quatre constats bloquants portent le même défaut : une affirmation **écartée par le vote** reparaît, reformulée, dans une réponse-titre ou une entrée de socle. La réponse à Q3 écrivait « aucun ancrage de confiance opposable, aucun régime de révocation, aucune gouvernance des clés » — trois négatifs de corpus, dont deux reprenaient la substance d'affirmations tuées 3-0. L'entrée **F-08** titrait « Aucune gouvernance des clés publiée » là où son balayage ne couvrait **qu'un fichier**. La réponse à Q2 posait « il n'existe pas d'attaque propre à A2A », que l'axe qui l'avait produite déclarait pourtant être « une faute » d'écrire.

⚠ **Le mécanisme est instructif : le vote protège les affirmations, il ne protège pas la prose qui les résume.** Chaque synthèse a réintroduit, par commodité d'écriture, l'universalité que le vote venait de retirer. *La règle que le lot L-03 avait lui-même dégagée — un fait négatif borné tient, un fait négatif de corpus tombe — s'appliquait d'abord à son propre §1.*

**(b) L'escalade du verbe le long de la chaîne documentaire.** Le rapport écrivait « ne soutient pas » ; la remontée R-G-03 écrivait « n'est pas soutenue » ; le PRD écrivait « **a réfuté** ». Trois documents, trois crans de plus en plus forts, aucun fait nouveau entre eux. Le relecteur l'a nommé pour ce que c'est : **un décompte d'intitulés ne réfute pas un décompte d'attaques**. Corrigé partout en « non soutenue ».

**(c) Le contrôle qui ne couvrait pas le fichier où la faute s'est produite.** R-12 et CA-12 visaient « la Partie IV » — des chapitres dont aucun n'est écrit —, alors que **toute la matière offensive de P1 vit dans `verification/`**. Conséquence directe : trois passages opératoires ont été déposés dans un dépôt public, et l'en-tête du rapport les couvrait d'une attestation auto-délivrée — « aucune procédure d'attaque n'y figure » — **fausse sur pièce**.

## 2. Les sept constats bloquants et leur traitement

| # | Lentille | Constat | Correctif appliqué |
|---|---|---|---|
| 1 | socle | **F-08** restaure au socle un négatif de corpus écarté 3-0, et l'élargit encore | Entrée **retitrée** sur son objet réel — le `SECURITY.md` — ; le corpus non spécifié renvoyé à F-11, en [B] |
| 2 | socle | **PRD §10, lacune 2** pose en gras l'affirmation écartée, puis **interdit deux lignes plus loin** qu'elle resurgisse | Réécrite en **deux énoncés de degrés distincts** : degré 1 pour le vocabulaire de la spécification, **degré 3** pour l'absence d'identifiant |
| 3 | socle | **Rapport L-08 §1** : la réponse-titre reprend deux affirmations écartées et **contredit sa propre section D** | Reformulée au degré 3, bornée au corpus consulté ; la contradiction est consignée dans la pièce |
| 4 | dualité | **Citation opératoire** : un verbatim de fiche de vulnérabilité livrait produit, versions, chemin du point d'entrée **et l'opération à effectuer** | Citation **tronquée avant la clause opératoire**, chemin retiré des quatre emplacements ; le constat architectural, qui porte tout, est conservé |
| 5 | dualité | **Attestation R-12 auto-délivrée**, fausse sur pièce, adossée à aucun contrôle consigné — alors que CA-14 l'interdit en toutes lettres | Cellule réécrite pour dire **ce qui a réellement été fait** : relecture dédiée, par qui, à quelle date, **trois passages retirés**. Le présent compte rendu en est la trace |
| 6 | gouvernance | **PRDPlan §3.1** prescrivait une élévation de H-31 que **R-G-02 déclarait impossible le même jour** — l'artefact qui clôt J-2 portait la consigne fautive | §3.1 aligné sur le régime tranché ; **R-G-02 doté d'une section « Report »** |
| 7 | gouvernance | Les trois remontées ont été **ouvertes et tranchées par la même instance**, sans que la règle d'escalade désigne d'arbitre | **PRDPlan §5.3 complété** : instance d'arbitrage désignée, et **seuil de remontée à l'auteur** posé. ⚠ Constat conservé : **R-G-03 relevait de ce seuil et a été tranchée en deçà** |

## 3. Les majeurs de fond, corrigés

- **R-13 : la parade de remplacement était elle-même inopérante.** Elle imposait « fichier + section + cardinal » — or **deux des trois échelles comptent quatre niveaux**. Le discriminant réel est la **numérotation**. Règle corrigée au PRD et au PRDPlan, troisième formule complétée.
- **R-13 : l'interdiction sans son instrument.** R-G-01 interdisait « copilote » employé seul, et le motif de balayage ne contenait pas la chaîne — alors que R-04, invoqué comme modèle, porte bien `\bACP\b`. **`copilote` ajouté au motif**, et la note de clôture de §A.6 amendée pour dater l'ajout.
- **F-03 excédait son balayage** : « une signature ne périme pas » contredisait F-07 du même socle. Qualificatif rétabli.
- **Les Réserves étaient tronquées à la génération** — 36 lignes en L-08, 23 en L-03 —, et coupées **précisément sur les six entrées offensives**, en plein milieu des clauses qui **bornent** l'exposition. ⚠ *Résultat exactement inverse de l'intention : la matière restait, le bornage disparaissait.* Annexes **régénérées avec les réserves intégrales**.
- **R-G-02 portait un quantificateur universel faux** (« les huit réaffectations pointent toutes vers des entrées héritées » — l'annexe E pointe vers un ouvrage externe). Borné à sept sur huit. *Une leçon de gouvernance qui viole la règle qu'elle vient d'apprendre n'est pas opposable.*
- **Champs d'état périmés** : le TOC affirmait « aucun socle F-xx constitué » deux lignes au-dessus d'une thèse citant F-18 ; le chapeau du PRD §10 affirmait « aucune n'est instruite » au-dessus de quatre clôtures datées. Les deux redatés.
- **Vecteur exposé à demi** : une technique publiée nommant A2A était citée sans entrer au socle ni être déclinée. **Tranché** : caractérisée au seul niveau architectural, entrée refusée en l'état, décision reportée au ch. 12.
- **§12.4 du TOC** portait encore l'absence générale d'incident, que le vote a écartée. Réécrit sur l'objet restreint.

## 4. Ce que les relecteurs ont tenté de casser sans y parvenir

*Consigné parce qu'une relecture qui ne rapporte que ses trouvailles ne permet pas de juger de sa profondeur.*

- **Le cœur factuel de R-G-01 tient.** Les trois échelles existent, aux sièges annoncés, avec les cardinaux annoncés : le relecteur a rouvert les fichiers du Vol. I et vérifié un à un les paliers, les niveaux et les libellés.
- **Le traitement des vulnérabilités d'injection indirecte est exemplaire**, et le relecteur a explicitement tenté d'en dériver une attaque sans y parvenir : identifiant, date, vecteur, énoncé strictement architectural, et refus déclaré d'affirmer quoi que ce soit sur le mécanisme.
- **Les deux entrées académiques les plus sensibles sont correctement bornées** : les taux d'efficacité sont publiés sans la méthode d'optimisation, et le relecteur a vérifié qu'aucun paramètre ni seuil ne figurait ailleurs dans le fichier.
- **Le lot L-03 est indemne sous la lentille de dualité d'usage.** Sa carte des défaillances est intégralement tirée du texte normatif public ; le seul vecteur qui exigerait une recette est **nommé et déclaré non instruit** — geste correct, fait **sans que R-12 l'y oblige**.
- **Le socle du §7.8 ne porte aucun élément opératoire** : la contamination était confinée aux rapports de lot. *C'est ce qui rend le verdict « à corriger » et non « non défendable ».*
- **La réarticulation R-G-03 ne dissimule aucune affirmation offensive** et la restriction corrélative de R-08 est correctement dérivée de F-21.

## 5. Verdict après correctifs

**P1 est close.** Les sept bloquants sont traités, les majeurs de fond aussi. Deux constats sont **conservés comme dette déclarée** plutôt que corrigés :

1. **R-G-03 a été tranchée en deçà de son seuil.** Le correctif de règle est posé (PRDPlan §5.3) ; l'arbitrage lui-même n'est pas défait, il est **signalé**. Un auteur qui le renverserait ne heurterait aucun texte.
2. **Quatre entrées de F-26 portent un vote incomplet** — cinq juges perdus sur erreur de connexion. Elles restent en **[B]**, à revalider avant tout emploi central. *Vote incomplet n'est pas vote favorable.*

⚠ **Ce que cette relecture démontre, et qui vaut pour toute la suite** : le vote adversarial a protégé **les affirmations**, et c'est **la prose qui les résume** qui a réintroduit ce qu'il avait retiré. La boucle qualité du §5.2 place la relecture adversariale au point 5, après l'auto-contrôle du point 3 — *l'ordre est le bon, et c'est ici la démonstration que le point 3 ne remplace jamais le point 5*.
