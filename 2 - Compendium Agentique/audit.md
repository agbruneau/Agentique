# Audit de couverture et de conformité — Compendium « La somme agentique » (Vol. IV)

| Champ | Valeur |
|---|---|
| **Objet** | Audit de couverture thématique, méthodologique, technique et réglementaire du Compendium Vol. IV (*La somme agentique*) |
| **Périmètre audité** | [`README.md`](README.md) (Conspectus v0.14), [`PRD.md`](PRD/PRD.md) (Gouvernance v0.2), [`TOC.md`](PRD/TOC.md) (Spécification v0.14, 57 chapitres, 10 livres) |
| **Date** | 24 juillet 2026 |
| **Statut** | **Audit complété — Adéquation globale confirmée avec 4 axes d'amélioration critiques** |

---

## 1. Synthèse exécutive & Verdict global

L'analyse du contenu du compendium *La somme agentique* confirme que **la couverture globale du sujet est extrêmement adéquate, rigoureuse et novatrice**. L'ouvrage réussit l'unification complexe de quatre sous-domaines généralement traités de manière isolée dans la littérature :

$$\text{Architecture Agentique} = \text{Coopérer (Protocoles)} + \text{Encadrer (Conformité/Droit)} + \text{Faire confiance (Identité/PQC)} + \text{Livrer (Artefacts/Ops)}$$

### Verdict par dimension

| Dimension | Évaluation | Constat |
|---|---|---|
| **Périmètre fonctionnel & technique** | **Très élevé** | Couverture complète des piles émergentes (`MCP`, `A2A`, `AP2`, `AGNTCY`, `AgentMesh`, OpenTelemetry GenAI). |
| **Ancrage réglementaire financier** | **Excellente (Centré CA)** | Traitement ultra-précis des exigences BSIF/OSFI E-23, Loi 25 (art. 12.1), AMF Québec, et des rails bancaires Lynx / RTR. |
| **Discipline épistémique & Preuve** | **Exemplaire** | Tri strict `PROGRAMMÉ`/`PROJETÉ`/`SPÉCULATIF`, niveaux $[A]/[B]/[C]$, traçabilité continue des faits datés $F\text{-}xx$. |
| **Consensus & Systèmes distribués** | **Insuffisant** | Absence totale de théorisation du consensus asynchrone (0 occurrence du terme dans le plan) et de la résilience aux pannes byzantines. |
| **Couverture d'exécution (*Harnais*)** | **Angle mort déclaré** | Le harnais d'exécution (runtime, boucle perception-action, compression contextuelle) est hors périmètre (Risque 14). |

---

## 2. Évaluation détaillée des 4 Piliers d'Ingénierie

### 1. Plan « Coopérer » — Protocoles et Interopérabilité (Livres I, II, VII)
- **Forces** : Distinction doctrinale claire entre *« MCP dans les agents »* (agent-outil) et *« A2A entre les agents »* (agent-agent). Traitement poussé des registres et de la découverte.
- **Faiblesses** : Sensibilité aiguë à l'horloge de péremption (ex. ratification MCP 2026-07-28).

