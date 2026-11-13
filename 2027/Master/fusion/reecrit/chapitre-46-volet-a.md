## Mise en œuvre — Souveraineté cognitive, portabilité multi-cloud et reprise après sinistre cognitif {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Ancrer des processus vitaux dans un fournisseur unique de modèles frontières infonuagiques concentre deux risques que les plans de continuité TI classiques ignorent. Le premier est juridictionnel et extraterritorial : le CLOUD Act américain, la Loi 25 québécoise, BSIF E-23 et les régimes européens de souveraineté entrent en conflit sur les états d’agents et les KV-caches. Le second est l’arrêt cognitif : panne régionale d’un hyperscaler, hausse tarifaire ou retrait unilatéral d’une version de modèle, qui rompt la fidélité d’exécution des outils MCP.
- **Décisions architecturales structurantes** :
  1.  *Irréversible sur le plan légal* : Appliquer le géorepérage à tout l’état de l’agent, soit les journaux durables Temporal, les graphes bi-temporels Graphiti, les index vectoriels, les traces OpenTelemetry et les KV-caches GPU, par zone juridictionnelle souveraine. Imposer une pseudonymisation réversible à clé détenue localement (HYOK) avant tout appel à une API frontière externe.
  2.  *Structurante pour les charges sensibles* : Déployer l’inférence confidentielle sur des enclaves GPU attestées (NVIDIA H100/B200 TEE avec AMD SEV-SNP ou Intel TDX), de sorte que les logiciels et les administrateurs de l’exploitant infonuagique ne peuvent inspecter ni les consignes, ni les poids affinés, ni les tenseurs en cours de calcul. Un TEE élève le coût de l’accès sans le rendre impossible : le fabricant de la puce et la garde physique du serveur restent dans la base de confiance (section 46.2).
  3.  *Cible de conception en résilience prudentielle (BSIF E-23)* : Instituer un plan de reprise après sinistre cognitif, testé chaque trimestre, qui vise une bascule en moins de quinze minutes (`RTO < 15 min`, `RPO = 0`) d’un modèle propriétaire défaillant vers une grappe souveraine à poids ouverts, calibrée d’avance sur les mêmes contrats Open Responses et MCP. Ce seuil de quinze minutes n’a pas de source : c’est une cible de conception, à fixer par classe de tâche et à valider par exercice (section 46.4).
- **Indicateurs de gouvernance** : Couverture d’état résidant dans sa juridiction légale cible (100 %), RTO cognitif mesuré en exercice réel ($< 15\text{ min}$), maintien du score $\text{pass}^5$ en mode de secours ($\ge 94\,\%$ du nominal) et zéro clé maîtresse de déchiffrement exposée hors HSM d’entreprise.
::::

## 46.9 Résidence juridictionnelle de l’état complet et conflits de lois

La section 46.1 inventorie les états d’un agent; sa grille, une proposition sans source, en compte six, composés autrement que les couches ci-dessous. Dans une entreprise agentique de niveau L3 ou L4, une requête métier se dissémine entre divers substrats de persistance, dont plusieurs échappent aux inventaires des équipes de gouvernance des données. Les six couches qui suivent sont un inventaire proposé, non un décompte établi : « six substrats d’état » ne se retrouve dans aucune source.

### Les six couches d’état d’une saga agentique

Pour démontrer à un régulateur (Commission d’accès à l’information du Québec sous Loi 25, BSIF sous ligne directrice E-23, ou autorités européennes sous RGPD / EU Data Act) qu’un renseignement personnel ou un secret industriel réglementé n’a pas quitté indûment sa juridiction, l’architecte gouverne simultanément :

