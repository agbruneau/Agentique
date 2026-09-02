# Audit intégral du compendium et plan d'exécution des correctifs

*Audit conduit le 2 septembre 2026 sur l'arbre de travail du dépôt (branche `main`, dernier commit `c81be4a`). Périmètre : le dossier `2 - Compendium/` en totalité, c'est-à-dire les cinquante chapitres des cinq Livres, leurs rendus `.html`, les cinq `README` de Livre, le `README` du dossier, le `PRD/` (PRD, TOC, socle consolidé, registres de gel, contrôles et harnais de mutation), `figures/`, `build/`, les deux annexes présentes et le PDF composé.*

---

## 1. Résumé

Le compendium est **clos et déclaré tel** (D-13 du 8 août 2026, rouvert une fois pour le titre par D-14 le 25 août). Les cinquante pièces sont rédigées, cohérentes entre elles au grain des renvois de section, et **honnêtes sur leur propre inachèvement** : chaque pièce déclare ses portes non franchies, ses énoncés non centraux et ses remontées. L'audit ne remet pas ce jugement en cause.

Ce qu'il trouve, en revanche, est de trois ordres :

1. **Trois défauts d'appareil qui font mentir le dépôt sur lui-même** : un harnais de mutation dont une mutation n'est plus applicable, une vérification de bibliographie qui échoue, et cinquante rendus `.html` périmés depuis le 31 juillet alors que le contrat du dépôt veut que `.md` et `.html` soient versionnés ensemble.
2. **Une vingtaine d'incohérences vérifiables entre pièces d'appareil** (métadonnées de version, volumétries, en-têtes de tables du plan, sièges à contrôle partiel, tableau de péremption) : toutes petites, toutes datées, aucune arbitrée depuis la clôture.
3. **Des remontées de fond restées sans arbitrage** et des **événements de péremption échus depuis le gel** : le protocole du ch. 50 (§ 50.3) exige une revalidation de moins de trente jours avant publication ; au 2 septembre 2026, trois échéances du tableau 50.1 sont passées et une quatrième tombe le lendemain.

Le plan d'exécution (§ 4) sépare ce qui se corrige sans rouvrir la clôture (appareil, métadonnées, volumétrie, rendus) de ce qui exige une décision d'auteur (fond, péremption, annexes). **Toute modification du dépôt après D-13 doit être portée par une décision datée** (D-15), comme D-14 l'a fait pour le titre.

---

## 2. Méthode

**Ce qui a été lu intégralement** : les 50 chapitres (3 497 428 caractères), `PRD/PRD.md` (v0.18), `PRD/TOC.md` (v0.34) dont les journaux v0.3 à v0.31, `PRD/socle-consolide.md` (v1.2), `PRD/registre-gel.md`, les registres de gel du 27 et du 28 juillet, les six `README`, `APPAREIL.md`, les scripts de `PRD/`, `figures/genere.py` et `contenu1-6.py`, `build/assemble.py`, `build/assemble-bibliographie.py`, `build/build-pdf.sh`, `compendium.template`, `echantillon.py`.

**Ce qui a été rejoué** (sorties du 2 septembre 2026) :

| Contrôle | Résultat |
|---|---|
| `PRD/check-toc.py` | OK, C1 à C15 |
| `PRD/check-toc-mutations.py` | **KO** : M14 inapplicable, « des mutations échappent au script », code de sortie 1 |
| `PRD/check-sieges.py` | OK, 26 sièges sur 50 pièces |
| `PRD/check-sieges-mutations.py` | OK, 108 mutations vues |
| `PRD/check-compendium.py` | OK, P1 à P8, 3 rapports déclaratifs (P5) |
| `PRD/check-compendium-mutations.py` | OK, 17 mutations vues |
| `build/assemble-bibliographie.py --verifier` | **ÉCHEC** : « annexe-bibliographie.md ne correspond plus à ses sources », code 1 |
| `figures/genere.py --verifier` | OK, 115 figures gravées sur 49 pièces, 3 antérieures vérifiées |
| `PRD/decompte.sh` sur les 50 pièces | 331 791 mots au total |

**Ce qui n'a pas été fait** : aucune reprise de fait à sa source primaire, aucune collation de fond contre les volumes sources (G-4), aucune lecture des trois monographies. L'audit porte sur la cohérence interne du compendium et sur son appareil, pas sur la vérité de ses énoncés. Les constats marqués « vérifié » ont été constatés sur pièce ou par commande ; ceux marqués « à confirmer » sont des déductions à trancher par l'auteur.

---

## 3. Constats

Gravité : **B** bloquant (l'appareil est faux ou casse), **M** majeur (incohérence vérifiable entre pièces d'appareil), **m** mineur (forme ou trace), **D** déclaré (dette de fond déjà consignée par le dépôt, rappelée ici pour le plan).

### 3.1 Appareil et contrôles

