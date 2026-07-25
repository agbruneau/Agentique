# Lot L-01 — Identité machine héritée et étirement des RFC (OAuth 2.0, SCIM, jetons de transaction, WIMSE, SPIFFE/SPIRE)

| Champ | Valeur |
|---|---|
| Lot | **L-01** — phase **P2**, jalon J-3 |
| Débloque | **ch. 1, 2** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 2 en [A], 0 écartée(s) par le vote. **3 échecs de source** consignés |
| Vote | **2 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **3 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L01-A1` | **[B]** | 0 | RFC 6749 (OAuth 2.0, octobre 2012), section 1.1, définit le détenteur de ressource (*resource owner*) comme une entité quelconque, et réserve explicitement le terme *end-user* au cas où cette entité est une personne ; le rôle de *client* y est défini comme celui d'une application agissant pour le compte du détenteur de ressource et avec son autorisation. |
| `L01-A2` | **[A]** ⚖ | 0 | Le flux de code d'autorisation de RFC 6749 présuppose un agent utilisateur (*user-agent*) interposé : la section 4.1.1 prescrit que le client dirige le détenteur de ressource vers l'URI construite au moyen d'une redirection HTTP ou d'un autre moyen disponible via l'agent utilisateur, et le flux de la section 4.1 fait authentifier ce détenteur par le serveur d'autorisation via cet agent utilisateur. |
| `L01-A3` | **[B]** | 1 | La section 4 de RFC 7643 (SCIM Core Schema, septembre 2015), qui annonce définir « les schémas de ressource par défaut présents dans un serveur SCIM », ne comporte que trois sous-sections — 4.1 « User » Resource Schema, 4.2 « Group » Resource Schema, 4.3 Enterprise User Schema Extension — et aucune ne définit de type de ressource pour un mandataire logiciel autonome. |
| `L01-A4` | **[B]** | 0 | Les descriptions d'attributs du schéma « User » de RFC 7643 sont libellées en termes de personne : l'attribut `title` de la section 4.1.1 est décrit comme « The user's title, such as "Vice President". » et l'attribut `employeeNumber` de l'extension Enterprise User (section 4.3) comme un identifiant « assigned to a person, typically based on order of hire ». |
| `L01-A5` | **[A]** ⚖ | 0 | Au 21 juillet 2026, `draft-ietf-oauth-transaction-tokens` en est à sa version **09**, datée du 6 juillet 2026, expirant le **7 janvier 2027**, à l'état datatracker « In WG Last Call » dans le groupe de travail OAuth ; il s'agit d'un Internet-Draft en cours, non d'un RFC. |
| `L01-A6` | **[B]** | 0 | Au 21 juillet 2026, la page des documents du groupe de travail WIMSE recense sept Internet-Drafts de groupe de travail, tous non publiés en RFC : `arch-08` (6 juill. 2026, exp. 7 janv. 2027, I-D Exists), `http-signature-05` (20 juill. 2026, exp. 21 janv. 2027, I-D Exists), `identifier-03` (6 juill. 2026, exp. 7 janv. 2027, I-D Exists), `mutual-tls-02` (6 juill. 2026, exp. 7 janv. 2027, I-D actif), `workload-creds-02` (2 juill.… |
| `L01-A7` | **[B]** | 0 | La section 3.4.11 de `draft-ietf-wimse-arch-08` (6 juillet 2026, expirant le 7 janvier 2027, visée Informational) range les systèmes d'IA agentique parmi les charges de travail déléguées : « From WIMSE perspective, AI intermediaries are a special case of delegated workloads. » |
| `L01-A8` | **[B]** | 0 | La spécification SPIFFE-ID (statut « Stable ») définit l'identité SPIFFE comme un URI conforme à RFC 3986 composé d'un nom de domaine de confiance et d'un chemin, et le SVID comme le mécanisme par lequel une charge de travail communique son identité ; la validité d'un SVID y est établie par le seul fait qu'il a été signé par une autorité du domaine de confiance de l'identité SPIFFE. |
| `L01-A9` | **[B]** | 0 | La CNCF classe SPIFFE et SPIRE au niveau de maturité « Graduated » : sa page projet SPIFFE date ce passage du 23 août 2022 et sa page projet SPIRE du 22 août 2022, les deux projets ayant été acceptés à la CNCF le 29 mars 2018 et passés en « Incubating » le 22 juin 2020. |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 3 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L01-A4` | **clause d'exclusivité** | Au moins deux descriptions d'attributs du schéma « User » de RFC 7643 sont libellées en termes de personne : l'attribut `title` (section 4.1.1) est décrit comme « The user's title, such as "Vice President". » et l'attribut `employeeNumber` de l'extension Enterprise User (section 4.3) comme un identifiant « assigned to a person, typically based on order of hire ». |
| `L01-A7` | **verbe excessif** | La section 3.4.11 de `draft-ietf-wimse-arch-08` (Internet-Draft du 6 juillet 2026, expirant le 7 janvier 2027, visée Informational) énonce, du point de vue WIMSE, que les intermédiaires d'IA (*AI intermediaries*) sont un cas particulier de charges de travail déléguées : « From WIMSE perspective, AI intermediaries are a special case of delegated workloads. » |
| `L01-A8` | **clause d'exclusivité** | La spécification SPIFFE-ID (statut « Stable ») définit l'identité SPIFFE comme un URI conforme à RFC 3986 composé d'un nom de domaine de confiance et d'un chemin, et le SVID comme le document par lequel une charge de travail atteste son identité ; elle énonce qu'un SVID est considéré valide s'il a été signé par une autorité du domaine de confiance de l'identité SPIFFE qu'il porte. |

