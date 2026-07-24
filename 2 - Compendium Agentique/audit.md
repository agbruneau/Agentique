# Audit de couverture et de conformité — Compendium « La somme agentique » (Vol. IV)

| Champ | Valeur |
|---|---|
| **Objet** | Audit de couverture thématique, méthodologique, technique et réglementaire du Compendium Vol. IV (*La somme agentique*) |
| **Périmètre audité** | [`README.md`](README.md) (Conspectus), [`PRD.md`](PRD/PRD.md) (Gouvernance), [`TOC.md`](PRD/TOC.md) (Spécification, 57 chapitres, 10 livres) — état v0.14 du plan et v0.2 du PRD au moment de l'audit |
| **Date** | 24 juillet 2026 |
| **Statut** | **Audit complété.** Adéquation globale confirmée ; **un** axe d'amélioration retenu après vérification, trois constats déjà portés par le plan, un écarté |
| **Autorité — aucune** | ⚠ Ce rapport n'est **ni une source, ni un socle, ni une décision**. Il ne modifie aucun livrable : ses constats retenus vivent au [`TOC.md`](PRD/TOC.md) (risque 15) et au [`PRD.md`](PRD/PRD.md) (décision d'auteur D-7), qui seuls font autorité. En cas d'écart, ce sont eux qui priment |
| **Suites données** | TOC **v0.15** (risque 15, journal v0.15) et PRD **v0.3** (décision **D-7**), 24 juillet 2026 |

---

## 1. Synthèse exécutive & Verdict global

L'analyse du contenu du compendium *La somme agentique* confirme que **la couverture globale du sujet est adéquate, rigoureuse et novatrice**. L'ouvrage réussit l'unification de quatre sous-domaines généralement traités isolément : coopérer (protocoles), encadrer (conformité et droit), faire confiance (identité et PQC), livrer (artefacts et exploitation).

### Verdict par dimension

| Dimension | Évaluation | Constat |
|---|---|---|
| **Périmètre fonctionnel & technique** | **Très élevé** | Couverture complète des piles émergentes (`MCP`, `A2A`, `AP2`, `AGNTCY`, `AgentMesh`, OpenTelemetry GenAI). |
| **Ancrage réglementaire financier** | **Excellent (centré Canada)** | Traitement précis des attentes BSIF/OSFI E-23, de la Loi 25 (art. 12.1), de la ligne directrice de l'AMF, et des rails Lynx / RTR. |
| **Discipline épistémique & preuve** | **Exemplaire** | Tri strict PROGRAMMÉ / PROJETÉ / SPÉCULATIF, niveaux [A]/[B]/[C], traçabilité continue des faits datés F-xx. |
| **Accord sous défaillance** | **Insuffisant** | Aucune théorisation de l'accord entre agents sous asynchronie et défaillance partielle (mesure au §3). **Retenu** → risque 15 du TOC, décision D-7. |
| **Couche d'exécution (*harnais*)** | **Angle mort déjà déclaré** | Risque 14 du TOC depuis la v0.10, porte G-5, décision D-2. Rien à ajouter. |

---

## 2. Évaluation détaillée des quatre plans

### 1. « Coopérer » — protocoles et interopérabilité (Livres I, II et premier mouvement du VII)
- **Forces** : distinction doctrinale claire entre « MCP dans les agents » (agent-outil) et « A2A entre les agents » (agent-agent), attribuée au projet A2A et non donnée pour un accord des deux. Traitement poussé des registres et de la découverte.
- **Faiblesses** : sensibilité aiguë à l'horloge de péremption — ratification MCP **annoncée** au 28 juillet 2026.

### 2. « Encadrer » — autonomie sous contrôle déterministe (Livres IV, V, VI)
- **Forces** : continuum OO1→OO4 permettant de graduer l'autonomie ; traduction des attentes E-23 en *frames* normatifs d'architecture (ch. 33, le chapitre-pont).
- **Non retenu — le déséquilibre est un périmètre déclaré, non une lacune** : les cadres européens (DORA, NIS2) et américains (SEC, FINRA, OCC) sont traités à plus haut niveau que le cadre canadien (ch. 34), mais le titre même de l'ouvrage borne son terrain aux services financiers réglementés canadiens. Aucune modification recommandée.

