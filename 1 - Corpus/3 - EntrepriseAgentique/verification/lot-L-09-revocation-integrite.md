# Lot L-09 — L-09

| Champ | Valeur |
|---|---|
| Lot | **L-09** — phase **P2**, jalon J-3 |
| Débloque | **ch. 13, 14** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 2 en [A], 0 écartée(s) par le vote. **8 échecs de source** consignés |
| Vote | **3 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **6 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L09-A1` | **[B]** ⚖ | 1 | La page « Authorization » de la révision 2025-11-25 de la spécification du Model Context Protocol ne prescrit aucun mécanisme de révocation de jeton, d'autorisation ou de consentement : les chaînes « revoke », « revocation » et « revoked » sont absentes de l'intégralité de la page, et la RFC 7009 (OAuth 2.0 Token Revocation) ne figure pas parmi les documents de référence qu'elle énumère. |
| `L09-A2` | **[A]** ⚖ | 1 | La page « Tools » de la révision 2025-11-25 de la spécification du Model Context Protocol énumère huit champs pour le type de données « Tool » — name, title, description, icons, inputSchema, outputSchema, annotations, execution — dont aucun n'exprime une version, une empreinte cryptographique ou une signature, et les chaînes « hash », « signature », « integrity », « attestation », « checksum » et « digest » sont absentes de la… |
| `L09-A3` | **[A]** ⚖ | 0 | La RFC 7009 ne fait de l'invalidation des jetons d'accès une conséquence de la révocation d'un jeton de rafraîchissement qu'au titre d'une recommandation (SHOULD), et sa section 5 énonce que si le serveur d'autorisation ne prend pas en charge la révocation des jetons d'accès, ceux-ci ne sont pas immédiatement invalidés lorsque le jeton de rafraîchissement correspondant est révoqué. |
| `L09-A4` | **[B]** | 0 | La RFC 5280, section 3.3, borne la granularité temporelle de la révocation par liste de révocation (CRL) à la période d'émission de celle-ci, période qu'elle donne pour pouvant aller jusqu'à une heure, un jour ou une semaine selon la fréquence retenue. |
| `L09-A5` | **[B]** | 0 | La RFC 6960, section 2.2, énonce que l'état « good » d'une réponse OCSP ne signifie pas nécessairement que le certificat interrogé ait jamais été émis, ni que l'instant de production de la réponse soit compris dans la période de validité de ce certificat. |
| `L09-A6` | **[B]** | 0 | Let's Encrypt a arrêté ses répondeurs OCSP le 6 août 2025, au terme d'un calendrier en trois étapes datées annoncé le 5 décembre 2024, et publie depuis son information de révocation par listes de révocation (CRL) seulement, en invoquant un motif de protection de la vie privée et un motif de charge opérationnelle. |
| `L09-A7` | **[B]** | 1 | La proposition ETDI (Enhanced Tool Definition Interface), qui vise à contrer les attaques de type rug pull et tool poisoning sur le Model Context Protocol par vérification cryptographique d'identité, définitions d'outils versionnées immuables et gestion explicite des permissions appuyée sur OAuth 2.0, est publiée comme préprint arXiv (2506.01333v1, soumis le 2 juin 2025) et ne porte, sur sa notice arXiv consultée le 21 juillet… |
| `L09-A8` | **[C]** | 1 | Le brouillon « Agent Registry Specification » de la Cloud Security Alliance, daté du 27 mars 2026, prescrit quatre états d'agent — active, suspended, deprecated, revoked — et impose à un agent pair de rejeter la requête d'un agent dont le registre indique l'état suspended ou revoked, mais ne fixe aucun délai de propagation, budget de latence ni durée de validité de cache pour un changement d'état. |
| `L09-A9` | **[C]** | 1 | L'Internet-Draft draft-mp-agntcy-ads-01 (« Agent Directory Service », soumis le 24 février 2026, expirant le 28 août 2026, statut visé Informational) fonde l'intégrité de ses enregistrements sur l'adressage par contenu — toute modification produisant un identifiant différent — et ne comporte aucune occurrence des chaînes « revocation », « revoke » ni « revoked ». |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 6 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L09-A1` | **degré injustifié** | Sur la page « Authorization » de la révision 2025-11-25 de la spécification du Model Context Protocol, les chaînes « revoke », « revocation » et « revoked » sont absentes de l'intégralité de la page, et la RFC 7009 (OAuth 2.0 Token Revocation) ne figure pas parmi les documents de référence qu'elle énumère : cette page ne prescrit donc, sous ces termes, aucun mécanisme de révocation de jeton ou d'autorisation. Le bala… |
| `L09-A3` | **négatif de corpus** | La section 2.1 de la RFC 7009 formule l'invalidation des jetons d'accès issus de la même autorisation comme une recommandation (SHOULD), et non comme une exigence (MUST), lorsqu'un jeton de rafraîchissement est révoqué ; sa section 5 énonce que si le serveur d'autorisation ne prend pas en charge la révocation des jetons d'accès, ceux-ci ne sont pas immédiatement invalidés lorsque le jeton de rafraîchissement correspo… |
| `L09-A6` | **clause d'exclusivité** | Let's Encrypt a annoncé le 5 décembre 2024 un calendrier en trois étapes datées de retrait d'OCSP et déclare avoir arrêté ses répondeurs OCSP le 6 août 2025 ; l'organisme indique ne plus distribuer son information de révocation que par listes de révocation (CRL), et motive la décision par la protection de la vie privée et par la charge opérationnelle. |
| `L09-A7` | **promesse non démontrée** | Le préprint arXiv 2506.01333v1 (soumis le 2 juin 2025) expose la proposition ETDI (Enhanced Tool Definition Interface) : ses auteurs la présentent comme visant à contrer les attaques de type rug pull et tool poisoning sur le Model Context Protocol au moyen d'une vérification cryptographique d'identité, de définitions d'outils versionnées, d'une gestion explicite des permissions appuyée sur OAuth 2.0 — propriétés anno… |
| `L09-A8` | **négatif de corpus** | Le brouillon « Agent Registry Specification » de la Cloud Security Alliance, daté du 27 mars 2026, définit quatre états d'agent — active, suspended, deprecated, revoked — et énonce qu'un agent pair rejette la requête d'un agent dont le registre indique l'état suspended ou revoked. Les sections consultées — celle qui définit les états et celle qui définit la conduite de l'agent pair — n'y associent ni délai de propaga… |
| `L09-A9` | **promesse non démontrée** | L'Internet-Draft draft-mp-agntcy-ads-01 (« Agent Directory Service », soumis le 24 février 2026, expirant le 28 août 2026, statut visé Informational) décrit des enregistrements adressés par contenu, dont l'identifiant est dérivé du contenu de l'enregistrement ; le document présente cette dérivation comme faisant qu'une modification produise un identifiant différent, sans en fournir de démonstration ni renvoyer à une… |

