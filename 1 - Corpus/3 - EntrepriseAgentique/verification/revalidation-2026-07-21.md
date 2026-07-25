# Revalidation d'ouverture des faits chauds — 21 juillet 2026

| Champ | Valeur |
|---|---|
| Activité | **P0.6** du [PRDPlan](../prd/PRDPlan.md) — revalidation d'ouverture, phase P0, jalon J-1 |
| Périmètre | **Les sept lignes de [PRD.md](../prd/PRD.md) §8.3, sans exception.** Rien d'autre. |
| Date de consultation des sources | **21 juillet 2026** — c'est cette date qui fait foi, et non celle du PRD |
| Motif | ⚠ La révision majeure de la spécification MCP était attendue le **28 juillet 2026**, soit sept jours après cette passe. Un fait chaud revalidé à l'ouverture coûte une lecture ; revalidé à la publication, il coûte une réécriture. |
| Statut épistémique de ce rapport | **Aucune entrée F-xx n'est créée ici.** Une revalidation constate l'état d'une source à une date ; elle **n'est pas une passe d'instruction** et ne vaut ni extraction citée ni vote adversarial. Le socle propre reste à **0 entrée**. |

---

## 1. Verdicts — les sept lignes de PRD §8.3

| # | Fait chaud (PRD §8.3) | Chapitres | Verdict au 21 juillet 2026 |
|---|---|---|---|
| 1 | Révision majeure de la spécification MCP — protocole sans état, retrait de `Mcp-Session-Id` | ch. 2, 22 | **Substance confirmée au brouillon ; date non confirmée à la source** |
| 2 | Texte final du règlement du cadre bancaire ; arrêté désignant l'organisme de normalisation | ch. 21 | **Inchangé et précisé** — la désignation n'a **pas** eu lieu |
| 3 | Consolidation IETF du brouillon SCIM-agents ; état du brouillon CSA | ch. 2, 7 | **Deux verdicts distincts** : SCIM-agents **inchangé et renforcé** ; brouillon CSA **ÉVOLUÉ** |
| 4 | Statut de NIST IR 8547 | ch. 16, 17, 18 | **Inchangé** — toujours *Initial Public Draft* |
| 5 | Statut des conventions sémantiques OpenTelemetry pour les agents | ch. 24 | **ÉVOLUÉ** — et dans un sens qui **durcit** la réserve |
| 6 | Entrée en vigueur simultanée d'E-23 et de la ligne directrice IA de l'AMF au 1ᵉʳ mai 2027 | ch. 19, 20 | **Inchangé** — un point de vocabulaire à instruire |
| 7 | Jalons de dépréciation (2030) et d'interdiction (2035) visés par IR 8547 | Partie V | **Inchangé** |

**Deux faits ont évolué, un est confirmé en substance sans l'être en date, quatre sont inchangés.** Aucun n'invalide une thèse du TOC ; deux obligent à réinstruire un lot avant rédaction.

---

## 2. Détail par fait

### 2.1 Révision MCP — substance confirmée, date non confirmée

**Ce que le socle porte** (H-09) : « révision majeure attendue le **28 juillet 2026** (protocole sans état, retrait de `Mcp-Session-Id`) ».

**Ce que la source montre.** La page de versionnage de la spécification donne la version courante à **`2025-11-25`** et distingue trois états de révision — *Draft*, *Current*, *Final*. Le journal des changements du **brouillon** porte, en tête de ses changements majeurs, exactement les deux éléments annoncés :

1. « Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport » (SEP-2567) ;
2. « Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake » (SEP-2575).

**Verdict : la substance de la révision annoncée est confirmée — à l'état de brouillon.** La **date** du 28 juillet 2026 n'apparaît pas à la source consultée : le brouillon n'y porte pas de date de publication. ⚠ **R-09 s'applique intégralement** : un brouillon n'est pas une révision ratifiée, et le ch. 2 comme le ch. 22 écriront « annoncé au brouillon », jamais « publié le 28 juillet 2026 », tant que la version datée n'est pas sortie.

**Trois constatations collatérales, hors §8.3 mais utiles aux lots concernés** — consignées ici pour n'avoir pas à les redécouvrir, **sans être élevées au socle** :

