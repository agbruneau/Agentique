# Chapitre 45 — Réseaux B2B fédérés et négociation entre agents

*Question directrice : comment des agents de plusieurs entreprises négocient-ils et partagent-ils des données sans fuite de secrets, sans collusion et sans fraude au règlement ?*

> **Version 2 — 12 novembre 2026.** Faits arrêtés au 11 novembre 2026. État de référence : ODRL Information Model 2.2 (recommandation du W3C du 15 février 2018), Dataspace Protocol 2025-1, vLEI Ecosystem Governance Framework 4.0. Les sources [1] à [14] sont des pages primaires lues pour ce chapitre; les deux documents de [15] ont été repérés sans être lus. Les constructions demandées sans source identifiée sont présentées comme des cibles de conception à valider. Chapitre audité et révisé le 12 novembre 2026.

Entre deux entreprises, un agent ne rencontre plus un outil qu'il maîtrise, mais un autre agent, qui sert un intérêt contraire. Chacun détient ce que l'autre voudrait connaître : un prix plancher, une marge, un carnet de commandes. Chacun lit des messages que l'autre a rédigés. Et l'échange se termine par un paiement.

La thèse : aucune des trois protections demandées ne peut reposer sur le modèle de langage. Le modèle formule et propose; des composants déterministes, attestés ou contractuels décident. Les couches basses de cet assemblage sont normalisées; la négociation et la collusion relèvent encore de la recherche.

---

## 45.1 Du couple client-fournisseur au réseau fédéré

L'intégration interentreprises classique est bilatérale. Chaque paire de partenaires convient d'un canal, d'un format, d'une identité et d'un contrat, et rien de ce qui est convenu avec l'un ne sert avec le suivant.

Un réseau fédéré déplace l'accord du couple vers le réseau. Les participants adoptent un protocole, un vocabulaire de politiques et un mécanisme d'identité communs; chacun garde ses systèmes et ses données. Le Dataspace Protocol nomme cette fédération un *dataspace* : des entités y publient des données, négocient des accords et y accèdent sous contrôle d'usage [3].

L'arrivée d'agents y introduit des risques qui se traitent chacun à une couche différente. Plus on s'approche du comportement de l'agent, moins il existe de norme.

| Risque | Mécanisme | Maturité |
|---|---|---|
| Usage non convenu des données | ODRL, DSP, connecteur EDC | Recommandation du W3C; protocole stable |
| Contrepartie sans existence légale vérifiable | vLEI | Cadre publié; extension aux agents proposée |
| Fuite d'un secret de négociation | Séparation de la négociation et de l'évaluation | Cible de conception, sans source |
| Fuite lors d'un calcul conjoint | Environnement d'exécution de confiance | Produits offerts |
| Collusion | Revue des consignes, journalisation | Recherche; aucune défense éprouvée |
| Paiement indu | Rapprochement à trois voies | Pratique établie; raccord aux agents non spécifié |

---

## 45.2 Connecteurs et contrats d'usage : Eclipse Dataspace Components et ODRL

### ODRL : exprimer une politique

ODRL Information Model 2.2 est une recommandation du W3C datée du 15 février 2018 [1]. Une politique (`Policy`) regroupe des règles. Une règle est une permission, une interdiction ou un devoir, et porte sur une action exercée sur un actif par une partie. Une contrainte précise une action ou conditionne une règle.

Deux sous-classes structurent la négociation. Une offre (`Offer`) exige un cédant (`assigner`) et n'accorde rien. Un accord (`Agreement`) exige un cédant et un cessionnaire (`assignee`), et accorde les règles entre les parties [1].

Deux propriétés pèsent sur un usage par des agents. La propriété `conflict` vaut `perm`, `prohibit` ou `invalid`, cette dernière par défaut : une politique où une permission et une interdiction se contredisent est alors nulle en entier [1]. Une politique rédigée ou fusionnée par un modèle doit donc passer une validation déterministe avant d'être offerte. Ensuite, ODRL exprime et n'applique rien : la recommandation définit un évaluateur de règles, sans prescrire de mécanisme d'application [1].

### DSP : négocier un accord