| # | Gr. | Constat (vérifié) | Preuve rejouable |
|---|---|---|---|
| C-01 | B | Le harnais `check-toc-mutations.py` cherche pour M14 la rangée « Source » du `README` sous sa forme « TOC.md v0.33 (8 août 2026) », absente depuis la v0.34. La mutation est inapplicable et le bilan déclare que des mutations échappent au script (code de sortie 1). `APPAREIL.md` à la racine du dépôt (ligne 52) affirme encore « sortie 0, 23 sur 23 » et note que l'ancre avait été refixée le 21 août : la v0.34 du 25 août (D-14) l'a cassée une seconde fois, ce qui montre qu'une ancre portant un numéro de version se périme à chaque révision du plan. | `cd PRD && python check-toc-mutations.py` |
| C-02 | B | `build/assemble-bibliographie.py --verifier` échoue : le générateur émet un lien vers `audit-references.md`, fichier supprimé, alors que `annexe-bibliographie.md` versionné a été corrigé à la main. L'annexe I n'est plus reproductible. | `python build/assemble-bibliographie.py --verifier` |
| C-03 | B | Les 50 `.html` datent de la dernière génération du 31 juillet (commit `4b3e5fc`) : 114 des 115 figures en sont absentes, les révisions du 31 juillet au 3 août et du 8 août n'y sont pas, les commits `.html` ultérieurs sont des substitutions globales. Le rendeur (`rendre-piece.py`, `verifier-piece.py`) a été retiré le 31 juillet : la règle « `.md` et `.html` versionnés ensemble » est inapplicable. Les défauts du rendeur signalés par le ch. 28 y subsistent : 282 balises `<strong><em>` croisées sur 26 pages, 4 libellés de lien réduits à un nombre sur 3 pages. | `grep -L 'figures/' Livre*/*.html`, comptage regex |
| C-04 | M | `check-compendium.py` ligne 366, garde de P3 : `"Vol. II" in b and "Vol. III" in b`. « Vol. II » étant préfixe de « Vol. III », la garde est vraie pour toute pièce ne citant que le Vol. III. Signalé par le ch. 18 le 28 juillet, jamais corrigé. P3 est déclaratif, l'effet est un rapport faux, non un échec manqué. ⚠ **Corrigé en phase 0, et l'audit avait sous-estimé la portée** : *ce constat disait « rapport faux » sans le chiffrer, et la mesure a été faite sur le fichier entier avant de l'être sur `corps()`, seul domaine du script.* **Le rapport passe de 674 emplois sur 29 pièces à 524 sur 26** — sortent les ch. 13 (2 emplois), 18 (44) et 21 (104), qui ne relèvent pas du Vol. II. **Le cardinal « 670 » que le PRD §7.1 cite quatre fois est le nombre du garde-fou fautif**, et il reste écrit là où il est daté. | lecture du script, puis mesure |
| C-05 | M | `check-sieges.py` : 7 sièges sur 26 ont `"renvoi": None` (S5 désactivé) : irréversibilité § 31.1.1, risque systémique § 31.1.2, quatre-yeux § 31.3.4, tri prospectif § 49.0, verrou sémantique § 49.6, cinq points de contrôle § 43.3, modèle de maturité § 43.5. Trois motifs sont **périmés** : le quatre-yeux (« aligner le ch. 44 » : le ch. 44 § 44.1.7 nomme le siège, ligne 771) ; le tri prospectif (« aligner ch. 19 et 20 » : le ch. 20 le cite 5 fois, seul le ch. 19 reste à 0). Deux motifs **tiennent** : le ch. 49 § 49.9 et § 49.11.3 consomment la matière des deux sièges du § 31.1 sans nommer le ch. 31 (0 occurrence de « ch. 31 » dans le ch. 49). | grep sur les pièces ; `grep -n '"renvoi": None' PRD/check-sieges.py` |
| C-06 | M | Le ch. 43 § 43.3 nomme « ch. 39 § 39.2, siège » ; aucun siège de ce nom n'est déclaré au TOC ni versé à `check-sieges.py` (0 occurrence de « 39.2 » dans le script). Remonté par la relecture du ch. 39, non arbitré. | `grep -c '39\.2' PRD/check-sieges.py` |
| C-07 | M | Aucun contrôle ne refuse un identifiant de remontée `R-IV-nn` en double (R-IV-75 soldée à moitié, PRD §13 écrit la règle, `check-compendium.py` ne contient aucun motif `R-IV`). | `grep -c 'R-IV' PRD/check-compendium.py` → 0 |
| C-08 | m | `build/build-pdf.sh` dégrade la porte des 1000 pages en avertissement quand `pypdf` manque ; `echantillon.py` importe `fitz` non déclaré ; `echantillon.template` est périmé par rapport à `compendium.template`. | lecture des scripts |
| C-09 | m | Les déclencheurs de `check-sieges.py` sont compilés sans `re.IGNORECASE` (0 occurrence). Sans effet constaté : les signatures sont écrites en minuscules dans les pièces. | grep |
| C-10 | m | P5 de `check-compendium.py` rapporte trois pièces dont les cardinaux d'en-tête ne se reproduisent pas sous sa règle (ch. 48 « R-14 » déclaré 9, mesuré 2 ; ch. 49 « R-11 » 22 contre 2, « R-14 » 19 contre 1). Le dépôt le sait (décision 16c : « domaine déclaré, sans cardinal »), mais l'en-tête de ces pièces annonce des cardinaux que le seul instrument du dépôt ne sait pas relire. | `cd PRD && python check-compendium.py` |

### 3.2 Métadonnées, plan et registres

