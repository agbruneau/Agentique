# Chapitre 12 — Gouvernance d’entreprise, conformité réglementaire et FinOps agentique

Disposer d’agents protégés par identités non humaines (`NHI`) et portes d’intention (chapitre 10), instrumentés par `OpenTelemetry` et encadrés par des coupe-circuits `SRE` (chapitre 11), ne légitime pas leur généralisation en entreprise. Sans gouvernance institutionnelle, trois dérives menacent le portefeuille : prolifération hors inventaire (*Shadow AI*), exposition juridique lors de décisions automatisées et dérive des factures d’inférence. Selon l’enquête *State of FinOps 2026*, **98 %** des équipes FinOps gèrent désormais des dépenses d’IA (contre 31 % deux ans plus tôt), alors que **43 %** des organisations sondées en septembre 2026 dans *State of Tokenomics* peinent encore à démontrer leur retour sur investissement (`ROI`) [274].

Ce chapitre clôt la Partie IV sur le modèle opérationnel, la conformité et le `FinOps` agentique. En **lecture** `EA`, il fixe l’imputabilité, la maîtrise des risques, la conformité légale et l’économie du portefeuille ; en **lecture** `SA`, il les traduit en métadonnées de registre, preuves d’audit, leviers de cache/routage et signaux d’imputation. Par frontière d’étanchéité, l’architecture technique de l’`IAP`, de l’`AI Gateway` et du cycle `GitOps` relève du chapitre 13.

## 12.1 Modèle opérationnel cible : registre central d’agents, homologation par risque et Agent Owner

### 12.1.1 Du Shadow AI au registre central fédéré

L’essor des assistants configurables et des serveurs `MCP` permet à toute ligne d’affaires d’assembler un agent autonome en quelques heures [275] [276]. Dès que ces déploiements contournent les plans de contrôle, l’organisation ignore quels modèles traitent ses données sensibles et quelles délégations atteignent les `Systems of Record` (`SoR`) [275] [277]. Pour contenir ce *Shadow AI*, le `Cloud Adoption Framework` recommande d’étendre les mécanismes de gouvernance existants au lieu de bâtir une bureaucratie parallèle [275].

Prolongeant le catalogue posé devant l’`ARB` au chapitre 2, le **registre central d’agents** (`Agent Registry`) dissocie deux strates complémentaires [277] :

1. **La strate d’inventaire et de catalogue unifié (**`Agent Registry`**)** : elle répertorie tous les agents actifs — harnais internes, plateformes `PaaS` et offres `SaaS` tierces, incluant les agents sans identité native dits *registry-only* [277]. Adossée aux schémas `OASF` du chapitre 5, elle normalise les capacités déclarées, les serveurs `MCP` autorisés, la sensibilité des données, le palier `L0–L4` et la cote de risque [277] [276].
2. **La strate d’identité cryptographique (**`Agent Identity` **et** `Blueprints`**)** : reliée au socle `NHI` du chapitre 10, elle associe chaque fiche du registre à une identité technique instanciée depuis un modèle directeur (*Agent Identity Blueprint*) portant authentification, portées `OAuth` et accès conditionnel [277].

En **lecture SA**, aucun flux n’accède à la production sans liaison bidirectionnelle vérifiable entre l’identifiant du catalogue et l’identité d’exécution (`Agent ID` ou `SPIFFE ID`) [277] [276]. Le registre automatise aussi les politiques d’hygiène : révocation des agents inactifs selon une politique d’expiration configurable, recertification périodique et suspension immédiate en cas de dépassement des seuils `SRE` [277].

### 12.1.2 Séparation des rôles, Agent Owner et Trois Lignes de Défense (3LoD)

Les premiers projets agentiques souffrent fréquemment d’une responsabilité diluée entre équipes techniques, directions métier et fournisseurs de modèles [278] [279]. Publiée le 11 septembre 2025 par le Bureau du surintendant des institutions financières (`BSIF` / `OSFI`) avec prise d’effet au **1er mai 2027**, la **Ligne directrice E-23** (*Model Risk Management*) fournit aux institutions financières fédérales (`FRFI`) et aux grandes entreprises un cadre rigoureux directement transposable aux agents [278].

Le `BSIF` englobe explicitement l’IA, l’apprentissage automatique et les systèmes autonomes à apprentissage dynamique dans sa définition du modèle, exige un inventaire central (*Model Inventory*) et impose une séparation stricte des mandats sur tout le cycle de vie [278] :

- **L’**`Agent Owner` **(**`Model Owner`**)** : responsable métier nommé (jamais un compte générique) répondant du mandat d’usage, du budget et de la conformité [277] [278]. Il maintient la documentation, supervise les revues d’accès et active le coupe-circuit métier ; tout agent orphelin sans *sponsor* actif est suspendu [277] [278].
- **Le** `Model Developer` : conçoit le harnais `80/20`, intègre les outils `MCP`, exécute `EvalOps` et déploie les garde-fous locaux [278] [279].
- **Le** `Model Reviewer` : évalue indépendamment solidité conceptuelle, intrants, biais, sécurité et limites [278] [279].
- **Le** `Model Approver` **(**`ARB` **/ Comité IA)** : autorise ou révoque la mise en service selon l’appétit au risque, au vu des conclusions du `Model Reviewer` [278].