1.  **Le journal d’événements du moteur d’exécution durable (Temporal / Restate)** : Chaque argument d’outil et chaque réponse intermédiaire sérialisés dans l’historique de reprise contiennent les données métiers en clair, sauf chiffrement de charge utile côté client (Payload Codec).
2.  **La mémoire épisodique et sémantique (Graphiti / Letta / index vectoriels)** : Les plongements ne constituent pas une anonymisation opposable. Les attaques par inversion de vecteurs documentées de 2024 à 2026 reconstruisent jusqu’à 70 % des entités textuelles d’origine à partir d’un vecteur dense non chiffré.
3.  **Le cache clé-valeur d’attention (KV-cache GPU / mémoire désagrégée)** : Quand une passerelle d’inférence garde en VRAM ou sur NVMe, pendant trente minutes, les tenseurs d’attention précalculés pour réduire le TTFT (chapitre 44), ces tenseurs matérialisent le contenu exact du dossier client sur le serveur GPU hôte.
4.  **Les files de transit événementiel (Kafka / Solace) et les tampons A2A** : Les artefacts échangés entre agents spécialistes persistent sur disque selon la politique de rétention du courtier.
5.  **Le plan d’observabilité (OpenTelemetry `gen_ai.*`)** : Un collecteur SaaS hébergé dans une autre juridiction devient un vecteur d’exportation illicite si les attributs d’invite ne sont pas caviardés à la source (chapitre 33).
6.  **Les journaux d’abus et de télémétrie du fournisseur de modèle** : Sans contrat Zero-Data-Retention (ZDR) explicite, qui désactive toute mise en file d’inspection humaine chez l’éditeur, un simple appel HTTPS suffirait à conserver le contenu trente jours à l’étranger.

### Loi 25, BSIF E-23, EU Sovereign Cloud et CLOUD Act

En 2027, une organisation active au Québec, au Canada fédéral et dans l’Union européenne fait face à des exigences juridiques asymétriques. Même lorsqu’un hyperscaler américain héberge ses grappes GPU à Montréal, Toronto ou Francfort, le `U.S. CLOUD Act` (18 U.S.C. § 2713) maintient une compétence d’injonction judiciaire sur toute société mère de droit américain qui détient techniquement la capacité de déchiffrer les données. Le géorepérage n’y répond donc pas (section 46.1). L’article 17 de la Loi 25 exige une évaluation des facteurs relatifs à la vie privée (ÉFVP) démontrant une protection adéquate avant toute communication hors Québec. La ligne directrice BSIF E-23 (en vigueur le 1er mai 2027) et la ligne directrice BSIF B-10 (impartition et risque de concentration infonuagique) obligent les institutions financières fédérales à prouver leur maîtrise opérationnelle et leur stratégie de sortie face aux fournisseurs critiques de modèles.

La réponse d’ingénierie est une partition souveraine à trois zones, pilotée par agentgateway. Elle ne s’interdit pas les meilleurs modèles mondiaux et ne néglige pas le risque légal.

![Architecture de souveraineté cognitive : routage par géorepérage, enclaves GPU TEE sous clé HYOK et bascule Cognitive DR vers grappe Open-Weights souveraine.](figures/fig-46-a-1.svg)

| Classe de sensibilité métier | Résidence de l’état (Temporal, mémoire, OTel) | Régime d’inférence autorisé | Protection cryptographique exigée |
|:--------------------------|:------------------------|:-------------------------|:------------------------|
| C1 — Public / industriel non sensible | Infonuagique régional standard | API frontières mondiales ou SLM | TLS 1.3, contrat ZDR standard |
| C2 — Confidentiel affaires / PII réglementée (Loi 25) | Résidence stricte juridictionnelle (QC/CA ou UE) | API frontières régionales sous pseudonymisation ou GPU TEE | Tokenisation HMAC-FPE locale (HYOK) + Payload Codec Temporal |
| C3 — Secret stratégique / prudentiel critique (E-23 élevé, défense, santé) | Infrastructure souveraine dédiée (opérateur national ou sur site) | Exclusivement modèles internes à poids ouverts ou enclave TEE souveraine | Enclave matérielle CPU+GPU attestée, zéro transit hors juridiction |

------------------------------------------------------------------------

## 46.10 Inférence confidentielle sur GPU et pseudonymisation réversible déterministe sous clé HYOK

Les environnements d’exécution de confiance et la maîtrise des clés sont décrits aux sections 46.2 et 46.3.

### 1. Pseudonymisation réversible déterministe à conservation de structure (HYOK)

Lorsqu’une tâche de classe C2 exige la puissance de raisonnement d’un modèle frontière externe, par exemple l’analyse contradictoire d’une clause d’exclusion complexe dans un contrat d’assurance commerciale, le modèle a besoin de la structure logique et relationnelle du cas, non de la raison sociale de l’assuré, de son numéro de compte bancaire ni de l’adresse de son usine.