Le Dataspace Protocol 2025-1, déclaré stable, est publié sous licence Apache 2.0 et gouverné par l'Eclipse Dataspace Working Group, après l'IDSA [3].

Sa négociation de contrat est une machine à états [4]. Sept états sont définis : `REQUESTED`, `OFFERED`, `ACCEPTED`, `AGREED`, `VERIFIED`, `FINALIZED` et `TERMINATED`, le seul que la source lue qualifie de terminal. Le consommateur l'ouvre par une demande, ou le fournisseur par une offre. Chaque partie peut y mettre fin à tout moment. Avant la finalisation, le consommateur envoie un message de vérification de l'accord. Un accord désigne exactement un jeu de données, avec un horodatage, un cédant et un cessionnaire.

### EDC : mettre en œuvre

Eclipse Dataspace Components fournit le connecteur. Son plan de contrôle assemble les catalogues, crée les accords, gère les transferts et surveille le respect des politiques; les plans de contrôle des deux parties se parlent en DSP, et le transfert revient à un plan de données distinct [2]. Quatre traits comptent ici [2].

- **L'actif décrit, il ne contient pas.** La documentation déconseille de placer des secrets dans ses métadonnées.
- **Deux politiques par définition de contrat.** Une politique d'accès, cachée au consommateur, décide de ce qu'il voit; une politique de contrat figure dans l'offre. Le catalogue est produit à l'exécution, selon les justificatifs présentés.
- **La négociation est asynchrone.** Un fournisseur peut la retenir pour approbation manuelle : un point d'insertion pour l'humain dans la boucle (chapitre 22).
- **Un accord se retire.** Le retrait bloque les nouveaux transferts et fait terminer ceux qui sont en cours.

### Ce que cela donne à un agent, et ce qui manque

La négociation porte sur des politiques structurées et des transitions d'état, non sur du texte libre. Un agent ne « convainc » pas un connecteur; le modèle intervient en amont, dans le choix d'une offre et la formulation d'une demande. Le résultat expérimental du chapitre 37 va dans ce sens. L'API de gestion du connecteur ne doit jamais être exposée à un réseau non fiable [2] : un agent y accède par un outil étroit, derrière une passerelle (chapitre 24).

Trois limites restent. Une fois les données transférées, retirer un accord n'efface pas une copie : le respect de l'accord dépend du consommateur et du contrat. Les pages lues ne décrivent aucune négociation de prix; la sémantique commerciale reste à définir (chapitre 10). Enfin, le protocole désigne les parties par des identifiants propres à l'espace [4], sans dire qui elles sont.

---

## 45.3 Identité légale des organisations et des rôles

Le chapitre 29 conclut qu'entre organisations, les mécanismes d'identité transportent une assertion et que la confiance initiale reste contractuelle. Le vLEI (verifiable Legal Entity Identifier) vise ce maillon : rattacher une signature à une personne morale enregistrée.

### Ce que le cadre définit

La GLEIF tient le vLEI Ecosystem Governance Framework, dont la page lue indique la version 4.0 et un document principal daté du 25 mars 2026 [5]. La GLEIF détient un identifiant racine et qualifie des émetteurs, les Qualified vLEI Issuers (QVI), sur une infrastructure KERI. Le cadre décrit cinq justificatifs, dont trois comptent ici.

| Justificatif | Émetteur | Titulaire |
|---|---|---|
| Legal Entity vLEI Credential | QVI | Personne morale |
| Official Organizational Role (OOR) | QVI | Représentant officiel de la personne morale |
| Engagement Context Role (ECR) | Personne morale, ou QVI pour elle | Personne agissant dans un rôle autre qu'officiel |

### Le rôle OOR ne désigne pas un agent

Le justificatif OOR atteste qu'une personne occupe une fonction officielle dans une personne morale [5]. Rien, dans la page lue, ne prévoit son émission à un agent logiciel.

La GLEIF traite le sujet comme un chantier. Dans un billet daté du 1er septembre 2026, son chef de la direction soutient que le droit attribue déjà la responsabilité des actes d'un agent, et que ce qui manque est la preuve [6]. Il propose que chaque agent porte une preuve, lisible par machine, de l'identité légale de l'organisation qu'il sert, de l'autorité déléguée et de ses limites, par une chaîne cryptographique qui remonte à une personne vérifiée. Il préfère une autorité partitionnée (quel agent fait quoi, sous quel mandat) à une identité propre à chaque agent. Le billet décrit une orientation, sans émission en production à des agents.

