# Registre de gel par pièce — Vol. IV, *La somme agentique*

| Champ | Valeur |
|---|---|
| **Nature** | **Une ligne par pièce, cinquante pièces.** Registre de gel du Vol. IV, sur le modèle du Vol. III (`99-registre-gel.md`) : **statut, date de gel, cible, volumétrie réelle**. Livrable de la **condition de sortie (e) de la porte G-3** et du jalon **J-IV-2** ([PRD](PRD.md) §9 et §12). |
| **Version** | **1.0 — constitution, 28 juillet 2026.** Première version ; aucune version antérieure. |
| **Autorité** | ⚠ **Ce fichier ne porte aucune décision.** Il n'est ni une gouvernance (c'est le [PRD](PRD.md)), ni une spécification de contenu (c'est le [TOC](TOC.md)), ni un socle (c'est [`socle-consolide.md`](socle-consolide.md)). **En cas d'écart avec l'en-tête d'une pièce, c'est l'en-tête qui fait foi** pour le statut et la date de gel, et [`decompte.sh`](decompte.sh) pour la volumétrie. Le contrôle **P6** de [`check-compendium.py`](check-compendium.py) oppose les trois. |
| **Règle de tenue** | Une ligne se renseigne **au même commit que la pièce qu'elle décrit** (PRD §9). *Un statut qui ment est pire qu'un statut absent* — leçon du Vol. II, dont le tableau de suivi a annoncé « 0 rédigée » pendant deux phases entières. |
| **Volumétrie** | La colonne **Réel** porte la mesure de [`decompte.sh`](decompte.sh), **seule autorité de décompte du volume** (porte G-2, éprouvée sur les trois corpus entiers le 27 juillet 2026) — jamais un chiffre recopié d'un `README.md`. La colonne **Cible** est **indicative et non normative** : un écart se **documente**, et la décision d'auteur **D-4 interdit l'amputation comme le gonflement**. |

---

## ⚠ Ce que ce registre atteste, et ce qu'il n'atteste pas

**Il est alimenté rétroactivement.** Les cinquante pièces existaient avant lui : elles ont été
rédigées les 27 et 28 juillet 2026, hors portes, et ce registre est constitué **après**, en lisant
leurs en-têtes et en re-mesurant leur corps. Trois conséquences, et la première est la seule qui
compte.

