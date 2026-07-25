# Grille de relecture CA-1..CA-8 (jalon J-5 — PRDPlan P4.2)

| Champ | Valeur |
|---|---|
| Date | 17 juillet 2026 |
| Périmètre | 29 pièces : 24 chapitres + avant-propos + annexes A à D |
| Gouvernance | [PRD.md](../PRD.md) v1.10 §11 (les critères) ; [PRDPlan.md](../PRDPlan.md) v1.4 §4.3 (motifs de balayage), §4.4 (formulations imposées) — *pointeurs relevés le 17 juill. 2026 avec les suites de l'audit ; les contenus §11/§4.3/§4.4 cités sont inchangés sur le fond* |
| Revalidation adossée | [`revalidation-2026-07-17.md`](revalidation-2026-07-17.md) — P4.1, huit faits chauds revérifiés à leur source primaire |
| Résultat | **8/8 conformes**, après correction des écarts relevés ci-dessous — ⚠ **résultat partiellement démenti le 17 juillet 2026 par l'audit global** ([`audit.md`](../audit.md)) : voir l'addendum en fin de grille |

**Règle de cette grille.** Un critère n'est déclaré conforme que si un **contrôle exécuté** l'établit — jamais sur l'intention du rédacteur ni sur son auto-contrôle. La leçon est chèrement acquise : le 17 juillet 2026, trois blocs d'auto-contrôle sur quatre attestaient des décomptes qui n'avaient pas été passés, et deux attestaient des reproductions absentes du fichier. **Une attestation est du contenu, elle se vérifie comme le reste.**

---

## CA-1 — Traçabilité

> *100 % des affirmations factuelles centrales adossées au socle §7 ou à une source primaire nouvelle de qualité équivalente ; identifiants F-xx utilisables en notes.*

| Contrôle exécuté | Résultat |
|---|---|
| Tout F-xx cité existe-t-il au socle ? Comparaison mécanique de l'ensemble cité (29 pièces) à l'ensemble défini (PRD §7) | **Conforme.** Les seules occurrences de F-12, F-13 et F-14 — non attribués — sont les phrases qui énoncent qu'ils ne le sont pas |
| Notes appelées ↔ notes définies, par pièce | **Conforme** après correction. Une note orpheline créée le 17 juill. au ch. 21 (renvoi `[^10]` déjà pris ; corrigé en `[^22]`) |
| Cardinal du socle | **46 entrées** (F-01 à F-48 ; F-12 à F-14 non attribués ; F-23b). Recompté par la commande publiée en PRD §7 |

**Écarts relevés et corrigés.** Le marqueur d'inférence a été unifié en P2 (« **Lecture de l'auteur** » en prose ; « inférence d'auteur » en cellule de tableau — PRDPlan §4.4) : présent dans les 24 chapitres et les annexes A, B et C ; « inférence de lecture » : 0 occurrence.

**Trois défauts de traçabilité corrigés le 17 juillet, tous relevés par relecture adversariale et non par l'auto-contrôle :**

1. **Avant-propos** — le contrôle de traçabilité citait « F-18 (Scotiabank) ». F-18 est *TD, gouvernance* ; Scotiabank/AIDox est **F-21**. Se tromper d'entrée dans le document qui promet au lecteur que « la note lui donne l'entrée ».
2. **Annexe D** — l'en-tête omettait **F-26**, que l'entrée « adaptativité après déploiement » cite trois fois, et annonçait 23 entrées pour 24.
3. **Annexe B** — le journal attestait que la note `[^1]` portait les cinq membres de la formulation §8.2.4. Mesuré : « intentionally broad » et « couverture implicite » y ont chacun **une** occurrence — dans l'attestation elle-même ; les cinq analystes, **zéro**. Attestation rectifiée.

---

## CA-2 — Zéro réfuté

> *Aucune des affirmations R-1 à **R-8** (§8.1) ne figure dans le texte.*

Balayage **exhaustif** des 29 pièces, motifs de PRDPlan §4.3.

