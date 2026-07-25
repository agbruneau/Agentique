# Revalidation temporelle finale des faits chauds — 22 juillet 2026

| Champ | Valeur |
|---|---|
| Activité | **P5.1** du [PRDPlan](../prd/PRDPlan.md) — revalidation temporelle finale, phase P5, critère de sortie **J-6** |
| Périmètre | **Les sept lignes de [PRD.md](../prd/PRD.md) §8.3, sans exception**, plus le contrôle des **entrées héritées dont le siège a été retiré du dépôt** (§3 ci-dessous). Rien d'autre. |
| Date de consultation des sources | **22 juillet 2026** — c'est cette date qui fait foi, et non celle du PRD ni celle de la revalidation d'ouverture |
| Motif | **CA-04** exige un rapport de revalidation daté de **moins de trente jours** au moment de publier. Celui du 21 juillet 2026 constate l'état de sources à sa date ; il ne vaut pas pour la publication, et quatre de ses sept lignes portent une échéance à date indéterminée. |
| Rapport antérieur | [`revalidation-2026-07-21.md`](revalidation-2026-07-21.md) — **ouvert et lu avant cette passe**. Ses conclusions ne sont pas reconduites : chacune des sept lignes a été reprise **à la source primaire**, sans exception, y compris celles dont le résultat était connu d'avance. ⚠ Deux de ses conclusions avaient déjà été corrigées par les sources primaires des lots L-05 et L-14 (PRD §8.3) ; *une revalidation conduite sur du secondaire se trompe comme du secondaire.* |
| Statut épistémique de ce rapport | **Aucune entrée F-xx n'est créée ici.** Une revalidation constate l'état d'une source à une date ; elle **n'est pas une passe d'instruction**, ne vaut ni extraction citée ni vote adversarial, ne clôt aucun lot et n'arbitre aucune divergence. Le socle propre demeure à **98 entrées**, le socle hérité à **33**. |
| Outil de consultation | `WebFetch` et `WebSearch` exclusivement ; `pdftotext` pour l'extraction du texte de NIST IR 8547 ipd ; `git show` pour le contenu du commit `fd8f1be~1`. |

---

## 1. Verdicts — les sept lignes de PRD §8.3

| # | Fait chaud (PRD §8.3) | Chapitres | Verdict au 22 juillet 2026 |
|---|---|---|---|
| 1 | Révision majeure de la spécification MCP — protocole sans état, retrait de `Mcp-Session-Id` | ch. 2, 22 | **INCHANGÉ** — version courante toujours `2025-11-25` ; substance au brouillon ; **date du 28 juillet 2026 toujours absente de la source** |
| 2 | Texte final du règlement du cadre bancaire ; arrêté désignant l'organisme de normalisation | ch. 21 | **INCHANGÉ** — le règlement ne désigne pas ; la désignation demeure réservée à un arrêté ministériel |
| 3 | Consolidation IETF du brouillon SCIM-agents ; état du brouillon CSA | ch. 2, 7 | **INCHANGÉ** pour les deux — et le brouillon CSA **confirme F-39 à la source primaire** |
| 4 | Statut de NIST IR 8547 | ch. 16, 17, 18 | **INCHANGÉ** — toujours *Initial Public Draft* de novembre 2024 |
| 5 | Statut des conventions sémantiques OpenTelemetry pour les agents | ch. 24 | **INCHANGÉ au siège courant** (dépôt dédié) ; **ÉVOLUÉ au siège abandonné** (registre de `opentelemetry.io`) |
| 6 | Entrée en vigueur simultanée d'E-23 et de la ligne directrice IA de l'AMF au 1ᵉʳ mai 2027 | ch. 19, 20 | **INCHANGÉ** pour E-23 ; **INACCESSIBLE** pour l'AMF — HTTP 403 sur deux adresses |
| 7 | Jalons de dépréciation (2030) et d'interdiction (2035) visés par IR 8547 | Partie V | **INCHANGÉ** — libellés relevés dans le texte du document lui-même |

**Six lignes inchangées, une évolution collatérale sur un siège que le socle n'emploie plus, un accès refusé.** Aucun fait n'a bougé au point d'exiger une entrée de socle nouvelle. Aucune pièce ne devient fausse du fait de cette passe — mais **deux points appellent une décision d'auteur** avant publication (§4).

