## Mise en œuvre — Identités non humaines (NHI) de première classe et délégation cryptographique {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu d’affaires et de risque** : Un agent autonome peut s’authentifier en réutilisant le jeton interactif de l’employé (usurpation) ou au moyen d’un compte de service statique aux droits étendus, partagé entre plusieurs flux. Ce double raccourci supprime la non-répudiation comptable, élargit le rayon d’impact de toute injection de prompt (OWASP ASI03) et met l’organisation en défaut devant les obligations prudentielles de traçabilité nominative (BSIF E-23, SOX, Loi 25).
- **Décisions architecturales structurantes** :
  1.  *Irréversible et fondatrice* : Supprimer toute clé d’API statique au profit d’identités non humaines (NHI) de première classe, attestées cryptographiquement au démarrage de la charge de travail (SPIFFE/SPIRE) et gouvernées dans l’annuaire d’entreprise (Microsoft Entra Agent ID), avec un parrain humain obligatoire.
  2.  *Structurante sur chaque flux* : Imposer à chaque frontière entre agents (A2A v1.0) ou vers un serveur d’outils (MCP) un échange de jetons OAuth 2.1 conforme à la RFC 8693, qui préserve le sujet initial (`sub`), empile la généalogie des acteurs (`act`) et réduit strictement la portée fonctionnelle et financière (RFC 9396, RAR).
  3.  *Réversible par configuration* : Le mécanisme de liaison cryptographique du jeton au détenteur : mTLS (RFC 8705) sur le maillage interne, DPoP (RFC 9449) pour les franchissements infonuagiques ou partenaires.
- **Indicateurs de gouvernance associés** : Taux de couverture d’attestation matérielle/logique NHI (cible : 100 % des agents L2+), durée de vie médiane des justificatifs émis (cible : $\le 300\,\text{s}$ pour les jetons d’accès, $\le 15\,\text{min}$ pour les SVID), ratio d’atténuation des permissions par saut de délégation et délai de révocation globale d’une identité d’agent compromise.
::::

## 30.7 Impasse du jeton humain emprunté et du compte de service statique face aux graphes dynamiques

La gestion des identités et des accès (IAM) classique connaît deux appelants. Le premier est la personne présente derrière un écran, authentifiée par fédération OpenID Connect (OIDC) et par authentification multifacteur (FIDO2/WebAuthn). Le second est le démon logiciel déterministe, lot nocturne ou microservice d’intégration, doté d’un identifiant technique fixe (*service principal*) et dont le graphe d’appels a été codé en dur, puis validé avant la mise en production.

Un système multi-agents de troisième génération ne relève d’aucun des deux. La séquence d’appels d’un agent orchestrateur n’est pas figée à la compilation : elle émerge de la décomposition d’un objectif métier, confronté à un contexte événementiel variable. L’agent exécute des dizaines de requêtes inter-domaines par minute, reste exposé à la confusion entre données et instructions (OWASP ASI01) et travaille souvent de façon asynchrone, à 3 heures du matin, quand l’employé à l’origine du mandat est hors ligne.

Quand une organisation plaque ses patrons IAM traditionnels sur une flotte agentique sans les adapter, elle tombe dans l’un des deux antipatrons observés lors de la vague 2024–2025.

### Antipatron 1 : l’emprunt brut du jeton humain

L’application cliente capture le jeton d’accès OAuth de l’utilisateur connecté et le transmet tel quel, dans l’en-tête `Authorization: Bearer`, à l’agent d’interface. Celui-ci le relaie à un agent spécialiste, qui le présente à un serveur MCP ou à une API d’entreprise. MCP interdit à un serveur d’accepter ou de relayer un jeton qui n’a pas été émis pour lui (section 30.1). D’un agent à l’autre, la règle est qu’un sous-agent ne reçoit jamais le jeton de son parent (section 30.2). Cette pratique ouvre trois failles :

1.  **Héritage du rayon d’impact humain.** Un directeur financier ou un ingénieur principal détient légitimement, au cours de sa journée, des droits étendus sur des dizaines de modules (SAP, Workday, SharePoint, Snowflake). Il demande à un agent de « synthétiser les pénalités de retard du fournisseur X à partir du dossier courriel ». Si un document joint contient une charge d’injection indirecte, le relais de son jeton confère momentanément à l’agent la capacité technique d’approuver un virement ou d’extraire la grille salariale de sa division.
2.  **Perte de la distinction dans les journaux d’audit.** Pour le système d’enregistrement cible, une écriture faite directement par Marie Tremblay à son poste de travail et une écriture hallucinée par un agent qui détient son jeton produisent la même trace d’audit. Dans un litige réglementaire ou une fraude interne, la valeur probante des journaux est perdue.
3.  **Rupture sur les régimes asynchrones (T3 et T4).** Quand le jeton interactif initial expire, après soixante minutes, une saga durable suspendue dans Temporal ou Restate échoue. Les équipes pressées en viennent souvent à réclamer la portée `offline_access` et à stocker des jetons de rafraîchissement humains à longue durée de vie dans les bases d’état applicatives, où ils offrent une cible de choix à un attaquant.

### Antipatron 2 : le compte de service partagé aux droits étendus

Pour contourner l’expiration des sessions humaines et permettre le déclenchement par événements (Kafka, OPC UA, webhooks), de nombreuses équipes passent à l’extrême opposé. Elles provisionnent un compte de service unique pour l’orchestrateur ou le serveur MCP, avec un secret client statique, souvent renouvelé tous les douze à vingt-quatre mois, et l’union des permissions requises par tous les utilisateurs possibles.

Ce raccourci généralise à l’entreprise le cas du serveur plus puissant que chacun de ses appelants (section 30.1) : c’est le problème du délégué confus. Le système cible (Guidewire, Salesforce ou SAP S/4HANA) ne voit que l’identité générique `svc-boreal-ai-prod`. Ses contrôles natifs de sécurité au niveau des lignes (RLS) deviennent inopérants, puisque le compte technique a le droit de lire toutes les filiales. Le cloisonnement entre utilisateurs repose alors sur un filtre WHERE que l’agent ou son connecteur construit dynamiquement, c’est-à-dire sur la couche la plus exposée aux manipulations sémantiques.