### Lecture pour l'entreprise

La répartition suivante est une déduction, non un profil publié. Le justificatif d'entité établit qui est la contrepartie. Le justificatif OOR établit quel dirigeant peut l'engager. L'agent porte une délégation distincte, bornée et révocable, qui renvoie aux deux premiers; le justificatif ECR, que la personne morale émet et révoque elle-même, en est le support le plus proche. Aucune page lue n'en fixe le format; un brouillon de l'IETF et le document de réflexion de la GLEIF cité par le billet ont été repérés sans être lus [15]. Cette chaîne recoupe le Delegated Agent Participant ID que propose l'IDSA, vérifié par le connecteur avant toute transaction (chapitre 37). L'acceptation du vLEI par un espace de données donné n'a pas été vérifiée.

---

## 45.4 Négocier sans se dévoiler : séparer la négociation de l'évaluation

Un agent négociateur réunit par construction les trois conditions de la trifecta létale (chapitre 31) : une donnée privée, le prix de réserve; un contenu non fiable, les messages de la contrepartie; un canal sortant, ses réponses. Une injection dans un message adverse peut lui faire écrire ce qu'il sait.

### Une cible de conception, non un patron établi

La scission « Diplomate / Évaluateur interne » n'a été retrouvée sous ce nom dans aucune source : c'est une cible de conception, adossée à un principe publié. CaMeL sépare le flux de contrôle, tiré de la requête de confiance, du flux de données, de sorte qu'une donnée non fiable ne puisse jamais modifier le déroulement du programme; des capacités empêchent une donnée privée de sortir par un flux non autorisé [7]. Les auteurs rapportent 77 % de tâches résolues avec sécurité prouvable sur AgentDojo, contre 84 % sans défense : la séparation a un coût.

Appliqué à la négociation, le principe donne deux composants.

| | Diplomate | Évaluateur interne |
|---|---|---|
| Lit | Les messages de la contrepartie | Des offres structurées, à champs typés |
| Détient | Aucun secret | Seuils, coûts, règles d'approbation |
| Produit | Texte et offres structurées | Une décision bornée : accepter, refuser, contre-proposer |

Le Diplomate est un modèle de langage; l'Évaluateur, autant que possible, des règles et un calcul dans le système d'enregistrement. Le Diplomate ne peut pas divulguer ce qu'il ignore. L'Évaluateur ne peut pas être détourné par un texte qu'il ne lit pas. Entre les deux, la frontière est un schéma validé, non une consigne.

### Ce que la scission ne règle pas

Les décisions elles-mêmes renseignent l'adversaire. Une prépublication de juillet 2026, acceptée à l'atelier AI4TCI d'ARES 2026, formalise cette fuite comportementale : un observateur infère le prix de réserve à partir des trajectoires de concession, du rythme et des schémas de convergence, sans qu'aucune valeur soit divulguée [8]. Selon le résumé, les techniques cryptographiques protègent les valeurs explicites et laissent passer cette fuite. Le texte propose une politique de négociation aléatoire et rapporte, sur 3 000 négociations bilatérales synthétiques, une précision d'inférence adverse réduite de 43 à 50 %, le taux de succès et l'utilité restant supérieurs à 90 %. Fondé sur des simulations, le résultat indique une direction, pas un réglage.

Trois mesures en découlent, à titre d'hypothèses de travail : plafonner le nombre de tours, ne pas motiver un refus, répondre par paliers plutôt qu'en valeurs exactes.

---

## 45.5 Calcul partagé confidentiel : salles blanches et environnements d'exécution de confiance

Certaines collaborations exigent de calculer sur les données des deux parties : rapprocher une prévision de demande d'une capacité, vérifier qu'une zone d'accord existe. Aucune ne veut livrer ses données à l'autre, ni à un tiers.

Une salle blanche de données (*data clean room*) y répond : les données de chacun entrent dans un environnement où ne s'exécute qu'un code approuvé par tous, et seul un résultat convenu en sort. Un environnement d'exécution de confiance (TEE) y ajoute une garantie matérielle contre les logiciels et les administrateurs de l'exploitant, non contre qui tient physiquement le serveur (chapitre 46).