| # | Gr. | Constat (vérifié) | Où |
|---|---|---|---|
| C-11 | M | `PRD.md` : rangée `Date` encore au 8 août / v0.17 alors que `Version` est v0.18 ; §9 ligne 161 écrit « P1-P7 » et « 15 mutations » (le script a P1 à P8 et 17 mutations ; les lignes 28 et 475 du même PRD écrivent P1-P8). ⚠ **Ce constat portait un troisième grief, et il était faux** : *« §1 cite TOC v0.32 alors que le TOC est en v0.34 ».* Vérifié en phase 1, la rangée `Version` du PRD **cite bien la v0.34** ; les mentions « (v0.32) » sont des **attributions historiques** — la décision 18 a été prise sous cette version du TOC — et les corriger effacerait la seule chose qu'elles apportent. **Elles n'ont pas été touchées.** | `PRD/PRD.md:5`, `:23`, `:161` |
| C-12 | M | `TOC.md` : rangées `Date` et `Statut` non mises à jour pour la v0.34 ; l'entrée « Annexe B » du plan écrit « socle (v1.0) » alors que le socle est en v1.2 ; l'en-tête du socle dit que le PRD cite la v1.0. | `PRD/TOC.md` en-tête ; `PRD/socle-consolide.md` en-tête |
| C-13 | M | `registre-gel.md` ligne 25 écrit « le volet résiduel de G-1 n'est pas levé » ; le PRD §5 déclare le volet de faits levé le 28 juillet. Remonté par le ch. 50, non arbitré. | `PRD/registre-gel.md:25` |
| C-14 | M | Volumétrie : les 50 en-têtes (« Réel ») et `registre-gel.md` (Σ 324 817) portent des mesures antérieures aux relectures des 28 au 30 juillet ; la mesure courante donne 331 791. Les cinq `README` de Livre sont, eux, à jour. P6 couple le registre aux en-têtes : les deux se corrigent ensemble ou pas du tout. Exemples : ch. 49 en-tête 14 188, mesuré 14 373 ; ch. 50 en-tête 4 649, mesuré 4 709. | `bash PRD/decompte.sh Livre*/[0-9]*.md` |
| C-15 | M | TOC : 45 des 58 en-têtes « Table des matières détaillée du chapitre N » portent l'ancienne numérotation (écart +1 au ch. 12 à +7 au ch. 50 ; les 13 concordants sont les ch. 1 à 12 et le ch. 41). Déclaré exclu du remappage au journal v0.22, mais remonté comme « désalignement interne au plan » par les ch. 26, 28, 30, 36 et 39, chaque fois avec la demande de trancher « d'un seul geste ». Aucun des quinze contrôles ne le voit. | balayage `### Chapitre N` / titres de table |
| C-16 | M | TOC, table de couverture du ch. 14 (ligne 975) : renvoie à « ch. 25 § 25.1 » et déclare « les deux chapitres cibles ne sont pas rédigés » ; la grille est reçue au ch. 25 § 25.4 et au ch. 27 § 27.5, tous deux rédigés. | `PRD/TOC.md:975` |
| C-17 | M | TOC, entrée du ch. 30 : « retiré le RGPD de son ch. 19 » (deux fois) et « ch. 20 du Vol. III » dans le même bloc ; les ch. 27 et 30 rédigés retiennent ch. 20. Remonté par le ch. 30, non arbitré. | entrée ch. 30 |
| C-18 | m | TOC, entrée du ch. 44 : « ici il en suit quarante-deux » ; le ch. 44 suit quarante-trois chapitres. Remonté par le ch. 44, non corrigé. | entrée ch. 44 |
| C-19 | m | Défauts de colonnes de tableau : `PRD.md` ligne 12 et `TOC.md` ligne 19 (colonne vide surnuméraire en fin de rangée), ch. 49 ligne 13 (pipes dans un span de code : pandoc tient, GFM casse). | lignes citées |
| C-20 | m | `Livre III/README.md` ligne 337 date la clôture de R-IV-99 à « TOC v0.26 » ; le journal v0.27 l'enregistre. `Livre V/README.md` porte encore une remontée sur « quatre horloges » au § 47.8 déjà résolue en v0.29. | `Livre III/README.md:337` |
| C-21 | m | La recomposition du PDF du 26 août (commit `56cfbfb`, 13 164 965 octets, nouveau bandeau) n'est déclarée qu'au `README` racine, ni au `README` du compendium, ni au PRD, ni au TOC. | `git show 56cfbfb --stat` |
| C-22 | m | Livre IV : `## Synthèse` (h2) là où les quatre autres Livres écrivent `### Synthèse`. Sans effet sur les contrôles, effet sur la table des matières du PDF. | grep `^## Synthèse` |
| C-23 | m | Le ch. 4 (note) cite `eval.html` ; les ch. 7 et 10 citent un « skill de rédaction » ; les deux objets sont supprimés du dépôt. Le ch. 47 (R-IV-63) renvoie au « gabarit » du même skill. Déclarés irrésolubles par les pièces. | grep |
| C-24 | m | Le ch. 18 § 18.1 et sa signature dans `check-sieges.py` écrivent « Fondation d'identité ouverte » ; le ch. 30 § 30.3.3 écrit « OpenID Foundation ». La décision 15b (nommer l'attributeur) et le PRD Vol. II §8.4 (neutralité) sont en tension déclarée au ch. 30, non arbitrée. Sans effet sur le contrôle. | grep des deux formes |

### 3.3 Remontées de fond non arbitrées (vérifié : absentes du PRD et du TOC)

| # | Gr. | Constat | Origine |
|---|---|---|---|
| C-25 | M | Le tableau 50.1 (onze événements) n'inclut ni l'étape parlementaire de C-36 (ch. 26, objet d), ni les suites de la consultation 11-348 (ch. 28), ni le retrait annoncé de l'Assistants API au 26 août 2026 (ch. 9). Les trois demandes « inscrire ou motiver l'exclusion » sont sans réponse ; 0 occurrence des trois objets dans le ch. 50. | ch. 26 § 26.4, ch. 28 § 28.4, ch. 9 |
| C-26 | M | R-IV-110 (subdivision du § 35.8 à arbitrer), R-IV-111 (critère dette d'outillage / refus d'accès au registre du résiduel), R-IV-112 (volumétrie multi-sites) : numéros proposés par le ch. 35, jamais alloués, 0 occurrence au PRD et au TOC. | ch. 35 § 35.10 |
| C-27 | M | R-IV-69 se rouvre : la thèse du ch. 49 second mouvement dit « lacunes des trois socles sources » ; le TOC v0.26 écrivait qu'elle « redeviendra celle du socle consolidé quand G-3 sera franchie ». G-3 est franchie depuis le 28 juillet ; seule la v0.26 mentionne R-IV-69. Le registre du § 49.12 n'a jamais été rapproché d'un `S-nnn`. | ch. 49 § 49.15 |
| C-28 | m | PRD §7.1 compte « six » affirmations hors corpus au ch. 5 du Vol. I et les assigne au seul ch. 34 ; la relecture du ch. 36 en mesure onze, dont celles du §5.13.3 qui atterrissent au ch. 36. À confirmer sur le Vol. I. | ch. 36 § 36.6 |
| C-29 | m | Socle : le ch. 22 signale un intervalle « treize mois après le dépôt » pour S-035 (préimpression du 30 juin 2026) ; la ligne S-035 du socle ne porte plus ce libellé (grep négatif). Résolu ou reformulé : à confirmer. | ch. 22 |
| C-30 | m | ch. 33 : le cardinal « quatre cibles successives » (R-4 du Vol. II) n'est attesté que par la presse (contrôle du 30 juillet) ; la remontée à l'instance Vol. II reste ouverte. | ch. 33 § 33.2 |

### 3.4 Dettes déclarées par le dépôt (rappelées pour le plan)

