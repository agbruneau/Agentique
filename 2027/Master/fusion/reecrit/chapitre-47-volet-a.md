## Mise en œuvre — Usine logicielle agentique (Agentic SDLC) et modernisation assistée du patrimoine {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : En 2027, des flottes asynchrones d’agents logiciels qui ouvrent des demandes de tirage remplacent l’autocomplétion individuelle en IDE et multiplient par cinq le débit d’écriture. Le goulot se déplace vers la vérification d’exactitude, la sécurité et la cohérence architecturale. Sur les cœurs patrimoniaux (IBM i RPG, COBOL/CICS, PL/SQL), sans tests unitaires et dont la documentation a vingt ans de retard, une réécriture générative directe (« Big Bang IA ») oublie les règles fiscales ou actuarielles implicites enfouies dans les cas limites historiques.
- **Décisions architecturales structurantes** :
  1.  *Irréversible en gouvernance d’ingénierie* : Séparer les devoirs dans l’usine logicielle. L’agent qui écrit le code, dans un espace de travail isolé (OpenSandbox et `git worktree`), ne peut ni modifier le harnais de tests d’acceptation ni approuver sa propre fusion. La fusion exige des portes déterministes sans IA (typage, tests de mutation, SAST) et une revue contradictoire par un modèle d’une autre famille.
  2.  *Structurante pour l’extinction de la dette CUA (chapitre 25)* : Moderniser le patrimoine par le figuier étrangleur neuro-symbolique, qui combine un graphe d’appel statique exact (AST, et index SCIP là où un indexeur existe; section 47.2), des oracles de caractérisation (*Golden Master*) tirés de transactions historiques réelles et une exécution en miroir (*Shadow Mirroring*) d’au moins un cycle d’affaires complet avant la bascule (cible de trente jours, sans source : section 47.4).
- **Indicateurs de gouvernance** : Score de mutation minimal sur le code modifié, calibré par module ($\ge 85\,\%$ de mutants tués, seuil sans source; section 47.3); écart toléré en exécution en miroir financière (0,00 \$ CAD sur $\ge 100\,000$ transactions); taux de régression après déploiement (\< 0,5 %); nombre d’écrans CUA retirés au profit de serveurs MCP natifs.
::::

## 47.9 Topologie d’une usine logicielle agentique : séparation des devoirs, graphes AST/SCIP et revue contradictoire

Accélérer la production de code sans accélérer la preuve de sa justesse engorge les ingénieurs seniors de revues. Quand un même modèle écrit une fonction métier et le test qui la valide, il reproduit la même erreur des deux côtés de l’assertion : la suite est 100 % verte et fausse (47.1).

### Ancrer l’exploration du dépôt dans un graphe symbolique exact (AST / SCIP / LSP)

Dans un monoréférentiel ou un parc de microservices de dix millions de lignes, la recherche vectorielle par similarité lexicale ramène des fonctions au nom voisin et manque l’appelant indirect qui passe par une interface générique ou un déclencheur SQL. L’AST et l’index SCIP, décrits à la section 47.2, évitent ce défaut.

L’usine ancre donc toute exploration sur un index sémantique déterministe, exposé en lecture par un serveur MCP dédié qui interroge l’AST (Tree-sitter), le protocole LSP et un graphe SCIP inter-dépôts. Avant d’écrire une ligne, l’agent planificateur extrait la fermeture transitive des appelants, les schémas Protobuf/OpenAPI touchés et les propriétaires CODEOWNERS concernés.

![Architecture de l’usine logicielle Agentic SDLC et modernisation patrimoniale Strangler Fig : extraction AST/SCIP, séparation bâtisseur/oracle/critique et bascule Shadow Mirroring.](figures/fig-47-a-1.svg)

### Quatre rôles dotés de droits d’écriture distincts

La section 47.1 propose deux rôles à droits distincts, spécificateur et bâtisseur, qu’elle présente comme une extrapolation à valider; le passage de l’un à l’autre y est un point d’approbation humaine (chapitre 22). L’usine en compte quatre et place la signature humaine à la fusion, non entre la spécification et la construction : ce découpage va au-delà de ce que retient l’exposé et reste à valider. Pour appliquer au génie logiciel la séparation des tâches du chapitre 30, l’orchestrateur durable (Temporal) découpe toute tâche d’ingénierie entre quatre acteurs dotés de jetons et de systèmes de fichiers distincts :

