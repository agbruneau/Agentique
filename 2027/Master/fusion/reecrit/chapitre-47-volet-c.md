## Mise en œuvre — Volants d'inertie cognitifs, compilation de consignes et distillation LLM → SLM {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Au lancement d’un processus agentique, un grand modèle de raisonnement frontière (l’enseignant) permet d’atteindre vite le seuil de fiabilité métier. Laisser 100 % du trafic répétitif de production sur ce modèle, avec des prompts écrits à la main, a deux conséquences : un coût structurel qui pèse sur le coût par résultat, et des prompts fragiles à chaque changement de modèle. L’avantage cumulatif de 2027 tient à la conversion des traces d’exécution validées en petits modèles spécialisés internes (SLM).
- **Décisions architecturales structurantes** :
  1.  *Irréversible en ingénierie cognitive* : Remplacer la rédaction manuelle des prompts par la compilation déclarative de programmes cognitifs (paradigme DSPy : optimiseurs bayésiens de signatures et de démonstrations), évaluée contre la suite $\tau$-bench du domaine.
  2.  *Structurante pour l’économie d’échelle* : Opérer une boucle de données gouvernée (anonymisation irréversible Loi 25, filtrage anti-ASI06) qui distille périodiquement les trajectoires réussies de l’enseignant et les corrections contrastives des superviseurs HOTL vers des SLM d’entreprise (3B–8B, par SFT + DPO sur adaptateurs LoRA).
  3.  *Gouvernance du cycle de vie* : Ne promouvoir un SLM distillé sur agentgateway que si sa constance $\text{pass}^5$ sur le jeu de réserve scellé atteint au moins 99 % de celle de l’enseignant, avec une route d’escalade vers l’enseignant pour les entrées hors distribution.
- **Indicateurs de gouvernance** : Baisse du coût par résultat sur 4 trimestres (cible -65 % à -85 %), ratio de parité $\text{pass}^5_{\text{SLM}} / \text{pass}^5_{\text{Teacher}}$ ($\ge 0{,}99$), zéro fuite de PII mémorisée aux tests d’extraction par canaris sur les poids affinés, et baisse de la latence p95 (-60 % à -75 %).
::::

## 47.18 Des traces aux jeux d’entraînement : signal de sélection et sas d’assainissement

Croisées avec le dénouement des sagas métiers et les décisions des superviseurs humains, les traces de production forment un corpus propre à l’entreprise, que la boucle de données (47.7) transforme en exemples.

### Ancrer la sélection dans l’issue métier

Les sorties brutes d’un modèle plus grand conduisent l’élève à l’effondrement de modèle et amplifient ses biais. Seules les sorties vérifiées entrent dans le jeu d’entraînement (47.8) : la vérification vient de l’issue métier, non du jugement du modèle. Deux sources la fournissent :

1.  **Trajectoires positives certifiées par la saga.** Une trace multi-tours (OpenTelemetry `gen_ai.*`, chapitre 33) n’entre dans le candidat d’entraînement supervisé (SFT) que si la saga durable correspondante a atteint son état terminal d’affaires vérifié, sans action de compensation ultérieure, sans réouverture de billet client dans les quatorze jours et sans violation de garde-fou Cedar.
2.  **Paires préférentielles issues du poste HOTL.** Quand un superviseur humain HOTL (chapitre 41) rejette ou corrige la proposition $y_{\text{rejeté}}$ d’un agent au profit d’une décision amendée $y_{\text{choisi}}$ sur le même contexte $x$, le système capture sans coût supplémentaire un triplet $(x, y_{\text{choisi}}, y_{\text{rejeté}})$, exploitable directement par la DPO.

![Architecture du volant d’inertie cognitif (Data Flywheel) : collecte OTel et corrections HOTL, sas d’assainissement Loi 25, compilation déclarative + distillation LoRA et courbe économique trimestrielle.](figures/fig-47-c-1.svg)

### Le sas d’assainissement

Un contexte de session se purge par clé d’entité (chapitre 14). Un renseignement personnel inscrit dans les poids d’un modèle affiné ne s’en retire pas sans réentraînement complet : le droit à l’effacement (RGPD art. 17, Loi 25) est alors violé, et un risque d’exfiltration entre clients apparaît. Avant d’entrer dans l’entrepôt d’exemples validés, chaque trace traverse trois filtres bloquants :

