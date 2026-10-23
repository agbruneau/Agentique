# Audit d'actualité du Compendium — horizon du 31 décembre 2026

| Champ | Valeur |
|---|---|
| **Nature** | Audit seulement. Ni le PDF, ni les `.md`, ni le socle, ni le `JOURNAL.md` ne sont modifiés. Aucune décision d'auteur n'est numérotée pour cette passe. |
| **Date** | 22 octobre 2026 |
| **Objet** | `Compendium.pdf` (rendu Typst du 15 septembre 2026, recomposé le 19 octobre 2026, 1 000 pages) : gel du 27 juillet 2026, revalidation du 2 septembre 2026 |
| **Question** | Quels énoncés auront changé ou risquent de changer d'ici le 31 décembre 2026 ? |
| **Pagination** | « f. » = folio imprimé ; « PDF » = page du fichier ; PDF = f. + 14 (vérifié sur le rendu). |
| **Méthode** | Texte extrait par `pdftotext` ; 2 076 phrases datées ou prospectives repérées, 1 318 retenues après retrait des dates de procédure interne, toutes lues ; index de départ : les 484 repères de `window.ATLAS`. Faits confrontés en ligne le 22 octobre 2026 (sources à la fin). |
| **Régimes de preuve** | **Vérifié** : source primaire consultée. **Vérifié (secondaires)** : au moins deux sources secondaires concordantes, source primaire inaccessible ou non trouvée. **Supposé** : déduit ou non vérifié ; ce qui trancherait la question est nommé. |
| **Urgence** | **Haute** : l'énoncé est faux ou trompeur au 22 octobre 2026. **Moyenne** : version ou statut supplanté, ou échéance d'ici le 31 décembre 2026 qui imposera une reprise. **Basse** : temps grammatical, compte à rebours daté, version mineure, veille. |

---

## Résumé

**Résultat.** Huit constats d'urgence haute, onze de moyenne et vingt-deux de basse. Vingt et un faits contrôlés sont inchangés, dont un seulement supposé (CycloneDX), et n'appellent aucune correction (§ 7).

1. **Le report de l'AI Act a été publié avant le gel.** Le règlement (UE) 2026/1744 a paru au JO le 24 juillet 2026 et est en vigueur depuis le 27 juillet. Les ch. 30, 34 et 49 l'écrivent encore « sous réserve de publication » (H-01).
2. **A2A a rejoint l'Agentic AI Foundation le 17 août 2026.** Les ch. 7 et 37 le placent encore en projet autonome de la Linux Foundation (H-02).
3. **La révision MCP 2026-07-28 reste « annoncée au brouillon »** dans sept chapitres que la revalidation n'a pas repris (ch. 19, 20, 37, 39, 46, 47, 48). La revalidation du 2 septembre déclarait les ch. 36 et 46 intacts ; ils ne le sont pas (H-03, M-03).
4. **La loi canadienne sur les cryptomonnaies stables est adoptée** (C-15, sanction royale du 26 mars 2026). Le ch. 36 parle d'une « annonce, non texte adopté » (H-04).
5. **Swift a reporté le retrait des adresses non structurées** prévu le 14 novembre 2026. Le ch. 31 l'attend encore (H-05).
6. **Le CSF a publié son rapport final le 15 octobre 2026.** Le ch. 31 l'annonce encore comme à venir (H-06).
7. **Côté IETF :** le chaînage d'identité inter-domaines est en file de l'éditeur des RFC (H-07). Le groupe WIMSE a adopté un document sur l'authentification des agents d'IA, `draft-ietf-wimse-aims-00` (H-08). Les jetons de transaction sont passés à la révision −11, avec consensus du groupe de travail (M-01).
8. **Échéances d'ici le 31 décembre 2026 :**
   - lancement du rail temps réel visé au T4 (M-04) ;
   - directive (UE) 2024/2853 : transposition au 9 décembre, application aux produits mis sur le marché **après le 8 décembre** depuis un rectificatif (M-05) ;
   - portefeuilles d'identité européens au 24 décembre (M-06).

**Ce qui tient.** E-23 et la ligne directrice de l'AMF entrent toujours en vigueur le 1ᵉʳ mai 2027. Ont aussi été confirmés : NIST IR 8547 encore au stade de projet ; C-36 sans activité depuis la première lecture ; A2A en v1.0.1 ; MCP sans révision postérieure au 28 juillet ; AP2 en v0.2.0, non transféré ; aucune désignation d'organisme de normalisation pour le cadre bancaire n'a été trouvée.

**Recommandation de méthode.** La revalidation du 2 septembre ne couvrait qu'une publication antérieure au 2 octobre 2026 (§ 50.3). Prochaine passe recommandée : **début janvier 2027**. Elle tiendrait compte du RTR, des échéances européennes de décembre et du nouveau calendrier Swift, et suivrait l'ordre du protocole : socle d'abord (S-001, S-002, S-027, S-032/S-033, S-075, S-096, S-102, S-131, S-030), chapitres ensuite.

---

## 1. Urgence haute

### H-01 — AI Act : le report est publié depuis le 24 juillet 2026, soit avant le gel

- **Où :**
  - ch. 30 § 30.1.1, f. 523-524 · PDF 537-538 ;
  - ch. 30 § 30.2.3, f. 530 · PDF 544 ;
  - ch. 34 : f. 593 · PDF 607 ; f. 601 · PDF 615 ; tableau 34.3, f. 616 · PDF 630 ;
  - ch. 49 § 49.0.2, f. 863 · PDF 877 ; § 49.1.1, f. 865 · PDF 879 ;
  - ch. 10, f. 187 · PDF 201.