## D. Échecs de source consignés (8)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Récupération de la page « AP2 specification » à l'URL annoncée par la recherche | HTTP 404 Not Found. Contourné : l'URL réelle est https://ap2-protocol.org/ap2/specification/, ouverte ensuite avec succès. |
| Reproduction verbatim intégrale de la section 2.1 et de la note d'implémentation de la RFC 7009 | L'outil de récupération a refusé de reproduire les paragraphes complets au motif d'une limite de longueur de citation, et a livré des extraits abrégés. Deux passages courts, suffisants et exacts, ont été obtenus (clause SHOULD de la §2.1, p… |
| Lecture du texte intégral du brouillon « Agent Registry Specification » de la CSA | Seules les réponses ciblées de l'outil de récupération ont été obtenues, jamais le corps complet du document. Le fait négatif sur l'absence de délai de propagation repose donc sur un balayage non contre-vérifié par une seconde passe indépen… |
| Lecture du texte brut de l'Internet-Draft draft-mp-agntcy-ads-01 | Deux passes concordantes par deux chemins d'accès, mais toutes deux exécutées par l'outil de récupération sur une conversion, non par lecture du texte source par l'instructeur. Le rappel du balayage est donc inconnu ; niveau [C] proposé pou… |
| Datation et versionnage de la spécification AP2 | La page ne porte ni date de publication, ni déclaration de statut. La seule marque de version relevée est « (v0.2) » dans un intitulé de section. Le volume ne peut donc pas dater cette source ; toute citation d'AP2 devra dire « version non… |
| Recherche d'un mécanisme normalisé d'attestation d'intégrité à l'exécution pour serveurs d'outils (au-delà de MCP) | Non menée. Le registre officiel MCP, les mécanismes de provenance de paquets (signature, attestations de construction) et les catalogues d'éditeurs n'ont pas été ouverts. Aucune conclusion d'absence n'est tirée : c'est une ABSENCE DE DOCUME… |
| Ouverture du texte intégral du préprint ETDI (PDF) | Seule la notice arXiv a été ouverte (titre, auteurs, dates, catégories, résumé). Le contenu technique de la proposition — ce que sa construction démontrerait, son modèle de menace, ses hypothèses — n'a pas été lu. L09-A7 se borne donc au st… |
| Vérification indépendante de la présence ou de l'absence de dispositions de révocation dans les autres pages de la spécification MCP | Non ouverte, faute de budget d'instruction. Le fait L09-A1 est donc borné à la page « Authorization » et ne doit jamais être présenté comme portant sur la spécification MCP entière. |