Pour éviter que les revues manuelles n’asphyxient la livraison logicielle, l’organisation transpose les **Trois Lignes de Défense (**`3LoD`**)** à la cadence du code [279] [276]. La **1re ligne (**`1LoD`**)** intègre les contrôles déterministes dans le harnais et le pipeline (`Policy-as-Code`, filtres, plafonds) [279]. La **2e ligne (**`2LoD`**)** établit les grilles de risque et déploie des contrôles continus, pouvant mobiliser des agents vérificateurs spécialisés pour pré-auditer l’architecture face aux normes [279] [276]. La **3e ligne (**`3LoD`**)** — l’audit interne — exploite des pistes immuables pour attester indépendamment l’efficacité des contrôles amont [279].

> **[Figure]**
> - 1re ligne (1LoD — Produit & Plateforme)
> - Gouvernance centrale (ARB)
> - 2e ligne (2LoD — Contrôle)
> - 3e ligne (3LoD — Audit)
> - Agent Owner /Sponsor métier
> - Équipe Domaine & Harnais 80/20
> - Registre central (OASF + Agent ID) Homologation par
> - palier (R1 à R4)
> - Model Reviewer (Risque, RPRP, Sécurité)
> - Model Approver (ARB / Comité IA)
> - Audit interne (Pistes immuables)
> - Conformité, traçabilité
> - et maîtrise du risque
> - soumet dossier
> - endosse mandat
> - inscrit / suspend
> - évalue R3-R4
> - homologue
> - vérifie preuves
> - cadre

*Fig. 45. – Modèle opérationnel cible EA : registre central, homologation par palier de risque et Trois Lignes de Défense*

### 12.1.3 Paliers d’homologation par niveau de risque (R1 à R4) et cycle de décommissionnement

Appliquer le même processus d’approbation à un assistant documentaire interne qu’à un agent octroyant du crédit paralyse la livraison ou banalise le risque [275] [278]. Selon l’approche proportionnelle d’OSFI E-23, le registre classe chaque agent sur quatre paliers de risque inhérent (`R1` à `R4`) [275] [278].

| Palier | Périmètre et autonomie | Instance d’homologation | Exigences de validation | Cycle de révision et retrait |
| --- | --- | --- | --- | --- |
| `R1` **— Minimal** | Lecture interne (`L0–L1`), zéro mutation `SoR`, zéro renseignement personnel (`RP`) | `Agent Owner` + contrôles `1LoD` automatisés [275] [277] | Fiche `OASF`, `Agent ID`, plafond budgétaire | Revue annuelle et politique d’expiration sur inactivité (`Agent ID`) [277] |
| `R2` **— Modéré** | Synthèse métier (`L1–L2`), accès à corpus internes restreints | `Agent Owner` + revue ciblée `2LoD` (sécurité/données) [278] | Suite `EvalOps` initiale, propagation `ACL`, traces `OTel` [276] | Revue semestrielle de dérive et de coûts [278] |
| `R3` **— Élevé** | Traitement de `RP` sensibles, écritures compensables (`L2–L3`) | Revue indépendante (`Model Reviewer`) + approbation `ARB` [278] [279] | `ÉFVP` préalable, `red teaming`, coupe-circuit vérifié [278] [280] | Revue trimestrielle, recertification annuelle et audit `3LoD` [278] |
| `R4` **— Critique** | Décision à effet juridique/financier ou action irréversible (`L3–L4`) | Comité exécutif des risques (`Model Approver`) + `RPRP` [278] [281] | `ÉFVP` + fiche `AIA`, validation indépendante, repli `L0` prouvé [278] [282] | Surveillance continue, revue trimestrielle et plan de retrait testé [278] |

*Tableau 12.1 — Matrice d’homologation proportionnelle par palier de risque (*`R1` *à* `R4`*) et responsabilités* `3LoD`*.*

Tout changement substantiel (nouveau modèle frontalier, nouvel outil mutateur ou extension de population) déclenche une réévaluation de palier [278]. Enfin, le **décommissionnement** clôture formellement le cycle : révocation des certificats `NHI`, purge des mémoires selon les calendriers de conservation, archivage immuable des journaux et bascule vers un processus déterministe [277] [278].

> **Arbitrage EA / SA** — Interdire tout déploiement en production d’un agent absent du registre central, dépourvu d’`Agent Owner` humain nommé ou sans palier `R1–R4` assigné [277] [278]. L’`EA` impose la séparation entre concepteur (`1LoD`), évaluateur indépendant (`2LoD`) et approbateur (`ARB`) dès le palier `R3` [278] [279] ; le `SA` automatise l’homologation `R1–R2`, lie chaque identifiant de catalogue à son `Agent ID` cryptographique et applique la suspension automatique sur perte de *sponsor* ou inactivité [277] [276].

## 12.2 Conformité multi-juridictionnelle : Loi 25 (Québec), LPRPDE, EU AI Act, NIST AI RMF et ISO/IEC 42001

Une organisation opérant au Québec, au Canada et en Europe doit satisfaire simultanément des lois sur la vie privée, des directives publiques, des règlements par niveau de risque et des normes certifiables [281] [283] [284] [285]. L’architecture gagnante consiste à retenir l’enveloppe la plus exigeante de ces textes et à la convertir en preuves d’ingénierie unifiées [276] [285].