## D. Échecs de source consignés (3)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Communiqué de graduation SPIFFE/SPIRE de la CNCF — devait servir à recouper la date divergente (22 vs 23 août 2022) entre les deux pages projet | HTTP 404 Not Found au 21 juillet 2026 (URL vraisemblablement périmée ou renommée ; aucune recherche de l'URL de remplacement n'a été menée dans ce lot) |
| Interruption d'outillage en début de lot : six appels WebFetch/WebSearch consécutifs refusés | Indisponibilité temporaire du classificateur de sûreté de l'outil (« claude-sonnet-5[1m] is temporarily unavailable »), levée après attente ; un appel curl de contournement a par ailleurs été refusé par le système de permissions. Aucune don… |
| Vérification du numéro de sous-section exact de la phrase « The authorization server authenticates the resource owner (via the user-agent)… » de RFC 6749 | L'outil de rendu l'a rattachée tantôt à l'étape (B) du flux de la section 4.1, tantôt à la section 4.1.2, sans stabilité entre deux interrogations. Le rattachement fin n'est pas établi ; consigné en caveat de L01-A2 plutôt qu'affirmé. |

## E. Ce que le lot déclare n'avoir pas couvert

Non couvert par ce lot, et pourquoi. (1) **RFC 6749 section 4.4 (client credentials grant)** : relevée et citable (« The client can request an access token using only its client credentials … when the client is requesting access to the protected resources under its control, or those of another resource owner that have been previously arranged with the authorization server »), mais écartée du lot faute de place sous le plafond de neuf affirmations ; c'est le complément le plus direct de L01-A2 pour le chapitre 2 et elle devrait être reprise. (2) **RFC 7644 (protocole SCIM)** non ouvert : les constats SCIM de ce lot portent sur le seul schéma de base. (3) **Les drafts individuels (non-WG) apparentés à WIMSE** — la page du groupe en listait une dizaine, dont un consacré à l'identité des agents d'IA et un à la délégation inter-organisationnelle — n'ont été ni ouverts ni énumérés : un draft individuel n'est pas un document de groupe de travail, et les confondre fausserait l'état de l'art du chapitre 1. (4) **Spécifications SPIFFE autres que SPIFFE-ID** (Workload API, X509-SVID, JWT-SVID, fédération) non ouvertes : ce que SPIFFE établit est ici borné au document SPIFFE-ID. (5) **Aucune métrique d'adoption ou de déploiement** n'a été cherchée, pour aucun des objets du lot ; « Graduated » est un niveau de maturité de fondation et ne dit rien du déploiement en entreprise. (6) **Aucune extrapolation** n'a été faite des dates d'expiration : elles sont recopiées des fiches, jamais calculées. (7) Le relevé des sept drafts WIMSE est **horodaté et périssable** — `draft-ietf-wimse-wpt-01` expire le 3 septembre 2026 et `draft-ietf-oauth-transaction-tokens-09` le 7 janvier 2027 : toute rédaction du chapitre 2 postérieure à septembre 2026 doit rejouer L01-A5 et L01-A6 avant citation.