Avant que la requête ne franchisse la frontière du réseau interne, un filtre déterministe couplé à un SLM local de reconnaissance d’entités remplace chaque identifiant direct par un pseudonyme syntaxiquement réaliste et cohérent sur toute la session (`Assuré_7F3A`, `Usine_QC_04`, montants mis à l’échelle par un facteur secret si requis). Ce pseudonyme est dérivé par chiffrement à préservation de format (FF1/FF3-1 ou HMAC salé par saga), dont la clé maîtresse réside exclusivement dans le module matériel de sécurité (HSM) de l’entreprise (HYOK). Pour parer à la ré-identification indirecte par recoupement (Loi 25), le sas généralise aussi les quasi-identifiants structurels rares (capacité industrielle singulière, municipalité à faible densité, date exacte de sinistre) en plages catégorielles avant l’envoi. À la réception de la sortie structurée du modèle externe, la passerelle réhydrate localement les identifiants réels avant l’appel d’outil MCP interne : l’opérateur infonuagique externe n’a jamais vu la donnée nominative.

### 2. Enclaves matérielles GPU attestées

Lorsque la tâche porte sur des données non pseudonymisables (imagerie médicale, plans CAO industriels propriétaires, code source critique, grands corpus financiers) et s’exécute sur une infrastructure infonuagique louée, l’architecture s’appuie sur le calcul confidentiel GPU, arrivé à maturité sur les générations NVIDIA Hopper (H100) et Blackwell (B200), couplées à des processeurs hôtes AMD SEV-SNP ou Intel TDX.

L’amorçage, selon un modèle zéro confiance, suit trois étapes :

1.  La machine virtuelle confidentielle (CVM) et le pilote GPU établissent un canal PCIe chiffré de bout en bout (SPDM / CMA). La mémoire VRAM du GPU est isolée de l’hyperviseur de l’hébergeur par le matériel.
2.  Le matériel produit un rapport d’attestation signé par sa racine silicium. Il contient les mesures cryptographiques (PCR, *Platform Configuration Registers*) du microcode, du noyau, du moteur d’inférence (vLLM / SGLang) et de l’empreinte exacte des poids du modèle.
3.  Le rapport est soumis au service d’attestation souverain de l’entreprise cliente. Seulement si les mesures correspondent au manifeste signé approuvé, le HSM interne libère vers l’enclave la clé éphémère qui déchiffre les poids affinés et ouvre le tunnel mTLS depuis agentgateway. Cette étape applique la politique de libération des secrets de la section 46.2.

#### Extrait 46.1 — Politique d’attestation matérielle et de routage souverain HYOK (sovereign-gateway.yaml)

Cette configuration d’agentgateway applique le géorepérage juridictionnel, la pseudonymisation HYOK et la vérification d’attestation TEE avant le routage :

``` yaml
apiVersion: gateway.aaif.linuxfoundation.org/v1
kind: SovereignRoutingPolicy
metadata:
  name: boreal-jurisdictional-cognitive-fence
spec:
  keyManagement:
    mode: "HYOK_EXTERNAL_HSM"
    hsmEndpoint: "pkcs11://hsm-mtl-01.internal.boreal.ca:5696"
    sessionTokenTtlSeconds: 300
  jurisdictionRules:
    - matchClassification: "C2_QUEBEC_LAW25_PII"
      allowedStateRegions: ["ca-central-montreal"]
      primaryInferenceTarget:
        provider: "frontier-cloud-ca-east"
        requireZeroDataRetention: true
        preInferenceFilter: "HMAC_FPE_PSEUDONYMIZER_V2"
      fallbackInferenceTarget: "boreal-sovereign-tee-mtl"
    - matchClassification: "C3_OSFI_E23_HIGH_MATERIALITY"
      allowedStateRegions:
        - "ca-central-montreal"
        - "ca-east-toronto"
      forbidPublicApiEndpoints: true
      primaryInferenceTarget:
        clusterId: "boreal-sovereign-tee-mtl"
        confidentialComputing:
          requireCpuTee: "AMD_SEV_SNP"
          requireGpuTee: "NVIDIA_CC_ON"
          attestationUrl: "https://attest.sec.boreal.ca/verify"
          runtimeSha256:
            "23bee86edf807c3dc40afc55e3c56076e409f8405b0cd850413e338ae081918b"
```