### 12.2.1 Québec (Loi 25) : RPRP, ÉFVP préalable et décisions exclusivement automatisées

Au Québec, la *Loi sur la protection des renseignements personnels dans le secteur privé* (`RLRQ, c. P-39.1`, modernisée par la **Loi 25**) impose trois exigences directes sur les `Systems of Agency` [281] :

1. **Responsable de la protection des renseignements personnels (**`RPRP`**,** `article 3.1`**)** : l’entreprise répond de tout renseignement personnel (`RP`) détenu, y compris ceux traités ou inférés par des agents [281]. Le rôle incombe par défaut à la plus haute autorité (délégation écrite possible) et agit en vérificateur `2LoD` sur les projets `R3–R4` [278] [281].
2. `ÉFVP` **dès l’amorce et portabilité (**`article 3.3`**)** : tout projet d’acquisition, de développement ou de refonte traitant des `RP` impose une évaluation des facteurs relatifs à la vie privée (`ÉFVP`) proportionnelle à la sensibilité, à la finalité, à la quantité, à la répartition et au support des données, avec consultation du `RPRP` **dès le début du projet** [281]. Elle vérifie aussi la restitution des `RP` informatisés dans un **format technologique structuré et couramment utilisé**, contraignant les mémoires du chapitre 6 [281].
3. **Décisions exclusivement automatisées (**`article 12.1` **au privé,** `article 65.2` **au public)** : l’organisation informe la personne concernée **au plus tard lors de la communication de la décision** [281] [286]. Sur demande, elle divulgue les `RP` utilisés, les **raisons, facteurs et paramètres principaux**, le droit de rectification et permet de **présenter des observations à un membre du personnel habilité à réviser la décision** [281] [286].

Le guide normatif québécois souligne un point critique pour le `SA` : une intervention humaine mineure, dépourvue de répercussion réelle sur le résultat, ne soustrait pas le système à cette qualification [286]. Une interface `HITL` de pure approbation mécanique (identifiée au chapitre 1) laisse donc l’entreprise exposée aux exigences de l’article 12.1 ou 65.2 [286].

### 12.2.2 Canada fédéral (LPRPDE et Directive sur la prise de décisions automatisée)

Sur le plan fédéral, la planification architecturale doit s’appuyer sur le droit positif en vigueur en 2026 [283] [287]. Le **projet de loi C-27** (*Loi de 2022 sur la mise en œuvre de la Charte du numérique*, incluant le projet de `LIAD` /`AIDA`) est demeuré inachevé à l’étape du comité lors de la **prorogation parlementaire du 6 janvier 2025** et est mort au feuilleton sans devenir loi [287].

En conséquence, la **LPRPDE** reste la loi fédérale applicable au secteur privé canadien [283] [287]. Pour les systèmes génératifs et agentiques, le Commissariat à la protection de la vie privée du Canada (`CPVP` / `OPC`) et ses homologues provinciaux et territoriaux ont publié les *Principes pour des technologies d’IA générative responsables, dignes de confiance et respectueuses de la vie privée* [283]. Ces principes exigent une autorité légale et un consentement valide tout au long du cycle de vie (y compris lors d’inférences ou de données tierces), l’évitement de **zones interdites** (*no-go zones* : profilage discriminatoire ou atteinte grave aux droits), la gestion de l’exactitude face aux hallucinations probabilistes, la protection dès la conception, la transparence et l’exercice des droits d’accès et de rectification [283].

