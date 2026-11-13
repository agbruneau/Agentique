## Mise en œuvre — Orchestration en périphérie, opérations déconnectées et passerelles vers l'IA physique {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Dans l’extraction minière, la production hydroélectrique, le transport maritime, la défense, l’agroalimentaire et les entrepôts très robotisés, la liaison vers le nuage central est soit inexistante par cloisonnement de sûreté (isolement physique), soit sujette à des coupures de plusieurs heures ou de plusieurs jours (météo extrême, perte de faisceau satellite, sectionnement de fibre). Un système agentique dont le moteur d’état, les politiques d’autorisation ou le modèle de raisonnement exigent un aller-retour infonuagique immobilise l’outil industriel au moment où l’autonomie locale est la plus nécessaire.
- **Décisions architecturales structurantes** :
  1.  *Irréversible pour les sites distants* : Concevoir chaque site industriel comme une cellule autonome à survie locale, avec ses propres petits modèles de langage (SLM) quantifiés (3B–8B en INT4/FP8), son moteur d’exécution durable léger, son point de décision Cedar local et son serveur SPIRE adossé à une puce matérielle TPM 2.0.
  2.  *Structurante pour l’intégrité des données* : Remplacer les verrous synchrones distants par des types de données répliqués sans conflit (CRDT) assortis de quotas de droits préalloués, pour réconcilier les sagas au retour de la liaison sans double dépense.
  3.  *Exigée en sûreté physique (ISO 10218 / IEC 61508)* : Interdire tout pilotage direct d’actionneurs robotiques par un modèle neuronal; raccorder l’orchestration d’entreprise à ROS 2 (DDS) à travers une architecture Simplex matérielle, où un contrôleur temps réel déterministe vérifié coupe la consigne adaptative dès l’approche de l’enveloppe cinématique de sécurité. Simplex est un patron d’architecture, non une voie de certification : rien n’établit qu’il confère la conformité à l’ISO 10218 ni à l’IEC 61508 (section 46.7).
- **Indicateurs de gouvernance** : Durée de survie sans liaison WAN, calculée par site et vérifiée par essai (cible de conception : $\ge 72\text{ h}$, sans source; section 46.5), taux de conflits non résolus automatiquement à la reconnexion (\< 0,2 %), latence locale de décision d’enveloppe de sécurité ($\le 1\text{ ms}$ sur microcontrôleur dédié) et 100 % des lots déployés en périphérie vérifiés par signature TUF / Sigstore.
::::

## 46.14 Autonomie locale et réconciliation après la coupure

Le chapitre 28 traite l’usine reliée au système d’information central à travers les zones de sécurité du modèle Purdue. Cette section traite deux autres cas : une liaison coupée pendant quarante-huit heures en plein hiver boréal, et un site que la réglementation sectorielle isole physiquement de façon quasi permanente (diode unidirectionnelle). Les dépendances à couper et le principe des droits préalloués sont posés à la section 46.5.

### Trois blocages d’un agent conçu pour le nuage

Un agent conçu pour l’infonuagique et placé sur un site industriel distant se bloque de trois façons dès la première perte de liaison satellite ou cellulaire privée :

1.  **Identité et politique** : Si le renouvellement des certificats NHI (SVID de 15 minutes) ou la récupération des politiques OPA/Cedar dépend d’un serveur central distant, tous les agents locaux passent en refus d’accès au bout d’un quart d’heure. Les opérations s’arrêtent alors que le matériel local est intact.
2.  **Divergence de l’état partagé** : Pendant la coupure, l’agent local du site minier consomme trois roulements de rechange du magasin local et réaffecte deux techniciens. Au siège social, le planificateur central réserve ces mêmes pièces pour une maintenance programmée la semaine suivante. Au retour du réseau, une synchronisation par écrasement (la dernière écriture l’emporte) corrompt l’inventaire ERP et fausse la comptabilité matière.
3.  **Saturation du lien de retour** : Quand la liaison satellite à bande passante limitée revient, trente agents locaux qui poussent ensemble quarante-huit heures de journaux OpenTelemetry et d’historiques d’inférence saturent le lien. Les ordres prioritaires de sécurité et de réapprovisionnement ne passent plus.