| Garde-fou | Contrôle | Résultat |
|---|---|---|
| **R-1** (ACP fusionné dans A2A) | Occurrences d'`\bACP\b` inspectées une à une | **Conforme.** Toutes qualifiées (« l'ACP protocolaire », « *Agent Communication Protocol* ») ou en mention de l'interdiction. **Aucun sigle nu en emploi référentiel** |
| **R-2** (Entra ≠ registre) | `registre centralisé\|Entra.*registre` | **Conforme** |
| **R-3** (CSA/SPIFFE) | `SPIFFE\|SVID` | **Conforme** — « s'appuie sur », jamais « impose » |
| **R-4** (RTR : cible annoncée) | `aucune date` | **Conforme.** Aucune occurrence de « aucune date annoncée » ; le ch. 15 pose explicitement l'inverse |
| **réserve F-29** (RTR : pas lancé) | `RTR.*lancé\|en production` | **Conforme.** Toutes les occurrences sont en négation, au conditionnel, ou en statut « visé » |
| **R-5** (aucun standard désigné) | `FDX\|standard technique` | **Conforme.** FDX toujours « anticipation d'industrie » / « commentaire d'industrie ». **Revalidé à la source le 17 juill. 2026** : aucun arrêté (Gazette : « *will be designated* ») |
| **R-6** (Gartner MQ iPaaS) | `Gartner\|Magic Quadrant\|iPaaS` | **Conforme** dans le texte. **Écart corrigé** : R-6 était **entièrement absent** de l'annexe D §D.7, instrument opérationnel de ce critère |
| **R-7** (conformité E-23/B-13) | `E-23\|B-13` | **Conforme.** Motif massif en Partie III — contexte réglementaire pur, filtré (§4.3). En contexte produit : « inférence d'auteur » explicite, aucune conformité revendiquée |
| **R-8** (quatre emplois de « control plane ») | `\bACP\b\|control plane\|plan de contrôle` | **Conforme** après correction — voir ci-dessous |

**Écart le plus grave de tout P4.2 — R-8, annexe D §D.1.** La section qui **fait autorité** sur R-8 énonçait : « (a), (b) et (c) sont **sans aucun rapport** ». Vérification contre le socle : **F-48 établit l'absence de lien pour un seul couple**, (a)/(b) — « pure homonymie ». R-8 ne dit des autres que « objets distincts », **sans source ni balayage**. Or (a) et (c) sont **tous deux des objets d'IBM** : le couple où l'affirmation est la moins évidente est celui sur lequel elle était portée. C'est la faute que §4.4 nomme — *absence de documentation présentée comme fait négatif vérifié* — commise par le fichier qui la proscrit. **Elle avait déjà essaimé** : le ch. 1 §1.2 écrivait « le socle **atteste** trois emplois sans rapport entre eux ». Corrigés tous deux.

**Deux autres écarts corrigés.** (1) Annexe D §D.1 imposait « jamais dans un chapitre traitant des protocoles » — nulle part au socle, et **contredisant R-8**, qui prescrit le rappel de la désambiguïsation au ch. 3, chapitre de protocoles. (2) Le motif §4.3 `Forrester|TEI|Celent|ROI` n'était **pas ancré** : en français, `ROI` matche *t**roi**s*, *c**roi**sement*, *d**roi**t*. **769 occurrences sur l'ouvrage, 92 % de bruit** — le balayage exhaustif de ce critère en dépendait. Ancré (`\bROI\b`, `\bTEI\b`) : 58 occurrences, dont les seules réelles en prose sont *Forrester*, nommé comme commanditaire (§8.2.7). Relevé indépendamment par deux rédactions.

---

## CA-3 — Attribution

> *Toutes les métriques auto-déclarées attribuées conformément à §8.2.*

| Contrôle exécuté | Résultat |
|---|---|
| Balayage `[0-9]+ ?%\|M\$\|G\$\|heures\|modèles en production` sur les 29 pièces, inspection de chaque occurrence | **Conforme** après correction |
| §8.2.6 — la projection de ~70 % | **Conforme.** Présentée comme **projection** du BSIF et de l'ACFC à chaque occurrence, jamais comme taux observé |
| §8.2.7 — études d'analystes | **Conforme.** Commanditaire nommé |
| §8.2.1 — « soutien ≠ production » | **Conforme.** Les 60+ organisations d'AP2 sont un **soutien déclaré** |

**Écart corrigé — et il est instructif.** L'avant-propos citait « 90 % de quinze cents courriels » et « quinze heures à moins de trois minutes » **sans nommer les institutions**, en s'accordant une exemption : les chiffres y figuraient comme *illustrations de la règle d'attribution*, non comme faits. La relecture adversariale a **refusé l'exemption**, et elle avait raison : PRD §7.5 dit « à chaque occurrence » et ne connaît pas d'exception d'usage illustratif ; §8.2.2 vise nommément ces deux chiffres. **Le paragraphe qui énonçait la règle était celui qui l'enfreignait** — et sa phrase suivante prononçait sa propre sentence : « un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait ». La Banque Scotia (F-21) et TD (F-17) sont nommées, avec source et date ; les ordres de grandeur sont rendus tels que le socle les porte (« ~90 % », « ~1 500 ») et non durcis.