Pour les institutions fédérales — et à titre de gabarit dans les marchés publics — la **Directive sur la prise de décisions automatisée** du Conseil du Trésor (`SCT`) s’applique dès qu’un système recommande ou rend une décision administrative, **même lorsqu’un humain intervient dans la boucle** [282]. Elle impose de compléter et publier une **Évaluation de l’incidence algorithmique (**`ÉIA` **/** `AIA`**)**, outil ouvert évaluant conception du système, algorithme, type de décision, incidence et données afin d’imposer des mesures d’atténuation proportionnelles [282].

### 12.2.3 Union européenne : EU AI Act et amendements Digital Omnibus on AI

Pour les services opérant sur le marché européen, le **Règlement (UE) 2024/1689 (**`EU AI Act`**)** classe les systèmes selon quatre niveaux de risque (inacceptable/interdit, haut risque, transparence, minimal) et encadre les modèles à usage général (`GPAI`) sous la supervision de l’`AI Office` [284].

Le calendrier officiel de l’*AI Act Service Desk*, actualisé après les amendements du **Digital Omnibus on AI**, fixe des jalons précis pour les feuilles de route d’entreprise [288] :

1. **Depuis le 2 février 2025** : interdictions des pratiques à risque inacceptable et obligations de littératie IA [284] [288].
2. **Depuis le 2 août 2025** : application des règles visant les modèles `GPAI` et mise en place des autorités nationales et européennes de gouvernance [284] [288].
3. **Depuis le 2 août 2026 (et 2 décembre 2026)** : entrée en vigueur des **obligations de transparence (**`article 50`**)** — notification d’interaction avec un système d’IA et marquage lisible par machine des contenus synthétiques — complétée au 2 décembre 2026 par de nouvelles interdictions sur les hypertrucages sexuels non consentis et la fin de la période transitoire de l’article 50(2) pour les systèmes mis sur le marché avant août 2026 [288].
4. **D’août 2027 à août 2028** : ouverture d’au moins un bac à sable réglementaire par État membre au 2 août 2027, puis application des règles **haut risque de l’Annexe III** (crédit, emploi, services essentiels) le **2 décembre 2027**, et des composants intégrés aux produits réglementés de l’Annexe I le **2 août 2028** [288].

Pour les agents classés à haut risque à échéance de décembre 2027, l’`EA` et le `SA` doivent garantir dès la conception la qualité des données, la **journalisation automatique des événements**, la cybersécurité et une **surveillance humaine effective** dotée d’une capacité réelle d’interruption [284] [288].

### 12.2.4 Socle d’ingénierie commun : NIST AI RMF (AI 600-1) et ISO/IEC 42001:2023

Pour unifier ces obligations, l’entreprise s’appuie sur deux cadres d’ingénierie complémentaires :

- **Le** `NIST AI RMF 1.0` **(**`NIST AI 100-1`**) et le profil** `NIST AI 600-1` : `AI RMF 1.0` structure la gestion des risques en quatre fonctions continues (`Govern`, `Map`, `Measure`, `Manage`) autour de sept caractéristiques de confiance [289]. Le profil génératif `NIST AI 600-1` (juillet 2024) y ajoute douze risques propres à l’IA générative, incluant la confabulation, la fuite par mémorisation, l’injection de prompt, l’anthropomorphisation et la monoculture algorithmique [280]. La `CSA` et les initiatives du `NIST` étendent ce modèle à l’identité vérifiable et aux contrôles d’action des agents [276].
- **La norme certifiable** `ISO/IEC 42001:2023` **(**`AIMS`**)** : elle spécifie les exigences d’un système de management de l’IA couvrant politiques, objectifs, évaluations d’impact et amélioration continue [285]. Toutefois, l’utilisation d’une plateforme infonuagique certifiée `ISO/IEC 42001` ne dispense pas l’entreprise : selon le modèle de responsabilité partagée, celle-ci doit maintenir son propre `AIMS`, ses évaluations d’impact et sa Déclaration d’applicabilité (`SoA`) [285]. Côté `SA`, des paquets de conformité automatisés — à l’image du `Conformance Pack` `AWS Config` mappant jusqu’à 258 règles gérées sur les groupes de contrôles de l’Annexe A (`A.4` Ressources, `A.5` Impacts, `A.6` Cycle de vie, `A.7` Données et `A.9` Exploitation, comme la rotation des clés `A.9.2`) — rendent cette conformité vérifiable en continu [290].

> **[Figure]**
> - Juridictions applicables
> - Référentiels d'ingénierie
> - Artefacts de preuve exigibles
> - LPRPDE & Directive SCT Principes CPVP / Score AIA
> - Loi 25 (Québec) P-39.1 art. 3.1, 3.3, 12.1
> - EU AI Act + Digital Omnibus Art. 12, 14, 50 & Annexe III
> - NIST AI RMF 1.0 & AI 600-1 Govern, Map, Measure, Manage
> - ISO/IEC 42001:2023 AIMS & Annexe A
> - Dossier ÉFVP + Fiche AIA & Mandat RPRP
> - Déclaration d'applicabilité (SoA) & Registre risques
> - Preuves d'exécution Journal Art. 1 2 & Recours HITL
> - Score AIA
> - ÉFVP préalable
> - Recours humain
> - Traçabilité
> - Contrôles A.4-A.9

*Fig. 46. – Cartographie croisée des obligations réglementaires multi-juridictionnelles et des artefacts de preuve d’audit*

| Cadre / Texte | Portée et statut | Exigences clés sur les agents | Preuves et mécanismes `SA` associés |
| --- | --- | --- | --- |
| `Loi 25` **(**`P-39.1` **/** `A-2.1`**)** | Québec, en vigueur [281] [286] | `RPRP` (`3.1`), `ÉFVP` + portabilité (`3.3`), transparence, facteurs et révision humaine (`12.1` /`65.2`) [281] [286] | `ÉFVP` signée, export structuré `RP`, trace des facteurs et recours humain effectif [281] [286] |
| `LPRPDE` **&** `Directive SCT` | Privé fédéral (après caducité `C-27`) ; public `SCT` [283] [287] [282] | Autorité légale, zones interdites, exactitude (`CPVP`) ; `AIA` publique même avec humain (`SCT`) [283] [282] | Fiche `AIA`, filtres anti-profilage, contrôle de provenance et rectification [283] [282] |
| `EU AI Act` **(**`2024/1689`**)** | UE ; `art. 50` août 2026, Ann. III déc. 2027, Ann. I août 2028 [284] [288] | Interdictions, `GPAI`, transparence (`art. 50`), journalisation et surveillance humaine haut risque [284] [288] | Avis IA, marquage machine des sorties, journaux `OTel` immuables, bouton d’arrêt [284] [288] |
| `NIST AI RMF` **&** `AI 600-1` | Cadre volontaire transversal [289] [280] | `Govern-Map-Measure-Manage` ; 12 risques GenAI (confabulation, fuite, monoculture) [289] [280] | Registre des risques, `red teaming`, diversification multi-modèles [289] [280] |
| `ISO/IEC 42001:2023` | Norme `AIMS` certifiable (`A.4` –`A.9` automatisables) [285] [290] | `AIMS` propre du client distinct des certifications cloud du fournisseur [285] | `SoA` documentée et règles continues d’infrastructure (`Conformance Packs`) [285] [290] |