1.  **L’agent spécificateur et auteur d’oracle (écriture : uniquement `/specs` et `/tests/acceptance`)** : À partir du billet d’exigence et de l’ontologie Apache Ossie, il rédige les invariants formels, les tests par propriétés (Hypothesis, `proptest`) et les cas limites d’acceptation. Il ne voit jamais le code d’implémentation candidat.
2.  **L’agent bâtisseur en bac à sable isolé (écriture : uniquement `/src` et `/tests/unit`, dans un `git worktree` éphémère sous OpenSandbox)** : Sans accès libre à Internet, il tire ses paquets d’un dépôt interne approuvé, ce qui pare le Slopsquatting : l’hallucination d’un nom de bibliothèque que l’attaquant a piégé (risque OWASP ASI04). Il itère jusqu’à satisfaire le compilateur et l’oracle, en lecture seule.
3.  **Le portier déterministe sans IA (pipeline CI immuable)** : Aucun avis de modèle ne contourne les six portes binaires : compilation sans avertissement, typage statique strict, analyse statique de sécurité (SAST) et détection de secrets, vérification de licence et SBOM, exécution de l’oracle d’acceptation, tests de mutation. Ces derniers (47.3) sont ciblés de façon incrémentale sur les nœuds AST touchés par le différentiel, avec élagage statique des mutants sémantiquement équivalents, pour tenir le cycle CI sous six minutes. Ils injectent des centaines de micro-altérations syntaxiques (\> changé en \>=, négation d’une garde, suppression d’un arrondi) et exigent que la suite échoue sur au moins 85 % des mutants, ce qui mesure la densité réelle des assertions. Ce seuil n’a pas de source : la section 47.3 ne le retient comme barrière de fusion que calculé sur le code modifié, calibré par module à partir du score observé avant l’arrivée des agents et débarrassé des mutants équivalents reconnus.
4.  **L’agent critique contradictoire, puis le mainteneur humain** : Un modèle juge avec indulgence son propre style syntaxique. Pour briser ce biais, la revue automatisée de sécurité, de concurrence et de maintenabilité est confiée à un modèle d’une famille architecturale distincte de celle du bâtisseur. L’ingénieur humain signataire reçoit ensuite un dossier condensé de preuves.

| Garde-fou de l’usine | Défaut neutralisé | Mécanisme d’application |
|:-------------------------|:----------------------------------|:----------------------------------------|
| Cloisonnement oracle et bâtisseur | Tests tautologiques qui codent le même bogue que le code | Droits ACL Git refusant à l’identité NHI du bâtisseur toute écriture sous `tests/acceptance/` |
| Miroir interne de paquets scellé | Hallucination de paquets (Slopsquatting, OWASP ASI04) | Aucune sortie vers `npm`/PyPI/`crates.io` publics; proxy interne à liste blanche SBOM |
| Seuil de tests de mutation (cible de $\ge 85\,\%$, calibrée par module) | Couverture de lignes trompeuse, sans assertions métier fortes | Exécution bloquante de `cargo-mutants`, Stryker ou `mutmut` dans le pipeline |
| Critique hétérogène et signature humaine | Angles morts partagés par une même famille de poids; perte de maîtrise | Modèle critique distinct; fusion sur `main` protégée par la signature GPG/SSH d’un ingénieur |

### Pilotage par des métriques DORA adaptées aux agents

Le nombre de demandes de tirage ouvertes ou de lignes générées par semaine ne mesure pas l’usine : un agent non bridé écrit dix mille lignes verbeuses en une heure et ralentit pourtant la mise en production sûre. Quatre indicateurs couplés pilotent l’usine :