### 3. Chiffrement de charge utile dans l’orchestrateur et étanchéité des KV-caches

Sécuriser l’appel GPU ne suffit pas si le serveur d’orchestration durable garde en clair les arguments et résultats d’activités dans sa base relationnelle ou Cassandra. Sur Temporal comme sur Restate, l’architecture impose un encodeur cryptographique côté travailleur (Payload Codec). Avant qu’un état ne quitte le processus travailleur déployé dans le sous-réseau souverain, chaque charge utile est chiffrée en AES-256-GCM avec une clé d’enveloppe (DEK) dérivée par sujet et scellée par le HSM local (KEK en régime HYOK). Ce découplage permet aussi l’effacement crypto-sélectif, conforme au droit à l’oubli : révoquer la sous-clé d’un client rend ses historiques d’orchestration indéchiffrables sans altérer l’intégrité séquentielle du journal d’audit. Le plan de contrôle ne manipule que des blocs binaires opaques et des métadonnées de routage non sensibles (`saga_id`, `jurisdiction_zone`, `step_status`) : ce que son hébergeur peut remettre à une réquisition se limite à ces blocs. Les clés détenues réduisent ce qu’un exploitant peut remettre; elles ne constituent pas une réponse juridique (section 46.1).

Les grappes d’inférence mutualisées demandent un soin identique pour la mémoire vive. Quand vLLM ou SGLang met en œuvre le partage de préfixe (Prefix Caching, RadixAttention; chapitre 44), l’espace de hachage des blocs de KV-cache doit préfixer chaque clé de bloc par le couple `(tenant_id, jurisdiction_zone)`. Sans ce salage par locataire et par juridiction, une attaque par canal auxiliaire temporel sur le TTFT permettrait à un locataire malveillant de la même grappe de deviner si un préfixe réglementaire ou contractuel précis vient d’être traité par un autre département, ou provoquerait un recyclage involontaire de tenseurs entre zones juridiques distinctes. À l’extinction d’une session de classe C3, les pages VRAM et les tampons NVMe de débordement sont remis à zéro avant réallocation.

Dans le tableau suivant, la visibilité nulle sur les PII vient de la pseudonymisation en amont : HYOK seul est un levier de révocation, pas une barrière pendant le traitement, et, selon AWS, le risque accru pour la disponibilité et la performance dépasse, pour la plupart des charges, le bénéfice de sécurité perçu (section 46.3). La grille de décision réserve HYOK aux classes de données qui l’exigent, ce qui reste compatible avec l’exigence de l’ADR-027 pour les classes C2 et C3.

| Modèle de maîtrise cryptographique | Détenteur de la racine (KEK) | Visibilité de l’hébergeur sur le clair | Résistance à une injonction extraterritoriale | Cas d’usage cible |
|:------------------|:-------------------|:--------------------|:----------------------|:-------------------|
| Cloud KMS natif | Hyperscaler | Totale en mémoire; accès clé possible | Faible (l’hébergeur peut déchiffrer) | Classe C1 uniquement (données publiques) |
| BYOK (*Bring Your Own Key*) | Client (importée dans KMS Cloud) | Totale en mémoire GPU/CPU | Partielle (clé révocable, mais présente en Cloud) | Classe C1+ / charges internes non PII |
| HYOK + pseudonymisation amont | HSM physique exclusif du client | Nulle sur les PII (jetons opaques seuls) | Forte (la table de correspondance reste locale) | Classe C2 (Loi 25, contrats clients) |
| HYOK + enclave CPU/GPU TEE | HSM client après attestation silicium | Nulle pour les logiciels et les administrateurs de l’hébergeur (VRAM et bus PCIe chiffrés) | La plus élevée du tableau, non absolue : un TEE élève le coût de l’accès sans le rendre impossible (section 46.2) | Classe C3 (BSIF E-23 critique, R&D) |

#### Extrait 46.2 — Encodeur Payload Codec AES-256-GCM sous clé HYOK pour moteur durable (hyok_payload_codec.py)