⚠ **(a) Un registre rétroactif n'atteste pas qu'une pièce a été gelée à sa date — seulement ce que
son en-tête déclare.** *Une convention de datation sans registre est une déclaration d'intention ;
un registre constitué après coup est une déclaration d'intention **transcrite**.* La date de gel
portée ici est celle du **gel unique du 27 juillet 2026** (décision d'auteur **D-1**), que les
cinquante en-têtes portent sans exception. Elle ne dit pas qu'un fait a été re-vérifié ce jour-là :
le **volet résiduel de G-1 n'est pas levé**, et [`gel-2026-07-27.md`](gel-2026-07-27.md) ne reprend
que **douze faits, du seul Livre I**. *Ce qui n'a pas été re-daté porte la date de son volume source,
non celle du gel unique.*

**(b) Le statut est le même pour les cinquante, et c'est le résultat.** Toutes se déclarent
**brouillon de rédaction, non publiable** : **G-3 n'est pas franchie**, le socle consolidé n'était
pas constitué à leur rédaction, **CA-IV-11 et CA-IV-13 demeurent insatisfaites** — elles exigent un
relecteur distinct du rédacteur, que **D-6 ne fournit pas**. *Cinquante pièces écrites hors portes ne
franchissent aucune porte ; elles en documentent le coût.*

**(c) La colonne Réel est mesurée ici, non recopiée — et la mesure a été confrontée, non
supposée.** Les cinq totaux de Livre concordent **à l'unité près** avec les `README.md` des cinq
dossiers, re-mesurés par la passe de correction du 28 juillet 2026 : 64 750, 62 054, 91 477, 56 025
et 26 474. *Concorder n'est pas recopier* — les cinquante mesures ont été prises par
[`decompte.sh`](decompte.sh) pour ce registre, et la coïncidence est le résultat du contrôle, non
sa méthode.

⚠ **Une divergence subsiste néanmoins, et elle est d'un niveau supérieur** : le
[`CLAUDE.md` de la racine](../../CLAUDE.md) et celui du dossier portent encore les cardinaux
d'**avant** la passe de correction — 61 677 mots au Livre II (**+377** ici), 55 249 au Livre IV
(**+776**), 25 017 au Livre V (**+1 457**), et « +0,3 % » au Livre III pour **+1,6 %**. *Un corps
corrigé périme le cardinal qui le décrivait*, et ces quatre-là n'ont pas suivi. ⚠ **Ils ne sont pas
corrigés ici** — le périmètre de ce fichier est le registre, et *re-mesurer chez le voisin sans
mandat produit deux chiffres au lieu d'un.* La divergence est **signalée, non arbitrée** ; elle se
solde à la passe qui rouvrira ces deux fichiers.

---

## Les cinquante lignes

**Colonnes.** *Cible* : l'enveloppe déclarée au champ « Volumétrie cible » de la pièce — **dérivée,
non prescrite**. *Réel* : la mesure de `decompte.sh` au 28 juillet 2026. *En tête* : ☑ la pièce
publie sa mesure dans son en-tête (le contrôle P6 les oppose) ; ☐ elle la renvoie au `README.md` de
son Livre, et P6 ne contrôle alors que la date de gel et la cible.

| # | Pièce | Fichier | Statut | Date de gel | Cible | Réel | Écart | En tête |
|---|---|---|---|---|---|---|---|---|
| 1 | Chapitre 1 — L'interopérabilité comme problème d'intégration d'entreprise | [`Livre I/01-interoperabilite-integration-entreprise.md`](../Livre%20I/01-interoperabilite-integration-entreprise.md) | Brouillon, non publiable | 27 juillet 2026 | 11 000 | 10 724 | −2,5 % | ☑ |
| 2 | Chapitre 2 — Données, sémantique et ontologies | [`Livre I/02-donnees-semantique-ontologies.md`](../Livre%20I/02-donnees-semantique-ontologies.md) | Brouillon, non publiable | 27 juillet 2026 | 8 000 | 5 245 | −34,4 % | ☑ |
| 3 | Chapitre 3 — Sécurité, identité et gouvernance de l'interopérabilité | [`Livre I/03-securite-identite-gouvernance.md`](../Livre%20I/03-securite-identite-gouvernance.md) | Brouillon, non publiable | 27 juillet 2026 | 9 000 | 5 069 | −43,7 % | ☑ |
| 4 | Chapitre 4 — L'ingénierie des systèmes agentiques : anatomie, raisonnement, outils | [`Livre I/04-ingenierie-systemes-agentiques.md`](../Livre%20I/04-ingenierie-systemes-agentiques.md) | Brouillon, non publiable | 27 juillet 2026 | 9 000 | 7 145 | −20,6 % | ☑ |
| 5 | Chapitre 5 — Ancrage informationnel : mémoire, contexte, RAG agentique | [`Livre I/05-ancrage-informationnel.md`](../Livre%20I/05-ancrage-informationnel.md) | Brouillon, non publiable | 27 juillet 2026 | 7 500 | 4 397 | −41,4 % | ☑ |
| 6 | Chapitre 6 — Systèmes multi-agents, évaluation et sûreté | [`Livre I/06-multi-agents-evaluation-surete.md`](../Livre%20I/06-multi-agents-evaluation-surete.md) | Brouillon, non publiable | 27 juillet 2026 | 8 500 | 3 784 | −55,5 % | ☑ |
| 7 | Chapitre 7 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts | [`Livre I/07-genealogie-gouvernance.md`](../Livre%20I/07-genealogie-gouvernance.md) | Brouillon, non publiable | 27 juillet 2026 | 8 000 | 4 887 | −38,9 % | ☑ |
| 8 | Chapitre 8 — Anatomie : MCP (agent-outil) et A2A (agent-agent) | [`Livre I/08-anatomie-mcp-a2a.md`](../Livre%20I/08-anatomie-mcp-a2a.md) | Brouillon, non publiable | 27 juillet 2026 | 10 000 | 5 138 | −48,6 % | ☑ |
| 9 | Chapitre 9 — Découverte, registres, portabilité et pile protocolaire | [`Livre I/09-decouverte-registres-pile.md`](../Livre%20I/09-decouverte-registres-pile.md) | Brouillon, non publiable | 27 juillet 2026 | 9 000 | 5 530 | −38,6 % | ☑ |
| 10 | Chapitre 10 — Transaction et infrastructure : AP2 et AGNTCY | [`Livre I/10-transaction-infrastructure.md`](../Livre%20I/10-transaction-infrastructure.md) | Brouillon, non publiable | 27 juillet 2026 | 7 000 | 7 036 | +0,5 % | ☑ |
| 11 | Chapitre 11 — Modes d'échec et taxonomie des risques protocolaires | [`Livre I/11-modes-echec-risques-protocolaires.md`](../Livre%20I/11-modes-echec-risques-protocolaires.md) | Brouillon, non publiable | 27 juillet 2026 | 6 000 | 5 795 | −3,4 % | ☑ |
| 12 | Chapitre 12 — L'héritage et les standards étirés : un demi-siècle d'identités non humaines, puis OAuth, OIDC et SCIM face à l'agent | [`Livre II/12-heritage-standards-etires.md`](../Livre%20II/12-heritage-standards-etires.md) | Brouillon, non publiable | 27 juillet 2026 | 6 200 | 7 372 | +18,9 % | ☑ |
| 13 | Chapitre 13 — L'identité décentralisée : VC, DID et la promesse du portable | [`Livre II/13-identite-decentralisee-vc-did.md`](../Livre%20II/13-identite-decentralisee-vc-did.md) | Brouillon, non publiable | 27 juillet 2026 | 4 000 | 3 947 | −1,3 % | ☑ |
| 14 | Chapitre 14 — La grille des cinq questions | [`Livre II/14-grille-cinq-questions.md`](../Livre%20II/14-grille-cinq-questions.md) | Brouillon, non publiable | 27 juillet 2026 | 3 000 | 3 514 | +17,1 % | ☑ |
| 15 | Chapitre 15 — Émettre : Agent Card signée, annuaires, registres gouvernés | [`Livre II/15-emettre-carte-annuaires-registres.md`](../Livre%20II/15-emettre-carte-annuaires-registres.md) | Brouillon, non publiable | 27 juillet 2026 | 5 800 | 8 187 | +41,2 % | ☑ |
| 16 | Chapitre 16 — Le passeport d'agent : synthèse d'un objet encore virtuel | [`Livre II/16-passeport-agent.md`](../Livre%20II/16-passeport-agent.md) | Brouillon, non publiable | 27 juillet 2026 | 4 500 | 4 828 | +7,3 % | ☑ |
| 17 | Chapitre 17 — La chaîne de mandat et le problème des deux sauts | [`Livre II/17-chaine-mandat-deux-sauts.md`](../Livre%20II/17-chaine-mandat-deux-sauts.md) | Brouillon, non publiable | 27 juillet 2026 | 5 700 | 6 970 | +22,3 % | ☑ |
| 18 | Chapitre 18 — Know Your Agent : la vérification d'agent tiers inter-domaines | [`Livre II/18-know-your-agent.md`](../Livre%20II/18-know-your-agent.md) | Brouillon, non publiable | 27 juillet 2026 | 3 800 | 4 252 | +11,9 % | ☑ |
| 19 | Chapitre 19 — Taxonomie des attaques d'identité et de délégation | [`Livre II/19-taxonomie-attaques-identite-delegation.md`](../Livre%20II/19-taxonomie-attaques-identite-delegation.md) | Brouillon, non publiable | 27 juillet 2026 | 5 000 | 5 529 | +10,6 % | ☑ |
| 20 | Chapitre 20 — Usurpation, révocation et boucle défensive : du *rug-pull* à l'*agentic SOC* | [`Livre II/20-usurpation-revocation-boucle-defensive.md`](../Livre%20II/20-usurpation-revocation-boucle-defensive.md) | Brouillon, non publiable | 27 juillet 2026 | 6 200 | 8 868 | +43,0 % | ☑ |
| 21 | Chapitre 21 — L'horloge post-quantique : menace sur la pile identitaire, crypto-agilité et dette de migration | [`Livre II/21-horloge-post-quantique.md`](../Livre%20II/21-horloge-post-quantique.md) | Brouillon, non publiable | 27 juillet 2026 | 5 800 | 8 587 | +48,1 % | ☑ |
| 22 | Chapitre 22 — Options d'orchestration et paradigme APM : la taxonomie OO1-OO4 et l'autonomie encadrée | [`Livre III/22-options-orchestration-paradigme-apm.md`](../Livre%20III/22-options-orchestration-paradigme-apm.md) | Brouillon, non publiable | 27 juillet 2026 | 8 500 | 8 464 | −0,4 % | ☐ |
| 23 | Chapitre 23 — Les frameworks d'orchestration d'entreprise | [`Livre III/23-frameworks-orchestration-entreprise.md`](../Livre%20III/23-frameworks-orchestration-entreprise.md) | Brouillon, non publiable | 27 juillet 2026 | 5 000 | 4 435 | −11,3 % | ☐ |
| 24 | Chapitre 24 — Le passage à l'échelle de l'entreprise | [`Livre III/24-passage-echelle-entreprise.md`](../Livre%20III/24-passage-echelle-entreprise.md) | Brouillon, non publiable | 27 juillet 2026 | 9 500 | 12 628 | +32,9 % | ☐ |
| 25 | Chapitre 25 — E-23 : le risque de modèle à l'ère de l'IA | [`Livre III/25-e23-risque-modele.md`](../Livre%20III/25-e23-risque-modele.md) | Brouillon, non publiable | 27 juillet 2026 | 7 000 | 6 142 | −12,3 % | ☐ |
| 26 | Chapitre 26 — Le vide fédéral : de C-27 à C-36 | [`Livre III/26-vide-federal-c27-c36.md`](../Livre%20III/26-vide-federal-c27-c36.md) | Brouillon, non publiable | 27 juillet 2026 | 2 500 | 2 316 | −7,4 % | ☐ |
| 27 | Chapitre 27 — Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25 | [`Livre III/27-quebec-amf-article-12-1.md`](../Livre%20III/27-quebec-amf-article-12-1.md) | Brouillon, non publiable | 27 juillet 2026 | 7 500 | 6 984 | −6,9 % | ☐ |
| 28 | Chapitre 28 — Valeurs mobilières : l'avis ACVM 11-348 | [`Livre III/28-valeurs-mobilieres-acvm-11-348.md`](../Livre%20III/28-valeurs-mobilieres-acvm-11-348.md) | Brouillon, non publiable | 27 juillet 2026 | 2 500 | 2 379 | −4,8 % | ☐ |
| 29 | Chapitre 29 — Le pont : des contraintes réglementaires aux frames déterministes | [`Livre III/29-pont-frames-deterministes.md`](../Livre%20III/29-pont-frames-deterministes.md) | Brouillon, non publiable | 27 juillet 2026 | 4 000 | 4 580 | +14,5 % | ☐ |
| 30 | Chapitre 30 — Le maillage réglementaire international et la normalisation institutionnelle | [`Livre III/30-maillage-reglementaire-normalisation.md`](../Livre%20III/30-maillage-reglementaire-normalisation.md) | Brouillon, non publiable | 27 juillet 2026 | 7 500 | 8 017 | +6,9 % | ☐ |
| 31 | Chapitre 31 — Le vertical financier : pourquoi l'agentique y est durcie | [`Livre III/31-vertical-financier-durcisseurs.md`](../Livre%20III/31-vertical-financier-durcisseurs.md) | Brouillon, non publiable | 27 juillet 2026 | 8 500 | 8 517 | +0,2 % | ☐ |
| 32 | Chapitre 32 — Le cadre des services bancaires axés sur le consommateur | [`Livre III/32-cadre-bancaire-consommateur.md`](../Livre%20III/32-cadre-bancaire-consommateur.md) | Brouillon, non publiable | 27 juillet 2026 | 3 500 | 3 271 | −6,5 % | ☐ |
| 33 | Chapitre 33 — ISO 20022 : Lynx accompli, RTR visé | [`Livre III/33-iso-20022-lynx-rtr.md`](../Livre%20III/33-iso-20022-lynx-rtr.md) | Brouillon, non publiable | 27 juillet 2026 | 3 500 | 2 859 | −18,3 % | ☐ |
| 34 | Chapitre 34 — Les sous-domaines financiers : banque, assurance, patrimoine | [`Livre III/34-sous-domaines-financiers.md`](../Livre%20III/34-sous-domaines-financiers.md) | Brouillon, non publiable | 27 juillet 2026 | 9 500 | 9 629 | +1,4 % | ☐ |
| 35 | Chapitre 35 — Études de cas : la production agentique canadienne (2025-2026) | [`Livre III/35-etudes-de-cas-production-canadienne.md`](../Livre%20III/35-etudes-de-cas-production-canadienne.md) | Brouillon, non publiable | 27 juillet 2026 | 6 000 | 6 800 | +13,3 % | ☐ |
| 36 | Chapitre 36 — Prospective : AP2 sur les rails canadiens ? | [`Livre III/36-prospective-ap2-rails-canadiens.md`](../Livre%20III/36-prospective-ap2-rails-canadiens.md) | Brouillon, non publiable | 27 juillet 2026 | 5 000 | 4 456 | −10,9 % | ☐ |
| 37 | Chapitre 37 — Le maillage d'agents : du *service mesh* au point d'application (PEP/PDP et *zero trust* agentique) | [`Livre IV/37-maillage-agents-point-application.md`](../Livre%20IV/37-maillage-agents-point-application.md) | Brouillon, non publiable | 27 juillet 2026 | 11 000 | 9 756 | −11,3 % | ☐ |
| 38 | Chapitre 38 — L'observabilité agentique | [`Livre IV/38-observabilite-agentique.md`](../Livre%20IV/38-observabilite-agentique.md) | Brouillon, non publiable | 27 juillet 2026 | 6 000 | 5 693 | −5,1 % | ☐ |
| 39 | Chapitre 39 — Le cycle de vie opérationnel : évaluation continue, dérive et incident | [`Livre IV/39-cycle-de-vie-operationnel.md`](../Livre%20IV/39-cycle-de-vie-operationnel.md) | Brouillon, non publiable | 27 juillet 2026 | 6 500 | 6 165 | −5,2 % | ☐ |
| 40 | Chapitre 40 — Les indicateurs de l'AgentOps et le FinOps des agents | [`Livre IV/40-indicateurs-agentops-finops.md`](../Livre%20IV/40-indicateurs-agentops-finops.md) | Brouillon, non publiable | 27 juillet 2026 | 6 500 | 5 564 | −14,4 % | ☐ |
| 41 | Chapitre 41 — La fabrique d'agents : produire, certifier et réémettre le parc | [`Livre IV/41-fabrique-agents.md`](../Livre%20IV/41-fabrique-agents.md) | Brouillon, non publiable | 27 juillet 2026 | 5 000 | 3 765 | −24,7 % | ☐ |
| 42 | Chapitre 42 — La matrice protocoles × exigences réglementaires | [`Livre IV/42-matrice-protocoles-exigences.md`](../Livre%20IV/42-matrice-protocoles-exigences.md) | Brouillon, non publiable | 27 juillet 2026 | 4 000 | 3 529 | −11,8 % | ☐ |
| 43 | Chapitre 43 — L'architecture de référence unifiée par couches | [`Livre IV/43-architecture-reference-couches.md`](../Livre%20IV/43-architecture-reference-couches.md) | Brouillon, non publiable | 27 juillet 2026 | 6 500 | 5 839 | −10,2 % | ☐ |
| 44 | Chapitre 44 — La formalisation ArchiMate | [`Livre IV/44-formalisation-archimate.md`](../Livre%20IV/44-formalisation-archimate.md) | Brouillon, non publiable | 27 juillet 2026 | 8 500 | 6 016 | −29,2 % | ☐ |
| 45 | Chapitre 45 — Le blueprint instancié et son cycle de vie : de Boréalis au portefeuille IBM, puis la naissance, la vie et la mort d'un agent d'entreprise | [`Livre IV/45-blueprint-instancie-cycle-de-vie.md`](../Livre%20IV/45-blueprint-instancie-cycle-de-vie.md) | Brouillon, non publiable | 27 juillet 2026 | 12 000 | 6 781 | −43,5 % | ☐ |
| 46 | Chapitre 46 — Instrumentation et feuille de route vers le 1ᵉʳ mai 2027 | [`Livre IV/46-instrumentation-feuille-route.md`](../Livre%20IV/46-instrumentation-feuille-route.md) | Brouillon, non publiable | 27 juillet 2026 | 3 000 | 2 917 | −2,8 % | ☐ |
| 47 | Chapitre 47 — L'artefact livré : provenance des composants et mise en service | [`Livre V/47-artefact-livre-provenance-mise-en-service.md`](../Livre%20V/47-artefact-livre-provenance-mise-en-service.md) | Brouillon, non publiable | 27 juillet 2026 | 9 300 | 5 897 | −36,6 % | ☑ |
| 48 | Chapitre 48 — La sémantique d'effet : idempotence, compensation, réconciliation | [`Livre V/48-semantique-effet-idempotence-compensation.md`](../Livre%20V/48-semantique-effet-idempotence-compensation.md) | Brouillon, non publiable | 27 juillet 2026 | 4 700 | 3 305 | −29,7 % | ☑ |
| 49 | Chapitre 49 — L'horizon 2027-2032 et la frontière de la connaissance vérifiable | [`Livre V/49-horizon-frontiere-connaissance-verifiable.md`](../Livre%20V/49-horizon-frontiere-connaissance-verifiable.md) | Brouillon, non publiable | 27 juillet 2026 | 15 800 | 13 740 | −13,0 % | ☑ |
| 50 | Chapitre 50 — Péremption et protocole de revalidation | [`Livre V/50-peremption-protocole-revalidation.md`](../Livre%20V/50-peremption-protocole-revalidation.md) | Brouillon, non publiable | 27 juillet 2026 | 4 200 | 3 532 | −15,9 % | ☑ |

---

## Bilan par Livre

⚠ **Deux cibles coexistent et les confondre fausse la lecture.** L'**enveloppe** est celle que le
TOC assigne au Livre ; la **somme des cibles dérivées** est celle qu'obtiennent les pièces en se
partageant l'enveloppe au prorata de leurs sections. *Les deux coïncident pour quatre Livres sur
cinq* — et **divergent de 28 000 mots au Livre I**, dont les onze pièces ont chacune dérivé sa cible
sans que personne n'additionne les dérivations. **C'est la cible dérivée qui est fausse, non les
pièces qui sont courtes** ; le Livre I est à **−0,4 %** de son enveloppe réelle.

| Livre | Pièces | Enveloppe (TOC) | Σ cibles dérivées | Réel | Écart / enveloppe |
|---|---|---|---|---|---|
| **Livre I** — Coopérer | 11 | 65 000 | 93 000 | 64 750 | −0,4 % |
| **Livre II** — Faire confiance | 10 | 50 000 | 50 000 | 62 054 | +24,1 % |
| **Livre III** — Encadrer | 15 | 90 000 | 90 000 | 91 477 | +1,6 % |
| **Livre IV** — Appliquer, exploiter, produire, composer | 10 | 69 000 | 69 000 | 56 025 | −18,8 % |
| **Livre V** — Livrer et clore | 4 | 34 000 | 34 000 | 26 474 | −22,1 % |
| **Total** | **50** | **308 000** | **336 000** | **300 780** | **−2,3 %** |

⚠ **Un agrégat à −2,3 % ne prouve rien sur ses pièces, et c'est le résultat le plus transférable de
ce registre.** Les écarts individuels vont de **−55,5 %** (ch. 6) à **+48,1 %** (ch. 21) : cent trois
points d'amplitude, que la conformité de l'agrégat masque intégralement. *Deux forces jouent dans
tous les Livres, et ce qui change est laquelle domine* — **le bornage allonge** (Livre II, +24,1 %),
**le siège raccourcit** (Livres IV et V, dont les pièces renvoient là où une monographie
développerait). **L'enveloppe héritée n'avait budgété ni l'une ni l'autre.**

**C'est la mesure que la décision d'auteur D-4 attendait**, et elle ne la tranche pas : le
re-calibrage des enveloppes reste **remis à une passe unique de clôture**, et **l'amputation
demeure interdite**.

---

## Contrôle

```
python PRD/check-compendium.py     # P6 : une ligne par pièce, date et volumétrie concordantes
```

⚠ **Ne jamais tuyauter ce contrôle dans un enchaînement `&&`** avec `check-toc.py`,
`check-sieges.py` ou `decompte.sh` : le code de sortie du dernier maillon masquerait l'échec des
précédents — faute déjà commise sur le ch. 6, poussé avec un défaut de rendu alors que le contrôle
échouait.
