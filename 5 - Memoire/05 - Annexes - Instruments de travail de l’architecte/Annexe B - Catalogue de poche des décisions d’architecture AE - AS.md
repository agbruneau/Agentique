# Annexe B — Catalogue de poche des décisions d’architecture AE / AS

Générée automatiquement depuis `registre/decisions.json`.

## B.1 Correspondance principes PRIN, dix décisions CAD26 et principes PRI

| Principe PD28 (`PRI`) | Principes CAD26 (`PRIN`) | Décision structurante CAD26 | Règle directrice |
| --- | --- | --- | --- |
| PRI-001 | PRIN-04, PRIN-10 | Décision 2 : Rien ne contourne les points d’application | Registre, NHI, politiques et trace précèdent toute autonomie |
| PRI-002 | PRIN-08 | Décision 3 : La simplicité d’abord | Machine à états déterministe autour des cellules probabilistes |
| PRI-003 | PRIN-01, PRIN-02 | Décision 1 : Deux protocoles pivots, versions épinglées | Séparation stricte entre outil MCP vertical et pair A2A |
| PRI-004 | PRIN-03 | Décision 5 : Une identité propre à chaque agent, des droits délégués et de courte durée | Identité NHI distincte et jetons RFC 8693 atténués |
| PRI-005 | PRIN-07 | Décision 6 : Présomption d’injection | Politiques hors modèle, règle de deux et retrait d’exfiltration |
| PRI-006 | PRIN-04, PRIN-12 | Décision 4 : Une échelle d’autonomie unique | Autonomie méritée par domaine × classe et rétrogradation immédiate |
| PRI-007 | PRIN-05, PRIN-10 | Décision 9 : Une personne nommée répond de chaque agent | Supervision liée à h, anti-complaisance et recours client effectif |
| PRI-008 | PRIN-02, PRIN-09, PRIN-11 | Décision 10 : Conformité dès la conception | Sémantique versionnée, ACL amont et mémoire longue parcimonieuse |
| PRI-009 | PRIN-05, PRIN-12 | Décision 7 : Réversibilité par conception | Exécution durable, idempotence, Saga et canal de compensation dédié |
| PRI-010 | PRIN-03, PRIN-10 | Décision 10 : Conformité dès la conception | Cloisonnement étanche par personne morale, consentement et loi |
| PRI-011 | PRIN-09, PRIN-11, PRIN-12 | Décision 10 : Conformité dès la conception | Maîtrise juridictionnelle des six substrats et continuité bimodèle |
| PRI-012 | PRIN-03, PRIN-06 | Décision 5 : Une identité propre à chaque agent, des droits délégués et de courte durée | Certificats courts automatisés et transition post-quantique sans couture |
| PRI-013 | PRIN-06 | Décision 8 : On ne gouverne que ce qu’on voit | Corrélation OpenTelemetry sans renseignements personnels (RP) et voûte scellée |
| PRI-014 | PRIN-06, PRIN-08 | Décision 8 : On ne gouverne que ce qu’on voit | Modèle minimal suffisant, suivi carbone et pilotage au CPO |
| PRI-015 | PRIN-01, PRIN-09 | Décision 2 : Rien ne contourne les points d’application | Noyau de contrôle possédé, gravité des données et sortie |

## B.2 Sort des 31 ADR de 2027, rattachement aux 12 DEC et propriétaire