## F. Sources et citations

### `L01-A1` — [B]

RFC 6749 (OAuth 2.0, octobre 2012), section 1.1, définit le détenteur de ressource (*resource owner*) comme une entité quelconque, et réserve explicitement le terme *end-user* au cas où cette entité est une personne ; le rôle de *client* y est défini comme celui d'une application agissant pour le compte du détenteur de ressource et avec son autorisation.

**Balayage (degré 0)** — Texte intégral de RFC 6749 ouvert sur rfc-editor.org (versions .txt et .html) le 21 juillet 2026 ; lecture ciblée de la section 1.1 « Roles » et relevé des deux définitions.

- **primaire** — RFC 6749 — The OAuth 2.0 Authorization Framework — RFC 6749, Standards Track, octobre 2012, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc6749.txt>
  > An entity capable of granting access to a protected resource. When the resource owner is a person, it is referred to as an end-user.
- **primaire** — RFC 6749 — The OAuth 2.0 Authorization Framework, section 1.1 (Roles) — RFC 6749, octobre 2012, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc6749.html>
  > An application making protected resource requests on behalf of the resource owner and with its authorization.

**Réserve** — La définition n'exclut pas formellement un détenteur de ressource non humain ; ce qui est établi ici est la dissymétrie lexicale (entité / personne), pas une interdiction. L'endroit où l'hypothèse humaine devient opérante est le flux de la section 4.1 (voir L01-A2), pas la section 1.1.

### `L01-A2` — [A]

Le flux de code d'autorisation de RFC 6749 présuppose un agent utilisateur (*user-agent*) interposé : la section 4.1.1 prescrit que le client dirige le détenteur de ressource vers l'URI construite au moyen d'une redirection HTTP ou d'un autre moyen disponible via l'agent utilisateur, et le flux de la section 4.1 fait authentifier ce détenteur par le serveur d'autorisation via cet agent utilisateur.

**Balayage (degré 0)** — RFC 6749 ouvert le 21 juillet 2026 ; lecture des sections 4.1, 4.1.1 et 4.1.2, avec vérification de rattachement demandée deux fois à l'outil de rendu.

- **primaire** — RFC 6749 — The OAuth 2.0 Authorization Framework, section 4.1.1 (Authorization Request) — RFC 6749, octobre 2012, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc6749.html>
  > The client directs the resource owner to the constructed URI using an HTTP redirection response, or by other means available to it via the user-agent.
- **primaire** — RFC 6749 — The OAuth 2.0 Authorization Framework, flux de la section 4.1 (Authorization Code Grant) — RFC 6749, octobre 2012, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc6749.txt>
  > The authorization server authenticates the resource owner (via the user-agent) and establishes whether the resource owner grants or denies the client's access request.

**Réserve** — Le rattachement de section a été vérifié deux fois et n'est stable que pour la première phrase (section 4.1.1). L'outil de rendu a rattaché la seconde phrase (« The authorization server authenticates the resource owner (via the user-agent)… ») tantôt à l'étape (B) du flux de la section 4.1, tantôt à la section 4.1.2 : citer cette seconde phrase en nommant « le flux de la section 4.1 », et re-constater le numéro exact de sous-section sur le texte avant toute citation fine.

### `L01-A3` — [B]

La section 4 de RFC 7643 (SCIM Core Schema, septembre 2015), qui annonce définir « les schémas de ressource par défaut présents dans un serveur SCIM », ne comporte que trois sous-sections — 4.1 « User » Resource Schema, 4.2 « Group » Resource Schema, 4.3 Enterprise User Schema Extension — et aucune ne définit de type de ressource pour un mandataire logiciel autonome.

