# Lot L-05 — L-05

| Champ | Valeur |
|---|---|
| Lot | **L-05** — phase **P2**, jalon J-3 |
| Débloque | **ch. 7** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 3 en [A], 0 écartée(s) par le vote. **7 échecs de source** consignés |
| Vote | **3 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **5 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L05-A1` | **[A]** ⚖ | 0 | Consultée le 21 juillet 2026, la page de la spécification « Agent Registry » du Lab Space de la Cloud Security Alliance porte l'en-tête « White Paper \| 2026-03-27 \| Status: draft » ; le Lab Space qui l'héberge se décrit comme accueillant des travaux qui ne sont pas encore un projet officiel de la CSA — le document est donc un brouillon de laboratoire, non une norme ratifiée. |
| `L05-A2` | **[B]** | 1 | Le balayage de la page de la spécification CSA « Agent Registry », telle que rendue le 21 juillet 2026, n'y fait apparaître aucune chaîne de date postérieure au 27 mars 2026, ni section de révision, ni mention « last updated » ou « modified » : le relevé ne soutient pas l'affirmation d'une mise à jour de cette spécification au 20 mai 2026. |
| `L05-A3` | **[B]** | 0 | Dans la version consultée le 21 juillet 2026 (en-tête 2026-03-27), la spécification CSA « Agent Registry » range `toolAccessList` et `permissionBoundaries` parmi les champs obligatoires du schéma de profil d'agent, le premier énumérant les outils et serveurs MCP que l'agent est autorisé à invoquer, le second portant limites de portée, contraintes d'accès aux données et actions prohibées. |
| `L05-A4` | **[B]** | 0 | La spécification CSA « Agent Registry » se déclare conçue pour se composer avec des travaux existants et désigne le brouillon IETF `draft-abbey-scim-agent-extension` comme son modèle d'interopérabilité pour l'approvisionnement inter-domaines d'agents, en le citant dans sa version -00 de 2025. |
| `L05-A5` | **[A]** ⚖ | 2 | Au 21 juillet 2026, la fiche IETF de `draft-abbey-scim-agent-extension` le donne pour « Expired Internet-Draft (individual) », expiré et archivé, en une unique version -00 datée du 16 octobre 2025, sans flux (« stream ») ni adoption par un groupe de travail, et porte la mention qu'il n'est pas endossé par l'IETF et n'a aucun statut formel dans le processus de normalisation. |
| `L05-A6` | **[B]** | 2 | À la session du groupe de travail SCIM de l'IETF 125, tenue le 19 mars 2026, Pamela Dingle et Ismael Kazzouzi ont présenté une consolidation des brouillons `draft-abbey-scim-agent-extension` et `draft-wahl-scim-agent-schema`, et la conclusion consignée au procès-verbal est qu'il faut d'abord apporter des cas d'usage avant de porter le brouillon plus loin — aucun appel à adoption n'y est consigné. |
| `L05-A7` | **[B]** | 0 | Au 21 juillet 2026, le brouillon `draft-wzdk-scim-agent-resource-00` — « AI Agent Resource Extension for the System for Cross-domain Identity Management (SCIM) », révision du 5 juin 2026, expirant le 7 décembre 2026 — est actif mais demeure une soumission individuelle de quatre auteurs (Mark Wahl, Microsoft ; Danny Zollner, Okta ; Pamela Dingle, Microsoft ; Ismael Kazzouzi, Nextident), et non un document du groupe de travail S… |
| `L05-A8` | **[A]** ⚖ | 2 | La documentation du protocole A2A (version publiée 1.0.0, projet hébergé par la Linux Foundation) définit un chemin de découverte normalisé `https://{agent-server-domain}/.well-known/agent-card.json`, énumère trois stratégies de découverte — URI bien connue, registres organisés, configuration directe — et déclare explicitement que la spécification courante ne prescrit pas d'API normalisée pour les registres organisés. |
| `L05-A9` | **[B]** | 0 | Le registre d'AGNTCY — l'Agent Directory Service — est spécifié dans le brouillon IETF `draft-mp-agntcy-ads`, dont la révision 02 du 6 juillet 2026, de statut visé « Informational » et expirant le 7 janvier 2027, demeure une soumission individuelle de deux auteurs de Cisco ; il stocke les enregistrements comme artefacts OCI adressés par contenu, les annonce et les découvre par table de hachage distribuée, et prévoit une signat… |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 5 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L05-A3` | **statut non dit** | Dans la version consultée le 21 juillet 2026, le brouillon CSA « Agent Registry » (en-tête « White Paper \| 2026-03-27 \| Status: draft ») range `toolAccessList` et `permissionBoundaries` parmi les champs qu'il déclare obligatoires dans son schéma de profil d'agent : le premier énumère les outils et serveurs MCP que l'agent est autorisé à invoquer, le second porte limites de portée, contraintes d'accès aux données et… |
| `L05-A4` | **statut non dit** | Le brouillon CSA « Agent Registry » (statut « draft », en-tête 2026-03-27) déclare être conçu pour se composer avec des travaux existants et y désigne le brouillon IETF `draft-abbey-scim-agent-extension` comme modèle d'interopérabilité pour l'approvisionnement inter-domaines d'agents, en le citant dans sa version -00 de 2025. |
| `L05-A5` | **degré injustifié** | Au 21 juillet 2026, la fiche IETF Datatracker de `draft-abbey-scim-agent-extension` affiche l'état « Expired Internet-Draft (individual) », ne liste qu'une révision, -00, datée du 16 octobre 2025, ne renseigne aucun flux (« stream ») ni groupe de travail adoptant, et porte la mention type selon laquelle un Internet-Draft n'est pas endossé par l'IETF et n'a aucun statut formel dans le processus de normalisation. |
| `L05-A8` | **négatif de corpus** | La section de la documentation A2A 1.0.0 consacrée à la découverte d'agents (projet hébergé par la Linux Foundation) définit le chemin `https://{agent-server-domain}/.well-known/agent-card.json`, y énumère trois stratégies de découverte — URI bien connue, registres organisés, configuration directe — et y déclare que la version courante de la spécification ne prescrit pas d'API normalisée pour les registres organisés. |
| `L05-A9` | **promesse non démontrée** | Le brouillon IETF `draft-mp-agntcy-ads` — révision 02 du 6 juillet 2026, statut visé « Informational », expirant le 7 janvier 2027, soumission individuelle de deux auteurs de Cisco — spécifie l'Agent Directory Service d'AGNTCY : il prescrit un stockage des enregistrements sous forme d'artefacts OCI adressés par contenu, une annonce et une découverte par table de hachage distribuée, et une signature fondée sur Sigstor… |