## E. Ce que le lot déclare n'avoir pas couvert

CE QUE LE LOT COUVRE — l'inventaire de la révocation, mécanisme par mécanisme, est le livrable ; le voici sous forme de tableau, chaque ligne bornée à ce qui a été ouvert.  \| Mécanisme \| Ce que la spécification PRESCRIT en matière de révocation \| Section lue \| Entrée \| \|---\|---\|---\|---\| \| A2A v1.0.0 \| Interdit (MUST NOT) l'emploi d'une clé expirée ou révoquée, sans définir aucun moyen d'en établir le statut \| §8.4 \| déjà au socle (L-03 : L03-A8, L03-A3-03) — NON REPRIS ICI \| \| MCP, rév. 2025-11-25, page Authorization \| Rien : aucune occurrence de « revoke/revocation/revoked » ; RFC 7009 non citée ; la seule limitation temporelle prescrite est la durée de vie courte des jetons (SHOULD) \| page entière \| L09-A1 \| \| MCP, rév. 2025-11-25, page Tools \| Rien sur l'intégrité : le type Tool n'a ni version, ni empreinte, ni signature ; le changement de liste à l'exécution est notifié sans contrôle prescrit \| page entière \| L09-A2 \| \| AP2 (non daté, v0.2) \| Rien : « revoke/revocation/revoked/status list/expiry/expiration/expires/lifetime/cancel » absents de la page de spécification ; la seule borne temporelle est une RECOMMANDATION de fixer le claim `exp` au plus court. La page « Agent Authorization Framework » ne porte non plus aucun de ces termes \| pages /ap2/specification/ et /ap2/agent_authorization/ \| non érigé en affirmation (voir ci-dessous) \| \| Registre CSA (brouillon, 27 mars 2026) \| Quatre états dont « revoked » ; rejet imposé au pair ; point de terminaison /v1/verify — mais aucun délai de propagation ni TTL \| §6 et protocole de vérification inter-agents \| L09-A8 \| \| Registre AGNTCY (I-D 01, expire le 28 août 2026) \| Rien : adressage par contenu, aucune occurrence des chaînes de révocation \| document entier, deux passes \| L09-A9 \| \| OAuth — RFC 7009 \| Point de terminaison de révocation spécifié ; invalidation des jetons d'accès en SHOULD seulement ; non-invalidation immédiate déclarée en §5 \| §2.1 et §5 \| L09-A3 \| \| X.509 — RFC 5280 (CRL) \| Révocation pleinement spécifiée, latence structurelle déclarée par la RFC elle-même (jusqu'à une semaine) \| §3.3 \| L09-A4 \| \| X.509 — RFC 6960 (OCSP) \| Statut en ligne spécifié ; l'état « good » ne démontre ni l'émission, ni la validité \| §2.2 \| L09-A5 \|  CE QUE LE LOT N'A PAS COUVERT, ET POURQUOI.  1. AP2 — le relevé (zéro occurrence de neuf chaînes de révocation et d'expiration sur deux pages) N'EST PAS érigé en affirmation. Motif : la page ne porte ni date ni déclaration de statut, le balayage n'a pas été contre-vérifié par une seconde passe, et le volume porte déjà une divergence non arbitrée sur la gouvernance d'AP2 (PRD §7.5) qu'un fait négatif fragile aggraverait. À reprendre en L-06, avec double passe et sur le texte source. Consigné ici comme piste, non comme fait.  2. Aucune clause d'exclusivité n'a été écrite. Le lot ne dit nulle part qu'un mécanisme est « le seul » à prescrire ou à ne pas prescrire la révocation : chaque ligne du tableau est bornée à ce qui a été ouvert, et l'inventaire n'est PAS exhaustif — SPIFFE/SVID, les listes d'état de justificatifs du W3C (Bitstring Status List), OpenID for Verifiable Credentials, les jetons de transaction et les mécanismes propriétaires (Entra Agent ID) n'ont pas été instruits.  3. Le volet (a) — attestation d'intégrité à l'exécution — est instruit par la NÉGATIVE côté protocole (L09-A2) et par la PROPOSITION côté littérature (L09-A7). Il n'a PAS été instruit côté chaîne d'approvisionnement : provenance de paquets, attestations de construction, registres signés. Le lot ne conclut donc rien sur l'existence ou l'absence d'un mécanisme d'attestation disponible : c'est une absence de documentation (degré 3) dans le corpus consulté.  4. Le volet (d) — précédent PKI — repose sur trois pièces : la latence déclarée de la CRL (L09-A4), la portée limitée de la réponse OCSP (L09-A5) et l'abandon d'OCSP par un opérateur majeur pour motif de coût (L09-A6). Le vote du CA/Browser Forum rendant OCSP facultatif, la révocation de masse consécutive à Heartbleed et le mouvement vers les certificats de courte durée n'ont PAS été instruits : la thèse du chapitre 14 pourra s'appuyer sur trois pièces, pas sur une tendance établie.  5. GARDE-FOU DE DUALITÉ D'USAGE (R-12) — régime de rédaction déclaré. Le traitement du rug pull se tient au niveau du maillon : la définition d'outil est le support de la décision d'invocation, le protocole autorise son remplacement après l'octroi de la confiance, et il ne prescrit aucun réexamen — ce qui cède, et pourquoi. Les sources ouvertes par ce lot sont des textes normatifs, des pages de spécification et une notice de préprint (§F) ; le texte intégral du préprint ETDI, seule pièce du lot portant un modèle de menace, n'a pas été ouvert (§D). ⚠ La conformité de ce rapport à R-12 ne s'atteste pas depuis ce rapport : elle relève de la relecture CA-12, distincte du rédacteur et consignée sous verification/.  6. FORMULATIONS IMPOSÉES pour tout emploi de ces entrées (R-02) — écrire que la RFC 7009 SPÉCIFIE un point de terminaison de révocation, jamais qu'elle « garantit » la révocation ; qu'une réponse OCSP « good » DÉMONTRE l'absence d'inscription au registre du répondeur interrogé, jamais qu'elle « atteste » le certificat ; que l'adressage par contenu d'AGNTCY DÉMONTRE la non-modification d'un enregistrement, jamais sa validité courante. Et R-03 : ETDI est une proposition d'auteurs en préprint, jamais une extension du protocole.

## F. Sources et citations

### `L09-A1` — [B]

La page « Authorization » de la révision 2025-11-25 de la spécification du Model Context Protocol ne prescrit aucun mécanisme de révocation de jeton, d'autorisation ou de consentement : les chaînes « revoke », « revocation » et « revoked » sont absentes de l'intégralité de la page, et la RFC 7009 (OAuth 2.0 Token Revocation) ne figure pas parmi les documents de référence qu'elle énumère.

**Balayage (degré 1)** — Fait négatif de DEGRÉ 1, borné à UNE page nommée d'UNE révision nommée, récupérée intégralement le 21 juillet 2026 (de « # Authorization » jusqu'à la section terminale « MCP Authorization Extensions »). Chaînes cherchées sur le texte retourné : « revoke », « revocation », « revoked » — zéro occurrence. La section « Standards Compliance » énumère cinq documents : OAuth 2.1 IETF DRAFT (draft-ietf-oauth-v2-1-13), RFC 8414, RFC 7591, RFC 9728, draft-ietf-oauth-client-id-metadata-document-00. Les autres RFC citées ailleurs dans la page sont 8707, 6750, 3986 et 9068. La RFC 7009 n'apparaît à aucun de ces endroits. Le seul dispositif de limitation temporelle prescrit est l'émission de jetons d'accès de courte durée (SHOULD) et la rotation des jetons de rafraîchissement pour les clients publics (MUST).

- **primaire** — Model Context Protocol — Specification — Authorization (révision 2025-11-25) — révision 2025-11-25 (identifiée par les liens internes de la page vers…, consultée le 2026-07-21 — <https://modelcontextprotocol.io/specification/latest/basic/authorization>
  > Authorization servers SHOULD issue short-lived access tokens to reduce the impact of leaked tokens.
- **primaire** — Model Context Protocol — Specification — Authorization (révision 2025-06-18) — révision 2025-06-18, consultée le 2026-07-21 — <https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization>
  > OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728))

