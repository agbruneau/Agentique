# Lot L-03 — La carte d'agent signée : ancrage, révocation, gouvernance des clés

| Champ | Valeur |
|---|---|
| Lot | **L-03**, déclaré **bloquant au sens fort** ([PRD](../prd/PRD.md) §7.6) — sans lui, le ch. 5 n'a pas d'objet |
| Question instruite | **Q3 du Vol. II, ch. 21 §21.2** — « Que vaut cryptographiquement une carte d'agent signée ? » |
| Ce qu'il devait établir | L'ancrage de confiance, le régime de révocation et la gouvernance des clés — **ou l'établissement que la spécification ne les documente pas** |
| Date d'instruction | **21 juillet 2026** — quatre axes menés en parallèle (format et chaîne de signature ; ancrage ; révocation et durée de vie ; gouvernance des clés hors spécification) |
| Sources | Spécification A2A v1.0.0 (`docs/specification.md`), définition Protobuf normative (`specification/a2a.proto`), `SECURITY.md`, `GOVERNANCE.md`, registre des versions et suivi d'incidents du dépôt `a2aproject/A2A` |
| Vérification | **Vote adversarial à trois juges** sur chaque affirmation centrale — lentilles *fidélité à la source*, *statut et datation*, *qualification logique*. Chaque juge est chargé de **réfuter**, non de valider ; le doute non levé profite à la réfutation |
| Résultat | **32 affirmations** — **11 en [A]** (trois juges, aucune réfutation), **16 en [B]**, **5 écartées par le vote**. **19 échecs de source consignés** |
| Statut du lot | ☑ **CLOS. Q3 est instruite, et sa réponse est défavorable au mécanisme.** |

---

## 1. Réponse à Q3, en une phrase

> **La signature d'une Agent Card A2A démontre qu'un détenteur de clé a signé une carte canonicalisée. Elle ne démontre rien de plus.** La spécification **renvoie l'ancrage hors du protocole** — dispositif hors-bande facultatif et non spécifié (F-09) —, **n'outille pas la révocation** (F-06), et le `SECURITY.md` du dépôt **ne porte aucune disposition de gouvernance des clés** (F-08). Elle porte en outre une contradiction interne : elle **interdit** d'employer une clé révoquée sans fournir **aucun moyen d'établir qu'elle l'est** (F-07).

⚠ **Formulation corrigée à la relecture P1.4.** La première rédaction de cette réponse écrivait « aucun ancrage de confiance opposable, aucun régime de révocation, aucune gouvernance des clés » — **trois négatifs de corpus**, dont deux reprenaient la substance d'affirmations que le vote avait **écartées 3-0** (`L03-A2-2`, `L03-A4-02`). *Le rapport débordait son propre socle, qui, lui, se tenait.* La leçon du §6 s'appliquait d'abord à la synthèse du §1 : **un fait négatif borné tient, un fait négatif de corpus tombe** — y compris quand c'est le rédacteur du lot qui l'écrit.

⚠ **Formulation imposée pour tout emploi de ce résultat** (R-02) : la carte signée **démontre** l'intégrité de son contenu relativement à une clé ; elle **ne documente ni** l'appartenance de cette clé à une organisation, **ni** son statut de révocation à l'instant de la vérification. Proscrire « garantit », « prouve l'identité », « atteste ». *L'ouvrage naît de Q3 ; il ne peut pas reproduire la faute que Q3 dénonce.*

## 2. Ce que la spécification démontre

Quatre acquis, tous en **[A]**, tous adossés au texte normatif :

- **Le format est spécifié avec soin.** Signature JWS au sens du RFC 7515 ; canonicalisation **obligatoire** du contenu selon le JSON Canonicalization Scheme du RFC 8785 avant signature ; exclusion **obligatoire** du champ `signatures` lui-même du contenu signé, « to avoid circular dependencies » (`L03-A5`).
- **La charge utile n'est pas transportée** : l'entrée de signature est construite selon la formule du RFC 7515, et le vérificateur doit **reconstruire** la charge en re-canonicalisant la carte reçue (`L03-A6`). ⚠ La spécification ne nomme jamais ce dispositif « detached » et ne désigne aucune des sérialisations du RFC 7515 : le mécanisme est décrit sans être rattaché à son vocabulaire d'origine.
- **La structure est close à trois membres** — `protected`, `signature`, `header` — sans membre de charge utile (`L03-A2`).
- **L'en-tête protégé est énuméré** : `alg`, `typ`, `kid` obligatoires, `jku` seul paramètre facultatif nommé (`L03-A7`).

*Le soin apporté au format rend le reste plus remarquable, non moins : ce n'est pas un mécanisme bâclé, c'est un mécanisme complet sur ce qu'il couvre et muet sur ce qu'il ne couvre pas.*

## 3. Ce que la spécification ne documente pas — trois faits négatifs vérifiés

**Degré 1 au sens du PRD §8.6** : l'absence est établie par le balayage documenté d'un texte ouvert, et chaque balayage nomme son document, sa version, sa date et les chaînes cherchées.

| Ce qui manque | Constat | Réf. |
|---|---|---|
| **Toute validité temporelle de la signature** | L'énumération normative de l'en-tête JWS protégé ne comporte aucun paramètre temporel — ni `nbf`, ni `iat`, ni `exp`. Une signature d'Agent Card ne périme pas | `L03-A7` **[A]** |
| **Toute validité ou statut de la carte** | Le message `AgentCard` de la définition Protobuf normative compte **quatorze champs**, dont aucun n'exprime une date d'émission, une expiration, une fenêtre de validité ni un indicateur de révocation | `L03-A3-04` **[A]** |
| **Tout moyen d'établir le statut d'une clé** | La §8.4 ne mentionne ni liste de révocation, ni OCSP, ni CRL, ni point de terminaison de statut, ni chaîne de certificats, ni délai de re-validation ; la procédure de vérification en six étapes ne comporte **aucune étape de contrôle de statut ou de fraîcheur** | `L03-A3-03` **[A]** |

## 4. La contradiction interne, et c'est le résultat le plus fort du lot

Deux énoncés de la même section, tous deux en **[A]** :

> « Expired or revoked keys **MUST NOT** be used for verification » — §8.4.3, *Security Considerations* (`L03-A3-02`)

et l'établissement qu'**aucun mécanisme ne permet au client de savoir qu'une clé est expirée ou révoquée** (`L03-A8`, `L03-A3-03`).

⚠ **C'est le cas typique du mécanisme nommé sans être défini** : l'obligation est posée en toutes lettres, au niveau normatif le plus fort du vocabulaire RFC 2119 ; la procédure qui permettrait de s'y conformer est absente. Un implémenteur qui respecte la lettre de la spécification **ne peut pas** établir qu'il la respecte. ⚠ Noter que l'interdiction porte sur la **clé**, non sur la **carte** (`L03-A3-02`) : une carte signée demeure vérifiable indéfiniment tant que sa clé est réputée valide.

**La rotation, elle, est outillée** — plusieurs signatures peuvent être portées par une même carte —, mais sans procédure de retrait d'une clé compromise (`L03-A8`). *Une pile qui sait ajouter une clé et ne sait pas en retirer une reproduit l'asymétrie que le ch. 14 prend pour objet.*

## 5. Le régime de confiance réel

- **La signature est facultative et sa vérification n'est que recommandée** : les cartes **MAY** être signées ; les clients **SHOULD** vérifier au moins une signature avant d'accorder confiance (`L03-A3`, **[A]**). ⚠ **Conséquence, et elle est structurante pour tout l'ouvrage** : une chaîne A2A **entièrement conforme** peut ne comporter aucune signature apposée ni aucune vérification effectuée.
- **L'ancrage est renvoyé hors du protocole.** La récupération de la clé publique passe par `kid` et `jku`, ou par un magasin de clés de confiance côté client que les clients « **MAY** maintain » — facultatif et non spécifié (`L03-A2-5`, **[B]**). ⚠ **Tension interne relevée** : la procédure de vérification fait reposer la récupération de la clé sur « the `kid` and `jku` », alors que `jku` n'est que **facultatif** dans l'en-tête protégé (`L03-A7`).
- **Le `SECURITY.md` ne porte aucune disposition de gouvernance des clés.** Il tient en deux phrases et ne décrit qu'une procédure de signalement de vulnérabilité (`L03-A4-01`, **[A]**, degré 1 — balayage exhaustif par construction, le document entier tenant en trois lignes). La charte de gouvernance n'attribue à aucun organe une responsabilité de gestion des clés (`L03-A4-07`, **[B]**). ⚠ **Énoncé borné à la relecture P1.4** : dire que « la gouvernance des clés n'existe pas comme document » serait un **négatif de corpus**, et c'est précisément ce que le vote a écarté 3-0 en `L03-A4-02`. Ce que le lot établit porte sur **les documents qu'il a ouverts**, nommés un à un.

## 6. Ce que le vote a écarté — et pourquoi c'est le résultat le plus instructif

**Cinq affirmations sur trente-deux ont été écartées**, et elles ont un trait commun : **ce sont toutes des faits négatifs trop larges**.

- « La spécification ne contient aucune occurrence de *trust anchor*, *issuer*, *x5c*, *x5u*, *jku*, *federation* » — **réfutée 3-0** : `jku` y figure, et c'est précisément le mécanisme de découverte de clés.
- « La découverte de clé repose exclusivement sur `kid` et `jku`, sans aucun mécanisme protocolaire » — **réfutée 3-0**.
- « Le projet ne publie, hors spécification, ni modèle de menace, ni document de sécurité » — **réfutée 3-0**.
- « Aucun des sept documents balayés ne mentionne la rotation ni la révocation des clés » — **réfutée 3-0** : la rotation **est** nommée, par le dispositif des signatures multiples.

**Règle qui en découle, et qui vaut pour tout le volume** : *un fait négatif borné à une section nommée tient ; un fait négatif de corpus tombe.* Les trois faits négatifs retenus au §3 ci-dessus sont bornés — une section, un fichier, une énumération. Les cinq écartés portaient sur « la spécification », « le projet », « les sept documents ». **La différence n'est pas de prudence rédactionnelle : elle est de vérifiabilité.**

## 7. Ce que ce lot ne permet pas de dire

1. **Rien sur la v1.0.1.** Le registre des versions du dépôt porte une étiquette **v1.0.1 publiée le 28 mai 2026**, postérieure à la v1.0.0 lue, alors que l'en-tête du document de spécification déclare « Latest Released Version 1.0.0 ». **L'écart est consigné, non arbitré** ; la v1.0.1 n'a pas été ouverte (échec de source déclaré). ⚠ **À reprendre en P5.1.**
2. **Rien sur la §8.6 « Caching ».** Normative et existante, elle n'a pas pu être ouverte : le récupérateur tronque le document. Elle pourrait porter des exigences de fraîcheur qui nuanceraient le §3.
3. **Aucun balayage hors ligne.** Le téléchargement local des fichiers a été refusé par le bac à sable d'exécution ; les balayages ont été conduits dans le DOM des pages rendues et sur les fichiers bruts. ⚠ **Réserve de méthode déclarée par l'instruction elle-même** : sur un test de contrôle, le récupérateur distant a rapporté un décompte incomplet. Les degrés 1 de ce lot reposent sur la **convergence de plusieurs balayages indépendants**, non sur un seul.
4. **Rien sur les implémentations.** Le lot porte sur ce que la spécification prescrit, jamais sur ce que les trousses de développement font.

