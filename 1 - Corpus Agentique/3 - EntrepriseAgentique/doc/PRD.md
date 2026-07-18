# PRD — Monographie « L'entreprise agentique : identité non humaine, délégation vérifiable, maillage d'agents et AgentOps »

| Champ | Valeur |
|---|---|
| Version | **0.1 — premier PRD du volume III** (18 juillet 2026). Établi à partir de [`TOC.md`](TOC.md) v0.4, et **contre** les Vol. I et II lus sur pièces : sept extractions parallèles ont vérifié chacun des renvois que le TOC porte vers les deux volumes précédents et vers le dépôt. Neuf écarts constatés, tous consignés en §7.4 — dont trois qui invalident un renvoi du TOC et un qui invalide une affirmation de son en-tête (ligne « Filiation » : la numérotation prêtée au Vol. I, §7.4.1). Aucun n'est corrigé dans le TOC par ce document : le PRD **ne réécrit pas** le fichier qui le précède, il refuse de propager ses erreurs et demande sa révision (§12, jalon J-1). |
| Date | 18 juillet 2026 |
| Statut | **Proposition — socle propre vide.** Le volume n'a constitué **aucune entrée factuelle par ses propres passes**. Il hérite de 33 entrées (§7.2, §7.3) et ouvre 15 lots d'instruction (§7.6). Aucun chapitre n'est rédigeable avant la clôture du lot dont il dépend (§7.0). |
| Livrable encadré | Monographie exhaustive — 28 chapitres en 9 parties, avant-propos, annexes A à E ; **102 500 mots** de cible re-sommée (§6.1 ; le TOC annonce « ≈ 100 000 », enveloppe arrondie) |
| Autorité | Ce PRD prime sur le TOC en cas de conflit de contenu, comme au Vol. II. Le TOC conserve l'autorité sur le **découpage** : toute modification du nombre ou de l'ordre des chapitres passe par lui (version++), et se répercute ici. |
| Méthodologie | **À exécuter, non exécutée.** Le protocole (Annexe A) reconduit celui du Vol. II — extraction d'affirmations falsifiables, vérification adversariale à trois juges, niveaux [A]/[B]/[C] — augmenté du tri prospectif PROGRAMMÉ / PROJETÉ / SPÉCULATIF du Vol. I, et d'un **seuil de vote abaissé et déclaré** (§A.4), le sujet étant choisi pour sa sous-documentation. |
| Corpus | 0 source récupérée par ce volume. 33 entrées héritées, dont 16 du Vol. II (13 à niveau conservé, 3 hors socle factuel) et 17 du Vol. I (**entrant en [C]**, §7.1). Corpus d'appui annoncé : **3 ouvrages, 0 déposé** (§7.7). |

---

## 1. Objet du document

Ce PRD définit les exigences de contenu, de structure, de qualité et de traçabilité du volume III du triptyque — **l'entreprise agentique**. Il fournit :

1. l'**état réel du socle** (§7) : ce dont le volume hérite, à quel niveau de preuve, avec quelle date de péremption ; et le **programme de constitution** de ce qu'il ne possède pas encore ;
2. les **garde-fous rédactionnels** (§8) — quatorze formulations proscrites, règles d'attribution, sensibilité temporelle, traitement défensif exclusif ;
3. la **structure imposée** (§6) et les **critères d'acceptation** (§11) ;
4. la **spécification du blueprint** (Annexe B) et de la **grille des cinq questions** (Annexe C) qui structure transversalement les Parties II, IV, VI, VII et l'annexe B de l'ouvrage.

Le PRD n'est pas la monographie : il en est le cahier des charges et la base documentaire.

**Ce qu'il ne fait pas, et pourquoi il faut le dire d'entrée.** Le PRD du Vol. II a été écrit *après* trois passes de recherche : son §7 énumérait 46 faits vérifiés. Celui-ci est écrit *avant* toute passe. Il ne peut donc pas fournir un socle ; il fournit son inventaire d'héritage et son plan d'acquisition. **Un §7 qui énumérerait des faits que personne n'a vérifiés serait la faute exacte que ce volume prétend documenter au ch. 5** — qualifier un mécanisme par ce qu'il promet plutôt que par ce qu'il démontre. Le socle est vide ; le document le dit à chaque page où c'est vrai.

## 2. Contexte et justification

Le triptyque progresse par élargissement du sujet réel : les protocoles (Vol. I, gel juin 2026), les cadres réglementaires canadiens (Vol. II, gel 16-17 juillet 2026), **l'organisation qui doit les faire tenir ensemble** (Vol. III). Ce troisième objet n'est pas un choix de convenance : les deux volumes précédents le désignent l'un et l'autre comme leur verrou résiduel.