1.  **Temps de cycle net jusqu’à fusion vérifiée** : Durée totale, revue humaine et portes de mutation comprises. Si elle augmente alors que la génération s’accélère, les lots soumis par les agents sont trop volumineux : ils se bornent à $\le 250$ lignes modifiées par demande de tirage atomique.
2.  **Taux d’échec post-changement et survie du code à 30 jours** : Part du code généré par agent qui doit être réécrite ou annulée dans le mois suivant sa mise en production (seuil d’alerte : \> 8 %).
3.  **Densité d’invariants formels par millier de lignes** : Rapport entre les assertions de propriétés et les tests de caractérisation d’une part, le volume de code applicatif de l’autre.
4.  **Coût complet d’ingénierie par point fonctionnel modernisé** : Somme des jetons d’analyse, de l’exécution OpenSandbox de compilation et de mutation et du temps de l’architecte validateur, rapportée au service patrimonial effectivement éteint.

### Propriétés universelles contre le sur-apprentissage

Un oracle d’acceptation de dix exemples fixes (`input -> output`) reste vulnérable au sur-apprentissage, même séparé du bâtisseur : un agent qui lit les messages d’échec du pipeline peut spécialiser ses branchements sur ces cas ponctuels sans respecter la loi du domaine.

L’agent spécificateur exprime donc les invariants métier en propriétés universelles (Hypothesis en Python, `proptest` en Rust, `fast-check` en TypeScript). À chaque exécution CI dans le répertoire verrouillé `/tests/acceptance`, le moteur génère des milliers de combinaisons aléatoires ou adverses aux frontières (montants nuls, années bissextiles, taux extrêmes) et réduit tout contre-exemple au cas minimal reproductible.

#### Extrait 47.1 — Harnais d’invariants algébriques en lecture seule pour l’agent bâtisseur (lease_invariants_test.py)

L’agent d’oracle rédige seul ce harnais, que protège une ACL Git. Il vérifie le déterminisme, la conservation comptable au centime et la monotonie actuarielle sur des milliers de tirages :

``` python
from decimal import Decimal
from hypothesis import given, strategies as st

cents = st.decimals(
    min_value=Decimal("100.00"),
    max_value=Decimal("500000.00"),
    places=2,
    allow_nan=False,
    allow_infinity=False,
)
rates = st.decimals(
    min_value=Decimal("0.0000"),
    max_value=Decimal("0.1500"),
    places=4,
    allow_nan=False,
    allow_infinity=False,
)
months = st.integers(min_value=1, max_value=84)

def make_oracle_suite(calc_fn):
    @given(
        principal=cents,
        rem_months=months,
        rebate_rate=rates,
    )
    def test_buyout_algebraic_laws(
        principal: Decimal,
        rem_months: int,
        rebate_rate: Decimal,
    ) -> None:
        q1 = calc_fn(principal, rem_months, rebate_rate)
        q2 = calc_fn(principal, rem_months, rebate_rate)
        # 1. Déterminisme pur et échelle au centime exact
        assert q1 == q2
        assert q1.total_payout.as_tuple().exponent == -2
        # 2. Identité comptable exacte sans perte d'arrondi
        expected = (
            q1.principal_balance
            - q1.actuarial_rebate
            + q1.provincial_tax
        )
        assert q1.total_payout == expected
        # 3. Monotonie temporelle de la remise actuarielle
        if rem_months > 1:
            q_next = calc_fn(
                principal, rem_months - 1, rebate_rate
            )
            assert (
                q1.actuarial_rebate >= q_next.actuarial_rebate
            )

    return test_buyout_algebraic_laws
```

------------------------------------------------------------------------

## 47.10 Modernisation du patrimoine (RPG, COBOL, PL/SQL) : extraction neuro-symbolique et figuier étrangleur

Le chapitre 25 pose qu’un agent CUA qui pilote un écran vert 5250/3270 est un pont tactique transitoire, jamais une cible. Reste à moderniser le cœur : 1,5 million de lignes RPG ILE sur IBM i (AS/400), ou COBOL/CICS sur z/OS, qui calculent chaque nuit au centime près des amortissements de crédit-bail, des retenues fiscales interprovinciales et des réserves actuarielles. Le figuier étrangleur est décrit au chapitre 25, l’exécution en miroir (*Shadow Mirroring* dans les extraits et l’ADR) à la section 47.4. Pour COBOL et RPG, la liste d’indexeurs SCIP lue ne compte aucun indexeur : l’index vient de l’outillage de l’éditeur ou n’existe pas (section 47.2). Aucune source lue ne traite RPG : l’application à ce langage est une extrapolation (section 47.4).