### Cellule embarquée, CRDT et quotas de droits

Le nœud en périphérie est le système maître de sa réalité physique immédiate. Le nuage central agrège de façon asynchrone, assure la curation des modèles et réconcilie les sites entre eux. La figure retient une coupure de 72 h, cible de conception : l’exposé précise que ce seuil n’a pas de source (section 46.5).

![Architecture d’orchestration Edge déconnectée : cellule locale SLM + CRDT sur coupure WAN 72 h, passerelle MCP vers ROS 2 (DDS) et enveloppe cyber-physique Simplex.](figures/fig-46-b-1.svg)

Sur une passerelle industrielle durcie (typiquement biprocesseur redondant sans ventilateur, dotée d’accélérateurs basse consommation NVIDIA Jetson Thor / IGX ou d’un NPU serveur de 35 à 150 W), la pile autonome compte quatre briques :

- **Inférence et durabilité embarquées** : Deux modèles spécialisés quantifiés tournent localement, un SLM 4B d’extraction et de routage et un SLM 8B de diagnostic technique, en INT4 AWQ, avec une latence déterministe inférieure à 80 ms. Une instance locale légère d’un moteur d’exécution durable les pilote : Restate (binaire unique en Rust) ou un travailleur Temporal sur un magasin transactionnel SQLite WAL ou RocksDB, répliqué en paire haute disponibilité locale.
- **Racine de confiance matérielle locale (TPM 2.0 et SPIRE imbriqué)** : Une autorité SPIRE intermédiaire locale, scellée dans la puce TPM 2.0 du châssis, détient un certificat intermédiaire valide 30 jours. Elle émet et renouvelle toutes les dix minutes les jetons courts des agents locaux, même en coupure totale de la liaison.
- **État partagé sans conflit** : Les ressources partagées entre le nuage et les sites se modélisent par des CRDT associés à des baux de capacité préalloués, non par un solde entier qu’une écriture peut écraser :
  - Un compteur PN-Counter additionne séparément les incréments et les décréments signés par chaque nœud $i$. La fusion, par maximum composante par composante, est commutative, associative et idempotente ($S_A \sqcup S_B = S_B \sqcup S_A$).
  - Chaque nœud détient un quota local préréservé $Q_i^{\text{local}}$ tel que $\sum_{i=1}^{N} Q_i^{\text{local}} \le Q_{\text{global}} - M_{\text{sécurité}}$.
  - Le bail d’un quota est indexé par un numéro d’époque monotone, ce qui évite la double dépense qu’une dérive d’horloge provoquerait pendant une partition asymétrique. Le nuage ne peut pas le reprendre unilatéralement sur simple délai mural (TTL) : il lui faut un message signé de restitution (`LeaseEpochSurrender`). En attendant le retour du nœud muet, les autres sites puisent uniquement dans la réserve centrale $M_{\text{sécurité}}$.
- **Reprise du réseau par file de priorité** : À la reconnexion, un ordonnanceur écoule d’abord les alertes critiques et les deltas CRDT (quelques kilo-octets en Protobuf), puis les résumés de sagas clôturées, et enfin, aux heures creuses seulement, les lots compressés de télémétrie OpenTelemetry.

#### Extrait 46.4 — Magasin d’escrow hors ligne à convergence CRDT sans double dépense (edge_crdt_escrow.py)

Le composant autorise localement, hors ligne, des sorties de pièces ou des dépenses d’urgence, sans pouvoir violer le plafond global d’entreprise à la reconnexion :