## 8. Conséquences opposables

| Pièce | Ce que ce lot y impose |
|---|---|
| **ch. 5** | Le chapitre a son objet, et sa thèse est **confirmée par le texte** : la signature vaut ce que valent son ancrage, sa révocation et sa gouvernance des clés — trois éléments que la spécification documente **inégalement**, et pour deux d'entre eux **pas du tout**. Le §5.4 rend le verdict par la grille : la carte répond à **Q-A partiellement** (identifiant vérifiable mais non révocable) et **ne répond ni à Q-B** (aucun ancrage) **ni à Q-C** |
| **ch. 8** | ⚠ **La première des quatre pièces du passeport n'apporte pas ce que l'assemblage lui demande.** Le §8.1 le dit : le passeport ne peut pas hériter d'un ancrage que la carte ne porte pas |
| **ch. 14** | L'asymétrie émission/révocation, thèse du chapitre, est **établie sur pièce** pour A2A : émission spécifiée en six étapes, révocation interdite d'usage mais jamais outillée |
| **ch. 17** | `alg` est un paramètre d'en-tête, sans plancher ni liste : la crypto-agilité de la carte est **structurellement présente** (§17.2) |
| **Lacune n° 1** (PRD §10) | **Instruite et close.** Elle s'écrit désormais au gabarit **« passe conduite »**, et non plus au gabarit « aucune passe conduite » |

---

## A. Relevé des affirmations retenues (27)

Niveau : **[A]** = trois juges, aucune réfutation ; **[B]** = extraction citée, ou vote non unanime, ou vote incomplet. Degré : 0 = affirmation positive ; 1 = fait négatif **vérifié** (balayage documenté) ; 2 = fait négatif **établi** ; 3 = **absence de documentation**.

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L03-A1` | **[B]** | 0 | Dans le modèle de données A2A, le champ de l'AgentCard qui porte les signatures se nomme « signatures » et est un tableau répété d'objets AgentCardSignature, déclaré non requis. |
| `L03-A2` | **[A]** | 1 | La structure AgentCardSignature comporte exactement trois membres — « protected » (requis, chaîne), « signature » (requis, chaîne) et « header » (facultatif, objet) — et ne comporte aucun membre « payload ». |
| `L03-A2-1` | **[A]** | 0 | La spécification A2A définit la signature de l'Agent Card comme une signature JSON Web Signature (RFC 7515) calculée sur une forme canonicalisée de la carte selon le JSON Canonicalization Scheme (RFC 8785), la liste `signatures` elle-même étant exclue du contenu signé. |
| `L03-A2-5` | **[B]** | 0 | Le seul dispositif d'ancrage hors-bande prévu par la procédure de vérification de la spécification A2A est facultatif et non spécifié : la spécification énonce que les clients « MAY maintain a trusted key store for known agent providers » sans en définir ni la provenance, ni le format, ni les critères d'inscription. |
| `L03-A2-6` | **[B]** | 1 | La spécification A2A interdit l'emploi de clés expirées ou révoquées pour la vérification d'une Agent Card mais ne définit aucun mécanisme de révocation ni de publication d'état de révocation : la chaîne « revocation » est absente du document et « revoked » n'y apparaît qu'une seule fois, dans l'énoncé de l'interdiction elle-même. |
| `L03-A2-7` | **[B]** | 2 | La documentation officielle A2A porte une réserve explicite d'absence sur les registres d'agents : elle déclare que la spécification en vigueur ne prescrit aucune API normalisée pour les registres curés, qui seraient la voie naturelle d'un ancrage de confiance tiers. |
| `L03-A2-8` | **[B]** | 0 | L'absence de mécanisme protocolaire de vérification de l'authenticité d'une Agent Card est reconnue comme question ouverte au dépôt officiel A2A : l'issue #1672, ouverte le 22 mars 2026 et non close au 21 juillet 2026, énonce qu'un agent qui découvre l'Agent Card d'un autre ne dispose d'aucun mécanisme de niveau protocolaire pour en vérifier l'authenticité. |
| `L03-A3` | **[A]** | 0 | La spécification A2A qualifie la signature d'une Agent Card de JSON Web Signature au sens du RFC 7515, en pose l'apposition comme facultative (« MAY ») et n'exige de la part du client qu'une recommandation (« SHOULD ») de vérifier au moins une signature avant d'accorder confiance à la carte. |
| `L03-A3-01` | **[B]** | 1 | Dans la spécification A2A v1.0.0 (§8.4.2), l'en-tête JWS protégé d'une signature d'Agent Card ne comporte aucun paramètre temporel : les paramètres imposés sont alg, typ et kid, et le seul paramètre facultatif nommé est jku. |
| `L03-A3-02` | **[A]** | 0 | La spécification A2A v1.0.0 pose une interdiction normative d'employer une clé expirée ou révoquée pour vérifier une signature d'Agent Card, et cette interdiction porte sur la clé de signature, non sur la carte elle-même. |
| `L03-A3-03` | **[A]** | 1 | La spécification A2A v1.0.0 impose de ne pas employer une clé expirée ou révoquée sans définir, en §8.4, aucun moyen d'en établir le statut : la section ne mentionne ni liste de révocation, ni OCSP, ni CRL, ni point de terminaison de statut, ni chaîne de certificats, ni délai de re-validation, et la procédure de vérification en six étapes ne comporte aucune étape de contrôle de statut ou de fraîcheur. |
| `L03-A3-04` | **[A]** | 1 | Le message AgentCard de la définition Protobuf normative d'A2A comporte quatorze champs, dont aucun n'exprime une validité temporelle ou un statut : ni date d'émission, ni date d'expiration, ni fenêtre de validité, ni indicateur de révocation. |
| `L03-A3-05` | **[B]** | 1 | Le message AgentCardSignature de la définition Protobuf normative d'A2A ne comporte que trois champs — protected (requis), signature (requis) et header (facultatif) — et aucun champ de validité, d'expiration, de numéro de série ou de statut. |
| `L03-A3-06` | **[B]** | 1 | Le seul dispositif de rotation de clé prévu par la §8.4 de la spécification A2A v1.0.0 est la faculté de porter plusieurs signatures sur une même Agent Card ; la section ne prescrit ni procédure de rotation, ni période de recouvrement, ni périodicité. |
| `L03-A3-07` | **[B]** | 0 | Depuis la version 1.0 d'A2A, le schéma JSON a2a.json n'est pas normatif : il est un artefact de compilation dérivé du fichier a2a.proto, non versionné dans le dépôt et régénéré à chaque construction de la documentation. |
| `L03-A3-08` | **[B]** | 0 | Le guide de découverte d'A2A (documentation d'accompagnement, non normative) rattache la fraîcheur d'un Agent Card à la sémantique de cache HTTP — en-tête Cache-Control avec max-age, ETag dérivé du champ version ou d'une empreinte de contenu, requêtes conditionnelles — et renvoie à la section 8.6 de la spécification pour les exigences normatives. |
| `L03-A4` | **[B]** | 0 | La version de la spécification A2A lue est la 1.0.0, publiée le 12 mars 2026 selon le registre des versions du dépôt officiel, et le champ « signatures » de l'AgentCard y a été introduit à la version 0.3.0, publiée le 30 juillet 2025. |
| `L03-A4-01` | **[A]** | 1 | Le fichier SECURITY.md publié à la racine du dépôt a2aproject/A2A tient en deux phrases et ne décrit qu'une procédure de signalement de vulnérabilité — courriel à security@lists.a2aproject.org, puis coordination et divulgation par GitHub Security Advisory ; il ne comporte aucune disposition sur la génération, la conservation, la rotation, la compromission ou la révocation de clés de signature. |
| `L03-A4-03` | **[B]** | 1 | Le seul document thématique du projet A2A consacré au déploiement en entreprise, docs/topics/enterprise-ready.md, borne son propos à TLS, authentification, autorisation, confidentialité des données, traçabilité et gestion d'API, et ne traite en aucun point de la gouvernance des clés de signature d'Agent Card. |
| `L03-A4-05` | **[B]** | 0 | La documentation « What's New in A2A Protocol v1.0 » du projet A2A indique que la vérification de signature d'Agent Card repose sur JWS avec canonicalisation JSON et que la clé publique de vérification est récupérée soit par l'en-tête `jku`, soit depuis des keystores tenus pour de confiance. |
| `L03-A4-06` | **[B]** | 0 | Le projet Agent2Agent est gouverné par un Technical Steering Committee dont la charte publiée attribue huit sièges nominatifs à Google, Microsoft, Cisco, Amazon Web Services, Salesforce, ServiceNow, SAP et IBM, les décisions se prenant par vote à la majorité des membres présents sous condition de quorum ; l'hébergement du projet par la Linux Foundation a été annoncé le 23 juin 2025. |
| `L03-A4-07` | **[B]** | 1 | La charte du projet A2A (GOVERNANCE.md) n'attribue à aucun organe une responsabilité de gestion des clés : sa seule mention de sécurité range la politique de signalement d'incident parmi les prérogatives du Technical Steering Committee. |
| `L03-A4-08` | **[B]** | 1 | Les points d'entrée de signalement de vulnérabilité divergent d'un dépôt à l'autre de l'organisation a2aproject : le dépôt de spécification renvoie à security@lists.a2aproject.org, les SDK Python et JavaScript renvoient au programme de Google (g.co/vulnz), le SDK Java renvoie à quatre adresses individuelles chez Red Hat, et le SDK Go ne publie aucun SECURITY.md. |
| `L03-A5` | **[A]** | 0 | La spécification A2A impose (« MUST ») que le contenu de l'Agent Card soit canonicalisé selon le JSON Canonicalization Scheme du RFC 8785 avant signature, et que le champ « signatures » lui-même soit exclu du contenu signé. |
| `L03-A6` | **[A]** | 1 | La charge utile signée n'est pas transportée dans l'objet AgentCardSignature — l'entrée de signature est construite selon la formule ASCII(BASE64URL(UTF8(JWS Protected Header)) \|\| '.' \|\| BASE64URL(JWS Payload)) et le vérificateur doit reconstruire cette charge en re-canonicalisant la carte reçue — sans que la spécification nomme ce dispositif « detached » ni ne désigne laquelle des sérialisations du RFC 7515 elle emploie. |
| `L03-A7` | **[A]** | 1 | L'énumération normative des paramètres de l'en-tête JWS protégé d'une Agent Card A2A comprend « alg », « typ » et « kid » comme obligatoires et « jku » comme seul paramètre facultatif nommé, et ne comporte aucun paramètre de validité temporelle de la signature. |
| `L03-A8` | **[A]** | 1 | La spécification A2A interdit (« MUST NOT ») l'emploi de clés expirées ou révoquées pour la vérification d'une Agent Card sans définir de mécanisme permettant au client d'établir l'expiration ou la révocation d'une clé. |

## B. Affirmations écartées par le vote (5)

*Trois juges de lentilles distinctes, chargés de **réfuter** et non de valider. Écartée à deux réfutations sur trois.* ⚠ **Ces écarts sont un résultat du lot, pas un déchet de production** : chacun est une affirmation qui aurait passé une relecture ordinaire.

### `L03-A2-2` — écartée, 3 réfutations sur 3

> Le texte de la spécification A2A ne contient aucune occurrence des chaînes « trust anchor », « root of trust », « issuer », « x5c », « x5u », « jwks_uri », « federation » ni « federated » : la spécification ne définit ni autorité d'émission, ni racine de confiance, ni chaîne de certificats, ni fédération pour les clés de signature des Agent Cards.

- **qualification logique** — Réfutation sur trois plans.  (1) DEGRÉ NON JUSTIFIÉ. Le degré 1 exige un balayage documenté d'un texte réellement ouvert. La preuve déclare elle-même que le balayage a été délégué à l'agent d'extraction de l'outil web, sans commande locale reproductible. Les « deux passes indépendantes » ne le sont pas : même médiateur, même document, même mode de défaillance. Degré 3 au mieux ; déclarer 1 est en soi une réfutation (PRD §8.6, R-14).  (2) LE MÉDIATEUR PRODUIT DES ZÉROS FAUX — constaté, non supposé. Contre-vérification menée à l'instant sur deux URL : sur https://a2a-protocol.org/latest/specification/ l'extraction…
- **fidélité à la source** — Refutation sur trois motifs, dont un decisif constate sur piece. (1) Glissement source/affirmation : la §8.4 de la specification A2A (signature des Agent Cards, JWS RFC 7515 + canonicalisation JCS RFC 8785) definit explicitement une decouverte de cles de signature — en-tete protege avec `kid` et `jku` decrit comme « URL to JSON Web Key Set (JWKS) containing the public key », etape de verification « Retrieve the public key using the `kid` and `jku` (or from a trusted key store) », plus « Public keys SHOULD be retrieved over secure channels (HTTPS) », « Clients MAY maintain a trusted key store for known agent provi…
- **statut et datation** — Réfutation partielle, sur trois défauts constatés sur la source primaire elle-même (docs/specification.md, branche main, récupérée le 21 juillet 2026 ; contrôle par trois interrogations indépendantes du texte brut). 1) CONTRE-EXEMPLE DANS LA CITATION MÊME : la seule citation invoquée à l'appui — « validating its TLS certificate against trusted certificate authorities (CAs) during the TLS handshake » — nomme une autorité d'émission et une validation de chaîne de certificats. La proposition « la spécification ne définit ni autorité d'émission... ni chaîne de certificats » est donc fausse telle qu'énoncée ; elle n'e…

### `L03-A2-3` — écartée, 3 réfutations sur 3

> La découverte de la clé publique de vérification d'une Agent Card signée repose exclusivement sur deux paramètres d'en-tête JWS empruntés à la RFC 7515 — `kid`, requis, et `jku`, optionnel — sans qu'aucun mécanisme de découverte de clés propre à A2A (point de terminaison well-known dédié, champ `jwks_uri`, registre) ne soit défini.

- **fidélité à la source** — Les trois citations existent bien aux emplacements annoncés (§8.4.2 : « `jku`: URL to JSON Web Key Set (JWKS) containing the public key », `kid` listé parmi les paramètres requis du protected header ; §8.4.3 : « Retrieve the public key using the `kid` and `jku` (or from a trusted key store) » ; schéma v0.3.0 : `"required": ["protected", "signature"]`, aucune occurrence de « kid », « jku », « jwks » ni « jwks_uri »). Le second membre de l'affirmation — aucun mécanisme de découverte de clés propre à A2A (le seul `.well-known` du document, `/.well-known/agent-card.json`, sert à trouver l'Agent Card, pas les clés ; n…
- **qualification logique** — Deux défauts de qualification logique, dont un auto-réfutant.  (1) « Exclusivement » est contredit par la source citée elle-même. La citation §8.4.3 versée à l'appui se lit « Retrieve the public key using the `kid` and `jku` (or from a trusted key store) » : la parenthèse nomme une **troisième** voie d'obtention de la clé, hors bande, qui n'est pas un paramètre d'en-tête JWS. Vérification à la source (raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md, consultée le 21 juillet 2026) : la spécification pose bien « Clients MAY maintain a trusted key store for known agent providers ». L'affirmation c…
- **statut et datation** — Sources bien PRIMAIRES (dépôt officiel a2aproject/A2A : texte de spécification + schéma JSON), date de consultation réelle et cohérente. La réfutation porte sur deux points, l'un de fond, l'autre de statut/datation.  1) « Exclusivement » est contredit par la citation même de l'affirmation. §8.4.3, étape 2, verbatim constaté sur main : « Retrieve the public key using the `kid` and `jku` (or from a trusted key store) ». La parenthèse ouvre une troisième voie, hors bande, explicitement admise. Une affirmation qui reproduit cette parenthèse dans sa propre citation ne peut pas conclure à l'exclusivité des deux paramèt…

### `L03-A2-4` — écartée, 2 réfutations sur 3

> L'exemple de la spécification fait pointer le paramètre `jku` d'une Agent Card signée vers un jeu de clés hébergé sur le domaine de l'agent lui-même (`https://example.com/agent/jwks.json`), c'est-à-dire vers une ressource contrôlée par l'entité dont la carte est à vérifier.