### 3. « Faire confiance » — identité, délégation et PQC (Livres III et second mouvement du VII)
- **Forces** : la **grille des cinq questions** (ch. 15) fournit une matrice d'évaluation de l'identité non humaine ; intégration de l'horloge post-quantique (NIST IR 8547, statut brouillon, jalons **visés**) aux architectures conçues aujourd'hui.
- **Faiblesses** : ces livres reposent sur une source (Vol. III) déclarée « rédigée, non publiable » — 15 remontées ouvertes, dette de vote sur F-92 et F-96. **Déjà porté** : risque 11 du TOC, porte G-4 (volet de fond restant dû).

### 4. « Livrer » — artefacts logiciels & AgentOps (Livre IX)
- **Forces** : traitement de l'agent comme artefact logiciel non reproductible (nomenclatures, versionnement à quatre horloges, sémantique d'effet, réconciliation ISO 20022).
- **Faiblesses** : matière neuve sans aucun socle factuel hérité. **Déjà porté** : risque 13 du TOC, porte G-6, décision D-3 (retrait prévu si le socle ne se constitue pas).

---

## 3. Axe retenu : l'accord entre agents sous défaillance

⚠ **Lacune doctrinale retenue** : le compendium modélise les échanges d'agents via A2A et le maillage, mais n'aborde nulle part l'**accord** — ce que deux agents de deux institutions tiennent pour vrai sous asynchronie, partition réseau, division du plan de contrôle, ou face à un pair vivant qui répond faux.

**Mesure, sur la zone des chapitres** de `PRD/TOC.md` — de `### Chapitre 1` à `# Annexes`, 24 juillet 2026, insensible à la casse :

```bash
sed -n '/^### Chapitre 1 /,/^# Annexes/p' "PRD/TOC.md" | grep -icE "consensus|byzantin|quorum|BFT|split-brain"
```

Résultat : **0**. Le motif `saga` renvoie **une** occurrence dans la même zone — ch. 54, « compensation et sagas au grain de l'agent » —, c'est-à-dire au grain d'une **action unique**, non de l'accord entre pairs ; `idempot` et `réconcili` n'y figurent qu'au même chapitre.

⚠ **La zone, et non le fichier.** Depuis la v0.15, ces termes figurent dans la *déclaration* du plan — bandeau, risque 15, journal — et une mesure sur le fichier entier ne distinguerait plus l'objet décrit de son constat d'absence. C'est le motif pour lequel la commande publiée ici est bornée, et elle a été exécutée sur son domaine entier après édition, non sur un échantillon.

**Ce que le plan couvre déjà, et qu'il ne faut pas confondre avec l'accord** : la communication (Livre II, ch. 41-42), la sûreté du collectif au grain du modèle de menace (ch. 6), les modes d'échec protocolaires (ch. 11), les coûts et points de défaillance du maillage (ch. 42), l'effet à moitié réussi d'une action isolée (ch. 54). L'agent compromis y est traité — mais comme un problème d'**identité** : le *rug-pull* du ch. 21 est une question d'admission et de révocation. Révoquer un porteur ne dit pas ce que le système tient pour vrai pendant la fenêtre où il répondait encore.

### Points d'atterrissage possibles — à arbitrer, non à insérer

⚠ **Ce rapport ne modifie pas le plan.** La règle du volume est explicite : l'ajout de matière est une **décision d'auteur**, non une décision de passe (précédent des risques 13 et 14). Les points d'atterrissage ci-dessous sont proposés à l'arbitrage **D-7** du PRD ; aucun n'est appliqué.