Le codec s’exécute uniquement dans les travailleurs internes de la zone souveraine : le serveur d’orchestration ne persiste jamais une donnée métier qu’un tiers pourrait déchiffrer :

``` python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class SovereignHyokPayloadCodec:
    def __init__(self, jurisdiction: str, hsm_client: object):
        self.jurisdiction = jurisdiction
        self._hsm = hsm_client

    def encode_state(
        self, raw_bytes: bytes, key_id: str
    ) -> dict:
        dek = self._hsm.derive_ephemeral_dek(
            key_id=key_id, zone=self.jurisdiction
        )
        nonce = os.urandom(12)
        aad = f"zone:{self.jurisdiction}|kid:{key_id}".encode()
        ciphertext = AESGCM(dek).encrypt(nonce, raw_bytes, aad)
        return {
            "encoding": "binary/aes256gcm-hyok-v1",
            "zone": self.jurisdiction,
            "key_id": key_id,
            "nonce_hex": nonce.hex(),
            "payload_hex": ciphertext.hex(),
        }

    def decode_state(self, envelope: dict) -> bytes:
        if envelope.get("zone") != self.jurisdiction:
            err = "CROSS_JURISDICTION_STATE_DENIED"
            raise PermissionError(err)
        key_id = envelope["key_id"]
        dek = self._hsm.derive_ephemeral_dek(
            key_id=key_id, zone=self.jurisdiction
        )
        nonce = bytes.fromhex(envelope["nonce_hex"])
        data = bytes.fromhex(envelope["payload_hex"])
        aad = f"zone:{self.jurisdiction}|kid:{key_id}".encode()
        return AESGCM(dek).decrypt(nonce, data, aad)
```

### 4. Plongements propres à l’entreprise pour garder le RAG opérationnel en reprise

Un piège fréquent ruine des plans de reprise cognitive bien conçus. L’entreprise prépare un modèle génératif de secours à poids ouverts, mais ses cinquante millions de fragments documentaires et sa mémoire sémantique (Graphiti) ont été indexés avec le modèle de plongements propriétaire du fournisseur primaire en panne. Dès que l’API externe tombe, aucune requête ne peut plus être vectorisée dans le même espace latent, et toute la mémoire de l’entreprise devient inutilisable.

La règle est formelle : ne dépendre d’aucune API propriétaire fermée pour la vectorisation ni pour le reclassement des référentiels maîtres. Les pipelines d’indexation utilisent dès le premier jour un modèle de plongements multilingue compact à poids ouverts, figé et exécuté en interne (0,5B à 1,5B paramètres, latence `< 8 ms`), complété par la recherche lexicale déterministe BM25. Lors d’une bascule, 100 % des index vectoriels et des graphes restent interrogeables sans réindexation d’urgence. Cette règle prolonge la mesure « l’état hors du fournisseur » de la section 46.4.

------------------------------------------------------------------------

## 46.11 Reprise après sinistre cognitif : panne ou retrait d’un modèle frontière

La section 46.4 établit que rétablir un accès ne rétablit pas un comportement. Remplacer dans l’urgence un modèle propriétaire victime d’une panne mondiale par un modèle à poids ouverts d’une autre famille, sans préparation, provoque fréquemment une cascade d’échecs : arguments JSON de MCP structurés autrement, verbosité modifiée qui fait déborder un budget de jetons, propension accrue aux faux positifs d’escalade. Une architecture soumise à des exigences de haute disponibilité ou à la supervision prudentielle (BSIF E-23, DORA en finance européenne) conçoit donc la reprise après sinistre cognitif comme une discipline propre. Le secours retenu ici est toujours une grappe souveraine à poids ouverts : cela va au-delà de la section 46.4, qui retient un modèle de secours par classe de tâche, chez un autre exploitant, et autohébergé pour les classes critiques.

### Les quatre piliers d’une bascule sans rupture (`RTO < 15 min`, `RPO = 0`)