---

## 2. Détail par fait

### 2.1 Révision MCP — inchangé : ni la date ni la publication ne sont à la source

**Ce que le socle porte** (H-09) : révision majeure attendue le **28 juillet 2026** (protocole sans état, retrait de `Mcp-Session-Id`).

**Ce que les sources montrent, au 22 juillet 2026.** La page de versionnage donne toujours la version courante à **`2025-11-25`** et distingue les trois mêmes états — *Draft*, *Current*, *Final*. **Aucune révision datée de 2026 n'y figure**, et le brouillon n'y porte pas de date de publication. Le journal des changements du brouillon porte toujours, en tête de ses changements majeurs, les deux éléments annoncés — verbatim relevés :

1. « Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport » (SEP-2567) ;
2. « Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake » (SEP-2575).

Le journal en compte aujourd'hui **neuf** au registre des changements majeurs, ainsi que la dépréciation de *Roots*, *Sampling* et *Logging* (SEP-2577) et celle de l'enregistrement dynamique de client au profit des *Client ID Metadata Documents*. ⚠ **Ce cardinal n'établit aucune évolution depuis le 21 juillet** : le rapport d'ouverture citait les deux premiers éléments sans annoncer de cardinal, et les deux relevés ne sont pas comparables.

**Verdict : INCHANGÉ.** La substance demeure confirmée **à l'état de brouillon** ; la date du 28 juillet 2026 demeure absente de la source. ⚠ **R-09 s'applique intégralement, sans atténuation** : les ch. 2 et 22 écrivent « annoncé au brouillon », **jamais** « publié le 28 juillet 2026 ».

⚠ **Point à porter à la décision d'auteur, et il est temporel, non factuel.** La date annoncée tombe **six jours après cette consultation**, à l'intérieur de la phase P5. Si une révision datée paraît avant la publication, la formule « annoncé au brouillon » cesse d'être exacte aux ch. 2 et 22 — non parce qu'elle aurait été fausse, mais parce qu'elle aura été dépassée. *Une formule prudente se périme aussi.* → §4, point 1.