## D. Échecs de source consignés (7)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Jeu de diapositives « SCIM Agentic Draft Progress » présenté à la session SCIM de l'IETF 125 — extraction verbatim des titres de diapositives, des brouillons co… | Fichier PDF de 73,5 ko à flux de contenu compressés (deflate) ; l'outil de récupération n'a pu extraire aucun texte fiable et a refusé de paraphraser. Seul le titre de métadonnée « SCIM Agent Workstream » a été lisible. L'affirmation L05-A6… |
| Section 14.3 « Well-Known URI Registration » de la spécification A2A — vérification de l'enregistrement IANA du chemin `.well-known/agent-card.json` et des énon… | Contenu de la page tronqué à la récupération : la table des matières atteste l'existence de la section 14.3, mais son corps n'a pas été rendu. Aucune citation verbatim possible. |
| Page d'aperçu de l'Agent Directory d'AGNTCY sur le site de documentation principal | La page ne renvoie qu'un avis de redirection sans contenu de destination. Contournée par https://dir.agntcy.org/latest/dir/dir-overview/, qui a rendu le contenu. |
| Billet d'annonce de la version 1.0 du protocole A2A — date de publication et énoncés de stabilité | HTTP 404 Not Found. La chaîne de version « Latest Released Version 1.0.0 » a été relevée sur la page de spécification, mais aucune date de publication de la v1.0 n'est établie à la source primaire ; les dates circulant en presse secondaire… |
| Procès-verbal de la session SCIM de l'IETF 125 par l'URL canonique de document | HTTP 404 Not Found. Contourné par la fiche de session puis l'URL de matériel minutes-125-scim-202603190100-01, qui a rendu le contenu. |
| Vérification de la date de dernière modification de la page CSA par en-tête HTTP ou métadonnée de CMS (pour trancher la question du 20 mai 2026) | L'outil de récupération convertit la page en markdown et n'expose ni les en-têtes HTTP (Last-Modified, ETag) ni les balises meta (article:modified_time). Récupération directe par ligne de commande refusée par la politique d'exécution de l'e… |
| Toutes les recherches et récupérations web pendant les dix premières minutes de la session | Indisponibilité du classificateur de sûreté de l'environnement (« claude-sonnet-5[1m] is temporarily unavailable »). Six appels rejetés avant rétablissement ; aucune source perdue, toutes reprises ensuite. |