- **Finalité et consentement.** Sont exclus tout locataire B2B dont le contrat ODRL (chapitre 45) comporte la clause `aiTrainingProhibited`, ainsi que les dossiers visés par une opposition au profilage.
- **Désidentification irréversible.** Les noms de personnes, numéros d’assurance sociale, coordonnées bancaires, plaques et numéros de contrat sont remplacés par des entités synthétiques de même distribution linguistique. Des canaris synthétiques y sont injectés pour vérifier, après l’entraînement, que le taux d’extraction par mémorisation reste nul (47.7).
- **Filtre anti-empoisonnement (OWASP ASI06).** Toute session qui a déclenché une alerte du détecteur d’injection de prompt, ou dont les entrées externes contiennent des instructions anormales, est écartée. Aucune porte dérobée ne doit être distillée dans le futur SLM interne.

------------------------------------------------------------------------

## 47.19 Compilation déclarative des consignes

Avant tout affinage, la première économie vient des prompts. Un prompt monolithique de trois cents lignes, rédigé à la main, ne survit pas au remplacement d’un modèle frontière par un SLM ni à une nouvelle version du modèle (chapitre 46).

### Séparer la signature de sa mise en œuvre compilée

Selon le paradigme de DSPy et des compilateurs déclaratifs d’agents, le développeur ne rédige plus le texte final du prompt. Il déclare en code typé :

1.  La signature entrée/sortie et les invariants métiers, par exemple `DiagnosticVibratoire(spectre_fft, historique_pannes) -> cause_racine_ossie, urgence_l0_l4, outil_mcp_recommande`.
2.  La topologie modulaire du sous-graphe : chaîne de raisonnement bornée, vérification d’assertions déterministes.
3.  La fonction objectif à maximiser sur le banc d’évaluation de développement, par exemple l’exactitude sémantique pondérée sous contrainte de budget de jetons.

Un optimiseur automatique, tel que MIPROv2 (47.7) ou la recherche évolutionnaire contrainte, explore l’espace des instructions concises. Il retient dans le jeu d’exemples validés les 3 à 5 démonstrations qui maximisent le score $\text{pass}^5$ pour le couple tâche et modèle cible. Changer de modèle ne demande plus trois semaines de réécriture à la main, mais une recompilation automatisée de deux heures en CI/CD.

#### Extrait 47.8 — Signature cognitive déclarative et métrique de compilation composite (declarative_compile_spec.py)

Le contrat typé remplace le texte figé, et la fonction de récompense pénalise à la fois l’erreur métier et l’inflation de jetons :