- **Énoncé :** le report est « adopté dans la fenêtre du socle, sous la seule réserve de la publication officielle à suivre » ; « tant que la publication n'est pas intervenue, une architecture prudente conserve la trajectoire antérieure » ; « publication au Journal officiel à suivre ». Au ch. 10 : « la mise en conformité générale se poursuivant jusqu'au 2 août 2027 ».
- **Constat (vérifié) :**
  - le règlement (UE) 2026/1744 (« Digital Omnibus on AI ») est adopté le 8 juillet 2026, publié au JO L le 24.7.2026 et en vigueur le 27 juillet 2026 (EEA-Lex de l'AELE ; Hunton, 28 juillet 2026) ;
  - le régime de l'annexe III s'applique au 2 décembre 2027, celui de l'annexe I au 2 août 2028 ;
  - la publication précède le gel de trois jours : la réserve était déjà caduque au 27 juillet.
- **Correction :**
  - citer le règlement 2026/1744 et sa date de publication ;
  - retirer la réserve de publication et la consigne de « trajectoire antérieure » ;
  - au tableau 34.3, remplacer « report adopté sous réserve de publication » par « report publié (Règl. 2026/1744), en vigueur le 27 juillet 2026 » ;
  - au ch. 10, distinguer GPAI (2 août 2025 et 2 août 2027), annexe III (2 décembre 2027) et annexe I (2 août 2028) ;
  - au ch. 30 (PDF 537), passer au passé « le pouvoir de supervision et de sanction […] à partir du 2 août 2026 ».
  - *Supposé :* l'échéance de marquage des contenus synthétiques, écrite « au 2 décembre 2026 » (PDF 544), ne viserait selon des sources secondaires que les systèmes mis sur le marché avant le 2 août 2026. À vérifier sur l'art. 50 modifié du règlement 2026/1744.

### H-02 — A2A est hébergé par l'Agentic AI Foundation depuis le 17 août 2026

- **Où :**
  - ch. 7 § 7.4.1, f. 126 · PDF 140 : « Deux protocoles relèvent directement de la fondation faîtière ; le troisième relève d'une fondation dédiée » ;
  - ch. 7 § 7.4.2, f. 128 · PDF 142 : l'AAIF « accueille […] le protocole agent-outil, un environnement d'exécution d'agents et un format de configuration » ;
  - ch. 7 § 7.6, f. 130 · PDF 144 : « la Linux Foundation — fondation faîtière des deux protocoles » ;
  - ch. 37 § 37.2.3, f. 664 · PDF 678 : « transféré à la Linux Foundation en juin 2025 » ;
  - ch. 37, tableau du § 37.2.1, f. 662 · PDF 676 : agentgateway, « projet déclaré de la Linux Foundation » ;
  - ch. 49 § 49.3, f. 869 · PDF 883.
- **Constat (vérifié) :**
  - l'AAIF annonce le 17 août 2026 qu'A2A la rejoint comme projet hébergé (aaif.io) ;
  - le même billet range agentgateway, MCP, goose et AGENTS.md parmi les projets de l'AAIF ;
  - au ch. 49, la phrase « la couche agent-outil et agent-agent relève de l'AAIF », attribuée au Vol. I à juin 2026, devient exacte, mais seulement depuis le 17 août.
- **Correction :**
  - ch. 7 : les deux protocoles relèvent désormais de l'AAIF ;
  - ch. 37 : ajouter le second transfert et requalifier agentgateway en projet de l'AAIF ;
  - ch. 49 : dater la phrase au 17 août 2026.
  - Ce changement touche aussi la rangée « révisions protocolaires » du tableau 50.1 (§ 5).

### H-03 — Révision MCP 2026-07-28 encore « annoncée au brouillon »

- **Où :**
  - ch. 19, f. 327 · PDF 341 : « une révision majeure […] est annoncée au brouillon […] les décomptes portant sur ce protocole sont à rejouer » ;
  - ch. 20 § 20.1, f. 343 · PDF 357, et tableau du § 20.4, f. 348 · PDF 362 : « MCP, révision 2025-11-25, page "Authorization" » ;
  - ch. 37, f. 664 · PDF 678 : corrigé à moitié, à la page suivante ;
  - ch. 39, f. 703 · PDF 717 ;
  - ch. 46, tableau 46.3, f. 828 · PDF 842 : « annoncée au brouillon, sa date n'est pas confirmée à la source » ;
  - ch. 47, f. 840 · PDF 854 ;
  - ch. 48, f. 854 · PDF 868.
- **Constat :**
  - *Vérifié.* La version 2026-07-28 est la dernière publication du dépôt de la spécification (GitHub, aucune après) ; le livre lui-même la constate aux ch. 8, 11, 38 et 50.
  - *Vérifié (secondaires).* La révision déprécie l'enregistrement dynamique de client, déplace les tâches dans une extension et retire les sessions.
  - *Supposé.* Les constats du ch. 20 sur l'autorisation MCP, établis sur la révision 2025-11-25, peuvent ne plus valoir ; à rejouer sur la page *Authorization* de la révision 2026-07-28.
  - *Vérifié.* La revalidation du 2 septembre (`PRD/revalidation-2026-09-02.md` § 4) déclarait que « rien » ne touchait le ch. 46. Son tableau 46.3, intitulé « jalons à surveiller », oriente pourtant mal le lecteur.
- **Correction :**
  - remplacer « annoncée au brouillon » par « ratifiée le 28 juillet 2026 (S-001, ☑ changée) » ;
  - rejouer sur le texte ratifié les balayages des ch. 19 et 20 (§ 20.4) ;
  - au tableau 46.3, retirer la rangée ou la passer à FAIT ÉTABLI.

### H-04 — La loi sur les cryptomonnaies stables est adoptée

- **Où :** ch. 36 § 36.2.7, f. 649 · PDF 663.
- **Énoncé :** « Côté monnaie tokenisée, un cadre fédéral a été annoncé dans un contexte budgétaire […] — annonce, non texte adopté ».
- **Constat (vérifié par secondaires : Fasken, Blakes/Mondaq, Lexology, Digital Policy Alert) :**
  - la *Loi sur les cryptomonnaies stables* (Stablecoin Act) est édictée par la section 45 de la partie 5 de C-15, sanctionnée le 26 mars 2026, soit avant le gel ;
  - la Banque du Canada en assure la supervision ;
  - l'entrée en vigueur se fera par décret ; la Banque l'évoque pour la mi-2027 ou la fin de 2027 ;
  - le texte consolidé n'a pas été trouvé sur Justice Laws, d'où le régime « secondaires ».
- **Correction :** « cadre légiféré (Loi sur les cryptomonnaies stables, C-15, sanction royale le 26 mars 2026), non en vigueur, entrée en vigueur par décret ». La réserve R-5 sur le contenu reste applicable tant que le texte n'est pas au socle.

### H-05 — Swift : le retrait des adresses non structurées n'aura pas lieu en novembre 2026

- **Où :** ch. 31 § 31.2.2, f. 551 · PDF 565.
- **Énoncé :** « le retrait des adresses non structurées est attendu en novembre 2026 — une échéance annoncée, à re-vérifier ».
- **Constat (vérifié par secondaires : fintech.garden, 28 août 2026 ; WislaCode ; J.P. Morgan ; Mambu) :**
  - le 27 août 2026, Swift a reporté tous les changements « paiements » de SR2026, prévus le 14 novembre 2026, dont l'obligation d'adresse ;
  - le nouveau calendrier est attendu « d'ici décembre 2026 » ;
  - SR2025 reste en vigueur et accepte les adresses non structurées, hybrides et structurées ;
  - le titre du communiqué Swift (« Swift accepts community request to extend structured address migration… ») figure aux résultats, mais la page swift.com refuse l'accès (403).
- **Correction :** « échéance de novembre 2026 reportée par Swift le 27 août 2026 ; nouveau calendrier annoncé pour décembre 2026 ». Revalider en janvier 2027.

### H-06 — Le rapport final du CSF est publié

- **Où :** ch. 31 § 31.1, f. 547 · PDF 561.
- **Énoncé :** « rapport final attendu en octobre 2026 […] PROGRAMMÉ […] et non advenu au gel de la somme ».
- **Constat (vérifié) :** le CSF a publié le 15 octobre 2026 *Sound Practices for Responsible Adoption of Artificial Intelligence (AI): Final report*, non contraignant, en douze pratiques (fsb.org). La passe du 19 octobre l'avait relevé (constat *a*) sans pouvoir le constater.
- **Correction :** passer l'énoncé au FAIT ÉTABLI, avec titre et date.

### H-07 — Chaînage d'identité inter-domaines : approuvé, en file de l'éditeur des RFC

- **Où :** ch. 17 § 17.2, f. 297 · PDF 311.
- **Énoncé :** « révision −17 du 19 juillet 2026, Internet-Draft actif du groupe de travail OAuth soumis à l'IESG pour publication, expirant le 20 janvier 2027 ».
- **Constat :**
  - *Vérifié.* L'état IESG est « RFC Ed Queue » (Datatracker, dernière mise à jour du 21 août 2026). L'IESG a donc approuvé le document ; l'expiration n'a plus d'objet.
  - *Supposé.* La publication en RFC peut survenir d'ici la fin de 2026 ; le registre de l'éditeur des RFC le dira.
- **Correction :** « approuvé par l'IESG, en file de l'éditeur des RFC » ; inscrire la publication en RFC à la veille du ch. 50.

### H-08 — IETF WIMSE : un document sur les agents d'IA est adopté, et le groupe ne compte plus « sept » documents

- **Où :**
  - ch. 12 § 12.1, f. 216-217 · PDF 230-231 : sept documents, « un seul — […]-practices-05 […] Submitted to IESG », « l'un des sept expirant six semaines après » ;
  - ch. 16 § 16.4, f. 286-288 · PDF 300-302 ;
  - ch. 18, f. 315 · PDF 329 : « ZÉRO TEXTE RATIFIÉ […] deux brouillons de l'IETF sont des soumissions individuelles non adoptées » ;
  - ch. 30 § 30.3, f. 539-541 · PDF 553-555 ;
  - ch. 45, f. 810 · PDF 824 ;
  - ch. 50, tableau 50.1, f. 906 · PDF 920 ;
  - annexe B, S-131, f. 923 · PDF 937.
- **Constat (vérifié, Datatracker) :**
  - le groupe WIMSE compte huit documents ;
  - `draft-ietf-wimse-aims-00`, « AI Identity Management System », est adopté le 15 septembre 2026 (il remplace `draft-klrc-aiagent-auth`). Son résumé propose des bonnes pratiques d'authentification et d'autorisation des interactions d'agents d'IA, sur l'architecture WIMSE et OAuth, sans protocole neuf ;
  - `workload-identity-practices` est passé en −07 (22 septembre 2026), à l'état « AD Evaluation » ;
  - `wimse-wpt` est passé en −02 ;
  - aucun RFC encore.
- **Portée :**
  - le ch. 50 (§ 50.3) pose lui-même que « ce qui change la citabilité d'un document est son adoption par un groupe de travail » ;
  - les faits négatifs datés du 21 juillet restent vrais à leur date, mais la voie « extension d'un texte de l'IETF » du tableau 16.3 (scénario 1) n'est plus sans document adopté.
- **Correction :**
  - re-mesurer le cardinal à huit ;
  - inscrire `aims-00` aux ch. 12, 16 et 18, avec son statut à chaque mention : document de groupe de travail, non RFC, visée non arrêtée ;
  - réexaminer le tri du scénario 1 (PROJETÉ) ;
  - amender S-131 et S-096 au socle d'abord.

---

## 2. Urgence moyenne

### M-01 — Jetons de transaction : révision −11, consensus du groupe de travail

- **Où :**
  - ch. 12, tableau du § 12.5, f. 224 · PDF 238 ;
  - ch. 17, f. 295 et 305 · PDF 309 et 319 ;
  - ch. 37, f. 676 · PDF 690 ;
  - ch. 49, tableau 49.2, f. 891 · PDF 905 ;
  - ch. 50 : tableau 50.1, f. 908 · PDF 922, et § 50.3, f. 912 · PDF 926 ;
  - annexe B, S-075, f. 920 · PDF 934.
- **Énoncé :** « révision −09 du 6 juillet 2026, expirant le 7 janvier 2027, à l'état d'appel de dernière relecture ».
- **Constat (vérifié, Datatracker) :**
  - révision −11 du 30 juillet 2026, expirant le 31 janvier 2027 ;
  - état du groupe de travail : « WG Consensus: Waiting for Write-Up » ; état IESG : « I-D Exists » ;
  - l'échéance du 7 janvier 2027 n'a plus d'objet.
- **Correction :** porter −11, son expiration et son état ; le tableau 50.1 doit cesser de citer le 7 janvier 2027.

### M-02 — Brouillons individuels d'identité d'agent renouvelés

- **Où :**
  - ch. 18, tableau 18.1, f. 313 · PDF 327 : `draft-drake-agent-identity-registry-03`, « expirant le 24 novembre 2026 » ; `draft-sharif-…-01`, « expirant le 27 février 2027 » ;
  - ch. 50, tableau 50.1, f. 908 · PDF 922 : « deux de ses lignes reposent sur des documents expirant les 27 septembre et 24 novembre 2026 ».
- **Constat (vérifié, Datatracker) :**
  - drake est en −04 (25 septembre 2026, expire le 29 mars 2027) ;
  - sharif est en −02 (21 octobre 2026, expire le 24 avril 2027) ;
  - les deux restent des soumissions individuelles non adoptées : le constat qualitatif du ch. 18 tient.
- **Correction :** mettre à jour révisions et expirations. La phrase du tableau 50.1 est périmée depuis le 2 septembre (pour sharif) ; elle confirme le « démenti » que le § 50.3 consigne.

### M-03 — Ch. 36 : le règlement administratif du RTR est encore écrit au futur

- **Où :** ch. 36 § 36.2.7, f. 649 · PDF 663.
- **Énoncé :** « son règlement administratif […] doit entrer en vigueur le 24 août 2026 ».
- **Constat (vérifié) :** il est en vigueur depuis le 24 août 2026 (DORS/2026-133, constaté par la revalidation du 2 septembre et repris au ch. 33). Le rapport de revalidation déclare pourtant le ch. 36 non touché ; même remarque qu'en H-03 pour le ch. 46.
- **Correction :** « en vigueur depuis le 24 août 2026 (DORS/2026-133) ». Ajouter le ch. 36 au domaine de la prochaine revalidation.

### M-04 — Rail temps réel : l'échéance du T4 2026 tombe dans l'horizon

- **Où :**
  - ch. 33, f. 579-587 · PDF 593-601 ;
  - ch. 36, f. 643 et 649-652 · PDF 657 et 663-666 ;
  - ch. 34, tableau 34.3, f. 616 · PDF 630 ;
  - ch. 50, tableau 50.1, f. 904 · PDF 918 ;
  - annexe B, S-027, f. 918 · PDF 932.
- **Énoncé :** « À la mi-juillet 2026, le rail de paiement en temps réel n'est pas en production » ; « cible T4 2026 » ; à S-027, « Cible T4 2026 non réalisée ».
- **Constat :**
  - *Vérifié.* La page de Paiements Canada porte toujours « launching in Q4 of 2026 ».
  - *Vérifié (secondaires).* Le 13 octobre 2026, le rail était « on track » pour un lancement par vagues au T4 2026, tous les participants ayant accès en 2027.
  - *Supposé.* D'ici le 31 décembre, soit une première vague est lancée (les énoncés « pas en production » et la réserve F-29 deviennent non actuels), soit la cible glisse et une cinquième cible apparaît. Seul le constat au 1ᵉʳ janvier 2027 tranchera.
  - À S-027, « non réalisée » est ambigu avant la fin du trimestre.
- **Correction :** aucune avant l'événement. Revalider ce point en premier en janvier 2027 ; à S-027, écrire « cible T4 2026, non réalisée au 2 septembre 2026 ».

### M-05 — Directive (UE) 2024/2853 : un rectificatif a déplacé la date d'application

- **Où :**
  - ch. 24, f. 451 · PDF 465 ;
  - ch. 30, f. 527 · PDF 541 ;
  - ch. 49 § 49.10, f. 881 · PDF 895 : « transposition […] due au 9 décembre 2026 — date à re-vérifier — et qui ne s'applique qu'aux produits mis sur le marché après ce terme ».
- **Constat (vérifié) :**
  - le rectificatif JO L 2026/90364 du 7 mai 2026 modifie l'art. 2, § 1 : la directive s'applique aux produits mis sur le marché « après le 8 décembre 2026 » (texte lu dans la version espagnole) ;
  - l'échéance de transposition du 9 décembre 2026 n'est pas touchée ;
  - les deux dates tombent dans l'horizon.
- **Correction :** distinguer la transposition (9 décembre) de l'application (après le 8 décembre, par rectificatif). Passer au passé après le 9 décembre.

### M-06 — Portefeuille d'identité numérique européen : échéance du 24 décembre 2026

- **Où :** ch. 3 § 3.3, f. 57 · PDF 71.
- **Énoncé :** « généralisation attendue à compter de 2026 — échéance à re-vérifier ».
- **Constat (vérifié par secondaires) :**
  - le règlement 2024/1183 (art. 5 bis) oblige chaque État membre à fournir au moins un portefeuille dans les 24 mois de l'entrée en vigueur des actes d'exécution (24 décembre 2024), donc d'ici le 24 décembre 2026 ;
  - la Commission admet que tous les États ne seront pas prêts.
- **Correction :** remplacer « généralisation attendue » par l'obligation datée, sans conclure à la généralisation effective. Constater en janvier 2027.

### M-07 — « LangGraph Platform » s'appelle « LangSmith Deployment » depuis octobre 2025

- **Où :**
  - ch. 23 : thèse, f. 411 · PDF 425 ; titre du § 23.2, f. 415-416 · PDF 429-430 ;
  - annexe B, S-030, f. 918 · PDF 932.
- **Constat (vérifié par secondaires, renvoyant au journal des modifications de LangChain, non ouvert) :** le produit a été renommé en octobre 2025, avant le gel ; la disponibilité générale du 14 mai 2025 reste exacte.
- **Correction :** « LangGraph Platform (renommée LangSmith Deployment en octobre 2025) » à la première mention.

### M-08 — OSWorld : le seuil humain serait déjà franchi

- **Où :** ch. 6 § 6.3, f. 110 · PDF 124.
- **Énoncé :** le taux des agents a « progressé vers le plafond de performance humaine, approché entre fin 2025 et début 2026 sans encore le rejoindre ».
- **Constat (supposé) :** des sources secondaires discordantes donnent 72,6 % contre 72,36 % pour l'humain (Simular, décembre 2025), puis 75 à 85 % en 2026. Le classement officiel n'a pas été lu : sa page redirige vers `osworld-v1.xlang.ai`. Le classement OSWorld-Verified tranchera.
- **Correction :** si le classement confirme, « dépassé dès décembre 2025 sur OSWorld-Verified (seuil humain ≈ 72,4 %) ».

### M-09 — Annexe B : abrégés en retard sur le socle et sur les chapitres

- **Où :** annexe B, f. 917-925 · PDF 931-939.
- **Constats (vérifiés) :**
  - **S-001** porte « Spécification rév. 2025-11-25, revalidée le 16 juill. 2026 », alors que l'entrée est ☑ changée au 28 juillet 2026 ;
  - **S-020** porte « règlement à venir », alors qu'il est prépublié depuis le 27 juin 2026 ;
  - **S-027** : voir M-04 ; **S-030** : voir M-07 ; **S-075** : voir M-01 ;
  - **S-102** porte « ATLAS 2026.06 », alors que la version courante est v2026.09 (B-01) ;
  - **S-131** porte « sept Internet-Drafts » : voir H-08.
- **Correction :** régénérer les abrégés depuis `PRD/socle-consolide.md` après amendement du socle.

### M-10 — Ch. 50 : le cardinal « onze » survit en trois endroits

- **Où :**
  - f. 903 · PDF 917 : « le seul des onze dont la date reste inconnue » ;
  - § 50.3, f. 912 · PDF 926 : « les onze événements du § 50.2 », et l'énumération « (3 septembre 2026, 7 janvier 2027) » ;
  - légende de la figure 50.4, f. 915 · PDF 929 : « les onze événements ».
- **Constat (vérifié dans le PDF) :**
  - le tableau 50.1 compte quatorze rangées depuis le 2 septembre ;
  - l'échéance du 3 septembre a été repoussée en février 2027, et celle du 7 janvier 2027 est caduque (M-01).
- **Correction :** quatorze ; énumération à jour. *Défaut de cohérence interne, mais il porte sur le registre de péremption lui-même.*

### M-11 — FIS et Anthropic : disponibilité générale annoncée pour le second semestre 2026

- **Où :**
  - ch. 31, f. 563 · PDF 577 ;
  - ch. 34, f. 592 et 612 · PDF 606 et 626.
- **Constat (vérifié par secondaires) :** au 22 octobre 2026, aucune annonce de disponibilité générale ; les communiqués FIS maintiennent « GA planned 2H 2026 ». L'échéance tombe dans l'horizon.
- **Correction :** aucune avant l'événement ; constater en janvier 2027.

---

## 3. Urgence basse

| # | Où (f. · PDF) | Énoncé | Constat et régime | Correction proposée |
|---|---|---|---|---|
| B-01 | ch. 19, f. 325 · PDF 339 ; ch. 20 § 20.10, f. 360 · PDF 374 | « La collection courante est la 2026.06 » | Vérifié : ATLAS v2026.07, .08, puis v2026.09 (15 sept. 2026) sur GitHub | « 2026.06 au relevé du 21 juillet 2026 » ; courante : v2026.09 |
| B-02 | ch. 13, f. 234-235 · PDF 248-249 ; ch. 16, f. 286 · PDF 300 ; ch. 17, f. 305 · PDF 319 ; ch. 50, f. 906 · PDF 920 | VC 2.1 « brouillon de travail du 11 mai 2026 » | Vérifié : toujours *Working Draft* ; version datée du 22 oct. 2026 sur /TR. Le statut tient, la date est supplantée | Dater le relevé ; garder SPÉCULATIF |
| B-03 | ch. 18, f. 313 · PDF 327 ; ch. 20, f. 361 · PDF 375 ; ch. 37, f. 674 · PDF 688 | Document de concept du NCCoE au stade de projet public initial | Vérifié : synthèse des commentaires publiée (614 réponses, page non datée) ; le NCCoE « entend publier » un projet de description de projet, sans date | Ajouter la synthèse ; tri PROJETÉ inchangé |
| B-04 | ch. 37, f. 662-663 et 669 · PDF 676-677 et 683 | agentgateway v1.4.0-alpha.2 / v1.3.1 | Vérifié : v1.6.0 (2 oct. 2026) est la dernière version stable ; v1.7.0-alpha.1 du 21 oct. | Dater au 21 juillet ; voir aussi H-02 pour la gouvernance |
| B-05 | ch. 34, f. 609 et 612 · PDF 623 et 626 | « système d'exploitation d'agents » bancaire, disponibilité générale « annoncée pour août 2026 » | Supposé : échéance passée, non vérifiée (source [C], Klover.ai) | Constater ou retirer la date |
| B-06 | ch. 47, f. 836-837 · PDF 850-851 ; ch. 40, f. 730 · PDF 744 | SPDX 3.0 « courante » ; FOCUS 1.4, « version suivante » pour les jetons | Vérifié (secondaires) : SPDX 3.1 en RC1 (janv. 2026), aucune version stable trouvée ; FOCUS 1.5 visée vers la fin 2026 | Veille ; corriger si publication d'ici le 31 déc. |
| B-07 | ch. 9 § 9.4, f. 163 · PDF 177 | Assistants API, « fixé le retrait au 26 août 2026 » | Vérifié (rapport du 2 sept.) : retrait survenu le 26 août 2026 ; le ch. 9 ne le dit pas | « retirée le 26 août 2026 » |
| B-08 | ch. 1, f. 10 · PDF 24 | La politique de dépréciation « vaut pour la révision candidate […] non pour le texte ratifié » | Vérifié dans le PDF : la revalidation du ch. 8 (30 juillet) confirme la fenêtre de douze mois dans le texte ratifié | Clore par renvoi au ch. 8 § 8.3 |
| B-09 | ch. 16, f. 287 · PDF 301 ; ch. 50, f. 906 · PDF 920 ; S-091 | AP2 : « trois mois après, le transfert n'est pas matérialisé » | Vérifié : toujours v0.2.0, dépôt `google-agentic-commerce/AP2` sans mention de la FIDO Alliance | « près de six mois après (22 oct. 2026) » ; le constat tient |
| B-10 | ch. 26, f. 477 · PDF 491 ; S-022 | C-36 : « douze jours sans progression » | Vérifié : LEGISinfo, « At second reading », aucune activité depuis le 15 juin 2026 | « aucune activité au 22 oct. 2026 » si l'on re-date |
| B-11 | ch. 28 § 28.3, f. 504-505 · PDF 518-519 | ACVM 11-348 : « ce silence sur quinze mois » | Supposé : la recherche n'a trouvé aucune suite (absence de documentation, degré 3) ; la page de la CVMO ou de l'AMF tranchera | Garder la durée datée au gel |
| B-12 | f. 175 · PDF 189 ; f. 475 · PDF 489 ; f. 668 · PDF 682 ; f. 842 · PDF 856 ; f. 885 · PDF 899 | « à ce jour » | Ambigu hors de la date de gel | « au 27 juillet 2026 » |
| B-13 | ch. 26, f. 479 · PDF 493 ; ch. 32, f. 573-574 · PDF 587-588 ; ch. 33, f. 585 · PDF 599 ; ch. 46, f. 825 · PDF 839 | Comptes à rebours : « neuf mois et quatre jours », « 278 jours », « vingt-huit jours », etc. | Exacts à la date du gel et dits tels ; au 31 décembre 2026, il reste 121 jours avant le 1ᵉʳ mai 2027 | Aucune, sauf re-datation d'ensemble |
| B-14 | ch. 30, f. 532 · PDF 546 | MiCA : « période de transition s'étendant jusqu'à la fin juin 2026 » | Échue (vérifié par le texte du livre lui-même) | Passer au passé |
| B-15 | ch. 15, f. 264 · PDF 278 | Entra Agent ID : licence « coming soon » (PROJETÉ) ; capacités en préversion au 21 juillet | Supposé : non re-vérifié ; la documentation Microsoft tranchera | Veille |
| B-16 | ch. 30, f. 531 · PDF 545 ; ch. 34, f. 597 · PDF 611 | Guidance interagences américaine (17 avril 2026), RFI « annoncée » | Vérifié (secondaires : OCC Bulletin 2026-13, SR 26-2) : la RFI n'est pas confirmée publiée | Nommer SR 26-2 / OCC 2026-13 ; veille de la RFI |
| B-17 | ch. 3, f. 53 · PDF 67 | OAuth 2.1 « encore à l'état de projet » | Vérifié : `draft-ietf-oauth-v2-1-16` (3 sept. 2026), « I-D Exists » | Aucune |
| B-18 | ch. 25, f. 471 · PDF 485 | Projection BSIF/ACFC d'environ 70 % d'adoption « d'ici 2026 » | Supposé : l'horizon de la projection est atteint au 31 déc. ; aucune mesure de réalisation cherchée | Veille d'une nouvelle enquête |
| B-19 | ch. 21, f. 367 · PDF 381 | Décret 14412 et M-26-15 | Vérifié : décret signé le 22 juin 2026 (FR 91 38483), M-26-15 du 24 juin ; leurs livrables à 90, 120 et 270 jours tombent de septembre 2026 à mars 2027 | Aucune ; veille des livrables |
| B-20 | ch. 49 § 49.2, f. 867 · PDF 881 | « programmes de priorité sans engagement temporel » | Vérifié (secondaires) : feuille de route MCP du 22 août 2026, cinq priorités dont l'identité d'agent, sans date | Peut s'illustrer par cette feuille de route |
| B-21 | ch. 2, f. 43 · PDF 57 | Révision RDF/SPARQL « en cours au gel de la source (juin 2026) » | Vérifié : RDF 1.2 *Concepts* en CR Snapshot du 7 avril 2026 | Préciser le stade CR |
| B-22 | `draft-wzdk-scim-agent-resource-00` : ch. 12, f. 225 · PDF 239 ; `draft-mp-agntcy-ads-02` : ch. 15, f. 272 · PDF 286 | Expirations du 7 déc. 2026 et du 7 janv. 2027 | Vérifié : inchangés au 22 oct. 2026 | Veille (adoption ou abandon, § 50.3) |

---

## 4. Échéances du 22 octobre au 31 décembre 2026, à constater

| Date | Objet | Constats |
|---|---|---|
| T4 2026 | Lancement de la première vague du RTR | M-04 |
| 2ᵉ semestre 2026 | Disponibilité générale de l'agent FIS–Anthropic | M-11 |
| novembre 2026 → reporté | Swift SR2026 (adresses) ; nouveau calendrier attendu en décembre | H-05 |
| 2 déc. 2026 | AI Act : fin d'un délai de grâce sur le marquage (*supposé*, à vérifier sur l'art. 50 modifié) | H-01 |
| 7 déc. 2026 | Expiration de `draft-wzdk-scim-agent-resource-00` si non renouvelé | B-22 |
| 8-9 déc. 2026 | Directive (UE) 2024/2853 : application, puis transposition | M-05 |
| 24 déc. 2026 | Portefeuilles d'identité numérique européens | M-06 |
| d'ici la fin 2026 (*supposé*) | RFC du chaînage d'identité ; envoi à l'IESG des jetons de transaction ; FOCUS 1.5 ; SPDX 3.1 | H-07, M-01, B-06 |
| sans date | Règlement final du cadre bancaire (« fin 2026 ou début 2027 » selon des secondaires) ; désignation de l'organisme ; 2ᵉ lecture de C-36 ; RFI américaine | § 5 |