**Balayage (degré 1)** — Texte de RFC 7643 ouvert sur rfc-editor.org (.txt et .html) le 21 juillet 2026 ; relevé de la phrase d'ouverture de la section 4 et de l'énumération complète de ses intitulés de sous-sections (4.1, 4.2, 4.3).

- **primaire** — RFC 7643 — System for Cross-domain Identity Management: Core Schema — RFC 7643, Standards Track, septembre 2015, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc7643.txt>
  > This section defines the default resource schemas present in a SCIM server.
- **primaire** — RFC 7643 — SCIM Core Schema, section 4.1 — RFC 7643, septembre 2015, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc7643.html>
  > SCIM provides a resource type for "User" resources.

**Réserve** — Fait négatif borné à l'énumération des sous-sections de la section 4 de RFC 7643 seule. Il ne dit rien de RFC 7644 (protocole SCIM), rien des extensions de schéma enregistrées ailleurs, rien des profils propriétaires, et rien d'un éventuel travail SCIM postérieur. Le balayage porte sur des intitulés de sous-sections, non sur toutes les occurrences du corpus SCIM.

### `L01-A4` — [B]

Les descriptions d'attributs du schéma « User » de RFC 7643 sont libellées en termes de personne : l'attribut `title` de la section 4.1.1 est décrit comme « The user's title, such as "Vice President". » et l'attribut `employeeNumber` de l'extension Enterprise User (section 4.3) comme un identifiant « assigned to a person, typically based on order of hire ».

**Balayage (degré 0)** — RFC 7643 ouvert le 21 juillet 2026 ; relevé verbatim des descriptions de name, displayName, nickName, profileUrl, title, userType, preferredLanguage, locale, timezone (section 4.1.1) et de employeeNumber, manager, organization (section 4.3).

- **primaire** — RFC 7643 — SCIM Core Schema, section 4.1.1 (Singular Attributes) — RFC 7643, septembre 2015, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc7643.html>
  > The user's title, such as "Vice President".
- **primaire** — RFC 7643 — SCIM Core Schema, section 4.3 (Enterprise User Schema Extension) — RFC 7643, septembre 2015, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc7643.html>
  > A string identifier, typically numeric or alphanumeric, assigned to a person, typically based on order of hire or association with an organization.

**Réserve** — Constat de sémantique rédactionnelle, non d'interdiction normative : rien dans RFC 7643 n'interdit de peupler ces attributs pour une entité non humaine. L'affirmation porte sur le libellé des descriptions, pas sur une contrainte de validation.

### `L01-A5` — [A]

Au 21 juillet 2026, `draft-ietf-oauth-transaction-tokens` en est à sa version **09**, datée du 6 juillet 2026, expirant le **7 janvier 2027**, à l'état datatracker « In WG Last Call » dans le groupe de travail OAuth ; il s'agit d'un Internet-Draft en cours, non d'un RFC.

**Balayage (degré 0)** — Page datatracker du document et de sa version 09 ouvertes le 21 juillet 2026, puis texte source `draft-ietf-oauth-transaction-tokens-09.txt` sur ietf.org ouvert pour constater l'en-tête et la clause d'expiration.

- **primaire** — draft-ietf-oauth-transaction-tokens-09 — fiche datatracker — version 09, 6 juillet 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/09/>
  > Active Internet-Draft (oauth WG) … In WG Last Call
- **primaire** — Transaction Tokens (Txn-Tokens), draft-ietf-oauth-transaction-tokens-09 — 6 juillet 2026, consultée le 2026-07-21 — <https://www.ietf.org/archive/id/draft-ietf-oauth-transaction-tokens-09.txt>
  > This Internet-Draft will expire on 7 January 2027.
- **primaire** — Transaction Tokens (Txn-Tokens) — Abstract — draft-09, 6 juillet 2026, consultée le 2026-07-21 — <https://www.ietf.org/archive/id/draft-ietf-oauth-transaction-tokens-09.txt>
  > Transaction Tokens (Txn-Tokens) are designed to maintain and propagate user identity, workload identity and authorization context throughout the Call Chain within a trusted domain during the processing of external requests (e.g. such as API calls) or requests initiated internally within the Trust Domain.