### Pourquoi la traduction directe par un LLM échoue sur les systèmes centraux

Demander à un grand modèle de traduire un programme COBOL de 8 000 lignes en service Go ou Rust échoue pour trois raisons :

- **L’arithmétique décimale fixe et les arrondis bancaires implicites** : Une division intermédiaire en décimal condensé (COMP-3 / `PACKED(15:4)` en RPG), tronquée à la quatrième décimale, ne donne pas sur trente-six mensualités le même résultat qu’un flottant IEEE 754 (`float64`). Il en résulte des écarts d’arrondi en audit financier.
- **Le couplage par zones mémoire partagées et fichiers physiques** : Les règles métier sont réparties entre des structures d’inclusion (COPYBOOK, `/COPY`), des indicateurs numériques conditionnels (`*IN01` à `*IN99`), des tables de paramètres DB2 et des lots nocturnes CL/JCL.
- **Les bogues historiques devenus fonctionnalités contractuelles** : Des exceptions codées en dur en 2004 reflètent des avenants contractuels toujours en vigueur, absents de tout cahier des charges écrit.

### La méthode en quatre phases

L’usine combine analyse statique formelle et synthèse bornée par un agent pour remplacer le système central brique par brique :

1.  **Découpage par domaine selon le graphe d’accès aux tables** : Un parseur grammatical déterministe (ANTLR / Tree-sitter spécialisé RPG/COBOL) construit le graphe biparti $\mathcal{G} = (P, T, E)$ qui relie chaque programme $p \in P$ aux tables physiques DB2 $t \in T$ qu’il lit ou modifie. Un algorithme de partitionnement isole les sous-graphes à couplage minimal (par exemple *Calcul de rachat anticipé de bail* ou *Vérification de plafond de garantie*), extractibles en serveur MCP autonome.
2.  **Oracle de caractérisation (*Golden Master*) de 10 000 à 100 000 cas réels** : Avant d’écrire une ligne du nouveau service, on rejoue ou l’on capture, par journalisation non intrusive, un échantillon stratifié d’entrées et de sorties historiques de production, anonymisées si nécessaire. Un solveur de contraintes (Z3) y ajoute des cas synthétiques aux frontières, à partir des conditions de branchement extraites de l’AST patrimonial. Ce jeu immuable sert de référence du comportement fonctionnel.
3.  **Synthèse du service moderne en arithmétique décimale exacte, exposé par MCP** : L’agent bâtisseur traduit les règles extraites vers une spécification lisible, alignée sur Apache Ossie, et vers un service à typage fort qui n’emploie que des types décimaux à précision fixe (`rust_decimal`, aucun flottant binaire). Le service est enveloppé dans un serveur MCP Streamable HTTP doté de clés d’idempotence.
4.  **Validation par exécution en miroir avant la bascule** : Déployé derrière un réplicateur de trafic en production pendant au moins un cycle d’affaires complet, clôture périodique comprise (section 47.4), le nouveau service exécute chaque requête réelle en parallèle du programme IBM i, qui reste maître, sans commettre ses écritures. Un comparateur enregistre le taux de concordance exacte :

$$\Delta_{\text{shadow}} = \sum_{k=1}^{N} \mathbb{I}\!\left(\,\bigl\lVert y_k^{\text{moderne}} - y_k^{\text{legacy}} \bigr\rVert_{\infty} > 0\,\right) = 0 \quad \text{sur } N \ge 100\,000$$

Toute divergence ($\Delta_{\text{shadow}} > 0$) renvoie le cas discordant dans l’oracle de l’usine, pour affiner la règle avant qu’un client réel soit touché. Les trente jours et l’écart de 0,00 \$ sont des cibles de conception sans source (section 47.4) : l’écart nul se défend, la durée se discute, car trente jours couvrent une fin de mois, pas une fin d’exercice. Chaque écart ignoré est une décision signée, pas un réglage de l’agent. Une fois le zéro écart tenu sur un cycle complet, le trafic bascule progressivement (`5 % → 50 % → 100 %`), avec une réplication inverse CDC de repli. Le robot CUA d’écran vert peut alors être désactivé définitivement.

