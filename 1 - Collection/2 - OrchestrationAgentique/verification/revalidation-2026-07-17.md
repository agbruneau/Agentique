# Rapport de revalidation — 17 juillet 2026

| Champ | Valeur |
|---|---|
| Jalon | PRDPlan P4.1 (revalidation temporelle **finale** avant publication) |
| Périmètre | Faits « chauds » de PRD §8.3 + points de revalidation ouverts de `monographie/99-registre-gel.md` |
| Méthode | Consultation directe des sources primaires (WebFetch/WebSearch bornée aux domaines officiels), une passe, sans vote adversarial |
| Passe précédente | `verification/revalidation-2026-07-16.md` (P0.1/P0.2, PRD v1.2.1 → v1.3) |
| PRD amendé | **Non** — aucun amendement matériel requis (voir §« Amendements requis au socle ») |

**Contexte** : un jour s'est écoulé depuis P0.1. La stabilité générale constatée ci-dessous est le résultat attendu ; aucune évolution n'a été recherchée pour justifier la passe.

---

## 1. Faits chauds — verdicts

### F-01 — MCP : révision de spécification

**Statut : INCHANGÉ (révision courante) — RC du 28 juillet 2026 CONFIRMÉE à l'échéance**

| Élément | Constat |
|---|---|
| Révision publiée courante | **2025-11-25** — toujours la dernière publiée, confirmée aux deux sources |
| RC 2026-07-28 | Existe, verrouillée, **finalisation toujours annoncée au 28 juillet 2026** |

Sources primaires consultées le 17 juillet 2026 :

1. `https://modelcontextprotocol.io/specification/latest` — la page de spécification pointe vers le schéma `schema/2025-11-25/schema.ts` et l'ensemble des cartes de navigation (Architecture, Base Protocol, Server Features, Client Features) renvoient à `/specification/2025-11-25/`. Aucune révision postérieure publiée. À noter : la page décrit toujours le protocole comme reposant sur des « Stateful connections » — cohérent avec le fait que la refonte sans état n'est pas encore en vigueur.
2. `https://github.com/modelcontextprotocol/modelcontextprotocol/releases` — ordre des publications : **MCP 2026-07-28 RC** (préversion, 29 mai) ; **2025-11-25** (25 nov., « stable release », dernière version finale) ; 2025-11-25-RC ; 2025-06-18 ; 2025-03-26 ; 2024-11-05-final. Mention explicite : « this specification is not final. Changes may be introduced between the RC and the final release ».
3. `https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/` (billet du 21 mai 2026) — citations verbatim :
   - « the final specification ships on **July 28, 2026** » ;
   - « The release candidate is locked as of May 21, 2026 » ;
   - « The headline change is that MCP is now stateless at the protocol layer » ;
   - « The `Mcp-Session-Id` header and the protocol-level session that came with it are also removed ».