1.  **Contrats normalisés et purge des états opaques** : Aucun code applicatif n’appelle le SDK propriétaire d’un fournisseur de modèles. Toute requête d’inférence emprunte l’enveloppe normalisée Open Responses (gouvernée par l’AAIF), et toute invocation d’outil respecte les schémas JSON canoniques de MCP, validés par un décodage contraint (grammaires CFG sur la grappe de secours vLLM). À mi-parcours d’une saga multi-tours, l’adaptateur Open Responses écarte les blocs de délibération chiffrés propres au fournisseur défaillant et reconstruit le contexte du modèle de secours à partir du seul journal canonique des faits et des sorties d’outils validés. Même un modèle de secours plus sobre ne peut alors émettre un appel d’outil syntaxiquement invalide.
2.  **Double profil de consignes précompilé** : Chaque agent critique L3 est homologué en CI/CD (chapitre 34) sous deux profils jumeaux, versionnés ensemble : un profil nominal, optimisé pour le modèle primaire, et un profil de secours, compilé pour un modèle à poids ouverts souverain, audité et figé dans le registre interne d’artefacts de l’entreprise (par exemple avec DSPy, chapitre 47). L’homologation exige $\text{pass}^5_{\text{DR}} \ge 0{,}94 \cdot \text{pass}^5_{\text{nominal}}$ sur la suite $\tau$-bench du domaine. Ce profil réalise la qualification d’avance de la section 46.4.
3.  **Grappe de secours à montée en charge élastique** : Maintenir 100 % de la capacité GPU de pointe allumée à vide doublerait la facture FinOps. Un noyau minimal reste allumé et héberge déjà les SLM quotidiens, qui couvrent immédiatement les flux vitaux P0. Des réservations capacitaires prioritaires d’instances GPU souveraines chargent les poids, préchargés dans le cache NVMe local, en moins de 180 secondes.
4.  **Resserrement prudentiel automatique des seuils HOTL** : Tant que la fabrique opère sur le modèle de secours, le moteur de politique abaisse de 15 à 25 % les plafonds financiers d’engagement autonome L3. Les cas limites les plus subtils passent temporairement aux superviseurs humains HOTL, sans interrompre le flux courant (`RPO = 0` grâce à la mise en file durable Temporal). Cette mesure donne une forme chiffrée au mode dégradé de la section 46.4.

Le seuil de quinze minutes de la formule n’a pas de source : c’est une cible de conception, à fixer par classe de tâche et à valider par exercice. Il n’est plausible que pour le reroutage vers un modèle déjà qualifié; la requalification forme une seconde horloge, courte seulement si le travail est fait d’avance (section 46.4).

Le temps de reprise cognitif effectif $\text{RTO}_{\text{cog}}$ se modélise et se vérifie lors des exercices trimestriels selon :

$$\text{RTO}_{\text{cog}} = t_{\text{détection}} + t_{\text{quiescence}} + \max\bigl(t_{\text{warmup}}^{\text{GPU}},\, t_{\text{switch}}^{\text{gateway}}\bigr) + t_{\text{canary}}^{\text{santé}} \le 15\text{ min}$$

#### Extrait 46.3 — Orchestrateur de bascule Cognitive DR sans perte de transaction (cognitive_dr_switch.py)

Ce contrôleur coordonne la suspension des activités Temporal en vol, la commutation vers le profil homologué à poids ouverts et l’ajustement des seuils Cedar. L’extrait ne montre que la décision de bascule :