*Tableau 12.2 — Matrice de correspondance réglementaire et normative multi-juridictionnelle.*

> **Arbitrage EA / SA** — Proscrire les architectures de conformité morcelées par territoire ou fondées sur des textes non adoptés comme l’ancien projet de loi `C-27` [287]. L’`EA` impose un socle unique structuré autour d’`ISO/IEC 42001` et de `NIST AI RMF / AI 600-1` dont le jeu de preuves satisfait par construction la `Loi 25` (`ÉFVP`, `art. 12.1`), la `LPRPDE`, la `Directive SCT` et l’`EU AI Act` (`art. 50` et préparation `Annexe III`) [281] [283] [288] [285]. Le `SA` matérialise ce socle par la journalisation des facteurs décisionnels, l’exportation structurée des `RP`, le marquage machine des contenus générés et des écrans de révision dotés d’un réel pouvoir de modification [281] [286] [288].

## 12.3 FinOps agentique : économie unitaire par transaction métier, facteur d’amplification, caching et cascade SLM/LLM

À la différence de l’infonuagique facturée à l’heure de calcul ou au stockage, l’entreprise agentique consomme des unités volatiles — jetons d’entrée, de sortie et de raisonnement, appels d’outils et débits provisionnés — liées au harnais et au modèle [274].

### 12.3.1 Économie unitaire : dépasser le coût au jeton vers le coût par résultat réussi

Piloter au tarif du million de jetons trompe l’analyse [274] [291]. La capacité **Unit Economics** de la `FinOps Foundation` sépare les métriques techniques (coût par jeton) des métriques métier [274] [291] : un modèle bon marché qui échoue ou réessaie en boucle détruit la marge [274] [292].

L’indicateur directeur est le **coût par résultat métier réussi** (*cost per successful outcome* : réclamation réglée, billet clos, écriture validée) [274] [291], soumis à deux règles :

1. **Inclusion des pertes** : imputer aux transactions réussies les jetons consommés par les sorties rejetées sous le seuil qualité et l’infrastructure environnante [274] [292].
2. **Suivi par distribution** : suivre ce coût en distribution (`p50`, `p90`, `p99`) plutôt qu’en moyenne trompeuse [274].

### 12.3.2 Anatomie du facteur d’amplification multi-tours et multi-agents

Le coût d’un agent dépasse de plusieurs ordres de grandeur celui d’une simple invite en raison de quatre facteurs multiplicatifs :

- **Le préambule de contexte** : les jetons saisis par l’usager ne reflètent pas les jetons facturés, car chaque appel inclut les consignes système, les schémas d’outils `MCP`, la mémoire récupérée et les résultats `RAG` [274].
- **La dérive quadratique** `O(T²)` **des boucles multi-tours** : dans une boucle `ReAct` de `T` tours sans compaction ni mise en cache, chaque itération ré-expédie le socle initial `P` augmenté de tous les échanges et retours d’outils précédents. Avec un ajout moyen `Δ` par tour, la consommation cumulée d’entrée croît en `T × P + Δ × T(T - 1)/2`, pénalisant sévèrement les boucles profondes.
- **L’asymétrie tarifaire entrée / sortie** : les jetons générés en sortie sont facturés bien plus cher que l’entrée — un facteur exact de **5×** sur la gamme Anthropic Claude documentée (`20 $/MTok` contre `4 $/MTok` sur Opus 5.5, `10 $/MTok` contre `2 $/MTok` sur Sonnet 5.5) [293]. Contraindre la concision des sorties typées protège directement le budget.
- **L’amplification multi-agents** : comme établi empiriquement au chapitre 7, un agent unique outillé consomme déjà environ **4×** plus de jetons qu’un échange conversationnel simple, et une topologie multi-agents environ **15×** plus par duplication de contexte et coordination inter-nœuds.

La partition hybride **80/20** du chapitre 3 constitue ainsi le premier levier financier : conserver 80 % du contrôle déterministe en code classique réduit à zéro le coût d’inférence sur ces segments [274].

### 12.3.3 Optimisation en cascade : Prompt Caching KV, Semantic Caching et routage SLM/LLM

Sur les 20 % cognitifs restants, l’architecture `FinOps` empile trois filtres d’optimisation complémentaires :