``` python
from dataclasses import dataclass

@dataclass(frozen=True)
class TriageSignatureSpec:
    input_fields: tuple[str, ...] = (
        "fft_harmonics_json",
        "asset_ossie_class",
        "recent_maintenance_summary",
    )
    output_fields: tuple[str, ...] = (
        "failure_mode_code",
        "autonomy_tier_required",
        "recommended_mcp_tool",
    )
    max_compiled_prefix_tokens: int = 850

def composite_compile_score(
    pred_code: str,
    gold_code: str,
    pred_tool: str,
    gold_tool: str,
    prompt_tokens: int,
    token_budget: int = 850,
) -> float:
    if pred_code != gold_code or pred_tool != gold_tool:
        return 0.0
    over = max(0, prompt_tokens - token_budget)
    brevity_bonus = max(0.0, 1.0 - (over / 500.0))
    return 0.90 + 0.10 * brevity_bonus
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Propriété intellectuelle et contrats fournisseurs — titularité juridique des poids LoRA distillés**
:::

Deux précautions contractuelles conditionnent la légalité d’une boucle de distillation :

1.  **Conditions d’utilisation de l’enseignant.** Certains fournisseurs d’API propriétaires restreignent l’usage de leurs sorties pour entraîner un modèle commercial concurrent généraliste. Les contrats d’entreprise négociés et les grands modèles à poids ouverts sous licence permissive (Apache 2.0, MIT) autorisent la distillation interne à des fins métier. Le Centre d’Excellence vérifie la licence de l’enseignant avant d’activer la collecte de traces SFT, comme le demande 47.8.
2.  **Cloisonnement entre clients dans les offres SaaS B2B.** Un éditeur SaaS, comme la division BSN de Boréal, ne distille un adaptateur partagé entre clients que sur des grandeurs physiques anonymisées, et seulement si ses contrats B2B l’y autorisent. Pour les grands comptes à clause de confidentialité stricte, un adaptateur LoRA dédié par locataire (40 Mo chiffrés sous clé client) préserve l’étanchéité de la propriété intellectuelle.
::::

------------------------------------------------------------------------

## 47.20 Distillation continue LLM → SLM : rentabilité, service multi-adaptateurs et dérive

Quand le volume d’un flux stabilisé dépasse quelques dizaines de milliers d’exécutions par mois, la compétence compilée se transfère de l’enseignant (70B à \> 400B paramètres) vers un élève spécialisé (3B à 8B paramètres), servi à haute densité sur l’infrastructure de l’entreprise (47.8).

### Pourquoi un petit modèle suffit sur une tâche bornée

Dans une cellule agentique bien découpée (chapitre 17 et chapitre 5 : au plus douze outils MCP cohérents et un domaine ontologique Apache Ossie précis), l’entropie fonctionnelle réelle est beaucoup plus basse que ce que couvre un modèle frontière généraliste. Un élève 8B distillé peut y égaler ou surpasser un modèle géant.

La recette de 47.8 prend ici les volumes suivants : SFT sur 2 000 à 15 000 trajectoires validées et compilées, DPO sur 500 à 2 000 corrections contrastives HOTL, au moyen d’adaptateurs de rang faible (LoRA / QLoRA, rang $r \in \{16, 32, 64\}$).

### Rentabilité et routage selon l’incertitude

La distillation a un coût fixe d’entraînement et de validation $C_{\text{distill}}$, amorti sur le volume mensuel d’exécutions $V$. Dans une cascade, l’élève examine d’abord chaque requête au coût $c_S \ll c_T$, résout directement la part $\alpha \in [0, 1]$ du flux et n’escalade que la fraction $(1 - \alpha)$ vers l’enseignant, au coût $c_T$. Le coût unitaire moyen est $c_S + (1 - \alpha) c_T$. Le seuil mensuel de rentabilité nette $V_{\min}$ vérifie :

$$V \cdot (\alpha c_T - c_S) > \frac{C_{\text{distill}}}{M_{\text{amort}}} \iff V_{\min} = \frac{C_{\text{distill}}}{M_{\text{amort}} \cdot (\alpha c_T - c_S)}$$

Avec des paramètres typiques en 2027 ($C_{\text{distill}} = 900$ \$ CAD, GPU et CI inclus; durée de vie $M_{\text{amort}} = 3\text{ mois}$ avant rafraîchissement; $c_T = 0{,}042$ \$ CAD; $c_S = 0{,}003$ \$ CAD; $\alpha = 0{,}82$), le point mort est franchi dès $V_{\min} \approx 9\,540$ exécutions par mois, soit un peu plus de trois cents dossiers par jour. Au-delà, chaque million de transactions économise plus de 31 400 \$ CAD et divise par quatre le TTFT.

Pour ne pas sacrifier la qualité sur les cas inédits (nouveau produit, clause juridique atypique), agentgateway maintient une cascade à rejet d’incertitude. L’alignement DPO tend à resserrer la distribution des log-probabilités (resserrement de l’entropie). Après l’affinage, un facteur de température de Platt est donc réétalonné sur le jeu de développement (15 %), et le seuil d’entropie $\tau_H$ est fixé par prédiction conforme. Si l’entropie calibrée des jetons structurels dépasse $\tau_H$, ou si le validateur de préconditions signale un cas hors distribution, la requête est rejouée de façon transparente vers l’enseignant en moins de 300 ms. Sa résolution alimente le prochain cycle trimestriel de distillation.

Les chiffres du tableau suivant illustrent une cible de conception : selon la section 47.8, la recette Multi-LoRA (SFT + DPO) compose des briques sourcées séparément et reste à valider, et aucune mesure n'a été lue sur un élève distillé par cette recette.

| Critère opérationnel | 100 % modèle frontière (enseignant) | SLM générique nu (sans distillation) | Cascade SLM LoRA distillé (85 %) + enseignant (15 %) |
|:--------------------------|:----------------------|:-----------------------|:----------------------------|
| Constance $\text{pass}^5$ ($\tau$-bench métier) | 97,4 % (référence) | 71,8 % *(insuffisant en L3)* | 97,2 % (parité préservée) |
| Latence p95 par tour d’outil | 2 450 ms | 340 ms | 490 ms (-80 %) |
| Coût moyen pour 1 000 résultats | 42,00 \$ CAD | 3,10 \$ CAD *(mais échecs coûteux)* | 9,40 \$ CAD (-77,6 % net) |
| Souveraineté et exécution en périphérie | Dépend d’une API ou d’un gros cluster | Possible mais peu fiable | Exécutable localement sur 1 GPU ou en périphérie |

#### Extrait 47.9 — Pipeline déclaratif de curation, distillation LoRA et porte de promotion $\text{pass}^5$ (flywheel_distill_gate.py)

Ce portier valide, avant d’enregistrer un nouvel adaptateur LoRA en production, l’absence de mémorisation de PII, la parité $\text{pass}^5$ sur le jeu de réserve scellé (*holdout*) et le gain économique :

``` python
from dataclasses import dataclass