### Un exemple documenté

La documentation de Confidential Space, chez Google Cloud, décrit ce modèle sans employer le terme de salle blanche [9]. Trois rôles y sont séparés et supposés se méfier les uns des autres. Les collaborateurs de données fixent les conditions d'accès à leurs données; ils ne voient pas celles des autres et ne modifient pas le code. L'auteur de la charge de travail écrit le code, sans accès aux données ni aux résultats. L'exploitant la lance, sans accès aux données ni prise sur le code.

Le mécanisme central est l'attestation. Un service vérifie des assertions sur l'image du système, le conteneur et la machine virtuelle, puis émet un jeton. Chaque collaborateur conditionne l'accès à ses clés aux attributs de ce jeton : la donnée ne se déchiffre que pour la charge de travail convenue. Le matériel pris en charge comprend AMD SEV, Intel TDX et Intel TDX avec NVIDIA Confidential Computing [9].

### Les limites à retenir

La page en signale deux [9]. Les collaborateurs peuvent accéder aux résultats, selon ce que produit la charge de travail : le TEE protège le calcul, pas la sortie. Et tous les rôles doivent coopérer pour qu'un résultat existe.

La confidentialité dépend donc du code approuvé autant que du matériel. Un code qui renvoie une ligne par client divulgue tout, enclave ou non. La revue du code et la forme de la sortie (agrégat, seuil minimal, réponse binaire) sont l'objet réel de l'accord.

---

## 45.6 Collusion algorithmique

Le mot recouvre deux risques : des agents de tarification concurrents qui s'alignent au détriment des clients, et des agents qui se coordonnent en secret au détriment de leurs mandants.

### L'alignement des prix

Le résultat fondateur est évalué par les pairs : Calvano et ses coauteurs montrent en 2020 que des algorithmes de tarification par apprentissage Q, en concurrence répétée, apprennent de façon constante à pratiquer des prix supraconcurrentiels, sans communiquer entre eux [10].

Fish, Gonczarowski et Shorrer étendent le constat aux modèles de langage [11]. Dans leurs expériences en oligopole, des agents de tarification fondés sur un LLM atteignent rapidement et de façon autonome des prix supraconcurrentiels. Des variations de formulation en apparence anodines dans les consignes modifient fortement l'écart, et les résultats s'étendent aux enchères. Le texte, révisé le 31 août 2026, indique une acceptation à la conférence EC 2026.

La consigne d'un agent de tarification est donc un objet de conformité : elle se versionne et se fait revoir par le contentieux, comme une politique de prix.

### La coordination secrète

Une prépublication de Motwani et de ses coauteurs, révisée en juillet 2025, formalise la collusion secrète entre agents génératifs, où une coordination non voulue passe par des canaux stéganographiques difficiles à détecter [12]. Le résumé juge les capacités stéganographiques des modèles testés encore limitées, avec un saut pour GPT-4, et recommande une surveillance continue des modèles de pointe.

### L'état du droit et des défenses

Au Canada, le Bureau de la concurrence a publié le 22 janvier 2026 un compte rendu de sa consultation sur la tarification algorithmique, qui a recueilli plus de cent mémoires. L'un des quatre thèmes récurrents est que cette tarification peut mener à des comportements anticoncurrentiels [13]. Le document rapporte des avis et ne fixe aucune règle. L'argument de l'autonomie ne protège pas l'entreprise (chapitre 36).

Le chapitre 31 constate que les menaces multi-agents n'ont aucune défense éprouvée; rien de ce qui a été lu ici ne le contredit. Les mesures suivantes sont des précautions, non des parades :

- journaliser, côté entreprise, tous les échanges entre agents;
- préférer des messages structurés au texte libre, ce qui restreint, par déduction, l'espace d'un canal caché;
- faire examiner toute salle blanche partagée avec un concurrent, dont le résultat peut être un signal de prix.

---

## 45.7 Du contrat au règlement : rapprochement à trois voies

### Un contrôle comptable établi