---

## 5. Registre de péremption (tableau 50.1) : état de chaque rangée au 22 octobre 2026

| Rangée | État au 22 octobre 2026 | Régime |
|---|---|---|
| Désignation de l'organisme de normalisation (cadre bancaire) | Aucune désignation ni publication finale en partie II trouvée ; des secondaires visent un règlement final pour « fin 2026 ou début 2027 » | Supposé : recherche négative, index de la Gazette partie II non balayé |
| Lancement du RTR | Toujours visé au T4 2026, par vagues | Vérifié (M-04) |
| Révisions protocolaires | MCP : aucune révision après 2026-07-28. A2A : version inchangée (v1.0.1), mais **gouvernance déplacée vers l'AAIF le 17 août** | Vérifié (H-02) |
| Transfert de gouvernance d'AP2 | Toujours non matérialisé : v0.2.0, dépôt d'origine | Vérifié (B-09) |
| Normalisation du passeport d'agent | **Un document de groupe de travail de l'IETF est adopté** (`wimse-aims-00`) ; aucun RFC | Vérifié (H-08) |
| Conventions sémantiques OpenTelemetry GenAI | Toujours aucune version étiquetée au dépôt dédié, statut *Development* | Vérifié (secondaires) |
| Premier incident public d'usurpation du justificatif d'un agent | Non instruit par cet audit | Hors périmètre |
| Jalons post-quantiques | NIST IR 8547 et SP 800-131A r3 toujours en projet public initial ; décret 14412 confirmé | Vérifié |
| E-23 et AMF au 1ᵉʳ mai 2027 | Inchangé | Vérifié |
| Expiration des documents de groupe de travail | Toutes les échéances citées sont repoussées : jetons de transaction au 31 janv. 2027, drake au 29 mars 2027, sharif au 24 avr. 2027 | Vérifié (M-01, M-02) |
| Textes réglementaires finaux (été 2026) | Règlement administratif du RTR en vigueur ; règlement bancaire toujours prépublié | Vérifié, puis supposé |
| Retrait de l'Assistants API | Survenu le 26 août 2026 | Vérifié (rapport du 2 sept.) |
| C-36 | Aucune activité depuis la première lecture | Vérifié |
| Suites de l'avis ACVM 11-348 | Aucune suite trouvée | Supposé (B-11) |