| ADR | Verdict | DEC cible | Rôle | Appui sourcé | Réserve ou condition |
| --- | --- | --- | --- | --- | --- |
| ADR-001 | Maintenue | — | AE↔AS | C27 § 1.4, 25.2 ; EXIG-ARC-17 | Invariant : zéro écriture SQL directe (PRI-002) |
| ADR-002 | Maintenue | — | AS | C27 § 17.1, 17.6 ; EXIG-ORC-01 | Séquencement maître déterministe maintenu (suivi SIG-013) |
| ADR-003 | Maintenue | — | AE | C27 § 8.7, 43.1 ; EXIG-GOV-08 | Recalée sur Stades 0–4 et Classe 1 (SIG-008) |
| ADR-004 | À réviser sur signal | — | AE | C27 § 11.2, 27.5 ; EXIG-INT-06 | Réviser selon gouvernance AAIF/IETF (SIG-004, SIG-008) |
| ADR-005 | À réviser sur signal | — | AS | C27 § 5.2, 13.3 ; EXIG-MCP-06 | Réviser sur MCP SEP-3398 et web (SIG-005, SIG-103) |
| ADR-006 | Généralisée | DEC-001 | AS | C27 § 6.4, 49.5 ; EXIG-A2A-03 | Retrait couplage incubation, agilité PQC (SIG-004, SIG-009) |
| ADR-007 | Généralisée | DEC-002 | AS | C27 § 7.1, 10.6 ; EXIG-ARC-03 | Neutralisée sur catalogues déclaratifs fermés (SIG-004, SIG-102) |
| ADR-008 | Maintenue | — | AS | C27 § 13.5, 15.3 ; EXIG-ARC-16 | Invariant : ACL amont sans repli service (PRI-008) |
| ADR-009 | Généralisée | DEC-003 | AE↔AS | C27 § 12.1, 12.2, 12.4 (p. 250) ; EXIG-INT-02 | Épingle l’ontologie 0.1.1 sans moteur en excluant 0.3.0.dev0 (p. 250), en dissonance avec l’Extrait 12.1 en 1.0.0 ; couplage rejeté par DEC-003 (SIG-110) |
| ADR-010 | Généralisée | DEC-004 | AS | C27 § 14.5, 31.6 ; EXIG-ARC-23 | Neutralisée : bi-temporalité et purge Loi 25 (SIG-106) |
| ADR-011 | Maintenue | — | AS | C27 § 16.6, 21.5 ; EXIG-ORC-02 | Invariant : zéro graphe cyclique libre (suivi SIG-014) |
| ADR-012 | Généralisée | DEC-005 | AS | C27 § 18.2, 18.5 ; EXIG-ORC-11 | Moteur durable neutre et revalidation réveil (SIG-014) |
| ADR-013 | Généralisée | DEC-005 | AS | C27 § 18.4, 19.7 ; EXIG-ORC-15 | Courtier neutre, Saga pivot et canal dédié (SIG-104) |
| ADR-014 | Généralisée | DEC-006 | AS | C27 § 44.3, 44.5 ; EXIG-ARC-08 | Passerelle modèles neutre, 3 paliers, KV-cache (SIG-015) |
| ADR-015 | Généralisée | DEC-007 | AE | C27 § 26.9, 27.4 ; EXIG-ARC-21 | Noyau possédé et étiquette d’entité groupe (SIG-108) |
| ADR-016 | Généralisée | DEC-008 | AE↔AS | C27 § 25.1, 25.4 ; EXIG-ARC-14 | Décimal exact et extinction CUA 12 mois (SIG-103) |
| ADR-017 | Maintenue | — | AS | C27 § 28.4, 28.5 ; EXIG-AUT-09 | Réserve § 28.5 : prototypes sans terrain (SIG-109) |
| ADR-018 | À réviser sur signal | — | AS | C27 § 29.4, 30.2 ; EXIG-IAM-08 | Réviser sur profils RFC WIMSE/PQC (SIG-003, SIG-011) |
| ADR-019 | Généralisée | DEC-009 | AS | C27 § 31.4, 49.7 ; EXIG-MCP-20 | Épinglage SHA-256 neutre et règle de deux (SIG-101) |
| ADR-020 | Généralisée | DEC-009 | AS | C27 § 30.6, 32.3 ; EXIG-SEC-08 | Politiques hors modèle neutres et microVM fermée (SIG-101) |
| ADR-021 | À réviser sur signal | — | AS | C27 § 33.2, 33.4 ; EXIG-OBS-01 | Réviser au passage Stable de gen_ai.* (SIG-006) |
| ADR-022 | Généralisée | DEC-010 | AS | C27 § 34.2, 48.5 ; EXIG-EVA-03 | Qualification pass^k sur bancs internes audités (SIG-013) |
| ADR-023 | Généralisée | DEC-011 | AE | C27 § 40.2, 40.5 ; EXIG-FIN-01 | Séquencée : affichage P1 puis refacturation P2 (SIG-015) |
| ADR-024 | À réviser sur signal | — | AE | C27 § 35.1, 38.4 ; EXIG-CON-11 | Réviser sur RIA, AMF IA, fédéral (SIG-001, SIG-102) |
| ADR-025 | Maintenue | — | AE | C27 § 39.3, 41.4 ; EXIG-GOV-01 | Étoile, parrain RH et anti-complaisance (SIG-017, SIG-106) |
| ADR-026 | Généralisée | DEC-012 | AE↔AS | C27 § 45.3, 45.7 ; EXIG-INT-22 | vLEI, Diplomate/Évaluateur et scellement PQC (SIG-007, SIG-009) |
| ADR-027 | À réviser sur signal | — | AE↔AS | C27 § 37.1, 46.1 ; EXIG-CON-05 | 6 substrats, repli [S] ; réviser TEE (SIG-016) |
| ADR-028 | Généralisée | DEC-008 | AS | C27 § 46.5, 46.8 ; EXIG-ORC-27 | Quotas déconnectés CRDT [S] et moniteur Simplex (SIG-109) |
| ADR-029 | Maintenue | — | AS | C27 § 47.1, 47.4 ; EXIG-GOV-03 | Réserve § 47.1 : gains contrastés, cibles [S] |
| ADR-030 | Généralisée | DEC-010 | AS | C27 § 15.1, 47.6 ; EXIG-SEC-17 | Quarantaine WAP amont et zéro interpréteur libre (SIG-109) |
| ADR-031 | À réviser sur signal | — | AE↔AS | C27 § 47.7, 47.8 ; EXIG-CON-10 | Distillation sous sas anti-RP [S] selon CPO (SIG-015) |