Le rapprochement à trois voies (*three-way matching*) est une pratique des comptes fournisseurs. La documentation d'un progiciel de gestion la définit ainsi : rapprocher le prix de la facture du prix du bon de commande, et la quantité facturée de la quantité des réceptions [14]. Le rapprochement à deux voies s'arrête au prix.

Les écarts se comparent à des tolérances, fixées par entité, par fournisseur ou par article. Dans l'exemple de la documentation, une facture à 1,10 pour un article commandé à 1,00, sous une tolérance de 5 %, est retenue jusqu'à résolution de l'écart [14].

### Pourquoi il compte davantage avec des agents

Les protocoles de paiement agentiques prouvent autre chose. Un mandat AP2 établit qu'un paiement est autorisé pour un panier; x402 place le paiement dans l'échange HTTP (chapitre 10). Ni l'un ni l'autre ne prouve que la chose commandée a été livrée, et les litiges restent hors du champ des spécifications. Une facture injectée, un prix modifié après l'accord ou une livraison partielle passent sans contrôle si l'agent qui négocie est aussi celui qui paie.

### Une cible de conception

L'exigence d'un rapprochement à trois voies avant un règlement AP2 ou x402 n'a été trouvée dans aucune spécification ni documentation lue. Elle est proposée ici comme cible de conception.

| Voie | Achat de biens | Échange de données fédéré |
|---|---|---|
| Ce qui a été convenu | Bon de commande | Accord finalisé en DSP [4] |
| Ce qui a été reçu | Réception enregistrée | État du transfert au connecteur [2] |
| Ce qui est réclamé | Facture | Demande de paiement présentée à l'agent |

Quatre règles la rendent effective.

1. **Trois sources indépendantes.** Une réception déclarée par le fournisseur n'en est pas une.
2. **Un code déterministe.** Le rapprochement est un calcul, pas un jugement de modèle (chapitre 17); les tolérances vivent dans le système d'enregistrement.
3. **Une séparation des tâches.** L'agent qui négocie ne déclenche pas le paiement; le mandat ne s'émet qu'après un rapprochement réussi.
4. **Un écart suspend.** Hors tolérance, le dossier passe à un humain (chapitre 22).

Un cas échappe au schéma : le micropaiement x402, où le service est rendu dans la réponse qui suit le paiement. L'option du chapitre 10 s'applique : un portefeuille dédié et plafonné, complété ici par un rapprochement a posteriori. Un paiement indu se traite par compensation (chapitre 18).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Droits d'usage | ODRL 2.2, validé par code avant toute offre | Partenaire unique sous contrat classique |
| Accès aux données | DSP par un connecteur; l'agent passe par un outil étroit | Aucun espace commun : entente bilatérale (chapitre 29) |
| Identité et délégation | Justificatif d'entité vérifiable (vLEI si le réseau l'accepte); délégation distincte, bornée, révocable | Réseau fermé à adhésion contractuelle |
| Secrets de négociation | Hors du contexte du modèle exposé à la contrepartie | Paramètres publics |
| Calcul sur données conjointes | TEE avec attestation, code revu, sortie agrégée | Données non sensibles : transfert sous accord |
| Consignes de tarification | Versionnées et revues par le contentieux | — |
| Règlement | Rapprochement à trois voies avant tout mandat ou signature | Micropaiement : plafond et rapprochement a posteriori |

---

## Points à retenir

- Le modèle de langage propose; les protections tiennent à des composants déterministes, attestés ou contractuels.
- ODRL exprime une politique et DSP en fait un accord par une machine à sept états. Ni l'un ni l'autre n'applique l'accord une fois les données copiées.
- Le connecteur EDC offre trois points de contrôle : politique d'accès cachée, approbation manuelle, retrait d'un accord.
- Le justificatif OOR du vLEI désigne un représentant officiel humain. Son extension aux agents est une orientation de la GLEIF, sans format publié dans les pages lues.
- La scission « Diplomate / Évaluateur interne », sans source, applique un principe publié : une donnée non fiable ne doit pas atteindre ce qui détient un secret. Elle ne suffit pas, car les concessions révèlent le prix de réserve.
- Un TEE protège le calcul contre les logiciels et les administrateurs de l'exploitant, pas la sortie contre les participants.
- Des agents de tarification fondés sur des LLM atteignent en expérience, de façon autonome, des prix supraconcurrentiels; la formulation des consignes pèse sur le résultat.
- Un mandat de paiement prouve une autorisation, non une livraison. Le rapprochement à trois voies comble l'écart; son raccord aux protocoles d'agents reste à spécifier.