## E. Ce que le lot déclare n'avoir pas couvert

Ce que ce lot N'A PAS couvert, et pourquoi.  1. **La date du 20 mai 2026 n'est pas retrouvée** — c'était la première tâche du lot, et son résultat est négatif : la page CSA telle que rendue le 21 juillet 2026 ne porte que « 2026-03-27 \| Status: draft ». Le relevé ne soutient pas la mise à jour au 20 mai 2026 consignée en verification/revalidation-2026-07-21.md §2.3 (b) ; il ne la réfute pas non plus (une édition sur place sans changement d'en-tête serait indétectable par ce balayage). ⚠ **H-03 ne doit donc pas être amendée sur la foi de cette date** : soit la revalidation d'ouverture produit la pièce d'où elle tenait le 20 mai, soit la date tombe. C'est une remontée de gouvernance, pas une décision d'agent.  2. **Le socle hérité était périmé sur un autre point, plus lourd que la version CSA** : la revalidation du 21 juillet 2026 conclut « Aucune consolidation IETF n'est constatée — ni à l'IETF 125 ni ailleurs ». C'est **faux à la source**. Une consolidation a bien été présentée à l'IETF 125 le 19 mars 2026 (L05-A6), et un brouillon actif à quatre auteurs, `draft-wzdk-scim-agent-resource-00`, a été publié le 5 juin 2026 (L05-A7). Le sens de la réserve tient — rien n'est adopté par le groupe de travail, rien n'est ratifié — mais l'énoncé « aucune consolidation » ne tient plus.  3. **Non couvert faute de source ouverte** : le jeu de diapositives « SCIM Agentic Draft Progress » de l'IETF 125 (PDF non extractible) ; la section 14.3 « Well-Known URI Registration » de la spécification A2A, donc l'enregistrement IANA effectif du chemin `.well-known/agent-card.json` ; le régime de gouvernance et de révocation des registres A2A (la spécification ne prescrivant pas d'API de registre, il n'y a rien à relever de ce côté sans passer à des mises en œuvre particulières).  4. **Ouvert mais non porté en entrée**, faute de place (plafond de neuf) : la découverte fédérée de la spécification CSA et l'exclusion par défaut de `behavioralFingerprints` et du détail des `permissionBoundaries` (citation verbatim conservée au caveat de L05-A3) ; les cinq composantes de la spécification CSA et son API conforme à OpenAPI 3.1 ; l'alignement déclaré sur l'OWASP Top 10 for Agentic Applications (2026), ASI03/ASI07/ASI10 — ⚠ **cet alignement figure déjà dans la version du 27 mars 2026 et n'est donc pas un indice de mise à jour postérieure**, contrairement à ce que la revalidation d'ouverture en tirait.  5. **Non instruit, hors périmètre de L-05** : les annonces CSA de mai 2026 (autorisation comme CVE Numbering Authority, acquisition des spécifications AARM et Agentic Trust Framework, STAR for AI Catastrophic Risk Annex) ne sont connues ici que par presse secondaire ; aucune n'est portée en affirmation. Le brouillon voisin `draft-jimenez-agent-directory` et `draft-narajala-ans` (Agent Name Service) ont été aperçus au fil des recherches et **n'ont pas été ouverts** : ils élargiraient l'inventaire des registres concurrents du ch. 7 et méritent un passage complémentaire.  6. **Rappel de qualification, à tenir à chaque mention** : la spécification CSA est un brouillon de laboratoire, non une norme ratifiée ; `draft-wzdk-scim-agent-resource-00` et `draft-mp-agntcy-ads-02` sont des soumissions individuelles actives, non des documents de groupe de travail ; `draft-abbey-scim-agent-extension` et `draft-wahl-scim-agent-schema` sont expirés et archivés. Quatre statuts distincts, quatre formulations distinctes.

## F. Sources et citations

### `L05-A1` — [A]