**Rangées candidates à l'inscription**, au titre de la transposition du § 50.3 (« augmentés de ce que le calendrier réglementaire aura fait apparaître ») :

- le report de l'AI Act, à passer en FAIT ÉTABLI ;
- la directive 2024/2853 (8-9 déc. 2026) ;
- les portefeuilles européens (24 déc. 2026) ;
- le calendrier Swift reporté ;
- l'entrée en vigueur de la loi sur les cryptomonnaies stables (décret, 2027) ;
- l'adoption de `wimse-aims`.

**Lacunes du Livre V (tableaux 49.1 et 49.2, f. 887-891 · PDF 901-905).**

- Aucune lacune n'est comblée par un fait trouvé ici.
- Deux rangées voient leur état décrit changer :
  - « Jetons de transaction : révision du 6 juillet 2026, expirant le 7 janvier 2027 » (tableau 49.2) : voir M-01 ;
  - « Désignation de l'organisme » : reste ouverte, sans acte trouvé.

---

## 6. Énoncés relatifs au gel

- **Datés et sains.** La plupart des faits négatifs sont datés (« au 16 juillet 2026 », « au 21 juillet 2026 », « au 28 juillet 2026 ») et restent vrais à leur date : la convention du § 50.4 fonctionne.
- **À corriger.** Les seuls défauts sont les cinq « à ce jour » sans date (B-12) et les énoncés au futur dont l'événement est survenu (H-01, H-03, H-06, M-03, B-07, B-14).