``` python
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelHealthMetrics:
    error_rate_5m: float
    p95_ttft_ms: int
    consecutive_429_or_5xx: int
    provider_deprecation_flag: bool

@dataclass(frozen=True)
class DrFailoverPlan:
    activate_dr: bool
    target_profile_id: str
    hotl_threshold_multiplier: float
    reason: str

def evaluate_cognitive_dr_trigger(
    metrics: ModelHealthMetrics,
    dr_pass5_score: float,
) -> DrFailoverPlan:
    unhealthy = (
        metrics.provider_deprecation_flag
        or metrics.error_rate_5m >= 0.08
        or metrics.p95_ttft_ms >= 12000
        or metrics.consecutive_429_or_5xx >= 25
    )
    if not unhealthy:
        return DrFailoverPlan(
            activate_dr=False,
            target_profile_id="PRIMARY_FRONTIER_V2027",
            hotl_threshold_multiplier=1.0,
            reason="NOMINAL_HEALTH",
        )

    if dr_pass5_score < 0.90:
        return DrFailoverPlan(
            activate_dr=True,
            target_profile_id="SAFE_HOLD_L2_HUMAN_QUEUE",
            hotl_threshold_multiplier=0.0,
            reason="DR_MODEL_BELOW_SAFETY_FLOOR",
        )

    return DrFailoverPlan(
        activate_dr=True,
        target_profile_id="SOVEREIGN_OPEN_WEIGHTS_70B_INT8",
        hotl_threshold_multiplier=0.80,
        reason="AUTOMATIC_COGNITIVE_DR_FAILOVER",
    )
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Institutions financières (BSIF E-23 et B-10, DORA UE) — tester le risque de concentration cognitive**
:::

À compter de mai 2027 au Canada (BSIF E-23 conjuguée à B-10) et sous le règlement DORA en Europe, dépendre d’une seule API de modèle externe pour l’octroi de crédit, la gestion des sinistres ou la surveillance anti-fraude constitue un risque de concentration de tiers critique. Les inspecteurs exigent la preuve documentée d’au moins un exercice annuel de débranchement réel du fournisseur principal de LLM. L’exercice doit montrer que la coupure franche ne provoque ni corruption comptable, ni violation d’un délai réglementaire de déclaration, ni fuite de données vers une région de repli hors juridiction.
::::

------------------------------------------------------------------------

## 46.12 Application au fil rouge : architecture souveraine Québec–Canada–UE et exercice de bascule chez Groupe Boréal

Groupe Boréal Inc. a mis à l’épreuve sa souveraineté cognitive et sa reprise après sinistre juste avant l’audit prudentiel du printemps 2027.

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : cloisons souveraines Loi 25 / UE et bascule vers le modèle de secours en 11 minutes**
:::

**Défi réglementaire et opérationnel** : Chez Boréal Capital & Assurances (BCA), les sagas d’indemnisation manipulent des états financiers non publics et des dossiers personnels québécois (Loi 25 classe C2/C3). Les filiales allemande et française de BSN sont contractuellement liées à quatre grands industriels européens, qui interdisent tout traitement hors d’un *EU Sovereign Cloud* détenu et opéré sous droit européen. Lors d’un incident réel fin janvier 2027, une panne d’authentification de 3 h 40 chez un fournisseur américain de modèle frontière avait gelé les files d’analyse contractuelle de niveau 3.

**Architecture déployée** :

1.  **Trois cellules d’état souveraines et Payload Codec Temporal** : Boréal a cloisonné l’état en trois cellules : Montréal (QC/CA), Francfort (UE souverain) et Chicago (US). Tous les journaux Temporal et les graphes Graphiti sont chiffrés avec des clés conservées dans deux HSM physiques que Boréal détient à Montréal et à Francfort (HYOK).
2.  **Inférence TEE et pseudonymisation HMAC-FPE** : Pour les dossiers C3 de souscription BSIF E-23, l’inférence tourne exclusivement sur une grappe d’enclaves NVIDIA H100 Confidential Computing hébergée au Québec, avec attestation distante vérifiée à chaque démarrage. Pour les cas C2, le filtre HMAC-FPE d’agentgateway pseudonymise 100 % des entités nominatives avant tout appel externe.
3.  **Reprise cognitive bimodèle** : Chaque saga critique dispose d’un profil jumeau homologué en CI/CD sur un modèle à poids ouverts de 70 milliards de paramètres, servi par SGLang avec décodage grammatical contraint MCP.

**Exercice de bascule audité (avril 2027)** : Un mardi ouvrable à 10 h 30, l’équipe SRE a coupé au pare-feu l’accès sortant vers le fournisseur de modèle primaire :

- Détection par agentgateway en 28 secondes; quiescence sans perte (`RPO = 0`) des 142 sagas en cours sur Temporal.
- Montée en charge des nœuds GPU souverains à Montréal et Francfort et commutation des profils en 11 minutes et 14 secondes (`RTO < 15 min` respecté).
- Maintien de 96,4 % de réussite bout en bout (`pass^5`), avec resserrement automatique de 20 % des seuils d’escalade vers les souscripteurs HOTL pendant les quatre heures de l’exercice, validant sans réserve le volet continuité du dossier BSIF E-23.
::::

------------------------------------------------------------------------

## 46.13 Décision d’architecture normative et points de contrôle

La décision ADR-027 fixe l’indépendance juridictionnelle et l’indépendance à l’égard du fournisseur de la fabrique agentique.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-027 — Géorepérage de l'état complet, inférence confidentielle HYOK/TEE et reprise après sinistre cognitif bimodèle**
:::

- **Statut** : Acceptée \| Périmètre : Infonuagique, sécurité, données et continuité d’activité \| Révision : semestrielle
- **Contexte** : Dépendre d’un seul fournisseur infonuagique de modèles frontières expose l’organisation aux conflits extraterritoriaux (CLOUD Act contre Loi 25 / RGPD), à la persistance involontaire de données dans les KV-caches et les journaux d’orchestration, ainsi qu’à l’arrêt complet des processus métiers lors d’une panne ou de la dépréciation d’une API.
- **Options évaluées** :
  1.  *Dépendance mono-fournisseur avec clauses contractuelles standards* : Rejetée — insuffisante techniquement face aux pannes régionales et au risque de concentration BSIF E-23 / B-10.
  2.  *Interdiction totale des modèles infonuagiques au profit exclusif de petits modèles sur site* : Rejetée — pénalise la qualité de raisonnement sur les cas complexes non sensibles ou correctement pseudonymisés.
  3.  *Cloisonnement juridictionnel des 6 couches d’état inventoriées à la section 46.9, sous clé HYOK, enclaves GPU TEE pour la classe C3, et homologation CI/CD obligatoire d’un profil de secours souverain à poids ouverts (cible de conception `RTO < 15 min`, section 46.4)*. Retenue.
- **Décision** : (a) Interdire tout transfert hors juridiction des journaux durables, mémoires vectorielles/graphes et KV-caches des classes C2/C3; (b) exiger HYOK (pseudonymisation HMAC-FPE ou enclave TEE attestée); (c) bloquer en CI/CD toute saga critique L3/L4 dépourvue d’un profil de secours à poids ouverts atteignant $\ge 94\,\%$ du $\text{pass}^5$ nominal et testé trimestriellement.
- **Conséquences** : Réduction de ce que l’exploitant peut remettre à une réquisition, sans valoir réponse juridique (section 46.1), et résilience aux pannes ou aux hausses tarifaires d’hyperscalers, au prix d’une capacité GPU souveraine maintenue en attente et d’une double validation CI/CD.
::::

### Liste de contrôle de mise en production

1.  **Cartographie des 6 substrats d’état proposés (section 46.9)** : Les journaux Temporal/Restate, graphes mémoire, index vectoriels, KV-caches, courtiers d’événements et traces OTel résident-ils tous physiquement dans la juridiction légale requise ?
2.  **Chiffrement HYOK et Payload Codec** : Les charges utiles d’orchestration et les index vectoriels sont-ils chiffrés avec des clés détenues dans un HSM sous contrôle exclusif de l’entreprise ?
3.  **Pseudonymisation déterministe amont** : Les requêtes de classe C2 routées vers une API externe subissent-elles une tokenisation réversible locale et bénéficient-elles d’un engagement contractuel Zero-Data-Retention ?
4.  **Attestation matérielle GPU TEE** : Pour les charges critiques C3 en infonuagique, le HSM vérifie-t-il automatiquement le rapport d’attestation silicium CPU+GPU avant de libérer les clés de session ?
5.  **Abstraction Open Responses et décodage contraint** : Le code métier est-il exempt d’appels SDK propriétaires et la grappe de secours impose-t-elle le respect grammatical strict des schémas MCP ?
6.  **Double homologation CI/CD** : Chaque agent critique possède-t-il un profil de consignes secondaire validé sur un modèle souverain à poids ouverts avec un score $\text{pass}^5$ supérieur au seuil minimal ?
7.  **Ajustement prudentiel en mode dégradé** : La bascule resserre-t-elle automatiquement les plafonds d’autonomie L3 au profit d’une supervision HOTL accrue ?
8.  **Exercice de bascule trimestriel** : La déconnexion réelle du fournisseur primaire a-t-elle été testée, avec mesure du délai réel face à la cible de `RTO < 15 min` et preuve d’un `RPO = 0` ?