Consultée le 21 juillet 2026, la page de la spécification « Agent Registry » du Lab Space de la Cloud Security Alliance porte l'en-tête « White Paper \| 2026-03-27 \| Status: draft » ; le Lab Space qui l'héberge se décrit comme accueillant des travaux qui ne sont pas encore un projet officiel de la CSA — le document est donc un brouillon de laboratoire, non une norme ratifiée.

**Balayage (degré 0)** — En-tête du document et page racine du Lab Space ouvertes toutes deux le 21 juillet 2026 ; index du Lab Space (labs.cloudsecurityalliance.org/agentic/) ouvert le même jour : la spécification y est listée « Agent Registry Specification (v1) », sans autre étiquette de statut.

- **primaire** — Agent Registry Specification — 2026-03-27, Status: draft, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > **White Paper** \| 2026-03-27 \| Status: draft
- **primaire** — CSA Lab Space — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/>
  > This could be open source software tools, research – anything that aligns with CSA's mission, but is not yet an official project.

**Réserve** — Le statut « draft » est celui que le document se donne à lui-même ; aucune procédure de ratification CSA n'est décrite sur la page. Le Lab Space ne publie pas d'avertissement formel distinct : la réserve tient à la formule de la page racine, pas à un encadré de mise en garde.

### `L05-A2` — [B]

Le balayage de la page de la spécification CSA « Agent Registry », telle que rendue le 21 juillet 2026, n'y fait apparaître aucune chaîne de date postérieure au 27 mars 2026, ni section de révision, ni mention « last updated » ou « modified » : le relevé ne soutient pas l'affirmation d'une mise à jour de cette spécification au 20 mai 2026.

**Balayage (degré 1)** — Page ouverte deux fois le 21 juillet 2026 (deux requêtes distinctes, mêmes résultats). Chaînes cherchées : « last updated », « updated », « modified », « revision », « changelog », « 2026-05 », « May 2026 », et relevé exhaustif de toutes les chaînes de date de la page. Dates trouvées, dans l'ordre : 2026-03-27 ; 2026-02-01 ; 2026-03-15T09:00:00Z ; 2026-03-15T14:30:00Z ; 2026-02-01 ; November 2025 ; October 2025 ; November 20, 2025 ; May 2025 ; February 2025 ; July 2025 ; January 2023 ; August 20, 2025. Aucune postérieure au 27 mars 2026. L'index du Lab Space listant la spécification ne porte pas non plus de date de mise à jour, là où d'autres pièces du même index portent des horodatages (« 20260327 », « 20260328 »).

- **primaire** — Agent Registry Specification — 2026-03-27, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > **White Paper** \| 2026-03-27 \| Status: draft
- **primaire** — CSAI 2026 Strategic Mission Documents — index du Lab Space agentique — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/>
  > Agent Registry Specification

**Réserve** — Fait négatif borné à ce que rend la page en texte : il ne porte ni sur les en-têtes HTTP, ni sur les métadonnées du CMS, ni sur un éventuel historique de version non publié. Une édition sur place sans changement d'en-tête ne laisserait aucune trace détectable par ce balayage. Conclusion à écrire « le relevé ne soutient pas », jamais « la mise à jour n'a pas eu lieu ». ⚠ Conséquence directe pour H-03 : la révision d'ouverture du 21 juillet 2026 (verification/revalidation-2026-07-21.md §2.3 b) datait la spécification du 20 mai 2026 ; cette date n'est pas retrouvée à la source et doit être re-instruite avant amendement du socle.

### `L05-A3` — [B]

Dans la version consultée le 21 juillet 2026 (en-tête 2026-03-27), la spécification CSA « Agent Registry » range `toolAccessList` et `permissionBoundaries` parmi les champs obligatoires du schéma de profil d'agent, le premier énumérant les outils et serveurs MCP que l'agent est autorisé à invoquer, le second portant limites de portée, contraintes d'accès aux données et actions prohibées.

**Balayage (degré 0)** — Table des champs de la section « Agent Profile Schema » relevée intégralement : champs obligatoires — agentId, displayName, agentVersion, frameworkId, frameworkVersion, foundationModelId, foundationModelVersion, capabilities, toolAccessList, permissionBoundaries, owningOrganization, ownerEmail, deploymentContext, behavioralFingerprints, registrationTimestamp, lastModifiedTimestamp, status ; champs optionnels — trustProfileRef, lineageRef, externalCertifications, metadata. Les deux champs figurent aussi dans l'exemple JSON de la même section.