- **fidélité à la source** — Réfutation partielle : la citation verbatim est authentique, l'interprétation qui en est tirée ne l'est pas.  VÉRIFIÉ — 1) La chaîne `{"alg":"ES256","typ":"JOSE","kid":"key-1","jku":"https://example.com/agent/jwks.json"}` figure bien en §8.4.2 « Signature Format » de `docs/specification.md` (branche main). Contrôle indépendant : le décodage base64url du champ `protected` de l'exemple (`eyJhbGciOiJFUzI1NiIs…`) restitue exactement cette chaîne. 2) La phrase « Implement access controls on the HTTP endpoint serving the Agent Card (e.g., `/.well-known/agent-card.json` or registry API). » figure bien sur la page Agent…
- **qualification logique** — Le noyau littéral tient, la qualification ne tient pas.  VÉRIFIÉ SUR PIÈCE (spécification A2A, branche main, §8.4.2 « Signature Format ») : l'en-tête protégé décodé de l'exemple est bien, mot pour mot, {"alg":"ES256","typ":"JOSE","kid":"key-1","jku":"https://example.com/agent/jwks.json"}. La citation et le renvoi de section sont exacts.  CE QUI EST RÉFUTÉ — trois défauts de qualification logique.  1. « sur le domaine de l'agent lui-même » n'est PAS démontré par l'exemple. Le §8.4.2 est un exemple de signature autonome (« Given a canonical Agent Card payload and signing key ») : aucune Agent Card ne l'accompagne,…

### `L03-A4-02` — écartée, 3 réfutations sur 3

> Le projet A2A ne publie, hors de sa spécification, ni modèle de menace, ni document de sécurité dédié, ni page « security considerations » : ni la racine du dépôt, ni le répertoire docs/topics/, ni la navigation du site de documentation, ni le répertoire adrs/ n'en contiennent.

- **qualification logique** — RÉFUTÉ sur trois fronts, dont deux depuis la preuve fournie elle-même.  (1) Contradiction interne, décisive. Le balayage déclaré liste à la racine un `SECURITY.md` — c'est même la citation retenue pour cette source (« quote »: « SECURITY.md »). L'affirmation nie qu'il existe un « document de sécurité dédié » et pose que « ni la racine du dépôt […] n'en contien[t] ». Un fichier nommé `SECURITY.md` est, par son nom, un document de sécurité dédié. Le balayage ne l'écarte pas : il ne cherche que `threat`, `trust`, `key` et ne rapporte aucune ouverture du contenu de `SECURITY.md`. Le volet « document de sécurité dédié…
- **fidélité à la source** — Les quatre URL ont été ouvertes ; les quatre citations verbatim s'y trouvent réellement. La réfutation ne porte pas sur l'existence des citations mais sur le glissement entre ce qu'elles écrivent et ce que l'affirmation en tire — et deux d'entre elles établissent l'inverse de la thèse qu'elles sont censées appuyer.  1) RACINE — contradiction frontale par la citation elle-même. Le listing de la racine contient `SECURITY.md`, et c'est précisément le verbatim invoqué (« SECURITY.md »). L'affirmation soutient que « ni la racine du dépôt […] n'en contien[t] » de « document de sécurité dédié » ; sa propre source produi…
- **statut et datation** — Réfutation par la source primaire invoquée elle-même. 1) Contradiction interne : le listing racine cité porte comme extrait « SECURITY.md ». Vérification indépendante (api.github.com/repos/a2aproject/A2A/contents/, consulté le 21 juillet 2026) : la racine contient bien SECURITY.md, aux côtés de CHANGELOG.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md, GOVERNANCE.md, MAINTAINERS.md, mkdocs.yml. Lecture du fichier (raw.githubusercontent.com/a2aproject/A2A/main/SECURITY.md) : politique de sécurité dédiée — signalement à security@lists.a2aproject.org, coordination et divulgation privées via GitHub Security Advisory. C'est u…

### `L03-A4-04` — écartée, 3 réfutations sur 3

> Aucun des sept documents du projet A2A situés hors de la spécification et balayés le 21 juillet 2026 ne mentionne la rotation ni la révocation des clés de signature d'Agent Card.

- **fidélité à la source** — Les trois citations invoquées sont authentiques et vérifiées sur pièce (agent-discovery.md : phrase exacte présente ; extension-and-binding-governance.md : titre exact ; roadmap.md : phrase présente mais TRONQUÉE — le texte réel est « Prioritize community-led development with standardized processes for contributing to the specification, SDKs and tooling »). L'affirmation est néanmoins réfutée sur trois motifs. (1) DÉFAUT DE PREUVE SUR LE PÉRIMÈTRE : l'affirmation porte sur SEPT documents ; trois seulement sont cités. Quatre ne sont ni nommés ni sourcés. Un négatif universel sur un corpus exige l'énumération du co…
- **statut et datation** — Lentille statut/datation — l'affirmation ne tombe pas sur le fond (les documents que j'ai pu ouvrir ne mentionnent effectivement ni rotation ni révocation), mais elle est irrecevable telle que formulée, sur trois constats faits sur pièce le 21 juillet 2026.  1) DATATION CONTREDITE PAR LA PIÈCE. Le fichier `docs/roadmap.md` porte sa propre ligne « Last updated: March 10, 2026 ». La fiche source lui attribue « branche main, état du 21 juillet 2026 » et n'en rapporte pas la date propre. Un silence constaté dans un document figé depuis le 10 mars 2026 n'atteste rien de l'état du projet au 21 juillet 2026 : la date dé…
- **qualification logique** — Réfutation partielle, portant sur la qualification et non sur la mesure. Contre-vérification indépendante du 21 juillet 2026 (branche main) : les sept documents ont été rouverts un à un et les décomptes 0/0 pour « rotat » et « revoc » sont exacts (SECURITY.md, GOVERNANCE.md, docs/roadmap.md, docs/whats-new-v1.md, docs/topics/enterprise-ready.md, docs/topics/agent-discovery.md, docs/topics/extension-and-binding-governance.md). Le degré 1 est donc légitime — mais seulement sur ce que le balayage couvre, et l'énoncé couvre davantage. Trois défauts. (1) DOMAINE PRÉSENTÉ COMME EXHAUSTIF. La tournure « les sept documen…