---

## 7. Faits vérifiés inchangés au 22 octobre 2026

Aucune correction n'est requise pour les faits suivants.

- **Protocoles et normes :**
  - MCP 2026-07-28 reste la dernière révision ;
  - A2A v1.0.1 (28 mai 2026) reste la dernière version ;
  - AP2 reste en v0.2.0 ;
  - SLSA v1.2 reste à jour ;
  - aucune CycloneDX 1.8 n'a été trouvée (*supposé*).
- **Brouillons et documents de travail :**
  - OAuth 2.1 reste un brouillon ;
  - DID 1.1 reste en CR Snapshot du 5 mars 2026 ;
  - l'en-tête Idempotency-Key reste expiré (−07) ;
  - `draft-mp-agntcy-ads-02` est inchangé.
- **Post-quantique :** NIST IR 8547 et SP 800-131A r3 restent en projet public initial.
- **Réglementation canadienne :**
  - E-23 et la ligne directrice de l'AMF entrent en vigueur le 1ᵉʳ mai 2027 ;
  - C-36 est toujours en deuxième lecture, sans activité ;
  - DORS/2026-133 est en vigueur ;
  - la cible du RTR reste le T4 2026.
- **États-Unis :** la reconnaissance de FDX par le CFPB court jusqu'au 8 janvier 2030 ; la règle 1033 est suspendue par injonction.
- **Produits :**
  - l'édition de contexte d'Anthropic reste en bêta (`context-management-2025-06-27`) ;
  - l'intégration A2A de Confluent reste en préversion ouverte ;
  - les conventions OpenTelemetry GenAI n'ont toujours aucune version.