### Loi d’atténuation monotone sur un graphe de délégation

La loi qui suit est une cible de conception. Aucune norme adoptée ne garantit l’atténuation de saut en saut : en attendant, chaque saut repasse par le serveur d’autorisation et l’orchestrateur consigne la chaîne (section 30.2). Dans un graphe d’exécution dynamique de $k$ sauts successifs entre un sujet initiateur $u$ et des acteurs non humains $a_1, a_2, \dots, a_k$, le modèle de confiance zéro agentique impose que l’ensemble des permissions effectives $P_i$ au saut $i$ obéisse à une loi d’intersection et d’atténuation monotone stricte :

$$P_i \subseteq P_{i-1} \cap M(a_i) \cap R_i, \quad P_0 = D(u) \cap S_0$$

$D(u)$ et $S_0$ bornent les droits initiaux de la session humaine. $M(a_i)$ est le plafond maximal de permissions homologué statiquement sur le gabarit (*Blueprint*) de l’agent $a_i$. $R_i$ est le sous-ensemble minimal d’opérations que requiert la seule sous-tâche déléguée au saut $i$. Deux corollaires en découlent :

- **Aucune amplification de privilèges.** Dans ce modèle, un agent aval $a_i$ n’exerce jamais un droit que l’initiateur humain $u$ n’a pas, même si son connecteur technique le permettrait. Inversement, un utilisateur très privilégié ne peut pas forcer un agent spécialisé de lecture (L1) à écrire hors de son mandat $M(a_i)$.
- **Décroissance monotone du rayon d’impact.** Plus l’exécution approche des feuilles spécialisées du graphe ($P_k \subset \dots \subset P_1 \subset P_0$), plus le jeton transporté est étroit, éphémère et lié à un objet métier précis, par exemple un seul numéro de série d’équipement et un plafond monétaire explicite.

Le tableau compare les quatre approches d’identité observées dans l’industrie.

| Critère d’évaluation (confiance zéro) | Clé d’API / Compte statique partagé | Emprunt brut du jeton humain | Flux `client_credentials` isolé par agent | Cible 2027 : NHI attestée (SPIFFE) + RFC 8693 atténué |
|:-----------------|:--------------------|:--------------------|:-------------------|:----------------------|
| Identité de l’initiateur (`sub`) | Perdue (écrasée par le compte technique) | Présente mais non distinguée de l’agent | Absente (contexte purement machine) | Préservée de bout en bout et vérifiable |
| Généalogie des agents (`act`) | Inexistante | Inexistante (usurpation opaque) | Limitée au dernier appelant direct | Chaîne imbriquée (`act`), informative selon la RFC 8693 et consignée par l’orchestrateur (section 30.2) |
| Principe du moindre privilège | Violé (union de tous les cas d’usage) | Violé (hérite de 100 % des droits humains) | Statique par classe d’agent | Dynamique par tâche (RFC 9396 RAR) |
| Résistance au vol de jeton | Nulle (secret rejouable partout, long TTL) | Faible (jeton rejouable jusqu’à expiration) | Moyenne si secret stocké en coffre | Forte (mTLS / DPoP + TTL $\le 5\,\text{min}$) |
| Compatibilité asynchrone (T3/T4) | Oui, mais hors de tout contrôle nominatif | Non (échoue à l’expiration de session) | Oui pour événements purement techniques | Native (mandats bornés + escalade CIBA) |
| Homologation BSIF E-23 / Loi 25 | Non conforme (échec d’audit critique) | Non conforme (défaut de non-répudiation) | Partielle (flux techniques sans PII) | Conforme (auditabilité et SoD prouvables) |

---

## 30.8 Identité cryptographique et provenance d’agent : SPIFFE/SPIRE, Entra Agent ID et W3C DIDs

Élever les agents au rang d’identités non humaines (NHI) de première classe exige de séparer trois préoccupations que les architectures historiques confondaient : l’attestation physique et logique de la charge de travail, la gouvernance dans l’annuaire d’entreprise et la fédération de provenance entre organisations.

### Couche 1 : attestation continue sans secret sur disque avec SPIFFE et SPIRE

Le problème du secret zéro est le défaut d’origine des identités machines. Pour récupérer ses clés dans un coffre-fort numérique, un conteneur doit déjà détenir un premier secret d’amorçage, injecté par variable d’environnement ou fichier monté. Ce secret peut fuir par un journal d’erreur, un instantané disque ou une attaque par exécution de code (ASI05).

SPIFFE (projet gradué de la CNCF) et son implémentation de référence SPIRE n’exigent aucun secret pré-partagé (section 29.4). Quand un pod qui héberge un agent spécialiste démarre sur un nœud Kubernetes ou une machine virtuelle :

1.  L’agent SPIRE local du nœud, lui-même attesté matériellement par un module TPM 2.0 ou par un jeton d’instance infonuagique signé, inspecte hors bande le processus appelant par l’API locale Unix (*Workload API*). Il interroge directement le noyau Linux, le démon de conteneurs (`containerd`) et l’API `kubelet`.
2.  Il vérifie un ensemble strict de sélecteurs d’attestation : espace de noms Kubernetes, compte de service, signature cryptographique et condensat SHA-256 exact de l’image OCI de l’agent, voire le condensat de son paquet de configuration immuable.
3.  Quand tous les sélecteurs concordent, et alors seulement, SPIRE délivre en mémoire vive un SVID (*SPIFFE Verifiable Identity Document*) sous deux formes : un certificat X.509-SVID pour le chiffrement et l’authentification mutuelle mTLS du transport, et un JWT-SVID de courte durée (typiquement 15 minutes, renouvelé automatiquement à mi-vie) qui encode l’identifiant canonique, tel que `spiffe://boreal.ca/ns/bca-prod/sa/warranty-adjudicator-v2`.