## C. Échecs de source consignés (19)

*Un échec documenté est un résultat : il borne ce que le lot peut affirmer.*

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Schéma JSON de la spécification A2A (specification/json/a2a.json), visé comme troisième source d'énumération indépendante des membres de AgentCardSign… | HTTP 404. Vérification faite sur le listage du répertoire specification/json/ : il ne contient qu'un README.md, qui indique que a2a.json est un artefact de compilation non normatif volontairement non versionné. Ce n'est donc pas u… |
| Lecture de la spécification sur la page de documentation officielle a2a-protocol.org (rendu HTML), pour §4.4.7 et §8.4 | Contenu tronqué à la récupération (interruption vers §4.1.6) : les sections 4.4.7 et 8.4 n'étaient pas atteintes. Contourné en lisant la source Markdown du même document au dépôt officiel, sur la branche main puis sur l'étiquette… |
| Téléchargement local de docs/specification.md et de a2a.proto en vue d'un balayage par grep exécuté et reproductible | Commande PowerShell (Invoke-WebRequest) refusée par la politique d'exécution de la session. Conséquence portée dans les caveats de L03-A6 et L03-A8 : les balayages ont été conduits par l'outil de récupération distante, dont le rap… |
| Contenu de la version v1.0.1 de la spécification (étiquette postérieure à celle lue) | Non ouverte, faute de temps d'instruction. L'existence de l'étiquette est établie par le registre des versions (publiée le 2026-05-28), mais aucun énoncé du présent axe n'est revalidé sur elle. Signalé au caveat de L03-A4. |
| Téléchargement local de la spécification pour balayage par `grep` reproductible (curl via Bash, puis Invoke-WebRequest via PowerShell) | Permission refusée par le système de permissions de la session pour les deux shells (« Permission to use Bash ... has been denied », idem PowerShell). Conséquence directe sur la qualité de preuve : tous les balayages de chaînes de… |
| Schéma JSON normatif de la branche courante (définition AgentCardSignature à jour) | HTTP 404. Le chemin a changé depuis la v0.3.0. Contournement : la définition a été extraite du tag v0.3.0 (https://github.com/a2aproject/A2A/blob/v0.3.0/specification/json/a2a.json), qui répond. L'écart de version entre v0.3.0 et… |
| Fichier protobuf annoncé comme définition normative unique des objets du protocole | HTTP 404 (chemin deviné à partir d'un extrait de résultat de recherche annonçant que « spec/a2a.proto is the single authoritative normative definition » et que le JSON est un artefact de compilation non normatif). Le chemin réel n… |
| Spécification de développement (brouillon post-1.0) pour établir si l'ancrage de confiance y évolue | Page récupérée mais tronquée par l'extraction avant la §8.4 : seuls les titres de la table des matières ont été obtenus, le corps s'interrompant plus haut dans le document. Impossible donc de dire si le brouillon modifie le traite… |
| Confirmation des dates de publication des versions A2A (v1.0.0, v1.0.1, v0.3.0) | Page récupérée, mais GitHub y affiche les dates sous forme abrégée (« 12 Mar », « 28 May ») dont le millésime a été INFÉRÉ par l'agent d'extraction, non lu sur la page. Les dates avancées — v1.0.0 le 12 mars 2026, v1.0.1 le 28 mai… |
| Balayage par grep local des documents téléchargés (méthode reproductible hors ligne) | Les outils shell (PowerShell Invoke-WebRequest, Bash curl) ont été refusés par le bac à sable de la session : « Permission to use PowerShell/Bash … has been denied ». Conséquence méthodologique à déclarer : les décomptes d'occurre… |
| Politique de sécurité à l'échelle de l'organisation (dépôt a2aproject/.github) | HTTP 404. Le dépôt .github existe mais ne contient, à sa racine, que .gitignore, CODE_OF_CONDUCT.md, CONTRIBUTING.md, LICENSE et les répertoires .github/ et profile/. Il n'y a donc pas de politique de sécurité par défaut couvrant… |
| SECURITY.md du SDK Go officiel | HTTP 404, confirmé par le listing complet de la racine du dépôt via l'API Contents. Échec documenté valant constat d'absence, non défaut d'accès. |
| Recherche de code à l'échelle de l'organisation a2aproject (chaînes « key rotation », « revocation », « JWKS ») pour couvrir les dépôts non énumérés | Non tentée : l'interface de recherche de code de GitHub est rendue par JavaScript et l'API de recherche de code exige une authentification, indisponible dans cette session. L'exhaustivité organisationnelle n'est donc pas établie ;… |
| Charte technique officielle de la Linux Foundation pour A2A (Series Agreement) en tant que document distinct | GOVERNANCE.md renvoie à un « Series Agreement » et se désigne comme « Charter », mais aucun document contractuel distinct n'a été localisé sur le site de la Linux Foundation ni dans le dépôt. Le texte de charte disponible est donc… |
| Texte normatif de la §8.6 « Caching » et de la §13.3 « Extended Agent Card Access Control » de la spécification A2A v1.0.0 | L'outil de récupération tronque le fichier au milieu de la §8.5 (bloc JSON de l'exemple d'Agent Card) ; trois tentatives, dont une demandant explicitement les 50 dernières lignes reçues, confirment la troncature au même point. L'e… |
| Schéma JSON a2a.json sur la branche main du dépôt | HTTP 404. Motif documenté par le dépôt lui-même : artefact généré, volontairement non versionné (voir L03-A3-07). |
| Recherche littérale à l'échelle du dépôt (contournement de la troncature) via grep.app | HTTP 429 Too Many Requests. |
| Index de recherche du site mkdocs, tenté comme second contournement de la troncature | Fichier trop volumineux : la récupération n'a restitué que les premiers enregistrements (pages d'accueil et d'annonce) ; les enregistrements des §8.6 et §13.3 n'y étaient pas atteignables. |
| Page publiée de la spécification, tentée pour lire la §8.4 in extenso | Troncature de la conversion au milieu de la §4.1.6 : la page est plus longue que ce que l'outil restitue. Contournée par le fichier source docs/specification.md, qui porte plus loin (jusqu'à la §8.5). |

## D. Ce que chaque axe déclare n'avoir pas couvert

- **format-signature** — Ce que cet axe n'a PAS couvert. (1) La chaîne de confiance en amont de la signature : la spécification renvoie à un JWKS par le paramètre « jku », mais aucune source n'a été ouverte sur la manière dont ce JWKS est lui-même authentifié, ni sur l'existence d'une autorité, d'un registre ou d'un ancrage de confiance A2A — c'est le maillon décisif pour le ch. 5 et il reste entier. (2) Le lien entre la signature et l'origine de service : il n'a pas été établi si la signature lie la carte à l'URI « .well-known » d'où elle est servie, ni à un domaine ; la question du rejeu d'une carte signée valide servie depuis un autre hôte n'est pas instruite. (3) La carte étendue authentifiée (« authenticated extended card ») : la page de découverte d'agents la mentionne, mais son articulation avec la signature n'a pas été lue. (4) L'écosystème d'implantation : aucun SDK (a2a-python, a2a-js, a2a-java) n'a été ouvert, donc rien n'est établi sur ce qui est réellement implanté ni sur le taux d'apposition de signatures en pratique — les énoncés du présent axe portent sur le texte de la spécification, jamais sur le déploiement. (5) Les algorithmes admis : la spécification donne « ES256 », « RS256 » à titre d'exemple (« e.g. »), sans liste fermée ; aucun profil cryptographique obligatoire n'a été recherché, et il ne faut pas conclure de ces deux exemples à une restriction. (6) L'historique du dispositif entre v0.3.0 et v1.0.0 : seule la date d'introduction du champ est établie ; les évolutions éventuelles du format entre ces deux versions n'ont pas été retracées. (7) Aucune corroboration secondaire n'a été employée dans cet axe : les huit énoncés reposent exclusivement sur trois fichiers du dépôt officiel et sur le registre des versions GitHub. Le niveau proposé est B pour l'ensemble ; l'élévation en A suppose le vote et, pour L03-A6 et L03-A8, la reprise du balayage par grep local.
- **ancrage** — CE QUE L'AXE 2 A ÉTABLI, EN UNE LIGNE : la spécification A2A prescrit un format de signature (JWS RFC 7515 sur canonicalisation JCS RFC 8785) et une procédure de vérification, mais renvoie intégralement l'ANCRAGE de cette signature à l'implémenteur et au déploiement — aucune autorité d'émission, aucune racine de confiance, aucune fédération, aucun mécanisme de découverte de clés propre à A2A. La réponse à « qui signe les signataires ? » est : la spécification ne le dit pas, et ne prétend pas le dire.  CE QUE L'AXE 2 N'A PAS COUVERT, ET POURQUOI :  1. Le fichier .proto déclaré normatif — non ouvert (404 sur le chemin deviné). Tant qu'il n'est pas ouvert, les affirmations de structure d'objet (L03-A2-3) reposent sur un schéma JSON dont une source secondaire affirme qu'il est un artefact de compilation non normatif. À instruire en priorité : c'est la seule faiblesse structurelle du lot.  2. L'évolution post-1.0 — la spécification de développement n'a pas pu être lue au-delà de sa table des matières. Aucun énoncé PROGRAMMÉ n'est donc formulé sur l'ancrage de confiance : le lot ne dit rien de ce que la prochaine révision fera. Ne pas combler par inférence.  3. Les implémentations de référence (SDK Python, Java, JavaScript, Go du dépôt a2aproject) — non consultées. Ce que le code fait réellement lorsque `jku` est absent, lorsqu'il pointe vers un domaine tiers, ou lorsqu'aucun magasin de clés n'est configuré, reste inconnu. C'est l'écart le plus intéressant à instruire pour un chapitre : une spécification muette sur l'ancrage laisse chaque SDK trancher, et ces choix-là sont observables. Axe à ouvrir séparément.  4. Le croisement avec les mécanismes concurrents — passeport d'agent d'autres cadres, Entra Agent ID, DID, Sigstore, extension `trust.signals[]` (issue #1628), issues #1497/#1472/#1501/#1575 — délibérément hors périmètre de cet axe, qui portait sur ce que LA SPÉCIFICATION A2A documente. Ces pistes sont des paris de recherche non adoptés ; aucune ne doit être présentée comme un mécanisme A2A (R-01, R-02).  5. Le lien entre l'ancrage de la carte et l'authentification des APPELS subséquents (schémas OAuth 2.0 / OpenID Connect déclarés dans la carte) — non instruit. La chaîne complète « je fais confiance à la carte → je fais confiance au jeton » n'a pas été suivie.  AVERTISSEMENT DE MÉTHODE, à reporter au registre : l'accès au shell ayant été refusé, aucun balayage n'a pu être exécuté par `grep` local. Les degrés 1 revendiqués (L03-A2-2, L03-A2-6) reposent sur des recherches littérales déléguées à l'agent d'extraction web, demandées avec décompte d'occurrences et redondées sur deux passes indépendantes concordantes. C'est plus qu'un repérage, moins qu'un balayage rejouable. Avant que ces deux entrées n'entrent en chapitre — et elles sont centrales —, refaire le scan par `grep` sur copie locale et consigner la commande. En l'état, un relecteur adverse aurait raison de contester le degré 1.  PIÈGE DE FORMULATION POUR LA RÉDACTION : ne jamais écrire que la signature de l'Agent Card « prouve l'identité » ou « atteste » de l'agent. Ce que la spécification démontre se borne à ceci : le détenteur d'une clé désignée par un `kid` a signé une forme canonicalisée de la carte. Le lien entre cette clé et une organisation réelle n'est établi par aucun énoncé de la spécification.
- **gouvernance-cles** — Ce que cet axe n'a PAS couvert, et pourquoi. (1) La spécification elle-même — docs/specification.md et le répertoire specification/ n'ont pas été ouverts : l'axe porte explicitement sur le corpus HORS spécification, et un balayage fiable de la spécification (fichier volumineux, risque de troncature par l'outil de récupération) relève des axes 1 à 3 de L-03. Aucune affirmation ci-dessus ne porte donc sur ce que la spécification dit ou ne dit pas de la rotation, de la révocation ou de la détention des clés : la seule chose établie est que le corpus non spécifié est muet. (2) Le code des SDK n'a pas été audité : la manière dont a2a-python, a2a-js, a2a-java, a2a-go, a2a-dotnet ou a2a-rs génèrent, chargent ou valident une clé de signature n'est pas documentée ici — un SDK peut imposer en pratique une gouvernance que la documentation ne décrit pas. (3) Les archives de la liste security@lists.a2aproject.org, les comptes rendus de réunion du TSC et les enregistrements de la plateforme de réunion de la Linux Foundation n'ont pas été consultés : une décision de gouvernance des clés pourrait y avoir été prise sans document publié. (4) Les tickets et demandes de tirage ouverts du dépôt (issues, PR, discussions) n'ont pas été balayés : un travail en cours sur un cadre de confiance des cartes signées ne serait pas visible dans les fichiers figés. (5) Le dépôt experimental-ext-oid4vp-auth (« OID4VP In-Task Authorization Extension for A2A ») touche aux justificatifs vérifiables et n'a pas été examiné, faute d'entrer dans le périmètre « gouvernance des clés d'Agent Card ». (6) L'articulation avec l'Agentic AI Foundation n'est établie que négativement (A2A absent des trois contributions fondatrices du 9 décembre 2025) ; l'éventuelle évolution ultérieure du rattachement de A2A à l'AAIF n'a pas été instruite. (7) Aucun avis de vulnérabilité n'ayant été publié pour le dépôt de spécification, l'axe ne fournit aucun cas concret de traitement d'une compromission de clé.
- **revocation** — Ce que cet axe n'a PAS couvert. (1) La §8.6 « Caching » et la §13.3 (carte étendue) de la spécification, toutes deux normatives et toutes deux inaccessibles par troncature — c'est la lacune la plus lourde de cet axe, puisque §8.6 est précisément le siège annoncé des exigences de fraîcheur. Tout balayage global présenté ici est donc borné aux sections 1 à 8.5 telles que restituées ; les balayages de degré 1 sont, eux, bornés à des blocs récupérés verbatim et relus intégralement (§8.4 entière ; messages AgentCard et AgentCardSignature du .proto), ce qui les rend vérifiables. (2) Le comportement des SDK officiels (a2a-python, a2a-js, Java, Go, .NET, Rust) : aucune implémentation de vérification n'a été ouverte — on ignore si l'une contrôle une fraîcheur non prescrite. (3) Les RFC 7515 (JWS) et 7517 (JWK) n'ont pas été balayées : l'absence de champ d'expiration dans un JWK n'est pas établie ici et ne doit pas être supposée. (4) Le versionnage : la documentation de la branche main annonce « Latest Released Version 1.0.0 », alors que l'API des versions du dépôt (https://api.github.com/repos/a2aproject/A2A/releases, consultée le 21 juillet 2026) porte une étiquette v1.0.1 postérieure (28 mai 2026) à v1.0.0 (12 mars 2026) ; l'écart entre l'étiquette et la version documentée n'a pas été instruit, et aucune affirmation ne s'y adosse. (5) Les propositions communautaires ouvertes qui visent ce manque (identité ancrée DANE, identité DID, cadres de confiance) n'ont pas été instruites au-delà d'une citation de corroboration : ce sont des propositions ouvertes, non des mécanismes du protocole, et elles ne doivent en aucun cas être présentées comme PROGRAMMÉES. (6) La révision de la spécification MCP attendue le 28 juillet 2026 est hors périmètre de cet axe.