| # | Constat | Portée |
|---|---|---|
| C-31 | **Péremption échue depuis le gel**, dépôt clos : ratification MCP du 28 juillet (payée le 30 juillet) ; By-law no 10 du rail temps réel en vigueur le **24 août 2026** ; clôture des commentaires du règlement bancaire le **26 août 2026** ; retrait de l'Assistants API le 26 août (ch. 9) ; expiration d'un document d'identité de charge de travail le **3 septembre 2026** ; documents du ch. 18 expirant les 27 septembre et 24 novembre 2026 ; cible RTR au T4 2026 ; jetons de transaction le 7 janvier 2027 ; E-23 et AMF le 1ᵉʳ mai 2027. Le § 50.3 impose une revalidation de moins de trente jours avant publication (CA-IV-04). | ch. 50 § 50.2-50.3, ch. 32, ch. 33, ch. 18 |
| C-32 | Appareil du plan non rédigé : avant-propos (~4 000 mots, TOC ligne 126) et annexes A (méthode), D (chronologie), E (glossaire), F (matrice), G (patrons), H (ADS Boréalis). Existent : Annexe B (`socle-consolide.md`), Annexe C (dans le TOC), Annexe I (`annexe-bibliographie.md`) et une annexe hors plan non lettrée (`annexe-references.md`). Les renvois des pièces vers E, F, G, H et vers l'avant-propos (ch. 18 § 18.3, ch. 20 § 20.9, ch. 31 § 31.0) sont des renvois de plan permanents. Le `README` racine projette « 9 annexes ». | TOC lignes 3084-3147 |
| C-33 | Ré-adossement `S-nnn` jamais fait (PRD §7.1 l'écarte) : 91 des 159 entrées citées, 674 emplois nus `F-xx`/`H-xx` (CA-IV-09 mesuré par P3). | PRD §7.1, P3 |
| C-34 | Portes G-4 (volet de fond), G-5, G-6 ouvertes ; CA-IV-11 et CA-IV-13 insatisfaisables (D-6) ; D-3 : trois lots L1-L3 ouverts, publication du premier mouvement du Livre V bloquée ; D-8 : ch. 41 maintenu sous réserve, retrait possible ; R-IV-101 bloque la publication du § 44.1.9 et, par dépendance, du ch. 45 (préalable C260 non tenu) ; J-IV-7 (cinquième horloge contre ch. 37-40) et J-IV-8 (§ 48.4) non exécutés. | PRD §5, §12, §16 |
| C-35 | Le harnais (couche d'exécution, risque 14) n'a de chapitre nulle part ; D-2 l'a borné par deux sections d'atterrissage ; le tableau 50.1 n'a aucune ligne pour lui. | ch. 47 § 47.8.1, ch. 50 § 50.2 |

---

## 4. Plan d'exécution

### 4.1 Cadre

- **Une décision d'auteur préalable, D-15**, datée, qui rouvre le dépôt pour un périmètre nommé (au minimum les phases 0 à 3) et le referme par un nouveau D-13. Sans elle, chaque commit contredit la clôture. Le précédent est D-14.
- **Une passe unique par famille**, jamais pièce par pièce : c'est la règle que les pièces répètent pour la volumétrie, le ré-adossement et les en-têtes de table.
- **Ordre imposé** : appareil (phase 0) avant tout, puisque c'est lui qui atteste les phases suivantes ; rendus (phase 3) en dernier, puisqu'ils projettent l'état final des `.md`.
- **Critère de sortie commun** : les six contrôles du § 2 passent, `assemble-bibliographie.py --verifier` passe, `genere.py --verifier` passe, et chaque commit nomme la décision qui l'autorise.

### 4.2 Phase 0 : appareil (préalable, sans effet sur le fond)

| Tâche | Constats | Geste | Critère de sortie |
|---|---|---|---|
| 0.1 | C-01 | Réancrer M14 sur un motif indépendant du numéro de version (par exemple la rangée `Source` du `README` reconnue par expression régulière sur « TOC.md v0.NN »), rejouer le harnais, réaligner la ligne 52 d'`APPAREIL.md` à la racine. | `check-toc-mutations.py` : toutes les mutations vues, code 0 |
| 0.2 | C-02 | Faire émettre par `assemble-bibliographie.py` le lien vers `annexe-references.md` (ou retirer le lien), régénérer, comparer au fichier versionné, committer les deux ensemble. | `--verifier` : OK |
| 0.3 | C-04 | Remplacer la garde P3 par un test de frontière (`re.search(r"\bVol\. II\b(?!I)", b)`), ajouter la mutation correspondante au harnais. | `check-compendium-mutations.py` : 18 mutations vues |
| 0.4 | C-05 | Réactiver S5 pour le quatre-yeux (`"renvoi": r"ch\.\s*31\b"`) ; pour le tri prospectif, aligner le ch. 19 puis réactiver ; pour § 31.1.1 et § 31.1.2, ajouter le renvoi au ch. 49 § 49.9 et § 49.11.3 puis réactiver ; documenter les trois motifs restants (§ 49.6, § 43.3, § 43.5) avec leur condition de levée. Rejouer le harnais. | `check-sieges.py` OK ; au plus 3 `renvoi: None`, chacun motivé |
| 0.5 | C-06 | Décider si § 39.2 est un siège : le verser à la table avec signature et déclencheur, ou retirer le mot « siège » du ch. 43 § 43.3. | cohérence ch. 43 / table |
| 0.6 | C-07 | Ajouter à `check-compendium.py` un motif P9 : unicité des identifiants `R-IV-nnn` sur les 50 pièces, avec mutation. | P9 passe, mutation vue |
| 0.7 | C-08, C-09 | Déclarer `pypdf` et `fitz` dans un `requirements.txt` de `build/` ; faire échouer `build-pdf.sh` si `pypdf` manque ; réaligner ou supprimer `echantillon.template`. `IGNORECASE` : ne rien changer, consigner. | `build-pdf.sh` refuse sans `pypdf` |
| 0.8 | C-10 | Choix d'auteur : soit ramener les trois en-têtes (ch. 48, 49) à la règle littérale de P5, soit faire porter à P5 la mention « domaine déclaré » pour les exempter. Ne pas laisser un cardinal que l'instrument contredit. | P5 : 0 rapport déclaratif, ou exemption écrite |

Dépendances : 0.1 à 0.3 indépendantes ; 0.4 et 0.5 après relecture des pièces touchées ; 0.6 avant toute nouvelle allocation de remontée (phase 4).

### 4.3 Phase 1 : métadonnées et plan (un commit, une décision)

| Tâche | Constats | Geste |
|---|---|---|
| 1.1 | C-11 | PRD : `Date` à la v0.18 ; §1 « TOC v0.34 » ; §9 « P1-P8, 17 mutations » ; §7.1 recompter les affirmations hors corpus après lecture du ch. 5 du Vol. I (C-28). |
| 1.2 | C-12 | TOC : `Date`, `Statut`, entrée Annexe B « v1.2 » ; socle : en-tête aligné. |
| 1.3 | C-13 | `registre-gel.md` ligne 25 : nommer le volet (« volet de faits levé le 28 juillet ; volets de pièce et de relèves dus »). |
| 1.4 | C-15 | Trancher d'un seul geste les 45 en-têtes de table : soit les remapper sur la numérotation courante (recommandé, avec un contrôle C16 dans `check-toc.py` qui apparie le titre de table à l'entrée qui le porte), soit les déclarer « cartes de correspondance » dans une note unique du TOC et les préfixer d'une marque lisible. |
| 1.5 | C-16, C-17, C-18 | TOC : couverture du ch. 14 (§ 25.4 et § 27.5, « rédigés ») ; entrée ch. 30 (ch. 19 ou ch. 20, une seule forme) ; entrée ch. 44 (« quarante-trois »). |
| 1.6 | C-19, C-22 | Colonnes de tableau (3 lignes) ; normaliser `### Synthèse` au Livre IV ou déclarer l'écart. |
| 1.7 | C-20, C-21 | `README` Livre III (v0.27), Livre V (retrait de la remontée résolue) ; déclarer la recomposition du 26 août au `README` du compendium et au journal du TOC. |
| 1.8 | C-24 | Décider la règle : un attributeur qui est un organisme de normalisation se nomme (15b) ; aligner ch. 18 § 18.1 et la signature dans `check-sieges.py` dans le même commit, puis rejouer le harnais. |

Critère de sortie : `check-toc.py`, harnais, `grep` des versions citées cohérents (une seule version du TOC, du PRD et du socle citée partout).

### 4.4 Phase 2 : volumétrie (un commit, après toute édition de corps)

| Tâche | Constats | Geste |
|---|---|---|
| 2.1 | C-14 | Une invocation unique de `PRD/decompte.sh` sur les 50 pièces ; report dans les 50 champs « Réel » des en-têtes, dans `registre-gel.md` et dans les cinq `README` de Livre, le même commit. |
| 2.2 | C-14 | Rejouer P6 (registre contre en-têtes) et ajouter, si absent, un motif qui oppose le registre à la mesure elle-même (P6 ne voit aujourd'hui qu'une copie contre une copie). |

Cette phase se rejoue **après la phase 4** si celle-ci touche des corps.

### 4.5 Phase 3 : rendus HTML et PDF

Deux options, à trancher dans D-15 :

- **Option A, régénérer** : réécrire un rendeur minimal (pandoc suffit, le template existe) qui produit les 50 `.html` depuis les `.md` courants, y compris les figures ; corriger au passage les deux classes de défauts du rendeur retiré (balises croisées, libellés de lien en span de code) ; ajouter un contrôle de parité `.md`/`.html` au titre et à la figure près (le ch. 48 documente un bloc omis silencieusement par l'ancien générateur). Puis recomposer le PDF et déclarer sa taille.
- **Option B, retirer** : supprimer les 50 `.html`, amender la règle « versionnés ensemble » au PRD et au `CLAUDE.md` du dossier, et déclarer le PDF seul rendu de référence.

L'option A est la seule compatible avec la règle actuelle du dépôt ; l'option B est la moins coûteuse et la plus honnête si personne ne consomme les `.html`. Dans les deux cas : les `.html` actuels ne doivent pas rester dans l'état où ils sont, ils présentent un texte que le `.md` ne dit plus.

### 4.6 Phase 4 : fond et péremption (décisions d'auteur, chacune datée)

Ces tâches rouvrent la clôture au sens du PRD §16 et ne se font pas sans décision. L'audit les ordonne par coût croissant et par dépendance.

| Tâche | Constats | Décision attendue |
|---|---|---|
| 4.1 | C-25 | Tableau 50.1 : inscrire C-36, la consultation 11-348 et le retrait de l'Assistants API, ou écrire le motif de leur exclusion en légende. |
| 4.2 | C-26 | Allouer R-IV-110 à R-IV-112 (après 0.6) et les solder : subdivision du § 35.8 admise ou retirée ; critère « dette d'outillage / refus d'accès » porté au registre du résiduel ; volumétrie multi-sites couverte par la phase 2. |
| 4.3 | C-27 | Thèse du ch. 49 second mouvement : la rendre au « socle consolidé » et refaire le registre du § 49.12 contre les `S-nnn`, ou maintenir « trois socles sources » et l'écrire au journal. |
| 4.4 | C-31 | **Revalidation post-gel** : porter à leur source les événements échus (24 août, 26 août, 3 septembre 2026, retrait Assistants) et ceux qui tombent avant toute republication (27 septembre, 24 novembre, T4 2026), amender le socle d'abord puis les pièces (§ 50.3), re-dater les pièces touchées (ch. 9, 18, 32, 33, 36, 46, 50), et redéclarer le seuil des trente jours. Sans cette tâche, le compendium se publie en contradiction avec son propre protocole, et il le sait. |
| 4.5 | C-30, C-28, C-29 | Instruire les trois points ouverts : R-4 « quatre cibles » (instance Vol. II), décompte « hors corpus » du PRD §7.1, libellé de S-035. |
| 4.6 | C-32 | Trancher l'appareil non rédigé : écrire l'avant-propos et les annexes A, D, E, F, G, H, ou les retirer du plan et convertir les renvois des pièces en renvois vers les sièges existants (E vers le glossaire du Vol. II, H vers l'Annexe B du Vol. I, etc.). La seconde option est cohérente avec D-13 ; la première n'est pas compatible avec un dépôt clos. |
| 4.7 | C-33 | Ré-adossement `S-nnn` : décision explicite de ne pas le faire (état actuel, PRD §7.1) ou passe unique sur les 50 pièces contre les deux tables de correspondance. Hors périmètre d'une réouverture d'appareil. |
| 4.8 | C-34, C-35 | Sans action recommandée par l'audit : G-4, G-5, G-6, D-3, D-8, R-IV-101, J-IV-7, J-IV-8 et le risque 14 sont des chantiers de fond que D-13 a explicitement laissés ouverts. Les nommer dans D-15 comme « non rouverts » suffit. |

### 4.7 Séquence recommandée et effort

1. **D-15** (auteur) : périmètre = phases 0, 1, 2, 3 et les tâches 4.1 à 4.4 ; le reste déclaré non rouvert.
2. Phase 0 (une session, ~8 commits, rejeu des harnais après chacun).
3. Phase 1 (un commit) puis tâches 4.1 à 4.3 (deux ou trois commits, chacun avec sa ligne de journal au TOC).
4. Tâche 4.4 (la plus longue : une passe de revalidation à la source, puis reprise des sept pièces).
5. Phase 2 (un commit, après tout le reste).
6. Phase 3 (option A ou B), recomposition du PDF, déclaration de la taille et du hachage.
7. **Nouveau D-13** : clôture redéclarée, avec la date de revalidation et le seuil de trente jours recalculé.

Effort indicatif, sans reprise à la source primaire : phases 0 à 3 tiennent en deux sessions de travail ; la tâche 4.4 dépend du nombre de sources qui refusent l'accès (le registre du 28 juillet en comptait 22 sur 123).

---

## 5. Limites de cet audit

- Les constats de fond (§ 3.3, § 3.4) reposent sur ce que les pièces déclarent d'elles-mêmes ; l'audit n'a rouvert aucune source primaire et n'a pas lu les trois monographies. Un désaccord entre une pièce et sa source ne serait pas visible ici.
- Le comptage des défauts HTML (C-03) est un comptage par expressions régulières ; le nombre exact peut varier de quelques unités, la classe de défaut ne varie pas.
- Les constats C-28 et C-29 sont marqués « à confirmer » : ils opposent une remontée de pièce à l'état courant d'un fichier, sans que l'audit ait pu établir lequel des deux a bougé.
- L'historique montre que le dépôt a déjà retiré des rapports d'audit internes (commit `7a1b7f2`, Traité). Le sort de ce fichier après exécution du plan appartient à l'auteur ; ses constats, eux, doivent être portés au journal du TOC ou au PRD pour survivre à sa suppression.

---

## 6. Commandes de rejeu

```bash
cd "2 - Compendium"
export PYTHONUTF8=1
( cd PRD && python check-toc.py && python check-toc-mutations.py )
( cd PRD && python check-sieges.py && python check-sieges-mutations.py )
( cd PRD && python check-compendium.py && python check-compendium-mutations.py )
python build/assemble-bibliographie.py --verifier
( cd figures && python genere.py --verifier )
bash PRD/decompte.sh --verifier
bash PRD/decompte.sh --registre
python PRD/reporter-volumetrie.py --verifier
python build/verifier-piece.py && python build/verifier-piece-mutations.py
bash build/build-pdf.sh
```

*Les deux dernières lignes de ce bloc et les deux commandes `decompte.sh` n'existaient pas au moment
de l'audit : elles sont sorties de son exécution (§7). Les sondes qui l'ont conduit se relisent
ci-dessous — elles ne rendent plus rien, et c'est le résultat.*

```bash
grep -L 'figures/' Livre*/*.html | wc -l      # 49 avant la phase 3, 1 depuis — le ch. 28,
                                              # seule pièce du volume sans figure
grep -n '"renvoi": None' PRD/check-sieges.py  # 7 avant la phase 0, 1 depuis
```

---

## 7. Exécution des phases 0 à 3 — journal du 2 septembre 2026

*Sur instruction d'auteur, les phases 0 à 3 du plan ci-dessus ont été exécutées le jour même de
l'audit. La passe est la **décision d'auteur D-15** ([PRD](PRD/PRD.md) **v0.19** §18) et la
**décision 22** du [TOC](PRD/TOC.md) **v0.35**. Cette section dit ce qui a été fait, ce qui a été
**refusé**, et ce que l'exécution a **appris contre l'audit lui-même**.*

### 7.1 Ce qui a été fait

| Phase | État | Ce qu'elle laisse derrière |
|---|---|---|
| **0 — appareil** | ☑ close | M14 ancrée sur un motif ; bibliographie reproductible ; garde de P3 corrigée ; **P9** (unicité des remontées) et **P10** (forme des tableaux) ajoutés ; **six sièges réarmés**, harnais de 108 à **114** ; `pypdf` exigé et déclaré |
| **1 — métadonnées et plan** | ☑ close | `Date`, `Statut` et version du socle réalignés au PRD et au TOC ; volet résiduel de G-1 nommé au registre ; ch. 44, ch. 30 et table du ch. 14 corrigés ; **C16** ajouté ; décision 18 appliquée à la table 18.1 ; décompte « hors corpus » re-mesuré |
| **2 — volumétrie** | ☑ close | **331 797 mots** mesurés en une invocation ; **26 en-têtes**, **50 lignes de registre** et **5 `README`** réalignés au même commit ; **`decompte.sh --registre`** ajouté |
| **3 — rendus** | ☑ close, **option A** | [`rendre-piece.py`](build/rendre-piece.py) et son gabarit ; **50 `.html` régénérés** avec **118 figures** ; [`verifier-piece.py`](build/verifier-piece.py) et son harnais (**6 mutations**) ; PDF recomposé à **1 000 pages** |
| **4 — fond et péremption** | ☑ **close le même jour** (**D-16**) | Voir §8 : revalidation post-gel, tableau 50.1 porté à quatorze événements, trois remontées allouées, sept livrables retirés du plan, ré-adossement des `S-nnn` écarté |

**Batterie complète, sorties 0** : `check-toc` (C1-C16) et ses **24** mutations ; `check-sieges`
(26 sièges) et ses **114** ; `check-compendium` (P1-P10, cinq rapports) et ses **23** ;
`decompte.sh --verifier` et `--registre` ; `verifier-piece` et ses **6** ; `assemble-bibliographie`
(1 154 entrées) ; `genere.py` (118 figures) ; `build-pdf.sh` (1 000 pages).

### 7.2 Ce que l'exécution a refusé de faire, et le motif est mesuré

⚠ **La tâche 1.4 recommandait de remapper les 45 en-têtes de table détaillée sur la numérotation
courante. Elle a été écartée, et la recommandation était fausse.** Huit entrées sont des **fusions**
et portent **deux** tables de source chacune — ch. 12, 20, 21, 22, 37, 45, 47 et 49 : les renuméroter
les rendrait **homonymes**, et le lecteur ne pourrait plus dire quel mouvement chaque table décrit.
*Le numéro de source n'était pas la faute ; l'absence de la mention l'était.* La seconde option du
plan a donc été retenue, et durcie : **chaque en-tête déclare son entrée courante**, et **C16**
l'exige.

⚠ **La tâche 3 offrait de retirer les cinquante `.html`. Écarté aussi.** *Supprimer cinquante
fichiers versionnés et amender une règle permanente du dépôt est une décision de fond ; régénérer
n'est que l'exécution de la règle en vigueur.*

### 7.3 Ce que l'exécution a appris contre l'audit

1. **C-04 sous-estimait sa portée.** L'audit disait « rapport faux » sans le chiffrer. Mesuré : **674
   emplois sur 29 pièces → 524 sur 26**. La première mesure, prise sur le fichier entier plutôt que
   sur `corps()`, avait conclu à un défaut **latent** ; il était **actif**. *Mesurer sur le mauvais
   domaine donne un chiffre juste et une conclusion fausse.*
2. **C-11 portait un grief faux.** Les mentions « TOC (v0.32) » du PRD sont des **attributions
   historiques**, non des citations périmées. *Un audit qui compare deux versions sans lire la phrase
   qui les relie produit exactement le défaut qu'il dénonce.*
3. **C-15 décrivait une erreur là où il y avait une convention.** Les en-têtes de table citent la
   numérotation de la **source** ; la note du ch. 41 l'écrivait déjà, à quatorze cents lignes de la
   première occurrence qu'elle explique. **Une convention écrite une fois, loin de ce qu'elle régit,
   est une convention que cinq lecteurs successifs prennent pour une erreur.**
4. **Un constat manquait, et il n'est pas mineur : la décision 18 n'avait été appliquée à aucune
   table du corpus.** La table 18.1 du ch. 18 portait encore **huit périphrases sur neuf rangées** —
   « Consortium du Web », « Fondation d'identité décentralisée », « Institut national de
   normalisation » — que la décision 18 du 30 juillet 2026 a renversées en faisant primer la citation
   nominative. *L'audit n'avait relevé que la rangée qu'une remontée nommait.*
5. **Six sièges étaient désactivés sur des motifs périmés, et l'audit ne l'avait pas mesuré.** Aucun
   texte n'a été édité pour les rétablir : *la condition de réactivation était remplie depuis des
   semaines, et personne n'était revenu la mesurer.*
6. **Trois contrôles neufs existent parce qu'un contrôle en place passait.** P6 opposait deux copies
   du même chiffre ; rien ne distinguait un `.html` régénéré d'un `.html` modifié au même commit que
   sa source ; aucun contrôle ne lisait la forme d'un tableau. **Un contrôle vert qui ne mesure plus
   rien est pire qu'un contrôle absent : il atteste.**

### 7.4 Ce qui reste ouvert

Rien de la **phase 4**, et elle n'a pas été entamée : la **péremption** des faits datés de 2026 ; le
**versement des `S-nnn`** au corps des pièces (**524** emplois nus mesurés, CA-IV-09) ; les **trois
objets supprimés du dépôt** que quatre pièces citent encore (C-23) ; le **siège du § 39.2**, qui ne
peut être versé sans réécrire une pièce close ; le **§ 43.5**, dont S5 reste désactivé sur une
homonymie qu'aucun déclencheur ne sépare. ⚠ **Et le fond n'a pas bougé d'un mot** : le volet de fond
de **G-4** reste entier, **CA-IV-11 et CA-IV-13** demeurent insatisfaites faute de relecteur tiers,
et **le statut du volume est inchangé** — clos, brouillon non publiable.

---

## 8. Exécution de la phase 4 — journal du 2 septembre 2026

*La phase 4 a été exécutée le même jour que les phases 0 à 3, sur instruction d'auteur, comme
**décision D-16** ([PRD](PRD/PRD.md) **v0.20** §19) et **décisions 23 à 26** du [TOC](PRD/TOC.md)
**v0.36**. ⚠ **Elle rouvre la clôture au sens du PRD §16**, ce que D-15 s'était refusé : elle tranche
du fond, amende le socle et retire des livrables du plan.*

### 8.1 Les huit tâches

| Tâche | État | Ce qu'elle laisse derrière |
|---|---|---|
| **4.1** | ☑ close | **Tableau 50.1 porté de onze à quatorze événements** ; trois remontées soldées (ch. 9, 26, 28) ; ventilation re-mesurée, figure 50.2 regravée |
| **4.2** | ☑ close | **`R-IV-110` à `R-IV-112` allouées** ; subdivision du § 35.8 **admise** et dépliée au plan ; **critère de reprise** porté au registre du volet résiduel |
| **4.3** | ☑ close | **Thèse du ch. 49 maintenue « trois socles sources », définitivement** — *la condition de retour du plan était sur le mauvais critère* |
| **4.4** | ☑ close | **Rapport de revalidation** [`revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) ; trois entrées de socle amendées, six chapitres repris ; seuil des trente jours redéclaré |
| **4.5** | ☑ close | `S-035` corrigée **et son intervalle défini** ; décompte « hors corpus » re-mesuré (sous D-15) ; **`R-4` instruite, laissée ouverte à son instance** |
| **4.6** | ☑ close | **Avant-propos et annexes A, D, E, F, G, H retirés du domaine de livraison**, chacun avec son siège aux sources |
| **4.7** | ☑ close | **Ré-adossement des `S-nnn` explicitement écarté** — le manque devient définitif, daté, chiffré |
| **4.8** | ☑ close | **D-3, D-8, R-IV-101, J-IV-7, J-IV-8, le risque 14 et les trois objets supprimés sont nommés « non rouverts »** au §19.8 |

☑ **Et deux instruments naissent de cette phase** : [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py), qui **propage** la mesure aux trois sites qui la publient *sans jamais mesurer lui-même* — il invoque l'autorité et recopie —, et la **garde du zéro** de `decompte.sh`. *Le premier existe parce que la propagation a dû être refaite **trois fois dans la journée** : une opération qu'on refait trois fois à la main se fait mal la troisième.*

### 8.2 Ce que la revalidation a démenti, et c'est son résultat principal

⚠ **Trois des quatre échéances documentaires ne sont PAS survenues.** *Les documents ont été
**renouvelés dans les dix jours précédant leur terme**, et leurs échéances tombent en février 2027.*
**Une lecture par inférence aurait conclu à l'expiration** — c'est le sens ordinaire d'une date passée,
et le corpus l'annonçait ainsi. ***L'événement que la somme surveillait n'est pas celui qui la
menace*** : une expiration d'`Internet-Draft` se repousse à volonté par son auteur ; ce qui change la
citabilité est l'**adoption**, ce qui l'éteint est l'**abandon**. **Le tableau 50.1 surveillait le bon
objet sous le mauvais critère, et cinq semaines ont suffi à le montrer.**

☑ **Ce qui est bel et bien survenu** : le règlement du rail temps réel **en vigueur le 24 août**
(DORS/2026-133), le retrait d'interface **le 26 août**, la clôture des commentaires du règlement
bancaire **le 26 août sans publication finale**.

### 8.3 Deux refus, et un ordre inversé

⚠ **La tâche 4.3 offrait de rendre la thèse du ch. 49 au « socle consolidé ». Écarté.** *G-3 franchie
fait exister l'Annexe B ; elle n'arbitre aucune lacune.* Le socle se déclare **« constitué, non
arbitré »**, **n'élève aucune entrée** et **ne porte aucun registre de lacunes propre** : ***« lacune
du socle consolidé » n'a pas de référent.*** **La condition de retour que le plan avait posée était sur
le mauvais critère**, et elle est retirée.

⚠ **La tâche 4.6 offrait d'écrire l'avant-propos et six annexes. Écarté aussi** — *ce serait une passe
de rédaction, que D-13 ne prévoit plus.* **La seconde option a été retenue et durcie** : les sept
livrables sont **retirés du domaine**, et **chacun reçoit son siège dans les volumes sources** — aucun
n'est inventé, les trois volumes faisant foi.

### 8.4 Ce que l'exécution a appris contre l'audit, et contre elle-même

1. **C-29 était faux.** L'audit disait que le libellé « treize mois » ne figurait plus au socle
   (« grep négatif ») ; **il y était**. *Un grep qui ne trouve rien prouve que le motif est absent, pas
   que le fait l'est.*
2. **La demande du ch. 22 avait deux moitiés, et l'audit n'avait retenu que la première.** Corriger
   l'intervalle ne suffisait pas : **il fallait dire ce qu'il mesure**, faute de quoi la correction se
   périmait le mois suivant.
3. ⚠ **La revalidation s'est trompée avant de trouver.** *Deux règlements ont été prépubliés le même
   jour, dans le même numéro de la Gazette — l'un à trente jours, l'autre à soixante. La première
   lecture a ouvert le mauvais et a cru prendre la somme en défaut.* **La somme avait raison.**
   ***Un document se restitue depuis sa source, jamais depuis une source voisine*** — c'est la
   décision 18 du plan, appliquée aux sources et non plus aux noms.
4. ⚠ **Un défaut de l'autorité de décompte a été découvert par accident, et il était grave.**
   `decompte.sh` rendait **zéro mot par pièce** sous un `bash` strict, *sans erreur ni code de retour* :
   sur un arbre de travail rendu en CRLF, la ligne de séparation ne s'appariait plus. **Corrigé aux
   deux bouts** — le motif tolère le `\r`, et **le zéro se refuse au lieu de se rapporter**.
5. ☑ **Un contrôle écrit le matin a mordu le soir.** *`decompte.sh --registre`, créé à la phase 2, a
   **refusé** le registre après les reprises de fond : sept corps avaient bougé.* **L'instrument a pris
   en défaut la passe qui l'avait créé, le jour même** — et **P10**, **P5** et **S4** ont fait de même
   sur trois éditions de cette phase.
6. ⚠ **Le calage du PDF n'est pas une constante du gabarit.** *La cible de mille pages a demandé
   **16,98 pt** le matin et **16,80 pt** le soir* — dix-huit centièmes en une passe, pour 1 584 mots
   d'appareil. **C'est une fonction du corpus, et elle se re-mesure à chaque passe qui touche un
   corps.**

### 8.5 Ce qui reste, et ne sera pas fait

☐ **Nommé « non rouvert » plutôt que tu** (PRD §19.8) : le volet de fond de **G-4**, **G-5**, **G-6**,
le **volet résiduel de G-1** sur les chapitres ; **D-3** (trois lots, publication du premier mouvement
du Livre V bloquée) ; **D-8** (ch. 41 sous réserve) ; **R-IV-101** (préalable C260, qui bloque le
§ 44.1.9 et le ch. 45) ; **J-IV-7** et **J-IV-8** ; le **risque 14**, dont la couche d'exécution n'a
toujours de chapitre nulle part. ☐ **Le ré-adossement des `S-nnn`** — **524 emplois nus** — est
**écarté par décision**, non reporté. ☐ **Les trois objets supprimés du dépôt** que quatre pièces
citent restent **irrésolubles**, et les pièces les déclarent tels. ☐ **`CA-IV-11` et `CA-IV-13`**
demeurent insatisfaites : **D-6 ne fournit pas de relecteur tiers**, et aucune passe d'appareil ne
peut y suppléer.

⚠ **Le statut du volume n'a pas changé d'un mot** : **clos**, **brouillon de rédaction non
publiable**, **aucune porte franchie**, **rien de publié**.
