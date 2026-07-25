# Audit global du contenu de la monographie

| Champ | Valeur |
|---|---|
| Date | 17 juillet 2026 |
| Objet | Audit de conformité de la monographie publiée (`mono-v1.0`) au regard de [PRD.md](PRD.md) v1.9 (socle §7, garde-fous §8, lacunes §10, critères §11), de [PRDPlan.md](PRDPlan.md) v1.3 (§4.2–4.4) et de [TOC.md](TOC.md) v1.4 |
| Périmètre | Les 29 pièces publiées (24 chapitres, avant-propos, annexes A–D), plus `monographie/README.md`, `monographie/99-registre-gel.md`, et les documents de gouvernance en incidence |
| Méthode | Sept relectures adversariales parallèles (une par groupe de pièces), chacune contre le PRD lu en entier ; contrôles mécaniques transversaux (identifiants F-xx, notes, motifs interdits §4.3, dates de gel, décomptes, liens) ; **contre-vérification à la source, par l'auditeur principal, de chacun des constats majeurs** — voir §8 |
| Posture | **Aucune attestation antérieure créditée sans constat.** La grille `verification/relecture-CA.md` (« 8/8 conformes ») a été traitée comme du contenu à vérifier, non comme une preuve |
| Résultat | **0 bloquant ; 15 constats majeurs ; 44 constats mineurs ; 29 observations** — décomptes recomptés sur les tableaux du présent document avant livraison |
| Nature | Audit en lecture seule à sa rédaction. ⚠ **EXÉCUTÉ INTÉGRALEMENT le 17 juillet 2026** à la demande de l'auteur — voir §9 « Exécution » en fin de document. Toutes les corrections ont suivi le processus du projet : socle d'abord, boucle §4.2 avec relecteur distinct, version++ |

---

## 1. Verdict d'ensemble

**La monographie tient ses garde-fous de fond.** Sur les 29 pièces, le balayage exhaustif des huit garde-fous (R-1 à R-8) ne relève **aucune affirmation réfutée** : l'ACP protocolaire est partout présenté comme fusionné dans A2A ; le RTR n'est jamais dit lancé et la cible T4 2026 est partout attribuée ; FDX reste une anticipation d'industrie ; aucune conformité E-23/B-13 n'est revendiquée pour IBM ; « exigé par E-23 » et « fiche de modèle » prêtés au BSIF : zéro occurrence ; « trois sources indépendantes » : zéro assertion. L'attribution des métriques auto-déclarées (CA-3) est tenue presque sans faute — le chapitre 17, le plus exposé, est exemplaire. Les onze lacunes de PRD §10 sont toutes exposées et aucune n'est comblée par du non-vérifié. Les 29 dates de gel sont présentes et concordent avec le registre.

**Les défauts trouvés relèvent, pour l'essentiel, de deux mécaniques que le projet a lui-même nommées :**

1. **La cascade interrompue.** Un correctif de gouvernance adopté après le gel d'une pièce n'a pas été propagé à toutes les pièces qui portaient la formulation corrigée : « dès l'origine » (retiré du TOC, toujours au ch. 1 et dans l'en-tête du ch. 4) ; la glose « mémoire persistante » (rétractée au glossaire le 17 juillet, toujours au ch. 4) ; l'« indépendance » des sources académiques (retirée du socle en v1.5, toujours affirmée au ch. 6) ; le marquage F-09 « [A/B mixte] » (PRD v1.7, appliqué aux ch. 18 et 20, jamais au ch. 19) ; la formulation imposée de PRDPlan §4.4 (enrichie après le gel des ch. 9-11, qui attestent un verbatim devenu inexact).
2. **Le statut qui ment** — la maladie que le PRD v1.9 diagnostique dans ses propres registres. Le registre de gel contredit frontalement la grille CA-7 sur la relecture des cinq pièces de P4 ; le README publie un décompte de mots faux (88 021) en citant la méthode qui donne 90 362 ; quatre pièces portent des blocs « À FAIRE » ou « reste dû » périmés ; l'annexe B se déclare « premier jet, relecture NON FAITE » alors qu'elle est relue et publiée ; l'annexe A atteste « 2043 mots » là où la commande de référence en mesure 2046 ; le ch. 17 certifie « exhaustive » une partition qui omet RBC.

Aucun de ces défauts ne renverse une conclusion de l'ouvrage. Plusieurs, en revanche, touchent ce que l'ouvrage vend de plus précieux — la traçabilité de chaque affirmation vers le socle — et la grille « 8/8 conformes » de `verification/relecture-CA.md` est **partiellement démentie** : CA-1 (traçabilité) et CA-7 (relecture) ne tiennent pas en l'état constaté ; CA-4, CA-5 et CA-6 portent des accrocs localisés ; CA-2, CA-3 et CA-8 tiennent.

---

## 2. Constats majeurs (15)

Chaque constat a été contre-vérifié à la source par l'auditeur principal (citation relue dans le fichier), sauf M-07, retenu sur la preuve du relecteur avec une racine à arbitrer.