#### Extrait 47.2 — Contrat de pipeline Agentic SDLC imposant séparation des devoirs et parité *Golden Master* (sdlc-modernization-gate.yaml)

Ce descripteur bloque la promotion d’un module modernisé tant que les portes déterministes et l’exécution en miroir ne sont pas validées :

``` yaml
apiVersion: sdlc.boreal.ca/v2027.1
kind: AgenticModernizationPipeline
metadata:
  moduleId: "bca-lease-early-buyout-calc"
  legacySource: "QRPGLESRC/LEASBUY400"
  targetLanguage: "rust-2024-decimal-strict"
spec:
  segregationOfDuties:
    specAgentNhi: "spiffe://boreal.ca/sdlc/spec-oracle-writer"
    builderAgentNhi: "spiffe://boreal.ca/sdlc/rust-builder"
    criticModelFamily: "heterogeneous-distinct-from-builder"
    forbidBuilderWritePaths:
      - "specs/**"
      - "tests/golden_master/**"
      - ".github/workflows/**"
  deterministicGates:
    forbidBinaryFloatsInDomain: true
    minMutationKillScore: 0.88
    goldenMasterCorpusSize: 50000
    maxAllowedCentDeviationCad: "0.00"
    networkEgressSandbox: "INTERNAL_ARTIFACTORY_ONLY"
  stranglerCutoverPolicy:
    minShadowMirrorDays: 30
    minShadowTransactions: 100000
    requiredExactMatchRate: 1.000000
    requireHumanPrincipalEngineerSignoff: true
```

------------------------------------------------------------------------

## 47.11 Sécurité du code généré et comparateur de parité en miroir

Le code que les agents produisent à grande vitesse présente, même sous tests fonctionnels, deux risques que les revues classiques sous-estiment : des vulnérabilités subtiles de concurrence ou d’injection (OWASP ASI05) et une dérive silencieuse sur des états transitoires de base de données que la seule réponse HTTP ne reflète pas.

Le comparateur ne s’en tient donc pas au corps JSON renvoyé à l’appelant. Il compare l’intention complète d’écriture transactionnelle (lignes comptables du grand livre, codes de taxes ventilés TPS/TVQ/TVH, événements émis) dans un mode d’essai à blanc isolé, et mesure l’écart de latence p99. La section 47.4 borne la technique : sûre seulement pour du code qui ne modifie pas de données, elle recommande pour les écritures d’écrire dans les deux systèmes puis de comparer à la lecture et, sur un traitement par lots, d’exécuter les deux systèmes sur le même fichier d’entrée en rapprochant les sorties enregistrement par enregistrement. Le mode d’essai à blanc décrit ici est une variante propre à ce volet, que cette section ne décrit pas.

#### Extrait 47.3 — Comparateur déterministe de parité *Shadow Mirroring* entre IBM i et service MCP moderne (shadow_parity_judge.py)

Exécuté de façon asynchrone, hors du chemin critique de latence client, ce juge compare champ par champ les résultats décimaux et alimente la suite de non-régression en cas d’écart :

``` python
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class BuyoutQuoteResult:
    contract_id: str
    principal_balance: Decimal
    actuarial_rebate: Decimal
    provincial_tax: Decimal
    total_payout: Decimal
    ledger_codes: tuple[str, ...]

def verify_shadow_parity(
    tx_id: str,
    legacy: BuyoutQuoteResult,
    modern: BuyoutQuoteResult,
) -> tuple[bool, list[str]]:
    diffs: list[str] = []
    fields = (
        "principal_balance",
        "actuarial_rebate",
        "provincial_tax",
        "total_payout",
    )
    for fname in fields:
        v_leg = getattr(legacy, fname)
        v_mod = getattr(modern, fname)
        if v_leg != v_mod:
            diffs.append(f"{fname}:leg={v_leg}!=mod={v_mod}")

    if legacy.ledger_codes != modern.ledger_codes:
        diffs.append(
            f"ledger:leg={legacy.ledger_codes}"
            f"!=mod={modern.ledger_codes}"
        )

    is_exact = len(diffs) == 0
    return (is_exact, [f"tx={tx_id} " + d for d in diffs])
```