### Couche 2 : gouvernance d’annuaire, *Blueprints* et parrainage humain (Microsoft Entra Agent ID)

SPIFFE prouve quel code s’exécute sur quelle infrastructure. Il ne gère ni les politiques d’entreprise, ni les revues d’accès trimestrielles, ni la responsabilité hiérarchique. C’est le rôle du plan de gouvernance d’annuaire, que Microsoft Entra Agent ID incarne en 2026–2027, avec des extensions NHI équivalentes chez Okta, Ping et AWS IAM.

Ces annuaires distinguent les agents des *service principals* applicatifs par trois primitives (section 29.2) :

- **Le gabarit d’identité (*Agent Identity Blueprint*).** Modèle déclaratif immuable qui décrit une classe d’agent : son niveau d’autonomie L1–L4, les portées maximales $M(a_i)$ qu’il pourra solliciter en délégation, sa classification de risque BSIF E-23 et ses justificatifs d’identité fédérés (*Federated Identity Credentials*, FIC), qui pointent vers l’émetteur SPIRE de l’entreprise.
- **L’instance d’identité d’exécution (*Agent Identity*).** Entité distincte, instanciée à partir du Blueprint pour un environnement ou une division. Elle a ses propres journaux de connexion, ses politiques d’accès conditionnel, qui évaluent l’état de conformité du cluster ou le score de risque en temps réel, et un interrupteur de désactivation immédiate.
- **Le parrain humain obligatoire.** Aucune identité d’agent ne peut être créée ni maintenue active sans être rattachée nominativement, dans l’annuaire, à un responsable métier et à un propriétaire technique actifs dans le SIRH (Workday). Si le parrain quitte l’organisation ou change de division, un flux de gouvernance d’identité (IGA) transfère la responsabilité sous 72 heures ou suspend automatiquement le renouvellement des jetons de l’agent.

### Couche 3 : provenance entre entreprises par W3C DIDs et Verifiable Credentials

Quand la Fabrique Agentique franchit les frontières de l’entreprise, ni le domaine de confiance SPIFFE interne (`boreal.ca`) ni le locataire Entra ID ne sont partagés. C’est le cas lorsque l’*Agent Approvisionnement* de Boréal négocie par A2A v1.0 des délais et des pénalités avec l’*Agent Commercial* d’un aciériste allemand.

Pour éviter le retour aux clés d’API bilatérales, ingérables à l’échelle de 2 000 fournisseurs, l’écosystème inter-entreprises 2027 (notamment sous l’impulsion d’AGNTCY et des profils A2A B2B) s’appuie sur les standards du W3C : les identifiants décentralisés (W3C DID v1.0, méthodes `did:web` ou `did:webvh` avec historique de clés vérifiable), couplés aux attestations vérifiables (W3C Verifiable Credentials Data Model 2.0). Les DID sont présentés à la section 29.6. L’agent externe publie ses clés publiques de signature sous son domaine DNS corporatif durci (DNSSEC et transparence des clés). Lors de la poignée de main A2A, il présente une attestation vérifiable signée par la chambre de commerce, un auditeur externe ou la direction juridique de son entreprise. Elle établit son mandat légal et son plafond d’engagement contractuel.

#### Extrait 30.1 — Attestation locale SPIRE et document de provenance externe W3C DID / VC 2.0

Le bloc YAML enregistre l’agent dans SPIRE et exige la correspondance simultanée du compte Kubernetes et du condensat exact de l’image signée. Le bloc JSON est l’attestation W3C VC 2.0 exposée lors d’une fédération A2A externe :

``` yaml
# 30.1a — Enregistrement déclaratif SPIRE (CRD Kubernetes Controller Manager)
apiVersion: spire.spiffe.io/v1alpha1
kind: ClusterSPIFFEID
metadata:
  name: bca-warranty-adjudicator-prod
spec:
  spiffeIDTemplate: >-
    spiffe://boreal.ca/ns/{{ .PodMeta.Namespace }}/sa/{{
    .PodSpec.ServiceAccountName }}
  jwtIssuer: "https://spire-oidc.identity.boreal.ca"
  ttl: "15m"
  podSelector:
    matchLabels:
      app.kubernetes.io/name: "warranty-adjudicator"
      agent.boreal.ca/autonomy-tier: "L3"
      agent.boreal.ca/bsif-e23-class: "tier-2-material"
  namespaceSelector:
    matchLabels:
      environment: "production"
      division: "bca"
  workloadSelectorTemplates:
    - "k8s:sa:warranty-adjudicator-v2"
    - "k8s:container-image-sha256:8f4e2b9c71d03a6ef92c14b7085a3e19\
      d4f72c80b165e9a43c4b901a6d2e5f18"
```

``` json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://schemas.agntcy.org/credentials/agent-mandate/v1"
  ],
  "id": "urn:uuid:7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "type": ["VerifiableCredential", "EnterpriseAgentMandateCredential"],
  "issuer": {
    "id": "did:web:boreal.ca:legal-entity",
    "name": "Groupe Boréal Inc. (LEI: 549300BOREALCA2027X9)"
  },
  "validFrom": "2027-01-15T00:00:00Z",
  "validUntil": "2027-04-15T00:00:00Z",
  "credentialStatus": {
    "id": "https://trust.boreal.ca/status/2027/mandates#4412",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "4412",
    "statusListCredential": "https://trust.boreal.ca/status/2027/mandates"
  },
  "credentialSubject": {
    "id": "did:web:agents.boreal.ca:bel:procurement-negotiator",
    "spiffeFederationBinding":
      "spiffe://boreal.ca/ns/bel-prod/sa/procurement-negotiator",
    "agentCardUrl": "https://agents.boreal.ca/bel/proc/agent-card.json",
    "authorizedActions": [
      "rfq.issue",
      "delivery.reschedule",
      "po.propose_amendment"
    ],
    "maxBindingCommitmentCad": 25000,
    "humanSponsorRole": "VP Approvisionnement Industriel BEL"
  },
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "eddsa-jcs-2022",
    "created": "2027-01-15T08:30:00Z",
    "verificationMethod": "did:web:boreal.ca:legal-entity#key-ed25519-2027-01",
    "proofPurpose": "assertionMethod",
    "proofValue": "z4oJ8h7R9mKpL2xQvN5tWzY3cBfD6gHjM1nPqRsTuVwXyZ8aBcDe"
  }
}
```