@dataclass(frozen=True)
class DistillationCandidateMetrics:
    adapter_id: str
    teacher_holdout_pass5: float
    student_holdout_pass5: float
    canary_pii_memorization_hits: int
    asi06_adversarial_bypass_rate: float
    p95_latency_ms: int
    estimated_cost_saving_ratio: float

def evaluate_slm_promotion_gate(
    m: DistillationCandidateMetrics,
) -> tuple[bool, str]:
    if m.canary_pii_memorization_hits > 0:
        return (False, "BLOCK_LAW25_PII_MEMORIZATION_DETECTED")

    if m.asi06_adversarial_bypass_rate > 0.005:
        return (False, "BLOCK_SECURITY_REGRESSION_ASI06")

    if m.teacher_holdout_pass5 <= 0:
        return (False, "INVALID_TEACHER_BASELINE")

    parity = m.student_holdout_pass5 / m.teacher_holdout_pass5
    if parity < 0.99:
        reason = f"BLOCK_PASS5_PARITY_LOW:{parity:.4f}<0.9900"
        return (False, reason)

    low_saving = m.estimated_cost_saving_ratio < 0.40
    if low_saving or m.p95_latency_ms > 900:
        return (False, "BLOCK_INSUFFICIENT_EFFICIENCY_GAIN")

    return (True, f"PROMOTE_CANARY_10PCT:{m.adapter_id}")