- **Ligne directrice de l'AMF.** La date de publication reste divergente selon les sources : 7 avril 2026 (Blakes, BLG), « décision du 30 mars » (Norton Rose Fulbright), titre du PDF indexé « Mars 2026 ». Le site de l'AMF refuse toujours l'accès (403). La position « avril 2026, trois états » du ch. 27 reste la plus prudente.

---

## 8. Relevés hors périmètre (cohérence, non actualité)

- **Ch. 50 § 50.4, f. 914 · PDF 928 :**
  - une note s'est insérée dans la phrase : « … n'y en a aucune Depuis le 2 septembre 2026, six des neuf sont retirées […] dans les volumes sources., faute d'être écrit » ;
  - « la remontée est au § 50.515 » colle l'appel de note 15 au numéro de section.
- **Ch. 8, f. 138 · PDF 152 :** révision candidate MCP « gelée le 21 mai 2026 », alors que l'étiquette GitHub `2026-07-28-RC` est datée du 29 mai. Ce n'est pas forcément contradictoire (gel puis étiquetage), mais c'est à vérifier.
- **Atlas et PDF.** Certains repères de `window.ATLAS` ne concordent pas avec le PDF, par exemple agentgateway « v1.4.0 publié, non signalé pré-version » contre v1.4.0-alpha.2 dans le PDF (f. 662 · PDF 676). Hors objet ici, mais l'Atlas dérive du PDF et devra suivre toute reprise.

