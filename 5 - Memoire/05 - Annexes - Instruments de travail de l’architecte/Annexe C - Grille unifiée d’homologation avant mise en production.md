# Annexe C — Grille unifiée d’homologation avant mise en production

Générée automatiquement depuis `registre/homologation.json` (fusion `CAD26 Annexe A` × `75 PRR C27` × `15 POR PD28`).

## C.1 Contrôles unifiés par domaine (A.2 à A.8)

**Légende et raccordements —** Chaque code PRR suivi d’un astérisque (\*) est [BLOQUANT] sans dérogation en autonomie L3/L4 (24/75 en C27 Annexe G recalibrée W1.3 ; 26 Conditionnel ; 25 Élevée/Moyenne). La grille couvre l’ensemble des 305 exigences de CRE-IA-2026-01 v1.2 (287 socle + 12 EXIG-AMF + 6 PQC/ACVM/RTR/EN 18286). La colonne Statut recense les 46 exigences DOIT / NE DOIT PAS non dérogeables de CAD26 Annexe A, réconciliées à zéro écart avec les 10 interdictions EXIG-GOV-17 (C.2), hors 16 recommandations DEVRAIT isolées dans exigences_devrait et hors EXIG-GOV-16.

| Rubrique | Contrôle d’homologation | Exigences (`EXIG-*`) | Codes `PRR` | Statut (`GOV-17` / `L3-L4`) | Preuve système | Portes |
| --- | --- | --- | --- | --- | --- | --- |
| A.2.1 | Fiche registre et parrain actif | EXIG-GOV-01, EXIG-GOV-05, EXIG-GOV-06, EXIG-GOV-07, EXIG-GOV-08, EXIG-GOV-09, EXIG-GOV-10, EXIG-GOV-11, EXIG-GOV-13, EXIG-GOV-14 | G-01\* | GOV-17 ND (9/10 ; hors DEVRAIT : GOV-06) · [BLOQUANT] (1/1) | Fiche signée, lien RH, rejet réseau | POR-001, POR-015 |
| A.2.2 | Séparation des fonctions et RACI | EXIG-GOV-02, EXIG-GOV-03, EXIG-GOV-04 | S-15\*, F-11 | GOV-17 ND : GOV-02, GOV-04 · Mixte (1/2 [BLOQUANT]) | Protection dépôt, charte un seul A | POR-003, POR-015 |
| A.2.3 | Classe de risque et plafonds | EXIG-CON-01, EXIG-CON-02, EXIG-AUT-01, EXIG-AUT-02, EXIG-AUT-03, EXIG-AUT-06, EXIG-AUT-07 | G-03\*, G-04 | GOV-17 ND : CON-02, AUT-01, AUT-02, AUT-03, AUT-07 · Mixte (1/2 [BLOQUANT]) | Cote E-23 validée, blocage technique NX | POR-001, POR-014 |
| A.2.4 | Domaine ODD et sobriété topologique | EXIG-AUT-04, EXIG-AUT-05, EXIG-ORC-01, EXIG-ORC-02, EXIG-ORC-03 | G-02 | Standard | Contrat ODD borné, gain multiagent mesuré | POR-003, POR-006 |
| A.2.5 | Réévaluation, dérogations et catalogue | EXIG-GOV-12, EXIG-GOV-15, EXIG-GOV-16, EXIG-GOV-17, EXIG-GOV-18, EXIG-GOV-19, EXIG-GOV-20, EXIG-CON-03 | O-03 | GOV-17 ND : GOV-15 (méta-règle GOV-17 ; GOV-16 transitoire) | Manifeste SemVer, dérogations bornées et revues | POR-001, POR-015 |
| A.2.6 | Qualification SaaS et prérequis achat | EXIG-ARC-21, EXIG-APP-01, EXIG-APP-02, EXIG-APP-03, EXIG-APP-04, EXIG-APP-05, EXIG-APP-06 | R-12 | Standard | Régime SaaS (erratum ARC-02 → ARC-21), arrêt propre | POR-004, POR-008 |
| A.3.1 | Sémantique et contrats du catalogue | EXIG-INT-01, EXIG-INT-02, EXIG-INT-03, EXIG-INT-04, EXIG-INT-05, EXIG-INT-06, EXIG-INT-07, EXIG-INT-08, EXIG-INT-09, EXIG-INT-10, EXIG-INT-11 | G-09, F-13 | DEVRAIT : INT-05, INT-11 | Schémas versionnés (G-09 écarté par DEC-003), sas WAP | POR-005 |
| A.3.2 | Épinglage, coexistence et paiements tiers | EXIG-INT-12, EXIG-INT-13, EXIG-INT-14, EXIG-INT-15, EXIG-INT-16, EXIG-INT-17, EXIG-INT-18, EXIG-INT-19, EXIG-INT-20, EXIG-INT-21, EXIG-INT-22, EXIG-INT-23 | G-13, F-01, F-03 | Standard | Verrouillage SHA-256 et rapprochement tripartite | POR-001, POR-013 |
| A.3.3 | Serveurs MCP sans état sécurisés | EXIG-MCP-01, EXIG-MCP-02, EXIG-MCP-03, EXIG-MCP-04, EXIG-MCP-08, EXIG-MCP-09, EXIG-MCP-10, EXIG-MCP-12, EXIG-MCP-13, EXIG-MCP-22 | R-09 | Standard | Transport HTTP sans état, sessions bornées | POR-001, POR-008 |
| A.3.4 | Intention métier et hygiène MCP | EXIG-MCP-05, EXIG-MCP-06, EXIG-MCP-07, EXIG-MCP-14, EXIG-MCP-15, EXIG-MCP-16, EXIG-MCP-17, EXIG-MCP-18, EXIG-MCP-19, EXIG-MCP-20, EXIG-MCP-21 | S-07 | DEVRAIT : MCP-05 | Empreintes signées, alerte substitution schéma | POR-001 |
| A.3.5 | Cartes signées et tâches A2A | EXIG-A2A-01, EXIG-A2A-02, EXIG-A2A-03, EXIG-A2A-04, EXIG-A2A-05, EXIG-A2A-06, EXIG-A2A-07, EXIG-A2A-08, EXIG-A2A-09, EXIG-A2A-10, EXIG-A2A-11, EXIG-A2A-12, EXIG-A2A-13, EXIG-A2A-14, EXIG-A2A-15 | S-13, F-02, G-14 | DEVRAIT : A2A-15 | Vérification JWS, mTLS, isolation diplomate externe | POR-006, POR-013 |
| A.3.6 | Bus CloudEvents et anti-boucle | EXIG-EVT-01, EXIG-EVT-02, EXIG-EVT-03, EXIG-EVT-04, EXIG-EVT-05, EXIG-EVT-06, EXIG-EVT-07, EXIG-EVT-08, EXIG-EVT-09, EXIG-EVT-10 | R-04, R-05 | DEVRAIT : EVT-01 | Arrêt compteur sauts et rejeu isolé | POR-006 |
| A.4.1 | Couches et interfaces métier validantes | EXIG-ARC-02, EXIG-ARC-03, EXIG-ARC-04, EXIG-ARC-07, EXIG-ARC-13, EXIG-ARC-14, EXIG-ARC-15, EXIG-ARC-16, EXIG-ARC-17, EXIG-ARC-18, EXIG-ARC-19, EXIG-ARC-20 | R-01\*, R-13, F-12 | DEVRAIT : ARC-15, ARC-18 · Mixte (1/3 [BLOQUANT]) | Zéro SQL, miroir [S], sas OT | POR-004, POR-008 |
| A.4.2 | Exécution durable et reprise d’état | EXIG-ARC-05, EXIG-ARC-06, EXIG-ORC-11, EXIG-ORC-12, EXIG-ORC-13, EXIG-ORC-14 | R-02, O-08 | DEVRAIT : ORC-14 | Reprise panne, retour arrière 2 min [S] (O-08) | POR-003 |
| A.4.3 | Clés d’idempotence et pré-engagement | EXIG-ORC-21, EXIG-ORC-22 | R-03\*, R-07\* | [BLOQUANT] (2/2) | Double envoi dédupliqué et tampon actif | POR-003 |
| A.4.4 | Sagas, compensations et injection fautes | EXIG-ORC-15, EXIG-ORC-16, EXIG-ORC-17, EXIG-ORC-18, EXIG-ORC-19, EXIG-ORC-20 | R-06\*, R-15 | Mixte (1/2 [BLOQUANT]) | Journal préalable, chaos sans écriture orpheline | POR-003 |
| A.4.5 | Gouvernance des patrons multiagents | EXIG-ORC-04, EXIG-ORC-05, EXIG-ORC-06, EXIG-ORC-07, EXIG-ORC-08, EXIG-ORC-09, EXIG-ORC-10, EXIG-ORC-23, EXIG-ORC-24, EXIG-ORC-25, EXIG-ORC-29, EXIG-ORC-30 | O-06 | DEVRAIT : ORC-10 | Blocage troisième saut, coupure boucle sémantique | POR-006 |
| A.4.6 | Plafonds, repli bimodèle et coupe-circuit | EXIG-ORC-26, EXIG-ORC-27, EXIG-ORC-28, EXIG-IAM-20, EXIG-SEC-26 | S-14\*, R-10, R-11, F-07, F-08, F-09 | Mixte (1/6 [BLOQUANT]) | Arrêt < 10 s [S] (15 min CAD26), canal dédié | POR-003, POR-006, POR-015 |
| A.5.1 | Paliers d’outils et union stricte | EXIG-AUT-08, EXIG-AUT-10, EXIG-AUT-11 | S-09\* | [BLOQUANT] (1/1) | Évaluation déterministe hors modèle mode fermé | POR-001, POR-003 |
| A.5.2 | Approbation hors bande liée P3 | EXIG-AUT-09, EXIG-AUT-12, EXIG-AUT-13, EXIG-AUT-14 | S-10 | GOV-17 ND (3/4 ; hors DEVRAIT : AUT-14) | Jeton CIBA/FIDO2 lié au condensat JCS | POR-003 |
| A.5.3 | Ergonomie fidèle et vigilance humaine | EXIG-AUT-15, EXIG-AUT-16, EXIG-AUT-19, EXIG-AUT-20, EXIG-AUT-21 | G-11, G-12 | Standard | Écran I-JSON différentiel et dossiers témoins | POR-009, POR-014 |
| A.5.4 | Agents ambiants et persistance pré-effet | EXIG-AUT-17, EXIG-AUT-18 | R-08 | Standard | Revalidation au réveil, réautorisation périodique | POR-015 |
| A.5.5 | Décisions automatisées Loi 25 | EXIG-AUT-22, EXIG-AUT-23, EXIG-CON-07, EXIG-CON-08, EXIG-CON-09 | G-06\* | GOV-17 ND (5/5) · [BLOQUANT] (1/1) | Avis, facteurs explicables, dossier 1 an | POR-002, POR-014 |
| A.6.1 | Identité NHI sans secret statique | EXIG-IAM-01, EXIG-IAM-02, EXIG-IAM-03, EXIG-IAM-04, EXIG-IAM-05, EXIG-IAM-06, EXIG-IAM-07 | S-01\* | [BLOQUANT] (1/1) | Attestation SPIFFE SVID, zéro clé statique | POR-001, POR-011 |
| A.6.2 | Échange RFC 8693 sans relais | EXIG-IAM-08, EXIG-IAM-09, EXIG-IAM-10, EXIG-IAM-11, EXIG-IAM-12, EXIG-MCP-11 | S-03\*, S-04 | GOV-17 ND : IAM-08, IAM-09, IAM-12, MCP-11 · Mixte (1/2 [BLOQUANT]) | Jeton audience unique, rejet tout relais | POR-001, POR-011 |
| A.6.3 | Profil OAuth et liaison expéditeur | EXIG-IAM-13, EXIG-IAM-14, EXIG-IAM-15, EXIG-IAM-16 | S-05 | DEVRAIT : IAM-15 | Jeton court DPoP/mTLS, renouvellement 47 j | POR-007, POR-011 |
| A.6.4 | Coupure passerelles d’agents et modèles | EXIG-ARC-01, EXIG-ARC-08, EXIG-ARC-09, EXIG-ARC-11, EXIG-ARC-12, EXIG-IAM-17, EXIG-IAM-18, EXIG-IAM-19, EXIG-IAM-21 | S-06\*, F-14\* | DEVRAIT : ARC-09, IAM-19 · [BLOQUANT] (2/2) | Blocage réseau hors passerelle, zéro interpréteur | POR-001, POR-012 |
| A.6.5 | Règle de deux anti-exfiltration | EXIG-SEC-01, EXIG-SEC-02, EXIG-SEC-03, EXIG-SEC-04, EXIG-SEC-05, EXIG-SEC-06, EXIG-SEC-07 | S-08\* | GOV-17 ND : SEC-06 · [BLOQUANT] (1/1) | Retrait déterministe outils sortants et P3 | POR-003 |
| A.6.6 | Bac à sable réseau fermé | EXIG-ARC-10, EXIG-SEC-08, EXIG-SEC-09, EXIG-SEC-10, EXIG-SEC-11, EXIG-SEC-12, EXIG-SEC-13, EXIG-SEC-14, EXIG-SEC-15, EXIG-SEC-16, EXIG-SEC-17 | S-11\* | DEVRAIT : SEC-11 · [BLOQUANT] (1/1) | Sortie réseau/IMDS bloquée, isolation IOMMU/microVM | POR-003 |
| A.6.7 | Provenance signée et tests adverses | EXIG-SEC-18, EXIG-SEC-19, EXIG-SEC-20, EXIG-SEC-21, EXIG-SEC-22, EXIG-SEC-23, EXIG-SEC-24, EXIG-SEC-25 | S-02, F-10 | Standard | Signatures artefacts vérifiées, suite attaques CI | POR-003, POR-007 |
| A.6.8 | Agilité cryptographique et transition post-quantique (NIST IR 8547) | EXIG-SEC-27, EXIG-SEC-28 | S-14 | Standard | Inventaire crypto, TLS ≤ 47 j, signatures PQC/rescellement ≤ 5 ans, en-têtes ≤ 8 Ko | POR-002, POR-007 |
| A.7.1 | Traces OpenTelemetry épinglées au collecteur | EXIG-OBS-01, EXIG-OBS-02, EXIG-OBS-03, EXIG-OBS-04, EXIG-OBS-05, EXIG-OBS-06 | O-01 | Standard | Trace causale complète normalisée au collecteur | POR-002 |
| A.7.2 | Double couloir RP (PII) sans contenu | EXIG-OBS-07, EXIG-OBS-08, EXIG-OBS-09, EXIG-OBS-10 | O-02\*, F-15 | Mixte (1/2 [BLOQUANT]) | Zéro renseignement personnel (RP) index général, canaris [S] | POR-002 |
| A.7.3 | Journal d’audit JCS chaîné ancré | EXIG-OBS-11, EXIG-OBS-12, EXIG-OBS-13 | G-15\* | GOV-17 ND : OBS-11 · [BLOQUANT] (1/1) | Audit 5 éléments, ancrage horaire, PQC | POR-002, POR-007, POR-011 |
| A.7.4 | Évaluation E1–E3 pass^k et dérive | EXIG-EVA-01, EXIG-EVA-02, EXIG-EVA-03, EXIG-EVA-04, EXIG-EVA-05, EXIG-EVA-06 | O-04, O-05, O-07, O-14 | Standard | CI pass^k (≥ 50 EXIG-EVA-02 vs ≥ 100 PRR O-04 [S]) | POR-003, POR-014, POR-015 |
| A.7.5 | Enveloppes FinOps, CPO et carbone | EXIG-FIN-01, EXIG-FIN-02, EXIG-FIN-03, EXIG-FIN-04, EXIG-FIN-05, EXIG-FIN-06, EXIG-FIN-07, EXIG-FIN-08, EXIG-FIN-09, EXIG-FIN-10 | O-09\*, O-10, O-11, O-12, O-13 | DEVRAIT : FIN-08 · Mixte (1/5 [BLOQUANT]) | Disjoncteur coût, tableau CPO, portée 3 | POR-004, POR-009, POR-016 |
| A.8.1 | ÉFVP préalable et finalités vérifiées | EXIG-CON-04, EXIG-CON-06 | G-05\* | GOV-17 ND (2/2) · [BLOQUANT] (1/1) | Dossier ÉFVP signé, consentement par entité | POR-002, POR-012 |
| A.8.2 | Six substrats d’état et clés | EXIG-CON-05 | F-04\*, F-05, F-06 | GOV-17 ND (1/1) · Mixte (1/3 [BLOQUANT]) | Matrice 6 substrats [S], clés souveraines, enclave | POR-002 |
| A.8.3 | Isolation CoALA et effacement vérifiable | EXIG-ARC-22, EXIG-ARC-23, EXIG-ARC-24, EXIG-ARC-25, EXIG-CON-10 | S-12, R-14\*, G-10\* | Mixte (2/3 [BLOQUANT]) | Étanchéité multilocataire et preuve de purge | POR-005 |
| A.8.4 | Conformité multi-régimes E-23, AMF, RIA | EXIG-CON-11, EXIG-CON-12, EXIG-CON-13, EXIG-CON-14, EXIG-CON-15, EXIG-CON-16, EXIG-CON-17, EXIG-CON-18, EXIG-CON-21 | G-08 | GOV-17 ND (9/9) | Base de preuves unique, dossier RIA | POR-002, POR-012 |
| A.8.5 | Transparence, incidents et impact unifié | EXIG-CON-19, EXIG-CON-20, EXIG-CON-22, EXIG-CON-23, EXIG-CON-24, EXIG-CON-25, EXIG-CON-26 | G-07\* | GOV-17 ND : CON-19, CON-20, CON-22 (art. 50 RIA ; légal CON-24..26 § A.1.3) · [BLOQUANT] (1/1) | Divulgation active, impact unifié, gel preuves | POR-002 |
| A.8.6 | Dix clauses contractuelles et sortie | EXIG-APP-07, EXIG-APP-08, EXIG-APP-09, EXIG-APP-10, EXIG-APP-11, EXIG-APP-12, EXIG-APP-13, EXIG-APP-14, EXIG-APP-15, EXIG-APP-16, EXIG-APP-17 | O-15 | Standard | Grille fournisseur signée, essai annuel d’extraction | POR-004, POR-016 |
| A.8.7 | Secteurs financiers ACVM 11-348, RTR ISO 20022, EN 18286 et AMF | EXIG-CON-27, EXIG-CON-28, EXIG-CON-29, EXIG-CON-30, EXIG-AMF-01, EXIG-AMF-02, EXIG-AMF-03, EXIG-AMF-04, EXIG-AMF-05, EXIG-AMF-06, EXIG-AMF-07, EXIG-AMF-08, EXIG-AMF-09, EXIG-AMF-10, EXIG-AMF-11, EXIG-AMF-12 | G-15 | Standard | Dossiers ACVM 7 ans, tampon RTR pacs.008, SMQ EN 18286 et répertoire AMF | POR-004, POR-009 |