- **primaire** — Agent Registry Specification — Agent Profile Schema — 2026-03-27, Status: draft, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > The `toolAccessList` specifies explicit list of tools and MCP servers the agent is authorized to invoke
- **primaire** — Agent Registry Specification — Trust Profile / federated discovery — 2026-03-27, Status: draft, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > A capability expansion — the addition of new entries to the `capabilities` or `toolAccessList` fields — invalidates the Trust Profile for the same reason.

**Réserve** — Deux règles attachées à ces champs ne figurent pas au socle hérité (H-03) et sont à porter au ch. 7 : (i) « A capability expansion — the addition of new entries to the `capabilities` or `toolAccessList` fields — invalidates the Trust Profile for the same reason. » ; (ii) « The `behavioralFingerprints` array and full `permissionBoundaries` details are excluded from federated responses by default. » La première fait du profil de confiance un objet à durée de vie conditionnelle ; la seconde borne ce qu'une fédération de registres expose. R-02 s'applique : le document décrit un régime de champs et d'invalidation, il ne démontre aucune propriété cryptographique par ce seul fait.

### `L05-A4` — [B]

La spécification CSA « Agent Registry » se déclare conçue pour se composer avec des travaux existants et désigne le brouillon IETF `draft-abbey-scim-agent-extension` comme son modèle d'interopérabilité pour l'approvisionnement inter-domaines d'agents, en le citant dans sa version -00 de 2025.

**Balayage (degré 0)** — Section de composition avec les standards existants et bloc de références bibliographiques de la spécification, ouverts le 21 juillet 2026 ; la citation complète relevée est « M. Abbey and R. S. Cohen (Okta), 'SCIM Agents and Agentic Applications Extension,' IETF Internet-Draft draft-abbey-scim-agent-extension-00, 2025. »

- **primaire** — Agent Registry Specification — composition with existing standards — 2026-03-27, Status: draft, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > The IETF draft-abbey-scim-agent-extension draft provides an existing interoperability model for cross-domain agent provisioning.
- **primaire** — Agent Registry Specification — composition with existing standards — 2026-03-27, Status: draft, consultée le 2026-07-21 — <https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/>
  > SPIFFE/SPIRE provides the workload attestation layer on which agent cryptographic identities are anchored.

**Réserve** — La même phrase de composition adosse aussi la spécification à SPIFFE/SPIRE (couche d'attestation de charge de travail) et aux Verifiable Credentials du W3C (format d'attestation portable). ⚠ À lire avec L05-A5 : le brouillon désigné comme « modèle d'interopérabilité » est expiré et archivé, et n'a été adopté par aucun groupe de travail.

### `L05-A5` — [A]

Au 21 juillet 2026, la fiche IETF de `draft-abbey-scim-agent-extension` le donne pour « Expired Internet-Draft (individual) », expiré et archivé, en une unique version -00 datée du 16 octobre 2025, sans flux (« stream ») ni adoption par un groupe de travail, et porte la mention qu'il n'est pas endossé par l'IETF et n'a aucun statut formel dans le processus de normalisation.

**Balayage (degré 2)** — Fiche datatracker ouverte le 21 juillet 2026 : ligne de statut « Expired Internet-Draft (individual) », version 00 du 16 octobre 2025, dernière mise à jour au 19 avril 2026, « (No stream defined) », aucune ligne « Replaced by », auteurs Macy Abbey et Rafael S. Cohen.