```

### Dérive du modèle et décommissionnement

Un SLM spécialisé reste efficace tant que le monde métier ressemble à sa distribution d’entraînement. Il vieillit dès qu’une nouvelle réglementation fiscale ou une nouvelle gamme de machines apparaît. Deux mécanismes détectent et corrigent cette dérive :

1.  **Échantillonnage sentinelle de 2 % vers l’enseignant.** Même après la promotion, agentgateway route en ombre 2 % des requêtes vers le modèle frontière de référence, pour mesurer l’écart de décision en conditions réelles. Quand le taux d’accord glissant sur sept jours fléchit de plus de 1,5 point, une alerte déclenche une recompilation et une redistillation sur les données fraîches, et relève temporairement le seuil de repli vers l’enseignant. Le ratio de la porte de promotion et ce taux d’accord situent l’élève par rapport à l’enseignant, ce qui va au-delà de ce que retient la section 47.8 : l’élève s’y mesure sur le banc interne du chapitre 33, pas contre l’enseignant, dont il hérite les erreurs.
2.  **Date de péremption des adaptateurs (TTL de 90 à 180 jours).** Inscrit au registre des agents (chapitre 34), tout adaptateur LoRA non réhomologué sur le jeu de réserve actualisé à son échéance semestrielle est décommissionné automatiquement au profit du palier supérieur.

### Test d’exposition des canaris

Pour prouver au responsable de la protection des renseignements personnels (Loi 25) qu’un adaptateur distillé n’a mémorisé aucune séquence nominative susceptible d’être restituée à un autre utilisateur, le pipeline applique la méthode d’exposition différentielle de Carlini (47.7). À la constitution du jeu d’entraînement assaini, le sas insère $K = 200$ chaînes secrètes synthétiques uniques, au format exact d’un identifiant sensible (par exemple POLICE-CANARI-9481-7720).

Une fois l’affinage SFT + DPO achevé, le vérificateur compare la log-vraisemblance (perplexité) que l’élève assigne à ces 200 canaris vus à l’entraînement à celle de 10 000 canaris témoins jamais présentés. Si le rang de vraisemblance d’un seul canari d’entraînement se distingue statistiquement des témoins (exposition $> \tau_{\text{mem}}$), ou si un décodage glouton préfixé complète un seul chiffre exact, la régularisation (dropout LoRA, écrêtage de la norme du gradient de type SGD à confidentialité différentielle, ou déduplication accrue) est jugée insuffisante. L’artefact de poids est alors détruit automatiquement, avant toute copie hors du bac d’entraînement. Ce protocole va au-delà de ce que retient la section 47.7 : un canari y est une séquence artificielle unique glissée dans le jeu d’entraînement, dont on mesure l’exposition dans le modèle, et la publication est bloquée s’il ressort; le résumé seul de l’article de Carlini ne décrit ni les canaris ni la métrique d’exposition; ces éléments proviennent du texte complet de l’article, recoupé par extraits le 14 novembre 2026, et le nombre de canaris et de témoins, le seuil et le décodage ne sont décrits dans aucune source lue.

### Service multi-adaptateurs à haute densité et dimensionnement VRAM

L’économie ne vient pas seulement de la petite taille de l’élève (8B contre 400B), mais aussi de la mutualisation des adaptateurs en mémoire graphique (VRAM). Un seul modèle de base 8B, chargé une fois, sert dans un même lot vingt adaptateurs métiers de quelques dizaines de mégaoctets chacun, sans coût de commutation. Vingt conteneurs GPU séparés pour vingt agents spécialisés laisseraient 85 % des unités de calcul inactives aux heures creuses de chaque division.

Grâce aux noyaux CUDA/Triton de multiplication matricielle groupée hétérogène (S-LoRA / Punica, intégrés nativement à vLLM et SGLang), un serveur à deux cartes de 80 Go garde un seul tronc gelé $W_0$ en précision FP8 (\~8,5 Go). Il applique à la volée, requête par requête dans le même lot continu, le couple d’adaptateurs de bas rang $\Delta W_m = B_m A_m$ propre à la route métier $m$. L’empreinte mémoire totale pour héberger $M$ adaptateurs actifs simultanés de rang $r$ sur $L$ couches de dimension $d$ est :

$$M_{\text{VRAM}}^{\text{total}} = M_{\text{tronc}}(W_0) + M_{\text{KV-cache}} + \sum_{m=1}^{M} 2 \, L \, N_{\text{proj}} \, d \, r \, b_{\text{octets}}$$

Pour un modèle 8B ($L = 32$, $N_{\text{proj}} = 4$, $d = 4096$, $r = 32$, FP16 à $b = 2\text{ octets}$), chaque adaptateur métier complet pèse 67 Mo. Héberger simultanément en VRAM chaude trente spécialistes n’occupe que 2,0 Go et laisse plus de 140 Go au KV-cache partagé. Le serveur absorbe des centaines de requêtes concurrentes avec un TTFT médian inférieur à 90 ms.

Le cycle d’un adaptateur couvre un trimestre :

| Phase trimestrielle du cycle LoRA | Volume minimal requis | Action automatisée du pipeline ADLC | Garde-fou de sécurité et de réversibilité |
|:----------------------|:---------------------|:----------------------------|:---------------------------|
| 1. Collecte et assainissement (J+1 à J+75) | $\ge 2\,500$ sagas réussies + paires HOTL | Filtrage ODRL, désidentification Loi 25 + injection de 200 canaris | Rejet de toute session ayant levé une alerte ASI01/ASI06 |
| 2. Compilation et affinage (J+76 à J+80) | Jeu partitionné 70 / 15 / 15 | Optimisation MIPROv2, puis SFT + DPO au rang `r = 32` | Test d’exposition de Carlini (0 mémorisation tolérée) |
| 3. Recette et déploiement canari (J+81 à J+90) | Suite $\tau$-bench de réserve scellée | Porte $\text{pass}^5 \ge 99\,\%$ de l’enseignant, puis trafic `10 % → 100 %` | Adaptateur N-1 conservé en VRAM pour un retour arrière en moins de `5 s` |
| 4. Exploitation et extinction (J+91 à J+180) | Trafic nominal en cascade | Sentinelle en ombre de 2 % vers l’enseignant; révocation à l’échéance du TTL | Repli transparent vers l’enseignant si l’entropie dépasse 0,42 |

#### Extrait 47.10 — Règle de routage en cascade à rejet d’entropie et sentinelle 2 % (cascade-flywheel-route.yaml)

Cette configuration d’agentgateway exécute le trafic nominal sur l’adaptateur distillé, bascule vers l’enseignant en cas d’incertitude et mesure la dérive en continu :

``` yaml
apiVersion: gateway.aaif.linuxfoundation.org/v1
kind: CognitiveCascadeRoute
metadata:
  routeId: "boreal-warranty-triage-cascade-v3"