``` python
from dataclasses import dataclass, field

@dataclass
class BoundedPnCounterEscrow:
    node_id: str
    granted_quota: dict[str, int] = field(default_factory=dict)
    consumed: dict[str, int] = field(default_factory=dict)
    released: dict[str, int] = field(default_factory=dict)

    def remaining_local_budget(self, node: str) -> int:
        granted = self.granted_quota.get(node, 0)
        net = self.consumed.get(node, 0) - self.released.get(node, 0)
        return granted - net

    def try_commit_offline(self, units: int) -> tuple[bool, str]:
        if units <= 0:
            return (False, "INVALID_NON_POSITIVE_UNITS")
        avail = self.remaining_local_budget(self.node_id)
        if units > avail:
            msg = f"OFFLINE_ESCROW_EXCEEDED:avail={avail}"
            return (False, msg)
        self.consumed[self.node_id] = (
            self.consumed.get(self.node_id, 0) + units
        )
        return (True, f"COMMITTED_LOCAL:rem={avail - units}")

    def release_offline(self, units: int) -> tuple[bool, str]:
        net = (
            self.consumed.get(self.node_id, 0)
            - self.released.get(self.node_id, 0)
        )
        if units <= 0 or units > net:
            return (False, "INVALID_RELEASE_AMOUNT")
        self.released[self.node_id] = (
            self.released.get(self.node_id, 0) + units
        )
        return (True, "RELEASED_TO_LOCAL_ESCROW")

    def merge_peer_state(
        self, peer: "BoundedPnCounterEscrow"
    ) -> "BoundedPnCounterEscrow":
        def _lmax(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
            out = dict(a)
            for k, v in b.items():
                out[k] = max(out.get(k, 0), v)
            return out

        return BoundedPnCounterEscrow(
            node_id=self.node_id,
            granted_quota=_lmax(self.granted_quota, peer.granted_quota),
            consumed=_lmax(self.consumed, peer.consumed),
            released=_lmax(self.released, peer.released),
        )
```

### Réconciliation en deux phases après la coupure

Quand la liaison revient après quarante-huit heures d’isolement, les nœuds ne rouvrent pas aussitôt les vannes aux commandes centrales. Une phase transitoire de synchronisation d’horizon (`ANTI_ENTROPY_SYNC`) fusionne d’abord les compteurs CRDT, recalcule dans l’ERP central les réapprovisionnements déclenchés par la consommation des quotas locaux, renouvelle les baux $Q_i^{\text{local}}$ pour le cycle suivant et vérifie la révocation éventuelle d’identités dans la liste centrale. Le site repasse ensuite en mode fédéré nominal.

### Dimensionnement matériel et quantification

Contrairement à une salle informatique climatisée, qui dispose de baies de 40 kW, une sous-station électrique, un quai minier ou un navire impose des contraintes sévères : refroidissement passif sans ventilateur, étanchéité IP65 contre les poussières métalliques conductrices, plage thermique de $-25\,^\circ\text{C}$ à $+60\,^\circ\text{C}$, alimentation secourue par batteries 24 V DC et enveloppe électrique souvent plafonnée sous 75 à 180 watts. Deux choix d’ingénierie permettent de faire tenir une cellule multi-agents dans ce budget :

1.  **Quantification sensible à l’activation (AWQ / FP8), validée sur les appels d’outils** : Une quantification uniforme de tous les poids d’un SLM en INT4 dégrade souvent la précision syntaxique des arguments JSON de MCP et des identifiants alphanumériques de pièces. L’approche retenue garde en FP16/FP8 le 1 % de canaux saillants ainsi que les têtes de sortie grammaticale. Un modèle 8B complet et un contexte de 16 384 jetons tiennent alors dans moins de 6,8 Go de mémoire unifiée, sans perte mesurable sur la suite $\tau$-bench locale.
2.  **Exécution à l’événement, accélérateur en veille** : Un agent en périphérie ne doit pas scruter les capteurs en boucle continue par inférence neuronale. Un préfiltre déterministe léger (seuils spectraux FFT en Rust, moins de 2 W sur CPU) surveille en permanence les flux OPC UA et MQTT à 1 kHz. Il ne réveille l’accélérateur du SLM que lorsqu’une anomalie franchit l’enveloppe statistique nominale. Le facteur de marche énergétique moyen reste sous 8 % et le bridage thermique est évité.

Les autonomies de la dernière colonne sont des cibles de conception à mesurer, non des garanties : l’exposé établit que la durée de survie se calcule par site, comme le plus court de plusieurs délais (section 46.5).