## C.2 Dix interdictions sans dérogation (`EXIG-GOV-17`) et protocole d’exception

Dérogation écrite bornée à ≤ 6 mois (renouvelable 1 fois ; ≤ 90 j en classe faible par l’AE) sous mesures compensatoires ; zéro dérogation sur les 10 interdictions EXIG-GOV-17.

1. **Autonomie non bornée de niveau NX interdite en tout temps** (EXIG-AUT-03).
2. **Exécution d’une action P3 sans approbation humaine hors bande liée** (EXIG-AUT-09, EXIG-AUT-12, EXIG-AUT-13).
3. **Usurpation par un agent de l’identité de son mandant humain** (EXIG-IAM-08, EXIG-IAM-09).
4. **Relais direct d’un jeton entrant vers un serveur ou pair aval** (EXIG-IAM-12, EXIG-MCP-11).
5. **Exploitation sans fiche complète au registre ou parrain nommé (hors cohorte transitoire EXIG-GOV-16)** (EXIG-GOV-01, EXIG-GOV-02, EXIG-GOV-04, EXIG-GOV-05, EXIG-GOV-07, EXIG-GOV-08, EXIG-GOV-09, EXIG-GOV-10, EXIG-GOV-11, EXIG-GOV-13, EXIG-GOV-14, EXIG-GOV-15).
6. **Dépassement du plafond d’autonomie fixé par la classe de risque** (EXIG-AUT-01, EXIG-AUT-02, EXIG-CON-02).
7. **Autorisation au-delà de N2 d’un agent atteignant les seuils de la règle d’or** (EXIG-AUT-07).
8. **Exposition à la triade létale sans retrait déterministe des outils sortants** (EXIG-SEC-06).
9. **Exploitation d’un agent sans journal d’audit distinct, chaîné et ancré** (EXIG-OBS-11).
10. **Manquement à une obligation légale ou réglementaire applicable (dont Loi 25 art. 12.1 et part légale CON-10, 24..26 § A.1.3)** (EXIG-AUT-22, EXIG-AUT-23, EXIG-CON-04, EXIG-CON-05, EXIG-CON-06, EXIG-CON-07, EXIG-CON-08, EXIG-CON-09, EXIG-CON-11, EXIG-CON-12, EXIG-CON-13, EXIG-CON-14, EXIG-CON-15, EXIG-CON-16, EXIG-CON-17, EXIG-CON-18, EXIG-CON-19, EXIG-CON-20, EXIG-CON-21, EXIG-CON-22).