## E. Sources et citations des affirmations retenues

⚠ **Les Réserves ci-dessous sont reproduites intégralement.** Elles sont l'instrument de R-12 et de la qualification des absences : une réserve tronquée laisse la matière et retire le bornage. *(Défaut constaté et corrigé à la relecture P1.4 du 21 juillet 2026.)*

### `L03-A1` — [B]

Dans le modèle de données A2A, le champ de l'AgentCard qui porte les signatures se nomme « signatures » et est un tableau répété d'objets AgentCardSignature, déclaré non requis.

- **primaire** — a2a.proto — définition Protocol Buffers normative du protocole A2A — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/specification/a2a.proto>
  > // JSON Web Signatures computed for this `AgentCard`.   repeated AgentCardSignature signatures = 13;
- **primaire** — Agent2Agent (A2A) Protocol Specification, §4.4.1 (table AgentCard) — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > signatures \| AgentCardSignature[] \| No \| Array of digital signatures verifying Agent Card authenticity and integrity

**Réserve** — Le champ est facultatif : une Agent Card conforme peut ne porter aucune signature.

### `L03-A2` — [A]

La structure AgentCardSignature comporte exactement trois membres — « protected » (requis, chaîne), « signature » (requis, chaîne) et « header » (facultatif, objet) — et ne comporte aucun membre « payload ».

**Balayage (degré 1)** — Balayage de trois énumérations exhaustives et indépendantes de la structure, toutes ouvertes le 2026-07-21 : (1) le message protobuf AgentCardSignature de specification/a2a.proto (branche main), qui déclare les champs numérotés 1, 2 et 3 et aucun autre ; (2) la table de champs de §4.4.7 de docs/specification.md (v1.0.0) ; (3) la liste à puces de §8.4.2 « Signature Format » de docs/specification.md, lue à la fois sur main et sur l'étiquette v1.0.0. Chaîne cherchée : « payload » comme nom de membre de la structure — absente des trois énumérations.