L’entrée `BitstringStatusListEntry` (liste de révocation du W3C par champ de bits compressé) permet à un partenaire externe de vérifier en une milliseconde, sans appel téléphonique ni divulgation d’information confidentielle, que le mandat de l’agent négociateur de Boréal n’a pas été révoqué dans l’heure précédente.

---

## 30.9 Délégation multi-sauts OAuth 2.1 OBO, RFC 8693 (sub/act), atténuation RAR et escalade CIBA

Le mandat d’un utilisateur humain, ou d’un événement métier authentifié, traverse une chaîne d’agents spécialistes jusqu’au serveur MCP final. Chaque agent y porte l’identité ancrée dans SPIFFE et gouvernée dans l’annuaire. Quatre briques assurent la propagation : OAuth 2.1, l’échange de jetons (RFC 8693), les requêtes d’autorisation riches (RFC 9396, RAR) et les preuves de possession (mTLS, RFC 8705; DPoP, RFC 9449). Cette combinaison va au-delà de ce que retient l’exposé. Ni MCP ni AIMS ne s’appuient sur la RFC 9396, et aucun profil ne l’applique aux agents (section 30.3).

![Délégation cryptographique multi-sauts : attestation SPIFFE, échange RFC 8693 à portée atténuée (RAR), preuve de possession et escalade hors bande OpenID CIBA.](figures/fig-30-a-1.svg)

### Anatomie du flux d’échange RFC 8693 à délégation explicite

En mode délégation (section 30.2), la RFC 8693 distingue le `subject_token`, qui représente la chaîne d’autorité courante jusqu’au sujet initial, de l’`actor_token`, ou de l’assertion client JWT-SVID, qui prouve l’identité de l’agent demandeur.

À chaque saut $i$, l’agent appelant contacte le STS (*Security Token Service*), serveur d’autorisation de l’entreprise ou Entra ID, avant d’invoquer un pair A2A ou un serveur MCP :

1.  **Authentification sans secret de l’agent appelant.** L’agent s’authentifie auprès du point de terminaison `/token` en présentant son JWT-SVID SPIFFE frais par `client_assertion` (RFC 7523).
2.  **Jeton amont et restriction par RAR.** L’agent fournit dans `subject_token` le jeton reçu à l’entrée, désigne l’audience (`audience`) unique du prochain destinataire et précise la restriction des droits par `authorization_details` (RFC 9396, section 30.3). Une chaîne comme `sap.spare_parts.reserve` ignore les paramètres métiers. Un objet structuré `authorization_details` permet d’encoder dans le jeton signé que l’agent aval ne peut réserver qu’une seule unité de la pièce ROTOR-KIT-HX9 pour le dossier SN-WO-773190, sous un plafond de 5 000 \$ CAD.
3.  **Liaison à la clé de l’agent et garde-fous anti-rejeu.** L’agent joint un en-tête DPoP (RFC 9449, section 29.5), signé avec une clé privée asymétrique générée en mémoire non exportable, ou présente son certificat X.509-SVID en mTLS. Le STS inscrit l’empreinte SHA-256 de la clé publique dans la revendication `cnf` (*Confirmation*) et impose un plafond de profondeur de délégation (`max_act_depth <= 4`). À l’appel de l’outil MCP, la passerelle vérifie que la preuve DPoP lie la méthode HTTP (`htm`), l’URI exacte sans paramètres de requête (`htu`), le condensat du jeton d’accès (`ath`) et un défi serveur frais (DPoP-Nonce), avec un cache anti-rejeu sur `jti`. Un jeton ou une preuve interceptés dans un journal restent inexploitables ailleurs.

#### Extrait 30.2 — Requête HTTP d’échange RFC 8693 + RAR + DPoP et jeton JWT résultant

La requête est émise au saut n° 2 par l’*Agent Spécialiste Garantie* de BCA, qui s’apprête à invoquer le serveur MCP adossé à Guidewire et IBM i. Elle est suivie de la charge utile décodée du jeton T2 que le STS délivre :

``` http
POST /oauth2/v2.1/token HTTP/1.1
Host: sts.identity.boreal.ca
Content-Type: application/x-www-form-urlencoded
DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0...

grant_type=urn:ietf:params:oauth:grant-type:token-exchange
&client_id=agent-bca-warranty-adjudicator-prod
&client_assertion_type=
  urn:ietf:params:oauth:client-assertion-type:jwt-bearer
&client_assertion=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI...
&subject_token=eyJhbGciOiJFUzI1NiIsInR5cCI6ImF0K2p3dCJ9.eyJzdW...
&subject_token_type=urn:ietf:params:oauth:token-type:access_token
&audience=mcp://gateway.boreal.ca/mcp/bca-guidewire-contracts
&scope=bca.warranty.preauthorize
&authorization_details=[{"type": "boreal_warranty_adjudication",
  "actions": ["preauthorize_claim"], "equipmentSerial": "BOR-CMP-90441",
  "maxAmountCad": 4500.00, "sagaId": "saga-inc-2027-088412"}]
```