### Coexistence transitoire : couche d’anticorruption et synchronisation CDC bidirectionnelle

Pendant les six à dix-huit mois que dure l’étranglement d’un monolithe patrimonial (IBM i DB2/400 ou IMS/DB2 z/OS), les services modernes exposés en MCP servent déjà en temps réel les sagas agentiques, alors que des lots nocturnes non migrés (états réglementaires trimestriels, réconciliations fiscales de fin d’exercice) lisent encore les tables physiques historiques. Deux écueils guettent : le nouveau service écrit directement dans les tables DB2/400 aux noms de six caractères (CSTNBR, AMTPD1) et hérite du modèle de données patrimonial, ou les deux bases divergent dès la première écriture moderne. Deux patrons complémentaires résolvent cette transition :

1.  **La couche d’anticorruption bidirectionnelle** : Le service moderne a son propre schéma relationnel, aligné sur la nomenclature canonique Apache Ossie (`contract_id`, `principal_balance_cad`). Une passerelle déterministe et sans état traduit, à la frontière seulement, les événements métier en enregistrements au format tabulaire qu’attendent les traitements par lots restants. Elle transcode les pages de codes EBCDIC (CCSID 037 / 1147) vers UTF-8 et décode sans perte de signe les zones décimales condensées COMP-3.
2.  **La réplication transactionnelle par capture de changements (CDC et patron *Outbox*), ordonnée par LSN avec un jeton anti-rebond** : Quand un module passe de l’exécution en miroir (lecture et comparaison seules) au rôle de maître en écriture, chaque transaction commise dans la base moderne écrit atomiquement dans une table `outbox`. Debezium / Kafka Connect la lit et répercute la mise à jour vers les récepteurs de journaux DB2 for i (JRNRCV) ou z/OS en moins de 200 ms, dans l’ordre strict du numéro de séquence de journal (LSN). Les traitements nocturnes patrimoniaux se poursuivent, et un retour arrière immédiat sans perte de données reste possible si une anomalie exigeait de redonner temporairement la main au programme RPG. Un marqueur d’origine (`origin_system_id`) empêche toute boucle de réplication croisée entre l’ancien et le nouveau système.

| Approche face au patrimoine sans API | Délai initial | Latence et coût à l’exécution | Risque de régression métier | Verdict architectural 2027 |
|:--------------------|:------------------|:------------------|:--------------------|:----------------------|
| Encapsulation CUA permanente | Rapide (2–4 sem.) | Élevés (5–15 s, \> 0,40 \$) | Moyen (fragilité des écrans) | Pont tactique transitoire uniquement |
| Réécriture « Big Bang » par LLM | Trompeur (mois/ans) | Faibles une fois terminée | Extrême (échec \> 70 %) | À proscrire |
| Transpilation syntaxique 1:1 brute | Moyen (3–6 mois) | Faibles (Java/`C#` généré) | Moyen, code illisible (« *JOBOL* ») | Acceptable seulement avant refactorisation |
| Figuier étrangleur, oracle de caractérisation et exécution en miroir | Incrémental (6–8 sem./domaine) | Optimaux (`< 20 ms`, \< 0,003 \$) | Quasi nul (cible : 0,00 \$ d’écart sur un cycle d’affaires complet; section 47.4) | Standard de référence du compendium |

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur Public, Fiscalité & Retraites — Explicabilité légale des règles extraites du patrimoine**
:::

Dans les ministères du Revenu, les caisses de retraite publiques et les régies d’assurance maladie qui exploitent de vastes systèmes COBOL, la modernisation par l’usine ajoute un bénéfice juridique. L’agent spécificateur extrait chaque branchement obscur de 1995 vers une table de décision DMN / Apache Ossie vérifiée contre l’oracle de caractérisation. Le code exécutable rejoint ainsi le texte de la loi votée, et chaque décision automatisée devient explicable au citoyen au sens de l’article 65.2 de la Loi sur l’accès.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur Bancaire & Assurances (BSIF E-23) — Gouvernance des outils de génération de code sur systèmes importants**
:::