1. `Prompt Caching` **au niveau préfixe (tenseurs** `KV`**)** : en mémorisant les tenseurs clé-valeur d’un préfixe inchangé, les fournisseurs réduisent fortement le coût des entrées répétées [293] [294]. Chez **Anthropic**, le préfixe suit l’ordre `tools`, `system` puis `messages` jusqu’au marqueur `cache_control` [293]. Malgré une prime d’écriture initiale (`1,25×` pour 5 minutes rafraîchies à chaque lecture, ou `2×` pour 1 heure), les lectures tombent à **90 %–95 % de rabais** (`0,05×` –`0,10×`, voire `0,025×` sur Fable 5.2) [293]. Sur **Amazon Bedrock**, le *prompt caching* à 5 minutes abaisse jusqu’à **90 %** les coûts et **85 %** la latence [295]. Chez **OpenAI**, le cache sur préfixe exact réduit de **50 % à 95 %** l’entrée selon les générations tout en allégeant les quotas `TPM`, mais reste sensible aux réglages (`tools`, `parallel_tool_calls`, `reasoning.effort` ou `Compaction` modifiant l’historique) [294]. Chez **Google Gemini**, le *context caching* implicite s’active par défaut dès Gemini 2.5 au-delà de **2 048 ou 4 096 jetons** [296]. Un seul champ dynamique en tête de requête invalide tout le préfixe [294] [296].
2. `Semantic Caching` **vectoriel** : avant tout appel modèle, la requête est vectorisée et comparée par index `HNSW` (p. ex. `Redis`) [297]. Au-dessus d’un seuil cosinus calibré entre **0,70 et 0,95**, la réponse mémorisée est servie sans coût d’inférence, abaissant la latence de `2,7 s` à `0,3 s` (**-89 %**) [297]. Ce levier exige des `TTL` adaptés (`30–300 s` sur données volatiles, `3 600+ s` sur corpus stables) et un cloisonnement `ACL` [297].

3. **Modélisation** `FinOps` **des cascades et du routage** `SLM` **/**`LLM` : prolongeant le chapitre 3, le choix répond à une équation de seuil explicite. Une cascade `FrugalGPT` — abaissant les coûts jusqu’à **98 %** à qualité égale sur les tâches évaluées — reste rentable tant que `C_SLM + C_verif + p_escalade × C_LLM < C_LLM`, soit `p_escalade < 1 - (C_SLM + C_verif) / C_LLM`, tout en ajoutant une latence sur les cas escaladés [298]. Le routage amont évite ce double appel : `RouteLLM` atteint **95 %** de la performance de `GPT-4 Turbo` avec seulement **14 %** d’appels forts sur `MT-Bench` (75 % moins cher qu’un routeur aléatoire) et **54 %** sur `MMLU` [299], tandis qu’`Amazon Bedrock Intelligent Prompt Routing` réduit jusqu’à **30 %** les coûts intra-famille sans perte de précision [295].

> **[Figure]**
> - Filtres de déflation FinOps
> - Optimisation d'inférence (20 %
> - cognitif)
> - 1. Règle 80/20 Code déterministe (0 jeton)
> - 2. Cache sémantique Index HNSW (0,70-0,95) (0 jeton sur hit)
> - 3. Routeur / Cascade SLM vs Frontier (RouteLLM / FrugalGPT)
> - 4. Préfixe & Budget KV Prompt Caching (-50 % à -95 %) + Compaction anti-O(T²)
> - Transaction métier entrante Résultat métier validé (Coût unitaire)
> - Évalue
> - 80 % déterministe
> - 20 % cognitif Hit cache (latence -89 %)
> - Miss cache
> - Modèle calibré
> - Sortie bornée

*Fig. 47. – Entonnoir d’optimisation FinOps agentique : réduction du coût unitaire et endiguement de l’amplification*

| Levier d’optimisation | Mécanisme | Gains vérifiés | Conditions et risques |
| --- | --- | --- | --- |
| **Règle hybride** `80/20` | Déport des flux prévisibles en code déterministe | `0` jeton sur 80 % de la logique applicative | Éviter de rigidifier les nœuds réellement ambigus [274] |
| `Semantic Caching` **(**`HNSW`**)** | Réponse vectorielle sous seuil cosinus `0,70–0,95` [297] | `0` jeton sur *hit* ; latence `-89 %` (`2,7 s → 0,3 s`) [297] | Faux positifs si seuil bas ; exiger `TTL` court et cloisonnement `ACL` [297] |
| `KV Prompt Caching` | Réemploi de tenseurs sur préfixe exact stable [293] [294] | `-50 %` à `-95 %` en entrée [293] [294] ; `-90 %` coût / `-85 %` latence sur Bedrock [295] | Toute mutation avant le point d’arrêt invalide le cache ; prime d’écriture `1,25×–2×` [293] [294] |
| **Routage amont (**`RouteLLM` **/** `IPR`**)** | Aiguillage prédictif vers `SLM` ou modèle fort dès l’entrée [295] [299] | `14 %–54 %` d’appels forts pour `95 %` de qualité [299] ; jusqu’à `-30 %` intra-famille [295] | Réétalonnage requis lors des changements de modèles [274] [299] |
| **Cascade** `SLM → LLM` **(**`FrugalGPT`**)** | Appel `SLM` puis escalade conditionnelle [298] | Jusqu’à `-98 %` sur charges majoritairement simples [298] | Latence double à l’escalade ; non rentable si `p_escalade ≥ 1 - (C_SLM+C_verif)/C_LLM` [298] |

*Tableau 12.3 — Leviers d’optimisation* `FinOps` *agentique, gains vérifiés et conditions d’efficacité.*