---

## 9. Limites de cet audit

- **Méthode.** Audit mené seul, sans vote adversarial. Les verdicts « vérifiés » s'appuient sur une consultation unique datée du 22 octobre 2026 ; ce sont des relevés, non des confirmations au sens du socle.
- **Sources inaccessibles.** swift.com, lautorite.qc.ca et eur-lex.europa.eu (texte de l'acte) ont refusé l'accès ou renvoyé une page vide. Les constats correspondants (H-05, H-01) s'appuient sur EEA-Lex et sur des secondaires concordantes.
- **Non vérifié :**
  - le classement OSWorld officiel (M-08) ;
  - Microsoft Entra Agent ID (B-15) ;
  - le « système d'exploitation d'agents » (B-05) ;
  - les études de cas bancaires du ch. 35 (statuts « bêta » d'avril-mai 2026) ;
  - le premier incident public d'usurpation.
- **Hors périmètre :** les 159 entrées du socle n'ont pas été rejouées une à une. Seuls les objets datés ou prospectifs du PDF ont été confrontés.
- **Volume ignoré :** les pages d'appareil (bibliographie, Annexe I, f. 926 et suivants) n'ont pas été auditées pour l'actualité.

---

## Sources consultées le 22 octobre 2026

- MCP, versions : https://github.com/modelcontextprotocol/modelcontextprotocol/releases
- MCP, feuille de route (secondaire) : https://www.cdata.com/blog/official-mcp-roadmap-explained
- A2A, versions : https://github.com/a2aproject/A2A/releases
- A2A rejoint l'AAIF (17 août 2026) : https://aaif.io/blog/a2a-joins-aaif
- AP2, versions : https://github.com/google-agentic-commerce/AP2/releases
- FIDO Alliance, 28 avril 2026 : https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/
- agentgateway, versions : https://github.com/agentgateway/agentgateway/releases
- MITRE ATLAS, versions : https://github.com/mitre-atlas/atlas-data/releases
- IETF Datatracker :
  - https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
  - https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/
  - https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/
  - https://datatracker.ietf.org/wg/wimse/documents/
  - https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/
  - https://datatracker.ietf.org/doc/draft-drake-agent-identity-registry/
  - https://datatracker.ietf.org/doc/draft-sharif-openid-agent-identity/
  - https://datatracker.ietf.org/doc/draft-wzdk-scim-agent-resource/
  - https://datatracker.ietf.org/doc/draft-mp-agntcy-ads/
  - https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- W3C :
  - https://www.w3.org/TR/did-1.1/
  - https://www.w3.org/TR/vc-data-model-2.1/
  - https://www.w3.org/TR/rdf12-concepts/
- NIST :
  - https://csrc.nist.gov/pubs/ir/8547/ipd
  - https://csrc.nist.gov/pubs/sp/800/131/a/r3/ipd
  - https://pages.nist.gov/nccoe-ai-identity/summary-of-comments.html
- Décret 14412 et M-26-15 :
  - https://www.federalregister.gov/documents/2026/06/25/2026-12909/securing-the-nation-against-advanced-cryptographic-attacks
  - https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf
- Anthropic, édition de contexte : https://platform.claude.com/docs/en/build-with-claude/context-editing
- AI Act, omnibus :
  - https://www.efta.int/eea-lex/32026r1744
  - https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force
- Directive 2024/2853, rectificatif (JO L 2026/90364) : https://www.boe.es/doue/2026/90364/L00001-00001.pdf
- Portefeuilles européens (secondaire) : https://www.garrigues.com/en_GB/garrigues-digital/european-digital-identity-wallet-now-has-timetable-tasks-be-completed-december
- CSF, rapport final du 15 octobre 2026 : https://www.fsb.org/2026/10/fsb-finalises-sound-practices-for-the-responsible-adoption-of-artificial-intelligence-ai/
- Swift, report (secondaires) :
  - https://fintech.garden/news/2026-08-28-swift-grants-reprieve-on-iso-20022-structured-address-mandate-after-banks-flag-r/
  - https://wislacode.com/blog/iso-20022-structured-addresses-what-becomes-mandatory-in-november-2026/
  - https://www.jpmorgan.com/insights/payments/fx-cross-border/iso-20022-migration
- Paiements Canada, RTR : https://www.payments.ca/systems-services/payment-systems/real-time-rail-payment-system
- BSIF, E-23 : https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027
- AMF, ligne directrice IA (secondaires) :
  - https://www.blakes.com/insights/quebec-s-amf-issues-guideline-on-the-use-of-ai-for-financial-institutions/
  - https://www.nortonrosefulbright.com/en/knowledge/publications/27e0daab/amf-s-ai-guideline-is-now-official-what-financial-institutions-need-to-know
- C-36, LEGISinfo : https://www.parl.ca/legisinfo/en/bill/45-1/c-36
- Cadre bancaire, prépublication : https://gazette.gc.ca/rp-pr/p1/2026/2026-06-27/html/reg3-eng.html
- Loi sur les cryptomonnaies stables (secondaires) :
  - https://www.fasken.com/en/knowledge/2026/03/budget-2025-the-bank-of-canadas-mandate-expands-to-stablecoin-and-open-banking-supervision
  - https://www.lexology.com/library/detail.aspx?g=a5ff681d-f34a-46d2-b36b-513361be5a63
- Guidance interagences américaine : https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html
- LangSmith Deployment (secondaire, renvoyant au journal de LangChain) : https://www.langchain.com/langsmith/deployment
- FIS et Anthropic : https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-brings-agentic-ai-to-banking-with-anthropic-starting-with-financial-crimes
- Confluent, mise à jour du T1 2026 : https://www.confluent.io/blog/2026-q1-confluent-intelligence-update/
- OpenTelemetry GenAI (secondaire) : https://john-hodge.com/blog/opentelemetry-genai-semantic-conventions/