Sous la ligne directrice BSIF E-23, qui entre en vigueur le 1er mai 2027, comment qualifier le risque de modèle quand un modèle génératif réécrit la logique de calcul d’un système financier important ? Le service déployé en production est un programme déterministe compilé (Rust/Go/Java), validé par 100 000 cas de parité exacte au centime près et signé par un ingénieur responsable. L’IA n’intervient qu’à l’étape d’outillage d’atelier, hors production : aucune incertitude stochastique ne subsiste à l’exécution financière réelle.
::::

------------------------------------------------------------------------

## 47.12 Application au fil rouge : modernisation progressive de 1,4 million de lignes RPG sur IBM i chez Boréal Capital & Assurances (BCA)

Chez BCA, l’usine résorbe la dette patrimoniale AS/400 sans interrompre une seule journée les opérations réglementées.

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Extinction programmée de la cellule CUA d'écran 5250 par modernisation RPG → Rust/MCP chez BCA**
:::

**Situation initiale chez BCA** : Au chapitre 25, BCA avait ouvert son cœur IBM i par deux voies : un serveur MCP sur ses 14 programmes RPGLE maîtres (93,5 % du volume) et une seule cellule CUA (*Computer-Use Agent*) confinée, qui pilotait en écran vert 5250 le sous-module d’avenants acquis en 2008, sans sources modifiables (6,5 % du volume). Restait le patrimoine lui-même : 1,4 million de lignes RPG III et RPG ILE accumulées depuis 1998, maintenues par trois spécialistes seniors à dix-huit mois de la retraite. À 19 secondes par avenant, la cellule CUA, bien que sécurisée, bloquait le passage à l’échelle à haute fréquence. La refonte « Big Bang », estimée à 28 M\$ CAD, restait gelée.

**Déploiement de l’usine chez Boréal** :

1.  **Cartographie symbolique complète en trois semaines** : Un parseur RPG/CL/DB2 a indexé les 2 140 programmes et isolé 14 domaines fonctionnels faiblement couplés, en commençant par les trois modules qui concentraient 78 % des appels d’agents (*Éligibilité Garantie*, *Calcul Rachat Anticipé*, *Avenant Franchise*).
2.  **Capture de l’oracle *Golden Master* et boucle à séparation des devoirs** : Sur chaque module, 60 000 transactions historiques anonymisées de 2024–2026 ont formé l’oracle scellé. Au premier cycle d’exécution en miroir du module de rachat anticipé, le comparateur (Extrait 47.3) a intercepté 17 divergences de 0,01 \$ à 0,04 \$ CAD sur des contrats bissextiles signés au Nouveau-Brunswick. Elles venaient d’une règle d’arrondi implicite de 2007 qu’aucun analyste humain ne connaissait plus, intégrée et prouvée avant la bascule.

**Bilan audité après neuf mois** :

- **5 des 14 domaines cœurs** (490 000 lignes RPG équivalentes) convertis et homologués en services Rust décimaux, exposés en MCP Streamable HTTP, sans écart comptable en production.
- **Retrait de la cellule CUA d’écran 5250** : le sous-module d’avenants de 2008, dont le chapitre 25 finançait la réécriture, a été refait par l’usine d’après son seul oracle de transactions, faute de sources; un avenant se traite en 11 millisecondes, contre 19 secondes.
- Les trois experts RPG seniors, libérés de la maintenance corrective nocturne, agissent désormais comme architectes validateurs des invariants métier aux côtés de l’équipe plateforme.
::::

------------------------------------------------------------------------

## 47.13 Décision d’architecture normative et points de contrôle

La décision ADR-029 régit tout recours à des agents autonomes pour le développement logiciel et la modernisation du patrimoine applicatif.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-029 — Pipeline Agentic SDLC à séparation des devoirs et modernisation patrimoniale par oracle Golden Master et Shadow Mirroring**
:::