> **Arbitrage EA / SA** — Exiger la modélisation du **coût par résultat métier réussi** (en distribution `p50` /`p90` /`p99` incluant les échecs) pour tout agent `R2–R4` avant homologation [274] [292]. L’`EA` impose de justifier le multiplicateur multi-agents (`~15×`) face à la règle `80/20` et de vérifier l’équation de seuil des cascades `SLM` /`LLM` [274] [298] ; le `SA` fige l’ordre `tools → system → messages` pour préserver le `KV Prompt Caching`, applique des seuils prudents en `Semantic Caching` et borne la dérive `O(T²)` par compaction et plafonds de tours [293] [294] [297].

## 12.4 Pilotage budgétaire, refacturation interne (showback/chargeback), TCO/ROI ajusté du risque et réversibilité

### 12.4.1 Attribution unifiée (OpenTelemetry GenAI + FOCUS) et pilotage des anomalies

Sans imputation granulaire reliant chaque jeton à son propriétaire, l’optimisation technique ne se traduit pas en responsabilité financière [274]. Or, les factures directes des API d’inférence manquent souvent d’étiquetage natif (*thin allocation data*) lorsque plusieurs produits partagent les mêmes clés d’organisation [274].

L’architecture d’imputation couple deux standards ouverts complémentaires [274] [300] [301] :