| Profil de nœud en périphérie | Enveloppe électrique et thermique | Capacité cognitive locale type | Autonomie sans liaison et usage cible |
|:-----------------------|:----------------------|:------------------------|:------------------------------|
| Passerelle sur rail DIN sans ventilateur (IP65) | 35–65 W (`-25 °C` à +60 °C) | SLM 3B–4B INT4 + Cedar + SQLite | 72 h+ — Sous-station électrique, tête de puits, écluse |
| Serveur durci d’atelier ou de mine | 150–300 W (redondance N+1 locale) | Paire de SLM 8B AWQ + Restate + ROS 2 | 7 à 14 jours — Mine nordique, usine isolée, navire |
| Calculateur embarqué sur robot AMR | 25–45 W sur batterie LiFePO4 | Politique Nav2/VLA locale + MCU SIL 3 | Quart complet de 10 h — Chariot autonome sans Wi-Fi continu |

---

## 46.15 Passerelle vers l’IA physique : MCP, A2A, ROS 2 et arbitre Simplex

L’orchestration d’entreprise parle A2A v1.0 et MCP, en JSON-RPC sur HTTP. La flotte, faite de robots mobiles autonomes (AMR), de chariots élévateurs automatisés et de cellules robotisées, tourne sous ROS 2 (distributions Jazzy et Kilted) et communique en temps réel sur DDS (section 46.6) ou sur Eclipse Zenoh.

### Missions sémantiques et boucles d’asservissement

Un modèle de langage ne doit pas émettre de consignes continues de bas niveau (vitesses linéaires `cmd_vel`, angles articulaires, couples moteurs) sur un topique DDS. Même embarqué, il présente une gigue de plusieurs dizaines de millisecondes et reste sujet à des hallucinations spatiales, incompatibles avec l’inertie d’un chariot de deux tonnes qui croise un cariste humain. L’agent reste hors de la boucle de commande (section 46.6). Le pont entre MCP / A2A et ROS 2 découple trois couches :

1.  **Couche entreprise (A2A v1.0 vers le gestionnaire de flotte Open-RMF)** : La saga délègue un objectif métier de haut niveau (*« Transférer la palette PAL-8841 de la travée B-14 vers le quai d’expédition Q-03 avant 14 h 20, priorité haute, colis fragile »*).
2.  **Passerelle sémantique MCP–ROS 2 (validation géométrique et traduction en ROS 2 Actions)** : Elle n’expose que des primitives discrètes de haut niveau (`NavigateToNamedWaypoint`, `InspectGaugeAtPose`, `DockAtStation`). Avant d’instancier un objectif typé ROS 2 Action (Goal → Feedback périodique → Result) avec un profil de qualité de service DDS déterministe (RELIABLE, `DEADLINE = 50 ms`), elle vérifie l’existence du point de passage dans le graphe topologique homologué du bâtiment, l’absence de consignation de sécurité (*Lockout/Tagout*, LOTO) dans le registre Cedar et l’état de la batterie du robot.
3.  **Arbitre Simplex matériel (ISO 10218-1:2025, ISO 3691-4 et IEC 61508)** : Dans le robot mobile (ISO 3691-4) ou la cellule articulée (ISO 10218-1:2025; l’intégration relève de l’ISO 10218-2, section 46.7), les contrôleurs adaptatifs, soit les planificateurs Nav2 et les politiques locales Vision-Langage-Action VLA de manipulation, saisissent ou déplacent des charges irrégulières. Leurs commandes passent par un arbitre déterministe, logé sur un microcontrôleur temps réel séparé (MCU Safety PLC, boucle à $1\text{ ms}$). C’est la forme matérielle des trois étages décrits à la section 46.7.

L’arbitre évalue en continu l’invariant de distance d’arrêt en fonction de la vitesse instantanée $v(t)$, de la vitesse maximale d’approche humaine $v_h$, du temps de réaction matériel $t_r$ et de la décélération minimale garantie $a_{\min}(m)$, abaissée selon la masse embarquée $m$ que mesurent les jauges d’essieu :