spec:
  studentTier:
    baseModel: "boreal-base-8b-fp8"
    loraAdapter: "warranty-triage-lora-2027q4"
    maxTokenEntropyThreshold: 0.42
    requireValidMcpSchemaDecode: true
  teacherFallbackTier:
    modelAlias: "frontier-reasoning-tier1"
    triggerOnEntropyExceed: true
    triggerOnOodDetectorScoreAbove: 0.78
  continuousDriftSentinel:
    shadowSampleRatioToTeacher: 0.02
    rollingWindowDays: 7
    minAgreementRateBeforeRetrainAlert: 0.985
    adapterHardExpirationUtc: "2028-03-31T23:59:59Z"
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur financier (BSIF E-23) et santé — gouvernance du risque de modèle pour des adaptateurs distillés fréquents**
:::

Comment concilier un cycle trimestriel ou mensuel d’affinage LoRA avec la validation indépendante des modèles qu’exigent BSIF E-23 ou les référentiels cliniques ? L’erreur consiste à traiter chaque rafraîchissement d’adaptateur comme un système inédit soumis à six mois de comité manuel. Les institutions matures font homologuer chaque année, par la seconde ligne de défense, l’usine de distillation elle-même et ses bornes d’acceptation (*Predetermined Change Control Plan*, inspiré du cadre PCCP des autorités médicales). Tant que le tronc de base, la taxonomie d’outils MCP, le test de canaris nul et la parité $\text{pass}^5 \ge 99\,\%$ sur le jeu de réserve gouverné par la fonction Risque sont respectés et consignés dans un registre de lignage immuable (`Dataset Hash -> LoRA SHA-256 -> Rapport τ-bench`), la promotion par déploiement canari se fait sans gel bureaucratique.
::::

------------------------------------------------------------------------

## 47.21 Application au fil rouge : distillation des huit flux majeurs chez Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : baisse de 68 % du coût par résultat des huit flux majeurs par compilation DSPy et Multi-LoRA**
:::

**Chantier d’optimisation T2–T4 2027** : Une fois la fiabilité fonctionnelle et réglementaire acquise sur ses 11 sagas transversales, la cellule FinOps IA du *Hub* Boréal (chapitre 40 et chapitre 41) a constaté que 8 flux à haute fréquence (triage vibratoire BSN, qualification de garantie BCA, rapprochement documentaire d’expédition BEL, extraction d’avenants, routage multilingue de billets, normalisation de la nomenclature Apache Ossie, pré-diagnostic SRE et classification douanière) représentaient 84 % de la consommation totale de jetons du groupe.

**Mise en œuvre de la boucle** :

1.  **Sas d’assainissement certifié Loi 25.** 190 000 trajectoires positives validées par Temporal et 6 400 arbitrages contrastifs issus des consoles HOTL ont été anonymisés, avec injection de 500 canaris synthétiques (0 mémorisation détectée à l’audit).
2.  **Compilation déclarative, puis Multi-LoRA sur 4 GPU internes.** Une première passe d’optimisation automatique des signatures a réduit de 38 % la taille des préfixes de prompts et augmenté la réutilisation du KV-cache. Une seconde passe d’affinage SFT + DPO a produit 8 adaptateurs LoRA, servis simultanément sur le même modèle de base 8B, qui alimente aussi, en version quantifiée INT4, les boîtiers de périphérie miniers du chapitre 46.

