# Rapport de revalidation — 16 juillet 2026

| Champ | Valeur |
|---|---|
| Jalon | PRDPlan P0.1 (revalidation temporelle initiale) et P0.2 (élévations [C]→[B] prioritaires) |
| Méthode | 9 recherches ciblées par agents parallèles, WebSearch/WebFetch sur sources primaires, sans vote adversarial (hors budget P0 — « meilleur effort borné », une passe par lacune, PRDPlan §2) |
| PRD amendé | Oui — v1.2.1 → v1.3 |

---

## P0.1 — Revalidation temporelle des faits « chauds » (PRD §8.3)

| # | Fait chaud | Verdict | Détail | Source primaire |
|---|---|---|---|---|
| 1 | RTR — cible de lancement | **INCHANGÉ** | Toujours T4 2026 ; « industry solution assurance testing » en cours (confirmé) ; By-law No. 10 publié le 1er juillet 2026 (Gazette partie II), entrée en vigueur inchangée au 24 août 2026. **Ajout mineur** : la page officielle des partenaires de livraison liste désormais **Deloitte Canada** comme 4e partenaire (rôle non précisé), en plus d'IBM Canada, CGI et Interac. | payments.ca (page RTR + page « delivery partners » + billet du 30 juin 2026) |
| 2 | Règlement du cadre bancaire — commentaires / désignation | **INCHANGÉ** | Période de commentaires toujours fixée au 26 août 2026, aucun amendement recensé. **Aucun arrêté ministériel de désignation de l'organisme de normalisation technique publié à ce jour** — question ouverte PRD §10.1 non résolue. Aucune mention officielle de FDX/FAPI/OAuth dans le texte réglementaire ou les pages Banque du Canada. | gazette.gc.ca (Partie I, vol. 160, no 26) ; bankofcanada.ca |
| 3 | Clôture de l'acquisition Confluent par IBM | **ÉVOLUÉ** | **Clôturée le 17 mars 2026** (annonce préalable : 8 déc. 2025 → expiration HSR 12 janv. 2026 → approbation actionnaires 12 févr. 2026 → clôture 17 mars 2026). PRD F-41 amendé : réserve « clôture non confirmée » levée, niveau de preuve porté à [B]. | newsroom.ibm.com (« IBM Completes Acquisition of Confluent... ») |
| 4 | Trajectoire C-36 | **ÉVOLUÉ (caractérisation corrigée)** | Le projet de loi existe bien (parrainé par Evan Solomon, 1re lecture le 15 juin 2026, 2e lecture au 16 juillet 2026) mais **n'est pas une loi IA autonome** : titre officiel *Protecting Privacy and Consumer Data Act* (PPCDA), réforme de la LPRPDE créant la Digital Safety and Data Protection Commission of Canada. Les trois volets déjà cités au PRD (droit à l'effacement, données des enfants, transparence IA) sont confirmés, mais comme composantes d'une loi sur la vie privée, pas d'une loi IA dédiée. Le vide réglementaire IA fédéral est confirmé et renforcé par des sources additionnelles (« Canada remains the only G7 nation without a binding AI regulatory framework » — AIMag). PRD F-24 réécrit en conséquence. | parl.ca/LEGISinfo (45-1/c-36) ; Fasken, DLA Piper, Canadian Lawyer Magazine (juin 2026) |
| 5 | Versions MCP / A2A | **ÉVOLUÉ (MCP) / INCHANGÉ (A2A)** | **MCP** : révision de spécification courante = **2025-11-25** (le PRD citait 2025-06-18) ; une *release candidate* majeure (refonte sans état, retrait de `Mcp-Session-Id`) est verrouillée pour finalisation le **28 juillet 2026** — fait chaud à re-surveiller en P4.1. Gouvernance AAIF/Linux Foundation inchangée. **A2A** : toujours en ligne v1.0 (tag v1.0.1, correctifs mineurs, 28 mai 2026) ; 150+ organisations (aucun décompte plus récent public) ; TSC inchangé. PRD F-01 amendé ; F-02 confirmé sans changement matériel. | modelcontextprotocol.io/specification/2025-11-25 ; blog.modelcontextprotocol.io (RC 2026-07-28) ; github.com/a2aproject/A2A/releases ; linuxfoundation.org |

**Aucune revalidation nécessaire au-delà de ce qui précède** — tous les autres éléments de §8.3 (Loi 25, Lynx, AIDox) sont hors périmètre de cette passe (déjà stables, non listés comme « chauds » pour cette itération).

---

## P0.2 — Élévations [C] → [B] prioritaires (PRD §10)