$$d_{\text{sécurité}}(t) = \left(v(t) + v_h\right) t_r + \frac{v(t)^2}{2\,a_{\min}(m)} + d_{\text{marge}} \le d_{\text{LiDAR}}(t)$$

Dès que $d_{\text{LiDAR}}(t)$ s’approche de $d_{\text{sécurité}}(t)$ ou qu’une commande viole les butées articulaires, l’arbitre coupe physiquement le multiplexeur du contrôleur IA et bascule en moins d’une milliseconde sur le contrôleur de repli vérifié (niveau visé : SIL 3 / PL e), jusqu’à l’arrêt sûr complet. Simplex est un patron d’architecture, non une voie de certification : rien n’établit qu’il confère la conformité à l’ISO 10218 ni à l’IEC 61508, dont les niveaux d’intégrité ne sont pas abordés par l’exposé (section 46.7 et « Limites de ce chapitre »).

| Couche du pont cyber-physique | Protocole et cadence | Nature du composant | Niveau de sûreté et responsabilité |
|:--------------------|:-----------------------------|:------------------------|:--------------------------|
| Saga métier et flotte | A2A v1.0 / MCP ($0{,}5\text{–}5\text{ s}$) | Moteur d’exécution durable + SLM local | Cohérence métier, priorités, quotas |
| Passerelle MCP ↔︎ ROS 2 | DDS / Zenoh Actions ($20\text{–}50\text{ ms}$) | Traducteur déterministe Rust/C++ | Validation des points de passage, consignations LOTO |
| Planification locale / VLA | Bus interne du robot ($10\text{–}30\text{ ms}$) | Nav2 / politique neuronale locale | Efficacité de la trajectoire et de la préhension (non-SIL) |
| Arbitre Simplex et arrêt sûr | Bus de terrain PROFIsafe / FSoE ($\le 1\text{ ms}$) | Microcontrôleur de sécurité matériel isolé | Vie humaine et intégrité de la machine (IEC 61508) |

#### Extrait 46.5 — Garde-fou déterministe de passerelle MCP ↔︎ ROS 2 vérifiant consignation LOTO et enveloppe Simplex (mcp_ros2_guard.py)

Avant de traduire l’appel d’outil d’un agent logistique en objectif ROS 2 Action sur le bus DDS, la passerelle vérifie de façon synchrone l’absence de cadenassage humain (LOTO), la validité du point de passage et le battement de cœur matériel du moniteur Simplex :

``` python
from dataclasses import dataclass

@dataclass(frozen=True)
class PlantSafetyState:
    approved_waypoints: frozenset[str]
    active_loto_zones: frozenset[str]
    simplex_heartbeat_age_ms: int
    battery_soc_pct: float

def validate_ros2_mission_goal(
    waypoint_id: str,
    zone_id: str,
    state: PlantSafetyState,
) -> tuple[bool, str]:
    if state.simplex_heartbeat_age_ms > 5:
        return (False, "ABORT_SIMPLEX_HEARTBEAT_STALE")
    if zone_id in state.active_loto_zones:
        return (False, f"DENY_ZONE_UNDER_HUMAN_LOTO:{zone_id}")
    if waypoint_id not in state.approved_waypoints:
        return (False, f"DENY_UNKNOWN_WAYPOINT:{waypoint_id}")
    if state.battery_soc_pct < 18.0:
        return (False, "REDIRECT_MANDATORY_CHARGER_DOCK")
    return (True, f"DISPATCH_DDS_ACTION:{waypoint_id}")
```

### Gradation de l’autonomie selon la durée de la coupure

Même avec des SLM locaux et des compteurs CRDT, l’incertitude sur l’environnement global croît avec la durée de la coupure : tarifs douaniers périmés, certificats CRL non rafraîchis, quotas épuisés. L’orchestrateur local applique donc une atténuation progressive de l’autonomie. Les paliers ci-dessous sont des cibles de conception à valider par essai : l’exposé établit que le seuil de 72 h n’a pas de source et que la durée de survie se calcule par site, comme le plus court de plusieurs délais (jetons, certificats, journal local, quotas; section 46.5). De 0 à 24 h, l’autonomie nominale L3 est pleine sur le périmètre local. De 24 à 72 h, les engagements externes différés sont gelés et l’effort se recentre sur le maintien en condition opérationnelle et sur la sécurité. Au-delà de 72 h, le site bascule de façon ordonnée en mode consultatif assisté L1/L2 : le chef de quart cosigne localement les sorties majeures de magasin jusqu’au rétablissement des communications.