*Sources : [modelcontextprotocol.io/specification/versioning](https://modelcontextprotocol.io/specification/versioning) et [le journal du brouillon](https://modelcontextprotocol.io/specification/draft/changelog), consultés le 22 juillet 2026.*

### 2.2 Cadre bancaire et arrêté de désignation — inchangé

**Ce que le socle porte** (H-08, H-16) : aucun standard technique désigné ; clôture des commentaires au **26 août 2026** ; arrêté de désignation à date inconnue.

**Ce que la source montre.** Le règlement prépublié à la *Gazette du Canada*, Partie I, vol. 160, n° 26, **ne désigne pas** d'organisme de normalisation technique : il établit le processus et les critères de désignation. Verbatim relevé sur la page : « The Act includes authorities for the Minister of Finance to designate and revoke the technical standards body, through a Ministerial Order, and other criteria to inform the assessment of candidates for said body. » La page déclare une période de prépublication **prolongée à 60 jours** ; elle **n'énonce pas de date de clôture en toutes lettres**.

**Verdict : INCHANGÉ.** Le fait négatif **VÉRIFIÉ** de H-08 (degré 1, PRD §8.6) tient, et **Q5 du Vol. II ch. 21 §21.2 reste ouverte**. ⚠ **Le ch. 21 énumère des scénarios, il ne pronostique pas.**

⚠ **Borne de cette ligne, et elle est nouvelle.** La date du **26 août 2026** n'a **pas** été relue à une page primaire dans cette passe : la page de la Gazette ne la porte pas, et le communiqué du ministère des Finances a renvoyé **HTTP 403**. Elle se déduit de la prépublication du 27 juin 2026 majorée de 60 jours, et elle est corroborée par des sources secondaires (cabinets). *Une date déduite d'un délai et une date lue sont deux choses différentes* — H-16 la porte, cette passe ne la reconfirme pas au primaire.

*Sources : [Gazette du Canada, Partie I, vol. 160, n° 26](https://gazette.gc.ca/rp-pr/p1/2026/2026-06-27/html/reg3-eng.html), consultée le 22 juillet 2026. Communiqué du ministère des Finances : **inaccessible** (HTTP 403). Corroboration secondaire, nommée à son emploi : [Fasken](https://www.fasken.com/en/knowledge/2026/07/draft-consumer-driven-banking-regulations-released) — jamais source unique d'un fait central.*

### 2.3 Brouillon SCIM-agents et brouillon CSA — inchangés, et le second confirme F-39

**(a) `draft-abbey-scim-agent-extension`.** Le registre de l'IETF porte, verbatim : « This Internet-Draft is **not endorsed by the IETF** and has **no formal standing** in the IETF standards process » ; « Type: Expired Internet-Draft (individual) » ; « IESG state: Expired » ; « This Internet-Draft is no longer active. » Version **00**, seule et dernière, du **16 octobre 2025**, « Expired & archived ».

**Verdict : INCHANGÉ.** Aucune consolidation IETF n'est constatée. Le fait que la spécification CSA s'adosse à un texte **expiré et archivé** demeure entier, et le ch. 7 le porte.

**(b) Spécification CSA « Agent Registry ».** L'en-tête de la page porte, verbatim : « **White Paper | 2026-03-27 | Status: draft** ». **Aucun champ de mise à jour ultérieure n'y figure.** L'alignement sur l'OWASP Top 10 for Agentic Applications (2026) y est bien exposé, avec ASI03 et ASI10 nommés.

**Verdict : INCHANGÉ — et c'est une confirmation à la source primaire de F-39.** La date portée par la page est exactement celle que le socle hérité donne à H-03, **27 mars 2026** ; l'alignement OWASP, que la revalidation d'ouverture avait pris pour indice d'une mise à jour au 20 mai 2026, est présent **sans** date de révision associée. ⚠ **Le retrait prononcé le 21 juillet 2026 est donc soutenu par une seconde lecture indépendante** : la conclusion « le brouillon CSA a été mis à jour le 20 mai 2026 » ne trouve aucun appui à la source. Le statut demeure **brouillon de *labs***, non une norme ratifiée (R-09).

*Sources : [datatracker.ietf.org — draft-abbey-scim-agent-extension](https://datatracker.ietf.org/doc/draft-abbey-scim-agent-extension/) ; [CSA Labs — Agent Registry Specification](https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/), consultées le 22 juillet 2026.*

### 2.4 NIST IR 8547 — inchangé, toujours un projet

**Ce que le socle porte** (H-17) : *Initial Public Draft*, avec la réserve du Vol. I — « dates à re-vérifier, le document étant à l'état de *Initial Public Draft* ».

**Ce que les sources montrent.** La fiche du NIST donne le document comme **initial public draft**, publié le **12 novembre 2024**, période de commentaires close le **10 janvier 2025**, note de planification du **21 janvier 2025** signalant la mise à disposition des commentaires reçus. **Aucune version finale n'est constatée au 22 juillet 2026** ; l'historique de la fiche ne porte qu'une ligne, « 11/12/24: IR 8547 (Draft) ». Le texte du document lui-même, extrait du PDF, porte en tête de page courante « NIST IR 8547 ipd (Initial Public Draft) — November 2024 ».

**Verdict : INCHANGÉ.** ⚠ **R-11 s'applique sans atténuation** : l'horloge de toute la Partie V repose sur un **projet**, et *une horloge fondée sur un projet doit dire qu'elle l'est*.

**La piste « NISTIR 8647 » se résout, et par la négative.** Le rapport d'ouverture signalait un fil de la liste `pqc-forum` mentionnant un identifiant « NISTIR 8647 » portant le même intitulé. Le fil a été ouvert : **son corps référence systématiquement 8547** — annonce de Dustin Moody du 12 novembre 2024, projet public initial, commentaires jusqu'au 10 janvier 2025. La chaîne « 8647 » n'apparaît qu'au **titre** du fil. ⚠ **Aucune renumérotation n'est constatée** — et ce constat est borné à cette page : il n'établit pas qu'aucun document successeur n'existe ailleurs.

*Sources : [csrc.nist.gov/pubs/ir/8547/ipd](https://csrc.nist.gov/pubs/ir/8547/ipd) ; [fil `pqc-forum`](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/uHMw8RNGkC8) ; [NIST IR 8547 ipd (PDF)](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf), consultés le 22 juillet 2026.*

### 2.5 Conventions sémantiques OpenTelemetry — inchangé au siège courant, évolué au siège abandonné

**Ce que le socle porte** (F-74, F-75, F-76, F-77, F-90, F-95) : déplacement daté du 12 juin 2026 vers un dépôt dédié ; statut *Development* relevé sur deux fichiers agentiques ; aucune version citable, « Schema URL » à « TODO » ; échelle des groupes de conventions sémantiques à cinq échelons.

**Ce que les sources montrent, et il faut distinguer deux sièges.**

- **Siège courant — le dépôt dédié `open-telemetry/semantic-conventions-genai`.** La page du dépôt porte « **No releases published** » ; la rubrique « Schema URL » de sa documentation porte « **TODO** ». Le document `docs/gen-ai/gen-ai-agent-spans.md` déclare en tête de ses sections « **Status:** Development », et ce marquage est constant sur l'ensemble des segments couverts — création d'agent, invocation, flux de travail, planification, exécution d'outil. **Verdict : INCHANGÉ.** F-74, F-75 et F-77 demeurent soutenus à leur siège.
- **Siège abandonné — `opentelemetry.io/docs/specs/semconv/`.** La page GenAI ne porte plus qu'un avis de déplacement. ⚠ **Le registre d'attributs a changé de marquage** : là où la revalidation d'ouverture avait relevé le statut **Development** sur tous les attributs GenAI, le registre les affiche aujourd'hui **Deprecated**, chacun assorti de la note « Moved to the OpenTelemetry GenAI semantic conventions repository ». **Verdict : ÉVOLUÉ.**

**Ce que cet écart ne fait pas.** Il ne rend faux aucun énoncé du **ch. 24** : la pièce ancre ses constats sur le **dépôt dédié**, les date au 21 juillet 2026 et déclare leurs bornes fichier par fichier (§24.2). *Un statut « Deprecated » posé sur l'emplacement d'origine d'un document déplacé qualifie l'emplacement, non le document.* Le confondre avec le statut de maturité des conventions serait exactement la faute que F-76 met en garde de commettre — deux échelles distinctes ne se fusionnent pas.

⚠ **Borne sur l'échelle, et elle est déclarée plutôt que résolue.** La page de versionnage et de stabilité du projet OpenTelemetry, consultée ce jour, décrit une échelle de maturité **des signaux** — *Development* → *Stable*, plus *Deprecated* et *Removed* — et **ne nomme ni `alpha`, ni `beta`, ni `release_candidate`** comme échelons de maturité des groupes de conventions sémantiques. C'est la **seconde** échelle que F-76 signale explicitement, et non celle qu'il établit. **L'échelle à cinq échelons des groupes de conventions sémantiques n'a pas été rejouée à son siège dans cette passe** : F-76 n'est ni confirmée ni infirmée ici.

*Sources : [github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai) ; [`docs/gen-ai/gen-ai-agent-spans.md`](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) ; [opentelemetry.io/docs/specs/semconv/gen-ai/](https://opentelemetry.io/docs/specs/semconv/gen-ai/) ; [registre des attributs GenAI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) ; [versionnage et stabilité](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/), consultés le 22 juillet 2026.*

### 2.6 Entrée en vigueur du 1ᵉʳ mai 2027 — E-23 inchangé, AMF inaccessible

**E-23.** La fiche du BSIF donne la publication au **11 septembre 2025** et l'entrée en vigueur au **1ᵉʳ mai 2027** — concordant avec H-04. La page **ne mentionne aucune disposition ni période transitoire**. **Verdict : INCHANGÉ.**

⚠ **Le point de vocabulaire signalé le 21 juillet 2026 demeure ouvert** : des commentaires de cabinets décrivent l'intervalle publication → entrée en vigueur comme une « période de transition de 18 mois » là où le socle porte « aucune disposition transitoire ». La lecture de ce jour **ne trouve rien de tel sur la page de l'éditeur**, ce qui est cohérent avec le socle sans le trancher — *l'absence d'une mention sur une page de présentation n'est pas un balayage du texte de la ligne directrice* (PRD §8.6, la distinction entre les degrés 1 et 3).

**Ligne directrice IA de l'AMF — INACCESSIBLE.** Deux adresses ont été tentées, l'une anglaise, l'autre française : **HTTP 403 sur les deux**. ⚠ **C'est le même refus que celui rencontré par les outils du Vol. II**, et il confirme que la **lacune 4** demeure entière. Il en découle deux conséquences, et aucune n'est tranchée ici :

1. la **date d'entrée en vigueur au 1ᵉʳ mai 2027** — seul élément de cette ligne de §8.3 qui concerne l'AMF — **n'a pas été reconfirmée à sa source** dans cette passe. Elle demeure portée par le socle hérité et concordante entre les livrables du dépôt ;
2. la **divergence sur la date de publication** — 30 mars 2026 au Vol. II, 7 avril 2026 à la veille technologique — demeure une **divergence non arbitrée** (PRD §7.5). *Ce rapport la signale et ne la tranche pas ;* elle n'entre pas dans le périmètre d'une revalidation.

*Sources : [BSIF — Ligne directrice E-23 (2027)](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027), consultée le 22 juillet 2026. `lautorite.qc.ca` : **inaccessible** (HTTP 403), deux adresses tentées.*

### 2.7 Jalons 2030 et 2035 — inchangés, relevés dans le texte du document

Le texte du PDF a été extrait et lu. Les tableaux 2 et 4 du document portent, verbatim, la colonne « Transition » suivante : **« Deprecated after 2030 »** au niveau de sécurité de 112 bits et **« Disallowed after 2035 »** — pour ECDSA, EdDSA et RSA (tableau 2, signatures) comme pour Diffie-Hellman en corps fini, MQV, Diffie-Hellman sur courbes elliptiques et RSA (tableau 4, établissement de clés). Le §4.1.2 précise que le NIST « intends to instead deprecate rather than fully disallow classical key-establishment schemes at the 112-bit security level ».

**Verdict : INCHANGÉ.** Le document n'ayant pas été révisé (§2.4), les jalons qu'il porte ne peuvent pas avoir changé — et ils ont néanmoins été relus dans son texte plutôt que déduits de ce raisonnement.

⚠ **R-11 dans les deux sens** : écrire « dépréciation **visée** pour 2030 », « interdiction **visée** pour 2035 », **avec le statut de projet du document qui les porte**, et jamais une formule d'obligation légale.

⚠ **Une borne perdue est signalée, et elle vit dans le rapport d'ouverture, non dans une pièce.** Le §2.7 de [`revalidation-2026-07-21.md`](revalidation-2026-07-21.md) écrit que « les modes hybrides restent admis au-delà de 2035 ». **Le document ne l'écrit pas.** Son §3.2 donne les solutions hybrides pour « typically expected to be temporary measures that lead to a second transition to cryptographic tools that use only PQC algorithms », et ses §3.2.1 et §3.2.2 énoncent seulement que le NIST « will accommodate the use of a hybrid key-establishment mode and dual signatures in FIPS 140 validation when suitably combined with a NIST-approved scheme » — **sans borne de date**. ☑ **Le ch. 17 §17.3, patron 2, porte déjà la réserve exacte** : « le projet **ne dit pas** que les modes hybrides restent admis au-delà de 2035, et lui prêter cette autorisation serait lui faire dire ce qu'il n'écrit pas ». *La pièce est bornée là où le rapport qui l'a précédée ne l'était pas.* Le rapport du 21 juillet **n'est pas corrigé par cette passe** — il constate un état à sa date, et le réécrire effacerait la trace de l'écart.

⚠ Les jalons du **décret 14412** et ceux du **Quantum Safe Financial Forum** d'Europol **n'ont pas été revalidés** : ils ne figurent pas à PRD §8.3. Ils **ne se fusionnent jamais** avec ceux d'IR 8547.

*Source : [NIST IR 8547 ipd (PDF)](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf), texte extrait et lu le 22 juillet 2026.*

---

## 3. Les entrées héritées — vérification contre un blob git, et pourquoi c'est une borne

**Le mur, énoncé avant le résultat.** Le commit **`fd8f1be`** (« Phase 4 en cours », 22 juillet 2026, auteur : André-Guy Bruneau) supprime `Synthese Monographie.md` et son `.pdf`, au **Vol. I** comme au **Vol. II** — constat direct par `git show --name-status fd8f1be`, filtré sur le motif `*Synthese*` : **quatre lignes `D`**. ⚠ **Ce relevé est borné à son filtre** : la consignation du [`CLAUDE.md`](../CLAUDE.md) du volume porte six suppressions hors du volume III, les deux `index.html` compris ; ils n'entrent pas dans le motif employé ici et n'ont pas été constatés par cette passe. Ce fichier est le **siège déclaré** de H-27, H-28, H-29, H-30, H-31 et H-32, ainsi que de trois des quatre occurrences de la formule de non-compositionnalité de la sûreté.

**Conduite sur l'arbre de travail, la revalidation des entrées héritées porterait sur un corpus absent du dépôt.** Elle a donc été conduite **contre le contenu du commit `fd8f1be~1`**, extrait par `git show "fd8f1be~1:1 - Corpus Agentique/1 - InteroperabiliteAgentique/Synthese Monographie.md"` — 1 039 lignes.

| Entrée | Siège déclaré | Constat au blob `fd8f1be~1` |
|---|---|---|
| **H-24** | `Monographie.md` §3.10.1 | ☑ **Vérifié sur l'arbre de travail**, non sur un blob : le fichier est **présent** au dépôt. Verbatim relevé : « un agent sûr et un outil sûr, une fois composés, ne donnent pas un système sûr. La sûreté n'est pas une propriété compositionnelle », et « la frontière de confiance n'est plus le périmètre d'un système mais *chaque arête* du graphe d'interaction » — même paragraphe, section `### 3.10.1 Cadrage : l'interopérabilité crée une surface d'attaque non-composable`. **Opposable.** |
| **H-27** | `Synthese Monographie.md` §10.3 | ☑ Présent au blob, section `### 10.3 Le quatrième terme : l'exploitation`. Verbatim relevé : « *Découplage, contrat, évolution* deviennent ainsi *découplage, contrat, évolution, exploitation*. » La reprise annoncée en §11.1 est présente, section `### 11.1 Résultat central : l'invariant réinstancié`. |
| **H-28** | `Synthese Monographie.md` §11.5 | ☑ Présent au blob, section `### 11.5 Fronts de recherche ouverts`. Verbatim relevé : « l'identité non humaine et la traçabilité de bout en bout des décisions déléguées au-delà de deux sauts restent des problèmes ouverts, dont l'urgence croît avec le degré d'autonomie consenti », et « le besoin d'une *science de l'évaluation* inter-fournisseurs […] et d'une métrique d'horizon de tâche déléguée ». |
| **H-29** | `Synthese Monographie.md` §11.6, tableau 15 | ☑ Présent au blob, section `### 11.6 Synthèse opérationnelle : l'invariant strate par strate`. Ligne relevée : `| Entreprise (§6) | Politique d'autorisation, plan de contrôle | Identité non humaine et délégation multi-saut |`. |
| **H-30** | `Synthese Monographie.md` §10.2 | ☑ Présent au blob, section `### 10.2 Plan de contrôle obligatoire et dorsale tri-plan`. Verbatim relevé, y compris « **plan de contrôle obligatoire** », « **dorsale d'intégration tri-plan** » et la phrase de logique en quatre membres. |
| **H-31** | `Synthese Monographie.md` §4.2, tableau 3 | ☑ Présent au blob. Le tableau porte la légende « Tableau 3 — Continuum d'autonomie et déplacement de la tenue de la boucle », l'en-tête `| Niveau | Désignation | Qui tient la boucle de contrôle | Rôle de l'humain |` et la ligne `| 2 | Copilote | L'humain, assisté par le modèle | Valide chaque étape |`. **C'est bien le seul siège des désignations du continuum à six niveaux**, sur lequel R-13 est calibré. |
| **H-32** | `Synthese Monographie.md` §10 — **fait négatif** | ☑ Le fait négatif se constate au blob : `grep -cE "[Bb]or[ée]alis"` sur le fichier entier retourne **0**. Le nom n'y figure pas, ni accentué ni non accentué. |
| **Formule de non-compositionnalité** | `Synthese` §5.10 (siège déclaré), §6.12, §11.3 | ☑ Les trois occurrences sont présentes au blob, dans les sections `### 5.10 Sécurité non composable et modes d'échec`, `### 6.12 Sécurité du parc d'agents à l'échelle` et `### 11.3 Tensions transversales et compromis`. La quatrième occurrence, `Monographie.md` §3.10.1, est **au dépôt** (H-24). |

**Contrôle d'existence des neuf sections citées par le volume.** `4.2`, `5.10`, `6.12`, `10.2`, `10.3`, `11.1`, `11.3`, `11.5`, `11.6` : chacune apparaît **exactement une fois** comme titre de niveau 3 dans le blob. Aucun renvoi du volume ne pointe vers une section inexistante.

### Ce que cette vérification est, et ce qu'elle n'est pas

⚠ **Elle a été faite contre un blob git, et non contre le dépôt.** Un blob est le contenu d'un fichier à un commit ; il n'est ni publié, ni consultable par un lecteur de l'ouvrage, ni opposable à un tiers. **Ce n'est pas une équivalence : c'est une borne.** *Un renvoi exact vers un fichier absent demeure un renvoi exact ; il cesse seulement d'être opposable.*

⚠ **La question de la restauration relève de l'auteur** et n'est pas tranchée ici : elle porte sur la charge éditoriale d'un autre volume, hors compétence de l'instance d'exécution. Elle est ouverte au registre sous **R-G-52**, et elle y reste. **Aucun fichier n'a été restauré. Aucun fichier hors du volume III n'a été modifié. Aucune citation n'a été réécrite.**

⚠ **Le volume II est dans le même cas et n'a pas été examiné** : le commit y supprime les mêmes fichiers, et les entrées H-01 à H-16 n'ont pas été revalidées par cette passe — elles ne figurent pas aux faits chauds de §8.3, et leur revalidation n'était pas mandatée.

---

## 4. Conséquences — ce qui doit être décidé, et par qui

| # | Conséquence | Instance | Où |
|---|---|---|---|
| 1 | **La révision MCP est attendue le 28 juillet 2026, soit six jours après cette passe.** Si elle paraît datée avant la publication, la formule « annoncé au brouillon » des ch. 2 et 22 est dépassée ; si elle ne paraît pas, elle tient. **Deux options, aucune tranchée ici** : *(a)* reconduire la formule et la borner à la date de gel des pièces ; *(b)* rouvrir les ch. 2 et 22 après le 28 juillet 2026 pour y porter l'état réel. L'option *(b)* rouvre du texte tenu pour fait et engage R-09 | **auteur** — la formulation d'un garde-fou et la réouverture de pièces closes ne relèvent pas de l'exécution | ch. 2, ch. 22 ; PRD §8.3 ligne 1 |
| 2 | **La ligne directrice IA de l'AMF demeure inaccessible** — HTTP 403 sur les deux adresses tentées, et le Vol. II avait déjà essuyé le même refus. La lacune 4 n'est pas comblée, et la date d'entrée en vigueur au 1ᵉʳ mai 2027 n'est pas reconfirmée à sa source. **Aucune source de moindre qualité ne s'y substitue** (règle du dépôt : *les lacunes s'exposent, elles ne se comblent pas*) | **auteur** — décider si une lacune d'accès à une source réglementaire est publiable en l'état | ch. 19, ch. 20 ; PRD §10, lacune 4 |
| 3 | **La date du 26 août 2026 (clôture des commentaires du cadre bancaire) est déduite, non relue** dans cette passe. H-16 la porte ; le communiqué du ministère est inaccessible | exécution | PRD §8.3 ligne 2 |
| 4 | **F-76 n'a pas été rejouée à son siège.** L'échelle constatée ce jour sur `opentelemetry.io` est la **seconde** échelle, celle des signaux, que F-76 signale explicitement comme distincte. Aucune contradiction n'est constatée ; aucune confirmation non plus | exécution — si un rejeu est jugé nécessaire, il relève de P5.2 | PRD §7.9, F-76 |
| 5 | **Le §2.7 du rapport du 21 juillet 2026 porte une borne perdue** sur les modes hybrides. Le ch. 17 §17.3 est, lui, borné correctement. **Le rapport n'est pas corrigé** : il constate un état à sa date | signalé, non corrigé | [`revalidation-2026-07-21.md`](revalidation-2026-07-21.md) §2.7 |
| 6 | **PRD §8.3 n'est pas amendé par cette passe.** Aucun des sept faits n'a bougé ; **une revalidation qui ne constate aucun mouvement n'a rien à porter au cadrage**. ⚠ Le §8.3 ne renvoie donc, à ce jour, qu'au rapport d'ouverture : y ajouter le renvoi au présent rapport est un travail de **renvoi**, relevant de P5.3 avec les autres porteurs | exécution, **en P5.3** | PRD §8.3 |
| 7 | **Ce rapport se périme à son tour.** CA-04 exige moins de trente jours au moment de publier : il couvre une publication jusqu'au **21 août 2026**. Au-delà, P5.1 se rejoue | exécution | CA-04, jalon J-6 |

---

## 5. Ce que ce rapport ne dit pas

*Une passe qui ne borne pas son périmètre laisse croire qu'elle l'a couvert.*

1. **Aucune entrée de socle n'est créée.** Les constatations ci-dessus sont des **lectures de pages et de textes à une date**, non des extractions citées soumises au vote : elles ne valent ni [A] ni [B]. Le socle propre demeure à **98 entrées**, le socle hérité à **33**.
2. **Aucun lot n'est clos ni rouvert. Aucune divergence n'est arbitrée** — ni celle d'AP2, ni celle de la date de publication de la ligne directrice de l'AMF (PRD §7.5). Une revalidation constate ; elle n'instruit pas.
3. **Deux sources n'ont pas pu être ouvertes** : `lautorite.qc.ca` (HTTP 403, deux adresses) et le communiqué du ministère des Finances sur `canada.ca` (HTTP 403). Les faits qui en dépendent demeurent portés par le socle hérité et par corroboration secondaire nommée, **jamais élevés au rang de reconfirmation**.
4. **Le PDF de NIST IR 8547 n'a pas été lu intégralement** : le texte a été extrait et les passages relatifs aux jalons, aux tableaux 2 et 4 et au §3.2 ont été lus. Aucun constat ne vaut pour le reste du document.
5. **Le dépôt `semantic-conventions-genai` n'a pas été balayé.** Deux ressources y ont été ouvertes — la page du dépôt et `docs/gen-ai/gen-ai-agent-spans.md`. Les autres fichiers du répertoire `docs/gen-ai` n'ont pas été rouverts par cette passe, leur cardinal n'a pas été re-mesuré, et le décompte d'ouverture porté par le ch. 24 §24.2 (six ouverts sur onze) n'a pas été revérifié.
6. **F-76 n'est ni confirmée ni infirmée** (§2.5, §4 point 4).
7. **Les entrées héritées ont été vérifiées contre un blob git, non contre le dépôt** (§3). C'est une borne déclarée, non une équivalence.
8. **Les entrées héritées du Vol. II (H-01 à H-16) n'ont pas été revalidées** : elles ne figurent pas aux faits chauds de §8.3.
9. **Les faits hors §8.3 n'ont pas été revalidés** : A2A, Entra Agent ID, AGNTCY, art. 12.1 de la Loi 25, avis ACVM 11-348, décret 14412, Quantum Safe Financial Forum, ainsi que l'ensemble des sources des lots L-01 à L-14b. Ils relèvent de leurs lots respectifs.
10. **Aucun motif de balayage du PRD §A.6 n'a été rejoué** : c'est l'objet de **P5.2**, distinct de cette passe.
11. **Aucune pièce n'a été relue, corrigée ni réécrite.** Les deux consultations de pièces rapportées ici — ch. 24 §24.2 et ch. 17 §17.3 — l'ont été pour établir si un fait déplacé rendait un énoncé faux. Il ne l'a pas fait. **Aucune modification n'a été portée à `monographie/`.**
12. **Aucune remontée n'a été ouverte au registre.** Aucun fait n'a bougé au point d'exiger une entrée nouvelle ; les deux points qui appellent une décision d'auteur (§4, points 1 et 2) sont posés ici avec leurs options, et leur inscription au registre relève de la passe qui les prendra en charge.