## B.3 Synthèse des 12 DEC neutralisées et gabarit décisionnel minimal

| DEC | Intitulé | Rôle | Exigences rattachées |
| --- | --- | --- | --- |
| DEC-001 | Contrat neutre de délégation, annuaire signé et PQC | AS | EXIG-A2A-01, EXIG-A2A-03, EXIG-IAM-08, EXIG-SEC-19 |
| DEC-002 | Interfaces génératives sur catalogue déclaratif sans code libre | AS | EXIG-ARC-03, EXIG-MCP-04, EXIG-MCP-19, EXIG-AUT-19 |
| DEC-003 | Couche sémantique gouvernée neutre et médiation sectorielle | AE↔AS | EXIG-INT-02, EXIG-INT-12, EXIG-ARC-14, EXIG-ARC-15 |
| DEC-004 | Parcimonie mémorielle, bi-temporalité auditable et purge Loi 25 | AE↔AS | EXIG-ARC-22, EXIG-ARC-23, EXIG-ARC-25, EXIG-CON-10 |
| DEC-005 | Exécution durable neutre, Saga pivot et sobriété événementielle | AS | EXIG-ORC-11, EXIG-ORC-15, EXIG-ORC-21, EXIG-ORC-28 |
| DEC-006 | Plan d’inférence neutre, routage frugal et continuité bimodèle | AE↔AS | EXIG-ARC-08, EXIG-ARC-09, EXIG-FIN-06, EXIG-ORC-27 |
| DEC-007 | Fédération par noyau possédé et cloisonnement inter-entités | AE | EXIG-ARC-01, EXIG-ARC-19, EXIG-ARC-21, EXIG-CON-11 |
| DEC-008 | Adaptateurs décimaux exacts, extinction CUA et quotas déconnectés | AE↔AS | EXIG-ARC-14, EXIG-ARC-17, EXIG-AUT-08, EXIG-ORC-27 |
| DEC-009 | Politiques hors modèle, bac à sable fermé, épinglage | AS | EXIG-IAM-21, EXIG-MCP-20, EXIG-SEC-06, EXIG-SEC-08 |
| DEC-010 | Qualification multi-essais, quarantaine amont et SRE sans interpréteur libre | AS | EXIG-EVA-02, EXIG-EVA-03, EXIG-ORC-20, EXIG-SEC-17 |
| DEC-011 | Pilotage séquencé au coût par résultat conforme | AE | EXIG-FIN-01, EXIG-FIN-04, EXIG-FIN-09, EXIG-FIN-10 |
| DEC-012 | Continuité post-quantique des mandats et fédération B2B vérifiable | AE↔AS | EXIG-INT-22, EXIG-OBS-12, EXIG-OBS-13, EXIG-APP-14 |

```
id: DEC-NNN  # Fiche exécutable sans produit ni seuil fictif (dérivée C27 Ann. F.4)
proprietaire: AE | AS | AE-AS
abb_cible: <bloc neutre>  # SBB substituable consigné séparément avec date
exigences_cad26: [EXIG-XXX-NN]
portes_et_signaux: {porte: POR-NNN, signal_revision: SIG-NNN}
preuve_ci: <test E1/E2 ou invariant passerelle vérifiable>
```