- le brouillon **déprécie** les fonctions *Roots*, *Sampling* et *Logging*, et recommande explicitement, pour la journalisation, « log to `stderr` (stdio) or use OpenTelemetry instead of Logging ». → matière du **ch. 24**, à croiser avec H-12 (la journalisation confiée aux agents « n'est généralement pas recommandée ») ;
- le brouillon documente la propagation du contexte de trace **OpenTelemetry** dans `_meta` (`traceparent`, `tracestate`, `baggage`, SEP-414). → matière directe du **ch. 24 §24.4**, corrélation trace ↔ chaîne de mandat ;
- le brouillon **déprécie l'enregistrement dynamique de client** (RFC 7591) au profit des *Client ID Metadata Documents*. → matière du **ch. 2** (étirement des RFC) et du **ch. 6**.

*Source : [modelcontextprotocol.io/specification/versioning](https://modelcontextprotocol.io/specification/versioning) et [le journal du brouillon](https://modelcontextprotocol.io/specification/draft/changelog), consultés le 21 juillet 2026.*

### 2.2 Cadre bancaire et arrêté de désignation — inchangé, et c'est le fait qui compte

**Ce que le socle porte** (H-08, H-16) : aucun standard technique désigné ; clôture des commentaires au **26 août 2026** ; arrêté de désignation à date inconnue.

**Ce que les sources montrent.** La *Consumer-Driven Banking Act* a reçu la sanction royale le **26 mars 2026** ; le règlement a été **prépublié** à la *Gazette du Canada*, Partie I, vol. 160, n° 26, le **27 juin 2026**, ouvrant une période de commentaires de 60 jours **close le 26 août 2026** — date concordante avec H-16. Le règlement **ne désigne pas** l'organisme de normalisation technique : la Loi réserve cette désignation à un **arrêté ministériel**, en imposant au ministre de tenir compte de principes énumérés (partage sûr, sécuritaire et efficace des données ; équité, accessibilité, transparence, bonne gouvernance).

**Verdict : inchangé.** Le fait négatif **VÉRIFIÉ** de H-08 (degré 1, PRD §8.6) tient, et **Q5 du Vol. II ch. 21 §21.2 reste ouverte**. ⚠ **Ne rien anticiper** : le ch. 21 énumère des scénarios, il ne pronostique pas.

*Sources : [Gazette du Canada, Partie I, vol. 160, n° 26](https://gazette.gc.ca/rp-pr/p1/2026/2026-06-27/html/reg3-eng.html) ; [communiqué du ministère des Finances, juin 2026](https://www.canada.ca/en/department-finance/news/2026/06/government-pre-publishes-regulations-to-prevent-fraud-and-facilitate-the-next-phase-of-consumer-driven-banking.html) ; [Loi sur les services bancaires axés sur le consommateur](https://laws-lois.justice.gc.ca/eng/acts/C-36.75/FullText.html). Corroboration secondaire (cabinets) : [Blakes](https://www.blakes.com/insights/proposed-consumer-driven-banking-regulations-released-for-comment/), [Bennett Jones](https://www.bennettjones.com/Insights/Blogs/Canada-Advances-Consumer-Driven-Banking-Framework-with-Proposed-Regulations) — jamais source unique d'un fait central.*

### 2.3 Brouillon SCIM-agents : inchangé et renforcé — brouillon CSA : **évolué**

**(a) `draft-abbey-scim-agent-extension`.** Le socle (H-03) porte l'expiration au **19 avril 2026**. Le registre de l'IETF confirme et **ajoute trois précisions qui renforcent la réserve** : le document est « Expired & archived » et « no longer active » ; sa dernière et unique version est la **00, publiée le 16 octobre 2025** ; il s'agit d'une soumission **individuelle**, « not endorsed by the IETF » et « no formal standing », **jamais adoptée par un groupe de travail** (*RFC stream* : *None*).

**Verdict : inchangé, et la réserve se durcit.** ⚠ **Aucune consolidation IETF n'est constatée** — ni à l'IETF 125 ni ailleurs. Le fait que la spécification CSA s'adosse à un texte **expiré et archivé** demeure entier, et le ch. 7 le porte. Le niveau reste [C] jusqu'à extraction citée en **L-01** et **L-05**.

**(b) Spécification CSA « Agent Registry ».** Le socle (H-03) la date du **27 mars 2026**. La page de la spécification porte une **mise à jour au 20 mai 2026** et un **alignement déclaré sur l'OWASP ASI Top 10 (2026)** ; les champs `toolAccessList` et `permissionBoundaries` y demeurent centraux, avec des règles que le socle ne porte pas (l'ajout au `toolAccessList` invalide le profil de confiance ; les `permissionBoundaries` sont exclues par défaut des réponses fédérées).

**Verdict : ÉVOLUÉ.** ⚠ **Le socle hérité est en retard de près de deux mois sur cette source.** Conséquence opérationnelle : **le lot L-05 réinstruit la spécification à sa version courante avant toute rédaction du ch. 7**, et H-03 sera amendée au socle — *amender le socle d'abord, jamais la pièce seule* (PRDPlan §5.2, point 6). Le statut reste **brouillon de *labs***, non une norme ratifiée (R-09).

*Sources : [datatracker.ietf.org — draft-abbey-scim-agent-extension](https://datatracker.ietf.org/doc/draft-abbey-scim-agent-extension/) ; [CSA Labs — Agent Registry Specification](https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/).*

### 2.4 NIST IR 8547 — inchangé, toujours un projet

**Ce que le socle porte** (H-17) : *Initial Public Draft*, avec la réserve du Vol. I lui-même — « dates à re-vérifier, le document étant à l'état de *Initial Public Draft* ».

**Ce que la source montre.** La fiche du NIST donne le document comme **initial public draft**, publié le **12 novembre 2024**, période de commentaires close le **10 janvier 2025**. **Aucune version finale n'est constatée** au 21 juillet 2026.

**Verdict : inchangé.** ⚠ **R-11 s'applique sans atténuation** : l'horloge de toute la Partie V repose sur un **projet**, et *une horloge fondée sur un projet doit dire qu'elle l'est*. Le lot **L-11** conserve sa consigne propre : établir le statut réel, et le dire.

*Piste pour L-11, non vérifiée par cette passe* : un fil de la liste `pqc-forum` du NIST mentionne un identifiant « NISTIR 8647 » portant le même intitulé. **Non instruit ici** — c'est un repérage, pas un fait.

*Source : [csrc.nist.gov/pubs/ir/8547/ipd](https://csrc.nist.gov/pubs/ir/8547/ipd).*

### 2.5 Conventions sémantiques OpenTelemetry — évolué, et la réserve se durcit

**Ce que le socle porte** : statut « expérimental ou stable » à dater au gel (PRD §8.3, lot L-14).

**Ce que les sources montrent.** Deux choses, et la seconde est la plus utile. (1) Les conventions GenAI **ont quitté** le dépôt principal des conventions sémantiques pour un **dépôt dédié** ; la page historique ne porte plus que l'avis de déplacement. (2) Le registre d'attributs affiche, pour **tous** les attributs GenAI — `agent`, `conversation`, `evaluation`, `retrieval` —, le statut **Development**, soit le premier échelon de l'échelle de maturité d'OpenTelemetry (*Development* → *Release Candidate* → *Stable*). **Ni version ni date** ne figurent aux pages consultées.

**Verdict : ÉVOLUÉ.** L'alternative « expérimental ou stable » que posait le PRD est **mal calibrée** : l'échelle réelle en compte trois échelons, et les conventions agentiques sont au premier. ⚠ **Conséquence pour le ch. 24 §24.2** : écrire « les conventions sémantiques GenAI d'OpenTelemetry, à l'état **Development** au [date], dans un dépôt distinct des conventions principales » — et **jamais** « le socle de standardisation de l'observabilité agentique » sans cette qualification. *« Conventions OTel » sans version et sans statut demeure une affirmation vide* : **L-14 doit établir la version, sa date et l'adresse du dépôt dédié.**

*Sources : [opentelemetry.io/docs/specs/semconv/gen-ai/](https://opentelemetry.io/docs/specs/semconv/gen-ai/) ; [registre des attributs GenAI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/).*

### 2.6 Entrée en vigueur du 1ᵉʳ mai 2027 — inchangé, un point de vocabulaire à instruire

**E-23.** Publication le **11 septembre 2025**, entrée en vigueur le **1ᵉʳ mai 2027** : concordant avec H-04. **Verdict : inchangé.**

⚠ **Point à instruire en L-12, et à ne pas trancher ici.** Plusieurs commentaires de cabinets décrivent le délai qui sépare la publication de l'entrée en vigueur comme une « **18-month transition period** », là où le socle porte « **aucune disposition transitoire** ». Les deux énoncés ne sont pas nécessairement contradictoires — *un délai d'entrée en vigueur n'est pas une disposition transitoire au sens du texte* —, mais l'écart de vocabulaire est exactement le genre qu'un chapitre reprend sans le voir. **Il se tranche sur le texte de la ligne directrice, pas sur son commentaire** (règle du « jamais source unique »).

**Ligne directrice IA de l'AMF.** ⚠ **Hors périmètre de cette passe, et volontairement.** La seule ligne de PRD §8.3 qui la vise est l'**entrée en vigueur au 1ᵉʳ mai 2027**, concordante entre les livrables du dépôt. La divergence sur la **date de publication** — 30 mars 2026 au Vol. II, 7 avril 2026 à la veille technologique — est une **divergence non arbitrée** (PRD §7.5) : ce rapport la **signale et ne la tranche pas**. Son instruction relève de **L-12**, avec la lacune 4 (contenu article par article, `lautorite.qc.ca` ayant renvoyé 403 aux outils du Vol. II). **Aucun accès n'a été tenté ici.**

*Sources : [BSIF — Ligne directrice E-23 (2027)](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027) ; [lettre d'accompagnement](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027-letter). Corroboration secondaire : [Blakes](https://www.blakes.com/insights/osfi-releases-final-guideline-e-23-for-model-risk-management-and-ai-use-by-frfis/), [Torys](https://www.torys.com/en/our-latest-thinking/publications/2025/10/osfi-updates-and-expands-scope-of-guideline-e-23), [BLG](https://www.blg.com/en/insights/2025/11/osfi-responds-to-the-growing-use-of-ai-key-updates-to-guideline-e-23).*

### 2.7 Jalons 2030 et 2035 — inchangés

Les jalons portés par IR 8547 demeurent : algorithmes à clé publique vulnérables au quantique (RSA, ECDSA, ECDH, DH en corps fini) **dépréciés après 2030** et **interdits après 2035** ; les modes hybrides restent admis au-delà de 2035 pour accompagner la migration.

**Verdict : inchangé.** ⚠ **R-11 dans les deux sens** : écrire « dépréciation **visée** pour 2030 », « interdiction **visée** pour 2035 », **avec le statut de projet du document qui les porte** (§2.4) — et **jamais** une formule d'obligation légale. ⚠ Les jalons du **décret 14412** et ceux du **Quantum Safe Financial Forum** d'Europol **n'ont pas été revalidés par cette passe** : ils ne figurent pas à PRD §8.3. Ils restent à instruire en L-11, et **ne se fusionnent jamais** avec ceux d'IR 8547.

*Source : [NIST IR 8547 ipd (PDF)](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf). Corroboration secondaire : [Encryption Consulting](https://www.encryptionconsulting.com/education-center/nist-ir-8547-sp-800-131a-algorithm-transitions/), [PQC Mandate Tracker](https://pqcmandates.com/mandate/nist-ir-8547).*

---

## 3. Ce que cette passe n'a pas fait

*Une passe qui ne borne pas son périmètre laisse croire qu'elle l'a couvert.*

1. **Aucune entrée de socle n'est créée.** Les constatations ci-dessus sont des **lectures de pages à une date**, non des extractions citées : elles ne valent ni [B] ni [A]. Le socle propre du volume reste à **0 entrée**.
2. **Aucun lot n'est clos.** Une revalidation n'instruit pas. Elle dit seulement quel lot doit être réinstruit **avant** que le chapitre correspondant ne s'écrive.
3. **Aucune divergence n'est arbitrée** — ni celle d'AP2, ni celle de la date de la ligne directrice de l'AMF (PRD §7.5).
4. **Aucune source secondaire n'est traitée comme primaire.** Les commentaires de cabinets ne servent ici que de corroboration, et sont nommés à chaque emploi.
5. **Les faits hors §8.3 n'ont pas été revalidés** : A2A v1.0.1, Entra Agent ID, AGNTCY, art. 12.1, ACVM 11-348, décret 14412, Quantum Safe Financial Forum. Ils relèvent de leurs lots respectifs et de la **revalidation finale P5.1**.

---

## 4. Conséquences — ce qui doit être fait, et par qui

| # | Conséquence | Où |
|---|---|---|
| 1 | **H-03 est à amender** : le brouillon CSA a évolué (20 mai 2026) ; le socle en reste au 27 mars 2026 | PRD §7.2 — à la clôture de **L-05**, jamais dans le chapitre seul |
| 2 | **L-05 réinstruit la spécification CSA à sa version courante** avant toute rédaction du ch. 7 | Phase P2 |
| 3 | **L-14 établit la version, la date et le dépôt** des conventions OTel ; l'alternative « expérimental / stable » du PRD §8.3 est à remplacer par l'échelle réelle à trois échelons | PRD §8.3 (v0.2) et phase P2 |
| 4 | **Les ch. 2 et 22 écrivent « annoncé au brouillon »**, jamais « publié le 28 juillet 2026 », tant que la version datée n'est pas sortie | R-09, phases P3-P4 |
| 5 | **L-12 tranche sur le texte** le vocabulaire « période de transition » / « disposition transitoire » d'E-23 | Phase P2 |
| 6 | **Revalidation finale P5.1 obligatoire** — ce rapport aura plus de trente jours à la publication, et quatre de ses sept lignes portent une échéance à date indéterminée | Phase P5 |

⚠ **Ce rapport se périme.** Il constate un état au 21 juillet 2026 ; il ne dispense d'aucune des sept revalidations de P5.1, qui reprennent **les sept lignes sans exception**.