Le ch. 17 — le chapitre où la règle pèse le plus — est **conforme sans réserve** : chaque métrique porte « déclare », sa source et sa date, et le chapitre expose jusqu'à la correction du socle sur le « 8 000 » de BMO (des **employés**, non des politiques).

---

## CA-4 — Datation

> *Chaque chapitre porte sa date de gel ; les faits sensibles (§8.3) revalidés à la publication.*

| Contrôle exécuté | Résultat |
|---|---|
| Les 29 pièces portent-elles une date de gel dans leur en-tête ? | **Conforme — 29/29** |
| Le registre `99-registre-gel.md` les recense-t-il toutes ? | **Conforme — 29 lignes** après correction |
| Revalidation < 30 jours à la publication (DoD §8) | **Conforme.** P4.1 exécutée le **17 juillet 2026** — le jour même |

**Répartition** : 22 pièces gelées au 16 juillet 2026 ; 7 au 17 juillet (ch. 13, ch. 21, avant-propos, annexes A à D).

**Écart corrigé.** Le registre ne portait « une ligne par **chapitre** fusionné » — donc **aucune ligne d'annexe** —, alors que ce critère exige une date de gel de chaque pièce publiée. Les annexes étaient gelées mais non enregistrables. Signalé par la rédaction de l'annexe A ; portée du registre étendue à toute pièce publiée.

**P4.1 — huit faits chauds, aucun amendement matériel requis.** Six revalidés par lecture directe d'une source primaire ; deux partiellement (`lautorite.qc.ca` renvoie 403 aux outils — **déclaré et tracé, non contourné**). La RC MCP du 28 juillet 2026 est **confirmée à l'échéance**, ni avancée ni reportée.

**Ce que le lecteur doit savoir, et que l'avant-propos lui dit** : les chapitres 1, 2 et 7 décrivent MCP comme protocole à état **douze jours** avant une révision qui l'en retire. Ils portent leur date ; ils ne s'en excusent pas.

---

## CA-5 — Bilinguisme terminologique

> *Terminologie anglaise entre parenthèses à la première occurrence ; citations verbatim en langue originale.*

| Contrôle exécuté | Résultat |
|---|---|
| Le glossaire (annexe D) est-il utilisable comme instrument du critère ? | **Conforme** après correction |
| Terme anglais en italique entre parenthèses à la première occurrence | **Conforme** par échantillonnage sur les 24 chapitres |
| Citations verbatim en langue originale | **Conforme.** Les citations d'E-23 sont en anglais ; l'art. 12.1 en français ; l'avis 11-348 est rendu en français **et le dit** — le socle n'en porte pas le libellé anglais |

**Limite assumée, non comblée.** Le socle ne porte aucune glose anglaise pour l'avis 11-348 ni pour l'art. 12.1, ni le terme anglais d'origine de la « multi-location d'entreprise » (§10.9) ni de l'« actionnabilité conversationnelle » (§10.10). **Aucune traduction n'est inventée** — c'est la bonne réponse, et la dette du ch. 18 sur ce point est close comme **non actionnable**.

**Écarts corrigés au glossaire — cinq sur-qualifications.** Le glossaire **définissait**, sous trace F-xx, cinq objets que le PRD déclare non caractérisés : le *frame* opérationnel (§10.10 — « seul le frame normatif est caractérisé »), trois risques protocolaires (§10.8 — le socle les « **nomme** », sans mécanique ni datation) et l'assurance de correction (F-37 la liste sans la définir). Vecteur d'erreur silencieux dans sa forme pure : plausible, estampillé, et chaque chapitre s'y fie. La clôture de P1 en avait déjà corrigé quatre ; ce n'étaient pas les dernières.

---

## CA-6 — Honnêteté des lacunes

> *Les questions ouvertes (§10) sont exposées, pas masquées.*

| Contrôle exécuté | Résultat |
|---|---|
| Chacune des **onze** lacunes de PRD §10 est-elle portée par au moins une pièce ? | **Conforme** après correction |
| Les gabarits d'encadré de §4.4 sont-ils employés correctement (trois cas) ? | **Conforme** après correction |
| Les échecs d'élévation sont-ils exposés ? | **Conforme.** FTM/ISO 20022 (§10.6) exposé comme échec, non comblé ; BMO et Sun Life en élévation **partielle**, résidus [C] dits comme tels |