1. **ch. 6** (*Systèmes multi-agents, évaluation et sûreté*) — théorie du collectif sous défaillance : impossibilité FLP, tolérance aux fautes byzantines, CAP et ses raffinements, appliqués au collectif d'agents.
2. **ch. 42** (*Le maillage comme point d'application*) — partition réseau et division du plan de contrôle : ce que devient l'application de politique quand le PDP est injoignable ou divisé.
3. **ch. 54** (*La sémantique d'effet*) — extension de l'existant : les sagas y sont **déjà planifiées** au grain d'une action ; l'ajout porterait sur l'accord entre agents, non sur l'idempotence.

**Économie du choix, différente de celle du risque 14** : la matière est ancienne, primaire et stable — l'objection n'est donc pas le socle (comme pour le harnais), mais le **périmètre** (une théorie des systèmes répartis se rattache-t-elle aux quatre plans ?) et la **volumétrie** (risque 1). Aucun chapitre neuf n'est proposé : la carte des dix livres reste close.

---

## 4. Matrice des risques — lecture du présent rapport

⚠ **Les gravités ci-dessous sont l'appréciation de ce rapport** : le registre du TOC n'ordonne pas ses risques par gravité. Les numéros et les parades, eux, sont ceux du plan.

| Risque | Description | Gravité *(appréciation du rapport)* | Parade au plan |
|---|---|---|---|
| **Risque 15** *(TOC v0.15)* | Accord entre agents sous défaillance — sans lieu dans la somme | **Moyenne** | Déclaré, non comblé ; arbitrage **D-7** avant la rédaction du Livre I |
| **Risque 14** | Angle mort de la couche d'exécution (le harnais) | **Moyenne** | Déclaré en v0.10 ; arbitrage en porte **G-5** (décision D-2) |
| **Risque 13** | Livre IX sans aucun socle hérité (F-xx) | **Élevée** | Socle propre depuis des sources primaires en **G-6**, ou retrait exécuté (D-3) |
| **Risque 11** | Source Vol. III rédigée mais « non publiable » | **Moyenne** | Collation de fond (**G-4**, volet structurel levé par la v0.14) avant fusion des Livres III et VII |
| **Risque 3** | Péremption à trois horloges — trois gels sources non synchrones | **Élevée** | Gel unique et re-datation systématique en porte **G-1** |
| *(PRD §13)* | Péremption **en cours de rédaction** — MCP au 28 juillet 2026, RTR, cadre bancaire | **Élevée** | Événements du ch. 57 surveillés à chaque jalon ; un fait qui bascule se traite au socle d'abord |

*Correction par rapport à la première rédaction de ce rapport : la péremption des protocoles y était donnée comme « risque 5 ». Le risque 5 du TOC porte sur les divergences rouvertes par inadvertance ; la péremption est le risque 3 (trois horloges) et une rangée du §13 du PRD.*

---

## 5. Recommandations prioritaires pour le lancement (portes G-1 à G-7)

1. **Porte G-1 — gel unique et re-datation** : fixer la date de gel D-1 pour stabiliser l'état des spécifications (MCP, A2A, NIST IR 8547) et instruire à la source primaire les relèves v0.7, v0.10 et v0.11.
2. **Porte G-3 — refonte du socle consolidé** : unifier les socles F-xx des Vol. II et III sous numérotation unique (deux tables de correspondance), puis **construire et valider par mutation** `check-compendium.py`, dont l'absence rend les contrôles de rédaction inopérants.
3. **Porte G-4 — collation de fond** : confronter les gloses et thèses des Livres III et VII au texte rédigé des 34 pièces du Vol. III, par lectures indépendantes chargées de réfuter. *(Le volet structurel est levé par la v0.14, à zéro écart ; seul le volet de fond reste dû.)*
4. **Décision D-7 — arbitrer l'accord sous défaillance** : sections dans les chapitres d'atterrissage (ch. 6, 42, 54), ou périmètre assumé et déclaré. Échéance : avant J-IV-4, la rédaction du Livre I.

---

## 6. Défauts corrigés dans ce rapport

Trois défauts de sa première rédaction, relevés à la vérification et corrigés ci-dessus :

1. **Ancrages de ligne périmés** — les renvois de la forme `PRD/TOC.md#L133` ne résolvaient plus vers les chapitres annoncés. Sur six ancrages : un seul juste (ch. 6) ; un tombant dans le premier des deux chapitres annoncés (ch. 20 pour « ch. 20-21 » — le même ancrage servant par ailleurs à désigner le ch. 34) ; quatre tombant dans des chapitres sans rapport (ch. 14, 19, 22, 26). Ils sont remplacés par des renvois **nommés** (« ch. 42 »), une ligne de fichier n'étant pas un point d'ancrage stable pour un document qui change de version à chaque passe.
2. **Risque mal numéroté** — voir la note du §4.
3. **Recommandation déjà planifiée** — l'extension de l'idempotence aux sagas figure **déjà** au ch. 54 ; seule l'extension à l'accord entre agents est neuve, et le §3 le dit désormais.

---
*Fin du document d'audit — rédigé le 24 juillet 2026, révisé le même jour après vérification sur pièces.*