1. **La télémétrie** `OpenTelemetry GenAI` : les conventions `semantic-conventions-genai` normalisent sur chaque trace `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, les jetons en cache et le modèle sollicité [301]. En y attachant l’identifiant du registre (`Agent ID`) et les étiquettes obligatoires (`Project`, `Environment`, `Team`, `CostCenter`, `Criticality`), l’entreprise relie chaque exécution à son centre de coûts [274] [301].
2. **Le format normalisé** `FOCUS` : la spécification *FinOps Open Cost & Usage Specification* (`v1.0` à `v1.4`) unifie les données de facturation entre fournisseurs infonuagiques, éditeurs de modèles, `SaaS` et centres de données [274] [300]. La révision `FOCUS v1.5` enrichit ce schéma avec l’identité du modèle, la séparation entrée/sortie, l’état de cache et l’attribution au demandeur, assurant le rapprochement comptable avec les traces `OpenTelemetry` [274] [300].

Côté budgétaire, la volatilité agentique exige des **fenêtres de prévision plus courtes** révisées fréquemment avec les finances et séparées entre enveloppes pilotes (`ShutdownEligible = True`) et budgets de production [274] [292]. Des détecteurs d’anomalies surveillent en continu boucles récursives, gonflements de contexte et reprises excessives pour déclencher des coupures budgétaires avant dépassement [274].

### 12.4.2 Refacturation interne (Showback puis Chargeback) et arbitrage de capacité (PAYG vs PTU)

L’imputation interne suit l’approche graduelle définie dans la capacité **Invoicing & Chargeback** [274] [302] :

- `Showback` **préalable** : exposer aux équipes et `Agent Owners` leurs dépenses ventilées par cas d’usage sans modifier immédiatement leur compte de résultat (`P&L`) [274]. Cette visibilité corrige rapidement le surdimensionnement de modèles tout en validant les règles d’allocation [274].
- `Chargeback` **comptable** : une fois l’attribution `FOCUS` réconciliée, imputer réellement les coûts aux budgets ou `P&L` produits selon les règles comptables internes, sans confondre ce choix comptable avec un palier de maturité supérieur [274] [302].

En parallèle, le portefeuille arbitre parmi six modèles tarifaires — à l’usage (*On-demand*), engagements de dépense, capacité provisionnée (`PTU`), lots asynchrones/préemptibles (*Batch/Spot*), abonnement par siège et paliers de volume [274]. L’arbitrage clé oppose paiement à l’usage (`PAYG`) et **unités de débit provisionnées (**`PTU`**)** : facturées à l’heure ou par réservation `Azure` qu’elles soient consommées ou non, les `PTU` garantissent la latence en production soutenue, mais deviennent plus onéreuses que le `PAYG` sur des charges intermittentes ou limitées aux heures ouvrables [274] [303]. Le modèle optimal alloue un socle `PTU` sous réservation — dimensionné via le calculateur de capacité selon la forme des requêtes, le ratio sortie/entrée et le taux de cache — complété par un **débordement (**`spillover`**) automatique** vers des terminaisons `PAYG` en pointe [303], tout en déportant les tâches différables vers le mode *Batch* [274].

### 12.4.3 TCO complet, ROI ajusté du risque et gouvernance de réversibilité (EU Data Act)

Démontrer la rentabilité face au constat des **43 %** d’entreprises incertaines de leur `ROI` impose de dépasser le seul coût des jetons [274]. Le `TCO` **complet** agrège cinq postes : (1) inférence, réessais et `GPU`, (2) stockage vectoriel, exécution durable et télémétrie, (3) ingénierie plateforme et connecteurs, (4) évaluations `EvalOps` et audits `3LoD`, et (5) travail humain de supervision (`HITL` / `art. 12.1 Loi 25` / `art. 14 AI Act`) [274] [292]. Le `ROI` **ajusté du risque** rapporte ensuite les gains métier (productivité, délais, résilience, croissance [274]) à ce `TCO` majoré du coût espéré des incidents résiduels [278] [274].

Enfin, la réversibilité prolonge les verrous du chapitre 2 [276] [304]. L’entreprise conserve la propriété exclusive de ses contrats `MCP` /`A2A` /`OASF`, mémoires vectorielles, jeux `EvalOps` et journaux [281] [285]. En Europe — et comme étalon contractuel — le **Data Act (**`Règlement (UE) 2023/2854`**)**, applicable depuis le **12 septembre 2025**, impose la facilité de changement de fournisseur infonuagique et supprime progressivement les frais de sortie jusqu’à leur interdiction complète prévue en janvier 2027 [304]. Combiné à la portabilité structurée de l’article 3.3 de la Loi 25 [281], ce cadre justifie des exercices annuels de bascule validant le coût et le délai de migration.

> **[Figure]**
> - Collecte normalisée
> - Moteur d'imputation FinOps
> - Pilotage & Réversibilité
> - Traces OTel GenAI gen_ai.usage.\* & Agent ID
> - Factures Cloud & API Schéma FOCUS v1.4 / v1.5
> - TCO complet par résultat (Jetons + Infra + EvalOps + HITL)
> - Détection d'anomalies & Plafonds budgétaires
> - Arbitrage capacité PAYG vs PTU vs Batch
> - Showback →Chargeback par Centre de coûts / P&L
> - Tests de réversibilité (EU Data Act & Portabilité)
> - Attribution agent
> - Coûts normalisés
> - Alertes dérive
> - Taux d'utilisation
> - Imputation P&L
> - ROI ajusté du risque

*Fig. 48. – Chaîne d’attribution, de refacturation interne (Showback/Chargeback) et de réversibilité FinOps*

| Dimension `FinOps` | Régime pilote / charge variable | Régime production soutenue | Règle d’arbitrage `EA` / `SA` |
| --- | --- | --- | --- |
| **Capacité d’inférence** | `PAYG` à l’usage ou *Batch* asynchrone | Socle `PTU` réservé + *spillover* `PAYG` | `PAYG` pour trafic intermittent ; `PTU + spillover` dès charge 24/7 soutenue [274] [303] |
| **Refacturation interne** | `Showback` par cas d’usage / équipe | `Chargeback` sur le `P&L` métier | `Showback` d’abord pour visibilité, puis `Chargeback` après validation `FOCUS` [274] [302] |
| **Pilotage budgétaire** | Enveloppe pilote (`ShutdownEligible`) | Prévision glissante courte par résultat | Séparer strictement budgets pilotes et production ; détection d’anomalies temps réel [274] [292] |
| **Évaluation de valeur** | Coût par résultat + taux de rejet qualité | `TCO` à 5 postes + `ROI` ajusté du risque | Bannir toute décision fondée sur le seul tarif au jeton [274] [291] |
| **Réversibilité** | Contrats ouverts `MCP` /`A2A` /`OASF` | Zéro frais de sortie (`Data Act`) + test annuel | Conserver `evals`, mémoires et données dans des formats structurés portables [281] [304] |

*Tableau 12.4 — Grille d’arbitrage budgétaire, refacturation interne, capacité et réversibilité.*

> **Arbitrage EA / SA** — Imposer le rapprochement `OpenTelemetry GenAI` + `FOCUS` avant d’activer le `Chargeback` comptable, en débutant systématiquement par le `Showback` [274] [300] [302] [301]. L’`EA` exige pour tout projet `R3–R4` un `TCO` complet à cinq postes, un `ROI` ajusté du risque intégrant le coût `HITL` et des clauses de sortie sans pénalité alignées sur le `Data Act` [274] [304] ; le `SA` rend obligatoire le marquage `Agent ID` / `CostCenter`, configure le débordement `PAYG` /`PTU` et exécute des tests réguliers de portabilité des mémoires et jeux `EvalOps` [274] [301] [303].

## Synthèse architecturale et transition vers la Partie V

Ce chapitre a établi la charpente institutionnelle, juridique et économique de l’entreprise agentique. Le modèle opérationnel ancre chaque agent dans un **registre central** avec un `Agent Owner` humain, la séparation des mandats d’**OSFI E-23** et les **Trois Lignes de Défense (**`3LoD`**)** graduées de `R1` à `R4` [277] [278] [279]. Un socle unifié `ISO/IEC 42001` **+** `NIST AI RMF / AI 600-1` satisfait conjointement **Loi 25**, **LPRPDE** / **Directive SCT** et **EU AI Act** [281] [283] [288] [285]. Enfin, le `FinOps` **agentique** pilote le coût par **résultat métier réussi**, freine l’amplification (`80/20`, cache sémantique, `KV Prompt Caching`, routage `SLM` /`LLM`), et garantit l’imputation `OpenTelemetry` /`FOCUS`, le `TCO` complet et la réversibilité [274] [300] [301] [304].

Avec la sécurité `Zero-Trust` (chapitre 10), l’observabilité `OpenTelemetry` /`EvalOps` (chapitre 11) et la gouvernance présentée ici, le Plan 4 est complet. La **Partie V** s’ouvre au **chapitre 13** pour matérialiser ces exigences dans l’`Internal Agentic Platform` **(**`IAP`**)**, l’`AI Gateway` **hybride** et le **GitOps cognitif**.