**Écart corrigé — et je l'avais créé le matin même.** La lacune **§10.11** (F-11 attribue au Budget 2025 la supervision par la Banque du Canada **sans la dater**) a été ouverte le 17 juillet et n'était portée par **aucun chapitre** : les vingt-quatre étaient gelés, et le ch. 21 recensait encore « dix lacunes ». Elle est désormais exposée au ch. 21 §21.1 et en encadré à l'annexe C ; le chapitre est regelé au 17 juillet.

**Écart corrigé — encadré du ch. 13.** L'encadré sur la ligne directrice de l'AMF employait le gabarit du **cas 1** (« Recherche menée le [date] ») sur une lacune **non instruite** — précisément ce que §4.4 signale comme **induisant la fabrication d'une passe qui n'a pas eu lieu**. Converti au cas 2, et enrichi du 403 constaté par P4.1.

**Ce que ce critère protège.** La ligne directrice sur l'IA de l'AMF est finale depuis le 30 mars 2026 ; son contenu n'est pas au socle. L'ouvrage n'en dérive **aucune** contrainte et le dit — au chapitre pivot, sur l'un des deux textes qui fixent l'échéance du 1er mai 2027. C'est le vide le plus coûteux de l'ouvrage, et il est exposé plutôt que reconstruit.

---

## CA-7 — Relecture

> *Passe de vérification finale point par point contre le PRD avant livraison.*

| Contrôle exécuté | Résultat |
|---|---|
| Chaque pièce a-t-elle passé la boucle §4.2, dont la **relecture adversariale par un relecteur distinct** (§4.2.4) ? | **Conforme — 29/29** |
| La présente grille est-elle remplie point par point contre PRD §11 ? | **Conforme** — c'est ce document |

**Couverture.** Les 24 chapitres ont été relus en P2/P3. Les 5 pièces de P4 — avant-propos, annexes A à D — l'ont été le **17 juillet 2026**, par trois relecteurs distincts de leurs rédacteurs. Verdicts initiaux : **avant-propos non publiable** (3 bloquants), **annexes A et C non publiables**, **annexes B et D non publiables**. Tous les bloquants ont été traités ; chacun a été **revérifié contre le PRD avant correction**, et l'un d'eux (« 4 701 irreproductible ») s'est révélé **infondé** — le chiffre l'est par la commande de référence, et c'est la coexistence de commandes maison périmées qui trompait le relecteur. Le défaut sous-jacent était réel ; le constat ne l'était pas.

**Ce que la relecture a coûté, et ce qu'elle a rapporté.** Le ch. 13 — chapitre pivot — a reçu le verdict le plus dur : « la passe du 17 juillet a **construit correctement et vérifié incorrectement** ». Les cinq dérivations E-23 étaient défendables ; l'appareil de vérification ne l'était pas. Six bloquants, dont une **certification d'arbitrage fausse** que j'avais moi-même écrite (« le §13.2 est conforme au socle corrigé » — sans avoir ouvert le PRD, dans un fichier qui porte trois blocs plus haut la leçon qui l'interdit).

---

## CA-8 — Traçabilité du blueprint

> *Chaque composant, principe et correspondance de la Partie VII tracé vers F-38..F-46 (ou le socle général) ; chaque lien réglementaire porte son statut « documenté » ou « inférence d'auteur » ; neutralité fournisseur (§8.4) contrôlée.*

| Contrôle exécuté | Résultat |
|---|---|
| Tableau B.3 (ch. 23) — chaque lien porte-t-il son statut ? | **Conforme** |
| Annexe B — colonne « Statut du lien » sur les 15 croisements | **Conforme.** 15/15 renseignés ; **zéro** cellule sans statut ; **zéro** statut « documenté » — conforme au ch. 18, qui établit qu'**aucun** des quinze croisements n'est documenté par une source du socle |
| Neutralité fournisseur §8.4 | **Conforme.** IBM est un cas d'instanciation documenté ; alternatives par renvoi ; faits négatifs exposés (dépréciation Event Streams/EP ; R-6 ; R-7 — aucune conformité E-23/B-13 revendiquée) |
| Strates de F-09 dans la Partie VII et les annexes | **Conforme.** Aucune occurrence de « F-09 (niveau [A]) » sur un contenu [B] |

**Écart corrigé — annexe B.** La règle du fait négatif vérifié était énoncée comme « réservé aux **deux** entrées […] **et à elles seules** : F-09 et F-35 ». §4.4 l'ouvre à **trois** (F-35, F-09, **F-46**). Le ch. 18 avait la formulation juste parce qu'il la **bornait** à sa matrice ; la borne avait sauté, le cardinal était resté.