| # | Lacune ciblée | Verdict | Détail | Statut PRD |
|---|---|---|---|---|
| 1 | BMO (rapport annuel 2025 — Lumi, bootcamps, risque matériel) | **ÉLEVÉ PARTIELLEMENT** | Lumi confirmé [B] par communiqué BMO recoupé (4 miroirs) avec citation directe ; correction factuelle au passage — le chiffre « 8 000 » qualifie des employés utilisateurs (source Qorus/Infosys awards), pas des politiques, comme le repérage initial le laissait penser. Bootcamps agentiques/multimodaux confirmés [B, attribué] via étude de cas Vector Institute (partenaire IA de BMO, pas BMO directement). **Facteur de risque matériel gen-IA : NON élevé** — PDF bmo.com/ir trop volumineux, dépôts SEC bloqués (403) ; reste [C]. Nouvelle entrée **F-47** créée. | Amendé (§7.5) |
| 2 | Sun Life (agents IA ; consortium « Agentic Control Plane ») | **ÉLEVÉ PARTIELLEMENT** | Communiqué primaire du consortium Lightworks–Scotiabank–Sun Life–TELUS retrouvé et lu intégralement (CNW, 7 juillet 2026) — élevé [B]. **Découverte critique** : cet « ACP » (*Agentic Control Plane*, produit commercial du consortium) est un homonyme sans rapport avec l'ACP protocolaire d'IBM/BeeAI fusionné dans A2A (F-43, R-1) — risque de confusion réel, nouveau garde-fou **R-8** ajouté. Agents IA pour adhésion/relevés fiscaux/réclamations : **NON élevé** — sunlife.com inaccessible aux outils (403), seule source restante The Logic (secondaire, paywall) ; reste [C]. Nouvelle entrée **F-48** créée. | Amendé (§7.5, §8.1) |
| 3 | Support A2A première main — LangChain, CrewAI | **ÉLEVÉ (CrewAI complet, LangChain partiel)** | **CrewAI** : documentation officielle de première main confirmée (`docs.crewai.com/en/learn/a2a-agent-delegation` — « CrewAI treats A2A protocol as a first-class delegation primitive »), historique de changelog daté depuis nov. 2025 — élevé [B]. **LangChain/LangGraph** : confirmé de première main mais **seulement pour LangGraph Platform/LangSmith Deployment** (`docs.langchain.com/langsmith/server-a2a`) — la bibliothèque open source `langgraph` n'a pas de support A2A natif documenté (requête ouverte GitHub #7398, 3 avril 2026) ; élevé [B] avec réserve de périmètre explicite. | Amendé (§7.6, F-32) |
| 4 | Solution FTM/ISO 20022 | **ÉCHEC D'ÉLÉVATION DOCUMENTÉ** | FTM confirmé comme produit IBM actif et documenté (`ibm.com/docs/en/ftmfm`, jusqu'à la version 4.0.8) ; lien MQ↔FTM↔ISO 20022 confirmé par citation directe, mais uniquement via un Redbook de 2016 (même niveau de preuve que l'entrée existante) — aucune page `ibm.com/docs` courante accessible pour une citation non-Redbook (403 systématique). Une source non-Redbook actuelle (« IBM App Connect Enterprise Solution for ISO 20022 Messaging », PDF officiel daté 4 févr. 2025) a été localisée mais ne mentionne pas FTM/MQ nommément — pas de contradiction, mais pas de confirmation croisée. **Conformément à la règle PRDPlan P0.2** (« l'échec d'élévation ne bloque pas P1 »), la lacune reste en §10, enrichie de ces éléments ; relecture humaine recommandée avant publication. | Documenté en §10 (gap inchangé, enrichi) |

---

## Amendements appliqués au PRD (v1.2.1 → v1.3)

- **F-01** (MCP) : révision de spécification mise à jour (2025-06-18 → 2025-11-25) ; RC du 28 juillet 2026 signalée comme fait chaud à resurveiller en P4.1.
- **F-24** (post-C-27/C-36) : caractérisation corrigée (loi sur la protection de la vie privée, pas loi IA autonome) ; élevé [B] par consultation directe LEGISinfo.
- **F-29** (RTR) : ajout de Deloitte Canada comme 4e partenaire de livraison documenté.
- **F-41** (Confluent) : réserve de clôture levée, date de clôture confirmée (17 mars 2026), élevé [B].
- **F-47** (nouveau) : BMO — Lumi et bootcamps élevés [B], facteur de risque matériel reste [C].
- **F-48** (nouveau) : Sun Life / consortium Agentic Control Plane — communiqué primaire élevé [B], agents IA adhésion/fiscal/réclamations restent [C].
- **§7.6** : entrée CrewAI (A2A) élevée [B] ; **F-32** (LangGraph) : ajout du support A2A de LangGraph Platform, élevé [B] avec réserve de périmètre.
- **§8.1** : nouveau garde-fou **R-8** (homonymie des deux « ACP »).
- **§10** : lacunes 2, 3, 6 mises à jour pour refléter les élévations et échecs documentés ci-dessus.
- **Annexe A** : complément méthodologique P0 ajouté.
- **§12** : jalon P0 marqué fait (16 juillet 2026).

## Limites de cette passe

- Pas de vote adversarial 3 juges (hors budget P0 — passe de « meilleur effort », conforme à PRDPlan §2).
- Plusieurs sources bloquées aux outils automatisés (bmo.com/ir PDF volumineux, sec.gov, ibm.com/docs, sunlife.com, a2a-protocol.org — tous 403 ou timeout) ; recoupement par miroirs/GitHub/changelogs utilisé en substitution documentée à chaque fois.
- Une hallucination détectée et écartée en cours de recherche (un résumé de recherche web affirmant l'existence d'un package `langchain-adk 0.3.14` non corroboré par aucune source primaire) — non retenue au PRD.
- Banque Nationale non re-recherchée dans cette passe (hors périmètre P0.2, aucun signal de nouvelle source primaire).