**Impact consolidé vérifié sur l’exercice** :

- **Parité de fiabilité intacte.** Le score moyen $\text{pass}^5$ sur les 8 suites $\tau$-bench passe de 97,1 % (modèle frontière initial, prompt manuel) à 97,6 % avec une cascade de 86 % de SLM LoRA et 14 % d’enseignant.
- **Baisse de 68 % du coût par résultat moyen sur ces 8 flux** (de 0,91 \$ CAD en début d’année à 0,29 \$ CAD au quatrième trimestre, ce qui ramène la moyenne globale du groupe à 0,41 \$ CAD). Elle dégage 1,45 M\$ CAD de marge additionnelle, qui autofinance l’ensemble du Centre d’Excellence Agentique.
::::

------------------------------------------------------------------------

## 47.22 Décision d’architecture normative, conclusion générale et points de contrôle

La décision ADR-031, la trente et unième et dernière, clôt le registre architectural du compendium. Selon la section 47.8, la recette qu’elle retient reste une cible de conception à valider.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-031 — Compilation déclarative des consignes et volant de distillation continue LLM → SLM sous sas anti-PII et porte pass\^5**
:::

- **Statut** : Acceptée \| Périmètre : Plateforme IA, FinOps et cycle de vie des modèles \| Révision : Semestrielle
- **Contexte** : Maintenir des prompts fragiles écrits à la main et exécuter indéfiniment des volumes répétitifs élevés sur des modèles frontières généralistes expose l’entreprise à des coûts unitaires prohibitifs, à une latence élevée et à des régressions à chaque changement de modèle.
- **Options évaluées** :
  1.  *Statu quo sur modèles frontières externes avec optimisation manuelle ponctuelle des prompts* : Rejetée — non compétitive économiquement à grande échelle et dépendante d’un savoir-faire artisanal non reproductible.
  2.  *Pré-entraînement maison d’un modèle fondationnel propriétaire à partir de zéro* : Rejetée — coût en capital GPU sans avantage mesurable face à la distillation ciblée de modèles à poids ouverts de pointe.
  3.  *Compilation programmatique des signatures cognitives (type DSPy) couplée à un cycle trimestriel de distillation SFT + DPO par adaptateurs LoRA sur traces assainies, protégé par une porte de parité $\text{pass}^5 \ge 99\,\%$ et une cascade à rejet d’incertitude*. Retenue.
- **Décision** : (a) Versionner les agents sous forme de signatures compilables plutôt que de prompts monolithiques figés; (b) interdire tout entraînement sur des traces brutes non purgées de PII (Loi 25), de clauses ODRL restrictives ou d’alertes ASI06; (c) conditionner la promotion de tout SLM distillé à la parité $\text{pass}^5$ sur le jeu de réserve scellé, assortie d’un échantillonnage sentinelle continu de 2 % vers l’enseignant et d’une date d’expiration de l’adaptateur.
- **Conséquences** : Avantage économique et de latence cumulatif d’un trimestre à l’autre et souveraineté accrue sur les poids spécialisés, en contrepartie d’une gouvernance stricte des jeux d’entraînement et du pipeline MLOps/AgentOps d’affinage.
::::

### Conclusion des parties I à IX

Une conviction d’ingénierie traverse les protocoles, les théorèmes de fiabilité et les garde-fous du compendium : la performance durable de l’entreprise agentique ne vient pas d’un abandon des garanties déterministes au profit d’un modèle réputé omniscient. Elle vient de l’encastrement de l’intelligence probabiliste dans les fondations éprouvées des systèmes distribués, de la cryptographie, du droit positif et de la responsabilité humaine.