- **primaire** — a2a.proto — message AgentCardSignature — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/specification/a2a.proto>
  > message AgentCardSignature {   // Required. The protected JWS header for the signature. This is always a   // base64url-encoded JSON object.   string protected = 1 [(google.api.field_behavior) = REQUIRED];   // Required. The computed signature, base64url-encoded.   string signature = 2 [(google.api.field_behavior) = REQUIRED];   // The unprotected JWS header values.   google.protobuf.Struct header = 3; }
- **primaire** — A2A Protocol Specification, §8.4.2 Signature Format — étiquette v1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/v1.0.0/docs/specification.md>
  > The [`AgentCardSignature`](#447-agentcardsignature) object represents JWS components using three fields: - **`protected`** (required, string) ... - **`signature`** (required, string) ... - **`header`** (optional, object)

**Réserve** — L'absence de membre « payload » est une propriété de la structure, non une interdiction de transporter la carte : la charge utile signée est la carte elle-même, que le vérificateur reconstruit (voir L03-A6).

### `L03-A2-1` — [A]

La spécification A2A définit la signature de l'Agent Card comme une signature JSON Web Signature (RFC 7515) calculée sur une forme canonicalisée de la carte selon le JSON Canonicalization Scheme (RFC 8785), la liste `signatures` elle-même étant exclue du contenu signé.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4 Agent Card Signing — branche main, consultée le 21 juillet 2026 ; le site officiel déclare…, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Before signing, the Agent Card content MUST be canonicalized using the JSON Canonicalization Scheme (JCS)
- **primaire** — A2A JSON Schema, définition AgentCardSignature (tag v0.3.0) — tag v0.3.0, consultée le 2026-07-21 — <https://github.com/a2aproject/A2A/blob/v0.3.0/specification/json/a2a.json>
  > AgentCardSignature represents a JWS signature of an AgentCard.\nThis follows the JSON format of an RFC 7515 JSON Web Signature (JWS).

**Réserve** — Le mécanisme est qualifié ici par ce que la spécification PRESCRIT (canonicalisation, format JWS), non par une propriété de sécurité démontrée. La spécification ne démontre aucune propriété d'authentification d'origine : une JWS établit qu'un détenteur de clé a signé un octet-stream, ce qui reste sans portée tant que le lien entre la clé et une organisation n'est pas établi hors du protocole (voir L03-A2-3 à L03-A2-5). Le texte scanné est celui de la branche main, qui peut être en avance sur la version publiée.

### `L03-A2-5` — [B]

Le seul dispositif d'ancrage hors-bande prévu par la procédure de vérification de la spécification A2A est facultatif et non spécifié : la spécification énonce que les clients « MAY maintain a trusted key store for known agent providers » sans en définir ni la provenance, ni le format, ni les critères d'inscription.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.3 Signature Verification — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Clients MAY maintain a trusted key store for known agent providers
- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.3 Signature Verification — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Clients SHOULD verify at least one signature before trusting an Agent Card

**Réserve** — Conjonction à ne pas perdre : la vérification d'au moins une signature est un SHOULD, la tenue d'un magasin de clés de confiance un MAY. La spécification prescrit donc de vérifier une signature sans prescrire par rapport à quoi l'ancrer — c'est le point exact où l'ancrage est renvoyé à l'implémenteur et au déploiement. Les niveaux d'exigence (MUST/SHOULD/MAY) sont reproduits tels qu'ils figurent dans le texte, en gras dans l'original.

### `L03-A2-6` — [B]

La spécification A2A interdit l'emploi de clés expirées ou révoquées pour la vérification d'une Agent Card mais ne définit aucun mécanisme de révocation ni de publication d'état de révocation : la chaîne « revocation » est absente du document et « revoked » n'y apparaît qu'une seule fois, dans l'énoncé de l'interdiction elle-même.

**Balayage (degré 1)** — Document balayé : docs/specification.md du dépôt officiel a2aproject/A2A, branche main, consultée le 21 juillet 2026. Chaînes cherchées avec décompte explicite : « revocation » (0 occurrence), « revoked » (1 occurrence, citée intégralement en source), « jwks_uri » (0), « x5c » (0), « x5u » (0). Aucune occurrence d'un mécanisme de type CRL, OCSP ou liste de révocation n'a été relevée. Même limite qu'en L03-A2-2 : shell refusé, balayage délégué à l'agent d'extraction web et redondé sur deux passes concordantes, non exécuté par `grep` local.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.3 Signature Verification — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Expired or revoked keys MUST NOT be used for verification

**Réserve** — Une obligation de ne pas employer une clé révoquée, sans mécanisme permettant d'apprendre qu'elle l'est, n'est pas vérifiable par le client. Cette remarque est une lecture de l'auteur ; le fait établi ici se limite à la présence de l'interdiction et à l'absence des chaînes recherchées.

### `L03-A2-7` — [B]

La documentation officielle A2A porte une réserve explicite d'absence sur les registres d'agents : elle déclare que la spécification en vigueur ne prescrit aucune API normalisée pour les registres curés, qui seraient la voie naturelle d'un ancrage de confiance tiers.

- **primaire** — Agent Discovery — A2A Protocol (documentation officielle) — page « latest », consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://a2a-protocol.org/latest/topics/agent-discovery/>
  > The current A2A specification does not prescribe a standard API for curated registries

**Réserve** — Degré 2 assumé : la réserve est portée par la source elle-même, sans que le texte des registres ait été balayé chaîne par chaîne. La qualification du registre curé comme « voie naturelle d'un ancrage tiers » est une lecture de l'auteur, pas un énoncé de la source.

### `L03-A2-8` — [B]

L'absence de mécanisme protocolaire de vérification de l'authenticité d'une Agent Card est reconnue comme question ouverte au dépôt officiel A2A : l'issue #1672, ouverte le 22 mars 2026 et non close au 21 juillet 2026, énonce qu'un agent qui découvre l'Agent Card d'un autre ne dispose d'aucun mécanisme de niveau protocolaire pour en vérifier l'authenticité.

- **primaire** — Proposal: Agent Identity Verification for Agent Cards (issue #1672) — ouverte le 22 mars 2026 ; statut « open » au 21 juillet 2026, consultée le 2026-07-21 — <https://github.com/a2aproject/A2A/issues/1672>
  > When Agent A discovers Agent B's Agent Card, it has no protocol-level mechanism to verify that the card is authentic.
- **primaire** — Sign agent cards for the love of god! (discussion #199) — réponse du mainteneur @mikeas1 datée du 15 juillet 2025, consultée le 2026-07-21 — <https://github.com/a2aproject/A2A/discussions/199>
  > Signatures should be optional, and adding them should be backwards compatible.

**Réserve** — STATUT PRÉ-NORMATIF À DIRE : #1672 est une PROPOSITION déposée par un contributeur, ni adoptée ni close ; elle n'engage pas le groupe de spécification et ne vaut pas feuille de route. Le tri SPÉCULATIF s'applique à tout énoncé sur son issue : aucune date d'adoption n'est annoncée, aucun mainteneur n'y a répondu dans le contenu consulté. Les pistes discutées ailleurs dans le dépôt (Sigstore, DID, X.509, extension `trust.signals[]` de l'issue #1628) sont des paris de recherche, à ne jamais présenter comme des mécanismes A2A. La citation de @mikeas1 provient d'un fil de discussion long, restitué par l'agent d'extraction ; le verbatim n'est pas revendiqué au mot près et demande re-vérification sur pièce avant citation en chapitre.

### `L03-A3` — [A]

La spécification A2A qualifie la signature d'une Agent Card de JSON Web Signature au sens du RFC 7515, en pose l'apposition comme facultative (« MAY ») et n'exige de la part du client qu'une recommandation (« SHOULD ») de vérifier au moins une signature avant d'accorder confiance à la carte.

- **primaire** — A2A Protocol Specification, §8.4 Agent Card Signing — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Agent Cards **MAY** be digitally signed using JSON Web Signature (JWS) as defined in [RFC 7515](https://tools.ietf.org/html/rfc7515) to ensure authenticity and integrity.
- **primaire** — A2A Protocol Specification, §8.4.3 Signature Verification — Security Considerations — étiquette v1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/v1.0.0/docs/specification.md>
  > Clients **SHOULD** verify at least one signature before trusting an Agent Card
- **primaire** — a2a.proto — commentaire du message AgentCardSignature — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/specification/a2a.proto>
  > // AgentCardSignature represents a JWS signature of an AgentCard. // This follows the JSON format of an RFC 7515 JSON Web Signature (JWS).

**Réserve** — R-02 : le texte cité énonce une finalité (« to ensure authenticity and integrity »), non une propriété démontrée. Ce que la spécification décrit est un mécanisme de signature ; l'énoncé de finalité de la spécification ne doit pas être repris comme qualification du mécanisme. Le couple MAY (apposition) / SHOULD (vérification) signifie qu'une chaîne A2A conforme peut ne comporter aucune signature apposée ni aucune vérification.

### `L03-A3-01` — [B]

Dans la spécification A2A v1.0.0 (§8.4.2), l'en-tête JWS protégé d'une signature d'Agent Card ne comporte aucun paramètre temporel : les paramètres imposés sont alg, typ et kid, et le seul paramètre facultatif nommé est jku.

**Balayage (degré 1)** — Document : docs/specification.md du dépôt a2aproject/A2A, branche main, version annoncée « Latest Released Version 1.0.0 », consulté le 21 juillet 2026. La section 8.4 entière (8.4.1 à 8.4.3) a été récupérée verbatim et relue ligne à ligne. Chaînes cherchées dans cette section : exp, nbf, iat, expir, expires, lifetime, ttl, valid, not-before, JWT. Occurrences trouvées : aucune, hormis « Expired or revoked keys » en 8.4.3 (qui porte sur la clé, non sur l'en-tête). Les seuls paramètres d'en-tête nommés sont alg, typ, kid, jku.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.2 Signature Format — version 1.0.0, branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > The protected header **MUST** include: `alg` [...] `typ` [...] `kid`: Key ID for identifying the signing key. The protected header **MAY** include: `jku`: URL to JSON Web Key Set (JWKS) containing the public key

**Réserve** — Le balayage est borné à la §8.4. La récupération du fichier complet est tronquée au milieu de la §8.5 (voir failures) : les sections 8.6 et suivantes n'ont pas été balayées.

### `L03-A3-02` — [A]

La spécification A2A v1.0.0 pose une interdiction normative d'employer une clé expirée ou révoquée pour vérifier une signature d'Agent Card, et cette interdiction porte sur la clé de signature, non sur la carte elle-même.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.3 Signature Verification — Security Considerations — version 1.0.0, branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Expired or revoked keys **MUST NOT** be used for verification

**Réserve** — L'énoncé figure sous l'intitulé « Security Considerations » de la §8.4.3, au même niveau que des recommandations en SHOULD et MAY ; il emploie néanmoins MUST NOT.

### `L03-A3-03` — [A]

La spécification A2A v1.0.0 impose de ne pas employer une clé expirée ou révoquée sans définir, en §8.4, aucun moyen d'en établir le statut : la section ne mentionne ni liste de révocation, ni OCSP, ni CRL, ni point de terminaison de statut, ni chaîne de certificats, ni délai de re-validation, et la procédure de vérification en six étapes ne comporte aucune étape de contrôle de statut ou de fraîcheur.

**Balayage (degré 1)** — Document : docs/specification.md du dépôt a2aproject/A2A, branche main, version 1.0.0, consulté le 21 juillet 2026 ; section 8.4 récupérée verbatim et relue intégralement. Chaînes cherchées : revoc, revoke, revoked, revocation list, CRL, OCSP, status, x5c, x5u, freshness, re-validation, expiry. Seules occurrences : « Expired or revoked keys MUST NOT be used for verification » (interdiction), et « kid » / « jku » (découverte de clé). Les six étapes normatives de la §8.4.3 sont : extraire la signature, récupérer la clé publique via kid et jku ou depuis un magasin de clés de confiance, retirer les propriétés à valeur par défaut, exclure le champ signatures, canonicaliser selon RFC 8785, vérifier la signature — aucune n'est un contrôle de statut.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.3 Signature Verification — version 1.0.0, branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Retrieve the public key using the `kid` and `jku` (or from a trusted key store)
- *secondaire* — Extension proposal: DANE-anchored identity for Agent Cards (DNSSEC TLSA binding for the signing key), issue ou… — ouverte le 2026-07-10, état « open » au 2026-07-21, consultée le 2026-07-21 — <https://github.com/a2aproject/A2A/issues/2043>
  > The spec is honest about this: it leans on channel security and a client-side trusted key store rather than a domain-level key binding.

**Réserve** — Portée du balayage limitée à la §8.4 (troncature de la récupération au milieu de la §8.5). La §8.6 « Caching », normative et existante, n'a pas pu être ouverte : elle pourrait porter des exigences de fraîcheur. La deuxième source est une corroboration secondaire nommée — une proposition d'extension ouverte dans le suivi officiel du projet, non un texte normatif.

### `L03-A3-04` — [A]

Le message AgentCard de la définition Protobuf normative d'A2A comporte quatorze champs, dont aucun n'exprime une validité temporelle ou un statut : ni date d'émission, ni date d'expiration, ni fenêtre de validité, ni indicateur de révocation.

**Balayage (degré 1)** — Document : specification/a2a.proto du dépôt a2aproject/A2A, branche main, consulté le 21 juillet 2026 ; le bloc « message AgentCard { … } » a été récupéré verbatim en entier (commentaire d'en-tête « Next ID: 20 » inclus). Champs constatés : name (1), description (2), supported_interfaces (3), provider (4), version (5), documentation_url (6), capabilities (7), security_schemes (8), security_requirements (9), default_input_modes (10), default_output_modes (11), skills (12), signatures (13), icon_url (14). Chaînes cherchées dans le fichier : revoke, revocation, expire, expiration, exp, nbf, iat, lifetime, ttl, rotate, rotation, valid_until, not_after — aucune occurrence ; « status » n'apparaît que dans TaskStatus et TaskState, sans rapport avec la validité d'une carte.

- **primaire** — specification/a2a.proto — message AgentCard (définition normative d'A2A) — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/specification/a2a.proto>
  > // JSON Web Signatures computed for this `AgentCard`.   repeated AgentCardSignature signatures = 13;

**Réserve** — Le champ « version » est la version de l'agent (exemple donné : « 1.0.0 »), non une date ni un numéro de série de certificat. Le commentaire « Next ID: 20 » indique que des numéros de champs ont été consommés puis retirés : l'historique de ces champs n'a pas été instruit.

### `L03-A3-05` — [B]

Le message AgentCardSignature de la définition Protobuf normative d'A2A ne comporte que trois champs — protected (requis), signature (requis) et header (facultatif) — et aucun champ de validité, d'expiration, de numéro de série ou de statut.

**Balayage (degré 1)** — Document : specification/a2a.proto, dépôt a2aproject/A2A, branche main, consulté le 21 juillet 2026 ; le bloc « message AgentCardSignature { … } » a été récupéré verbatim en entier. Chaînes cherchées dans ce bloc : exp, nbf, iat, expire, expiration, valid_until, not_after, lifetime, ttl, status, revoke, revocation — aucune occurrence. Seuls champs : protected = 1 (REQUIRED), signature = 2 (REQUIRED), header = 3 (google.protobuf.Struct).

- **primaire** — specification/a2a.proto — message AgentCardSignature — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/specification/a2a.proto>
  > // Required. The protected JWS header for the signature. This is always a   // base64url-encoded JSON object.   string protected = 1 [(google.api.field_behavior) = REQUIRED];

**Réserve** — Le champ header est une Struct libre : un déployeur peut y placer des paramètres non spécifiés, mais la spécification n'en prescrit aucun de nature temporelle (voir L03-A3-01).

### `L03-A3-06` — [B]

Le seul dispositif de rotation de clé prévu par la §8.4 de la spécification A2A v1.0.0 est la faculté de porter plusieurs signatures sur une même Agent Card ; la section ne prescrit ni procédure de rotation, ni période de recouvrement, ni périodicité.

**Balayage (degré 1)** — Document : docs/specification.md, dépôt a2aproject/A2A, branche main, version 1.0.0, consulté le 21 juillet 2026 ; section 8.4 récupérée verbatim et relue intégralement. Chaînes cherchées : rotate, rotation, rotating, roll-over, rollover, overlap, grace, periodic, schedule. Unique occurrence : « Multiple signatures MAY be present to support key rotation », en dernière puce des Security Considerations de la §8.4.3.

- **primaire** — Agent2Agent (A2A) Protocol Specification, §8.4.3 — Security Considerations — version 1.0.0, branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Multiple signatures **MAY** be present to support key rotation

**Réserve** — L'énoncé est en MAY : il autorise, il n'impose pas. Le champ signatures du proto est « repeated », ce qui rend la pluralité techniquement possible, sans plus.

### `L03-A3-07` — [B]

Depuis la version 1.0 d'A2A, le schéma JSON a2a.json n'est pas normatif : il est un artefact de compilation dérivé du fichier a2a.proto, non versionné dans le dépôt et régénéré à chaque construction de la documentation.

- **primaire** — A2A JSON Artifact — specification/json/README.md — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/specification/json/README.md>
  > `a2a.json` is a **non-normative build artifact** derived from the canonical proto definition at `specification/a2a.proto`. It is generated during builds and intentionally **not** committed to source control.

**Réserve** — Conséquence pratique constatée : l'URL historique du schéma (specification/json/a2a.json sur la branche main) répond 404 — voir failures. Toute vérification de champ doit donc porter sur le .proto, non sur un schéma JSON trouvé ailleurs.

### `L03-A3-08` — [B]

Le guide de découverte d'A2A (documentation d'accompagnement, non normative) rattache la fraîcheur d'un Agent Card à la sémantique de cache HTTP — en-tête Cache-Control avec max-age, ETag dérivé du champ version ou d'une empreinte de contenu, requêtes conditionnelles — et renvoie à la section 8.6 de la spécification pour les exigences normatives.

- **primaire** — Agent Discovery — Caching Considerations — branche main, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/topics/agent-discovery.md>
  > Including an `ETag` header — derived from the card's `version` field or a content hash — enables clients to make conditional requests and avoid re-downloading unchanged cards.

**Réserve** — Ce mécanisme porte sur la fraîcheur de la ressource HTTP, non sur la validité de la signature : la durée de vie ainsi obtenue est déclarée par le serveur qui sert la carte, et n'est pas couverte par la signature JWS (le champ signatures est exclu de la charge signée, et aucun paramètre temporel n'y figure — L03-A3-01). Le corpus consulté ne documente pas de durée de vie portée dans la carte signée elle-même. La §8.6, normative, n'a pas pu être ouverte : ne rien conclure de son contenu.

### `L03-A4` — [B]

La version de la spécification A2A lue est la 1.0.0, publiée le 12 mars 2026 selon le registre des versions du dépôt officiel, et le champ « signatures » de l'AgentCard y a été introduit à la version 0.3.0, publiée le 30 juillet 2025.

- **primaire** — Agent2Agent (A2A) Protocol Specification — en-tête du document — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > ??? note "**Latest Released Version** [`1.0.0`](https://a2a-protocol.org/v1.0.0/specification)
- **primaire** — Registre des versions publiées du dépôt a2aproject/A2A (API GitHub) — consulté le 2026-07-21, consultée le 2026-07-21 — <https://api.github.com/repos/a2aproject/A2A/releases?per_page=15>
  > v1.0.0 — published_at 2026-03-12T16:34:41Z ; v1.0.1 — published_at 2026-05-28T11:34:36Z ; v0.3.0 — published_at 2025-07-30T17:05:22Z
- **primaire** — Notes de version v0.3.0 du dépôt a2aproject/A2A — v0.3.0, 2025-07-30, consultée le 2026-07-21 — <https://api.github.com/repos/a2aproject/A2A/releases?per_page=15>
  > Add `signatures` to the `AgentCard` (#917)

**Réserve** — Écart à consigner, non arbitré : l'en-tête du document de spécification sur la branche main déclare « Latest Released Version 1.0.0 », alors que le registre des versions du même dépôt porte une étiquette postérieure v1.0.1 publiée le 2026-05-28. Le contenu de §8.4 a été relu sur l'étiquette v1.0.0 et concorde avec celui de main ; le contenu de v1.0.1 n'a pas été ouvert. Les énoncés L03-A1 à L03-A8 valent donc pour la 1.0.0 et ne sont pas revalidés sur la 1.0.1.

### `L03-A4-01` — [A]

Le fichier SECURITY.md publié à la racine du dépôt a2aproject/A2A tient en deux phrases et ne décrit qu'une procédure de signalement de vulnérabilité — courriel à security@lists.a2aproject.org, puis coordination et divulgation par GitHub Security Advisory ; il ne comporte aucune disposition sur la génération, la conservation, la rotation, la compromission ou la révocation de clés de signature.

**Balayage (degré 1)** — Fichier ouvert intégralement le 21 juillet 2026 (branche main, texte complet récupéré : titre « Security Policy » + deux phrases). Chaînes cherchées dans ce texte intégral : key, sign, signature, rotation, revocation, compromise, JWK, JWS — zéro occurrence. Le balayage est exhaustif par construction, le document entier tenant en trois lignes.

- **primaire** — SECURITY.md — dépôt a2aproject/A2A — branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/SECURITY.md>
  > To report a security issue, please use email <security@lists.a2aproject.org>. We use a mailing list for our intake, and do coordination and disclosure here using GitHub Security Advisory to privately discuss and fix the issue.
- **primaire** — Historique des commits touchant SECURITY.md (API GitHub) — trois derniers commits : b078419 (2025-11-20), d0ed759 (2025-10-02), 0…, consultée le 2026-07-21 — <https://api.github.com/repos/a2aproject/A2A/commits?path=SECURITY.md&per_page=3>
  > Adding project specific security list

**Réserve** — L'adresse de projet a remplacé un dispositif antérieur : le commit d0ed759 du 2 octobre 2025 porte le message « Adding project specific security list ». Le fichier n'a que trois commits en quinze mois. Registre : procédure organisationnelle, non normative pour les implémenteurs.

### `L03-A4-03` — [B]

Le seul document thématique du projet A2A consacré au déploiement en entreprise, docs/topics/enterprise-ready.md, borne son propos à TLS, authentification, autorisation, confidentialité des données, traçabilité et gestion d'API, et ne traite en aucun point de la gouvernance des clés de signature d'Agent Card.

**Balayage (degré 1)** — Document ouvert le 21 juillet 2026 (branche main). Chaînes cherchées, insensibles à la casse : signature, signing, JWS, JWK, rotat, revoc, compromis, private key, key management, HSM → 0 occurrence pour chacune. « trust » → 2 occurrences, l'une générale (« fosters trust »), l'autre relative aux autorités de certification TLS. Titres de niveau supérieur relevés dans l'ordre : Enterprise Implementation of A2A ; Transport Level Security (TLS) ; Authentication ; Authorization ; Data Privacy and Confidentiality ; Tracing, Observability, and Monitoring ; API Management and Governance.

- **primaire** — Enterprise Features (topics/enterprise-ready.md) — branche main, site publié en version 1.0, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/topics/enterprise-ready.md>
  > A2A clients should verify the A2A server's identity by validating its TLS certificate against trusted certificate authorities during the TLS handshake.

**Réserve** — Statut à dire à chaque citation : ce document n'est pas la spécification et ne déclare pas son propre statut normatif ; il mêle recommandations (« should », « strongly recommends ») et au moins une obligation rédigée en « must » (« Credentials must be transmitted in standard HTTP headers as per the requirements of the chosen authentication scheme »). Le citer comme recommandation d'implémentation, jamais comme exigence normative.

### `L03-A4-05` — [B]

La documentation « What's New in A2A Protocol v1.0 » du projet A2A indique que la vérification de signature d'Agent Card repose sur JWS avec canonicalisation JSON et que la clé publique de vérification est récupérée soit par l'en-tête `jku`, soit depuis des keystores tenus pour de confiance.

- **primaire** — What's New in A2A Protocol v1.0 (docs/whats-new-v1.md) — v1.0, comparaison avec v0.3.0 ; branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/whats-new-v1.md>
  > Supports detached signatures with public key retrieval via `jku` or trusted keystores
- **primaire** — A2A Protocol Surpasses 150 Organizations… in First Year (communiqué) — 9 avril 2026, consultée le 2026-07-21 — <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year>
  > Features include Signed Agent Cards for cryptographic identity verification
- **primaire** — What's New in A2A Protocol v1.0 — mention de l'objet vérifié — v1.0, branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/whats-new-v1.md>
  > Enables cryptographic verification of Agent Card integrity

**Réserve** — R-02 — qualifier par ce qui est démontré : la documentation du projet énonce une vérification d'INTÉGRITÉ de la carte (« verification of Agent Card integrity ») ; le communiqué de la Linux Foundation du 9 avril 2026 en parle, lui, comme d'une « cryptographic identity verification ». Les deux registres ne sont pas équivalents et la formulation du communiqué ne doit pas être reprise. Le document ne dit ni qui détient la clé privée de signature, ni par quelle procédure un keystore devient « de confiance », ni ce qu'il advient d'une carte signée par une clé compromise. Métrique auto-déclarée à attribuer à chaque occurrence si le communiqué est cité : « more than 150 organizations », chiffre avancé par la Linux Foundation.

### `L03-A4-06` — [B]

Le projet Agent2Agent est gouverné par un Technical Steering Committee dont la charte publiée attribue huit sièges nominatifs à Google, Microsoft, Cisco, Amazon Web Services, Salesforce, ServiceNow, SAP et IBM, les décisions se prenant par vote à la majorité des membres présents sous condition de quorum ; l'hébergement du projet par la Linux Foundation a été annoncé le 23 juin 2025.

- **primaire** — GOVERNANCE.md — charte du projet Agent2Agent — branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/GOVERNANCE.md>
  > The Agent2Agent project is governed by the Technical Steering Committee.
- **primaire** — GOVERNANCE.md — règle de vote — branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/GOVERNANCE.md>
  > decisions by vote at a meeting require a majority vote of those in attendance, provided quorum is met
- **primaire** — Linux Foundation Launches the Agent2Agent Protocol Project (communiqué) — 23 juin 2025, consultée le 2026-07-21 — <https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents>
  > Under the Linux Foundation's governance, A2A will remain vendor neutral, emphasize inclusive contributions

**Réserve** — Les huit sièges sont attribués nominativement à une personne par organisation (table Company / Representative / Title / Contact). Le document se désigne lui-même comme « Charter » et renvoie à un « Series Agreement » non joint au dépôt ; il ne nomme la Linux Foundation qu'une fois, à propos de la plateforme de réunion (« TSC Meetings are held on the Linux Foundation's meeting platform »). Il prévoit une révision de composition « 18 months following the inception of the Project ». À noter : A2A ne figure pas parmi les trois contributions fondatrices de l'Agentic AI Foundation annoncée par la Linux Foundation le 9 décembre 2025 (MCP, goose, AGENTS.md) — balayage de ce communiqué : 0 occurrence de « A2A » ou « Agent2Agent ».

### `L03-A4-07` — [B]

La charte du projet A2A (GOVERNANCE.md) n'attribue à aucun organe une responsabilité de gestion des clés : sa seule mention de sécurité range la politique de signalement d'incident parmi les prérogatives du Technical Steering Committee.

**Balayage (degré 1)** — GOVERNANCE.md ouvert le 21 juillet 2026 (branche main). Chaînes cherchées, insensibles à la casse : key → 0 ; cryptograph → 0 ; signature → 0 ; revoc → 0 ; rotat → 0 ; sign → 1 occurrence, dans « appointing representatives to work with other open source or open standards communities » ; security → 1 occurrence, dans l'énumération des responsabilités du TSC ; charter → 2 occurrences ; Linux Foundation → 1 occurrence.

- **primaire** — GOVERNANCE.md — responsabilités du Technical Steering Committee — branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/GOVERNANCE.md>
  > establishing community norms, workflows, issuing releases, and security issue reporting policies

**Réserve** — Le mandat cité porte sur la politique de SIGNALEMENT d'incident, procédure de coordination ; il ne constitue pas un mandat de gouvernance de clés cryptographiques. Ne pas en tirer que le TSC serait dépourvu de compétence en la matière : la charte est muette, ce qui n'est pas une exclusion.

### `L03-A4-08` — [B]

Les points d'entrée de signalement de vulnérabilité divergent d'un dépôt à l'autre de l'organisation a2aproject : le dépôt de spécification renvoie à security@lists.a2aproject.org, les SDK Python et JavaScript renvoient au programme de Google (g.co/vulnz), le SDK Java renvoie à quatre adresses individuelles chez Red Hat, et le SDK Go ne publie aucun SECURITY.md.

**Balayage (degré 1)** — Absence du SECURITY.md du SDK Go établie par deux voies le 21 juillet 2026 : requête directe sur https://raw.githubusercontent.com/a2aproject/a2a-go/main/SECURITY.md → HTTP 404 ; et listing complet de la racine du dépôt via l'API Contents (11 entrées : .gitignore, .golangci.yml, .release-please-manifest.json, AGENTS.md, CHANGELOG.md, CONTRIBUTING.md, GEMINI.md, LICENSE, README.md, go.mod, go.sum) → aucun fichier SECURITY.md. Le dépôt d'organisation a2aproject/.github, qui fournirait une politique par défaut, ne contient pas non plus de SECURITY.md (racine : .github/, profile/, .gitignore, CODE_OF_CONDUCT.md, CONTRIBUTING.md, LICENSE ; requête sur son SECURITY.md → HTTP 404).

- **primaire** — SECURITY.md — SDK Python officiel (a2aproject/a2a-python) — branche main ; fichier créé par le commit 91d278d du 2025-05-12, derni…, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/a2a-python/main/SECURITY.md>
  > To report a security issue, please use [g.co/vulnz](https://g.co/vulnz). The Google Security Team will respond within 5 working days of your report on g.co/vulnz.
- **primaire** — SECURITY.md — SDK JavaScript officiel (a2aproject/a2a-js) — branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/a2a-js/main/SECURITY.md>
  > To report a security issue, please use [g.co/vulnz](https://g.co/vulnz).
- **primaire** — Reporting of CVEs and Security Issues — SDK Java officiel (a2aproject/a2a-java) — branche main, état du 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/a2a-java/main/SECURITY.md>
  > To report a security issue, please email kkhan@redhat.com, ehugonne@redhat.com, jmesnil@redhat.com and/or smaestri@redhat.com.
- **primaire** — Listing de la racine du SDK Go (API GitHub Contents) — branche par défaut, 21 juillet 2026, consultée le 2026-07-21 — <https://api.github.com/repos/a2aproject/a2a-go/contents/>
  > go.mod
- **primaire** — Avis de sécurité publiés pour a2aproject/A2A (API GitHub) — interrogation du 21 juillet 2026, sans authentification, consultée le 2026-07-21 — <https://api.github.com/repos/a2aproject/A2A/security-advisories>
  > []

**Réserve** — Le SDK Java restreint en outre le correctif : « Note that we will only fix such issues in the most recent minor release of the A2A Java SDK. » Par ailleurs, l'API des avis de sécurité publiés du dépôt de spécification renvoie un tableau vide au 21 juillet 2026 : aucun avis publié — ce qui, sans authentification, ne dit rien d'éventuels brouillons ni des dépôts de SDK, non interrogés sur ce point.

### `L03-A5` — [A]

La spécification A2A impose (« MUST ») que le contenu de l'Agent Card soit canonicalisé selon le JSON Canonicalization Scheme du RFC 8785 avant signature, et que le champ « signatures » lui-même soit exclu du contenu signé.

- **primaire** — A2A Protocol Specification, §8.4.1 Canonicalization Requirements — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Before signing, the Agent Card content **MUST** be canonicalized using the JSON Canonicalization Scheme (JCS) as defined in [RFC 8785](https://tools.ietf.org/html/rfc8785).
- **primaire** — A2A Protocol Specification, §8.4.1 — règle 3 « Signature Field Exclusion » — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > **Signature Field Exclusion**: The `signatures` field itself **MUST** be excluded from the content being signed to avoid circular dependencies.

### `L03-A6` — [A]

La charge utile signée n'est pas transportée dans l'objet AgentCardSignature — l'entrée de signature est construite selon la formule ASCII(BASE64URL(UTF8(JWS Protected Header)) \|\| '.' \|\| BASE64URL(JWS Payload)) et le vérificateur doit reconstruire cette charge en re-canonicalisant la carte reçue — sans que la spécification nomme ce dispositif « detached » ni ne désigne laquelle des sérialisations du RFC 7515 elle emploie.

**Balayage (degré 1)** — Balayage de docs/specification.md sur l'étiquette v1.0.0 et sur la branche main, ainsi que de specification/a2a.proto (branche main), le 2026-07-21. Chaînes cherchées : « detached », « Detached », « Flattened », « Compact Serialization », « General JSON Serialization », « RFC 7797 », « b64 », « unencoded payload ». Résultat : aucune occurrence dans aucun des trois fichiers, les deux balayages du document de spécification (main et v1.0.0) et celui du fichier .proto concordant. Corroboration structurelle indépendante : les trois énumérations exhaustives des membres de AgentCardSignature (cf. L03-A2) ne comportent pas de membre « payload », alors que la sérialisation JSON aplatie du RFC 7515 en comporte un.

- **primaire** — A2A Protocol Specification, §8.4.2 — Signature Generation Process, étape 3 — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Construct the JWS Signing Input: `ASCII(BASE64URL(UTF8(JWS Protected Header)) \|\| '.' \|\| BASE64URL(JWS Payload))`
- **primaire** — A2A Protocol Specification, §8.4.3 Signature Verification — étapes imposées — étiquette v1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/v1.0.0/docs/specification.md>
  > 3. Remove properties with default values from the received Agent Card 4. Exclude the `signatures` field 5. Canonicalize the resulting JSON using RFC 8785 6. Verify the signature against the canonicalized payload

**Réserve** — Réserve de méthode sur le degré 1 : le téléchargement local des fichiers ayant été refusé par la politique d'exécution, les balayages ont été conduits au travers de l'outil de récupération distante, dont le rappel s'est révélé imparfait sur un test de contrôle (il a rapporté trois occurrences de « payload » alors que la seule §8.4.3 en contient une supplémentaire). La convergence de trois balayages indépendants et la corroboration structurelle par l'absence de membre « payload » soutiennent le degré 1, mais une re-vérification par grep local reste due avant emploi de cet énoncé comme fait négatif vérifié dans un chapitre. Le fait que le mécanisme corresponde en pratique à une charge détachée est une lecture de l'auteur, non un énoncé de la spécification.

### `L03-A7` — [A]

L'énumération normative des paramètres de l'en-tête JWS protégé d'une Agent Card A2A comprend « alg », « typ » et « kid » comme obligatoires et « jku » comme seul paramètre facultatif nommé, et ne comporte aucun paramètre de validité temporelle de la signature.

**Balayage (degré 1)** — Lecture intégrale des deux listes normatives de §8.4.2 « JWS Protected Header Parameters » (la liste « The protected header MUST include » et la liste « The protected header MAY include ») dans docs/specification.md, sur la branche main et sur l'étiquette v1.0.0, le 2026-07-21 : elles comptent respectivement trois et une entrées, sans autre. Chaînes cherchées dans le document v1.0.0 : « nbf », « iat », « exp" », « replay », « freshness » — aucune occurrence pertinente. « expired » n'apparaît qu'à propos des clés, jamais des signatures.

- **primaire** — A2A Protocol Specification, §8.4.2 — JWS Protected Header Parameters — 1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > The protected header **MUST** include: - `alg`: Algorithm used for signing (e.g., "ES256", "RS256") - `typ`: **SHOULD** be set to "JOSE" for JWS - `kid`: Key ID for identifying the signing key  The protected header **MAY** include: - `jku`: URL to JSON Web Key Set (JWKS) containing the public key

**Réserve** — Deux réserves. D'abord la spécification n'interdit pas d'autres paramètres d'en-tête : l'absence porte sur son énumération, non sur ce qu'un émetteur peut ajouter. Ensuite tension interne à consigner : l'étape 2 de vérification de §8.4.3 fait reposer la récupération de la clé publique sur « the `kid` and `jku` », alors que « jku » n'est que facultatif dans l'en-tête protégé ; une carte conforme sans « jku » n'offre au vérificateur aucun chemin de récupération de clé défini par la spécification, hors magasin de confiance préétabli.

### `L03-A8` — [A]

La spécification A2A interdit (« MUST NOT ») l'emploi de clés expirées ou révoquées pour la vérification d'une Agent Card sans définir de mécanisme permettant au client d'établir l'expiration ou la révocation d'une clé.

**Balayage (degré 1)** — Balayage de docs/specification.md sur l'étiquette v1.0.0, le 2026-07-21. Chaînes cherchées : « revocation », « revoked », « expired ». « revocation » : aucune occurrence. « revoked » et « expired » : une seule occurrence chacune, dans la même phrase des considérations de sécurité de §8.4.3 citée ci-contre. La lecture intégrale de §8.4.3 (six étapes imposées et cinq considérations de sécurité) ne fait apparaître ni liste de révocation, ni point d'état de clé, ni durée de vie de clé, ni renvoi à un mécanisme externe.

- **primaire** — A2A Protocol Specification, §8.4.3 — Security Considerations — étiquette v1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/v1.0.0/docs/specification.md>
  > Expired or revoked keys **MUST NOT** be used for verification
- **primaire** — A2A Protocol Specification, §8.4.3 — Security Considerations (suite) — étiquette v1.0.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/v1.0.0/docs/specification.md>
  > Clients **MAY** maintain a trusted key store for known agent providers ... Multiple signatures **MAY** be present to support key rotation

**Réserve** — Même réserve de méthode que L03-A6 sur la conduite du balayage à distance. C'est le cas typique du mécanisme nommé sans être défini : l'obligation est posée en toutes lettres, la procédure qui permettrait de s'y conformer ne l'est pas. La rotation de clés est, elle, nommée et outillée (signatures multiples), mais sans procédure de retrait d'une clé compromise.