``` json
{
  "iss": "https://sts.identity.boreal.ca",
  "sub": "emp-8841-marc.lavoie@boreal.ca",
  "aud": "mcp://gateway.boreal.ca/mcp/bca-guidewire-contracts",
  "iat": 1773588420,
  "exp": 1773588720,
  "jti": "tok-t2-9f81c3a4-7b2e-4d19-8a50-62e41c90b312",
  "client_id": "agent-bca-warranty-adjudicator-prod",
  "ent_sponsor": "emp-1042-claire.desjardins@boreal.ca",
  "scope": "bca.warranty.preauthorize",
  "act": {
    "sub": "spiffe://boreal.ca/ns/bca-prod/sa/warranty-adjudicator-v2",
    "blueprint_id": "bp-bca-warranty-tier2",
    "act": {
      "sub": "spiffe://boreal.ca/ns/bsn-prod/sa/maint-orchestrator-v4",
      "blueprint_id": "bp-bsn-orchestrator-tier2"
    }
  },
  "authorization_details": [
    {
      "type": "boreal_warranty_adjudication",
      "actions": ["preauthorize_claim"],
      "equipmentSerial": "BOR-CMP-90441",
      "maxAmountCad": 4500.00,
      "sagaId": "saga-inc-2027-088412"
    }
  ],
  "cnf": {
    "jkt": "0ZcOCORZNYy-DWpqq30jZyJGHTN0d2HglBV3uiguA4I",
    "x5t#S256": "bwcK0esc3ACC3DB2Y5_lESsXE8o9ltc05O89jdN-dg2"
  }
}
```

Ce jeton `at+jwt` (RFC 9068) tient en un bloc signé de moins de deux kilo-octets et vaut exactement cinq minutes (`exp - iat = 300`). Le serveur MCP destinataire y vérifie l’employé initiateur (`sub`), le responsable hiérarchique de l’agent (`ent_sponsor`), le plafond financier autorisé (4500.00 CAD sur le seul équipement BOR-CMP-90441) et la preuve que la connexion provient du conteneur attesté (`cnf`). Il y lit aussi les acteurs antérieurs (`act` imbriqué); selon la RFC 8693, ils sont informatifs et n’entrent pas dans la décision d’accès, et l’orchestrateur consigne la chaîne (section 30.2).

### Approbation asynchrone hors bande par OpenID CIBA pour l’escalade HOTL

Quand le devis estimé de réparation atteint 7 850 \$ CAD, il excède le plafond autonome L3 de 5 000 \$ CAD codé dans le Blueprint de l’agent. L’agent s’exécute en arrière-plan, dans un travailleur Temporal, sans navigateur ouvert : il ne peut pas rediriger (HTTP 302) vers une mire de connexion. Envoyer un simple lien cliquable par courriel ou par clavardage exposerait l’organisation à l’hameçonnage interne et à l’approbation inattentive.

CIBA, le flux d’authentification par canal secondaire d’OpenID (section 30.4), sépare l’approbation de la session de l’agent, dans le temps et dans le canal. Aucun standard ne couvre pourtant l’attestation de présence humaine : CIBA ne prévoit qu’une demande lancée par le client, et la confirmation en cours d’exécution appelle une spécification supplémentaire (section 30.4). La séquence suivante n’est donc pas un profil normalisé :