---

## 46.16 Déploiement signé hors ligne des poids, politiques et Agent Skills

Une flotte de cinquante ou de cinq cents nœuds en périphérie, répartis dans des usines, des mines ou des sous-stations électriques, expose la chaîne d’approvisionnement logicielle (OWASP ASI04). Un attaquant qui altère une mise à jour d’un paquet Agent Skills, d’un ensemble de règles Cedar ou d’un adaptateur de poids LoRA, sur une clé USB de maintenance (sites isolés) ou pendant un transfert intermittent, prend le contrôle simultané d’agents qui opèrent au contact direct d’équipements physiques.

La distribution vers la périphérie combine TUF (section 46.8) et les signatures sans clé (à clés éphémères) de Sigstore / `cosign` :

- **Lot atomique multi-artefacts** : Un nœud ne met jamais à jour un prompt isolément : il le reçoit avec le binaire d’outil MCP et le jeu de politiques Cedar avec lesquels il a été homologué en CI/CD. L’ensemble forme une archive immuable adressée par contenu (OCI Artifact), signée hors ligne par au moins deux rôles distincts (ingénierie de plateforme et sécurité OT), avec une date d’expiration anti-rejeu (protection contre l’attaque par gel).
- **Transport indifférent** : La confiance repose sur la chaîne cryptographique TUF, vérifiée contre les clés racines scellées dans le TPM 2.0 de la passerelle, et non sur le canal de transport. Le même lot peut donc être téléchargé pendant une fenêtre satellite nocturne de vingt minutes ou importé par une diode optique sur un site isolé classifié.
- **Activation A/B avec retour arrière automatique** : Le lot s’installe sur la partition passive B. Au redémarrage des travailleurs locaux, une sonde exécute dix scénarios synthétiques de santé en trente secondes. Au moindre échec d’inférence ou de connexion DDS, le chien de garde matériel rebascule sur la partition A saine précédente.

#### Extrait 46.6 — Manifeste de déploiement Edge signé TUF et garde-fou MCP-ROS2 (edge-fleet-bundle.yaml)

Ce descripteur scelle ensemble le SLM quantifié, l’espace des points de passage autorisés pour la passerelle ROS 2 et la politique de repli hors ligne. La valeur de 72 heures du repli en L1 est une cible de conception, non un seuil sourcé : la durée de survie se calcule par site (section 46.5) :