4. `https://blog.modelcontextprotocol.io/` — billets postérieurs confirmant la trajectoire, sans report annoncé : « Enterprise-Managed Authorization: Zero-touch OAuth for MCP » (18 juin 2026) et « Beta SDKs for the 2026-07-28 MCP Spec Release Candidate Are Here » (29 juin 2026, SDK bêta Python/TypeScript/Go/C#).

**Observation** : les deux éléments du socle sont validés — la révision 2025-11-25 reste la dernière publiée (le texte des chapitres 1, 2 et 7 demeure exact à leur date de gel), et la RC du 28 juillet est confirmée, ni avancée ni reportée. Aucun signal de glissement au 17 juillet 2026. Le point de revalidation post-publication du registre de gel est donc **maintenu, avec une probabilité élevée de matérialisation à onze jours**.

---

### F-02 — A2A : version courante

**Statut : INCHANGÉ**

Source primaire consultée le 17 juillet 2026 : `https://github.com/a2aproject/A2A/releases` — **v1.0.1 (28 mai 2026) demeure la dernière publication**. Contenu : correctifs mineurs (préférence pour `application/a2a+json` dans le binding HTTP, corrections de transcodage, correction des valeurs `TaskStatus` dans la spécification). Aucune version postérieure.

Le socle (ligne v1.0, tag v1.0.1 au 28 mai 2026) est exact.

---

### F-24 — Projet de loi C-36 (*Protecting Privacy and Consumer Data Act*)

**Statut : INCHANGÉ — avec une précision de formulation recommandée (non bloquante)**

Source primaire consultée le 17 juillet 2026 : `https://www.parl.ca/legisinfo/en/bill/45-1/c-36` (LEGISinfo).

| Étape | Statut LEGISinfo | Date |
|---|---|---|
| 1re lecture | **Complétée** | 15 juin 2026 |
| 2e lecture | Aucune activité | — |
| Étude en comité | Non atteinte | — |
| Rapport / 3e lecture / Sénat | Non atteintes | — |

Le statut affiché est « **At second reading in the House of Commons** », mais la **seule étape législative complétée demeure la première lecture** du 15 juin 2026 ; LEGISinfo n'enregistre aucune activité à l'étape de la deuxième lecture.

**Précision** : la formulation du socle (« en 2e lecture au 16 juill. 2026 ») est **exacte au sens de l'étape atteinte** — le projet de loi est bien *à* l'étape de la deuxième lecture. Elle pourrait toutefois se lire, pour un lecteur non familier de la procédure parlementaire, comme si la deuxième lecture avait été *franchie*. Ce n'est pas le cas : aucun débat ni vote de deuxième lecture n'est consigné. Le fait sous-jacent est inchangé depuis P0.1 ; il ne s'agit pas d'une correction factuelle mais d'un durcissement de formulation, laissé à l'appréciation de l'auteur (voir §« Amendements requis au socle », point optionnel).

---

### F-29 — Real-Time Rail (RTR) de Paiements Canada

**Statut : INCHANGÉ — T4 2026 demeure une cible conditionnelle**

Sources primaires consultées le 17 juillet 2026 :

1. `https://www.payments.ca/systems-services/payment-systems/real-time-rail-payment-system` — citation verbatim : « The Real-Time Rail, **launching in Q4 of 2026**, is Canada's new real-time exchange and clearing and settlement payment system that supports instant, data-rich payments. » Aucune date précise de lancement, aucun report annoncé.
2. `https://www.payments.ca/speech-opening-remarks-2026-payments-canada-summit` (allocution du 5 mai 2026, Sommet Paiements Canada) — citations verbatim :
   - « **Launch is targeted for late Q4 — driven by readiness, not by haste**, because the safety and soundness of this system is non-negotiable » ;
   - « User-acceptance testing is complete. Integrated performance testing is underway » (Susan Hawkins).
3. `https://www.payments.ca/canadas-real-time-rail-quarterly-update-jude-pinto-2026-q1` (mise à jour trimestrielle du 11 févr. 2026) — antérieure ; confirme la séquence de tests (UAT entamée fin 2025, poursuivie en 2026), sans engagement de date.

**Observation** : le lancement reste **une cible, pas une date ferme**, et la caractérisation conditionnelle du socle (« cible T4 2026, conditionnelle au succès des tests, avec historique de reports ») est confirmée mot pour mot par la source primaire (« driven by readiness, not by haste »). Progression notée depuis P0.1 sans changer le statut : l'UAT est désormais **complétée** et les tests de performance intégrés sont **en cours** — cohérent avec l'« industry solution assurance testing » relevé le 16 juillet. Le By-law No. 10 (entrée en vigueur le 24 août 2026) n'a fait l'objet d'aucune modification.

---

### F-34 / F-35 — Cadre bancaire axé sur le consommateur

**Statut : INCHANGÉ — le fait négatif tient : AUCUN organisme de normalisation technique désigné (garde-fou R-5 maintenu)**

Sources primaires consultées le 17 juillet 2026 :

1. `https://www.bankofcanada.ca/regulatory-oversight/consumer-driven-banking/` — **aucun organisme de normalisation technique n'est nommé**, aucune désignation ministérielle n'est mentionnée. La page renvoie aux « Proposed regulations » publiées à la *Gazette du Canada* le 27 juin 2026, sans autre échéance.
2. `https://gazette.gc.ca/rp-pr/p1/2026/2026-06-27/html/reg3-eng.html` (Gazette du Canada, Partie I, vol. 160, no 26 — *Consumer-Driven Banking Regulations*) — citations verbatim :
   - « The technical standards body **will be designated** according to the factors and processes set out in the Act. The designation factors include being meaningfully Canadian; having a governance structure that is fair, open, and accessible, with independent decision making and an ability to exercise powers and act in a manner consistent with the objectives of the Act; and ensuring the standard itself is safe, secure, and interoperable » ;
   - le texte autorise « the Minister of Finance to designate and revoke the technical standards body, **through a Ministerial Order** » — **la décision de désignation n'est pas prise** à la date de publication ;
   - période de commentaires : « the proposed Regulations are subject to an **extended prepublication period of 60 days** to provide stakeholders with adequate time to provide meaningful feedback ».

**Observation critique (R-5)** : à la lecture directe des deux sources primaires, **aucun arrêté ministériel de désignation n'a été pris** entre le 16 et le 17 juillet 2026. Ni la Gazette ni la Banque du Canada ne nomment FDX, FAPI ou OAuth. Le fait négatif du socle — **FDX n'est pas le standard retenu du cadre bancaire canadien** — reste vérifié et le garde-fou R-5 demeure pleinement applicable à tout le texte de la monographie. La question ouverte PRD §10.1 n'est pas résolue.

**Réserve de traçabilité honnête** : la Gazette énonce un délai de **60 jours** sans inscrire de date d'échéance explicite. La date du **26 août 2026** portée au socle est l'application arithmétique de ce délai à la date de prépublication (27 juin + 60 j) et avait été confirmée par le communiqué de Finances Canada lors de la passe P0.1. Ce communiqué n'a **pas pu être relu** ce jour (voir §3). La date reste cohérente et non contredite ; elle n'est pas re-confirmée par lecture directe dans cette passe.

---

### F-25 — Ligne directrice de l'AMF sur l'utilisation de l'intelligence artificielle

**Statut : INCHANGÉ — revalidé partiellement (lecture directe des pages bloquée)**

| Élément | Constat |
|---|---|
| Statut | Finale (ligne directrice publiée, non « en projet ») |
| Entrée en vigueur | **1er mai 2027** |

Vérification tentée le 17 juillet 2026 sur `https://lautorite.qc.ca/en/professionals/financial-institutions/artificial-intelligence`, `https://lautorite.qc.ca/grand-public/publications/professionnels/lignes-directrices-institutions-financieres`, `https://lautorite.qc.ca/en/professionals/insurers/guidelines/use-of-models/guideline-for-the-use-of-artificial-intelligence` et sur le PDF officiel `https://lautorite.qc.ca/fileadmin/lautorite/reglementation/lignes-directrices-assurance/LD-utilisation-intelligence-artificielle_fr.pdf` — **HTTP 403 Forbidden sur l'ensemble du domaine `lautorite.qc.ca`**, pages HTML comme PDF. Le domaine bloque les outils automatisés.

**Ce qui a pu être établi** : une recherche bornée au seul domaine primaire `lautorite.qc.ca` retourne, de façon convergente, (a) le PDF officiel de la ligne directrice intitulé « **00 Mars 2026** — LIGNE DIRECTRICE SUR L'UTILISATION DE L'INTELLIGENCE ARTIFICIELLE » (hébergé sous `/reglementation/lignes-directrices-assurance/`, soit l'emplacement des lignes directrices **en vigueur**, et non sous `/consultations/`), et (b) l'énoncé selon lequel la ligne directrice **prend effet le 1er mai 2027**, après une consultation publique tenue du 9 octobre au 19 décembre 2025, et remplacera la ligne directrice sur la gestion des risques liés à l'impartition, abrogée à cette même date.

**Portée exacte de ce constat** : il s'agit de l'index de recherche du domaine primaire, **pas d'une lecture directe de la page**. Conformément à la règle du projet, la mention est signalée pour ce qu'elle est. Les deux attributs portés au socle (caractère final ; entrée en vigueur au 1er mai 2027) sont **corroborés et non contredits** ; la date de publication précise du **30 mars 2026** n'est pas re-confirmée par lecture directe dans cette passe — le titre du PDF ne porte que « Mars 2026 ». Le fait reste au statut du socle, revalidé partiellement. Il avait été établi lors des passes antérieures et n'est pas contredit ; aucune action n'est requise.

---

### F-09 — Ligne directrice E-23 du BSIF (gestion du risque de modèle)

**Statut : INCHANGÉ**

Source primaire consultée le 17 juillet 2026 : `https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027` — **date d'entrée en vigueur : 1er mai 2027**. **Aucun avis de report, d'amendement ou de modification** de cette date n'est publié.

Éléments de contexte confirmés au même domaine (`osfi-bsif.gc.ca`, lettre et documents d'accompagnement de la ligne directrice) : publication officielle le 11 septembre 2025 ; entrée en vigueur en mai 2027 au terme d'une période de transition de 18 mois ; portée étendue à **tous les modèles de toutes les IFF** ; ajout de précisions visant le risque de modèle lié à l'IA/AA. Assujettis : banques, succursales de banques étrangères, sociétés d'assurance vie, sociétés d'assurance multirisque, sociétés de fiducie et de prêt.

Le socle est exact. Le point de revalidation du registre de gel (discours de « futur proche » aux chapitres 9, 11 et 20) reste ouvert jusqu'au 1er mai 2027.

---

### F-41 — Acquisition de Confluent par IBM

**Statut : INCHANGÉ (fait résolu) — vérification de courtoisie**

Source primaire consultée le 17 juillet 2026 : `https://newsroom.ibm.com/2026-03-17-ibm-completes-acquisition-of-confluent,-making-real-time-data-the-engine-of-enterprise-ai-and-agents` — « **IBM Completes Acquisition of Confluent, Making Real Time Data the Engine of Enterprise AI and Agents** ».

Éléments confirmés : clôture le **17 mars 2026** (acquisition de toutes les actions ordinaires émises et en circulation) ; **31 $ US par action**, valeur d'entreprise de **11 G$ US** ; annonce initiale le 8 décembre 2025. Intégrations de premier jour annoncées : IBM watsonx.data, IBM MQ, IBM webMethods Hybrid Integration, IBM Z. Confluent décrit comme servant plus de 6 500 entreprises, dont 40 % du Fortune 500 (**métrique auto-déclarée par IBM/Confluent — à attribuer à chaque occurrence, PRD §8.2**).

Le fait est résolu et sort de la liste des faits chauds, conformément à PRD §8.3.

---

## 2. Tableau de synthèse

| Fait | Objet | Statut au 17 juill. 2026 | Source primaire lue directement |
|---|---|---|---|
| **F-01** | MCP — révision de spécification | **Inchangé** (2025-11-25 dernière publiée) ; RC 2026-07-28 **confirmée à l'échéance** | Oui (spec site, GitHub releases, blog officiel) |
| **F-02** | A2A — version courante | **Inchangé** (v1.0 ; tag v1.0.1, 28 mai 2026) | Oui (GitHub releases) |
| **F-24** | Projet de loi C-36 | **Inchangé** (à l'étape de la 2e lecture ; seule la 1re lecture est complétée) | Oui (LEGISinfo) |
| **F-25** | Ligne directrice IA de l'AMF | **Inchangé — revalidé partiellement** (domaine 403) | Non — index du domaine primaire seulement |
| **F-29** | RTR — cible de lancement | **Inchangé** (cible T4 2026, conditionnelle à la readiness) | Oui (payments.ca, page RTR + allocution du Sommet) |
| **F-34/F-35** | Cadre bancaire — désignation | **Inchangé** — **aucune désignation ; R-5 maintenu** | Oui (Gazette Partie I ; Banque du Canada) |
| **F-09** | E-23 du BSIF | **Inchangé** (1er mai 2027 ; aucun report) | Oui (osfi-bsif.gc.ca) |
| **F-41** | Acquisition Confluent | **Inchangé** (résolu — clôturée le 17 mars 2026) | Oui (newsroom.ibm.com) |

**Six faits sur huit** revalidés par lecture directe d'une source primaire. **Un** (F-25) revalidé partiellement, blocage technique documenté. **Un** (F-34/F-35) revalidé par lecture directe sur le fond, avec une réserve de traçabilité sur la seule date du 26 août.

---

## 3. Sources inaccessibles aux outils — non-vérifications documentées

Conformément à la règle du projet, chaque blocage est déclaré plutôt que contourné par une affirmation non fondée.

| Source | URL | Blocage | Conséquence |
|---|---|---|---|
| AMF — pages et PDF de la ligne directrice IA | `lautorite.qc.ca` (4 URL distinctes, dont le PDF officiel) | **HTTP 403** sur tout le domaine | F-25 revalidé partiellement (index du domaine primaire), non par lecture directe |
| Finances Canada — communiqué de prépublication | `canada.ca/en/department-finance/news/2026/06/...` | **HTTP 403** | Date du 26 août 2026 non re-confirmée par lecture directe ; la Gazette confirme le délai de 60 jours dont elle découle |
| Finances Canada — page de mise en œuvre du cadre bancaire | `canada.ca/.../open-banking-implementation.html` | **HTTP 403** | Compensé : la Banque du Canada (source primaire du régulateur désigné) a été lue directement et confirme l'absence de désignation |
| Paiements Canada — index des nouvelles | `payments.ca/news` | **HTTP 404** (URL inexistante) | Compensé : page RTR et allocution du Sommet 2026 lues directement |

Aucune de ces non-vérifications n'affecte un fait central de la monographie : dans chaque cas, soit une source primaire équivalente a été lue (cadre bancaire, RTR), soit le fait était déjà établi lors d'une passe antérieure et n'est pas contredit (F-25).

---

## 4. Amendements requis au socle

**Aucun amendement matériel n'est requis. Le PRD (v1.3) est exact au 17 juillet 2026 sur les huit faits vérifiés ; il n'a pas été modifié.**

Un seul point, **optionnel et non bloquant**, est remonté à l'appréciation de l'auteur :

| # | Entrée | Nature | Proposition | Criticité |
|---|---|---|---|---|
| 1 | **F-24** (C-36) — et par ricochet le chapitre 10 | Précision de formulation, **pas** une correction factuelle | La mention « en 2e lecture au 16 juill. 2026 » désigne l'**étape atteinte** et est exacte. LEGISinfo n'enregistrant **aucune activité** à cette étape, une formulation du type « **parvenu à l'étape de la deuxième lecture, non encore franchie ; seule la première lecture (15 juin 2026) est complétée** » écarterait toute lecture erronée selon laquelle le projet de loi aurait progressé au-delà. Renforce l'argument du chapitre 10 (vide réglementaire IA fédéral) plutôt qu'il ne l'affaiblit. | Faible — cosmétique |

**Constats confirmatoires notables** (aucune action requise, mais utiles au dossier de publication) :

- **R-5 tient** : l'absence de désignation d'un organisme de normalisation technique est re-vérifiée à deux sources primaires le 17 juillet 2026. L'interdiction de présenter FDX comme le standard retenu du cadre bancaire canadien reste pleinement fondée à la date de publication.
- **F-29** : la caractérisation du socle (« cible », pas « date ») est confirmée verbatim par Paiements Canada — « driven by readiness, not by haste ». La prudence du socle est validée par la source.
- **F-01** : la RC du 28 juillet est confirmée à l'échéance et non reportée. La date de gel du 16 juillet 2026 des chapitres 1, 2 et 7 est **exacte à sa date**, mais son contenu protocolaire a une **espérance de vie de onze jours** (voir §5).

---

## 5. Points de revalidation restant ouverts après publication

Échéances postérieures au 17 juillet 2026, à reporter au registre de gel et à l'avant-propos.

| # | Fait | Chapitres touchés | Échéance | Nature et impact attendu |
|---|---|---|---|---|
| 1 | **F-01 — Révision MCP 2026-07-28** : protocole sans état, retrait de `Mcp-Session-Id`, extensions (MCP Apps, Tasks), autorisation alignée OAuth/OIDC, politique formelle de dépréciation | **1, 2, 7** | **28 juillet 2026** — soit **11 jours** après la publication | **Le plus imminent et le plus structurant.** RC verrouillée depuis le 21 mai 2026, SDK bêta livrés le 29 juin, date de livraison réaffirmée par la source primaire. Les descriptions de MCP comme protocole **à état** (chapitre 2 notamment) deviendront **historiquement datées** le 28 juillet. La date de gel du 16 juillet les couvre formellement ; une note de l'avant-propos signalant explicitement cette échéance au lecteur est **fortement recommandée**. |
| 2 | **F-34/F-35 — Texte final du règlement du cadre bancaire ; arrêté ministériel de désignation de l'organisme de normalisation technique** | **14, 15, 24** | **après le 26 août 2026** (clôture des commentaires) | Lève ou maintient **R-5**. Une désignation (de FDX ou d'un autre organisme) invaliderait le fait négatif central de ces chapitres. Le texte final peut différer du texte prépublié. **À surveiller en priorité après la RC MCP.** |
| 3 | **F-29 — Lancement effectif du RTR** | **15, 24** | **cible T4 2026** (« late Q4 ») | Lève ou maintient la réserve F-29. Cible conditionnelle à la readiness, avec historique de reports ; UAT complétée, tests de performance intégrés en cours. Jalon intermédiaire : entrée en vigueur du By-law No. 10 et des règles RTR le **24 août 2026**. |
| 4 | **F-09 et F-25 — Entrées en vigueur d'E-23 (BSIF) et de la ligne directrice IA de l'AMF** | **9, 11, 20** | **1er mai 2027** (les deux) | Le discours de « futur proche » de ces chapitres devra passer au présent. Échéance lointaine, faible risque de dérive d'ici là, mais **date commune aux deux régimes** — une seule passe suffira. À cette date, la ligne directrice de l'AMF sur la gestion des risques liés à l'impartition sera **abrogée** et remplacée. |
| 5 | **F-24 — Trajectoire de C-36** | **10** | **continue** | Aucune activité à l'étape de la deuxième lecture au 17 juillet 2026. Toute progression (débat, vote, renvoi en comité) ou toute prorogation/mort au feuilleton modifierait le tableau du vide réglementaire fédéral. Surveillance de faible intensité, LEGISinfo `45-1/c-36`. |
| 6 | **F-25 — Lecture directe de la ligne directrice IA de l'AMF** | 11 | à la prochaine occasion | **Dette de vérification, non une échéance.** Domaine `lautorite.qc.ca` en 403 pour les outils automatisés ; une consultation manuelle (navigateur) permettrait de confirmer par lecture directe la date de publication du 30 mars 2026. Fait non contredit ; enjeu de traçabilité, pas d'exactitude. |

---

## 6. Limites de cette passe

- **Une seule passe, pas de vote adversarial 3 juges** — cohérent avec le budget P4.1 ; les faits vérifiés sont majoritairement binaires et datés (une date d'entrée en vigueur, une étape parlementaire, un numéro de version), ce qui limite l'apport d'un vote adversarial.
- **Quatre sources bloquées** (§3), dont l'intégralité du domaine `lautorite.qc.ca`. Aucune n'a été contournée par une affirmation non fondée ; chaque blocage est déclaré et sa conséquence tracée.
- **Périmètre volontairement borné** aux faits chauds de PRD §8.3 et aux points ouverts du registre de gel. Les faits stables (Loi 25, Lynx, AIDox, C-15 sanctionné le 26 mars 2026) n'ont pas été re-vérifiés — hors périmètre, conformément à la consigne de la tâche.
- **Aucun fichier de gouvernance ni chapitre n'a été modifié.** Seul ce rapport est produit ; les amendements éventuels sont remontés au §4 pour décision de l'auteur.