1.  **Demande signée.** L’agent, ou le moteur d’orchestration qui agit comme client confidentiel attesté, soumet une requête signée au point de terminaison `/bc-authorize` du fournisseur d’identité. Elle désigne le groupe de souscripteurs habilités, un jeton de notification à usage unique (`client_notification_token`), un message de liaison lisible (`binding_message`) et le condensat cryptographique exact de la transaction proposée (`tx_hash`).
2.  **Veille durable.** Le moteur durable met l’activité en veille persistante (`awakeable`, ou attente d’un signal webhook en mode CIBA *Ping*/*Push*), sans consommer de fil CPU pendant les minutes ou les heures d’attente.
3.  **Signature locale.** Sur le téléphone corporatif sécurisé d’un souscripteur admissible, l’application d’authentification affiche les paramètres clés de l’engagement (montant, bénéficiaire, écart détecté) et exige une signature biométrique locale FIDO2, par clé d’accès, liée au condensat `tx_hash`.
4.  **Séparation des tâches.** Le fournisseur d’identité vérifie une règle de séparation des tâches (SoD) : l’approbateur CIBA ne doit être ni le sujet initiateur `sub` du flux, ni le développeur qui a déployé l’agent. Il notifie ensuite l’orchestrateur et émet un jeton d’approbation à usage unique, verrouillé sur cette seule transaction.

#### Extrait 30.3 — Coordinateur TypeScript d’approbation hors bande OpenID CIBA avec contrôle SoD

Le coordinateur lance la demande CIBA, attend le rappel, récupère les jetons, puis vérifie la séparation des tâches, l’assurance d’authentification et le condensat de la transaction :

``` typescript
import { createHash, randomBytes } from "node:crypto";
import { jwtVerify, createRemoteJWKSet } from "jose";

export interface HighValueClaimIntent {
  readonly sagaId: string;
  readonly initiatingSubjectId: string;
  readonly equipmentSerial: string;
  readonly amountCad: number;
  readonly beneficiaryVendorId: string;
}

export interface VerifiedCibaApproval {
  readonly approvalJti: string;
  readonly approverSubjectId: string;
  readonly transactionHash: string;
  readonly scopedAccessToken: string;
}

const JWKS = createRemoteJWKSet(
  new URL("https://sts.identity.boreal.ca/.well-known/jwks.json")
);

export function computeCanonicalTxHash(intent: HighValueClaimIntent): string {
  const canonical = JSON.stringify({
    amountCad: intent.amountCad.toFixed(2),
    beneficiaryVendorId: intent.beneficiaryVendorId,
    equipmentSerial: intent.equipmentSerial,
    initiatingSubjectId: intent.initiatingSubjectId,
    sagaId: intent.sagaId,
  });
  return createHash("sha256").update(canonical, "utf8").digest("base64url");
}

export async function initiateAndVerifyCibaStepUp(
  intent: HighValueClaimIntent,
  spiffeClientAssertion: string,
  waitForPingCallback: (
    authReqId: string,
    expectedNotificationToken: string,
    timeoutMs: number
  ) => Promise<void>
): Promise<VerifiedCibaApproval> {
  const txHash = computeCanonicalTxHash(intent);
  const shortCode = txHash.slice(0, 6).toUpperCase();
  const notificationToken = randomBytes(24).toString("base64url");
  const amtStr = intent.amountCad.toFixed(2);

  // 1. Initiation hors bande sur le point CIBA signé avec JWT-SVID (mode Ping)
  const initUrl = "https://sts.identity.boreal.ca/openid/ciba/bc-authorize";
  const initRes = await fetch(initUrl, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: "agent-bca-warranty-adjudicator-prod",
      client_assertion_type:
        "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: spiffeClientAssertion,
      client_notification_token: notificationToken,
      login_hint_token: "role:bca-senior-underwriter-l4",
      scope: "openid bca.warranty.approve_high_value",
      binding_message:
        `BCA-${shortCode} : Autoriser ${amtStr} CAD (${intent.equipmentSerial})`,
      request_context: JSON.stringify({ tx_hash: txHash, saga_id: intent.sagaId }),
      requested_expiry: "14400", // Fenêtre SLA de 4 heures maximum
    }),
  });

  if (!initRes.ok) {
    throw new Error(`Échec d'initiation CIBA : HTTP ${initRes.status}`);
  }
  const { auth_req_id, expires_in } = (await initRes.json()) as {
    auth_req_id: string;
    expires_in: number;
  };

  // 2. Mise en veille durable sans scrutation active (validation du jeton Ping)
  await waitForPingCallback(auth_req_id, notificationToken, expires_in * 1000);

  // 3. Récupération du jeton après signature FIDO2 du souscripteur
  const tokenRes = await fetch("https://sts.identity.boreal.ca/oauth2/v2.1/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "urn:openid:params:grant-type:ciba",
      auth_req_id,
      client_id: "agent-bca-warranty-adjudicator-prod",
      client_assertion_type:
        "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
      client_assertion: spiffeClientAssertion,
    }),
  });

  if (!tokenRes.ok) {
    throw new Error(`Approbation CIBA refusée ou expirée : HTTP ${tokenRes.status}`);
  }
  const { id_token, access_token } = (await tokenRes.json()) as {
    id_token: string;
    access_token: string;
  };

  // 4. Vérification cryptographique d'intégrité et de séparation des tâches (SoD)
  const { payload } = await jwtVerify(id_token, JWKS, {
    issuer: "https://sts.identity.boreal.ca",
    audience: "agent-bca-warranty-adjudicator-prod",
  });

  const approverSub = String(payload.sub ?? "");
  const approvedTxHash = String(payload.tx_hash ?? "");
  const amr = Array.isArray(payload.amr) ? payload.amr : [];

  if (!approverSub || approverSub === intent.initiatingSubjectId) {
    throw new Error(
      "Violation critique SoD : l'approbateur CIBA doit différer de l'initiateur."
    );
  }
  if (!amr.includes("hwk") && !amr.includes("fido")) {
    throw new Error("Assurance insuffisante : signature matérielle FIDO2 exigée.");
  }
  if (approvedTxHash !== txHash) {
    throw new Error("Intégrité rompue : condensat tx_hash divergent.");
  }

  return {
    approvalJti: String(payload.jti),
    approverSubjectId: approverSub,
    transactionHash: txHash,
    scopedAccessToken: access_token,
  };
}
```

### Gouvernance du cycle de vie des identités NHI d’agents

Les comptes d’employés suivent les processus d’embauche et de départ. Les identités d’agents prolifèrent au rythme des déploiements CI/CD, et sans gouvernance du cycle de vie les identités orphelines s’accumulent en quelques trimestres (section 29.2). Le tableau définit la norme opérationnelle en six phases.

| Phase du cycle de vie | Événement déclencheur | Contrôles obligatoires d’ingénierie et IGA | Indicateur / SLA de conformité |
|:---------------------|:----------------------|:---------------------------------|:-----------------------|
| 1. Conception & Blueprint | Création d’une nouvelle classe d’agent (L1–L4) | Définition du plafond $M(a_i)$, affectation de deux parrains humains (Workday), revue BSIF E-23 | Zéro *Blueprint* sans parrain actif ni cote d’autonomie |
| 2. Amorçage attesté | Déploiement CI/CD signé (Sigstore) en cluster | Vérification du condensat OCI par SPIRE, fédération FIC sans secret vers Entra Agent ID | 0 secret statique stocké en variable ou volume |
| 3. Exécution & Rotation | Activité opérationnelle nominale | Rotation automatique des SVID aux 15 min, échange RFC 8693 par saut (TTL $\le 5\,\text{min}$), liaison DPoP/mTLS | 100 % d’appels MCP mutatifs sous jeton contraint |
| 4. Revue périodique | Échéance mensuelle ou dérive télémétrique | Analyse d’écart entre portées accordées au Blueprint et portées réellement utilisées | Élagage automatique des portées inutilisées après 30 jours |
| 5. Quarantaine d’urgence | Alerte SOC (ASI01/ASI10) ou départ du parrain | Révocation instantanée du `ClusterSPIFFEID` + signal OpenID CAEP vers agentgateway | Blocage effectif multi-régions en $< 2\,\text{s}$ |
| 6. Décommissionnement | Retrait d’une version ou fin de programme | Suppression des FIC, révocation des W3C VC externes, scellement WORM des journaux sur 7 ans | Zéro identité NHI dormante active au-delà de 14 jours |

---

## 30.10 Application au fil rouge et éclairages sectoriels

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Refonte IAM sur Microsoft Entra Agent ID et SPIRE pour tracer chaque chaîne de délégation**
:::

**Situation de départ (T4 2026)** : L’audit déclencheur du chapitre 1 a porté sur les 47 initiatives agentiques du Groupe Boréal (14 500 employés, 6,8 G\$ CAD). L’équipe de sécurité a découvert 19 agents non déclarés et un incident majeur : un assistant interne utilisait un jeton de compte de service partagé (`svc-copilot-hr-fin`), doté d’un droit de lecture élargi sur Workday et Snowflake, ce qui exposait potentiellement les dossiers médicaux d’invalidité d’employés québécois (risque de sanction sévère sous la Loi 25). Sur le cœur patrimonial IBM i (AS/400) de Boréal Capital & Assurances (BCA), toutes les requêtes automatisées arrivaient sous un profil générique unique, QUSERAPI, ce qui interdisait toute démonstration de séparation des tâches devant les inspecteurs du BSIF.

**Architecture déployée (T1–T2 2027)** :

1.  **Suppression des secrets statiques par SPIRE hybride.** L’équipe plateforme déploie un plan de contrôle SPIRE fédéré, qui couvre les clusters Kubernetes infonuagiques (AKS Canada Central pour BSN) et les nœuds Linux sur site proches des usines BEL et du système central BCA. Les 28 classes d’agents homologuées reçoivent chacune un `ClusterSPIFFEID` verrouillé sur le condensat SHA-256 de leur image conteneur signée en CI/CD.
2.  **Gouvernance par Microsoft Entra Agent ID.** Chaque classe d’agent est déclarée comme *Agent Identity Blueprint*, rattaché par *Federated Identity Credential* à l’émetteur OIDC de SPIRE, avec un double parrainage obligatoire (un directeur métier divisionnaire et un architecte responsable). Les clés d’API des 19 agents non conformes sont coupées à la passerelle réseau.
3.  **Pont d’audit patrimonial vers IBM i (DB2 for i).** L’obstacle technique le plus redouté chez BCA était de préserver la chaîne RFC 8693 devant un AS/400 trentenaire, qui ignore tout d’OAuth 2.1. L’équipe encapsule les programmes RPG dans un serveur MCP dédié, placé derrière agentgateway. Ce serveur vérifie le jeton `at+jwt` contraint par mTLS, puis appelle, à l’ouverture de chaque transaction DB2, la procédure système `QSYS2.SET_CLIENT_INFO` avec `CLIENT_USERID = sub` (l’employé initiateur), `CLIENT_APPLNAME = act.sub` (l’identifiant SPIFFE de l’agent) et `CLIENT_ACCTNG = jti` (l’identifiant unique du jeton et de l’approbation CIBA). Les journaux natifs immuables QAUDJRN de l’IBM i reflètent ainsi toute la chaîne agentique, sans qu’une seule ligne de COBOL ou de RPG métier soit réécrite.

**Résultats mesurés après 90 jours** :

- **Secrets statiques et clés d’API de comptes d’agents en production** : passage de 64 secrets dispersés à 0.
- **Réduction de la surface de permissions active par appel** : -94 % en moyenne grâce à l’atténuation RFC 8693 + RAR par équipement et par dossier.
- **Latence additionnelle mesurée par saut d’échange STS + vérification DPoP** : 6,8 ms au 95e centile (négligeable devant les 400 à 1 800 ms d’inférence modèle), avec validation sans réserve lors du pré-audit BSIF E-23 d’avril 2027.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur Financier — Piste d'audit nominative exigée par BSIF E-23 et séparation des tâches (SoD) cryptographique**
:::

Pour les institutions financières fédérales canadiennes soumises à la ligne directrice BSIF E-23 au 1er mai 2027 (ainsi qu’aux contrôles internes SOX 404 et DORA en Europe), la gouvernance du risque de modèle ne s’arrête pas à la qualité statistique des prédictions. Elle exige une preuve opposable de l’attribution des décisions et de l’inviolabilité des délégations de pouvoirs financiers.

Dans une chaîne d’indemnisation d’assurance ou de restructuration de prêt outillée par des agents, trois invariants cryptographiques doivent pouvoir être reconstitués après coup devant un auditeur externe, pour toute écriture comptable :

1.  **Non-répudiation tripartite.** Le journal immuable (WORM, rétention minimale de 7 ans) lie, dans un même enregistrement signé, le sujet initiateur (`sub`), la version exacte du Blueprint et du modèle qui a formulé la proposition (`act` + attributs OpenTelemetry `gen_ai.request.model`) et, au-delà du seuil autonome, l’identité humaine distincte qui a apposé sa signature matérielle FIDO2 par CIBA.
2.  **Séparation des tâches cryptographique, entre agents et entre humain et agent.** Comme un analyste crédit ne peut approuver son propre décaissement, un *Agent Critique* (Archétype 5), chargé de contrôler la conformité d’un dossier instruit par un *Agent Spécialiste* (Archétype 2), doit posséder un SPIFFE ID distinct et un Blueprint distinct, et ne partager aucun jeton d’état mutable avec l’agent évalué. Le STS refuse d’émettre un jeton de décaissement final si la revendication `act` ne contient pas les deux attestations indépendantes ou un jeton CIBA d’un supérieur habilité.
3.  **Revalidation de fraîcheur après mise en veille (T4).** Quand une instruction de sinistre suspendue plusieurs jours se réveille, tout jeton antérieur est échu. Le STS réévalue en temps réel le statut actif de l’initiateur et du parrain dans l’annuaire avant d’accorder un nouveau mandat RFC 8693.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Santé & Secteur Public (Loi 25 / RGPD) — Finalité déclarée, minimisation des portées et expiration stricte sur données personnelles**
:::

Dans les réseaux hospitaliers, les organismes publics et toute entreprise qui traite des renseignements personnels sensibles au sens de la Loi 25 québécoise ou de l’article 9 du RGPD, l’accès légitime à une donnée dépend de sa finalité déclarée. Un agent administratif mandaté pour planifier un rendez-vous d’imagerie n’a aucun motif légal de lire les notes psychiatriques du dossier patient, même s’il interroge le même serveur FHIR encapsulé en MCP.

Utiliser des objets `authorization_details` (RFC 9396) dans l’échange RFC 8693 permet d’encoder obligatoirement un attribut normalisé `purposeOfUse` (par exemple `urn:oid:2.16.840.1.113883.5.8#APPT` en santé, ou un code du registre de consentement Loi 25). Le serveur MCP en aval refuse tout champ hors du périmètre strictement nécessaire à cette finalité, masque dynamiquement les identifiants directs avant le retour au contexte du LLM quand l’opération ne les requiert pas, et interdit structurellement d’émettre un jeton de rafraîchissement (`refresh_token`) sur des portées qui touchent aux renseignements personnels.
::::

---

## 30.11 Décision d’architecture normative et points de contrôle

L’ADR suivant va au-delà de ce que retient l’exposé. Il exige l’empilement de `act`, la RFC 9396 à chaque saut et CIBA pour toute approbation asynchrone, alors que les acteurs antérieurs de la RFC 8693 sont informatifs (section 30.2), qu’aucun profil n’applique la RFC 9396 aux agents (section 30.3) et que CIBA ne prévoit qu’une demande lancée par le client (section 30.4).

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-018 — Identité NHI unique par classe d'agent et échange de jetons RFC 8693 à portée atténuée à chaque saut**
:::

- **Statut** : Acceptée \| Périmètre : Identité IAM & confiance zéro \| Révision : Semestrielle
- **Contexte** : L’exécution de processus métiers transversaux par des flottes d’agents autonomes asynchrones rend caducs l’emprunt de jetons interactifs humains (sur-privilégiation, perte d’audit, échec hors ligne) comme les comptes de service partagés (vulnérabilité du délégué confus, secrets statiques exposés).
- **Options évaluées** :
  1.  *Clés d’API par agent stockées dans un coffre-fort central* : Elles isolent mieux qu’un compte unique, mais restent des secrets statiques exportables, perdent l’identité de l’utilisateur initiateur (`sub`) et n’atténuent pas les droits par tâche. Rejetée.
  2.  *Propagation du jeton utilisateur OAuth initial à travers la chaîne* : Elle préserve `sub`, mais viole le moindre privilège, empêche l’isolation par audience et échoue dès que la saga dépasse la durée de session interactive. Rejetée.
  3.  *Attestation de charge de travail SPIFFE/SPIRE fédérée à l’annuaire NHI (Entra Agent ID), échange obligatoire RFC 8693 + RAR à chaque saut avec jetons contraints (DPoP/mTLS), et escalade asynchrone OpenID CIBA* : Retenue.
- **Décision** : (a) Tout agent de niveau L1 à L4 reçoit un Blueprint nominatif, avec un parrain humain actif, et s’authentifie exclusivement par SVID éphémère (`TTL <= 15 min`), sans aucun secret persistant; (b) tout franchissement de frontière A2A ou MCP exige un échange RFC 8693 qui produit un jeton `at+jwt` (`TTL <= 5 min`) d’audience unique, contraint cryptographiquement (`cnf`), qui préserve `sub`, empile `act` et restreint les paramètres sensibles par la RFC 9396; (c) toute approbation humaine sur un flux asynchrone passe par OpenID CIBA, avec une signature matérielle FIDO2 liée au condensat `tx_hash`.
- **Conséquences** :
  - *Positives* : Suppression des secrets statiques d’agents, confinement du rayon d’impact à la sous-tâche courante, conformité native aux audits BSIF E-23 et Loi 25, prise en charge des sagas multi-jours.
  - *Négatives / Coûts assumés* : Exploitation d’une infrastructure SPIRE à haute disponibilité, latence réseau marginale de 4 à 8 ms par saut d’échange STS, et mise à niveau des serveurs MCP patrimoniaux pour qu’ils inspectent les revendications `sub`, `act` et `authorization_details`.
- **Condition de révision** : Révision semestrielle, alignée sur les travaux du groupe de travail OAuth de l’IETF sur les profils de délégation agentique native.
::::

### Liste de contrôle de mise en production

Avant qu’un agent ou un serveur MCP franchisse l’étape d’homologation sécurité en production, chacun des huit points suivants doit être validé :

1.  **Zéro secret statique.** L’agent démarre-t-il et s’authentifie-t-il auprès du STS exclusivement par une identité attestée SPIFFE (JWT-SVID ou X.509-SVID), sans clé d’API ni mot de passe stocké en variable d’environnement, fichier de configuration ou image conteneur ?
2.  **Parrainage nominatif actif.** L’*Agent Identity Blueprint* possède-t-il un propriétaire métier et un responsable technique actifs dans le SIRH, avec suspension automatique programmée en cas d’orphelinat ?
3.  **Interdiction du relais de jeton.** La passerelle agentgateway et chaque serveur MCP rejettent-ils systématiquement (HTTP 401/403) tout jeton dont la revendication `aud` ne désigne pas explicitement et uniquement leur propre URI canonique ?
4.  **Atténuation monotone et RAR.** Chaque saut de délégation RFC 8693 réduit-il l’ensemble des portées au strict nécessaire et borne-t-il les montants, quantités ou identifiants d’objets critiques dans `authorization_details` (RFC 9396) ?
5.  **Preuve de possession active (`cnf`).** Les jetons d’accès émis pour des opérations L2+ sont-ils liés cryptographiquement à la clé éphémère de l’agent, par mTLS (RFC 8705) ou DPoP (RFC 9449), avec une vérification anti-rejeu du `jti` ?
6.  **Traçabilité `sub` + `act` jusqu’au disque.** Les connecteurs vers les systèmes d’enregistrement (y compris patrimoniaux) propagent-ils le sujet initial (`sub`) et la chaîne d’acteurs (`act`) jusque dans les journaux d’audit applicatifs et les bases de données ?
7.  **Intégrité transactionnelle CIBA et SoD.** Pour toute escalade HOTL, la signature FIDO2 porte-t-elle sur le condensat SHA-256 exact des paramètres de l’action, en interdisant à l’initiateur d’approuver sa propre transaction ?
8.  **Fédération B2B révocable.** Si l’agent interagit avec des partenaires externes par A2A, ses attestations W3C DID / VC 2.0 comportent-elles une échéance courte et une liste de révocation `BitstringStatusList` vérifiée à chaque session ?