- Le Vol. I clôt sa synthèse opérationnelle par un tableau de verrous par strate. À la strate **Entreprise**, le verrou dominant à juin 2026 est nommé sans ambiguïté : « **Identité non humaine et délégation multi-saut** » (`Synthese Monographie.md` §11.6, tableau 15). Le même volume classe, en §11.5, « la traçabilité de bout en bout des décisions déléguées au-delà de deux sauts » parmi ses problèmes ouverts de gouvernance.
- Le Vol. II ouvre six questions de recherche en clôture (ch. 21 §21.2). Trois portent directement sur l'identité et le droit qui l'encadre : **Q2** (mécanique des risques protocolaires ; existe-t-il des attaques propres à A2A ?), **Q3** (que vaut cryptographiquement une carte d'agent signée ?), **Q5** (quelle organisation sera désignée organisme de normalisation technique du cadre bancaire ?). Son ch. 8 §8.4 conclut, sur l'identité et les registres : « Un architecte qui chercherait aujourd'hui, pour son dossier de conformité, la norme d'identité et de registre des agents ne la trouverait pas : elle n'existe pas. »

Aucun des deux ne comble ce vide, et chacun dit pourquoi : il est hors de son périmètre. Le Vol. III le prend pour objet. La justification éditoriale est donc **interne et vérifiable** — elle ne repose pas sur un constat de marché, mais sur deux lacunes déclarées par les livrables qui précèdent.

**Le risque symétrique doit être posé au même endroit.** Un sujet choisi *parce que* deux ouvrages le déclarent sous-documenté est un sujet dont le socle sera mince par construction. Ce PRD ne le nie pas : il abaisse et déclare son seuil de vote (§A.4), assume une proportion [C] supérieure à celle du Vol. II, et fait de l'exposition des lacunes un critère d'acceptation (CA-06) plutôt qu'une clause de style.

## 3. Objectifs et non-objectifs

### Objectifs

- **O1.** Établir l'**héritage identitaire** — comptes de service, X.509, clés d'API, workload identity — et localiser où l'agent casse ce modèle (Partie I).
- **O2.** Localiser, mécanisme par mécanisme, le **point de rupture des standards étirés** (OAuth/OIDC, SCIM, X.509, VC/DID) confrontés à l'agent : c'est l'apport propre de l'ouvrage (Parties I-II).
- **O3.** Instruire **Q3 du Vol. II ch. 21** : documenter l'ancrage de confiance, le régime de révocation et la gouvernance des clés des cartes d'agent signées — ou établir que la spécification ne les documente pas (ch. 5).
- **O4.** Construire le **passeport d'agent** comme objet de synthèse explicitement marqué construction d'auteur, et en projeter la normalisation sous tri prospectif (ch. 8).
- **O5.** Exposer la **frontière de la délégation multi-saut** (front ouvert du Vol. I, `Synthese Monographie.md` §11.5) plutôt que la combler (ch. 10).
- **O6.** Instruire **Q2 du Vol. II ch. 21** : constituer la taxonomie des attaques sur l'identité et la délégation agentiques, en traitement défensif strict (ch. 12).
- **O7.** Établir l'**horloge post-quantique** comme contrainte de conception, en portant le statut réel de ses jalons — dont le fait que NIST IR 8547 est, au socle du Vol. I, un *Initial Public Draft* (Partie V).
- **O8.** Relire les cadres canadiens (E-23, ligne directrice IA de l'AMF, Loi 25 art. 12.1, ACVM 11-348) **par la grille des cinq questions**, et instruire **Q5 du Vol. II ch. 21** (Partie VI).
- **O9.** Établir le **maillage d'agents** comme lieu d'application de l'identité, par filiation *service mesh*, avec tri strict annonce / GA / production (Partie VII).
- **O10.** Établir l'**AgentOps** comme troisième capacité — observabilité, évaluation continue, cycle de vie, incident — en prolongeant l'*exploitation*, quatrième terme ajouté à l'invariant par le Vol. I (Partie VIII).
- **O11.** Composer les huit parties en une **architecture de référence et une organisation** : trois étages, formalisation ArchiMate, modèle de maturité, répartition des rôles (Partie IX).

### Non-objectifs

- Ne pas produire de tutoriel d'implémentation ni de code.
- Ne pas émettre de conseil juridique. Le ch. 20 cartographie des lectures ; il ne tranche pas.
- Ne pas recommander de fournisseur. Entra Agent ID et ses pairs sont des **cas documentés**, jamais des recommandations (§8.4).
- **Ne pas fournir de recette d'exploitation.** La Partie IV traite la mécanique des attaques au niveau architectural, cite les identifiants de vulnérabilité et n'en reproduit aucun (§8.5, R-12).
- Ne pas normaliser le passeport d'agent. L'ouvrage le construit et le déclare construction d'auteur ; il ne prétend pas fixer ce que les organismes de normalisation n'ont pas fixé.
- Ne pas arbitrer les divergences entre volumes. Elles sont **signalées** (§7.5) ; leur arbitrage relève du Vol. IV, et n'a d'autorité qu'une fois celui-ci rédigé.

## 4. Public cible et registre

| Public | Besoin |
|---|---|
| Architectes d'entreprise, responsables IAM/CIAM d'institutions réglementées | Où les standards d'identité cèdent, et ce qui tient à leur place |
| RSSI, équipes de sécurité offensive et défensive | Taxonomie des attaques d'identité et de délégation ; révocation ; SOC agentique |
| Équipes plateforme, SRE, exploitation (AgentOps/MLOps) | Observabilité, évaluation continue, cycle de vie, réponse à incident d'un parc d'agents |
| Responsables conformité (E-23, ligne directrice IA de l'AMF, Loi 25) | Ce que les cadres présupposent sans le nommer, et ce qu'ils n'exigent pas |
| Dirigeants instruisant une trajectoire de maturité agentique | Paliers, rôles, conduite du changement |
| Chercheurs en identité décentralisée et sécurité multi-agents | Corpus tracé, lacunes exposées, questions formulées pour instruction |

Registre : **français canadien soutenu**, ton professionnel et neutre — pas de marketing, pas de première personne. Terminologie technique anglaise entre parenthèses et en italique à la première occurrence (« maillage d'agents (*agent mesh*) »). Citations verbatim en langue originale.

## 5. Portée

**Inclus** : identité machine héritée (comptes de service, X.509, workload identity, SPIFFE/SPIRE) ; extensions agentiques des standards (OAuth 2.x, OIDC, SCIM, drafts IETF) ; identité décentralisée (W3C VC, DID, DIF) ; cartes d'agent signées ; annuaires et registres d'agents (produits et spécifications) ; chaîne de mandat et délégation multi-saut ; KYA et admission inter-domaines ; attaques d'identité et de délégation, révocation, attestation d'intégrité ; migration post-quantique de la pile identitaire ; cadres canadiens relus par la grille du ch. 4 ; maillage d'agents comme point d'application ; AgentOps comme boucle d'exploitation ; blueprint et modèle de maturité.

**Exclus** : robotique ; IA agentique grand public ; comparatifs de modèles de fondation ; régimes UE/É.-U. hors contrepoint ; orchestration et interopérabilité protocolaire **pour elles-mêmes** (objets des Vol. I et II, mobilisés ici par renvoi).

### 5.1 Test d'appartenance — la parade au risque de dilution

Le TOC identifie comme risque n° 6 la dilution : trois objets (identité, maillage, exploitation) dans un même ouvrage, et il charge explicitement le PRD de couper. Voici le test, et il est opposable :

> **Test d'appartenance.** Un développement de Partie VII ou VIII n'entre dans l'ouvrage que s'il répond à l'une de ces deux questions : *que vérifie-t-il de l'identité ou du mandat d'un agent ?* ou *que produit-il comme preuve opposable sur cette identité ou ce mandat ?* Un développement qui ne répond ni à l'une ni à l'autre est **hors périmètre**, quelle que soit sa qualité.

Conséquences concrètes, énoncées pour n'avoir pas à les rediscuter chapitre par chapitre :

- la latence, le coût et la topologie d'un maillage entrent **uniquement** au titre des conditions qui renverseraient la recommandation (ch. 23 §23.4) — pas comme sujet d'ingénierie ;
- l'observabilité entre par la **corrélation trace ↔ chaîne de mandat** (ch. 24 §24.4), pas par le panorama des plateformes ;
- l'évaluation entre par la **revalidation du passeport après apprentissage** (ch. 25 §25.5), pas par la science de l'évaluation en général — laquelle reste un front ouvert du Vol. I ;
- le FinOps agentique, le routage sémantique pour lui-même et le comparatif de cadriciels d'agents sont **hors périmètre**.

Le test est vérifié à la relecture (CA-09).

## 6. Structure imposée de la monographie

Neuf parties, 28 chapitres, plus l'avant-propos et les cinq annexes — **34 pièces** (§6.1). Pour chaque partie et chaque pièce d'appareil : le contenu obligatoire, le socle mobilisable à ce jour, et le **lot d'instruction** (§7.6) dont la clôture conditionne la rédaction.

### 6.1 Volumétrie et découpage

| Bloc | Chapitres | Cible (mots) |
|---|---|---|
| Avant-propos et note méthodologique | — | 2 500 |
| Partie I — L'héritage | 1–4 | 11 000 |
| Partie II — Émettre l'identité | 5–8 | 12 000 |
| Partie III — La délégation | 9–11 | 9 500 |
| Partie IV — La confiance hostile | 12–15 | 12 000 |
| Partie V — L'horloge post-quantique | 16–18 | 9 000 |
| Partie VI — Le droit | 19–21 | 9 500 |
| Partie VII — Le maillage d'agents | 22–23 | 7 000 |
| Partie VIII — AgentOps | 24–26 | 10 000 |
| Partie IX — Blueprint | 27–28 | 11 000 |
| Annexes A–E | — | 9 000 |
| **Total** | **28 chapitres (34 pièces)** | **102 500** |

⚠ **Décompte re-sommé le 18 juillet 2026.** Le TOC annonce « ≈ 100 000 mots » ; la somme de ses propres cibles par bloc donne **102 500**. L'écart (+2,5 %) est un arrondi d'enveloppe, non une erreur — il est reporté ici pour que le chiffre qui fait foi soit celui qu'on peut recalculer. **34 pièces** = 28 chapitres + avant-propos + 5 annexes. La volumétrie est **indicative et non normative** : leçon du Vol. II, dont le total a dépassé de 12 % un plafond « ajustable » parce que les relectures adversariales ajoutent des réserves, jamais des thèses — *un écart se documente, il ne se corrige pas par amputation*.

### 6.2 Contenu obligatoire par partie et par pièce d'appareil

**Partie I — L'héritage : l'identité machine avant l'entreprise agentique (ch. 1-4).**
Généalogie des identités non humaines (comptes de service → workload identity) ; écart de gouvernance NHI ; pourquoi l'identité stable ne suffit pas face au comportement non déterministe ; OAuth 2.x et l'agent (*client* ou *resource owner* ?) ; drafts IETF pertinents **avec leur état et leur date d'expiration réels** ; SCIM et le provisionnement d'agents ; ce que les RFC ne disent pas ; corpus W3C (VC Data Model, DID Core) et fossé adoption ; **la grille des cinq questions** (Annexe C), **construction d'auteur** dont deux des quatre axes du Vol. I (*identité et confiance*, *gouvernance des frontières* — `Synthese Monographie.md` §11.2) fournissent l'inspiration et non la dérivation, appliquée-témoin à trois mécanismes, et croisée avec le spectre de maturité.
*Socle : H-03, H-18, H-19, H-20. Lots : L-01, L-02. **Le §4.4 (croisement grille × maturité) est bloqué par L-15** — il mobilise le corpus d'appui, non déposé.*

**Partie II — Les mécanismes émergents : émettre l'identité (ch. 5-8).**
Anatomie et valeur probante de la carte d'agent signée — format, chaîne de signature, ancrage, révocation, durée de vie, verdict par la grille ; Entra Agent ID (périmètre GA réel, licences, extensions des RFC) et ses pairs infonuagiques, avec verdict par la grille ; registres gouvernés (spécification CSA, registres A2A/AGNTCY, le registre comme objet réglementaire) ; **le passeport d'agent** — assemblage des quatre pièces, émetteur et vérificateur, trois scénarios de normalisation triés PROGRAMMÉ/PROJETÉ/SPÉCULATIF, verdict par la grille.
*Socle : H-01, H-02, H-03, H-10, H-18. Lots : L-03 (bloquant ch. 5), L-04, L-05.*

**Partie III — La délégation : le mandat dans l'entreprise (ch. 9-11).**
Le mandat dans les protocoles (mandats AP2, *on-behalf-of* OAuth, jetons de transaction) ; la chaîne de délégation comme objet de première classe ; ce que le droit civil du mandat éclaire et où l'analogie casse ; **l'humain comme acte de délégation daté et signé** — une approbation qui ne s'inscrit pas dans la chaîne de mandat n'est pas un contrôle ; le problème des deux sauts et sa question de recherche ; KYA, admission d'agent tiers, fédérations de confiance (eIDAS, FIDO).
*Socle : H-01, H-06, H-19, H-28. Lots : L-06 (porte l'arbitrage de la divergence AP2, §7.5), L-07. **Le §9.4 (typologie des patrons d'interaction humain-agent) est bloqué par L-15** — il mobilise le corpus d'appui, non déposé.*

**Partie IV — La confiance hostile : l'identité comme fondation de la défense (ch. 12-15).**
Recension des attaques — identifiants de vulnérabilité, incidents publics datés, littérature académique ; taxonomie par la grille ; empoisonnement de la mémoire et des sources comme problème d'identité **des sources** ; ce que la recension ne trouve pas ; *rug-pull* et vérification continue ; attestation d'intégrité à l'exécution ; inventaire de la révocation par mécanisme, précédent PKI, révocation en cascade ; SOC agentique et référentiels en mouvement.
*Socle : H-11, H-21, H-22, H-25, H-26. Lots : L-08 (bloquant ch. 12), L-09, L-10. **Traitement défensif exclusif — R-12.***

**Partie V — L'horloge post-quantique (ch. 16-18).**
Échéances et leurs sources, **avec le statut réel du document qui les porte** ; *harvest now, decrypt later* appliqué aux artefacts d'identité longue durée ; inventaire des artefacts qui cassent ; crypto-agilité comme application de l'invariant du Vol. I à la couche cryptographique ; audit de crypto-agilité des mécanismes de la Partie II ; dette de migration — ce que les sources portent, la méthode d'estimation plutôt qu'un chiffre.
*Socle : H-17, H-27. Lot : L-11. **Garde-fou R-11 : un jalon NIST n'est pas une obligation légale, et IR 8547 est un projet.***

**Partie VI — Le droit de l'entreprise agentique (ch. 19-21).**
E-23 et la ligne directrice IA de l'AMF relues par la grille ; le registre du ch. 7 comme pièce de conformité ; ce que les cadres **n'exigent pas** ; art. 12.1 et décision automatisée multi-agents — cartographie des lectures sans verdict ; mandat agentique en droit civil québécois ; désignation de l'organisme de normalisation technique (Q5) et ses conséquences architecturales ; normalisation internationale.
*Socle : H-04, H-05, H-06, H-07, H-08. Lot : L-12. **Formulations imposées d'E-23 : « attendu », jamais « exigé » ; « documentation de modèle », jamais « fiche de modèle » (R-06).***

**Partie VII — Le maillage d'agents : où l'entreprise applique la confiance (ch. 22-23).**
Généalogie *service mesh* (sidecar, passerelle, plan de contrôle / plan de données, mTLS, SPIFFE/SPIRE) ; anatomie du maillage agentique (passerelles MCP, courtage A2A, transport AGNTCY, routage sémantique) **à l'état daté des réalisations** ; l'arête comme conséquence architecturale de la non-compositionnalité de la sûreté ; grille appliquée au maillage ; PEP/PDP agentiques ; *zero trust* transposé du réseau au graphe ; ce que le maillage trace du problème des deux sauts et ce qu'il ne résout pas ; coûts et conditions de renversement.
*Socle : H-09, H-10, H-12, H-15, H-24, H-30. Lot : L-13. **Homonymies : R-04.***

**Partie VIII — AgentOps : exploiter la confiance dans la durée (ch. 24-26).**
De l'APM à l'AgentOps ; état daté des conventions sémantiques OpenTelemetry pour l'IA générative et les agents, **avec leur statut stable/expérimental** ; journalisation probatoire ; corrélation trace ↔ passeport ; évaluation en production ; dérive de modèle, d'outil, d'autonomie ; réponse à incident agentique ; GitOps du parc ; l'agent qui apprend et la revalidation du passeport après apprentissage ; recension critique des métriques publiées ; grille minimale d'indicateurs **marquée construction d'auteur** ; métrique d'horizon de tâche déléguée.
*Socle : H-11, H-12, H-14, H-16, H-23, H-27, H-28. Lots : L-14, L-15 (bloque §25.1 et §25.5).*

**Partie IX — Blueprint : l'entreprise agentique de confiance (ch. 27-28).**
Architecture de référence à trois étages et leurs contrats mutuels ; formalisation ArchiMate ; points d'intégration avec l'IAM et l'observabilité en place ; **modèle de maturité** confrontant les trois modèles du corpus d'appui, l'autonomie graduée du Vol. I et la grille du ch. 4 ; organisation de la fabrique (rôles, facteur humain, conduite du changement) ; cycle de vie complet d'un agent — naissance, vie, mort ; confrontation externe au cas fil rouge du corpus d'appui ; lacunes résiduelles ; événements de péremption et protocole de revalidation.
*Socle : H-15 (par l'Annexe B §B.1 ; prolongement principal en Partie VII), H-29, H-31, H-32 ; spécification en Annexe B. Lot : L-15 — **§27.4, §27.5 et §28.4 sont intégralement bloqués tant que le corpus d'appui n'est pas déposé.***

**Avant-propos et note méthodologique (pièce d'appareil).**
Définition d'auteur de l'« entreprise agentique » — **siège unique imposé par R-03** ; origine déclarée de l'ouvrage (le verrou « identité non humaine et délégation multi-saut ») ; méthode et **double héritage épistémique** — niveaux [A]/[B]/[C] et tri PROGRAMMÉ/PROJETÉ/SPÉCULATIF, qui ne se substituent pas l'un à l'autre (§7.1) ; règle d'attribution des métriques auto-déclarées, reconduite au mot du Vol. II ; avertissements — pas de conseil juridique, neutralité fournisseur, volumétrie indicative, lacunes de §10 annoncées d'entrée ; **convention cardinale** — un mécanisme cryptographique est qualifié par ce que sa spécification démontre (R-02).
*Socle : H-29, H-33. Lot : aucun — rédigeable dès l'ouverture de J-4, livré en J-5. **Garde-fous : R-02, R-03, §8.2.***

**Annexes A à E de l'ouvrage (pièces d'appareil).**
**A — Méthodologie** : report lisible de l'Annexe A du présent PRD (niveaux de preuve, seuil de vote déclaré, tri prospectif, régimes d'héritage). **B — Matrice des mécanismes** : mécanismes des Parties II-III et composants de maillage de la Partie VII croisés avec la grille du ch. 4, l'état PQC et la couverture d'observabilité — table de référence de l'ouvrage, régie par les règles d'emploi de l'Annexe C §C.2. **C — Chronologie 2024-2030** : chaque date portée par sa source et son statut réel, faits chauds de §8.3 compris. **D — Glossaire** : statut épistémique de chaque terme — norme, marché ou construction d'auteur — et sièges imposés par R-03 et R-04. **E — Catalogue de patrons de la confiance agentique** : gabarit contexte / problème / forces / solution / conséquences, chaque patron renvoyant à son chapitre et à son socle.
*Socle : H-33 (annexe A) ; matrice adossée à l'Annexe B du présent PRD. Lot : L-15 — **l'annexe E est intégralement bloquée tant que le corpus d'appui n'est pas déposé** (§7.7). **Garde-fous : R-03 et R-04 (annexe D), R-11 (annexe C).***

⚠ **Lecture du champ « Socle » de §6.2.** Une entrée H-xx y figure quand la partie la **mobilise**, ce qui n'est pas toujours le chapitre que sa flèche « → » désigne comme siège principal. Quatre cas : **H-19** en Partie I (siège ch. 11) y sert de témoin d'application de la grille ; **H-01** et **H-06** en Partie III (sièges ch. 5 et ch. 20) y fournissent respectivement le mandat protocolaire et l'obligation de révision humaine ; **H-29** en Partie IX (siège avant-propos) y ferme la boucle sur le verrou d'origine. La flèche donne le siège, le champ « Socle » donne l'usage — les deux ne coïncident pas nécessairement, et c'est voulu.

### 6.3 Contrôle de couverture

La bijection §6.2 ↔ TOC est vérifiée en J-1 : chaque élément de contenu obligatoire ci-dessus est assigné à un chapitre ou à une pièce d'appareil du TOC, et aucun chapitre ni aucune annexe du TOC n'introduit de contenu absent d'ici. **Le contrôle porte sur les 34 pièces, non sur les 28 chapitres** — la leçon du Vol. II est que l'appareil (avant-propos, annexes) est le lieu où la bijection se relâche sans qu'on le voie. Les lacunes de §10 et les garde-fous de §8 sont assignés à un chapitre porteur au même jalon. **Un garde-fou non assigné est un garde-fou non appliqué** — leçon du Vol. II, dont l'annexe D avait laissé un garde-fou entier hors de l'instrument censé le contrôler.

## 7. Socle factuel : état, héritage et programme de constitution

### 7.0 Règle cardinale

> **Aucun chapitre n'est rédigé avant la clôture du lot d'instruction dont il dépend (§7.6).** Un chapitre écrit sur un socle vide n'est pas un chapitre en avance : c'est une inférence longue, et le volume qui prend l'identité pour objet ne peut pas se permettre d'en produire.

Trois corollaires, tous hérités du Vol. II et reconduits sans amendement :

1. **Une entrée [C] ne porte jamais un fait central.** Elle signale une piste, pas un acquis.
2. **Une extraction de source primaire n'élève pas une entrée déjà votée 3-0** : elle l'enrichit d'un contenu de rang inférieur. Le niveau ne mesure pas la qualité de la source, il mesure **ce que l'affirmation a subi** — formule reprise de l'annexe A du Vol. II, qui la marque elle-même « Lecture de l'auteur » ; le PRD du Vol. II définit les niveaux par leur seule procédure.
3. **Les identifiants ne sont jamais renumérotés.** Ils sont cités en références croisées, ici et — le TOC du Vol. IV le documente déjà — dans le compendium à venir.

Un quatrième corollaire est propre à ce volume :

4. **Toute inférence d'auteur porte le libellé « Lecture de l'auteur »**, en gras, en tête de l'énoncé, suivi de ce que le socle établit et de ce qu'il n'établit pas. Le ch. 8 (passeport), le ch. 26 (grille d'indicateurs) et le §27.4 (modèle de maturité) sont des constructions d'auteur **en totalité** : ils portent le marquage à l'ouverture, pas seulement au paragraphe.

### 7.1 Deux régimes d'héritage — et pourquoi ils diffèrent

Le Vol. III hérite de deux volumes dont les **systèmes épistémiques ne sont pas les mêmes**, et les confondre serait une faute de méthode dès la première page.

| | Vol. II | Vol. I |
|---|---|---|
| Instrument | niveaux de preuve **[A] > [B] > [C]** — ce que l'affirmation a subi | tri prospectif **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** — ce que l'énoncé prétend sur le futur |
| Vérification | vote adversarial à trois juges (réfutation acquise à 2/3 ; [A] exige 3-0) sur les affirmations ; extraction primaire citée sinon | **vérification adverse des citations** : existence, auteurs, année, numéro de norme — elle porte sur la *référence*, non sur le *contenu de l'affirmation* |
| Gel | 16-17 juillet 2026 | juin 2026 |

Les deux instruments sont **orthogonaux** : un fait peut être [B] et PROJETÉ. L'ouvrage emploie les deux, jamais l'un pour l'autre.

**Règle d'entrée, en conséquence :**

- **Une entrée héritée du Vol. II conserve son niveau** ([A], [B], [C] ou mixte), avec sa provenance F-xx explicite. La méthode est identique ; il n'y a rien à re-subir. **Exception, trois entrées sur seize** : H-13 (garde-fou R-8), H-15 (construction d'auteur du ch. 19) et H-16 (ch. 20) ne proviennent pas du socle factuel du Vol. II — elles n'ont ni niveau ni F-xx, et entrent comme garde-fou ou comme thèses attribuées, jamais comme faits.
- **Une entrée héritée du Vol. I entre en [C]** — repérage. Non parce que le Vol. I serait moins fiable, mais parce que sa vérification porte sur les références et non sur les affirmations : le contenu n'a subi ni vote ni extraction citée au sens du Vol. II. **Chacune de ces entrées nomme la source primaire que le Vol. I cite** ; l'élévation en [B] est donc à une lecture de distance, et c'est précisément ce que les lots d'instruction organisent.

**Règle de péremption de l'héritage.** Un volume date de son gel, pas de sa lecture — même règle que pour un livre publié (risque n° 8 du TOC). Toute entrée héritée portant un fait figurant à la liste des faits chauds (§8.3) est **revalidée à la source primaire** avant d'entrer dans un chapitre, quel que soit son niveau d'origine. Le Vol. II a lui-même gelé le 16 juillet 2026 en sachant qu'une révision majeure de la spécification MCP tombait le 28.

### 7.2 Socle hérité du Vol. II — 16 entrées : 13 à niveau conservé, 3 hors socle factuel

Provenance : `1 - Corpus Agentique/2 - OrchestrationAgentique/doc/PRD.md` (v1.10) et les pièces de `monographie/`.

- **H-01 ← F-02 [A ; ligne v1.0.1 [B]] — A2A v1.0 et les cartes d'agent signées.** Lancé par Google en avril 2025, transféré à la Linux Foundation en juin 2025 ; v1.0 = première spécification stable : multi-protocole, multi-location d'entreprise, *Signed Agent Cards* (vérification cryptographique d'identité). Dernier correctif v1.0.1 le 28 mai 2026. **Réserve capitale, et c'est elle qui fonde le ch. 5** : le socle du Vol. II **ne documente ni l'ancrage de confiance, ni la révocation, ni la gouvernance des clés** des cartes signées, ni le mécanisme de la multi-location, ni son terme anglais d'origine, ni la date de publication de la v1.0 elle-même (lacune Vol. II §10.9). → *ch. 5 (Q3), ch. 22.*
- **H-02 ← F-07 [A] — Microsoft Entra Agent ID.** Disponibilité générale vers avril-mai 2026 pour tous les clients Entra ; identités d'agents et *blueprints* ; fondé sur OAuth 2.0 et OpenID Connect ; scénarios *app-only* et délégués. **Réserves** : des sous-fonctionnalités restent en préversion ; les fonctions de sécurité étendues relèvent de licences additionnelles (Entra ID P1/P2, M365 E5, Agent 365) ; **les flux *on-behalf-of* et de jeton d'agent étendent les RFC — ne jamais présenter le dispositif comme du « pur RFC »**. Le terme *blueprints* n'est pas défini par le socle. → *ch. 6.*
- **H-03 ← F-08 [A, statut BROUILLON] — Spécification CSA « Agent Registry ».** Publiée le 27 mars 2026 par CSA Labs : inventaire, découverte, cycle de vie, conformité ; profil d'agent ancré sur SCIM 2.0 (RFC 7643) et `draft-abbey-scim-agent-extension-00` (Okta) ; champs obligatoires `toolAccessList` et `permissionBoundaries`. **Réserves** : brouillon de labs, non une norme ratifiée ; **le brouillon IETF a expiré le 19 avril 2026** — soit vingt-trois jours après la publication de la spécification qui s'y adosse ; consolidation rattachée à l'IETF 125. → *ch. 2, ch. 7.*
- **H-04 ← F-09 [A/B mixte] — BSIF, ligne directrice E-23.** Publiée le 11 septembre 2025, **en vigueur le 1er mai 2027**, aucune disposition transitoire. **Fondée sur des principes**, rédigée au conditionnel. Définition de « modèle » laissée « intentionally broad », incluant les méthodes d'IA et d'AA. Cycle de vie à cinq volets ; inventaire d'entreprise (§C.1, Appendice 1) ; cotation graduée ; documentation ; surveillance continue visant expressément « autonomous decision making, autonomous re-parametrization » (prise de décision autonome, reparamétrisation autonome — traduction hors guillemets : le socle ne verse aucun rendu français de ces syntagmes). **Vérification négative mécanique, EN et FR** : « agentique » = 0, « agent(s) » = 0, « orchestration » = 0, « autonom\* » = 8. **« fiche de modèle » / « model card » = 0 occurrence.** → *ch. 19.*
- **H-05 ← F-25 [A] — AMF, ligne directrice sur l'IA.** Finale publiée le **30 mars 2026**, en vigueur le 1er mai 2027 — même date qu'E-23. **Deux réserves** : ne jamais écrire « en attente » ni « en projet » ; **la date du 30 mars est en divergence non arbitrée avec la veille technologique du dépôt, qui porte le 7 avril 2026** (§7.5). Le contenu article par article n'est **pas** au socle du Vol. II (sa lacune §10.4) — l'ouvrage hérite d'une date, pas d'un texte. → *ch. 19.*
- **H-06 ← F-27 [B] — Loi 25 (Québec), art. 12.1.** En vigueur depuis le 22 septembre 2023. Trois obligations pour toute « décision fondée exclusivement sur un traitement automatisé » : informer au plus tard au moment de la décision ; sur demande, communiquer les renseignements, « les raisons, ainsi que les principaux facteurs et paramètres » ; donner l'occasion de présenter ses observations « à un membre du personnel de l'entreprise en mesure de réviser la décision ». **Réserve [C]** : selon l'analyse Fasken, une intervention humaine significative *avant* la décision écarterait l'application — nuance de cabinet, non confrontée aux positions de la CAI. → *ch. 20.*
- **H-07 ← F-26 [B] — ACVM, avis 11-348.** Publié le 5 décembre 2024 ; les lois existantes s'appliquent aux systèmes d'IA (« la guidance ne crée ni ne modifie aucune exigence ») ; définition de « système d'IA » incluant des **niveaux variables d'autonomie et d'adaptativité après déploiement**. → *ch. 20, ch. 21.*
- **H-08 ← F-35 [A — fait négatif vérifié 9-0] — Aucun standard technique désigné.** La loi impose un standard technique unique fixé par un organisme désigné par arrêté ministériel ; recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI », « OAuth » dans le règlement prépublié, le communiqué et la page Budget 2025 : **zéro occurrence**. FDX relève du commentaire d'industrie. → *ch. 21 (Q5).*
- **H-09 ← F-01 [A] — MCP.** Interface client-serveur JSON-RPC 2.0 ; **cadre d'autorisation** fondé sur OAuth — écrire « cadre d'autorisation », jamais « sécurisé ». Gouvernance transférée en décembre 2025 à l'Agentic AI Foundation. **Fait chaud** : révision majeure attendue le **28 juillet 2026** (protocole sans état, retrait de `Mcp-Session-Id`) — dix jours après la date du présent PRD. → *ch. 2, ch. 22.*
- **H-10 ← F-05 [A] — AGNTCY.** Ouvert par Cisco en mars 2025, sous Linux Foundation depuis le 29 juillet 2025 ; couche d'infrastructure (annuaires de découverte, transport SLIM). **Lacune héritée (Vol. II §10.7)** : le socle n'établit ni l'intitulé complet de sa composante « ACP » ni son identité — ou sa non-identité — avec le protocole ACP d'IBM Research. Quatrième branche du garde-fou d'homonymie. → *ch. 7, ch. 22.*
- **H-11 ← F-36 [B] — Manifeste de recherche APM.** Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al., *Information Systems* 140, 102738 (2026) / arXiv:2603.18916. Apports mobilisés ici : *frames* normatifs et opérationnels ; **auto-modification scindée en adaptation éphémère et évolution persistante** ; **opérationnalisation locale des frames comme frontière de sécurité et de confidentialité** — restreindre le contexte et les capacités limite l'impact d'un agent compromis ; **paradoxe de confidentialité de l'explicabilité** ; empoisonnement de mémoire et patrons *Action-Selector* / *Plan-Then-Execute* (défi C2) ; **écart de responsabilité** entre développeur, organisation qui impose le frame, fournisseur de modèle et comportement émergent (défi C4). **Réserve héritée (Vol. II §10.10)** : le *frame* **opérationnel** n'est pas caractérisé par le socle — seul le normatif l'est. Le PDF est déposé au dépôt du Vol. II : l'élévation est à une relecture de distance. → *ch. 12, ch. 25.*
- **H-12 ← F-37 [B] — Cadre OO1–OO4 et preuves empiriques de l'encadrement.** Rinderle-Ma, Mangler et al., arXiv:2606.31518v1, **préprint non révisé par les pairs**. Mobilisé ici pour trois choses seulement : (a) l'enseignement que **la journalisation confiée aux agents « n'est généralement pas recommandée »** — fondement de PC2 et du ch. 24 ; (b) les métriques par propriété — **quatre propriétés instrumentées sur cinq ; l'autonomie n'en a aucune** ; (c) le verdict d'inacceptabilité de l'orchestration non encadrée **quand des exigences strictes d'exécution et de documentation s'appliquent** — verdict tiré d'un scénario unique, le don de sang sous directive 2002/98/CE. **Réserve** : source unique, préprint v1, sans reproduction indépendante — c'est Q1 du Vol. II ch. 21, que ce volume **n'instruit pas**. → *ch. 23, ch. 26.*
- **H-13 ← R-8 du Vol. II [garde-fou] — Les quatre emplois de « (agentic) control plane » / « ACP ».** (a) ACP protocolaire (IBM Research/BeeAI, fusionné dans A2A) ; (b) *Agentic Control Plane*, programme du consortium Lightworks–Scotiabank–Sun Life–TELUS (F-48) ; (c) *agentic control plane*, positionnement de watsonx Orchestrate (F-42) ; (d) composante ACP d'AGNTCY (H-10), **non caractérisée**. Le sigle « ACP » employé seul est proscrit. **Ce volume ajoute une cinquième branche** — le plan de contrôle au sens infrastructure (Partie VII) — et une sixième (§7.4.6). → *garde-fou R-04.*
- **H-14 ← F-44 [B] — Observabilité agentique outillée.** Instana AI Agent & LLM Observability (préversion publique, Think 2026) : découverte automatique des agents, modèles et dépendances, évaluations *LLM-as-a-judge*, visibilité par tâche ; watsonx.governance (Evaluation Studio, Risk Atlas agentique, inventaire par défaut). **Réserve capitale, reconduite — et bornée à ce que le socle porte** : la réserve du Vol. II vise **watsonx.governance**, dont aucune source ne documente le lien avec E-23 ; tout parallèle est une inférence d'auteur (R-07). Pour **Instana**, le socle est **muet** sur E-23 : absence de documentation, non fait négatif (§8.6, degré 3). → *ch. 24, ch. 26.*
- **H-15 ← Vol. II ch. 19 §19.3 [construction d'auteur du Vol. II] — Les cinq points de contrôle obligatoires.** PC1 l'événement de décision ; PC2 la trace d'instance, **produite par le cadre** ; PC3 le point d'arrêt humain ; PC4 la séparation de l'adaptation et de l'évolution ; PC5 le confinement local. ⚠ **Ce ne sont pas des faits de socle** : les cinq portent le marquage « Lecture de l'auteur » dans le Vol. II. Ils entrent ici comme **thèses d'un volume antérieur, à prolonger et à attribuer**, jamais comme acquis. ⚠ **Collision terminologique héritée, à ne pas résoudre en silence** : le glossaire du Vol. II réserve « point de contrôle » à la traduction de *checkpointing* ; « point de contrôle obligatoire » y désigne autre chose. Le Vol. II a signalé la collision sans la corriger ; le Vol. III la signale à son tour. → *ch. 23.*
- **H-16 ← Vol. II ch. 20 [transversal] — Instrumentation et jalons.** Feuille de route en trois mouvements — inventorier, coter puis encadrer, surveiller. Cinq jalons externes, dont quatre datés : 28 juillet 2026 (révision MCP), 24 août 2026 (règlement administratif du RTR), 26 août 2026 (clôture des commentaires du cadre bancaire), date inconnue (arrêté de désignation), 1er mai 2027 (entrée en vigueur commune E-23 / AMF). → *ch. 26, annexe C de l'ouvrage.*

### 7.3 Socle hérité du Vol. I — 17 entrées, entrant en [C]

Provenance : `1 - Corpus Agentique/1 - InteroperabiliteAgentique/`. ⚠ **Le volume vit en triple numérotation** (§7.4.1) : chaque entrée nomme son fichier.

- **H-17 [C] — L'horloge post-quantique.** `Monographie.md` §7.4.1 : NIST IR 8547 — dépréciation de RSA-2048 et des courbes P-256 **visée pour 2030**, interdiction **visée pour 2035**. ⚠ **Le Vol. I porte lui-même la réserve : « dates à re-vérifier, le document étant à l'état de *Initial Public Draft* ».** Portefeuille adossé : FIPS 203, FIPS 204. **Jalons distincts, à ne jamais fusionner** : décret 14412 (clés post-quantiques fin 2030, signatures fin 2031 — PROGRAMMÉ) et cibles 2030-2031/2035 du Quantum Safe Financial Forum d'Europol avec FS-ISAC (PROJETÉ). Fenêtre 2029-2032 d'un calculateur quantique cryptographiquement pertinent : SPÉCULATIF. → *ch. 16, 17, 18.*
- **H-18 [C] — Les jalons de normalisation 2027-2028.** `Monographie.md` §7.4.2 : WIMSE (IETF), architecture en RFC attendue 2026-2027 et pile complète 2027-2028 (`draft-ietf-wimse-arch-07`) — **PROGRAMMÉ mais sans date d'engagement ferme** ; W3C VC Data Model 2.1 en Candidate Recommendation à l'horizon 2027, API de cycle de vie en Recommandation en 2028 ; DID v1.1 en CR le 5 mars 2026 ; `did:webvh` v1.0 ; Web Bot Auth ; ANS v2. ⚠ **Le terme « passeport d'agent » figure dans le titre de §7.4.2 et n'est ni défini ni réemployé dans son corps.** Le Vol. I ne fournit donc pas l'objet — il fournit son agenda. → *ch. 3, ch. 8.*
- **H-19 [C] — KYA et la *trust fabric*.** `Monographie.md` §7.4.3 : Agent Identity Registry Protocol CG du W3C (proposé le 22 avril 2026) et livre blanc *Identity Management for Agentic AI* de l'OpenID Foundation — formes « encore concurrentes » ; l'Agent Identity Protocol de délégation vérifiable MCP↔A2A (arXiv:2603.24775) est étiqueté **SPÉCULATIF**. Verrous nommés : révocation quasi-temps réel, identité composite, fraîcheur d'autorité à chaque saut. **Fait saillant** : **aucun forum n'avait tranché à juin 2026** — ni FIDO, ni W3C, ni ISO — ce qui fait du KYA un verrou institutionnel plus que technique. ⚠ Le siège de la réserve « à juin 2026, le KYA n'est **pas un standard établi** ; les initiatives existantes relèvent du positionnement fournisseur […], non d'une norme ratifiée » est `Monographie.md` **§5.5.4**, non `Monographie.md` §7.4.3 (PRD §7.4.4). → *ch. 11.*
- **H-20 [C] — Les Community Groups agentiques du W3C.** `Monographie.md` §7.3.2 : quatre CG, dont trois datés — AI Agent Protocol (8 mai 2025), Agent Identity Registry Protocol (proposé le 22 avril 2026), Semantic Agent Communication (non daté au socle), AI Agent Memory Interoperability (proposé le 18 mai 2026, lancé le 3 juin 2026). **Un Community Group n'est pas un Working Group : il ne produit pas de Recommandation et n'engage aucun calendrier normatif.** Tri du Vol. I : l'existence des groupes est PROGRAMMÉ, leur conversion en standards reste SPÉCULATIF. → *ch. 3.*
- **H-21 [C] — Le SOC agentique.** `Monographie.md` §7.5.2 : défense agentique continue où des agents surveillent d'autres agents, *red-teaming* inter-agents permanent. Statut mixte assumé : PROGRAMMÉ pour les référentiels datés, PROJETÉ pour les prévisions. Une seule projection chiffrée, millésimée : Gartner (2024) anticipait ~25 % des brèches d'entreprise imputables à l'abus d'agents d'IA d'ici 2028 — **projection, à attribuer à chaque occurrence**. → *ch. 15.*
- **H-22 [C] — Les référentiels de sécurité agentique en mouvement.** `Monographie.md` §7.5.3 : MITRE ATLAS, techniques AML.T0104 (outils d'agent empoisonnés) et AML.T0105 (évasion vers l'hôte), dépôt versionné ; OWASP « Top 10 for Agentic Applications for 2026 » et « State of Agentic AI Security and Governance » ; **initiative « AI Agent Standards » du NIST CAISI, lancée le 17 février 2026, comportant un pilier identité et sécurité**. → *ch. 12, ch. 15.*
- **H-23 [C] — La science de l'évaluation.** `Monographie.md` §7.6.4 : à juin 2026, l'évaluation des systèmes d'agents est largement immature ; absence de bancs d'essai inter-fournisseurs reconnus et de métriques d'interopérabilité mesurables (Yehudai et coll., arXiv:2503.16416) ; taxonomie des défaillances MAST (arXiv:2503.13657). **Manque structurant nommé : il n'existe pas de métrique d'horizon de tâche déléguée** — l'horizon mesuré porte sur un agent isolé, non sur une délégation inter-agents. Conséquence retenue : « ce qui n'est pas mesurable n'est pas contractualisable ». → *ch. 25, ch. 26.*
- **H-24 [C] — La non-compositionnalité de la sûreté.** `Monographie.md` §3.10.1, **verbatim exact** : « un agent sûr et un outil sûr, une fois composés, ne donnent pas un système sûr. La sûreté n'est pas une propriété compositionnelle. » Et, dans le même paragraphe : « la frontière de confiance n'est plus le périmètre d'un système mais *chaque arête* du graphe d'interaction ». Corollaire de §3.10.2 : « un modèle de menace agentique doit raisonner sur le graphe de composition, pas sur l'inventaire des composants ». → *ch. 22 §22.3 — c'est la prémisse qui fait du maillage une conséquence architecturale et non une mode.*
- **H-25 [C] — Le *rug-pull* et l'intégrité continue.** `Monographie.md` §3.10.3 et §3.10.4 : un serveur initialement bénin modifie après coup la définition d'un outil approuvé ; mitigation ETDI (Bhatt et al., 2025). **Verrou ouvert en 2026** : « la vérification d'intégrité *continue*, seule réponse robuste au *rug-pull*, demeure immature — la signature au moment de la publication n'empêche pas une mutation ultérieure du comportement d'un serveur déjà approuvé, et aucun mécanisme normalisé ne garantit que ce qui a été audité reste ce qui s'exécute. » → *ch. 13 — la thèse du chapitre est déjà là ; il reste à l'instruire.*
- **H-26 [C] — Injection et empoisonnement.** `Monographie.md` §2.10.2.1 (injection d'invite directe et **indirecte** — l'instruction hostile placée dans un contenu que l'agent récupère lui-même : courriel, page web, passage RAG, sortie d'outil) ; §2.10.2.2 (empoisonnement d'outils par les descriptions en langage naturel ; *rug-pull* comme variante temporelle ; empoisonnement de mémoire comme prolongement dans le temps) ; §3.10.3 (**transitivité de la confiance**, illustrée par EchoLeak, CVE-2025-32711, CVSS 9.3). Le Vol. I pose l'injection comme **non résoluble au niveau du modèle** : le confinement relève du *containment*, non de la prévention. → *ch. 12 §12.3.*
- **H-27 [C] — L'invariant à quatre termes.** `Synthese Monographie.md` §10.3, **verbatim** : « *Découplage, contrat, évolution* deviennent ainsi *découplage, contrat, évolution, exploitation*. » Repris en §11.1 et en §12. Thèse associée : « l'interopérabilité agentique n'est durable que couplée à l'exploitation résiliente qui la maintient — un parc n'est conforme que s'il demeure observable et remédiable sans rompre ses propres invariants ». **C'est le fondement de la Partie VIII**, et l'énoncé canonique de l'invariant à trois termes est en `Monographie.md` §1.0.2.1. → *Partie VIII, ch. 17.*
- **H-28 [C] — La délégation au-delà de deux sauts.** `Synthese Monographie.md` §11.5, **verbatim** : « l'identité non humaine et la traçabilité de bout en bout des décisions déléguées au-delà de deux sauts restent des problèmes ouverts, dont l'urgence croît avec le degré d'autonomie consenti » ; et « le besoin d'une *science de l'évaluation* inter-fournisseurs, condition de toute certification, et d'une **métrique d'horizon de tâche déléguée** ». → *ch. 10, ch. 26 §26.3.*
- **H-29 [C] — Le verrou d'origine.** `Synthese Monographie.md` §11.6, tableau 15 (« Réalisation de l'invariant et verrou dominant, par strate »), ligne **Entreprise (§6)** : réalisation du contrat = « Politique d'autorisation, plan de contrôle » ; verrou dominant à juin 2026 = « **Identité non humaine et délégation multi-saut** ». → *avant-propos — c'est l'origine déclarée de l'ouvrage.*
- **H-30 [C] — Le plan de contrôle obligatoire.** `Synthese Monographie.md` §10.2, **verbatim** : « L'ADS traite la plateforme d'agents non comme un dispositif à gouverner après coup, mais comme un **plan de contrôle obligatoire** couplé à une **dorsale d'intégration tri-plan**. Sa logique tient en une phrase : l'agent prépare ; un humain ou un contrôle déterministe engage l'irréversible ; toute action transite par un point d'application de politique unique ; tout actif décisionnel est un modèle inventorié. » ⚠ Dans l'Annexe B du Vol. I, l'expression est **instanciée sur des produits nommés** : ne pas reprendre l'instanciation, seulement le principe. → *ch. 23 — le maillage en est le prolongement au grain de l'infrastructure.*
- **H-31 [C] — L'autonomie graduée.** `Monographie.md` §5.0.2 et §5.1.1 (siège du patron) : « un agent ne doit jamais exécuter une action irréversible sans garde-fou structurel ; la règle est la préparation par l'agent et la release humaine sur l'action irréversible » ; échelle à quatre paliers **assistance → copilote → orchestration sous revue → autonomie bornée**, indexée sur le produit matérialité × réversibilité, non sur la capacité brute du modèle. ⚠ **Trois échelles d'autonomie coexistent dans le Vol. I et sont fréquemment confondues** : celle-ci ; le « continuum d'autonomie, niveaux 0 à 5 » de §2.2.4 (analogie automobile) ; la graduation L0/L1/L2/L3 de l'Annexe B **§1.3** (siège — §12.2 n'en donne que la machine à états, « sans en redéfinir les niveaux »). **Le §27.4 emploie la première, et le dit** (R-13). → *ch. 27 §27.4.*
- **H-32 [C] — Le cas fil rouge.** Coopérative financière **Boréalis**, entreprise fictive : coopérative de services financiers du Québec, institution financière fédérale sous BSIF et assujettie à l'AMF ; cinq sous-domaines ; contraintes-pivots Loi 25 art. 12.1, résidence des renseignements personnels au Canada, E-23/B-10/B-13, ligne directrice IA de l'AMF. ⚠ **Le nom ne figure pas dans `Synthese Monographie.md`** : il est porté par `Monographie.md` § Annexe B et par `Chapitres/Annexe B - Architecture de Solutions.md` (§7.4.3). À ne pas confondre avec **Borealis-Go**, le démonstrateur logiciel du Vol. I, qui est un autre objet. → *ch. 28.*
- **H-33 [C] — Le tri prospectif.** `Monographie.md` §7.0.2, siège de la discipline. **PROGRAMMÉ** : engagement daté réel — texte réglementaire à entrée en vigueur future, feuille de route publiée, échéance de standard ; porte sa source et sa date. **PROJETÉ** : prévision d'analyste ou d'institution ; exige source nominative, millésime et périmètre. **SPÉCULATIF** : pari de recherche, scénario, discontinuité. **Règle absolue : ne jamais présenter du PROJETÉ ni du SPÉCULATIF comme acquis.** Une charte de Community Group ou de Working Group fait basculer un objet vers le programmé ; un préprint portant un programme de recherche relève par construction du spéculatif. → *méthode, avant-propos, ch. 8 §8.3, Partie V, annexe A de l'ouvrage.*

**Cardinal du socle hérité : 33 entrées** — H-01 à H-33, numérotation continue, sans discontinuité ni suffixe à ce jour. Commande de recomptage, à réexécuter à chaque enrichissement plutôt qu'à dériver de tête :

```sh
grep -oE '^- \*\*H-[0-9]+[a-z]?' PRD.md | sed 's/- \*\*//' | sort -u | wc -l
```

⚠ **Le cardinal (33) et le plus haut identifiant (H-33) coïncident aujourd'hui.** Ils se désolidariseront dès la première fusion ou le premier suffixe. Ne jamais dériver le cardinal d'une borne d'identifiants — c'est la faute que le Vol. II a mis deux phases à détecter, précisément parce que la coïncidence la rendait invisible à la relecture.

**Cardinal du socle propre : 0.** Aucune entrée F-xx n'est attribuée. Les identifiants F-01 et suivants sont **réservés** aux faits que ce volume vérifiera lui-même, et le premier sera attribué à la clôture du premier lot.

### 7.4 Écarts constatés entre le TOC et l'état réel des volumes

Sept extractions parallèles ont vérifié, le 18 juillet 2026, chacun des renvois que le TOC v0.4 porte vers les Vol. I et II et vers le dépôt lui-même. **Neuf écarts.** Ils sont consignés ici parce qu'un renvoi cassé, dans un ouvrage qui fait de la traçabilité sa thèse, est plus qu'une coquille — le TOC le dit lui-même à son risque n° 9. Aucun n'est corrigé dans le TOC par le présent document ; le PRD **refuse de les propager** et demande la révision (J-1).

**§7.4.1 — La numérotation du Vol. I est triple, non double ; et l'intervalle annoncé est faux.** Le TOC (en-tête, ligne « Filiation ») écrit que `Synthese Monographie.md` porte la « numérotation §3-§12 ». **Elle porte §1 à §12** (« ## 1. Introduction » … « ## 12. Conclusion »), en titres de niveau 2, sans aucun titre de niveau 1. Conséquence non anodine : **§3 à §7 existent dans les deux fichiers** — sections thématiques dans la synthèse, sous-sections des chapitres 3 à 7 dans la monographie. Un pointeur « §7.4 » est donc **ambigu**, et le TOC l'emploie sans nommer le fichier. S'y ajoute une **troisième numérotation** non signalée : l'Annexe B (`Monographie.md` à partir de la ligne 5333, et `Chapitres/Annexe B - Architecture de Solutions.md`) numérote ses propres sections de §0 à §17. **Règle du Vol. III : tout renvoi au Vol. I nomme son fichier** — et, pour l'Annexe B, le dit.

**§7.4.2 — « §7.0.1 » ne porte pas le quatrième terme.** Le TOC renvoie à « §7.0.1 et §10 » pour l'*exploitation*. Dans `Monographie.md`, §7.0.1 s'intitule « Mode d'emploi : acquis (ch.1-6) vs ajouté (ch.7) » et **ne mentionne pas l'exploitation** ; la phrase visée est en **§7.0**. Le siège canonique reste `Synthese Monographie.md` **§10.3**, qui porte l'énoncé complet. Renvoi corrigé en H-27.

**§7.4.3 — Boréalis n'est pas dans la synthèse.** Le TOC (ch. 28) écrit « continuité avec Boréalis, Vol. I, *Synthèse* §10 ». Le nom **n'apparaît pas une seule fois** dans `Synthese Monographie.md`, dont le §10 ne désigne l'entité que par « une entreprise fictive — une coopérative financière québécoise ». Le fil rouge nommé vit dans l'**Annexe B**. Renvoi corrigé en H-32.

**§7.4.4 — « KYA, terme de marché » n'est pas au `Monographie.md` §7.4.3.** Le TOC assigne au ch. 11 le garde-fou « « KYA » est un terme de marché avant d'être un terme de norme ». L'expression « terme de marché » **est introuvable dans tout le Vol. I**. L'énoncé équivalent existe, mais en **§5.5.4**, siège du KYA : « à juin 2026, le KYA n'est **pas un standard établi** ; les initiatives existantes relèvent du positionnement fournisseur ». Le garde-fou reste fondé ; sa **formulation est une construction d'auteur du Vol. III** et doit être marquée telle (R-05).

**§7.4.5 — La formule de non-compositionnalité est une condensation, et le TOC ne nomme pas son siège.** Le TOC (ch. 22 §22.3) cite « la sûreté n'est pas compositionnelle — la frontière de confiance se déplace vers chaque arête du graphe », sans dire d'où. Le Vol. I porte cette formule à **quatre endroits, sous trois formes**, ce que le TOC masque. Forme longue, en deux phrases distinctes : `Synthese Monographie.md` **§5.10** (« Sécurité non composable et modes d'échec » — **le siège déclaré**, vers lequel les autres renvoient) et `Monographie.md` **§3.10.1** (forme reprise en H-24). Forme courte, sans « propriété » : `Synthese Monographie.md` **§6.12**. Forme condensée, les deux membres en **une seule phrase** et au plus près du TOC : `Synthese Monographie.md` **§11.3** — « la sûreté n'est pas une propriété compositionnelle — un agent sûr et un outil sûr, composés, ne donnent pas un système sûr —, ce qui déplace la frontière de confiance de chaque système vers chaque arête du graphe d'interaction ». Le TOC condense donc fidèlement §11.3 — **il ne fabrique rien**, mais il élide (« de chaque système », « d'interaction ») et **ne nomme pas le fichier**, en contravention de la règle du §7.4.1. **Règle du Vol. III : citer cette formule en nommant son fichier et sa section** — `Synthese` §5.10 ou `Monographie.md` §3.10.1 pour la forme longue, `Synthese` §11.3 pour la condensée — et ne revendiquer le verbatim que sur l'une d'elles, mot pour mot (CA-05).

**§7.4.6 — L'homonymie « AgentMesh » a changé de nature.** Le TOC demande de noter l'homonymie avec « le nom de code du dépôt du diptyque (« AgentMesh ») ». Le dépôt s'appelle aujourd'hui **`Monographies`** ; « AgentMesh/ » ne survit que comme racine d'un bloc d'arborescence périmé dans le PRDPlan du Vol. II (§1.3). Mais l'homonymie **reste à traiter, pour une autre raison** : le TOC du Vol. IV emploie « AgentMesh » pour désigner **les équipes plateforme**. Le garde-fou est maintenu, sa justification corrigée (R-04, branche (f)).

**§7.4.7 — Le jeu de questions du ch. 21 en compte six, et ses étiquettes sont homonymes de celles du ch. 16.** Le §21.2 du Vol. II porte **Q1 à Q6**, non Q1 à Q5 — la sixième (« Comment le *frame* opérationnel s'articule-t-il au *frame* normatif ? ») existe et n'est pas reprise ici. Plus grave : **le ch. 16 §16.3 porte un jeu Q1-Q5 entièrement distinct**, sans aucun recouvrement. Le Vol. II disjoint son jeu du ch. 16 de la seule question de la désignation de l'organisme de normalisation, traitée au ch. 14 — « Les confondre serait fusionner deux ignorances que le socle tient séparées » — mais **il ne signale nulle part l'homonymie des étiquettes entre ses deux jeux**. Les cinq étiquettes Q1 à Q5 désignent donc **deux objets chacune**, le ch. 21 en ajoutant une sixième sans homonyme, et l'écart n'a été détecté ni en amont ni par le TOC. **Règle du Vol. III : toute reprise nomme le chapitre.** Couverture de ce volume, énoncée sans ambiguïté :

| Question | Objet | Traitement au Vol. III |
|---|---|---|
| **ch. 21 Q2** | mécanique des risques protocolaires ; attaques propres à A2A | **instruite** — ch. 12 (lot L-08) |
| **ch. 21 Q3** | valeur cryptographique d'une carte d'agent signée | **instruite** — ch. 5 (lot L-03) |
| **ch. 21 Q5** | désignation de l'organisme de normalisation technique | **instruite** — ch. 21 (lot L-12) |
| ch. 21 Q4 | art. 12.1 et décision multi-agents avec humain-dans-la-boucle | **prolongée, non tranchée** — ch. 20 |
| ch. 21 Q1 | reproduction indépendante d'OO1–OO4 | **non reprise** — reste au Vol. II |
| ch. 21 Q6 | articulation frame opérationnel / frame normatif | **non reprise** — reste au Vol. II |
| ch. 16 Q1-Q5 | AP2 et les rails de paiement canadiens | **hors périmètre**, sauf Q2 (gouvernance d'AP2) qui rejoint la divergence §7.5 |

**§7.4.8 — Le risque n° 9 (b) du TOC est périmé.** Le TOC reproche au README racine de décrire une arborescence `vol-1-…/`, `vol-2-…/` qui ne correspond pas aux dossiers réels. **Vérifié : zéro occurrence** de `vol-1`, `vol-2` ou `vol-3` dans le README et le CLAUDE.md racine ; le bloc d'arborescence reproduit les dossiers réels, y compris `3 - EntrepriseAgentique/`, et le README documente lui-même la resynchronisation. **Reproche à retirer.**

**§7.4.9 — Le risque n° 9 (a) est à moitié faux, et sa moitié fausse est auto-référentielle.** `commun/faits-partages.md` est bien **absent** du dépôt et bien **cité** — README racine, TOC du Vol. III (trois fois), TOC du Vol. IV. Mais `eval.md` **n'est cité nulle part dans le dépôt, sauf par le reproche lui-même** : le TOC affirme qu'il est « cité par le README racine et par ce TOC (ch. 9) », et ni l'une ni l'autre affirmation n'est vraie — le ch. 9 du TOC cite `commun/faits-partages.md`, pas `eval.md`. **Le reproche décrit un renvoi fantôme qui n'existe pas.** À retirer ; la moitié qui vise `commun/faits-partages.md` est à conserver et à trancher (§7.5).

### 7.5 Divergences non arbitrées — signalées, jamais uniformisées

Deux faits datés divergent entre les livrables du dépôt. Le CLAUDE.md racine impose de les signaler sans les arbitrer. Le Vol. III les **porte** et ne les tranche pas ; le Vol. IV projette de le faire, sans autorité tant qu'il n'est pas rédigé.

| Objet | Positions | Incidence sur le Vol. III |
|---|---|---|
| **Gouvernance d'AP2** | Vol. I (ch. 3) et veille technologique : transfert à la **FIDO Alliance le 28 avril 2026** (v0.2, prise en charge *Human-Not-Present*), présenté comme fait établi et daté — « FIDO Alliance, PAS Linux Foundation ». Vol. II (gel 16-17 juillet 2026) : **aucun transfert documenté**, position tenue en quatre endroits concordants (ch. 1, ch. 3, ch. 16 Q2, ch. 21 §21.1), où elle est rangée parmi les **ignorances déclarées**. | **ch. 9 §9.1** mobilise les mandats AP2. Le chapitre expose les deux positions, les attribue, et **instruit la divergence** (lot L-06) — c'est la tâche que le TOC lui assigne. Il ne choisit pas par défaut la plus récente : le Vol. II est postérieur au Vol. I et *plus* réservé, ce qui interdit l'arbitrage par chronologie. |
| **Date de la version finale de la ligne directrice IA de l'AMF** | Vol. II : **30 mars 2026**, avec dette de vérification déclarée (`lautorite.qc.ca` renvoie 403 aux outils). Veille : **7 avril 2026**. | **ch. 19** repose sur ce texte. Écrire la date avec sa divergence, ou n'écrire que ce qui ne dépend pas d'elle — **l'entrée en vigueur au 1er mai 2027 est concordante** et suffit à la thèse du chapitre. |

⚠ **Le fichier prévu pour porter ces divergences — `commun/faits-partages.md` — n'existe pas.** Le TOC le marque « à créer » ; le README racine signale son absence. **Décision de ce PRD** : le fichier n'est pas créé par le volume III. Les divergences vivent **ici**, en §7.5, qui devient leur source de vérité pour la durée de rédaction du volume ; les renvois du TOC vers `commun/faits-partages.md` sont à repointer vers cette section. Motif : créer un fichier partagé hors du périmètre d'un volume, à un moment où aucun autre volume n'est en écriture, ajouterait un troisième document de gouvernance à maintenir pour deux lignes de contenu. Si le Vol. IV entre en rédaction, la question se rouvre — et c'est lui qui la tranchera, puisque son cadrage annonce déjà de trancher ces divergences plutôt que de les signaler.

### 7.6 Programme de constitution du socle — 15 lots d'instruction

Chaque lot énonce : ce qu'il doit établir, les sources primaires à consulter, le niveau visé, et s'il **bloque** un chapitre. Un lot est **clos** quand ses affirmations centrales atteignent le niveau visé ou quand son échec est documenté (une lacune instruite et infructueuse est un résultat ; une lacune non instruite n'en est pas un — §8.6).

| Lot | Objet | Sources primaires visées | Niveau visé | Bloque |
|---|---|---|---|---|
| **L-01** | Identité machine héritée et étirement des RFC : OAuth 2.x appliqué à l'agent, SCIM et provisionnement, **jetons de transaction** (`draft-ietf-oauth-transaction-tokens`), WIMSE — **état et date d'expiration réels de chaque draft** | datatracker.ietf.org ; RFC 6749, 7643 ; SPIFFE/SPIRE (CNCF) | [B] | ch. 1, 2 |
| **L-02** | Corpus W3C : VC Data Model, DID Core — ce que les recommandations **établissent** ; chartes et état des Community Groups ; fossé adoption en entreprise financière | w3.org (recommandations datées) ; chartes des CG ; DIF | [B] | ch. 3 |
| **L-03** | **Q3 (ch. 21)** — carte d'agent signée : format, chaîne de signature, **ancrage de confiance, régime de révocation, gouvernance des clés** | spécification A2A ; documentation de gouvernance des clés du projet | **[A] visé, [B] plancher** | **ch. 5** |
| **L-04** | Entra Agent ID : périmètre GA **à date**, licences, nature des *blueprints* ; offres équivalentes des autres fournisseurs infonuagiques | Microsoft Learn ; docs AWS, Google Cloud | [B] | ch. 6 |
| **L-05** | Registres : état du brouillon CSA à date, consolidation IETF 125 ; registres et découverte A2A/AGNTCY | labs.cloudsecurityalliance.org ; docs.agntcy.org ; a2a-protocol.org | [B] | ch. 7 |
| **L-06** | Chaîne de mandat : mandats AP2, *on-behalf-of*, jetons de transaction ; **+ instruction de la divergence de gouvernance d'AP2 (§7.5)** | spécification AP2 ; FIDO Alliance ; Linux Foundation ; Google Cloud | [B] | ch. 9 |
| **L-07** | KYA : état des propositions, livre blanc OpenID Foundation, CG W3C ; précédents de fédération (eIDAS, FIDO) et leur transposabilité | openid.net ; w3.org ; textes eIDAS | [B] | ch. 11 |
| **L-08** | **Q2 (ch. 21)** — taxonomie des attaques : identifiants de vulnérabilité, **incidents publics datés**, littérature académique ; empoisonnement de mémoire et des sources | MITRE ATLAS ; OWASP ; CVE/NVD ; arXiv ; spécifications (sections sécurité) | **[A] visé sur les affirmations centrales** | **ch. 12** |
| **L-09** | *Rug-pull* et attestation d'intégrité à l'exécution ; **inventaire de la révocation par mécanisme** ; précédent PKI (CRL, OCSP) | spécifications ; RFC 5280, 6960 ; littérature ETDI | [B] | ch. 13, 14 |
| **L-10** | SOC agentique : offres datées et périmètres réels ; état 2026 des référentiels de sécurité agentique | MITRE ATLAS ; OWASP ; NIST CAISI ; documentation d'éditeurs | [B] | ch. 15 |
| **L-11** | Horloge post-quantique : **statut réel de NIST IR 8547** (projet ou final ?), FIPS 203/204, recommandations de crypto-agilité, études de coût publiées | nist.gov ; textes du décret 14412 ; Europol QSFF | [B] | ch. 16, 17, 18 |
| **L-12** | Droit : E-23 et **contenu article par article de la ligne directrice IA de l'AMF** (lacune héritée du Vol. II) ; art. 12.1 et positions de la CAI ; **Q5 (ch. 21)** — état de la désignation | osfi-bsif.gc.ca ; lautorite.qc.ca ; legisquebec.gouv.qc.ca ; cai.gouv.qc.ca ; gazette.gc.ca | [B] | ch. 19, 20, 21 |
| **L-13** | Maillage : passerelles MCP, courtage A2A, transport AGNTCY (SLIM), moteurs de politique ; *zero trust* (NIST SP 800-207) et ses déclinaisons agentiques — **tri strict annonce / GA / production** | nist.gov ; docs.agntcy.org ; documentation des passerelles ; corpus service mesh CNCF | [B] | ch. 22, 23 |
| **L-14** | Observabilité : **conventions sémantiques OpenTelemetry pour l'IA générative et les agents — statut stable ou expérimental, version et date** ; plateformes d'observabilité agentique | opentelemetry.io (spécification versionnée) ; documentation d'éditeurs | [B] | ch. 24, 26 |
| **L-15** | **Corpus d'appui : dépôt effectif des trois ouvrages**, puis extraction citée chapitre par chapitre | les trois ouvrages eux-mêmes (§7.7) | [C] à l'entrée, [B] par extraction citée | **§4.4, §9.4, §25.1, §25.5, §27.4, §27.5, §28.4, annexe E** |

**Trois lots sont déclarés bloquants au sens fort** — leur échec ne se contourne pas par une reformulation prudente, il supprime le chapitre ou le réduit à une lacune : **L-03** (sans lui, le ch. 5 n'a pas d'objet et Q3 reste ouverte), **L-08** (sans lui, la Partie IV n'est qu'une reprise du Vol. I), **L-15** (sans lui, sept sections et une annexe entière tombent — §7.7).

### 7.7 Corpus d'appui — l'écart entre l'annonce et le disque

Le TOC intitule sa section « **Corpus d'appui (déposé au dépôt, 18 juillet 2026)** » et décrit trois ouvrages. **Vérification du 18 juillet 2026 : aucun des trois n'est déposé.**

| Ouvrage | Annoncé | État réel |
|---|---|---|
| *Agentic Architectural Patterns for Building Multi-Agent Systems* — Arsanjani & Bustos (Packt) | déposé | **INTROUVABLE** |
| *Agentic AI for Engineers* — Nagasubramanian (Apress, 2026, ISBN 979-8-8688-2361-9) | déposé | **INTROUVABLE** |
| *Agentic AI in Enterprise* — Ranjan, Chembachere & Lobo (Apress, 2025, ISBN 979-8-8688-1542-3) | déposé | **INTROUVABLE** |

Méthode de vérification, donnée pour qu'elle soit rejouable : inventaire exhaustif des extensions du dépôt (**aucun `.epub`, `.mobi`, `.azw3`, `.djvu` ; 8 `.pdf`, tous identifiés** — six sorties produites par le dépôt, deux préprints arXiv rattachés au socle du Vol. II) ; recherche par nom d'auteur et par titre ; recherche des deux ISBN sur l'intégralité du dépôt — **ils n'apparaissent que dans le TOC lui-même** ; historique git complet (`git log --all --name-only`) — **aucun chemin contenant `epub`, `arsanjani`, `nagasu`, `ranjan`, `packt` ou `apress` n'a jamais existé**, ce n'est donc pas un fichier supprimé après coup ; absence de Git LFS.

**Conséquences, et elles sont structurantes.**

1. **Le corpus d'appui est décrit, non déposé.** Le titre de section du TOC est à corriger (J-1). Un ouvrage qu'on n'a pas sous la main ne peut être ni cité ni extrait : la règle d'élévation « [C] à l'entrée, [B] par extraction citée chapitre par chapitre » **présuppose l'accès au texte**.
2. **Sept sections et une annexe sont bloquées** : §4.4 (croisement grille × maturité), §9.4 (typologie des patrons d'interaction humain-agent), §25.1 (test-débogage-évaluation-déploiement), §25.5 (patrons d'apprentissage), §27.4 (les trois modèles de maturité), §27.5 (préparation organisationnelle), §28.4 (cas fil rouge *loan processing*), et l'**annexe E** dont le gabarit de patrons revendique la filiation avec Arsanjani-Bustos.
3. **Aucune de ces sections ne se rédige « de mémoire ».** Écrire ce que ces livres contiennent sans les avoir ouverts serait la faute exacte du risque n° 8 du TOC — traiter un manuel publié comme une entrée de socle au motif qu'il est imprimé — aggravée d'un cran, puisqu'il ne serait même pas lu.
4. **Deux issues, à trancher par l'auteur** (§12, J-1) : déposer les trois ouvrages et clore L-15 ; ou **retirer la filiation livresque** et réécrire les sept sections sur le socle propre — auquel cas §27.4 devient une construction d'auteur adossée à l'autonomie graduée du Vol. I (H-31) et à la grille du ch. 4, et l'annexe E revendique sa filiation avec l'héritage GoF/EIP que le Vol. I mobilise déjà, sans passer par Arsanjani-Bustos.

⚠ **Réserve de biais, à conserver dans les deux cas — et le TOC se contredit sur son étendue.** Son tableau du corpus d'appui n'attache la réserve d'écosystème Google Cloud qu'à Arsanjani & Bustos, tandis que son risque n° 7 écrit « deux des trois ouvrages sont d'auteurs Google Cloud » **sans nommer le second**, la justification entre parenthèses renvoyant à la préface de ce même premier ouvrage. Le TOC du Vol. IV reprend le « deux » sans le nommer davantage. **Incohérence interne à corriger au TOC (J-1)** ; elle ne se tranche qu'ouvrage en main. **Règle du « jamais seul » reconduite sans amendement** : aucune affirmation centrale n'est portée par le corpus d'appui sans source primaire concordante, et toute affirmation protocolaire reprise d'un livre est vérifiée à la spécification.

## 8. Garde-fous rédactionnels (obligatoires)

### 8.1 Formulations proscrites — R-01 à R-14

⚠ **Convention de numérotation.** Les garde-fous du Vol. III sont notés **R-01 à R-14** (deux chiffres) ; ceux du Vol. II, **R-1 à R-8** (un chiffre). Tout renvoi nomme le volume.

| # | À ne jamais écrire | À écrire |
|---|---|---|
| **R-01** | « le passeport d'agent, défini par [spécification] » ; toute formulation faisant du passeport un objet existant | **Le passeport d'agent n'existe dans aucune spécification de 2026.** C'est un objet de synthèse construit par cet ouvrage (ch. 8), assemblé de quatre pièces documentées séparément. Sa normalisation est **projetée**, jamais acquise. |
| **R-02** | « la carte signée **garantit** l'identité de l'agent » ; toute qualification d'un mécanisme cryptographique par sa promesse | **Convention cardinale du volume** : un mécanisme cryptographique est qualifié par ce que sa spécification **démontre**, jamais par ce qu'elle **promet**. Une signature vaut ce que valent son ancrage, sa révocation et sa gouvernance des clés — trois éléments dont l'état de documentation est le sujet du ch. 5. *L'ouvrage naît de Q3 ; il ne peut pas reproduire la faute que Q3 dénonce.* |
| **R-03** | « le maillage d'agents », « l'AgentOps », « l'entreprise agentique » employés comme des catégories établies | **Trois termes de marché sans définition normative à date.** Chacun reçoit sa définition d'auteur à un siège unique — « entreprise agentique » à l'avant-propos, « maillage d'agents » au ch. 22 §22.1 par filiation *service mesh*, « AgentOps » au ch. 24 §24.1 par filiation APM/MLOps — et son statut épistémique à l'annexe D. |
| **R-04** | Le sigle « ACP » employé seul ; « plan de contrôle » sans qualificatif | **Six emplois distincts, chacun avec son qualificatif complet** : (a) ACP protocolaire (IBM Research/BeeAI, fusionné dans A2A) ; (b) *Agentic Control Plane* du consortium Lightworks–Scotiabank–Sun Life–TELUS ; (c) *agentic control plane*, positionnement de watsonx Orchestrate, **attribué à IBM à chaque occurrence** ; (d) composante ACP d'AGNTCY, **non caractérisée, jamais agrégée à (a)** ; (e) **plan de contrôle au sens infrastructure** (Partie VII), par filiation *service mesh* ; (f) **« AgentMesh »**, employé par le cadrage du Vol. IV pour les équipes plateforme (§7.4.6). Désambiguïsation posée au ch. 22 §22.1, première occurrence réelle. |
| **R-05** | « KYA, terme de marché » présenté comme un constat du Vol. I | Le Vol. I écrit, en `Monographie.md` §5.5.4 : « le KYA n'est **pas un standard établi** ; les initiatives existantes relèvent du positionnement fournisseur ». La formule « terme de marché avant d'être terme de norme » est une **construction d'auteur du Vol. III** ; la marquer (§7.4.4). Ajouter le fait saillant : **aucun forum n'avait tranché à juin 2026.** |
| **R-06** | « exigé par E-23 », « E-23 impose », « l'exigence d'inventaire d'E-23 » ; « fiche de modèle » / « model card » ; « E-23 exige pour l'IA agentique » | **« attendu par E-23 », « les attentes d'E-23 », « E-23 attend que… »** — ligne directrice fondée sur des principes, rédigée au conditionnel. **« documentation de modèle »** et **« inventaire »**, jamais « fiche de modèle » (0 occurrence, EN et FR). La couverture agentique est une **couverture implicite** via la définition « intentionally broad », **attribuée aux analystes juridiques**, jamais au BSIF. ⚠ Le motif de balayage doit attraper « exigence » **sans le sigle sur la même ligne** : la faute est passée sous l'outil au Vol. II. |
| **R-07** | « [produit] est conforme à E-23 / à la ligne directrice de l'AMF » ; toute correspondance produit ↔ réglementation présentée comme documentée | « Le rapprochement entre [composant] et [exigence] est une **inférence d'auteur**. » Pour E-23 et B-13 uniquement, ajouter : « [éditeur] ne revendique aucune conformité, et aucune source ne documente ce lien » — **fait négatif établi**, non vérifié (§8.6). |
| **R-08** | « aucun incident public majeur n'est documenté, **donc** la pile est sûre » | **L'absence d'incident public est un fait à interpréter avec prudence, pas une preuve de sûreté** (ch. 12 §12.4). Elle peut signaler une surface encore peu déployée, une détection immature, ou une divulgation non publique. |
| **R-09** | « le W3C normalise le passeport d'agent » ; « le Community Group X prépare la norme Y » | **Une charte de Community Group n'est pas un standard.** Un CG ne produit pas de Recommandation et n'engage aucun calendrier normatif (H-20). Distinguer CG, Working Group, Candidate Recommendation et Recommandation à chaque mention. |
| **R-10** | Une affirmation centrale portée par le seul corpus d'appui | **Règle du « jamais seul ».** Aucune affirmation centrale n'est portée par un ouvrage du corpus d'appui sans source primaire concordante. Toute affirmation **protocolaire** reprise d'un livre est vérifiée à la spécification. Tout fait daté repris porte **la date du livre**, pas celle de sa lecture. |
| **R-11** | « la PQC est obligatoire en 2030 » ; « le NIST interdit RSA-2048 en 2035 » | **Un jalon NIST n'est pas une obligation légale**, et **IR 8547 est, au socle hérité, un *Initial Public Draft* dont le Vol. I porte lui-même la réserve « dates à re-vérifier »** (H-17). Écrire « dépréciation **visée** pour 2030 », « interdiction **visée** pour 2035 », avec le statut du document. **Ne jamais fusionner** les jalons IR 8547, ceux du décret 14412 et ceux du Quantum Safe Financial Forum. |
| **R-12** | Toute reproduction de charge utile, de séquence d'exploitation ou de preuve de concept offensive | **Traitement défensif exclusif.** La Partie IV décrit la mécanique des attaques **au niveau architectural** — quel maillon de la chaîne d'identité ou de mandat cède, et pourquoi. Elle **cite** les identifiants de vulnérabilité et les incidents ; elle ne les reproduit pas. Un lecteur ne doit pas pouvoir dériver une attaque du texte. |
| **R-13** | « l'autonomie graduée du Vol. I », sans autre précision | **Trois échelles coexistent au Vol. I** (H-31). Le §27.4 emploie l'échelle **assistance → copilote → orchestration sous revue → autonomie bornée** (`Monographie.md` §5.0.2, siège §5.1.1) et le nomme. Ne pas la confondre avec le continuum 0-5 de §2.2.4 ni avec la graduation L0-L3 de l'Annexe B **§1.3** (siège ; §12.2 n'en est que la machine à états). |
| **R-14** | « le socle ne documente pas X, **donc** X n'existe pas » | **Trois degrés d'absence, vocabulaire imposé** (§8.6). Une absence de documentation n'est pas un fait négatif, et un fait négatif établi n'est pas un fait négatif vérifié. La distinction décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable. |

### 8.2 Règles d'attribution

1. **Métriques d'adoption des protocoles et des standards** (organisations déclarant leur soutien) : auto-déclarées ; « soutien » ≠ production ; attribuer au communiqué et à sa date.
2. **Métriques d'éditeurs** (couverture d'un annuaire d'agents, nombre d'agents gérés, volumétrie d'un maillage) : auto-déclarées par l'éditeur ; **attribution nominative à chaque occurrence, sans exception d'usage illustratif**. La règle est celle de l'avant-propos du Vol. II, reconduite au mot : *un chiffre auto-déclaré qu'on cesse d'attribuer devient, en trois citations, un fait.*
3. **Chiffres de prolifération NHI** (ratios identités machines/humaines) : rapports d'éditeurs ; **illustration, jamais preuve** — la thèse du ch. 1 ne doit dépendre d'aucun de ces chiffres.
4. **Projections d'analystes** (part des brèches imputables aux agents, adoption du maillage) : source nominative, millésime et périmètre ; **PROJETÉ**, jamais acquis.
5. **Couverture agentique des cadres réglementaires** : inférence d'analystes juridiques — jamais « le BSIF exige pour l'IA agentique » (R-06).
6. **Statuts pré-normatifs** : brouillon de labs, *Internet-Draft* (avec sa date d'expiration), Candidate Recommendation, préversion — dits à chaque mention (R-09).
7. **Études d'analystes commandées** : commanditaire nommé à chaque citation.
8. **Corpus d'appui** : titre, auteurs, éditeur et **année de bouclage éditorial** à chaque reprise (R-10).

### 8.3 Sensibilité temporelle

Le domaine se périme par trimestres, et ce volume hérite de deux gels distincts — **juin 2026** (Vol. I) et **16-17 juillet 2026** (Vol. II). **Chaque chapitre porte sa propre date de gel**, consignée au registre (§11, CA-04).

Faits chauds à revalider avant toute rédaction qui en dépend, et de nouveau avant publication :

| Échéance | Objet | Chapitres touchés |
|---|---|---|
| **28 juillet 2026** | Révision majeure de la spécification MCP (protocole sans état, retrait de `Mcp-Session-Id`) — **dix jours après ce PRD** | ch. 2, 22 |
| après le 26 août 2026 | Texte final du règlement du cadre bancaire ; **arrêté désignant l'organisme de normalisation technique** — lève ou maintient Q5 | ch. 21 |
| indéterminée | Consolidation IETF du brouillon SCIM-agents (expiré le 19 avril 2026) ; état du brouillon CSA | ch. 2, 7 |
| indéterminée | **Statut de NIST IR 8547** — passage du projet au final, ou révision des dates | ch. 16, 17, 18 |
| indéterminée | Statut des conventions sémantiques OpenTelemetry pour les agents (expérimental → stable) | ch. 24 |
| **1er mai 2027** | Entrée en vigueur simultanée d'E-23 et de la ligne directrice IA de l'AMF — le « futur proche » de l'ouvrage devient du présent | ch. 19, 20 |
| 2030 / 2035 | Jalons de dépréciation et d'interdiction visés par IR 8547 | Partie V |

### 8.4 Neutralité fournisseur

Entra Agent ID, les passerelles MCP, les offres de maillage et les plateformes d'observabilité sont retenus comme **cas d'instanciation documentés par sources primaires**, jamais comme recommandations. Règles : (1) chaque capacité est attribuée à la documentation de l'éditeur, avec sa date et son statut — **GA documentée, annonce, feuille de route, préversion : quatre choses différentes** ; (2) aucune formulation de supériorité ; (3) les faits négatifs (absence de lien documenté avec un cadre réglementaire, dépréciations) sont exposés au même titre que les capacités ; (4) le tri **annonce / GA / production** est strict en Partie VII, où le vocabulaire de marché est le plus dense.

### 8.5 Dualité d'usage

La Partie IV documente des attaques. Elle le fait pour que des architectes les préviennent. **Traitement défensif exclusif** (R-12) : mécanique au niveau architectural, citation des identifiants et des incidents, aucune reproduction. Un chapitre qui ne saurait pas exposer un vecteur sans en donner la recette **ne l'expose pas**, et dit qu'il ne l'expose pas.

### 8.6 Trois degrés d'absence — vocabulaire imposé

Règle héritée du Vol. II — siège : `2 - OrchestrationAgentique/doc/PRDPlan.md` §4.4, et non son PRD —, reconduite sans amendement parce qu'elle y a coûté deux chapitres contradictoires avant d'être fixée.

1. **Fait négatif VÉRIFIÉ** — l'absence est établie par le **balayage documenté d'un texte**. Exemple hérité : H-04 (« agentique » / « agent » / « orchestration » = 0 sur le texte intégral d'E-23, EN et FR) ; H-08 (chaînes « FDX », « FAPI », « OAuth » cherchées dans le règlement et le communiqué).
2. **Fait négatif ÉTABLI** — le socle porte une **réserve explicite d'absence de lien dans son corpus**, sans balayage de texte. Exemple hérité : H-14 (« aucune source ne relie watsonx.governance à E-23 »).
3. **Absence de documentation** — le socle est **muet**. Formule imposée : « Le socle ne documente pas [X] : c'est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié. »

Le cas le plus fréquent de ce volume sera le troisième, et c'est normal : un ouvrage écrit sur un objet sous-documenté produit surtout des silences. **Un silence nommé est un résultat ; un silence habillé en constat est une faute.**

## 9. Corpus de sources

**Normes, spécifications et brouillons** : datatracker.ietf.org (RFC 6749, 7643 ; `draft-abbey-scim-agent-extension`, `draft-ietf-wimse-arch`, `draft-ietf-oauth-transaction-tokens`) ; w3.org (VC Data Model, DID Core, chartes des CG) ; identity.foundation (DIF) ; a2a-protocol.org ; modelcontextprotocol.io ; docs.agntcy.org ; spécification AP2 ; labs.cloudsecurityalliance.org ; opentelemetry.io (conventions sémantiques versionnées) ; nist.gov (IR 8547, FIPS 203/204, SP 800-207).

**Référentiels de sécurité** : MITRE ATLAS ; OWASP (Top 10 for Agentic Applications ; State of Agentic AI Security and Governance) ; NIST CAISI (AI Agent Standards) ; CVE/NVD pour les identifiants.

**Régulateurs et textes canadiens** : osfi-bsif.gc.ca (E-23) ; lautorite.qc.ca (ligne directrice IA) ; legisquebec.gouv.qc.ca et cai.gouv.qc.ca (Loi 25, art. 12.1) ; osc.ca et securities-administrators.ca (avis ACVM 11-348) ; gazette.gc.ca et canada.ca/Finances (cadre bancaire, arrêté de désignation).

**Éditeurs** : Microsoft Learn (Entra Agent ID) ; documentation AWS et Google Cloud ; documentation des passerelles MCP, des moteurs de politique et des plateformes d'observabilité agentique.

**Académique** : arXiv, avec la réserve de préprint systématique (H-12) ; corpus service mesh de la CNCF ; littérature IAM d'entreprise ; littérature MLOps/LLMOps transposée — **filiation à établir explicitement plutôt qu'à réinventer** (ch. 25).

**Corpus d'appui** : les trois ouvrages, **sous condition de dépôt** (§7.7). Littérature secondaire de cadrage : cadres conceptuels et vocabulaire, **jamais sources primaires de spécification**.

**Volumes du dépôt** : Vol. I (`Monographie.md`, `Synthese Monographie.md`, `Chapitres/Annexe B - Architecture de Solutions.md`) et Vol. II (`doc/PRD.md`, `monographie/**`) — cités **avec leur fichier** (§7.4.1) et **avec leur date de gel**.

**Corroboration secondaire admise** : cabinets juridiques canadiens ; presse spécialisée ; analyses d'éditeurs — **jamais comme source unique d'un fait central.**

## 10. Lacunes documentées et questions ouvertes

État au 18 juillet 2026. Ces lacunes sont **héritées ou constatées**, aucune n'est encore instruite — le volume n'a mené aucune passe. Chacune devient soit un encadré « état de la connaissance vérifiable », soit une question de recherche explicite (CA-06).

1. **Valeur probante des cartes d'agent signées** *(héritée — Vol. II Q3 ch. 21 et §10.9)*. Ni ancrage de confiance, ni révocation, ni gouvernance des clés au socle. → lot L-03, ch. 5.
2. **Mécanique et attestation des risques protocolaires** *(héritée — Vol. II Q2 ch. 21 et §10.8)*. Les risques sont **nommés** par le socle du Vol. II, jamais datés ni outillés d'une source dédiée ; **aucune attaque propre à A2A n'y figure** — absence de documentation, **non** fait négatif vérifié. → lot L-08, ch. 12.
3. **Désignation de l'organisme de normalisation technique** *(héritée — Vol. II Q5 ch. 21 et §10.1)*. Arrêté ministériel toujours à venir. → lot L-12, ch. 21.
4. **Contenu de la ligne directrice IA de l'AMF** *(héritée — Vol. II §10.4)*. Seules les dates sont au socle, et **l'une des deux est en divergence** (§7.5). `lautorite.qc.ca` renvoyait 403 aux outils du Vol. II. **La plus coûteuse des lacunes héritées** : le ch. 19 repose sur l'un des deux textes qui fixent l'échéance du 1er mai 2027. → lot L-12.
5. **Ce qui n'existe pas encore en matière de registre** *(héritée — Vol. II ch. 8 §8.4)*. Aucune norme ratifiée de registre d'agents, à quelque niveau que ce soit ; un produit en GA dont les flux étendent les RFC, une spécification à l'état de brouillon, une extension IETF expirée. → ch. 7.
6. **Délégation au-delà de deux sauts** *(héritée — Vol. I, `Synthese Monographie.md` §11.5)*. Aucun mécanisme documenté ne maintient une traçabilité opposable de bout en bout. **Exposée, non comblée** — c'est la fonction du ch. 10.
7. **Métrique d'horizon de tâche déléguée** *(héritée — Vol. I, `Synthese Monographie.md` §11.5 et `Monographie.md` §7.6.4)*. N'existe pas ; l'horizon mesuré porte sur un agent isolé. → ch. 26 §26.3.
8. **Composante ACP d'AGNTCY** *(héritée — Vol. II §10.7)*. Ni intitulé complet ni identité avec l'ACP protocolaire. → R-04, ch. 7, ch. 22.
9. **Caractérisation du *frame* opérationnel** *(héritée — Vol. II §10.10)*. Seul le frame normatif est caractérisé. Le PDF source est déposé au dépôt du Vol. II : **élévation possible en une passe de relecture ciblée** — mais c'est Q6 du Vol. II ch. 21, que ce volume n'instruit pas (§7.4.7). Signalée pour que le ch. 25 ne s'y adosse pas.
10. **Gouvernance d'AP2** *(divergence — §7.5)*. Deux positions inconciliables entre les livrables du dépôt, non arbitrées. → lot L-06, ch. 9.
11. **Corpus d'appui non déposé** *(constatée — §7.7)*. Trois ouvrages annoncés, zéro présent ; sept sections et une annexe bloquées. → lot L-15, décision J-1.
12. **`commun/faits-partages.md` inexistant** *(constatée — §7.4.9)*. Cité par trois documents — README racine, TOC du Vol. III (trois fois), TOC du Vol. IV —, absent du disque. **Décision prise en §7.5** : les divergences vivent au PRD ; les renvois sont à repointer.
13. **Statut réel de NIST IR 8547** *(constatée — H-17)*. Le Vol. I le donne comme *Initial Public Draft* avec réserve explicite, et l'ouvrage en fait son horloge. **Une horloge fondée sur un projet doit dire qu'elle l'est.** → lot L-11.
14. **Jetons de transaction** *(constatée — §7.2)*. Le ch. 2 §2.2 et le ch. 9 §9.1 du TOC les annoncent ; **le Vol. II ne les mentionne pas une seule fois** dans son chapitre d'identité. Rien n'est hérité **du Vol. II**. Le Vol. I, lui, porte l'objet et sa source primaire — `Monographie.md` §1.9.2.3 et sa bibliographie (`draft-ietf-oauth-transaction-tokens`, IETF OAuth WG) : matière [C] non encore inventoriée au socle hérité, à élever par lecture de la source primaire. → lot L-01.

**Exigence** : interdiction de combler une lacune par une source non vérifiée ou de moindre qualité. Une entrée [C] ne porte jamais un fait central sans élévation préalable. **Une lacune instruite et infructueuse se rédige au gabarit « passe conduite » ; une lacune non instruite se rédige au gabarit « aucune passe conduite »** — les confondre induit la fabrication d'une recherche qui n'a pas eu lieu (faute constatée au Vol. II).

## 11. Exigences de qualité et critères d'acceptation

- **CA-01 Traçabilité.** 100 % des affirmations factuelles centrales adossées à une entrée du socle (H-xx héritée ou F-xx propre) ou à une source primaire nouvelle de qualité équivalente. Les identifiants sont utilisables en notes. **Une affirmation tracée vers une entrée [C] n'est pas centrale, ou n'est pas rédigée.**
- **CA-02 Zéro proscrit.** Aucune des formulations R-01 à R-14 (§8.1) ne figure dans le texte. Contrôle outillé par les motifs de balayage (Annexe A §A.6), **complété par une inspection humaine** : la leçon du Vol. II est qu'une faute passe sous l'outil sans passer sous la règle.
- **CA-03 Attribution.** Toutes les métriques auto-déclarées, projections et études commandées attribuées conformément à §8.2, **à chaque occurrence, sans exception d'usage illustratif**.
- **CA-04 Datation.** Chaque pièce porte sa date de gel, consignée au registre. Les faits chauds (§8.3) sont revalidés avant publication, et le rapport de revalidation est daté de moins de trente jours au moment de publier.
- **CA-05 Fidélité des citations.** Toute citation présentée comme verbatim l'est. **Une reprise dans la substance se déclare comme telle** ; la revendication de verbatim est réservée aux reprises littérales, vérifiées contre le texte actuel de la source. *(Trois écarts de ce type ont été constatés au Vol. II ; le TOC de ce volume condense une formule du Vol. I sans nommer son siège — §7.4.5.)*
- **CA-06 Honnêteté des lacunes.** Les quatorze lacunes de §10 apparaissent toutes, en encadré ou en question de recherche. **Aucune silencieusement omise.** Le gabarit employé correspond à l'état réel de l'instruction (§10, exigence finale).
- **CA-07 Marquage des inférences.** Toute construction d'auteur porte le libellé **« Lecture de l'auteur »**, suivi de ce que le socle établit et de ce qu'il n'établit pas. Les ch. 8, 26 et le §27.4 le portent **à l'ouverture**, étant des constructions d'auteur en totalité.
- **CA-08 Bilinguisme terminologique.** Terme anglais entre parenthèses et en italique à la première occurrence ; citations verbatim en langue originale.
- **CA-09 Périmètre.** Le test d'appartenance (§5.1) est vérifié section par section en Parties VII et VIII. **Toute section qui ne répond ni « ce qu'elle vérifie de l'identité ou du mandat » ni « ce qu'elle en produit comme preuve » est coupée**, et sa coupe est consignée.
- **CA-10 Qualification des renvois.** Tout renvoi au Vol. I nomme son **fichier** (§7.4.1) ; tout renvoi à une question du Vol. II nomme son **chapitre** (§7.4.7) ; tout renvoi à un garde-fou nomme son **volume** (§8.1).
- **CA-11 Statut épistémique double.** Tout énoncé prospectif porte son tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF (H-33) ; tout fait porte son niveau [A]/[B]/[C]. **Les deux instruments ne se substituent pas l'un à l'autre** (§7.1).
- **CA-12 Traitement défensif.** Aucun élément de la Partie IV ne permet de dériver une attaque. Contrôle par relecture dédiée, distincte de la relecture de conformité.
- **CA-13 Traçabilité du blueprint.** Chaque composant, contrat et correspondance réglementaire de la Partie IX est tracé vers une entrée du socle ou marqué inférence d'auteur (Annexe B).
- **CA-14 Relecture adversariale.** Chaque pièce passe une relecture **par un relecteur distinct de son rédacteur**, chargée de réfuter et non de valider. **Une attestation de conformité n'est jamais rédigée depuis le souvenir de l'avoir vérifiée** : elle est portée par la constatation sur pièce.

## 12. Livrables et jalons

Aucun jalon n'est atteint. Le tableau est **prospectif**, et c'est sa différence principale avec celui du Vol. II.

| Jalon | Livrable | Critère de sortie |
|---|---|---|
| **J-0 (fait — 18 juill. 2026)** | [`TOC.md`](TOC.md) v0.4 — titre arrêté, découpage en 28 chapitres, 9 risques de cadrage | Table des matières commentée, statut *proposition* |
| **J-1 (à faire)** | **Révision du TOC** sur les neuf écarts de §7.4 ; **décision sur le corpus d'appui** (§7.7 — déposer ou retirer la filiation) ; repointage des renvois vers `commun/faits-partages.md` (§7.5) ; contrôle de couverture bijective §6.2 ↔ TOC ; assignation de chaque garde-fou et de chaque lacune à un chapitre porteur | TOC v0.5 ; PRD v0.2 ; **aucun garde-fou et aucune lacune non assignés** |
| **J-2 (à faire)** | **Exécution des lots bloquants L-03, L-08, L-15** | Q2 et Q3 instruites ou leur échec documenté ; premières entrées F-xx du socle propre ; corpus d'appui déposé **ou** sept sections et l'annexe E réécrites sans lui |
| **J-3 (à faire)** | Exécution des douze autres lots (L-01, L-02, L-04 à L-07, L-09 à L-14) | Socle propre constitué ; niveaux atteints ou écarts documentés ; PRD v1.0 |
| **J-4 (à faire)** | Rédaction des Parties I à VI (ch. 1 à 21) | Chaque chapitre tracé au socle, passé par la boucle qualité et la relecture adversariale ; registre de gel renseigné |
| **J-5 (à faire)** | Rédaction des Parties VII à IX (ch. 22 à 28), de l'avant-propos et des annexes A à E | Grille des cinq questions appliquée au maillage (§22.4) ; grille d'indicateurs du ch. 26 marquée construction d'auteur ; blueprint tracé (CA-13) ; matrice de l'annexe B livrée |
| **J-6 (à faire)** | Revalidation temporelle finale ; relecture CA-01 à CA-14 ; publication | Rapport de revalidation daté de moins de 30 jours ; grille CA intégralement conforme **et constatée sur pièce** ; PDF régénéré et versionné avec sa source |

**Définition de « terminé ».** Le volume est terminé quand : (1) les 28 chapitres et les 6 pièces d'appareil sont rédigés, relus adversarialement et tracés ; (2) la grille CA-01 à CA-14 est intégralement conforme, l'attestation portée par une constatation et non par un souvenir ; (3) la revalidation finale date de moins de trente jours ; (4) les lacunes de §10 apparaissent toutes, aucune silencieusement omise ; (5) les décomptes publiés — volumétrie, cardinal du socle, nombre de chapitres — sont **re-mesurés** et concordent entre le PRD, le TOC, le README du volume et le README du dépôt ; (6) le PDF est régénéré et poussé **avec** sa source.

⚠ **Point (5), et il n'est pas décoratif.** Le README du dépôt annonce déjà, pour ce volume, « 28 chapitres en 9 parties, ≈ 100 000 mots ». Le présent PRD porte **102 500**. Le chiffre vit donc à deux endroits au moins, et il en vivra à quatre. **Les mettre à jour ensemble, jamais l'un sans les autres.**

## 13. Risques du projet éditorial

| Risque | Impact | Parade |
|---|---|---|
| **Socle mince par construction** — le sujet est choisi *parce que* deux volumes le déclarent sous-documenté | Proportion [C] élevée ; affirmations centrales fragiles | Seuil de vote abaissé **et déclaré** (§A.4) ; règle cardinale §7.0 ; CA-01 refuse le fait central sur entrée [C] |
| **Fabrication du standard qu'on prétend décrire** (ch. 8, passeport) | Perte de crédibilité de l'ouvrage entier | R-01 ; marquage d'inférence à l'ouverture du chapitre (CA-07) ; relecture adversariale dédiée |
| **Péremption des Parties II-III** — brouillons et drafts vivent en mois | Faits périmés à la publication | Dates de gel par chapitre ; §8.3 ; revalidation J-6 |
| **Dilution** — trois objets dans un ouvrage | Perte de la ligne directrice | Test d'appartenance §5.1, opposable, vérifié par CA-09 |
| **Vocabulaire de marché** — « entreprise agentique », « maillage d'agents », « AgentOps » | Recension publicitaire ; périmètre flottant | R-03 ; définitions d'auteur à siège unique ; tri annonce/GA/production ; statut au glossaire |
| **Corpus d'appui non déposé** | Sept sections et une annexe sans fondement | L-15 bloquant ; décision J-1 ; R-10 |
| **Dualité d'usage** (Partie IV) | Ouvrage exploitable offensivement | R-12 ; CA-12 en relecture distincte |
| **Renvois cassés dans un ouvrage dont la thèse est la traçabilité** | Contre-argument vivant | §7.4 ; CA-10 ; contrôle J-1 |
| **Sources primaires inaccessibles** (403, rendu JS, paywall) | Lacunes non comblables | Documenter l'échec de la passe plutôt que de le combler ; gabarit « passe conduite et infructueuse » |
| **Deux gels hérités et deux systèmes épistémiques** | Confusion [B]/PROJETÉ ; faits périmés importés sans le savoir | §7.1 ; règle de péremption de l'héritage ; CA-11 |

---

## Annexe A — Méthodologie et protocole de constitution du socle

### A.1 Principe

Le volume ne dispose d'aucun socle propre. Sa première tâche n'est pas d'écrire mais de **constituer** — et le PRD est le document qui l'y oblige. Le protocole reconduit celui du Vol. II, augmenté du tri prospectif du Vol. I et de deux amendements rendus nécessaires par la minceur du socle (§A.4, §A.5).

### A.2 Les niveaux de preuve

Trois niveaux, dans un ordre strict, repris sans amendement du Vol. II :

- **[A]** — l'affirmation a passé le **vote adversarial à 3-0** : trois juges ont cherché à la réfuter, aucun n'y est parvenu.
- **[B]** — la **source primaire a été lue et extraite avec citation**, ou consultée directement, **sans vote adversarial**.
- **[C]** — **repérage documentaire** : la source est identifiée, son contenu n'a pas été extrait. **Une entrée [C] ne porte jamais un fait central.**

L'ordre est contre-intuitif et il commande le reste : une lecture directe d'un texte officiel vaut **moins** qu'un vote 3-0, non que le texte soit douteux, mais parce que la lecture n'a été relue par personne. **Le niveau ne mesure pas la qualité de la source ; il mesure ce que l'affirmation a subi.**

### A.3 Le tri prospectif

Superposé au précédent, non substitué (CA-11). **PROGRAMMÉ** : engagement daté réel, portant sa source et sa date. **PROJETÉ** : prévision d'analyste ou d'institution, exigeant source nominative, millésime et périmètre. **SPÉCULATIF** : pari de recherche, scénario, discontinuité. Un préprint portant un programme de recherche relève par construction du spéculatif ; une charte de groupe de travail fait basculer un objet vers le programmé. **Ne jamais présenter du PROJETÉ ni du SPÉCULATIF comme acquis.**

### A.4 Seuil de vote — abaissé et déclaré

Le Vol. II a soumis **75 affirmations sur 384** au vote à trois juges, sous plafond budgétaire ; les 309 autres sont entrées au socle en [B] ou [C]. Il l'a déclaré, et c'est ce qui rendait son socle lisible.

Ce volume déclare son seuil **avant** de commencer, et il le fixe autrement : **le vote adversarial est réservé aux affirmations centrales des trois lots bloquants** (L-03, L-08, L-15) et à toute affirmation qui porterait à elle seule la thèse d'un chapitre. Partout ailleurs, le plancher est **[B] par extraction citée**.

**Motif, et il faut l'écrire** : sur un objet sous-documenté, le vote à trois juges consomme son budget à faire réfuter des affirmations que personne ne conteste, faute de littérature contradictoire. La ressource est mieux employée à **lire des sources primaires que nul n'a extraites** qu'à faire voter trois fois sur une seule. **Conséquence assumée : le socle du Vol. III comptera proportionnellement moins d'entrées [A] que celui du Vol. II.** Un socle qui l'annonce vaut mieux qu'un socle qui laisse le lecteur le découvrir.

### A.5 Élévation de l'héritage

Une entrée héritée du Vol. I (§7.3) entre en [C] et **nomme la source primaire que le Vol. I cite**. Son élévation en [B] est donc une lecture, non une recherche. **Elle est obligatoire avant que l'entrée ne porte un fait central**, et elle se fait à la source primaire — jamais en recopiant le Vol. I, qui est un ouvrage second sur ce point.

Une entrée héritée du Vol. II conserve son niveau, sauf si elle figure aux faits chauds (§8.3), auquel cas elle est revalidée à la source avant emploi.

### A.6 Motifs de balayage — support de CA-02

À passer sur chaque pièce avant tout commit. Un motif qui ressort n'est pas une faute : c'est un point à inspecter contre l'attendu. **La liste est à compléter à la clôture de J-1**, quand les garde-fous seront assignés par chapitre.

```
R-01    passeport d'agent
R-02    garanti|prouve l'identité|atteste l'identité|sécuris
R-03    agent mesh|maillage d'agents|AgentOps|entreprise agentique
R-04    \bACP\b|control plane|plan de contrôle|AgentMesh
R-05    \bKYA\b|Know Your Agent
R-06    exigé par E-23|E-23 (impose|exige)|exigenc\w*|fiche de modèle|model card
R-07    conforme à E-23|conformité.*E-23|B-13|conform\w+.*(AMF|ligne directrice)
R-08    aucun incident|pas d'incident
R-09    Community Group|\bCG\b|W3C.*normalis
R-10    Arsanjani|Bustos|Nagasubramanian|Ranjan|Chembachere|Lobo
R-11    2030|2035|post-quantique|IR 8547
R-13    autonomie graduée|niveaux 0 à 5|L0|L1|L2|L3
R-14    le socle ne documente|n'existe pas|aucun
CA-03   [0-9]+ ?%|selon|déclare
CA-11   PROGRAMMÉ|PROJETÉ|SPÉCULATIF|\[A\]|\[B\]|\[C\]
```

⚠ **R-12 n'a pas de motif, et son absence est déclarée plutôt que subie.** La dualité d'usage ne se détecte pas par une chaîne de caractères : une recette d'exploitation s'écrit en prose ordinaire. **R-12 est contrôlé par CA-12 seul** — une relecture dédiée, distincte de la relecture de conformité, chargée de la seule question « un lecteur peut-il dériver une attaque de ce texte ? ». *Motif de cette note : au Vol. II, l'instrument censé contrôler les garde-fous en omettait trois, dont un en entier, et l'omission n'a été trouvée qu'en relecture finale. Un garde-fou sans motif est admissible ; un garde-fou absent de la liste sans explication ne l'est pas.*

⚠ **Le motif de R-06 attrape « exigence » sans le sigle sur la même ligne** — correction directe d'une faute qui, au Vol. II, était « passée sous l'outil, pas sous la règle ». ⚠ **Aucun motif ne remplace l'inspection.** Le balayage est un filet, pas un verdict.

### A.7 Boucle qualité par pièce

1. Vérifier que le **lot d'instruction** de la pièce est clos (§7.6). Sinon : ne pas rédiger.
2. Rédiger contre le socle, en traçant chaque affirmation centrale.
3. Passer les motifs §A.6, inspecter chaque occurrence.
4. **Relecture adversariale par un relecteur distinct**, chargée de réfuter (CA-14).
5. Appliquer les correctifs ; **amender le socle d'abord si la faute y siège**, jamais la pièce seule.
6. Renseigner la date de gel au registre ; consigner la volumétrie réelle au regard de la cible, **l'écart documenté et non corrigé**.

⚠ **Point 5, et c'est la leçon la plus chère du Vol. II** : deux de ses défauts de chapitres avaient leur racine au socle, et les corriger dans les chapitres aurait déplacé la faute sans la traiter.

### A.8 En-tête de pièce

Chaque pièce porte, avant son premier séparateur, un tableau à cinq champs — **Statut**, **Date de gel de l'information**, **Socle mobilisé** (H-xx et F-xx), **Garde-fous à surveiller** (R-xx), **Volumétrie cible** — suivi de la thèse du chapitre citée depuis le TOC. Format repris du Vol. II, où il a fait ses preuves sur 29 pièces.

---

## Annexe B — Spécification du blueprint (Partie IX)

Spécification de l'architecture de référence que les ch. 27 et 28 doivent détailler. Chaque composant est tracé au socle ; chaque correspondance réglementaire porte son statut **documenté** ou **inférence d'auteur** (CA-13). Contexte cible : institution financière canadienne réglementée, en continuité avec le cas fil rouge du Vol. I (H-32).

### B.1 Principes directeurs

1. **Rien n'entre au maillage sans passeport.** L'admission est un acte de vérification, pas de déclaration. *(ch. 8 ; H-01, H-02, H-03.)*
2. **Une identité vérifiée à l'admission ne dit rien du comportement en exploitation.** La vérification est continue ou elle n'est pas. *(H-25 : « la signature au moment de la publication n'empêche pas une mutation ultérieure ».)*
3. **La frontière de confiance est chaque arête**, non le périmètre. Le maillage est la conséquence architecturale de cette prémisse, pas une mode. *(H-24.)*
4. **Une approbation humaine qui ne s'inscrit pas dans la chaîne de mandat n'est pas un contrôle.** *(ch. 9 §9.4 ; H-15/PC3.)*
5. **La trace revient au cadre, jamais à l'agent.** *(H-12 : la journalisation confiée aux agents « n'est généralement pas recommandée » — **recommandation graduée d'un préprint non révisé, non interdiction** ; H-15/PC2 — **thèse du Vol. II, à attribuer**. La forme absolue du principe est une décision d'architecture du présent ouvrage.)*
6. **L'adaptation et l'évolution empruntent deux chemins techniques distincts**, et deux régimes d'autorisation. Sans quoi le moment où une exception devient une règle est indétectable dans les journaux. *(H-11 ; H-15/PC4 — **thèse du Vol. II, à attribuer**, non fait de socle.)*
7. **Le mécanisme de signature est un contrat versionné, pas une hypothèse câblée.** Crypto-agilité = application de l'invariant du Vol. I à la couche cryptographique. *(ch. 17 ; H-17, H-27.)*
8. **Le confinement local borne l'impact ; il ne prévient pas la compromission.** Et il entre en tension avec l'exigence d'explicabilité — **l'arbitrage se documente, il ne se déclare pas résolu**. *(H-11 ; H-15/PC5.)*

### B.2 Les trois étages et leurs contrats mutuels

| Étage | Fonctions | Socle | Contrat rendu à l'étage suivant |
|---|---|---|---|
| **E1 — La fabrique d'identité** (émettre) | Émission, registre, vérification, révocation ; chaîne de mandat ; admission d'agent tiers (KYA) | H-01, H-02, H-03, H-18, H-19 ; Parties II-III | Un **passeport vérifiable** et une **chaîne de mandat interrogeable à l'instant t** |
| **E2 — Le maillage** (appliquer) | PEP/PDP par arête ; passerelles ; politiques ; confinement | H-09, H-10, H-12, H-24, H-30 ; Partie VII | Une **décision d'autorisation par arête**, et sa **trace corrélée au mandat** |
| **E3 — L'AgentOps** (exploiter) | Observabilité, évaluation continue, dérive, incident, cycle de vie | H-11, H-14, H-16, H-23, H-27 ; Partie VIII | Un **signal de revalidation** qui remonte à E1 — révocation, re-cotation, retrait |

⚠ **La boucle E3 → E1 est la thèse d'architecture du volume.** Sans elle, le passeport certifie un comportement passé et jamais le comportement courant ; les trois étages ne sont pas une pile mais un cycle. C'est la réalisation opérationnelle du quatrième terme de l'invariant (H-27).

### B.3 Correspondance réglementaire

| Exigence | Réponse d'architecture | Socle | Statut du lien |
|---|---|---|---|
| E-23 — inventaire d'entreprise, cotation, cycle de vie, documentation, surveillance continue | E1 : registre comme inventaire ; E3 : surveillance et évaluation continues | H-04, H-14 | **Inférence d'auteur.** ⚠ Écrire « **attendu par** E-23 » (R-06) ; **fait négatif établi** pour watsonx.governance (§8.6, degré 2), **absence de documentation** pour les autres plateformes (degré 3) — ne pas généraliser |
| Ligne directrice IA de l'AMF | E1 + E3, paliers de risque | H-05 | **Inférence d'auteur.** ⚠ Le contenu du texte n'est pas au socle (lacune Vol. II §10.4 ; PRD §10, lacune 4) : ne rien en dériver |
| Loi 25, art. 12.1 | E1 : le point d'arrêt humain comme acte de délégation daté et signé ; E3 : trace d'instance produite par le cadre | H-06, H-15 | **Inférence d'auteur** ; nuance Fasken [C] à porter ; **Q4 prolongée, non tranchée** |
| ACVM 11-348 — autonomie et adaptativité après déploiement | E3 : détection de la dérive d'autonomie ; séparation adaptation/évolution | H-07, H-11 | **Inférence d'auteur** |
| Cadre bancaire — standard technique | E2 : passerelles conformes au standard **à venir** | H-08 | **Attente réglementaire — ne rien anticiper** (R-5 du Vol. II reconduit) |
| Jalons post-quantiques | E1 : crypto-agilité du mécanisme de signature | H-17 | **Inférence d'auteur** ; ⚠ un jalon NIST n'est pas une obligation légale (R-11) |

### B.4 Parcours à jouer contre l'architecture (ch. 28)

1. **Naissance** — enregistrement, émission du passeport, admission au maillage.
2. **Vie** — délégations, vérifications par arête, traces d'exploitation, évaluations continues, renouvellements, migration post-quantique.
3. **Mort** — révocation, **cascade dans la chaîne de mandat** (problème ouvert, ch. 14 §14.3), retrait du maillage, archivage probatoire.

Chaque transition est jouée contre les trois étages, au grain du cas fil rouge (H-32). **La transition la plus instructive est la troisième** : c'est là que le volume expose que la révocation est le mécanisme le moins spécifié de la pile.

### B.5 Lacunes propres au blueprint

1. La révocation en cascade n'a **aucun mécanisme documenté** — le blueprint expose le problème, il ne le résout pas. 2. La corrélation trace ↔ chaîne de mandat est le **chaînon manquant** que l'ouvrage documente sans le combler. 3. Le modèle de maturité (§27.4) est **bloqué** tant que L-15 n'est pas clos (§7.7). 4. Toute correspondance réglementaire est une inférence d'auteur, jamais une revendication. 5. **Le blueprint est daté** — revalidation obligatoire (§8.3).

---

## Annexe C — La grille des cinq questions

La grille du ch. 4 est le dispositif structurant de l'ouvrage — ce que la taxonomie OO1–OO4 était au Vol. II, à une différence près qui doit être posée d'emblée : **OO1–OO4 venait d'une source ; la grille est une construction d'auteur.** Elle est donc spécifiée ici, dans le document qui fait autorité, et non dérivée d'un socle qui ne la porte pas.

### C.1 Les cinq questions

Ce sont les questions que l'entreprise doit pouvoir poser à chacun de ses agents.

| # | Question | Ce qu'un mécanisme doit produire pour y répondre |
|---|---|---|
| **Q-A** | **Qui es-tu ?** | Un identifiant stable, vérifiable, résistant à l'usurpation, et **révocable** |
| **Q-B** | **Qui t'a créé ?** | Une chaîne de provenance jusqu'à une autorité d'émission, avec son ancrage de confiance |
| **Q-C** | **Pour qui agis-tu ?** | Une chaîne de mandat interrogeable **à l'instant t**, et non seulement à l'admission |
| **Q-D** | **Que peux-tu faire ?** | Des bornes de privilège explicites, opposables au point d'application |
| **Q-E** | **Qui en répond ?** | Une imputabilité traçable jusqu'à une personne ou une entité juridique |

### C.2 Règles d'emploi

1. **La grille s'applique par mécanisme, pas par produit.** Un même produit peut répondre à Q-A et laisser Q-C sans réponse.
2. **Une réponse partielle est une réponse partielle.** Trois verdicts seulement : *répond*, *répond partiellement — et on dit à quoi*, *ne répond pas*. Aucun quatrième verdict de complaisance.
3. **La thèse du ch. 4 est falsifiable, et c'est voulu** : « aucun mécanisme de 2026 ne répond aux cinq ». Un mécanisme qui répondrait aux cinq la réfute — **et la réfutation doit être écrite si elle survient**, pas contournée.
4. **Le ch. 8 §8.4 est le seul endroit où les cinq reçoivent une réponse** — et le passeport y étant une construction d'auteur, la réponse est « sur le papier ». R-01 s'applique intégralement à ce paragraphe.
5. **La grille est appliquée en Parties II (§5.4, §6.4, §8.4), IV (§12.2), VI (§19.1) et VII (§22.4)**, et sert de colonne à l'annexe B de l'ouvrage (matrice des mécanismes). **La Partie III ne porte aucun verdict par la grille** : elle *instruit* la question Q-C — pour qui agis-tu ? — au lieu de l'appliquer mécanisme par mécanisme, et le ch. 9 le déclare à son ouverture. Toute autre partie qui ne l'appliquerait pas s'en explique de même.

### C.3 Croisement avec la maturité

Le §4.4 croise la grille avec un spectre de maturité : plus l'autonomie consentie monte, plus une question sans réponse coûte cher — ce qui ordonne les exigences d'identité **par palier** plutôt qu'en absolu.

⚠ **Ce croisement est doublement contraint.** (a) Il mobilise le corpus d'appui : **bloqué tant que L-15 n'est pas clos** (§7.7). (b) La correspondance maturité ↔ exigences est une **construction d'auteur**, à marquer comme telle (CA-07). Si L-15 échoue, le croisement se refait sur l'autonomie graduée du Vol. I (H-31, échelle nommée — R-13), et le §4.4 le déclare.