---

## Sources

Pages primaires lues le 12 novembre 2026 :

1. [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
2. [Eclipse Dataspace Components — plan de contrôle](https://eclipse-edc.github.io/documentation/for-adopters/control-plane/)
3. [Dataspace Protocol 2025-1](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1/) — présentation et statut seulement.
4. [Dataspace Protocol — Contract Negotiation Protocol](https://raw.githubusercontent.com/eclipse-dataspace-protocol-base/DataspaceProtocol/main/specifications/negotiation/contract.negotiation.protocol.md) — source du dépôt.
5. [GLEIF — vLEI Ecosystem Governance Framework](https://www.gleif.org/en/vlei/introducing-the-verifiable-lei-vlei)
6. [GLEIF — When AI agents transact, who stands behind them?](https://www.gleif.org/en/newsroom/blog/when-ai-agents-transact-who-stands-behind-them-why-verifiable-organizational-identity-is-critical-to-agentic-payments) — billet d'organisme.
7. [Defeating Prompt Injections by Design (arXiv 2503.18813)](https://arxiv.org/abs/2503.18813) — résumé.
8. [Behavioral Privacy Leakage in Agentic Negotiation (arXiv 2607.06815)](https://arxiv.org/abs/2607.06815) — résumé.
9. [Google Cloud — Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) — documentation d'éditeur.
10. [Calvano et coll., AER 110(10), 2020](https://www.aeaweb.org/articles?id=10.1257/aer.20190623) — résumé.
11. [Algorithmic Collusion by Large Language Models (arXiv 2404.00806)](https://arxiv.org/abs/2404.00806) — résumé.
12. [Secret Collusion among AI Agents (arXiv 2402.07510)](https://arxiv.org/abs/2402.07510) — résumé.
13. [Bureau de la concurrence — communiqué du 22 janvier 2026](https://www.canada.ca/en/competition-bureau/news/2026/01/competition-bureau-report-highlights-public-feedback-on-algorithmic-pricing-and-competition.html)
14. [Microsoft Learn — Accounts payable invoice matching](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-invoice-matching) — documentation d'éditeur.

Repérés, non lus :

15. [draft-hood-agtp-lei-00](https://datatracker.ietf.org/doc/draft-hood-agtp-lei/); [GLEIF, Agentic AI in Payments](https://www.gleif.org/organizational-identity/research-publications/2026-08-13_agentic_ai_in_payments_v1.0-1.pdf).

## Limites de ce chapitre

- **Éléments demandés sans source.** « Diplomate / Évaluateur interne » et le rapprochement à trois voies avant un règlement AP2 ou x402 figurent comme cibles de conception. « Clean Rooms sur TEE » repose sur une seule documentation d'éditeur, qui n'emploie pas le terme; la définition d'une salle blanche et la description de l'intégration bilatérale viennent de la connaissance générale.
- **vLEI.** La page du cadre n'explique ni la vérification des rôles ni le lien avec ISO 5009. La répartition entité / OOR / délégation est une déduction. Le Delegated Agent Participant ID est repris du chapitre 37, sans relecture de sa source.
- **DSP, EDC, ODRL.** La machine à états a été lue dans la branche principale du dépôt; la page 2025-1, relue à l'audit, n'en affiche pas le texte. DCP, le moteur de politiques d'EDC, la fin de la recommandation ODRL et son vocabulaire n'ont pas été lus.
- **Articles.** [7], [8] et [10] à [12] sont connus par leur résumé.
- **Mesures proposées.** L'effet des messages structurés sur les canaux cachés et les mesures de la section 45.4 n'ont aucune mise en œuvre lue.
- **Concurrence.** Seul le communiqué du Bureau a été lu; aucune autre autorité n'a été vérifiée.
- **AP2 et x402.** Leur description reprend le chapitre 10. Les renvois aux autres chapitres ont été vérifiés à l'audit, sans relecture de leurs sources.