- **Statut** : Acceptée (la séparation en rôles à droits distincts reste une extrapolation à valider; section 47.1) \| Périmètre : Ingénierie Logicielle, DevSecOps & Patrimoine \| Révision : Semestrielle
- **Contexte** : Laisser des agents de codage générer à la fois le code métier et ses tests, importer librement des paquets externes ou réécrire d’un bloc des systèmes patrimoniaux non documentés produit des tests tautologiques, des risques d’empoisonnement ASI04 et des régressions financières.
- **Options évaluées** :
  1.  *Limitation à l’autocomplétion manuelle ligne à ligne en IDE* : Rejetée — insuffisante pour résorber à temps la dette patrimoniale critique face aux départs à la retraite.
  2.  *Traduction automatisée directe du patrimoine, sans double exécution ni séparation des tests* : Rejetée — perte des cas limites implicites et de l’exactitude d’arrondi décimal.
  3.  *Usine logicielle agentique qui sépare l’agent d’oracle de l’agent bâtisseur isolé, verrouillée par des tests de mutation (cible de $\ge 85\,\%$, calibrée par module), une revue contradictoire hétérogène et une bascule par figuier étrangleur après 30 jours d’exécution en miroir à zéro écart* : Retenue.
- **Décision** : (a) Interdire techniquement à tout agent bâtisseur de modifier les tests d’acceptation ou de fusionner sans portes déterministes ni approbation humaine; (b) confiner la résolution de dépendances à un dépôt interne approuvé; (c) exiger, pour toute modernisation patrimoniale, l’arithmétique décimale exacte, un corpus *Golden Master* historique et un cycle complet d’exécution en miroir sans divergence avant la bascule.
- **Conséquences** : Modernisation rapide et sûre des systèmes centraux et extinction progressive des CUA, au prix d’un investissement initial dans l’indexation AST/SCIP (là où un indexeur existe; section 47.2) et dans l’infrastructure de réplication de trafic en miroir.
::::

### Liste de contrôle de mise en production

1.  **Séparation des droits oracle et bâtisseur** : Les permissions du dépôt interdisent-elles à l’identité NHI de l’agent codeur toute modification des répertoires de spécifications, d’oracles *Golden Master* et de pipelines CI ?
2.  **Confinement réseau contre le *Slopsquatting*** : Le bac à sable OpenSandbox de compilation bloque-t-il tout téléchargement direct sur Internet, au profit du seul registre interne de paquets vérifiés (SBOM) ?
3.  **Indexation symbolique AST / SCIP** : L’analyse d’impact préalable repose-t-elle sur le graphe déterministe des appels et des tables, plutôt que sur une recherche vectorielle approximative (pour COBOL et RPG, la liste d’indexeurs SCIP lue n’en compte aucun : l’index vient de l’outillage de l’éditeur ou n’existe pas; section 47.2) ?
4.  **Porte de tests de mutation ($\ge 85\,\%$)** : Le pipeline rejette-t-il toute demande de tirage dont les tests ne détectent pas les mutants syntaxiques injectés, selon un seuil calculé sur le code modifié, calibré par module et hors mutants équivalents reconnus (le chiffre de 85 % n’a pas de source; section 47.3) ?
5.  **Revue contradictoire** : L’agent critique chargé de l’audit de sécurité et de concurrence repose-t-il sur une famille de modèles distincte de celle qui a produit le code, avec une validation humaine ensuite ?
6.  **Arithmétique décimale stricte** : Une règle d’analyse statique bannit-elle les types flottants binaires du code financier ou comptable modernisé, au profit de types décimaux exacts ?
7.  **Parité en miroir sur un cycle complet** : Le service modernisé a-t-il tourné au moins 30 jours (cible sans source), prolongés jusqu’à couvrir un cycle d’affaires complet, en exécution en miroir sur trafic réel, avec 0,00 \$ CAD d’écart et chaque écart ignoré signé, avant de recevoir du trafic en écriture ?
8.  **Plan de retour arrière CDC immédiat** : Pendant la bascule progressive par déploiement canari, la synchronisation inverse permet-elle de rendre la maîtrise au module patrimonial en moins d’une minute en cas d’anomalie ?