**Réserve** — Divergence de métadonnée à consigner telle quelle : l'en-tête du texte porte « Intended status: Standards Track », tandis que la fiche datatracker de la version 09 affiche « Intended RFC Status: (None) ». Le document remplace `draft-oauth-transaction-tokens`. « In WG Last Call » est un état de groupe de travail, non une approbation IESG ni une publication.

### `L01-A6` — [B]

Au 21 juillet 2026, la page des documents du groupe de travail WIMSE recense sept Internet-Drafts de groupe de travail, tous non publiés en RFC : `arch-08` (6 juill. 2026, exp. 7 janv. 2027, I-D Exists), `http-signature-05` (20 juill. 2026, exp. 21 janv. 2027, I-D Exists), `identifier-03` (6 juill. 2026, exp. 7 janv. 2027, I-D Exists), `mutual-tls-02` (6 juill. 2026, exp. 7 janv. 2027, I-D actif), `workload-creds-02` (2 juill. 2026, exp. 3 janv. 2027, I-D actif), `wpt-01` (2 mars 2026, exp. **3 septembre 2026**, I-D actif) et `workload-identity-practices-05` (30 juin 2026, exp. 1er janv. 2027), seul de la série à porter l'état « Submitted to IESG for Publication », en visée Informational.

**Balayage (degré 0)** — Page https://datatracker.ietf.org/wg/wimse/documents/ ouverte le 21 juillet 2026, puis fiche datatracker ouverte individuellement pour chacun des sept documents afin d'y relever version, date, date d'expiration et état.

- **primaire** — WIMSE — Workload Identity in Multi System Environments, documents du groupe de travail — état au 21 juillet 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/wg/wimse/documents/>
  > draft-ietf-wimse-workload-identity-practices-05 … Submitted to IESG for Publication
- **primaire** — draft-ietf-wimse-wpt — WIMSE Workload Proof Token — version 01, 2 mars 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-ietf-wimse-wpt/>
  > Active Internet-Draft (wimse WG)
- **primaire** — draft-ietf-wimse-http-signature — WIMSE Workload-to-Workload Authentication with HTTP Signatures — version 05, 20 juillet 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/>
  > I-D Exists

**Réserve** — Relevé horodaté au 21 juillet 2026 et périssable : `wpt-01` expire le 3 septembre 2026, soit six semaines après la consultation. Les fiches affichent « Intended RFC Status: (None) » pour plusieurs documents dont l'en-tête porte « Intended status: Standards Track » ; la divergence est de métadonnée et se cite telle quelle. La page listait en outre des drafts individuels (non-WG) apparentés, non énumérés ici. Aucune date de publication en RFC n'est annoncée pour aucun des sept.

### `L01-A7` — [B]

La section 3.4.11 de `draft-ietf-wimse-arch-08` (6 juillet 2026, expirant le 7 janvier 2027, visée Informational) range les systèmes d'IA agentique parmi les charges de travail déléguées : « From WIMSE perspective, AI intermediaries are a special case of delegated workloads. »

**Balayage (degré 0)** — Texte `draft-ietf-wimse-arch-08.txt` ouvert sur ietf.org le 21 juillet 2026 ; relevé de l'en-tête, de la clause d'expiration, de la définition de *workload* et des phrases de la section 3.4.11 « AI and ML-Based Intermediaries ».

- **primaire** — Workload Identity in a Multi System Environment (WIMSE) Architecture, draft-ietf-wimse-arch-08, section 3.4.11… — draft-08, 6 juillet 2026, consultée le 2026-07-21 — <https://www.ietf.org/archive/id/draft-ietf-wimse-arch-08.txt>
  > From WIMSE perspective, AI intermediaries are a special case of delegated workloads.
- **primaire** — draft-ietf-wimse-arch-08 — définition de *workload* et clause d'expiration — draft-08, 6 juillet 2026, consultée le 2026-07-21 — <https://www.ietf.org/archive/id/draft-ietf-wimse-arch-08.txt>
  > A workload is an independently addressable and executable software entity. … This Internet-Draft will expire on 7 January 2027.