| # | Lieu | Constat | Référence |
|---|---|---|---|
| M-01 | [00-avant-propos.md:21](monographie/00-avant-propos.md:21) | Deux universels négatifs présentés comme des faits : « Aucun régulateur canadien n'a écrit une ligne sur l'orchestration agentique ; aucune spécification protocolaire ne mentionne un texte canadien ». Le socle ne peut vérifier ni l'un ni l'autre — le contenu de la ligne directrice IA de l'AMF n'y est pas (§10.4) et aucun balayage des spécifications n'est documenté. Le même fichier enseigne la distinction « absence de documentation ≠ fait négatif vérifié » | PRD §10.4 ; PRDPlan §4.4 |
| M-02 | [ch-01:85](monographie/01-partie-I/ch-01-genealogie-gouvernance.md:85) | « le chapitre 4 documente les surfaces d'attaque connues **dès l'origine** » — formulation dont le TOC documente le retrait (correctif du 16 juill., TOC v1.3) et que le ch. 4 refuse lui-même d'affirmer (ch-04:39). Correctif non cascadé | PRD §10.8 ; TOC.md:85 |
| M-03 | [ch-04:11](monographie/01-partie-I/ch-04-risques-protocolaires.md:11) | L'en-tête attribue au TOC la thèse d'**avant** correctif (« documentés dès l'origine ») alors que TOC.md:84 porte la thèse amendée (« sans que le socle en date la documentation »). L'en-tête publié affirme ce que le corps réfute | TOC.md:84-85 |
| M-04 | [ch-04:27](monographie/01-partie-I/ch-04-risques-protocolaires.md:27) | « Le socle le définit par ce qu'il corrompt : la mémoire **persistante** de l'agent » — le glossaire établit l'inverse : « aucune caractérisation au socle. *(Glose d'auteur retirée le 17 juill. 2026.)* ». Rétractation non cascadée ; l'inférence qui suit repose sur cette prémisse | annexe-d:70 ; PRD §10.8 |
| M-05 | [ch-06:41](monographie/02-partie-II/ch-06-autonomie-encadree.md:41) | « les deux cadres sont indépendants » (F-36/F-37) — le socle réfute lui-même l'indépendance (Rinderle-Ma cosigne les deux, correctif F-46 v1.5) et le ch. 5 (l. 87) affirme l'inverse dans la même partie. Le bloc qualité du fichier porte encore la doctrine d'avant l'arbitrage | PRD §7.8 (F-46) |
| M-06 | [ch-09:115](monographie/03-partie-III/ch-09-e23-risque-modele.md:115) | Stratification F-09 fausse : la note [^1] range sous « Strate [A] mobilisée » l'anticipation de l'autonomie et le fait négatif — contenus que le PRD range expressément sous [B] (l'énumération [A] est close). Corollaire au corps (l. 49). C'est la classe de faute que le PRD §7 signale nommément | PRD §7.3 (F-09) |
| M-07 | [ch-09:55](monographie/03-partie-III/ch-09-e23-risque-modele.md:55) | Attestation de reproduction « sans altération » / « verbatim » de la formulation imposée §4.4, dont le texte actuel porte des membres absents du blockquote §9.3. La substance (§8.2.4) est respectée ; l'attestation est fausse au regard du référentiel actuel. Racine probable : §4.4 amendé après le gel sans cascade — à arbitrer en gouvernance | PRDPlan §4.4 |
| M-08 | [ch-10:57](monographie/03-partie-III/ch-10-vide-federal-c36.md:57) | Glose anglaise « (*decision based exclusively on automated processing*) » : le socle (F-27) ne porte que le texte français ; l'arbitrage consigné au ch. 13 établit que cette glose « ne peut pas être rendue par l'auteur » (élévation primaire requise) | PRD §7.3 (F-27) ; ch-13 (arbitrage f) |
| M-09 | [ch-11:39](monographie/03-partie-III/ch-11-quebec-amf-loi25.md:39) | Même glose anglaise hors socle — aggravée : le bloc qualité la présente comme **correctif CA-5** (« CA-5 était MANQUÉ… Corrigé »), attestation de conformité posée sur un contenu non tracé | idem M-08 |
| M-10 | [ch-15:79](monographie/04-partie-IV/ch-15-iso20022-lynx-rtr.md:79) | L'encadré §10.5 attribue au socle des sources qu'il ne contient pas : « aucune source du socle — pages officielles de Paiements Canada, **spécification AP2**, **communiqués Interac** — ». La spécification AP2 n'est pas au socle (F-04 ; §10.9e) — le ch. 16 le dit correctement — et les communiqués Interac n'y figurent pas. Surdéclaration du périmètre vérifié | PRD §7.1 (F-04), §10.5, §10.9 |
| M-11 | [ch-15:13](monographie/04-partie-IV/ch-15-iso20022-lynx-rtr.md:13) ↔ [TOC.md:155](TOC.md:155) | Amendement du TOC (intitulé §15.4) déclaré « dû » par le chapitre publié et jamais exécuté : le TOC porte toujours « richesse des données ». La bijection J-2 — critère de gouvernance du TOC — est rompue à la publication | TOC.md ; PRDPlan §3 |
| M-12 | [ch-17:19](monographie/05-partie-V/ch-17-etudes-de-cas.md:19) | Partition des dix institutions fausse deux fois : « **Trois** d'entre elles publient des sources primaires… : les communiqués de TD et de CIBC, les rapports annuels de Desjardins et d'Intact » (quatre institutions) ; et **RBC n'est classée dans aucune des trois catégories**. Le bloc qualité certifie la partition « refaite et rendue exhaustive sur les dix » — attestation fausse | PRD §7.5 ; leçon « un statut qui ment » |
| M-13 | [ch-19:124](monographie/06-partie-VI/ch-19-architecture-reference.md:124) | Marquage F-09 « niveau [B] — **élevée [C]→[B]** … PRD v1.6 » : reproduction mot pour mot de la formulation que le PRD déclare « **doublement faux** » (l'entrée n'a jamais été [C] ; [B] est sous [A] ; entrée [A/B mixte] depuis v1.7). Présent aussi en prose (l. 100 : « l'élévation de F-09 en [B] ») et au journal. La passe corrective v1.7 a atteint les ch. 18 et 20, jamais le ch. 19 | PRD §7.3 (F-09) |
| M-14 | [monographie/README.md:10](monographie/README.md:10) | « **88 021 mots** sur 29 pièces (méthode de décompte : PRDPlan §4.2) » — la commande de référence de PRDPlan §4.2, réexécutée sur les 29 pièces, donne **exactement 90 362**, chiffre que portent PRD §12, PRDPlan §1.4 et TOC. Le README contredit le document d'autorité et sa propre méthode déclarée | PRD §12 ; PRDPlan §4.2 |
| M-15 | [99-registre-gel.md:41](monographie/99-registre-gel.md:41) ↔ [relecture-CA.md:136](verification/relecture-CA.md:136) | Contradiction frontale sur la relecture adversariale des pièces P4 : le registre déclare « Cinq pièces portent un premier jet **sans** relecture adversariale… Elles ne sont pas présentées comme revues » (lignes 31-34 : « relecture adversariale due ») ; CA-7 déclare « Conforme — **29/29** », relectures du 17 juillet. État constaté dans les fichiers : annexes A, C, D **relues** (constats énumérés et appliqués — le registre est périmé) ; avant-propos relu dans les faits mais d'en-tête « premier jet » ; **annexe B ambiguë** — une rectification y est étiquetée « (relecture adversariale) » mais son bloc de gouvernance maintient « NON FAITE… reste DUE » : sur cette pièce, c'est CA-7 qui survend. Un des deux documents d'attestation ment nécessairement | PRDPlan §4.2.4 ; PRD v1.9 |

---

## 3. Constats mineurs (44)

| # | Lieu | Constat |
|---|---|---|
| m-01 | avant-propos:53 | Métrique TD (15 h → <3 min) sans source primaire ni date en prose (Scotia en a) ; l'auto-contrôle (l. 109-110) atteste pourtant « les deux institutions… avec source et date » |
| m-02 | avant-propos:5 | En-tête « Statut : Rédigé (premier jet) » alors que la relecture adversariale est faite (bloc l. 125 ; CA-7) |
| m-03 | ch-01:67 | « 65+ entreprises » AGNTCY non attribué au communiqué ni daté en prose (§8.2.1) — juxtaposé sans date aux chiffres d'avril 2026, comparaison que le ch. 3 qualifie lui-même de fautive |
| m-04 | ch-01:31 | Sigle « ACP » nu en emploi référentiel dans la séquence F-06 (« MCP → ACP → A2A → ANP ») — **seule entorse de forme à R-8 relevée sur l'ouvrage** ; désambiguïsée à la phrase suivante, et le ch. 3 (l. 61) rend la même séquence qualifiée |
| m-05 | ch-02:1 | Titre H1 divergent du TOC amendé (« deux protocoles complémentaires » vs « une complémentarité déclarée ») |
| m-06 | ch-02:13 | Bannière « l'amendement de TOC.md… reste dû » périmée — l'amendement est fait (TOC.md:73) |
| m-07 | ch-02:146-148 | Bloc « Commit + registre… À FAIRE » périmé ; et le point de revalidation P4.1 que le chapitre exige (statuts infonuagiques F-03) est absent de la table du registre |
| m-08 | ch-03:157 | Bloc « À FAIRE » périmé (chapitre enregistré, commit `cb4608f`) |
| m-09 | ch-04:41 | Encadré au gabarit « cas 1 » (« Recherche menée le… ») pour la lacune §10.8 non instruite — le gabarit cas 2 existe pour ce cas ; atténuant : l'absence de passe externe est dite |
| m-10 | ch-04:121 | Bloc « À FAIRE » périmé (commit `dc0a394`) |
| m-11 | ch-07:53 | Rendu français entre guillemets présenté comme citation (« sur une dorsale Kafka fiable et rejouable ») — l'original anglais n'est pas au socle ; le cas identique (F-16) a été corrigé en relecture. Racine : le PRD (F-33) porte lui-même ce rendu guillemeté |
| m-12 | ch-07:11 | Thèse d'en-tête « support MCP **généralisé** » (TOC v1.4) réfutée deux fois par le corps (l. 47, 99) — conflit en-tête/corps vivant dans la pièce publiée, amendement TOC non demandé |
| m-13 | ch-08:49 | « ce que le manifeste APM **appelle** un *frame* opérationnel » — le manifeste n'applique pas ce terme à cet objet (le frame opérationnel n'est pas caractérisé au socle, §10.10a) ; marqué « Lecture de l'auteur », note fidèle |
| m-14 | ch-08:107 | Note [^7] : « F-09 et F-25 (niveau [A]) » à plat — l'entrée F-09 est [A/B mixte] et « le marquage individuel prime » ; et « fait négatif » employé pour une absence de documentation (formule de distinction §4.4 non appliquée) |
| m-15 | ch-09:89-93 | Encadré §9.4 au gabarit cas 1 pour une lacune non instruite (« aucune passe primaire dédiée n'a été conduite ») — substance honnête, forme non conforme |
| m-16 | ch-10:55 | « que les institutions **doivent traiter comme acquise** » — recommandation que le ch. 9 marque « Lecture de l'auteur », ici assertée sans marqueur |
| m-17 | ch-10:81 | Note [^4] : « reprise **mot pour mot** » de la formulation §4.4 — inexact au regard du texte actuel du gabarit |
| m-18 | ch-11:41 + 107 | « toute entreprise » entre guillemets sous une note déclarant « verbatim du texte officiel » — membre que le socle porte hors guillemets (le ch. 13 l'exclut expressément de sa déclaration de verbatim) |
| m-19 | ch-11:67 | Encadré §11.3 au gabarit cas 1 pour la lacune §10.4 non instruite — le ch. 13 emploie le cas 2 pour la même lacune |
| m-20 | ch-11:51 + 103 | Attestations « dans la forme §4.4 » / « rétablie caractère pour caractère » inexactes au regard du texte actuel du gabarit |
| m-21 | ch-12:83 | Note [^2] : la vérification négative d'E-23 rangée en « seule strate [A] » — le PRD la range expressément sous [B] |
| m-22 | ch-12:35 | Gloses anglaises « (*autonomy*) », « (*adaptiveness*) » hors socle (F-26 : rendu français seul) — le ch. 13 a retiré ces gloses exactes sur relecture |
| m-23 | ch-16:41 | Divergence de découpage §16.2 vs TOC (« Scénarios d'articulation » → « Conditions de possibilité ») bien fondée au socle mais non déclarée — bijection J-2 rompue silencieusement, sans l'encadré de correctif que le ch. 15 s'impose |
| m-24 | ch-17:15 | « Cinq appuis pour dix institutions » — décompte catégoriellement faux : les rapports annuels (déclarations d'entreprise, §8.2.2) comptés comme corroboration externe ; finos.org (F-20) non compté |
| m-25 | ch-17:137 | Inférence Lumi ↔ Loi 25 (« le caractère bilingue… ce que la Loi 25 exige ») hors socle et sans marqueur « Lecture de l'auteur » |
| m-26 | ch-19:7 | En-tête : F-17, F-21, F-28 déclarés « en renvoi » alors qu'ils portent des faits au corps (§19.2) — l'en-tête est la liste de référence du contrôle CA-1 |
| m-27 | ch-19:27 | « frames » nu dans le tableau §19.1 avant sa première glose (CA-5), sous une attestation de liste « re-vérifiée terme à terme » |
| m-28 | ch-20:15 | Partition du ch. 18 mal paraphrasée : « les deux autres lignes… sont vides du côté des attentes » assimile deux espèces que le ch. 18 distingue expressément (AMF : premier terme manquant ; cadre bancaire : vide de texte) |
| m-29 | ch-21:134 | Note [^20] : « F-09 (niveau [B]) » sur un fait de strate [A] (entrée en vigueur) — sous-étiquetage, sens inverse de la faute proscrite mais marquage non rectifié |
| m-30 | ch-21:6/74/128 | Décomptes non ré-ancrés après le re-gel au 17 juillet : « douze jours après la date de gel » (17 → 28 juill. = onze) ; notes [^17] et [^20] ancrées au 16 juillet |
| m-31 | ch-21:145 | Journal : « 21 notes » — le fichier en définit 22 ([^22] ajoutée à l'amendement du 17 juillet) |
| m-32 | ch-21:25 | « Deux [lacunes] ne se comblent par aucune recherche » — inexact pour le volet AMF de §10.4 : le texte est final depuis le 30 mars 2026 et se comble par extraction primaire (ce que disent les ch. 18 et 20) |
| m-33 | ch-22:39 | « le socle n'a pas **vérifié** l'absence de revendication » — vocabulaire « vérifié » hors des trois entrées auxquelles §4.4 le réserve (racine : contradiction interne de PRDPlan §4.4, voir §5.G-1) |
| m-34 | ch-23:97 | Note [^1] : règle de réservation fausse — « terme réservé aux faits négatifs **[A]** » ; §4.4 le réserve à **trois entrées** (F-35 [A], F-09 [B], F-46 [B]), pas à un niveau. La conclusion est juste, le motif est faux |
| m-35 | ch-23:7 | En-tête « Socle mobilisé » sous-déclaré : manquent F-17, F-23, F-33, F-36 (mobilisés au corps ou en notes) |
| m-36 | ch-24:63 | « Ce fait négatif a été **vérifié** » (E-23/B-13) — même vocabulaire réservé ; le ch. 23 dit « établi » pour le même fait : les deux chapitres divergent en s'appuyant chacun sur une ligne de §4.4 |
| m-37 | ch-24:65 | Seconde occurrence (« L'absence de revendication est vérifiée… ») |
| m-38 | ch-24:125 | Note [^8] : partenaires RTR « avec CGI et Interac » sans **Deloitte Canada** — F-29 [A], revalidée, prime pour l'énumération (règle que le ch. 23 pose et que le ch. 22 a appliquée) |
| m-39 | ch-24:7 | En-tête omet F-36 et F-37, mobilisés au §24.1 (convergence) |
| m-40 | annexe-a:257 | Attestation « Résultat : **2043 mots** » — la commande de référence mesure **2046** (titre §A.5 modifié dans le même commit sans re-mesure). Un cardinal faux certifié dans le bloc qui fait la leçon sur les cardinaux faux |
| m-41 | annexe-b:5/335/338/464 | Statut menteur : en-tête « Rédigé (premier jet) », bloc « RELECTURE ADVERSARIALE… NON FAITE… reste DUE avant fusion » — pour une pièce relue (PRDPlan §1.4), fusionnée et publiée sous `mono-v1.0` |
| m-42 | annexe-c:38 | Expansion « (*Agent Communication Protocol*) » non tracée (racine : annexe D) |
| m-43 | annexe-d:8 | L'en-tête « Garde-fous » omet **R-6**, présent en §D.7 depuis le 17 juillet — même classe d'erreur que l'omission de F-26 que ce même en-tête raconte |
| m-44 | annexe-d:23 | La **forme imposée** de la branche (a) de R-8 fixe l'expansion « *Agent Communication Protocol* », absente du socle (PRD et TOC : 0 occurrence ; F-43 dit « le protocole ACP » sans l'expandre) — élément non tracé essaimé dans ~8 chapitres et l'annexe C, alors que le projet refuse ce geste ailleurs (« aucune traduction à inventer », §10.9) |

---

## 4. Observations (29)

Sans exigence de correction ; consignées pour une reprise future.

1. avant-propos:19 — « mis en production » couvre trois familles dont la seule plateforme agentique d'entreprise du socle (Manuvie/Akka, F-22) était « en bêta » à l'annonce.
2. ch-01:77 — prédiction (« peu de chances d'être abandonné dans les dix-huit mois… c'est exactement ce que ces chiffres établissent ») non marquée « Lecture de l'auteur ».
3. ch-01:61 et ch-03:37 — « quatre mois » dérivé d'un « mars 2025 » que F-05 ne date pas au jour (intervalle réel : 4 à ~5 mois).
4. ch-02 et ch-03 — la lacune §10.9 est exposée en prose et non en encadré, forme que TOC.md:254 assigne ; l'honnêteté CA-6 est satisfaite, la forme non.
5. ch-05:85 — encadré hybride : ouverture du cas 1 (« Recherche menée le… ») pour une recherche purement interne au corpus ; l'absence de recherche externe est dite.
6. ch-05:85 — « candidate à une entrée §10 » non rétro-annoté (la lacune est depuis §10.10) ; exact à la date de gel.
7. ch-05:91 — résidu « axe unique » en conclusion, corrigé en §5.1 (deux axes) par la relecture.
8. ch-07:27 — bidirectionnalité MCP (consommer/exposer) affirmée à l'indicatif sur la formule ambiguë de F-15 (« serveurs MCP appelables »).
9. ch-08:43 — « qui portent l'essentiel de la valeur d'architecture » : jugement d'auteur en incise non marqué.
10. ch-09:21-23 — « opposabilité » appliqué à E-23 (ligne fondée sur des principes, « should ») : tension avec la modalité « attendu », sans occurrence proscrite.
11. ch-10:49 — doctrine ACVM entre guillemets français sans la réserve de non-verbatim que le ch. 12 pose (instrument anglais).
12. ch-10:51 — « même véhicule législatif » pour la LPRPDE (loi modifiée, non véhicule).
13. ch-12:47-49 — clôture d'encadré (« en l'absence de source primaire extraite intégralement ») hors des trois gabarits §4.4 ; dette signalée par le chapitre, jamais versée en gouvernance.
14. ch-13:19-21 — titre §13.1 (« ce que les exigences imposent ») à la marge du motif F-09 bis ; le corps dit « attentes » partout.
15. ch-13:91 — encadré hybride cas 1/cas 2, défendable (la lecture intégrale des deux articles est une recherche réelle).
16. ch-13:459-471 — le bloc de traçabilité historique (« état du 16 juill. ») cite « PRD.md L180 » pour une formulation que le PRD ne porte plus — pointeur périmé qui peut égarer un mainteneur.
17. ch-14:45 — « les lignes directrices de la Partie III s'imposent à leurs assujettis sans acte préalable » : variante généralisée d'une caractérisation retirée du corps ; marquée « Lecture de l'auteur ».
18. ch-15:11 — bandeau de thèse au futur catégorique (« le RTR naîtra ») non attribué — reproduction fidèle de TOC.md:154 ; le corps attribue partout.
19. ch-17:181/199 — BMO comptée dans « quatre titulaires nommés au sommet » via un titre (Chief Data Analytics Officer) que F-47 n'établit que comme porte-parole du communiqué.
20. ch-17:191 — « six des dix publient un gain chiffré » englobe la **cible** RBC (700 M$–1 G$), qui n'est pas un gain.
21. ch-18:31/35 — le statut des croisements est porté par les règles de construction, non cellule par cellule ; l'exigence B.3 est satisfaite par construction globale.
22. ch-18:53 — « opposable après coup », aussitôt borné (« sans que le socle établisse qu'il suffise à une piste d'audit réglementaire »).
23. ch-20:49 — le parenthétique « (F-09) » du gabarit §8.2.4 omis ; les cinq membres présents, note traçante.
24. ch-22:96 — « s'échelonnent de décembre 2023 à juillet 2026 » : le dernier **statut** daté du tableau est du 30 juin 2026 (juillet = une annonce, exclue par la convention du chapitre).
25. ch-22:62/128 vs ch-23:65 — « Open Preview » rendu « préversion publique » ici, « préversion ouverte » là — pré-GA respecté, traduction non unifiée.
26. annexe-b:21 — l'énoncé de la règle 3 emploie « cellule » au sens que l'annexe rejette ailleurs (« le vide est celui du lien, jamais celui de la cellule ») ; le journal documente le piège.
27. registre-gel:9 — « destin d'ACP » : sigle nu dans un document interne (non une pièce publiée) — R-8 dit « dans tout l'ouvrage » ; à trancher.
28. annexe-d:48-55 — quatre gloses d'auteur restantes sous trace F-xx qui ne les porte pas textuellement (autonomie/automatisation ; traçabilité ; humain-dans-la-boucle ; *checkpointing*) — même classe que les cinq sur-qualifications retirées, gravité moindre (aucune n'est déclarée non caractérisée par §10).
29. PRDPlan §1.4 (P4.4) — « 38 liens, tous vérifiés » pour le README ; l'état actuel en compte 45, tous valides (décompte périmé, sans conséquence).

---

## 5. Racines de gouvernance

Quatre défauts ne siègent pas dans les pièces mais dans les documents qui les gouvernent — les corriger d'abord, sous peine de reproduire les écarts à chaque reprise (PRDPlan §7 : le socle d'abord, jamais les chapitres seuls) :

- **G-1 — PRDPlan §4.4 se contredit sur « établi »/« vérifié »** : une ligne nomme le cas « fait négatif **établi** (E-23, B-13 : R-7) », la ligne suivante écrit « ce fait négatif n'est **vérifié** que pour E-23 et B-13 », et la ligne « Fait négatif vérifié » réserve le terme à trois entrées (F-35, F-09, F-46). Le ch. 23 a suivi une ligne (en la citant mal), le ch. 24 l'autre — quatre mineurs (m-33, m-34, m-36, m-37) en découlent. À trancher d'un mot, version++.
- **G-2 — PRDPlan §4.4 (formulation « couverture agentique d'E-23 ») enrichie après le gel des ch. 9-11** sans cascade : trois chapitres attestent une reprise « verbatim » devenue inexacte (M-07, m-17, m-20). Arbitrer : soit dater le gabarit et admettre les rendus antérieurs, soit cascader.
- **G-3 — TOC.md porte trois dettes vivantes** : §15.4 « richesse des données » (M-11, amendement déclaré dû par le chapitre publié) ; §16.2 « Scénarios d'articulation » (m-23) ; thèse ch. 7 « support MCP généralisé » (m-12) — plus le bandeau « le RTR naîtra » (obs. 18). La bijection J-2 est le critère de sortie de ce fichier.
- **G-4 — PRD F-33** porte un rendu français entre guillemets sans l'original anglais — racine de m-11 ; et le glossaire (annexe D §D.1) impose une expansion d'« ACP » que ni le PRD ni le TOC ne portent (m-44) : élever l'expansion au socle (elle figure vraisemblablement dans les blogs research.ibm.com cités par F-43) ou la retirer de la forme imposée.

S'y ajoute la paire d'attestations en conflit : `verification/relecture-CA.md` (« 8/8 », « 29/29 ») contre `monographie/99-registre-gel.md` (« cinq pièces sans relecture ») — M-15. L'état vrai constaté est entre les deux ; les deux doivent être réalignés sur lui, pas l'un sur l'autre.

---

## 6. Ce qui tient — contrôles passés sans écart

Pour que cet audit ne soit pas lu comme un procès : l'essentiel du dispositif tient, et il a été **contrôlé**, pas présumé.

- **CA-2 (zéro réfuté)** : balayage des motifs §4.3 sur les 29 pièces — aucune violation de fond de R-1 à R-8. Une seule entorse de **forme** (m-04, sigle nu désambiguïsé à la phrase suivante). Les 121 occurrences de « ACP » ont été inspectées une à une.
- **CA-3 (attribution)** : tenue à chaque occurrence contrôlée — TD, Scotia, RBC (fourchette complète 700 M$–1 G$ partout), Manuvie, CIBC (jamais surqualifiée d'agentique), Intact (aucune terminologie agentique), BMO (~8 000 = employés, sources séparées), consortium, LangGraph, CrewAI, AP2/AGNTCY/A2A (« soutien ≠ production »), projection 70 % (toujours projection), Forrester TEI (commanditaire nommé à chaque citation). Exceptions : m-01, m-03.
- **CA-4 (datation)** : 29/29 dates de gel en en-tête, 29/29 concordantes avec le registre (contrôle exhaustif) ; revalidation P4.1 du jour même, vérifiée à sa source pour MCP et l'AMF.
- **CA-8 (blueprint)** : ch. 23 — 7 liens / 7 statuts ; annexe B — 15 lignes / 15 statuts, aucune cellule sans statut ; neutralité §8.4 (faits négatifs exposés au corps du ch. 22, alternatives par renvoi, aucun superlatif non attribué).
- **CA-6 (lacunes)** : les **onze** lacunes de §10 toutes exposées (recomposées 5+4+1+1 au ch. 21), aucune comblée par du non-vérifié ; Budget 2025 hors frise, en encadré, exactement comme §10.11 l'exige.
- **Mécanique** : tous les identifiants F-xx cités existent (F-12/13/14 uniquement en énoncé de leur non-attribution) ; notes de bas de page — zéro orpheline, zéro doublon sur les 29 pièces (les alertes du balayage brut étaient des mentions de labels « libérés » en blocs de contrôle, vérifiées une à une) ; l'arithmétique d'intervalles et de décomptes internes, recomptée par les sept relecteurs, est exacte à de rares exceptions près (m-30, m-31, m-40) ; les 37 événements de la frise (annexe C) concordent tous avec leur entrée de socle ; les 45 liens du README résolvent ; l'étiquette `mono-v1.0` existe ; la volumétrie de référence (90 362) est **reproduite exactement** par la commande publiée.
- **Le chapitre pivot (ch. 13) est conforme** : neuf dérivations, toutes « Inférence d'auteur », stratification F-09 exemplaire, aucune contrainte AMF dérivée, formulation F-46 imposée reproduite mot pour mot.

---

## 7. Recommandations, par ordre

1. **Trancher les racines de gouvernance (§5)** — PRDPlan §4.4 (un mot), TOC (trois amendements), PRD F-33/glossaire (expansion ACP) — avant toute retouche de chapitre, version++ à chaque document touché.
2. **Corriger les 15 majeurs** en commençant par les plus visibles au lecteur : M-13 et M-06 (marquage F-09 — la faute que le PRD documente nommément), M-08/M-09 (gloses hors socle), M-01 (universels de l'avant-propos), M-02/M-03/M-04 (cascade « dès l'origine »/« mémoire persistante »), M-05, M-10, M-12. Chaque pièce reprise repasse la boucle §4.2 avec relecteur distinct, est regelée et enregistrée (PRDPlan §7).
3. **Réaligner les attestations sur l'état vrai** : M-15 (registre ↔ CA-7 ↔ en-têtes de statut), M-14 (README 90 362), m-40 (annexe A 2046), et purger les blocs « À FAIRE »/« reste dû » périmés (m-02, m-06, m-07, m-08, m-10, m-41). Le projet a déjà nommé cette maladie ; ceci en est la liste de traitement.
4. **Normaliser les encadrés de lacune** sur les trois gabarits §4.4 (m-09, m-15, m-19 ; obs. 5, 13, 15) et statuer sur les gloses anglaises (élever le socle — version EN de P-39.1 sur LégisQuébec, avis 11-348 sur osc.ca — ou retirer les gloses : m-22, M-08, M-09).
5. À la prochaine reprise planifiée (28 juillet 2026, révision MCP — ch. 1, 2, 7), embarquer les corrections des pièces concernées (M-02, m-03, m-04, m-05, m-06, m-07, m-11, m-12) pour n'ouvrir la boucle qualité qu'une fois par pièce.

---

## 8. Méthode et limites de cet audit

**Exécution.** Sept relecteurs adversariaux indépendants (avant-propos + Partie I ; Partie II ; Partie III ; Parties IV-V ; Partie VI ; Partie VII + annexe B ; annexes A/C/D + README + registre + transversal), chacun ayant lu le PRD en entier et les pièces cibles intégralement, avec balayages mécaniques (motifs §4.3, notes, F-xx). En parallèle : contrôles mécaniques centraux (ensemble des F-xx cités vs socle ; intégrité des notes ; dates de gel ; commande de volumétrie ; motifs interdits ; liens ; étiquette git). **Chacun des 15 constats majeurs a ensuite été contre-vérifié par l'auditeur principal — passage relu dans le fichier, référence relue dans le PRD —, sauf M-07** (retenu sur la preuve textuelle du relecteur ; sa racine, un gabarit amendé post-gel, est à arbitrer). Deux faux positifs du balayage brut (notes « orphelines » du ch. 18 et de l'annexe B ; « F-2 ») ont été éliminés par cette contre-vérification.

**Limites.**

- Audit de **conformité interne** (pièces ↔ PRD/PRDPlan/TOC) : les entrées du socle elles-mêmes n'ont **pas** été re-vérifiées contre leurs sources primaires externes — c'est le rôle des passes de revalidation §8.3, dont la dernière date du 17 juillet 2026.
- Les balayages négatifs (« zéro occurrence ») valent pour les motifs balayés ; un balayage ne prouve pas l'absence de formulations fautives non anticipées.
- Les vérifications CA-5 (bilinguisme) et une partie des vérifications d'exactitude interne reposent sur échantillonnage, non sur exhaustivité.
- La question de fait « les relectures P4 ont-elles réellement eu lieu ? » (M-15) est tranchée ici sur les traces internes des fichiers (constats énumérés et appliqués) — c'est le seul témoin disponible dans le dépôt.
- Hypothèse de mission (tâche autonome) : l'audit a été mené en lecture seule, par relecteurs parallèles avec contre-vérification, sans le moteur de workflow multi-agents (mot-clé non fourni) — l'option la plus réversible.

---

## 9. Exécution (17 juillet 2026)

L'audit ci-dessus a été **exécuté en totalité** le jour de sa rédaction, à la demande de l'auteur. Non pas lu et classé : appliqué, dans l'ordre que son §7 prescrivait — les racines de gouvernance d'abord, puis les pièces, puis les attestations, puis une relecture adversariale par des relecteurs distincts. Ce qui suit est le compte rendu fidèle de cette exécution, y compris de ce qu'elle a coûté et de ce qu'elle a trouvé au-delà de l'audit.

### 9.1 Ce qui a été fait

**Phase A — les quatre racines de gouvernance (§5), tranchées avant toute pièce.** Deux se sont résolues non par retouche des chapitres mais par **élévation du socle**, les sources primaires étant déjà citées par les entrées concernées : F-43 porte désormais l'intitulé « *Agent Communication Protocol* » [B] (blog IBM Research du 28 mai 2025) ; F-33 porte le verbatim anglais « all over a reliable, replayable Kafka backbone » [B] (billet Confluent du 26 février 2026). G-1 (« établi » vs « vérifié ») est tranché par une ligne nouvelle de PRDPlan §4.4 — « Trois degrés d'absence » : **vérifié** (balayage de texte : F-35, F-09, F-46) > **établi** (réserve du socle : F-44, F-45) > **absence de documentation** (socle muet). G-2 (forme enrichie après gel) par un avertissement en tête de §4.4. G-3 (trois dettes du TOC) par leur exécution. Documents relevés : **PRD v1.10, PRDPlan v1.4, TOC v1.5**.

**Phase B — les pièces.** Les 24 chapitres, l'avant-propos et les annexes A/B/D corrigés par huit rédacteurs sur fichiers disjoints, chacun tenu de contre-vérifier chaque constat à la source et de refuser d'appliquer un constat qu'il jugerait infondé. Les 15 majeurs et les 44 mineurs traités ; aucune date de gel modifiée (aucune information nouvelle n'entre — ce sont des corrections de conformité, et regeler aurait fait mentir tous les décomptes « douze jours avant la révision MCP »).

**Phase C — les attestations.** Registre de gel réaligné sur l'état vrai (M-15) ; grille CA dotée d'un addendum qui reconnaît ce que l'audit a démenti ; volumétrie re-mesurée sur les 29 pièces et propagée aux cinq documents qui l'annoncent.

**Phase D — la relecture adversariale (PRDPlan §7), par trois relecteurs distincts des rédacteurs.** Verdict : **prose entièrement publiable, aucun bloquant de contenu.** Un seul bloquant, dans un document de gouvernance, trouvé et corrigé (§9.3).

### 9.2 Ce que l'audit avait manqué — et que l'exécution a trouvé

L'audit avait déclaré sa propre limite : « un balayage ne prouve pas l'absence de formulations fautives non anticipées ». L'exécution l'a vérifiée à ses dépens. **Cinq classes de fautes réelles lui avaient échappé :**

1. **La cascade des gloses était triple, non simple.** Le glossaire avait retiré trois gloses le 17 juillet (empoisonnement d'outils, injection d'invites, empoisonnement de mémoire) ; M-04 n'en couvrait qu'une. Le chapitre 4 portait encore les deux autres, sous une note les déclarant « définitions imposées » par un glossaire qui ne les portait plus.
2. **Seize des vingt-neuf pièces** portaient un statut « Commit + registre de gel : À FAIRE » sur des pièces fusionnées, enregistrées et étiquetées `mono-v1.0`. L'audit en avait relevé quatre.
3. **Deux notes** (ch. 10, ch. 11) déclaraient « ne mobilise que la strate [A] » dans la phrase même qui énonçait un fait de strate [B] — le défaut M-06, sur des notes que l'audit n'avait pas ouvertes.
4. **La commande de référence de volumétrie ne compte pas le mot « à »** — `[[:alnum:]]` en locale C ignore les accents, soit 1 158 occurrences et ~1,3 % de sous-comptage sur tout l'ouvrage. Aucun décompte publié n'était donc exact, et personne ne l'avait vu. Défaut documenté, **non corrigé** : tous les décomptes publiés en dérivent, et le changer au milieu d'une passe les aurait tous falsifiés d'un coup, pour un gain de 1,3 % sur une métrique déclarée indicative.
5. **La racine de M-14 n'était pas le README** mais PRDPlan §1.4, qui portait « 88 021 » dix lignes au-dessus de son propre « 90 362 ». Le README recopiait le document d'exécution.

### 9.3 Ce que l'exécution elle-même a mal fait — et qu'une relecture distincte a rattrapé

L'exécution n'a pas été exempte de la faute qu'elle corrigeait. Elle l'a même reproduite trois fois, et **aucune de ces récidives n'a été trouvée par son auteur** :

- **Trois blocs de gouvernance** (ch. 10, 11, 12) attestaient « NON CORRIGÉ » un point que la passe avait pourtant corrigé dans la prose — la faute cardinale du projet, reproduite dans le journal même de la passe qui la traitait. Trouvés par les relecteurs des groupes 1 et 2.
- **Un décompte bloquant** : en propageant la nouvelle volumétrie, l'auteur a mis à jour le total (92 059) et le bloc-somme des annexes (8 761), mais a laissé deux attestations de détail de l'annexe D à sa valeur d'avant la passe (2 596 pour 2 901 mesuré) — rendant le tableau du TOC contradictoire avec lui-même. Trouvé, et prouvé arithmétiquement, par le relecteur du groupe 3.
- **Un pointeur de version périmé** dans CLAUDE.md, introduit en mettant à jour la ligne voisine. Trouvé par le groupe 3 avant qu'une erreur réseau ne l'interrompe.

C'est le résultat le plus solide de toute l'opération, et il vaut d'être énoncé sans détour. L'audit avait écrit, aux dépens de la grille CA : « un contrôle ne vérifie pas ce qu'il croit avoir contrôlé ». L'exécution en fournit le dernier étage : **une passe de correction ne corrige pas ce qu'elle croit avoir corrigé** — elle introduit ses propres mensonges de statut, et seul un relecteur qui refait le travail sans le croire les voit. À chaque strate — la monographie, l'audit, la passe corrective —, le même défaut a reparu, et à chaque strate il a fallu un œil distinct pour le trouver. Ce n'est pas un échec du dispositif : c'est sa justification.

### 9.4 État à la clôture

| Objet | État |
|---|---|
| Constats de l'audit (0 bloquant, 15 majeurs, 44 mineurs) | Traités ; les observations consignées pour reprise future |
| Racines de gouvernance (G-1 à G-4) | Tranchées — PRD v1.10, PRDPlan v1.4, TOC v1.5 |
| Fautes hors audit (§9.2) | Corrigées, sauf le défaut de la commande de volumétrie — **documenté, non corrigé**, arbitrage laissé au projet |
| Volumétrie | Re-mesurée : **92 059 mots** (90 362 avant la passe ; +1 697, intégralement des réserves) |
| Relecture adversariale (PRDPlan §7) | Faite par trois relecteurs distincts ; prose publiable ; le seul bloquant (§9.3) corrigé |
| Dates de gel | **Inchangées** — aucune information nouvelle n'est entrée |

**Ce que cette exécution ne prétend pas.** Elle ne prétend pas que l'ouvrage soit désormais sans défaut : chaque strate de ce travail a montré qu'un contrôle laisse passer ce qu'il ne balaie pas, et rien ne garantit que la relecture adversariale du 17 juillet ait tout vu. Elle prétend seulement ceci : les défauts trouvés ont été corrigés plutôt qu'absorbés, ceux qu'on a choisi de ne pas corriger sont nommés et datés, et le prochain qui construira sur ces pages hérite d'un état documenté, non d'un « 8/8 » qui l'endormirait.