**Réserve** — Le balayage porte sur la conversion markdown renvoyée par l'outil de récupération, non sur le source HTML brut : une occurrence perdue à la conversion n'est pas exclue. Le fait est borné à cette page ; il ne dit RIEN des autres pages de la spécification (Security Best Practices, Basic, Server), ni des extensions d'autorisation référencées en fin de page (dépôt modelcontextprotocol/ext-auth), qui n'ont pas été ouvertes. Ne jamais élargir en « MCP ne traite pas la révocation ».

### `L09-A2` — [A]

La page « Tools » de la révision 2025-11-25 de la spécification du Model Context Protocol énumère huit champs pour le type de données « Tool » — name, title, description, icons, inputSchema, outputSchema, annotations, execution — dont aucun n'exprime une version, une empreinte cryptographique ou une signature, et les chaînes « hash », « signature », « integrity », « attestation », « checksum » et « digest » sont absentes de la page.

**Balayage (degré 1)** — Fait négatif de DEGRÉ 1, borné à UNE page nommée d'UNE révision nommée, récupérée intégralement le 21 juillet 2026. L'énumération sous « Data Types > Tool » est close et compte huit entrées. Chaînes cherchées et absentes : « hash », « signature », « integrity », « attestation », « checksum », « digest ». (La chaîne « sign » n'a PAS été retenue comme discriminante : elle est présente comme sous-chaîne de « designed ».) La page prévoit par ailleurs que la liste d'outils change à l'exécution — capacité « listChanged », notification « notifications/tools/list_changed », diagramme de flux « Server--)Client: tools/list_changed » suivi d'un nouveau « tools/list » — sans qu'aucune étape de comparaison, de re-consentement ou de vérification d'intégrité ne soit prescrite. La section « Security Considerations » de la page compte deux listes (cinq obligations serveur en MUST, cinq recommandations client en SHOULD) dont aucune ne porte sur l'intégrité ou la stabilité des définitions d'outils.

- **primaire** — Model Context Protocol — Specification — Tools — révision 2025-11-25, consultée le 2026-07-21 — <https://modelcontextprotocol.io/specification/2025-11-25/server/tools>
  > For trust & safety and security, clients MUST consider tool annotations to be untrusted unless they come from trusted servers.
- **primaire** — Model Context Protocol — Specification — Tools — List Changed Notification — révision 2025-11-25, consultée le 2026-07-21 — <https://modelcontextprotocol.io/specification/2025-11-25/server/tools>
  > When the list of available tools changes, servers that declared the listChanged capability SHOULD send a notification

**Réserve** — MAILLON QUI CÈDE (niveau architectural, sans recette) : la définition d'outil est le support de la décision d'invocation, et le protocole autorise le serveur à la remplacer après l'octroi de la confiance sans prescrire de la relier à ce qui avait été consenti. La spécification renvoie la décision au client par une réserve — « clients MUST consider tool annotations to be untrusted unless they come from trusted servers » — sans définir comment cette confiance s'établit ni comment elle se réévalue après un changement. R-02 : dire que la spécification NE PRESCRIT PAS de contrôle d'intégrité ; ne jamais écrire qu'elle « ne permet pas » d'en faire un hors protocole. Borné à cette page : ne dit rien du registre MCP officiel ni des mécanismes de distribution (paquets signés, provenance) hors protocole, non instruits.

### `L09-A3` — [A]

La RFC 7009 ne fait de l'invalidation des jetons d'accès une conséquence de la révocation d'un jeton de rafraîchissement qu'au titre d'une recommandation (SHOULD), et sa section 5 énonce que si le serveur d'autorisation ne prend pas en charge la révocation des jetons d'accès, ceux-ci ne sont pas immédiatement invalidés lorsque le jeton de rafraîchissement correspondant est révoqué.

**Balayage (degré 0)** — Affirmation positive, adossée à deux passages du texte normatif ouvert le 21 juillet 2026 : la clause SHOULD de la section 2.1 et la phrase de la section 5 (Security Considerations). La note d'implémentation de la section 2.1 confirme que le traitement dépend de l'architecture (jetons auto-portants contre références opaques) et propose comme solution de rechange l'émission de jetons d'accès de courte durée.

- **primaire** — RFC 7009 — OAuth 2.0 Token Revocation — Proposed Standard, août 2013, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc7009.html>
  > If the particular token is a refresh token...the authorization server SHOULD also invalidate all access tokens based on the same authorization grant.
- **primaire** — RFC 7009 — OAuth 2.0 Token Revocation, section 5 (Security Considerations) — Proposed Standard, août 2013, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc7009.html>
  > If the authorization server does not support access token revocation, access tokens will not be immediately invalidated when the corresponding refresh token is revoked.

**Réserve** — R-02 : la RFC 7009 SPÉCIFIE un point de terminaison de révocation ; elle ne DÉMONTRE aucune propagation de la révocation vers les serveurs de ressources, qu'elle laisse hors de son périmètre. C'est le siège textuel de l'asymétrie émission/révocation : l'émission est un MUST outillé de bout en bout, l'invalidation en aval un SHOULD conditionné à une capacité facultative du serveur d'autorisation. L'incident UNC6395 (révocation en masse des jetons Drift le 20 août 2025, déjà au socle par L-08) en est le corrélat opérationnel.

### `L09-A4` — [B]

La RFC 5280, section 3.3, borne la granularité temporelle de la révocation par liste de révocation (CRL) à la période d'émission de celle-ci, période qu'elle donne pour pouvant aller jusqu'à une heure, un jour ou une semaine selon la fréquence retenue.

**Balayage (degré 0)** — Affirmation positive, adossée au texte normatif ouvert le 21 juillet 2026, bornée à la section 3.3 (« Revocation »). Deux passages concordants : l'énoncé de périodicité et l'énoncé de la limitation qui en découle.

- **primaire** — RFC 5280 — Internet X.509 Public Key Infrastructure Certificate and CRL Profile, section 3.3 (Revocation) — Proposed Standard, mai 2008, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc5280.html>
  > the time granularity of revocation is limited to the CRL issue period
- **primaire** — RFC 5280, section 3.3 — périodicité d'émission — Proposed Standard, mai 2008, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc5280.html>
  > A new CRL is issued on a regular periodic basis (e.g., hourly, daily, or weekly).

**Réserve** — Précédent PKI applicable au chapitre 14 : un mécanisme de révocation pleinement spécifié depuis 2008 porte, dans son propre texte, la reconnaissance de sa latence structurelle. R-02 : la CRL DÉMONTRE l'état de révocation au moment de l'émission de la liste, non à l'instant de la vérification.

### `L09-A5` — [B]

La RFC 6960, section 2.2, énonce que l'état « good » d'une réponse OCSP ne signifie pas nécessairement que le certificat interrogé ait jamais été émis, ni que l'instant de production de la réponse soit compris dans la période de validité de ce certificat.

**Balayage (degré 0)** — Affirmation positive, adossée au texte normatif ouvert le 21 juillet 2026, bornée à la section 2.2 (« Response »). La même section porte la réserve symétrique sur l'état « revoked », qui peut être renvoyé alors même que l'autorité n'a jamais émis de certificat portant ce numéro de série.

- **primaire** — RFC 6960 — X.509 Internet PKI Online Certificate Status Protocol (OCSP), section 2.2 — Proposed Standard, juin 2013, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc6960.html>
  > This state does not necessarily mean that the certificate was ever issued or that the time at which the response was produced is within the certificate's validity interval.
- **primaire** — RFC 6960, section 2.2 — état « revoked » — Proposed Standard, juin 2013, consultée le 2026-07-21 — <https://www.rfc-editor.org/rfc/rfc6960.html>
  > This state MAY also be returned if the associated CA has no record of ever having issued a certificate with the certificate serial number in the request.

**Réserve** — R-02, et c'est le cœur de l'emploi qui en sera fait : un point de terminaison de statut DÉMONTRE l'absence d'inscription au registre de révocation du répondeur interrogé ; il ne démontre ni l'émission, ni la validité, ni l'identité. Transposition au chapitre 14 : un registre d'agents qui répond « actif » ne démontre pas davantage. Ne pas écrire qu'OCSP « atteste » le certificat.

### `L09-A6` — [B]

Let's Encrypt a arrêté ses répondeurs OCSP le 6 août 2025, au terme d'un calendrier en trois étapes datées annoncé le 5 décembre 2024, et publie depuis son information de révocation par listes de révocation (CRL) seulement, en invoquant un motif de protection de la vie privée et un motif de charge opérationnelle.

**Balayage (degré 0)** — Deux billets officiels de l'autorité de certification elle-même, ouverts le 21 juillet 2026 : l'annonce du 5 décembre 2024 (calendrier prospectif à l'époque : 30 janvier 2025, 7 mai 2025, 6 août 2025) et le billet du 6 août 2025 qui en constate l'exécution. Le PROGRAMMÉ de 2024 est donc devenu un fait constaté ; il se cite comme fait, non comme prévision.

- **primaire** — Ending OCSP Support in 2025 — 5 décembre 2024, consultée le 2026-07-21 — <https://letsencrypt.org/2024/12/05/ending-ocsp/>
  > For every year that we have existed, operating OCSP services has taken up considerable resources
- **primaire** — OCSP Service Has Reached End of Life — 6 août 2025, consultée le 2026-07-21 — <https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life/>
  > Going forward, we will publish revocation information exclusively via Certificate Revocation Lists (CRLs).

**Réserve** — MÉTRIQUE AUTO-DÉCLARÉE, à attribuer à sa source À CHAQUE occurrence : Let's Encrypt déclare avoir traité, au pic de son service, « approximately 340 billion OCSP requests per month ». Ce chiffre est celui de l'opérateur, non d'un mesureur tiers. Le précédent porté au chapitre 14 est celui du COÛT de l'infrastructure de révocation en temps quasi réel : l'exploitant le plus volumineux du web public a jugé ce coût non soutenable et est revenu à un mécanisme de latence bornée (CRL). Portée bornée : un opérateur, ses motifs déclarés — ne pas généraliser en « OCSP est abandonné » ; la RFC 6960 n'est ni retirée ni obsolète.

### `L09-A7` — [B]

La proposition ETDI (Enhanced Tool Definition Interface), qui vise à contrer les attaques de type rug pull et tool poisoning sur le Model Context Protocol par vérification cryptographique d'identité, définitions d'outils versionnées immuables et gestion explicite des permissions appuyée sur OAuth 2.0, est publiée comme préprint arXiv (2506.01333v1, soumis le 2 juin 2025) et ne porte, sur sa notice arXiv consultée le 21 juillet 2026, aucune référence de publication en revue ni en actes de conférence.

**Balayage (degré 1)** — STATUT PRÉ-NORMATIF, dit en toutes lettres : préprint arXiv, version unique v1, catégories cs.CR / cs.AI / cs.ET, champ « Comments » : 11 pages, 10 figures. Aucun champ « Journal ref » n'est porté sur la notice ; le seul DOI est celui, automatique, du dépôt arXiv (10.48550/arXiv.2506.01333). Le fait négatif est de DEGRÉ 1 borné à la notice arXiv de cet identifiant, et à elle seule : il n'établit pas qu'aucune version n'ait été publiée ailleurs sous un autre titre.

- **primaire** — ETDI: Mitigating Tool Squatting and Rug Pull Attacks in Model Context Protocol (MCP) by using OAuth-Enhanced T… — arXiv:2506.01333v1 [cs.CR], soumis le 2 juin 2025, consultée le 2026-07-21 — <https://arxiv.org/abs/2506.01333>
  > ETDI incorporates cryptographic identity verification, immutable versioned tool definitions, and explicit permission management, often leveraging OAuth 2.0.

**Réserve** — ETDI est une PROPOSITION D'AUTEURS, non une extension adoptée : ne jamais l'invoquer comme un mécanisme disponible, ni comme la position du projet MCP. R-02 : le préprint PROPOSE des définitions versionnées immuables et une vérification d'identité ; le lot n'a pas ouvert son texte intégral et n'établit donc rien de ce que sa construction démontrerait. Les auteurs déclarent des affiliations à des fournisseurs d'infonuagique dans le texte du préprint (non vérifié ici) ; à traiter en neutralité fournisseur (§8.4).

### `L09-A8` — [C]

Le brouillon « Agent Registry Specification » de la Cloud Security Alliance, daté du 27 mars 2026, prescrit quatre états d'agent — active, suspended, deprecated, revoked — et impose à un agent pair de rejeter la requête d'un agent dont le registre indique l'état suspended ou revoked, mais ne fixe aucun délai de propagation, budget de latence ni durée de validité de cache pour un changement d'état.

**Balayage (degré 1)** — STATUT PRÉ-NORMATIF : document déclaré « Draft », daté du 2026-03-27, hébergé dans l'espace « Lab Space » de la CSA ; il ne se déclare pas normatif. La partie positive (les quatre états, la clause de rejet, le point de terminaison /v1/verify, le comportement du verbe DELETE) est adossée à des citations verbatim obtenues du document. La partie négative — absence de délai de propagation — est de DEGRÉ 1 revendiqué SUR CE SEUL DOCUMENT, mais elle repose sur un balayage effectué par l'outil de récupération et non sur une lecture du texte intégral par l'instructeur : elle est proposée en [C] à ce titre.

- **primaire** — Agent Registry Specification (Draft) — Draft, 2026-03-27, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > If the status is `suspended` or `revoked`, Agent A must reject the request and log the attempted interaction.
- **primaire** — Agent Registry Specification (Draft) — énumération des états et verbe DELETE — Draft, 2026-03-27, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > Deactivate an agent (sets status to deprecated; records are retained for audit purposes)

**Réserve** — ⚠ Ne pas confondre deux verbes du même document : DELETE ne révoque pas — « Deactivate an agent (sets status to deprecated; records are retained for audit purposes) ». Le passage à « revoked » est un acte distinct. ⚠ Une valeur de « moins de 30 secondes » de propagation circule dans des résumés secondaires attribués à la CSA ; elle N'A PAS été retrouvée dans ce document et ne doit pas lui être imputée. Point d'architecture pour le chapitre 14 : prescrire un état de révocation et prescrire sa fraîcheur sont deux choses, et seule la première est ici faite — un pair qui interroge un registre sans borne de fraîcheur peut accepter une délégation d'un agent révoqué depuis un temps non spécifié.

### `L09-A9` — [C]

L'Internet-Draft draft-mp-agntcy-ads-01 (« Agent Directory Service », soumis le 24 février 2026, expirant le 28 août 2026, statut visé Informational) fonde l'intégrité de ses enregistrements sur l'adressage par contenu — toute modification produisant un identifiant différent — et ne comporte aucune occurrence des chaînes « revocation », « revoke » ni « revoked ».

**Balayage (degré 1)** — STATUT PRÉ-NORMATIF, dit avec sa date d'expiration réelle : Internet-Draft, version 01, auteurs Luca Muscariello et Ramiz Polic, soumis le 24 février 2026, expirant le 28 août 2026, actif au 21 juillet 2026, statut visé Informational — le texte porte la formule « This Internet-Draft will expire on 28 August 2026. » Le balayage a été mené DEUX FOIS, par deux chemins d'accès indépendants (fiche datatracker et rendu HTML sur ietf.org), avec des résultats concordants : zéro occurrence de « revocation », « revoke », « revoked ». La seconde passe a également relevé zéro occurrence de « delete », « deletion » et « unpublish », et une occurrence unique de « status » (renvoi procédural) et de « expire » (la clause d'expiration).

- **primaire** — Agent Directory Service — draft-mp-agntcy-ads-01 — Internet-Draft version 01, soumis le 24 février 2026, expire le 28 aoû…, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-mp-agntcy-ads/01/>
  > This Internet-Draft will expire on 28 August 2026.
- **primaire** — Agent Directory Service — draft-mp-agntcy-ads-01 (rendu HTML) — Internet-Draft version 01, 24 février 2026, consultée le 2026-07-21 — <https://www.ietf.org/archive/id/draft-mp-agntcy-ads-01.html>
  > Content identifiers are cryptographically derived from the data they represent, ensuring that any modification results in a different identifier.

**Réserve** — Fait négatif de DEGRÉ 1 revendiqué SUR CE SEUL DOCUMENT — l'Internet-Draft version 01 — et non sur la documentation AGNTCY, qui est un corpus distinct où des opérations de suppression sont documentées ailleurs (docs.agntcy.org, non ouvert ici). Ne jamais élargir en « AGNTCY ne documente pas la révocation » : c'est exactement la forme d'affirmation qu'un vote antérieur du volume a écartée (L08-A5-8). Les deux balayages ont été exécutés par l'outil de récupération, non par lecture du texte brut par l'instructeur : d'où le niveau [C] proposé. Point d'architecture : l'adressage par contenu DÉMONTRE qu'un enregistrement n'a pas été modifié ; il ne dit rien de sa validité courante — un enregistrement immuable ne se révoque pas, il ne peut qu'être supplanté, et le draft ne prescrit pas comment un lecteur apprend qu'il l'a été.