``` yaml
apiVersion: edge.aaif.linuxfoundation.org/v1
kind: SignedEdgeAutonomousBundle
metadata:
  bundleId: "boreal-edge-nordqc-2027.09.2"
  expiresUtc: "2027-12-31T23:59:59Z"
  tufThresholdSignatures: 2
spec:
  artifacts:
    slmWeights:
      modelId: "boreal-diag-slm-8b-awq-int4"
      ociDigest:
       "sha256:94c2cdf798d694ee5b8861d42c48a44b36ebce4731e02acb8aa2366ae58adaca"
    cedarPolicyBundle:
      version: "2027.09.2"
      ociDigest:
       "sha256:2415d45f7874f386982d0f2f883a90484d9d1bd39ea0a3c2c58cb3635ec56129"
    offlineSkillsPack:
      skills: ["compressor-vib-triage", "inventory-crdt-reserve"]
      ociDigest:
       "sha256:ca7ae6bf98cc8ce389b6017566459a3573abedc6dcc799bb1003090b1174faf1"
  ros2BridgeConstraints:
    ddsDomainId: 42
    allowedActionTypes: ["NavigateToWaypoint", "DockCharger"]
    waypointsMapSha256:
      "92329976c7ae4edf085237d1fc34a6ecdec98cebda198a59b3ad77837d0a598b"
    forbidRawVelocityTopics: true
    requireHardwareSimplexHeartbeatMs: 5
  offlineAutonomyPolicy:
    maxDisconnectedHoursBeforeL1Downgrade: 72
    localEmergencySpendCapCad: 5000
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Mines, énergie et infrastructures isolées — continuité sous norme NERC CIP et sites nordiques**
:::

Dans les postes de transport électrique soumis aux normes NERC CIP en Amérique du Nord ou sur les sites miniers souterrains du Bouclier canadien, aucune connexion entrante initiée depuis l’infonuagique n’est permise vers le réseau d’exploitation. L’architecture décrite ici respecte cette exigence : les agents diagnostiquent et coordonnent localement la maintenance en circuit fermé pendant des semaines, et n’exportent vers l’entreprise que des résumés signés, par une passerelle d’extraction contrôlée, pendant les fenêtres autorisées. Une panne infonuagique ne perturbe pas le site physique.
::::

---

## 46.17 Application au fil rouge : autonomie de 72 heures dans le Nord-du-Québec et entrepôt robotisé de Montréal-Est

Groupe Boréal Inc. déploie cette architecture chez BSN (sites miniers isolés) et chez BEL (entrepôt central robotisé).

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : sites miniers déconnectés au Nunavik et flotte AMR sous ROS 2 à Montréal-Est**
:::

**Deux terrains critiques** :

1.  **Sites miniers clients de BSN dans le nord du Québec (Nunavik / Côte-Nord)** : Quatorze complexes miniers exploitent des concasseurs et des compresseurs lourds Boréal, sous contrat de disponibilité garantie à 99,5 %. En février 2027, un blizzard majeur combiné à une coupure de fibre régionale a isolé un site pendant 51 heures. L’ancien agent de diagnostic infonuagique étant injoignable, une dérive thermique non arbitrée a entraîné la casse d’un réducteur principal (380 000 \$ CAD de pénalité et de remplacement).
2.  **Centre de distribution robotisé BEL de Montréal-Est** : 38 robots mobiles autonomes (AMR sous ROS 2 Jazzy) préparent les commandes de pièces urgentes 24/7 aux côtés de 60 techniciens logistiques humains.

**Architecture déployée** :

- **Boîtiers durcis sur les sites miniers** : BSN a déployé sur chaque site client nordique un serveur industriel biprocesseur redondant. Il exécute un SLM 8B INT4 distillé sur l’historique vibratoire Boréal, un magasin d’inventaire consigné en CRDT (extrait 46.4, plus haut) avec un quota local pour les pièces critiques en dépôt sur place, et un serveur SPIRE sur TPM 2.0.
- **Passerelle MCP–ROS 2 et enveloppe Simplex à Montréal-Est** : Les sagas de préparation Temporal délèguent les missions de transport à Open-RMF par la passerelle déterministe, qui interdit tout accès aux topiques moteurs bruts. Les scrutateurs LiDAR de sécurité coupent matériellement le canal de navigation hors du contrôleur SIL 3 dès qu’un opérateur franchit le rayon dynamique $d_{\text{sécurité}}(t)$.

**Résultats vérifiés en production** :

- Lors d’une coupure satellite réelle de 64 heures à l’automne 2027 sur un site minier, la cellule locale a détecté une cavitation de pompe hydraulique, réservé hors ligne la garniture mécanique en stock consigné (CRDT), généré en 42 secondes le bon de travail illustré pour le mécanicien sur place, puis resynchronisé l’inventaire SAP en 1,8 seconde au retour du lien, sans conflit.
- À Montréal-Est, les sagas agentiques ont orchestré 410 000 missions AMR sur neuf mois, sans incident de sécurité physique, avec un débit logistique accru de 31 % et 100 % des mises à jour déployées par lots signés TUF, sans interruption de quart.
::::

---

## 46.18 Décision d’architecture normative et points de contrôle

La décision ADR-028 encadre tout déploiement d’agents en périphérie industrielle ou au contact de systèmes robotisés.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-028 — Architecture Edge Local-First à synchronisation CRDT et pont robotique ROS 2 sous enveloppe matérielle Simplex**
:::

- **Statut** : Acceptée \| Périmètre : sites industriels, logistique robotisée et périphérie \| Révision : annuelle
- **Contexte** : Déployer des agents sur des sites industriels à connectivité précaire ou au contact de flottes robotiques expose l’entreprise à la paralysie opérationnelle sur perte de liaison, à des corruptions de stocks lors de la reconnexion et à des risques graves pour la sécurité physique si l’IA pilote directement des actionneurs.
- **Options évaluées** :
  1.  *Inférence et orchestration centralisées dans le nuage avec simple cache local* : Rejetée — inopérante au-delà de quelques minutes de coupure réseau et incompatible avec les sites isolés physiquement.
  2.  *Synchronisation de bases locales par écrasement (la dernière écriture l’emporte) et pilotage direct des topiques moteurs ROS 2 par un modèle embarqué* : Rejetée — perte de transactions financières ou de stocks et absence d’une enveloppe vérifiée, isolée du composant appris (section 46.7).
  3.  *Cellule autonome (SLM local, SPIRE/TPM, état CRDT à quotas de droits), distribution signée TUF/Sigstore et passerelle discrète MCP–ROS 2 doublée d’un arbitre matériel Simplex*. Retenue.
- **Décision** : (a) Exiger une survie autonome minimale de 72 heures sans liaison WAN pour tout site critique, avec repli automatique en L1 au-delà (cette exigence va au-delà de la section 46.5, qui ne retient aucun seuil sourcé : la durée de survie se calcule par site et se vérifie par essai); (b) modéliser tout état mutatif déconnecté par un CRDT borné par un quota de droits préalloué (escrow); (c) interdire tout accès d’un modèle probabiliste aux commandes cinématiques continues, hors d’une passerelle de missions homologuées et d’un moniteur matériel Simplex vérifié.
- **Conséquences** : Continuité industrielle hors réseau et sûreté des personnes confiée, en atelier robotisé, à un contrôleur vérifié et isolé du contrôleur appris, sans que Simplex vaille certification (section 46.7), en contrepartie de la gestion matérielle d’un parc de nœuds en périphérie et de la quantification des modèles embarqués.
::::

### Liste de contrôle de mise en production

1.  **Essai de déconnexion prolongée (cible de 72 h)** : La cellule maintient-elle l’inférence SLM, la rotation locale des identités SPIRE (TPM 2.0) et l’évaluation Cedar pendant la durée de survie calculée pour le site, avec 72 heures comme cible de conception sans source (section 46.5), câble WAN débranché ?
2.  **Convergence CRDT et quotas de droits** : Les stocks et les budgets manipulables hors ligne sont-ils protégés par des structures CRDT et par des plafonds locaux qui empêchent toute sur-allocation globale ?
3.  **Ordonnanceur de reconnexion** : Le mécanisme de retransmission donne-t-il la priorité aux deltas transactionnels et aux alertes critiques, devant l’évacuation différée des journaux OpenTelemetry ?
4.  **Frontière sémantique MCP–ROS 2** : A-t-on vérifié que la passerelle n’expose que des actions discrètes sur des points de passage homologués et bloque tout accès aux topiques d’asservissement moteur ?
5.  **Arbitre matériel Simplex (IEC 61508)** : Un contrôleur de sécurité temps réel indépendant surveille-t-il à la milliseconde la distance d’arrêt et coupe-t-il physiquement le canal adaptatif en cas de risque ?
6.  **Intégrité des consignations (LOTO)** : La passerelle interroge-t-elle l’état de verrouillage matériel de maintenance avant d’émettre un ordre de mouvement vers un équipement ?
7.  **Lots atomiques signés TUF / Sigstore** : Les poids des SLM, les politiques Cedar et les Agent Skills sont-ils distribués en archives signées à double clé, avec date d’expiration et bascule A/B automatique ?
8.  **Rétrogradation de sécurité après l’échéance** : Si l’isolement dépasse le plafond homologué (par exemple 72 h), le nœud rétrograde-t-il ses actions mutatives en mode consultatif L1 pour l’opérateur sur site ?