### 2. Plan « Encadrer » — Autonomie sous contrôle déterministe (Livres IV, V, VI)
- **Forces** : Modélisation continue $OO1 \rightarrow OO4$ permettant de graduer l'autonomie agentique. Traduction déterministe des exigences BSIF/OSFI E-23 en *frames* normatifs d'architecture ([Chapitre 33](PRD/TOC.md#L229)).
- **Faiblesses** : Prédominance du cadre canadien. Les cadres européens (DORA, NIS2) et américains (SEC, FINRA, OCC) sont abordés à haut niveau au [Chapitre 34](PRD/TOC.md#L235) mais mériteraient une profondeur équivalente.

### 3. Plan « Faire confiance » — Identité, Délégation et PQC (Livres III, VII)
- **Forces** : La **Grille des 5 questions** ([Chapitre 15](PRD/TOC.md#L195)) fournit une matrice robuste d'évaluation de l'identité non humaine. Intégration novatrice de l'horloge post-quantique (NIST IR 8547 / crypto-agilité) aux architectures conçues aujourd'hui.
- **Faiblesses** : Les Livres III et VII reposent sur une source (*Vol. III*) qualifiée de *« rédigée mais non publiable »* (dette de vote sur F-92/F-96 et 15 remontées ouvertes).

### 4. Plan « Livrer » — Artefacts logiciels & AgentOps (Livre IX)
- **Forces** : Traitement novateur de l'agent comme artefact logiciel non reproductible ($A\text{-}BOM$, versionnement à 4 horloges, sémantique d'effet et réconciliation financière ISO 20022).
- **Faiblesses** : Matière neuve sans aucun socle factuel hérité (Risque 13).

---

## 3. Axe d'amélioration majeur : Consensus Asynchrone & Résilience Multi-Agents

> [!WARNING]
> **Lacune doctrinale majeure identifiée** : Le compendium modélise les communications d'agents via A2A et AgentMesh, mais omet la théorie des **systèmes distribués sous asynchronie et défaillances byzantines**.

Dans des réseaux bancaires multi-établissements, les agents subissent des pannes de réseau (délais asynchrones, partitions) et des pannes byzantines (agents compromis par injection ou dérive). Le compendium doit intégrer :

```
[Agent Banque A] <--- A2A (Asynchrone/Partitions) ---> [Agent Banque B]
       |                                                      |
       +---> [Agent Validateur / Quorum Byzantine (BFT)] <----+
```

### Feuille de route d'enrichissement recommandée dans le TOC v0.14

1. **Livre I — [Chapitre 6](PRD/TOC.md#L133) (*Systèmes multi-agents*)** :
   - *Ajout requis* : Intégration d'une section sur la **Théorie des systèmes distribués appliquée aux LLM** (Impossibilité FLP, théorème PACELC agentique, quorums de décision sous synchronie partielle).
2. **Livre III — [Chapitres 20-21](PRD/TOC.md#L235) (*Versant hostile & Usurpation*)** :
   - *Ajout requis* : Intégration de la **Tolérance aux Fautes Byzantines (BFT agentique)** pour empêcher un agent corrompu (*Rug-pull*) de valider un état partagé.
3. **Livre VII — [Chapitres 41-42](PRD/TOC.md#L250) (*AgentMesh*)** :
   - *Ajout requis* : Définition de la gestion des **partitions réseau, du split-brain et de la réconciliation** au niveau du plan de contrôle (*Control Plane*).
4. **Livre IX — [Chapitre 54](PRD/TOC.md#L280) (*Sémantique d'effet*)** :
   - *Ajout requis* : Élargissement de l'idempotence individuelle au **consensus de transaction multi-agents (Sagas distribuées 2PC)**.

---

## 4. Matrice des Risques d'Exécution Éditoriale (PRD.md)

| Risque | Description | Gravité | Action / Parade |
|---|---|---|---|
| **Risque 14** | Angle mort de la couche d'exécution (*Le Harnais*) | **Moyenne** | Déclaré en v0.10. Recommandé : Arbitrer en porte G-5 si des sous-sections dédiées doivent entrer au Livre VII/IX. |
| **Risque 13** | Livre IX sans aucun socle hérité ($F\text{-}xx$) | **Élevée** | Constituer un socle propre depuis des sources primaires (G-6) sous peine de retrait du livre. |
| **Risque 11** | Source Vol. III rédigée mais « non publiable » | **Moyenne** | Effectuer la collation de fond (G-4) avant toute fusion des Livres III et VII. |
| **Risque 5** | Péremption des protocoles en cours de route (MCP 2026-07-28) | **Élevée** | Réaligner le Livre II lors du gel unique (Porte G-1). |

---

## 5. Recommandations prioritaires pour le lancement (Portes G-1 à G-7)

1. **Déclencher la Porte G-1 (Gel unique & Re-datation)** : Fixer la date de gel unique $D\text{-}1$ pour stabiliser l'état des spécifications (`MCP`, `A2A`, NIST IR 8547).
2. **Déclencher la Porte G-3 (Refonte du socle consolidé)** : Unifier les socles $F\text{-}xx$ du Vol. II et du Vol. III sous une numérotation unique et valider `check-compendium.py`.
3. **Mener la collation de fond (Porte G-4)** : Confronter les thèses des Livres III et VII au texte rédigé des 34 pièces du Vol. III.
4. **Intégrer le Consensus Asynchrone** : Appliquer les sous-sections recommandées au §3 dans le [`TOC.md`](PRD/TOC.md) avant l'ouverture de la rédaction.

---
*Fin du document d'audit — Généré le 24 juillet 2026.*