**Réserve** — Énoncé d'un Internet-Draft en cours (état « I-D Exists »), non d'une norme : il ne fait autorité sur rien et sa formulation peut changer à la révision suivante. La section 3.4.11 est une section d'architecture, pas une prescription protocolaire.

### `L01-A8` — [B]

La spécification SPIFFE-ID (statut « Stable ») définit l'identité SPIFFE comme un URI conforme à RFC 3986 composé d'un nom de domaine de confiance et d'un chemin, et le SVID comme le mécanisme par lequel une charge de travail communique son identité ; la validité d'un SVID y est établie par le seul fait qu'il a été signé par une autorité du domaine de confiance de l'identité SPIFFE.

**Balayage (degré 0)** — Document `standards/SPIFFE-ID.md` du dépôt github.com/spiffe/spiffe ouvert en version brute le 21 juillet 2026 ; relevé des définitions d'identité SPIFFE, de SVID, de domaine de confiance, et de la mise en garde de la section 4.1.1 sur les assertions.

- **primaire** — The SPIFFE Identity and Verifiable Identity Document — branche main, statut « Stable », consulté le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/spiffe/spiffe/main/standards/SPIFFE-ID.md>
  > A SPIFFE Verifiable Identity Document (SVID) is the mechanism through which a workload communicates its identity to a resource or caller. … An SVID is considered valid if it has been signed by an authority within the SPIFFE ID's trust domain.
- **primaire** — The SPIFFE Identity and Verifiable Identity Document — section 4.1.1 — branche main, consulté le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/spiffe/spiffe/main/standards/SPIFFE-ID.md>
  > The name of a service owner, role or group membership, and access policies are all examples of assertions that are more likely to change between the time of SVID issuance and the time of validation or use.

**Réserve** — Ce que la spécification démontre est une vérification de signature dans un domaine de confiance, non une preuve de propriété d'une entité ni une décision d'autorisation. Le document met lui-même en garde contre les assertions susceptibles de changer entre l'émission et l'usage. Deux réserves de méthode : le document ne définit pas formellement le terme *workload*, et il n'énonce pas explicitement ce que la vérification d'un SVID n'établit pas — cette dernière absence est de degré 3 (rien trouvé), pas un fait négatif.

### `L01-A9` — [B]

La CNCF classe SPIFFE et SPIRE au niveau de maturité « Graduated » : sa page projet SPIFFE date ce passage du 23 août 2022 et sa page projet SPIRE du 22 août 2022, les deux projets ayant été acceptés à la CNCF le 29 mars 2018 et passés en « Incubating » le 22 juin 2020.

**Balayage (degré 0)** — Pages cncf.io/projects/spiffe/ et cncf.io/projects/spire/ ouvertes le 21 juillet 2026, chacune interrogée deux fois avec consigne de reproduction littérale de la phrase de parcours du projet.

- **primaire** — SPIFFE — page projet CNCF — consulté le 21 juillet 2026, consultée le 2026-07-21 — <https://www.cncf.io/projects/spiffe/>
  > SPIFFE was accepted to CNCF on March 29, 2018, moved to the Incubating maturity level on June 22, 2020, and then moved to the Graduated maturity level on August 23, 2022.
- **primaire** — SPIRE — page projet CNCF — consulté le 21 juillet 2026, consultée le 2026-07-21 — <https://www.cncf.io/projects/spire/>
  > SPIRE was accepted to CNCF on March 29, 2018, moved to the Incubating maturity level on June 22, 2020, and then moved to the Graduated maturity level on August 22, 2022.

**Réserve** — Divergence d'un jour entre les deux pages de la CNCF elle-même (23 août pour SPIFFE, 22 août pour SPIRE), reproduite ici telle quelle et non arbitrée. La page d'annonce de graduation (cncf.io/announcements/2022/08/22/…) a renvoyé un HTTP 404 le 21 juillet 2026 : la date n'a donc pas pu être recoupée sur le communiqué. « Graduated » est un niveau de maturité de fondation, non une mesure d'adoption en entreprise.