Dans le système d’information, cette architecture sépare l’accès vertical aux outils (MCP) de la coopération horizontale entre pairs (A2A v1.0, AGNTCY), ancre le sens métier dans des couches sémantiques et bi-temporelles explicites (Apache Ossie, Graphiti), confie les mutations longues à des moteurs durables (Temporal, Restate), atténue cryptographiquement chaque saut d’identité (SPIFFE, OAuth 2.1 OBO) et protège le discernement de l’opérateur humain (HOTL). Aux frontières de l’organisation, puis dans l’usine logicielle interne, elle fédère les partenaires B2B sans exposer les marges (EDC / ODRL, vLEI, AP2), garantit la souveraineté cognitive et la survie hors ligne (TEE, Cognitive DR, CRDT, Simplex ROS 2), modernise le patrimoine sous oracle (Agentic SDLC, ODCS) et distille ses propres traces vers de petits modèles (DSPy, Multi-LoRA). Toutes ces briques obéissent à une même règle d’urbanisation : chaque erreur stochastique inévitable doit être localisée, observable, réversible et bornée économiquement.

D’ici 2030, l’avantage ira aux organisations qui auront bâti cette architecture ouverte, frugale, souveraine et gouvernée par des humains, plutôt qu’à celles qui auront multiplié les démonstrateurs sans contrôle ou différé l’action par crainte réglementaire.

| Domaine | Invariant architectural | Standard ou mécanisme pivot |
|:--------------------------|:-----------------------------------------|:-------------------------------|
| Fondations | Séparer le contrôle d’état déterministe du raisonnement stochastique | Maturité N1–N5, loi de Lusser |
| Protocoles ouverts | Découpler outils verticaux, pairs horizontaux et règlement B2B | MCP, A2A v1.0, AGNTCY, AG-UI, AP2 |
| Sémantique et mémoire | Unifier le sens métier et la validité bi-temporelle des faits | Apache Ossie, graphes Graphiti |
| Orchestration durable | Exiger idempotence et sagas à compensation sur toute mutation | Temporal / Restate, agentgateway |
| Intégration SI réel | Fédérer les jardins SaaS et valider l’OT sur jumeau numérique | OPC UA, CUA transitoire encadré |
| Identité et sécurité | Imposer une NHI atténuée à chaque saut et des garde-fous hors LLM | SPIFFE, OAuth 2.1 OBO, Cedar, OpenSandbox |
| AgentOps et FinOps | Piloter par constance $\text{pass}^k$ et coût par résultat vérifié | OTel `gen_ai.*`, $\tau$-bench, KV-cache |
| Droit et modèle HOTL | Préserver le discernement humain actif et l’opposabilité légale | BSIF E-23, Loi 25, EU AI Act, Hub & Spoke |
| B2B, souveraineté et périphérie | Collaborer sans livrer ses secrets et survivre aux coupures réseau | EDC/ODRL, vLEI, TEE, CRDT, Simplex |
| Ingénierie et distillation | Prouver le code par l’oracle et distiller les traces vers des SLM | Agentic SDLC, ODCS, DSPy, Multi-LoRA |

### Liste de contrôle de mise en production

1.  **Signal d’ancrage métier vérifié** : La boucle ne retient-elle que les traces de sagas terminées avec succès, sans compensation ni litige en aval, complétées par les paires contrastives HOTL ?
2.  **Sas d’assainissement Loi 25 et ODRL** : Les traces d’entraînement excluent-elles les partenaires opposés par contrat et subissent-elles une désidentification irréversible, validée par l’injection de canaris contre la mémorisation ?
3.  **Filtrage anti-empoisonnement (ASI06)** : Toute trace soupçonnée d’injection indirecte, ou rejetée par une politique Cedar, est-elle écartée du corpus de distillation ?
4.  **Étanchéité du jeu de réserve scellé** : Les 15 % de scénarios d’homologation finale sont-ils disjoints des données d’affinage LoRA et de la sélection d’exemples DSPy ?
5.  **Signatures cognitives compilables** : Les prompts des agents critiques sont-ils générés et optimisés par programme contre une métrique explicite, plutôt que figés à la main ?
6.  **Porte de parité $\text{pass}^5 \ge 99\,\%$** : Le pipeline bloque-t-il automatiquement tout élève qui dégrade de plus de 1 % la constance multi-essais de l’enseignant ?
7.  **Cascade à rejet d’entropie sur agentgateway** : Les requêtes ambiguës ou hors distribution sont-elles rejouées vers l’enseignant, sans échec visible pour l’utilisateur ?
8.  **Sentinelle 2 % et péremption d’adaptateur** : Un échantillonnage continu en ombre surveille-t-il la dérive réelle du SLM, avec expiration obligatoire de l’adaptateur à six mois ?