- **primaire** — draft-abbey-scim-agent-extension-00 — SCIM Agents and Agentic Applications Extension — version 00 du 16 octobre 2025 ; expiré (dernière mise à jour 2026-04-1…, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-abbey-scim-agent-extension/>
  > Expired Internet-Draft (individual)
- **primaire** — draft-scim-agent-extension-00 — SCIM Agents and Agentic Applications Extension — version 00 du 11 octobre 2025 ; expiré (dernière mise à jour 2026-04-1…, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-scim-agent-extension/>
  > Expired Internet-Draft (individual)

**Réserve** — Le fait négatif est de degré 2 : il repose sur la réserve explicite que porte le registre (« not endorsed by the IETF », « no formal standing », absence de flux), non sur un balayage exhaustif des adoptions de groupes de travail. ⚠ Piège de renvoi : le datatracker porte une seconde fiche au nom voisin `draft-scim-agent-extension` (sans préfixe d'auteur), même titre, mêmes auteurs, version 00 du 11 octobre 2025, dernière mise à jour au 14 avril 2026, également « Expired Internet-Draft (individual) ». Un renvoi non qualifié désigne deux objets ; nommer le nom complet du brouillon à chaque citation.

### `L05-A6` — [B]

À la session du groupe de travail SCIM de l'IETF 125, tenue le 19 mars 2026, Pamela Dingle et Ismael Kazzouzi ont présenté une consolidation des brouillons `draft-abbey-scim-agent-extension` et `draft-wahl-scim-agent-schema`, et la conclusion consignée au procès-verbal est qu'il faut d'abord apporter des cas d'usage avant de porter le brouillon plus loin — aucun appel à adoption n'y est consigné.

**Balayage (degré 2)** — Fiche de session IETF 125 / SCIM ouverte le 21 juillet 2026 : « Thursday, March 19, 2026 at 01:00 UTC », quatre jeux de diapositives dont « SCIM Agentic Draft Progress ». Procès-verbal officiel (minutes-125-scim-202603190100-01) ouvert le même jour : brouillons combinés nommés « draft-abbey-scim-agent-extension/ » et « draft-wahl-scim-agent-schema/ » ; réserve de Bjorn Hjelm sur la définition du terme « agent ».

- **primaire** — Minutes — SCIM WG, IETF 125 — session du 19 mars 2026, minutes révision 01, consultée le 2026-07-21 — <https://datatracker.ietf.org/meeting/125/materials/minutes-125-scim-202603190100-01>
  > before we bring draft, I hear that we need to bring use cases; will take that back as feedback.
- **primaire** — IETF 125 — session du groupe de travail SCIM — Thursday, March 19, 2026 at 01:00 UTC, consultée le 2026-07-21 — <https://datatracker.ietf.org/meeting/125/session/scim/>
  > Thursday, March 19, 2026 at 01:00 UTC
- **primaire** — draft-wahl-scim-agent-schema-01 — System for Cross-domain Identity Management: Agentic Identity Schema — version 01 du 18 août 2025 ; expiré, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-wahl-scim-agent-schema/>
  > Expired Internet-Draft (individual)

**Réserve** — Le fait négatif — pas d'appel à adoption — est de degré 2 : il repose sur ce que le procès-verbal consigné rapporte, non sur un balayage de l'ensemble des actes du groupe. Le jeu de diapositives « SCIM Agentic Draft Progress » n'a pas pu être extrait (PDF compressé, voir failures) : la présente affirmation repose sur le procès-verbal seul. `draft-wahl-scim-agent-schema-01` (Mark Wahl, Microsoft) est lui aussi « Expired Internet-Draft (individual) », dernière révision du 18 août 2025.

### `L05-A7` — [B]

Au 21 juillet 2026, le brouillon `draft-wzdk-scim-agent-resource-00` — « AI Agent Resource Extension for the System for Cross-domain Identity Management (SCIM) », révision du 5 juin 2026, expirant le 7 décembre 2026 — est actif mais demeure une soumission individuelle de quatre auteurs (Mark Wahl, Microsoft ; Danny Zollner, Okta ; Pamela Dingle, Microsoft ; Ismael Kazzouzi, Nextident), et non un document du groupe de travail SCIM.

**Balayage (degré 0)** — Fiche datatracker du brouillon ouverte le 21 juillet 2026 : « Active Internet-Draft (individual) », « 5 June 2026 », « 7 December 2026 », aucun champ « Replaces », aucun flux assigné. Le corps du brouillon définit un type de ressource Agent avec attributs requis `active`, `displayName`, `agentUserName`, et attributs `description` et `owners`.

- **primaire** — draft-wzdk-scim-agent-resource-00 — AI Agent Resource Extension for SCIM — révision 00 du 5 juin 2026 ; expire le 7 décembre 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-wzdk-scim-agent-resource/00/>
  > Active Internet-Draft (individual)
- **primaire** — draft-wzdk-scim-agent-resource — page du document — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-wzdk-scim-agent-resource/>
  > This Internet-Draft is submitted in full conformance with the provisions of BCP 78 and BCP 79.

**Réserve** — La date du 7 décembre 2026 est l'expiration automatique d'un Internet-Draft (six mois), non un jalon de publication : PROGRAMMÉ au sens mécanique, elle ne dit rien d'une adoption. ⚠ Ne pas écrire que ce brouillon « est » le produit de la consolidation présentée à l'IETF 125 : la concordance des noms d'auteurs avec les présentateurs est un indice, pas une filiation documentée — aucune source ouverte ne l'établit. Un brouillon individuel actif n'est pas une norme, et se dit comme tel à chaque mention (R-09).

### `L05-A8` — [A]

La documentation du protocole A2A (version publiée 1.0.0, projet hébergé par la Linux Foundation) définit un chemin de découverte normalisé `https://{agent-server-domain}/.well-known/agent-card.json`, énumère trois stratégies de découverte — URI bien connue, registres organisés, configuration directe — et déclare explicitement que la spécification courante ne prescrit pas d'API normalisée pour les registres organisés.

**Balayage (degré 2)** — Page « Agent Discovery » de a2a-protocol.org et sa source dans le dépôt a2aproject/A2A (docs/topics/agent-discovery.md) ouvertes le 21 juillet 2026 ; page de spécification a2a-protocol.org/latest/specification/ ouverte le même jour, portant « Latest Released Version 1.0.0 ».

- **primaire** — A2A — Agent Discovery (source du dépôt officiel) — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://github.com/a2aproject/A2A/blob/main/docs/topics/agent-discovery.md>
  > The current A2A specification does not prescribe a standard API for curated registries.
- **primaire** — Agent Discovery — A2A Protocol — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://a2a-protocol.org/latest/topics/agent-discovery/>
  > https://{agent-server-domain}/.well-known/agent-card.json
- **primaire** — A2A Protocol Specification — Latest Released Version 1.0.0, consultée le 2026-07-21 — <https://a2a-protocol.org/latest/specification/>
  > Latest Released Version

**Réserve** — Fait négatif de degré 2 : la réserve est portée en toutes lettres par la documentation du projet lui-même, non par un balayage du texte normatif de la spécification. La section 14.3 « Well-Known URI Registration » de la spécification n'a pas pu être extraite (contenu tronqué, voir failures) : l'enregistrement effectif du chemin auprès de l'IANA n'est donc pas constaté ici. La documentation note par ailleurs qu'une carte d'agent porteuse de données sensibles doit être protégée par authentification et autorisation — exigence de déploiement, non propriété démontrée du format (R-02).

### `L05-A9` — [B]

Le registre d'AGNTCY — l'Agent Directory Service — est spécifié dans le brouillon IETF `draft-mp-agntcy-ads`, dont la révision 02 du 6 juillet 2026, de statut visé « Informational » et expirant le 7 janvier 2027, demeure une soumission individuelle de deux auteurs de Cisco ; il stocke les enregistrements comme artefacts OCI adressés par contenu, les annonce et les découvre par table de hachage distribuée, et prévoit une signature fondée sur Sigstore.

**Balayage (degré 0)** — Fiche datatracker de draft-mp-agntcy-ads ouverte le 21 juillet 2026 (révisions 00, 01 du 24 février 2026, 02 du 6 juillet 2026 ; auteurs Luca Muscariello et Ramiz Polic, Cisco ; expiration 7 janvier 2027). Page « Agent Directory Service » de dir.agntcy.org ouverte le même jour : adressage par contenu pour l'unicité globale, tables de hachage distribuées pour la découverte, interfaces gRPC et protocol buffers, mécanismes cryptographiques d'intégrité et de provenance.

- **primaire** — draft-mp-agntcy-ads-02 — Agent Directory Service — révision 02 du 6 juillet 2026 ; expire le 7 janvier 2027 ; Information…, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-mp-agntcy-ads/>
  > Active Internet-Draft (individual)
- **primaire** — Overview — Agent Directory Service — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://dir.agntcy.org/latest/dir/dir-overview/>
  > The Agent Directory Service (ADS) is a distributed directory service designed to store metadata for AI agent applications.

**Réserve** — ⚠ La page de documentation d'AGNTCY qualifie elle-même la spécification d'« under active development as an IETF Internet Draft » : un brouillon individuel n'est ni adopté ni ratifié, et se dit ainsi à chaque mention (R-09). La signature Sigstore est un mécanisme déclaré par la spécification ; ce que la mise en œuvre démontre effectivement n'a pas été vérifié ici (R-02). La page docs.agntcy.org/dir/overview/ n'a pas rendu son contenu (redirection, voir failures) ; le relevé passe par dir.agntcy.org.

