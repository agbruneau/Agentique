# PRD — Compendium « La somme agentique » (Vol. IV)

| Champ | Valeur |
|---|---|
| Version | **0.2 — audit et réancrage sur le TOC v0.14** (23 juillet 2026). Révise la v0.1 (gouvernance posée le 23 juillet 2026, établie sur le TOC v0.13) **sans toucher à la gouvernance** — portes, régimes de preuve, seuil de vote, critères CA-IV, jalons et décisions d'auteur inchangés. Deux objets. **(1)** Réancrage de tous les renvois au plan sur le **TOC v0.14** : cette version du TOC est sa *collation d'appui structurelle* contre les trois monographies rédigées — couverture complète des sources, onze renvois de section au Vol. III résolus contre son texte rédigé, structure des 57 chapitres en dix livres intacte. **(2)** La porte **G-4** enregistre que son **volet structurel** (couverture et résolution des renvois) est **levé** par cette collation, à zéro écart ; **reste dû** son volet de fond — la confrontation adversariale de chaque glose et thèse au texte, par lectures indépendantes chargées de réfuter. ⚠ **Toujours aucune passe d'instruction, aucun socle constitué, aucun chapitre rédigé** : la refonte du socle (G-3) reste ouverte, et un PRD écrit avant elle fournit son inventaire d'héritage, jamais des faits (leçon du PRD du Vol. III, §1). |
| Historique v0.1 | **0.1 — gouvernance de la rédaction posée avant la première pièce** (23 juillet 2026). Établi sur le [`TOC.md`](TOC.md) **v0.13** et sur l'état réel des trois volumes sources, constaté sur pièces le 23 juillet 2026 (PRD v1.3 / TOC v0.8 / `CLAUDE.md` du Vol. III lus dans leurs en-têtes ; gels des Vol. I et II relevés à leurs sièges). ⚠ **Aucune passe d'instruction n'est menée par cette version, aucun socle n'est constitué, aucun chapitre n'est rédigé** : un PRD écrit avant la refonte du socle fournit son inventaire d'héritage et son plan d'acquisition, jamais des faits — leçon du PRD du Vol. III (son §1), reprise ici mot pour mot |
| Date | 23 juillet 2026 |
| Statut | **Gouvernance posée, exécution non commencée.** Zéro pièce rédigée sur 67 (57 chapitres, avant-propos, 9 annexes) ; socle consolidé à **0 entrée** (la refonte est la porte G-3) ; sept portes de lancement, toutes ouvertes ; six décisions d'auteur requises (Annexe A) |
| Livrable encadré | Compendium intégral — 57 chapitres en 10 livres, avant-propos, 9 annexes ; ≈ 369 000–394 000 mots projetés (fourchette indicative, non normative — TOC, Volumétrie) |
| Autorité | **Ce PRD prime en cas de conflit sur la gouvernance, le socle et les lacunes** — la règle que le compendium applique déjà à ses sources (« sur le socle et les lacunes, le PRD d'un volume prime son TOC », TOC v0.14, Filiation) vaut pour lui-même. Le **TOC conserve l'autorité sur le découpage et sur le contenu de chaque chapitre** : ses entrées (thèse, sections, ligne Fusion, socle, garde-fous) sont la spécification par chapitre, et ce PRD ne les duplique pas (périmètre des fichiers de doc, `CLAUDE.md` racine). Le Conspectus reste une vue dérivée sans autorité |
| Méthodologie | Méthode unifiée du TOC (avant-propos et Annexe A du plan) : niveaux [A]/[B]/[C], tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF, vote adversarial à seuil déclaré (§7), attribution des métriques auto-déclarées à chaque occurrence, trois degrés d'absence. **À exécuter, non exécutée** |
| Contrôles | `python check-toc.py` (C1-C14) avant toute publication du TOC ; `check-toc-mutations.py` après toute modification du script ; les contrôles de rédaction (§9) sont **une spécification sans exécutable** tant que `check-compendium.py` n'est pas construit et validé par mutation — le construire est un préalable à la première pièce publiée |

---

## 1. Objet du document

Ce PRD définit le **processus** qui rend la rédaction des 67 pièces du compendium possible et vérifiable : les portes de lancement (§5), l'ordre de rédaction (§6), les régimes de preuve et le seuil de vote (§7), les garde-fous et leur outillage (§8), les contrôles (§9), le régime des lacunes (§10), les critères d'acceptation (§11), les jalons (§12) et les risques d'exécution (§13).

**Ce qu'il ne fait pas.** Il ne spécifie pas le contenu des chapitres — le TOC v0.14 le fait, entrée par entrée, et chaque entrée du TOC **est** le cahier des charges de son chapitre : thèse, sections, ligne « Fusion » (provenance et arbitrages), socle assigné, garde-fous assignés, lacunes portées. Il ne fournit pas non plus de socle : la refonte (Annexe B du plan) est une porte de ce PRD, pas son contenu. Un §7 qui énumérerait des faits consolidés que personne n'a refondus serait la faute exacte que le Vol. III a nommée dans son propre PRD.

## 2. Contexte — l'état réel des trois sources au 23 juillet 2026

| Source | État | Gel | Socle | Réserve portante |
|---|---|---|---|---|
| Vol. I | Rédigé, vérifié (233 257 mots bruts) | juin 2026 | faits datés, vérification adverse des *références* | ⚠ sa *Synthèse* est **retirée du dépôt** depuis le commit `fd8f1be` (22 juill. 2026) — voir §13 |
| Vol. II | Rédigé, vérifié (92 059 mots, commande locale `C`) | 16-17 juill. 2026 | F-01…F-48 + F-23b, niveaux [A]/[B]/[C] | onze lacunes ouvertes à son gel (son PRD §10) |
| Vol. III | **Rédigé** — 34 pièces sur 34, 160 427 mots (commande PRDPlan §1.5) | 21 juill. 2026 | F-01…F-98 propres + H-01…H-33 héritées | « **rédigé ne vaut pas publiable** » : 15 remontées ouvertes, 12 arbitrages révocables, dette de vote (F-92, F-96) |

*État des sources constaté sur pièces le 23 juillet 2026 (TOC v0.14, Filiation ; constat de dépôt au journal v0.13).*

Tant que la somme n'est pas rédigée, **les trois volumes font foi** (TOC, Statut ; risque 7) : rien de ce que ce PRD ordonne ne corrige un volume source, et aucun écart entre eux ne s'arbitre ailleurs qu'à l'Annexe C du plan, sur source primaire nouvelle datée.

## 3. Objectifs et non-objectifs

### Objectifs

- **O1.** Rédiger les 57 chapitres et l'appareil en démontrant la thèse d'ensemble — un seul problème d'ingénierie continu sur quatre plans — sans diluer les thèses partielles absorbées (risque 6).
- **O2.** **Refondre les trois socles en un** (Annexe B du plan) : numérotation unique, deux tables de correspondance F-xx (Vol. II et Vol. III), re-datation au gel unique — le chemin critique du projet (risque 4).
- **O3.** Tenir la **couverture totale tracée** (décision 6) : chaque section source affectée ou coupée explicitement, la collation contre le Vol. III rédigé faite avant la fusion de ses livres (G-4).
- **O4.** Constituer le **socle propre du Livre IX** depuis des sources primaires, ou constater son échec et exécuter le retrait prévu (décision 9, risque 13).
- **O5.** Faire arbitrer et exécuter les **décisions d'auteur** que le TOC déclare hors de portée d'une passe (Annexe A de ce PRD).

### Non-objectifs

- Ne pas produire de thèse nouvelle hors du Livre IX (Nature du TOC : une somme, pas un cinquième volume).
- Ne pas corriger les volumes sources ni leurs TOC — leurs erreurs documentées (« §3-§12 », etc.) sont signalées chez eux, jamais lissées ici (risque 10).
- Ne pas re-trancher ce que les journaux gelés du TOC consignent, ni réécrire ces journaux.
- Ne pas émettre de conseil juridique ; ne pas recommander de fournisseur ; ne pas fournir de recette d'exploitation (héritages R-12/CA-12 du Vol. III pour les ch. 20-22).

## 4. Portée — le test d'appartenance

Trois critères, opposables et vérifiés par CA-IV-08 :

1. **Les quatre plans** : tout contenu se rattache à coopérer, encadrer, faire confiance ou livrer (thèse d'ensemble ; risque 6).
2. **Le critère des capacités** (Livres III et VII, hérité du Vol. III) : tout contenu de maillage ou d'exploitation sans lien à l'identité ou à la délégation est hors périmètre (risque 12).
3. **Le critère du Livre IX** : tout contenu sans rattachement aux livres amont (identité, encadrement, exploitation, blueprint) est hors périmètre (en-tête du Livre IX).

⚠ Leçon du Vol. III (CA-09, R-G-46) : le **grain** du test — section ou développement — a produit chez lui deux coupes invisibles au grain prescrit. Ce PRD fixe le grain d'emblée : **le développement**, une section qui passe n'immunisant pas ses développements.

## 5. Préalables de lancement — les sept portes

Aucun chapitre ne se rédige avant que **G-1, G-2 et G-3** soient franchies ; les portes G-4 à G-7 conditionnent les livres qu'elles nomment. C'est la règle cardinale du volume, héritée du PRD du Vol. III (§7.0) : *un chapitre écrit sur un socle vide n'est pas un chapitre en avance, c'est une inférence longue.*

| Porte | Objet | Conditionne |
|---|---|---|
| **G-1** | **Gel unique** (décision 5 du TOC) : date fixée par l'auteur (D-1) ; re-datation de tout fait périssable ; instruction à la source primaire des relèves v0.7, v0.10 et v0.11 consommées, chacune à son point d'atterrissage ; re-vérification des deux divergences de l'Annexe C (dont AP2/FIDO — réouverture déclenchée en v0.7, à consommer par extraction, jamais sur annonce) | tout |
| **G-2** | **Commande de décompte de référence** : `LC_ALL=C.UTF-8` (héritage PRDPlan du Vol. III §1.5), **validée sur les trois corpus entiers avant toute mesure publiée** — jamais sur un échantillon (leçon du Vol. II, quatre mesures successives ; leçon v0.5 du TOC, deux chiffres faux d'un facteur) | tout décompte publié |
| **G-3** | **Refonte du socle** (Annexe B du plan) : détail en §7. Sortie : socle consolidé numéroté, deux tables de correspondance, re-daté au gel — et `check-compendium.py` construit et validé par mutation (§9) | toute rédaction |
| **G-4** | **Collation contre le Vol. III rédigé** — l'homologue de la v0.6 du TOC pour les Vol. I-II : chaque ligne « Fusion », chaque glose et chaque thèse citant le Vol. III confrontée au texte final des 34 pièces, par lectures adverses indépendantes chargées de réfuter, écarts corrigés au TOC (version++) avant fusion. ⚠ **Volet structurel levé par la v0.14 du TOC** (collation d'appui : couverture complète et onze renvois de section résolus contre le texte rédigé, zéro écart) ; **reste dû le volet de fond** — confrontation adversariale des gloses et thèses au texte, lectures indépendantes chargées de réfuter | Livres III et VII, et toute entrée citant le Vol. III |
| **G-5** | **Arbitrage du risque 14** (la couche d'exécution — le harnais) : chapitre neuf, sections dans l'existant, ou périmètre assumé et déclaré — décision d'auteur (D-2) | Livres VII et IX |
| **G-6** | **Sort du Livre IX** : socle propre constitué depuis des sources primaires, ou retrait (décision 9, issue prévue ; renumérotation inverse 55-57 → 52-54 assumée) — décision d'auteur (D-3) | Livre IX |
| **G-7** | **Seuil de vote adversarial** : fixé en §7 de ce PRD — le TOC remettait cette décision « au lancement » ; elle est prise ici et ne se rediscute pas en cours de rédaction | toute entrée du socle consolidé |

## 6. Structure et ordre de rédaction

**Structure** : celle du TOC v0.14, sans reprise ici. Chaque pièce porte en tête le tableau à cinq champs hérité (Statut ; Date de gel ; Socle mobilisé — **chaque identifiant préfixé de son volume d'origine tant que la renumérotation G-3 n'est pas publiée** ; Garde-fous balayés — **y compris ceux à zéro occurrence**, contrepartie obligatoire des douze pièces de synthèse ; Volumétrie cible), suivi de la thèse citée depuis le TOC.

**Ordre de rédaction**, dicté par les portes et l'état des sources :

1. **Livres I, II, IV, V, VI** (sources : Vol. I et II, gelés et vérifiés) — après G-1/G-2/G-3.
2. **Livre VIII** (synthèse architecturale — consomme les précédents ; le ch. 48 attend en outre la re-vérification C260, préalable déclaré à son registre des stéréotypes).
3. **Livres III et VII** — après G-4 en plus ; leurs pièces re-vérifient l'état des remontées ouvertes du Vol. III qui les touchent.
4. **Livre IX** — dernier des livres de matière (décision 9c), après G-5 et G-6.
5. **Livre X** — la clôture ferme l'ouvrage : le ch. 56 enregistre l'état final des lacunes, le ch. 57 le registre de gel par chapitre.
6. **Appareil** : l'Annexe B vit dès G-3 et s'amende en cours de rédaction (régime des versements du Vol. III, PRD §7.10-§7.11 : une affirmation requise mais non versée se **verse au socle**, jamais citée depuis un rapport ni dans la pièce seule) ; les autres annexes se finalisent après le Livre X ; l'avant-propos en dernier.

**Déviation** : le plan s'aligne sur le chapitre, jamais l'inverse, et une déviation fondée **se déclare** (décision 8 du TOC, corollaires a-c). Toute modification du découpage passe par le TOC (version++), jamais par ce PRD.

## 7. Socle consolidé — refonte, régimes de preuve, seuil de vote

### 7.1 La refonte (porte G-3)

- **Vol. II — F-01…F-48 + F-23b** : niveaux conservés avec provenance (méthode identique, rien à re-subir). ⚠ Le Vol. II n'attribue pas F-12 à F-14 : le trou ne se comble pas en décalant (TOC, Annexe B).
- **Vol. III — F-01…F-98 et H-01…H-33** : niveaux conservés (méthode héritée du Vol. II) ; les H-xx se dédupliquent contre les entrées Vol. I/II dont elles proviennent. **F-92 et F-96 du Vol. III n'entrent pas** avant résorption de leur dette de vote ou reprise de la parade ⚖ (TOC v0.14, Annexe B).
- **Vol. I** : les faits datés entrent **en [C]** — sa vérification porte sur les références, non sur le contenu des affirmations (régime du PRD du Vol. III, §7.1) ; élévation en [B] **par lecture de la source primaire que le Vol. I cite**, obligatoire avant tout fait central ; une entrée sans source primaire tierce (construction d'auteur du Vol. I) reste une thèse attribuée et ne porte jamais un fait central.
- **Renumérotation** : unique pour les F-xx, avec **deux tables de correspondance** (une par série source) ; les R-xx, CA-xx, L-xx, H-xx et R-G-xx ne se renumérotent **jamais** et se citent préfixés de leur volume (décision 7).
- **Re-datation** : chaque entrée porte sa date de péremption re-vérifiée au gel unique (risque 3 — trois gels sources non synchrones).

### 7.2 Régimes de preuve et seuil de vote (porte G-7)

Trois régimes, déclarés au lecteur (Conspectus, « Régimes de preuve ») et différenciés à l'exécution :

| Régime | Livres | Vote adversarial (trois juges, charge de réfuter) | Plancher |
|---|---|---|---|
| Sources gelées et vérifiées | I, II, IV, V, VI, VIII, X | réservé aux affirmations qui portent à elles seules la thèse d'un chapitre, et aux faits vivants re-datés en G-1 | [B] par extraction citée pour tout fait central nouveau |
| Source rédigée non publiable | III, VII | idem, **plus** toute affirmation issue d'une pièce du Vol. III touchée par une remontée ouverte ou un arbitrage délégué révocable (l'option écartée se relit avant reprise) | niveau d'origine conservé, sous G-4 |
| Matière neuve | IX | **toutes les affirmations centrales** — le régime le plus dur, pour le livre le plus nu | sources primaires seules ; échec documenté = résultat (retrait, G-6) |

*Seuil fixé avant la première pièce, non rediscuté en cours de route.*

**Motif, hérité du Vol. III (§A.4) et adapté** : sur les livres à sources vérifiées, voter ce que personne ne conteste gaspille le budget de réfutation ; sur le Livre IX, tout est contestable par construction. Conséquence assumée : la proportion d'entrées [A] variera par livre, et chaque tête de livre la déclare (parade du risque 11).

**Relèves v0.7, v0.10, v0.11** : repérages [C] — aucune n'entre au socle consolidé sans extraction de la source primaire (G-1) ; leur point d'atterrissage est celui que les journaux du TOC désignent.

## 8. Garde-fous rédactionnels

**Pas de troisième série.** La somme applique les deux séries héritées — **R-1…R-8 du Vol. II** et **R-01…R-14 du Vol. III** — nommées par volume à chaque emploi (décision 7), telles que le TOC les assigne chapitre par chapitre. S'y ajoutent les formulations imposées héritées, dont les plus violées d'inadvertance :

- « **attendu par E-23** », jamais « exigé » ; la « supervision humaine » n'est pas une des cinq attentes au socle (PRD Vol. II §7.3, PRDPlan §4.4) ;
- RTR : « quatre **cibles successives** — 2019, 2022, 2023, 2026 », jamais « quatre reports » ; jamais « lancé » (réserve F-29, R-4) ;
- jalons NIST : « **visée** », jamais « fixée » (R-11 du Vol. III), statut du document porté ;
- MCP : « **cadre** d'autorisation », jamais « sécurisé » (réserve F-01) ;
- art. 12.1 : le flux outille un point d'arrêt humain, **jamais la révision de l'article 12.1** (Vol. II ch. 23) ;
- métriques auto-déclarées : attribuées **à chaque occurrence, sans exception d'usage illustratif** (PRD Vol. II §7.5) ;
- absences : fait négatif **vérifié** > **établi** > absence de documentation, jamais interchangeables (R-14) ;
- qualification cryptographique : par ce que la spécification **démontre**, jamais ce qu'elle promet (R-02) ;
- « AgentMesh », « control plane », « ACP », « autonomie graduée » : jamais nus (R-04 branche (f), R-8 du Vol. II, R-13 du Vol. III).

**Motifs de balayage** : la somme se dote des siens **à la clôture de G-3** — un critère d'acceptation sans motif qui le contrôle n'est pas vérifiable (PRD Vol. III §A.6, le gabarit) —, chaque motif **validé par mutation avant emploi** (voir-doit / ne-doit-pas-voir), assignation par pièce portée par le TOC. La dualité d'usage (ch. 20-22) n'a pas de motif et n'en aura pas : relecture dédiée seule (CA-IV-11), l'absence déclarée plutôt que subie.

## 9. Contrôles outillés

| Instrument | État | Domaine |
|---|---|---|
| `check-toc.py` (C1-C14) | ☑ versionné, validé par mutation (v0.12) | le TOC — avant toute publication du fichier |
| `check-toc-mutations.py` | ☑ versionné | le script lui-même — après toute modification |
| `check-compendium.py` | ☐ **à construire en G-3, valider par mutation avant la première pièce publiée** | les pièces : en-têtes à cinq champs, renvois « ch. N » 1-57, identifiants du socle consolidé résolvant contre l'Annexe B, identifiants préfixés de leur volume, registre de gel aligné pièce à pièce, motifs de balayage §8 |

*Un contrôle dont l'exécutable n'est pas versionné est une spécification, pas un contrôle (constat v0.7 du TOC — cinq passes l'ont payé).*

Le registre de gel par pièce suit le modèle du Vol. III (`99-registre-gel.md`) : statut, date de gel, cible, volumétrie réelle, renseigné **au même commit que la pièce** — et se re-vérifie contre l'en-tête de la pièce avant tout usage.

## 10. Lacunes et divergences — régime

L'**Annexe C du plan est le siège unique**. Règles :

1. Les **onze lacunes du PRD du Vol. II** y sont reprises par identifiant, portées par les chapitres que son registre désigne (contrôle C9). Aucune ne se clôt sans source primaire nouvelle datée.
2. Les **lacunes documentées du Vol. III** (22 à son gel, dont quatre closes — cardinal à **re-mesurer** en G-3 sur son PRD §10, jamais recopié d'ici) entrent au registre avec leur état au gel du Vol. III, sous la même règle.
3. Les **deux divergences tranchées** (date AMF ; gouvernance AP2) se re-vérifient à chaque gel de chapitre concerné (risque 5) ; la réouverture AP2/FIDO déclenchée en v0.7 se consomme par extraction en G-1, et l'écart éventuel avec le socle gelé du Vol. II **se déclare, ne se lisse pas**.
4. Une divergence tranchée n'est pas une lacune comblée ; aucune absence héritée n'établit un fait négatif (Annexe C, règle du Vol. II en toutes lettres).

## 11. Critères d'acceptation

- **CA-IV-01 Traçabilité.** Toute affirmation factuelle centrale adossée à une entrée du socle consolidé ou à une source primaire nouvelle de qualité équivalente ; une affirmation tracée vers une entrée [C] n'est pas centrale, ou n'est pas rédigée.
- **CA-IV-02 Zéro proscrit.** Aucune formulation proscrite des deux séries héritées (§8) ; contrôle outillé par les motifs de balayage, complété d'une inspection humaine — une faute passe sous l'outil sans passer sous la règle.
- **CA-IV-03 Attribution.** §8, métriques auto-déclarées : à chaque occurrence.
- **CA-IV-04 Datation.** Chaque pièce porte sa date de gel au registre, au même commit ; revalidation finale datée de moins de trente jours à la publication.
- **CA-IV-05 Fidélité des citations.** Verbatim réservé aux reprises littérales vérifiées contre le texte actuel de la source — ou contre **l'arbre gelé `fd8f1be~1`** pour la *Synthèse* du Vol. I, retirée du dépôt (§13) ; une reprise en substance se déclare telle.
- **CA-IV-06 Honnêteté des lacunes.** Toutes les lacunes du registre (§10) apparaissent, aucune silencieusement omise ; le ch. 56 les reprend une à une par identifiant.
- **CA-IV-07 Marquage des inférences.** Toute construction d'auteur porte « Lecture de l'auteur », suivi de ce que le socle établit et n'établit pas ; les trois chapitres du Livre IX le portent à l'ouverture ; les passages du Vol. III issus des réaffectations P0.2 conservent leur marquage CA-07 d'origine.
- **CA-IV-08 Périmètre.** Test d'appartenance (§4) vérifié au grain du **développement**, coupes consignées.
- **CA-IV-09 Qualification des renvois.** Décision 7 du TOC, intégralement : document nommé (Vol. I triple numérotation ; §8.x/§10.x du Vol. II ; TOC/PRD/PRDPlan du Vol. III ; les deux « Annexe B » du Vol. II), série nommée (deux séries « Q n »), volume nommé (R-N, et **F-xx depuis la v0.13**).
- **CA-IV-10 Statut épistémique double.** Niveau [A]/[B]/[C] et tri prospectif : deux instruments, jamais l'un pour l'autre.
- **CA-IV-11 Traitement défensif.** Ch. 20-22 : mécanique au niveau architectural, identifiants cités, aucune recette reproduite ; relecture dédiée par un relecteur distinct, compte rendu déposé et nommé dans la pièce ; l'attestation auto-délivrée est proscrite **même exacte**.
- **CA-IV-12 Traçabilité du blueprint.** Ch. 49-50 : chaque composant et lien réglementaire tracé au socle ou marqué inférence (CA-8 hérité du Vol. II) ; contrôle par confrontation à la spécification de cadrage, pas par relecture seule (leçon du ch. 27 du Vol. III : un découpage refait sans marquage survit aux relectures).
- **CA-IV-13 Relecture adversariale.** Chaque pièce, par un relecteur distinct du rédacteur, chargé de réfuter ; les correctifs s'appliquent **dans le pipeline de la passe**, jamais après (leçon P3 du Vol. III) ; si la faute siège au socle, on amende le socle d'abord, jamais la pièce seule.
- **CA-IV-14 Attestation sur pièce.** « Conforme », « vérifié », « résolu » s'écrivent depuis une constatation sur pièce, jamais depuis un document amont ni un souvenir ; un jalon s'atteste par un seuil, pas par son propre récit.

## 12. Livrables et jalons

| Jalon | Livrable | Critère de sortie (seuil) |
|---|---|---|
| **J-IV-0 (fait — 23 juill. 2026)** | Gouvernance posée : TOC v0.14, ce PRD v0.2, `check-toc.py` + harnais versionnés | ☑ C1-C14 sortie 0 ; 17 mutations détectées ; constat aux journaux v0.12-v0.14 du TOC |
| **J-IV-1** | Portes G-1 et G-2 : gel unique, relèves instruites, divergences re-vérifiées, commande validée | date de gel publiée ; chaque relève consommée ou reconduite avec motif ; commande exécutée sur les trois corpus entiers, résultats reproduits |
| **J-IV-2** | Porte G-3 : socle consolidé (Annexe B), tables de correspondance, `check-compendium.py` | 100 % des F-xx cités par le TOC résolvent contre l'Annexe B ; deux tables publiées ; script validé par mutation ; motifs de balayage publiés et mutés |
| **J-IV-3** | Portes G-4 à G-6 : collation Vol. III (**volet structurel levé par la v0.14, zéro écart** ; reste le volet de fond), arbitrages D-2/D-3 | écarts de collation corrigés au TOC (version++) ; décisions consignées à l'Annexe A avec date |
| **J-IV-4** | Livres I, II, IV, V, VI (28 chapitres) | chaque pièce : CA-IV-01 à 14 constatés, registre de gel aligné |
| **J-IV-5** | Livre VIII (ch. 46-51) | idem + re-vérification C260 consignée au ch. 48 |
| **J-IV-6** | Livres III et VII (ch. 12-24, 41-45) | idem + G-4 close |
| **J-IV-7** | Livre IX (ch. 52-54) — ou son retrait | socle propre publié et voté, ou retrait exécuté (renumérotation inverse, journaux) |
| **J-IV-8** | Livre X (ch. 55-57) + appareil complet | registre des lacunes intégral au ch. 56 ; registre de gel au ch. 57 ; 9 annexes livrées |
| **J-IV-9** | Revalidation finale, publication | revalidation < 30 jours ; grille CA-IV intégralement constatée ; décomptes concordants entre PRD, TOC, README du volume et README du dépôt ; **la somme se substitue aux volumes** (levée du risque 7) |

**Définition de « terminé »** : les 67 pièces rédigées, relues adversarialement et tracées ; grille CA-IV conforme par constatation ; lacunes toutes exposées ; décomptes re-mesurés et concordants entre porteurs ; le statut du TOC (« les volumes font foi ») retourné.

## 13. Risques du projet éditorial

Les **quatorze risques de cadrage** vivent au TOC et n'y sont pas dupliqués. Risques d'**exécution** propres à ce PRD :

| Risque | Impact | Parade |
|---|---|---|
| **La *Synthèse* du Vol. I est hors dépôt** (supprimée au commit `fd8f1be`, 22 juill. 2026 — constat direct, `git show --name-status` ; remontée R-G-52 du Vol. III à l'auteur, non tranchée) | les renvois « *Synthèse* §N » du TOC — exacts — ne sont plus opposables sur l'arbre courant ; la collation et CA-IV-05 perdent leur pièce | vérifier contre l'arbre gelé `fd8f1be~1` tant que R-G-52 n'est pas arbitrée ; ne pas restaurer le fichier (hors charge éditoriale) ; décision d'auteur D-5 |
| **Les remontées ouvertes du Vol. III bougent des passages déjà fusionnés** | re-travail des Livres III/VII | G-4 tardive (au plus près de la rédaction de ces livres) ; état des 15 remontées re-vérifié au gel |
| **Volumétrie : condensation réelle ~52 % sur les Livres III/VII** (TOC v0.14, Volumétrie) | enveloppes intenables ou coupes de bornes | décision d'auteur D-4 (re-calibrage éventuel) ; l'écart se documente, ne s'ampute pas — *amputer une borne et couper un hors-périmètre produisent le même chiffre* (leçon du Vol. III) |
| **Réversibilité de P0.2** (dépôt ultérieur des trois ouvrages) | huit emplacements + Annexe G à rouvrir | marqueurs « corpus d'appui » conservés (contrôle C10) ; réouverture = acte déclaré, jamais silencieux |
| **Péremption en cours de rédaction** — MCP 2026-07-28 ratifiée pendant le projet, RTR, arrêté du cadre bancaire | Livre II et ch. 36-37 périmés avant publication | événements de péremption du ch. 57 surveillés à chaque jalon ; re-datation G-1 ; un fait qui bascule se traite au socle d'abord |
| **Attestations non rejouables** — le projet vient d'en payer deux (script perdu des passes v0.3-v0.6 ; chemins `Tocs/` du journal v0.5) | contrôles fictifs, collations non rejouables | tout exécutable versionné et muté ; toute mesure ancrée à un commit ou une date ; CA-IV-14 |

---

## Annexe A — Décisions d'auteur requises et règle d'escalade

| # | Décision | Échéance | État |
|---|---|---|---|
| **D-1** | Date du **gel unique** | J-IV-1 | ☐ |
| **D-2** | **Risque 14** (harnais) : chapitre neuf, sections, ou périmètre déclaré | avant J-IV-6 (Livre VII) | ☐ |
| **D-3** | **Livre IX** : constitution du socle ou retrait | avant J-IV-7 | ☐ |
| **D-4** | **Re-calibrage éventuel** des enveloppes des Livres III/VII (condensation mesurée ~52 %) | J-IV-1 | ☐ |
| **D-5** | Régime des renvois à la ***Synthèse* du Vol. I** (R-G-52 : restauration, ancrage à `fd8f1be~1`, ou repointage vers `Monographie.md`) | avant G-4 | ☐ |
| **D-6** | **Instance d'arbitrage** désignée pour les remontées réservées à l'auteur — la lacune que le Vol. III a constatée deux fois sans la combler (son PRDPlan §5.3) | J-IV-1 | ☐ |

**Règle d'escalade — posée avant la première rédaction** (héritage PRDPlan du Vol. III §5.3, avec sa correction) : un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il **remonte**, et une remontée marquée « bloquant pour le ch. N » interdit de lancer le ch. N. L'instance d'exécution arbitre les remontées de renvoi, de siège, de cardinal ou de niveau, avec champ « Tranchée par » ; **remontent à l'auteur sans exception** : thèse d'ensemble, découpage, enveloppes, garde-fous, critères d'acceptation, et les six décisions D-1 à D-6. Les remontées se tranchent **entre les lots, jamais en fin de phase**.