**Non-sur-correction, vérifiée.** Le ch. 20 emploie « fiches de modèles » pour watsonx.governance : le terme est **exact pour ce produit** (F-44), en contexte produit et attribué à la documentation d'IBM. La réserve de F-09 vise E-23, pas IBM. Corriger ici aurait été une faute symétrique — le glossaire §D.7 porte désormais la distinction explicitement.

---

## Ce que cette grille ne dit pas

Elle ne dit pas que l'ouvrage soit exact : elle dit qu'il a passé les huit contrôles que le PRD s'est donnés, et que les écarts trouvés ont été corrigés plutôt qu'absorbés. Elle ne remplace pas la lecture d'une source primaire par qui construit sur ces pages.

Elle ne dit pas non plus que le dispositif soit suffisant. Les défauts les plus lourds trouvés le 17 juillet — un fait négatif fabriqué dans le fichier qui fait autorité, une attestation contredite par la mesure, un motif de balayage à 92 % de bruit, une commande de référence testée sur deux fichiers et publiée pour vingt-neuf — **ont tous été trouvés par des relecteurs adversariaux, aucun par l'auto-contrôle de leur rédacteur**. C'est le résultat le plus solide de cette passe, et il vaut d'être retenu : **un rédacteur ne vérifie pas ce qu'il croit avoir fait.**

---

## Addendum du 17 juillet 2026 — ce que l'audit global a démenti

Cette grille a été soumise, le jour même de sa rédaction, à un **audit global indépendant** ([`audit.md`](../audit.md)) qui l'a traitée comme du contenu à vérifier, non comme une preuve — conformément à sa propre règle. **Elle n'en sort pas indemne, et c'est la bonne nouvelle** : le dispositif fonctionne quand on l'applique à ses propres attestations.

**Deux critères ne tenaient pas en l'état constaté :**

- **CA-1 (traçabilité)** — déclaré conforme ici, il portait des écarts réels : un marquage de F-09 « élevée [C]→[B] » au ch. 19 reproduisant **mot pour mot la formulation que le PRD déclare « doublement fausse »** (la passe corrective de la v1.7 avait atteint les ch. 18 et 20, jamais le 19) ; deux gloses anglaises hors socle aux ch. 10 et 11, contre un arbitrage rendu au ch. 13 ; une partition d'institutions fausse et certifiée exhaustive au ch. 17.
- **CA-7 (relecture)** — déclaré « conforme — 29/29 ». Le constat est **exact**, mais il était **contredit** par le registre de gel, qui affirmait au même moment que cinq pièces n'étaient pas relues. La grille avait raison ; elle ne l'a pas emporté, parce que deux attestations qui se contredisent n'attestent plus rien. Le registre a été réaligné (M-15).

**Trois racines siégeaient hors des chapitres** — dans les documents de gouvernance eux-mêmes : PRDPlan §4.4 se contredisait sur « établi »/« vérifié » (le ch. 23 a suivi une ligne, le ch. 24 l'autre) ; la formule §8.2.4 avait été enrichie après le gel des ch. 9-11, qui en attestaient un verbatim devenu inexact ; le TOC portait trois dettes que des chapitres publiés réclamaient. Toutes tranchées le 17 juillet (PRD v1.10, PRDPlan v1.4, TOC v1.5).

**Ce que cet addendum établit, et qui vaut plus que le score.** Cette grille avait écrit : « *un rédacteur ne vérifie pas ce qu'il croit avoir fait* ». L'audit en donne le corollaire, aux dépens de la grille elle-même : **un contrôle ne vérifie pas ce qu'il croit avoir contrôlé.** Le « 8/8 » n'était pas mensonger — il était *incomplet*, et il l'ignorait. Aucun des écarts ci-dessus n'a été trouvé par les huit contrôles de cette page ; tous l'ont été par une passe qui les a refaits sans les croire. C'est le seul argument sérieux en faveur d'une relecture externe, et il est ici démontré plutôt qu'invoqué.

**Statut des critères au 17 juillet 2026, après les corrections de l'audit** : les écarts relevés ont été corrigés dans les pièces et les racines tranchées en gouvernance. **Ce statut n'est pas une nouvelle attestation de conformité** : il faudrait, pour la donner, une passe qui refasse les huit contrôles sur l'état corrigé — et une passe distincte de celle qui a corrigé. Elle n'a pas eu lieu. *La grille dit ce qu'elle a fait, pas ce qu'elle espère.*
