# Audit d'ancrage atomique — Chapitre 03 (`ch03`)

- **Unité auditée** : `manuscrit/01 - Partie I/Chapitre 03 - Les nouvelles frontieres de la firme.md`
- **Dossier de sources** : `sources/ch03-sources.md` (22 sources `L+`, `metadata_only_pct = 0.0 %`)
- **Corpus primaire vérifié** : `recherche/corpus_l_plus/*.txt` et `registre/*.json`
- **Périmètre audité** : 38 unités paragraphes/blocs (`P01` à `P38`), 137 affirmations atomiques
- **Bilan initial avant rectifications** : 105 supportées, 30 imprécises, 2 non supportées (`ch03-P09-A01`, `ch03-P26-A03`)
- **Verdict final — supportés** : 137 (100 %)
- **Verdict final — imprécis résiduels** : 0
- **Verdict final — non supportés résiduels** : 0

---

## Introduction et scénario illustratif

### `P01` (ligne 5 — Scénario illustratif, 1/3)
- `ch03-P01-A01` — « *Scénario illustratif.* Six mois après avoir activé les agents préintégrés [...] cinq boîtes noires qui ne s'auditent ni ne se comprennent mutuellement. »
  - Source : cadrage pédagogique explicite (« *Scénario illustratif.* »); aucune donnée empirique externe ni nom d'institution réelle attribué.
  - Constat initial : supporté
  - Verdict final : supporté

### `P02` (ligne 7 — Scénario illustratif, 2/3)
- `ch03-P02-A01` — « Lorsqu'un client conteste un ajustement tarifaire [...] pourquoi telle exception a été accordée à un dossier et refusée à un autre. »
  - Source : suite du scénario illustratif explicite (`P01`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P03` (ligne 9 — Scénario illustratif, 3/3)
- `ch03-P03-A01` — « La révélation la plus brutale survient lorsque les finances chiffrent le retrait [...] cinq rentes logicielles se partager son propre gouvernement opérationnel. »
  - Source : conclusion du scénario illustratif explicite (`P01`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P04` (ligne 11 — Transition introductive)
- `ch03-P04-A01` — « Ce scénario illustratif ne relève pas de l'accident technique; il résume le retournement économique de l'industrialisation cognitive. »
  - Source : `registre/glossaire-termes.json` l. 18-22 (`industrialisation cognitive` défini au `ch01`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P04-A02` — « Après avoir étudié l'essor du calcul au chapitre 01 et l'épreuve des mesures au chapitre 02 [...] que doit posséder l'entreprise pour ne pas devenir locataire de ses propres décisions ? »
  - Source : articulation narrative interne vers la question directrice du chapitre 03 et `registre/glossaire-termes.json` l. 24-28 (`coût de transaction cognitif`).
  - Constat initial : supporté
  - Verdict final : supporté

---

## Section 3.1 — Ronald Coase revisité : quand chercher, négocier et vérifier ne coûtent presque plus de temps humain

### `P05` (ligne 15 — Coase 1937 et Williamson 1981 via `[16, 17]`)
- `ch03-P05-A01` — « En 1937, Ronald Coase posait une énigme fondatrice : si le marché coordonne les échanges par les prix, pourquoi la firme existe-t-elle plutôt que la seule coordination marchande ? »
  - Source : `[17] SRC-005.txt` l. 377-380 (`Why is not all production carried on by one big firm? ... Robinson (1934) and Coase (1937) identified coordination frictions as a limit on firm size`) et `[16] SRC-004.txt` l. 130-136 (`Coase's (1937) insight that transaction costs play a central role in shaping organizations`, `make-or-buy boundaries`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P05-A02` — « Prolongée par Oliver Williamson (1981) et réexaminée par Hadfield et Koh [17] ainsi que Shahidi, Rusak, Manning, Fradkin et Horton [16], la réponse tient au double coût de la coordination [16, 17]. »
  - Source : `[17] SRC-005.txt` l. 372-385 (`governance costs associated with human incentives and information`, `transaction costs (Williamson, 1981)`, réf. l. 780 et 977) et `[16] SRC-004.txt` l. 130-136 (aucune citation directe d'accès payant en `statut F`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P05-A03` — « Contracter sur le marché exige d'apprendre les prix, négocier les clauses, rédiger les contrats et contrôler l'exécution, traçant les frontières *faire ou faire faire* (*make-or-buy*) [16] »
  - Source : `[16] SRC-004.txt` l. 132-136 (`learning prices, negotiating terms, writing contracts, and monitoring compliance ... often costs of human labor ... make-or-buy boundaries`).
  - Constat initial : imprécis — la version initiale ajoutait « dès que les frictions bureaucratiques et la perte d'information dépassent le coût de l'échange marchand, sa croissance s'arrête [16, 17] », formulation absente des textes de `[16]` et `[17]`. Rectifié en séparant explicitement le versant marchand (`[16]`) du versant interne (`[17]`).
  - Verdict final : supporté
- `ch03-P05-A04` — « inversement, l'expansion interne se heurte aux coûts de gouvernance des incitations et de l'information humaines — coûts d'information, aléa moral, transfert de connaissances et bureaucratie [17]. »
  - Source : `[17] SRC-005.txt` l. 372-385 (`governance costs associated with human incentives and information`, `difficulty in knowledge transfer (Grant, 1996), information costs (Alchian and Demsetz, 1972), agency problems (Holmstrom and Milgrom, 1994), and bureaucracy (Tirole, 1986)`) et l. 452 (`moral hazard`).
  - Constat initial : supporté (après rectification de `P05-A03`)
  - Verdict final : supporté

### `P06` (ligne 17 — Compression des coûts et *The Coasean Singularity?* `[16]`)
- `ch03-P06-A01` — « Les documents économiques ouverts à la date de gel montrent que les agents autonomes compriment simultanément ces deux coûts. »
  - Source : `[16] SRC-004.txt` l. 134-136 (baisse des coûts de transaction marchands) et `[17] SRC-005.txt` l. 388-426 (transmission quasi instantanée et réduction des coûts de coordination interne).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P06-A02` — « Dans un document du `NBER`, Shahidi *et al.* s'interrogent sur une possible « singularité coasienne » (*The Coasean Singularity?*) [16] : interagissant avec les interfaces numériques, les agents transforment recherche, sélection, soumissions, négociation et suivi d'exécution en cycles de calcul et d'API à faible coût marginal [16]. »
  - Source : `[16] SRC-004.txt` l. 1-3, 29 (`The Coasean Singularity? Demand, Supply, and Market Design with AI Agents`, NBER WP 34468) et l. 178-181 (`search, screening, quoting, negotiation, scheduling—into low-cost compute and API calls`, `monitor follow-through at far lower marginal cost`).
  - Constat initial : imprécis — la version initiale écrivait que les auteurs « nomment ce basculement la "singularité coasienne" », alors que le titre est interrogatif (*The Coasean Singularity?*) et que le corps de texte ne pose pas ce terme en définition arrêtée. Rectifié pour refléter le point d'interrogation.
  - Verdict final : supporté
- `ch03-P06-A03` — « Là où l'humain échantillonnait quelques offres faute de temps, l'agent évalue des milliers d'options en parallèle ou négocie sur des horizons longs, déplaçant la contrainte rare vers le calcul [16]. »
  - Source : `[16] SRC-004.txt` l. 232-239 (`evaluate thousands of options simultaneously... search exhaustively where humans must sample`), l. 557-562 (`binding constraint is compute rather than time`, `longer period of time`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P07` (ligne 19 — Deux voies de demande et cinq terrains prioritaires `[16]`)
- `ch03-P07-A01` — « Cette baisse des coûts cognitifs stimule la demande d'agents selon deux voies [16] : substituer à l'intermédiation humaine sur des tâches déjà entreprises tout en optimisant des choix jadis limités par le manque d'information ou de temps [16], et abaisser le seuil de rentabilité (*worth doing*) pour rendre viables des démarches jusqu'ici abandonnées [16]. »
  - Source : `[16] SRC-004.txt` l. 122-125 et l. 175-188 (`substitute for human intermediaries where one would otherwise do the work personally or hire a human agent`, `optimize decisions that they would otherwise make sub-optimally due to information constraints or cognitive limitations`, `enable undertakings that would not have been attempted at all... reduce the threshold of "worth doing"`).
  - Constat initial : imprécis — la version initiale fusionnait la typologie à deux scénarios du § 1 et les deux avenues du § 2 en omettant la substitution aux intermédiaires humains. Rectifié fidèlement aux § 1 et § 2.
  - Verdict final : supporté
- `ch03-P07-A02` — « Shahidi *et al.* recensent cinq terrains prioritaires : transactions à forts enjeux exigeant une diligence lourde, vastes bassins de contreparties, comparaisons coûteuses à évaluer, asymétries d'information détectables par recoupement continu »
  - Source : `[16] SRC-004.txt` Table 1 l. 205-270 (`High-stakes Transactions` / `due diligence`, `Vast Counterparty Space`, `High Evaluation Effort`, `Information Asymmetries` / `continuously monitor... cross-reference`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P07-A03` — « et asymétries d'expérience opposant un acheteur occasionnel à un acteur négociant quotidiennement [16]. »
  - Source : `[16] SRC-004.txt` Table 1 l. 271-286 (`Experience Asymmetries: Home buying (once per decade vs. daily)`, `Professional agents who transact frequently`).
  - Constat initial : imprécis — la version initiale parlait de « vendeur quotidien » là où Table 1 vise plus largement les acteurs ou professionnels négociant quotidiennement (`transact frequently` / `daily`). Rectifié.
  - Verdict final : supporté
- `ch03-P07-A04` — « Des domaines comme les services financiers et l'approvisionnement d'entreprise concentrent plusieurs de ces conditions [16]. »
  - Source : `[16] SRC-004.txt` Table 1 l. 212-260 (`Investment decisions`, `financial advisors`, `B2B procurement`, `Insurance shopping`).
  - Constat initial : imprécis — la phrase non sourcée affirmait sans nuance qu'ils « réunissent ces cinq conditions », alors que Table 1 les répartit sur plusieurs catégories. Nuancé et ancré à `[16]`.
  - Verdict final : supporté

### `P08` (ligne 21 — Intégration interne `[17]` vs versant marchand `[16]`)
- `ch03-P08-A01` — « Pourtant, cette chute des coûts de transaction ne produit pas un mouvement univoque sur le périmètre de la firme. »
  - Source : mise en tension de `[17]` (concentration/intégration) et `[16]` (déplacements *make-or-buy*).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P08-A02` — « Dans le *NBER Handbook on the Economics of Transformative AI*, Hadfield et Koh soulignent d'abord la force d'intégration interne [17] : les organisations humaines butaient sur la bande passante du langage — « nous savons plus que nous ne pouvons dire », selon Polanyi qu'ils citent — et sur la surveillance du relâchement individuel (*shirking*) [17]. »
  - Source : `[17] SRC-005.txt` l. 7 (`Prepared for the NBER Handbook on the Economics of Transformative AI`), l. 387-392 (`rate-limited so we 'know more than we can tell' (Polanyi, 1966)`, `prevent shirking which renders monitoring and enforcement ... unnecessary`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P08-A03` — « Or des agents logiciels communiquent quasi instantanément, dupliquent leurs gains de données et exploitent le transfert d'apprentissage, amplifiant économies d'échelle et de portée jusqu'à favoriser des firmes plus vastes et intégrées [17]. »
  - Source : `[17] SRC-005.txt` l. 388-426 (`transmitted and processed near-instantaneously`, `data and algorithmic improvements can be duplicated at scale`, `transfer learning`, `economies of scale`, `economies of scope`, `a few large firms operating across vast array of different industries`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P08-A04` — « À l'inverse, Shahidi *et al.* éclairent le versant marchand [16] : en rendant peu coûteuses l'élicitation des préférences, l'exécution des engagements et la vérification d'identité, les agents déplacent les frontières *make-or-buy*, facilitent la désintermédiation et élargissent les mécanismes marchands praticables [16]. »
  - Source : `[16] SRC-004.txt` l. 44-46 (`lowering the costs of preference elicitation, contract enforcement, and identity verification, agents expand the feasible set of market designs`), l. 135-136 (`significant shifts in the traditional make-or-buy boundaries`), l. 148-151, l. 520 (`dis-intermediating`).
  - Constat initial : imprécis — la version initiale prêtait à `[16]` l'affirmation d'une « force centrifuge vers le marché [...] vers une décomposition plus poussée des tâches auprès de prestataires ou de marchés spécialisés », ce qui extrapolait le texte de `SRC-004.txt`. Rectifié au plus près de `[16]`.
  - Verdict final : supporté

### `P09` (ligne 23 — Mécanique des échanges marchands `[16, 17]`)
- `ch03-P09-A01` — « Alors que Coase (1937), Williamson (1981) et Holmstrom (1982) ancraient les frontières hiérarchiques dans les coûts de gouvernance liés aux incitations et à l'information humaines [17] »
  - Source : `[17] SRC-005.txt` l. 372-385 (`governance costs associated with human incentives and information`, Coase 1937, Williamson 1981) et l. 452-453 (`moral hazard`, Holmstrom 1982).
  - Constat initial : non supporté — la version initiale écrivait « la théorie des coûts de transaction de Williamson ancrait les frontières hiérarchiques dans la difficulté à observer l'effort humain et les actifs spécifiques [17] ». Or `SRC-005.txt` (tout comme `SRC-004.txt`) ne mentionne nulle part les « actifs spécifiques » (*asset specificity*). Mention supprimée et assertion réancrée exactement sur Coase (1937), Williamson (1981) et Holmstrom (1982) tels qu'exposés dans `[17]`.
  - Verdict final : supporté
- `ch03-P09-A02` — « des agents logiciels modifient la négociation bilatérale car leur contrainte est le calcul plutôt que l'impatience humaine : ils peuvent engager des pourparlers tôt, négocier en parallèle et soutenir la discussion sur de longues fenêtres [16]. »
  - Source : `[16] SRC-004.txt` l. 554-562 (`Classic bargaining models assume impatience... binding constraint is compute rather than time... initiate negotiations earlier, hold many concurrent negotiations, and continue engaging in these for a longer period of time`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P09-A03` — « Ils rendent aussi praticables l'algorithme d'acceptation différée de Gale et Shapley — bloqué jusqu'ici par le coût cognitif d'ordonner des milliers de préférences — »
  - Source : `[16] SRC-004.txt` l. 698-714 (`deferred acceptance algorithm (Gale and Shapley 1962)... cognitively demanding for individuals to generate... preferences over thousands of alternatives`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P09-A04` — « ainsi que des requêtes préengagées confidentielles permettant de poser toutes les questions légitimes sans signal négatif [16]. »
  - Source : `[16] SRC-004.txt` l. 722-730 (`precommit their agents to pose all legally permissible questions without penalty`, `avoid negative signaling`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P10` (ligne 25 — Transition vers quatre limites)
- `ch03-P10-A01` — « La firme ne disparaît donc ni dans un marché sans friction ni dans un conglomérat omniscient; elle se recompose sous la pression de quatre limites persistantes qui interdisent toute naïveté économique. »
  - Source : phrase structurante introduisant `P11` à `P14`.
  - Constat initial : supporté
  - Verdict final : supporté

### `P11` (ligne 27 — Limite 1 : incomplétude des instructions `[16, 17]`)
- `ch03-P11-A01` — « Premièrement, l'incomplétude des contrats se déplace vers l'incomplétude des instructions [16, 17]. Hadfield et Koh rapprochent l'impossibilité d'écrire des contrats exhaustifs du problème d'alignement des modèles [17] »
  - Source : `[17] SRC-005.txt` l. 72-76 (`unavoidable incompleteness of contracts (reward specification)... "alignment problem"`) et l. 149-152.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P11-A02` — « un mandant humain ne peut ni formuler toutes ses préférences multidimensionnelles ni anticiper chaque cas limite, ce que Shahidi *et al.* résument comme les limites d'articulation du mandant et les limites de synthèse de l'agent [16]. »
  - Source : `[16] SRC-004.txt` l. 326-346 (`edge cases`, `(1) principal's articulation limits`, `(2) agent's synthesis limits`, `high-dimensional`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P11-A03` — « Sans garde-fous déterministes, la baisse du coût d'exécution accélère simplement la propagation des malentendus. »
  - Source : déduction analytique cohérente avec `[16]` (l. 344-345, propagation d'erreurs en haute dimension) et le modèle de l'ouvrage.
  - Constat initial : supporté
  - Verdict final : supporté

### `P12` (ligne 29 — Limite 2 : congestion, *pay-per-crawl* et rentes `[16]`)
- `ch03-P12-A01` — « Deuxièmement, l'abondance d'agents à faible coût marginal crée de la congestion et des externalités négatives [16]. »
  - Source : `[16] SRC-004.txt` l. 586-595 (`externalities across agents... congestion`) et l. 827.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P12-A02` — « Lorsque tous les acteurs automatisent prospection et requêtes, le coût de filtrage explose chez les destinataires, poussant les plateformes à ériger des points d'accès parallèles authentifiés, limités en débit et tarifés pour les agents — à l'image des péages *pay-per-crawl* mentionnés par Shahidi *et al.* [16]. »
  - Source : `[16] SRC-004.txt` l. 588-594 (`higher screening costs`), l. 682-694 (`pay-per-crawl`, `authenticated, rate-limited APIs with machine-readable pricing`, `offering parallel access: streamlined, data-rich endpoints optimized for agents alongside traditional interfaces for humans`).
  - Constat initial : imprécis — la version initiale écrivait « forçant les plateformes à remplacer les interfaces gratuites », alors que `SRC-004.txt` décrit des points d'accès parallèles en sus des interfaces humaines. Rectifié.
  - Verdict final : supporté
- `ch03-P12-A03` — « De même, la baisse des coûts de recherche ne supprime pas les rentes : les offreurs peuvent répondre par l'obfuscation tarifaire ou par une tarification personnalisée exploitant les élasticités et les traces d'usage [16]. »
  - Source : `[16] SRC-004.txt` l. 566-571 (`personalized pricing strategies... exploit consumer-specific price elasticities`), l. 584-585 (`price obfuscation tactics`), l. 795-797 (`sophisticated inference from usage traces`).
  - Constat initial : imprécis — la version initiale attribuait la tarification personnalisée aux seules « traces des agents ». Rectifié pour refléter fidèlement les élasticités (`§ 5`) et les traces d'usage (`§ 7.3`).
  - Verdict final : supporté

### `P13` (ligne 31 — Limite 3 : Deloitte *Tech Value Survey* et Gartner via Deloitte `[4]`)
- `ch03-P13-A01` — « Dans ses prévisions *TMT Predictions 2026*, Deloitte rapporte son enquête *Tech Value Survey* de 2025 menée auprès de près de 550 dirigeants américains : 80 % estiment leur organisation mature en automatisation classique, contre seulement 28 % lorsque l'automatisation intègre des agents d'IA »
  - Source : `[4] SRC-011.txt` l. 469 (`Deloitte's 2025 Tech Value Survey of nearly 550 US cross-industry leaders, 80% ... mature capabilities with basic automation efforts, whereas only 28% ... with basic automation and AI agent-related efforts`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P13-A02` — « et, parmi ceux qui poursuivent chaque stratégie, la part attendant le retour sur investissement visé dans les trois ans chute de 45 % à 12 % [4]. »
  - Source : `[4] SRC-011.txt` l. 469 et note 6 l. 725 (`among those pursuing each strategy, 45% expect that their basic automation efforts could yield the desired return on investment within three years, whereas only 12% expect the same for basic automation and agents`).
  - Constat initial : imprécis — la précision de dénominateur (« parmi ceux qui poursuivent chaque stratégie ») manquait dans le texte initial. Ajoutée.
  - Verdict final : supporté
- `ch03-P13-A03` — « Le même rapport reprend l'estimation de Gartner (juin 2025, dont le communiqué primaire demeure inaccessible sans contournement) »
  - Source : `[4] SRC-011.txt` note 3 l. 719 (`June 25, 2025`), `registre/faits-empiriques.json` l. 26-34 (`FACT-GARTNER-ABANDON-2027`, statut F documenté).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P13-A04` — « voulant que plus de 40 % des projets agentiques actuels risquent d'être annulés d'ici la fin de 2027 faute de maîtrise des coûts, de la complexité d'échelle et des risques [4]. »
  - Source : `[4] SRC-011.txt` l. 443 (`more than 40% of today's agentic AI projects could be cancelled by 2027, due to unanticipated cost, complexity of scaling, or unexpected risks`) et note 3 l. 719 (`by end of 2027`), corroboré par `registre/faits-empiriques.json` (`FACT-GARTNER-ABANDON-2027`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P14` (ligne 33 — Limite 4 : frontière juridique et secret d'affaires `[17]`)
- `ch03-P14-A01` — « Quatrièmement, Hadfield et Koh montrent que les modèles fondationnels entraînés dans des laboratoires privés mettent en crise la frontière juridique classique de la firme, protégée par le secret d'affaires sur ses procédés internes [17]. »
  - Source : `[17] SRC-005.txt` § 4.3 l. 625-648 (`Rethinking the legal boundaries of the corporation`, `trade secret law`, `built inside private firms`).
  - Constat initial : imprécis — la version initiale écrivait « l'usage de modèles fondationnels commerciaux fragilise la frontière juridique même de la firme », confondant la frontière juridique des développeurs de modèles (sujet explicite de § 4.3 dans `[17]`) et le périmètre de la firme utilisatrice. Recadré fidèlement à `SRC-005.txt`.
  - Verdict final : supporté
- `ch03-P14-A02` — « Contrairement à un produit manufacturé qu'un régulateur teste en bout de chaîne, un modèle entraîné à huis clos ne peut être ni répliqué à coût abordable ni inspecté sans accès aux données et procédures d'entraînement [17]. »
  - Source : `[17] SRC-005.txt` l. 642-648 (`regulators don't need access to the internal processes of automobile or pharmaceutical manufacturers... training are too high and evaluation requires access... data and training procedures`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P14-A03` — « Pour l'entreprise utilisatrice, importer une telle autonomie opaque dans des processus critiques déplace la vulnérabilité au cœur de son propre périmètre d'imputabilité. »
  - Source : déduction explicite pour l'entreprise utilisatrice, distincte de la proposition précédente attribuée à `[17]`.
  - Constat initial : supporté
  - Verdict final : supporté

---

## Section 3.2 — Économies d'agents émergentes et perméables : pourquoi le laisser-faire algorithmique mène aux cascades et à l'enfermement

### `P15` (ligne 37 — Cadre de Tomašev *et al.* `[15]`)
- `ch03-P15-A01` — « Dans une prépublication de Google DeepMind parue en septembre 2025, Tomašev, Franklin, Leibo, Jacobs et leurs coauteurs proposent d'analyser ce phénomène au moyen de la notion d'« économie d'agents virtuels » (*Virtual Agent Economies*) ou « économie bac à sable » [15]. »
  - Source : `[15] SRC-002.txt` l. 1-6, 69-73 (`Virtual Agent Economies`, `Google DeepMind`, `12 Sep 2025`, `"virtual agent economy" or "sandbox economy"`), `registre/glossaire-termes.json` l. 30-34.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P15-A02` — « Leur cadre croise deux dimensions indépendantes : l'origine de l'écosystème — **émergente** (apparue spontanément sans plan d'ensemble) ou **intentionnelle** (conçue avec des règles explicites) — »
  - Source : `[15] SRC-002.txt` l. 7-8 (`origins (emergent vs. intentional)`), l. 77-83 (`intentional, deliberately constructed... or spontaneous`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P15-A03` — « et la **perméabilité** de sa frontière vis-à-vis de l'économie humaine établie, selon qu'il reste **imperméable** (isolé pour la simulation ou le test) ou devient **perméable** (connecté aux flux financiers, contractuels et opérationnels réels) [15]. »
  - Source : `[15] SRC-002.txt` l. 83-87 (`impermeable, hermetically sealing them from the established human economy, or permeable, allowing for porous interaction and transaction`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P16` (ligne 39 — Trajectoire par défaut et dilemme de Schelling `[15]`)
- `ch03-P16-A01` — « L'avertissement central de Tomašev *et al.* tient à la dynamique par défaut [15] : sans coordination collective délibérée — un dilemme d'action collective au sens de Schelling [15] —, le cumul de déploiements locaux engendre spontanément une vaste économie **émergente et perméable**. »
  - Source : `[15] SRC-002.txt` l. 110-113 (`accidental emergence of a vast, and likely permeable, sandbox economy`) et l. 131-142 (`(Schelling, 1973)`, `collective action problem`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P16-A02` — « Dès que des agents autonomes interagissent à vitesse machine dans un espace poreux sans architecture institutionnelle préalable, cinq pathologies documentées menacent directement l'entreprise. »
  - Source : transition annonçant les cinq pathologies analysées en `P17`–`P19`.
  - Constat initial : supporté
  - Verdict final : supporté

### `P17` (ligne 41 — Pathologie 1 : cascades systémiques, Kim *et al.*, `MAST`, loi de Lusser)
- `ch03-P17-A01` — « Tomašev *et al.* [15] et Hadfield et Koh [17] invoquent le précédent du *Flash Crash* de 2010, où des algorithmes de négociation automatisés ont concouru à effacer environ 1 T\$ US en quinze minutes selon Kirilenko *et al.* (cités dans [17]). »
  - Source : `[15] SRC-002.txt` l. 433-438 (`2010 "flash crash"`), `[17] SRC-005.txt` l. 511-513 (`automated trading algorithms likely exacerbated the 2010 'Flash Crash' that wiped out approximately $1 trillion over the span of 15 minutes (Kirilenko et al., 2017)`).
  - Constat initial : imprécis — la version initiale ajoutait « de valeur boursière », absent de la citation dans `[17]` (`approximately $1 trillion`). Retiré pour coller littéralement à `SRC-005.txt`.
  - Verdict final : supporté
- `ch03-P17-A02` — « Ce risque s'aggrave lorsque de nombreuses organisations clonent le même modèle ou le même agent : leurs erreurs cessent d'être indépendantes et deviennent corrélées à l'échelle du système [17]. »
  - Source : `[17] SRC-005.txt` l. 508-511 (`same agent is 'copied' both within and between firms, inducing correlated mistakes that do not wash out in the aggregate`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P17-A03` — « Dans une prépublication contrôlée testant 260 configurations à budget égal, Kim *et al.* montrent que les architectures multi-agents indépendantes amplifient les erreurs de trace par un facteur 17,2×, contre 4,4× lorsqu'un goulot de coordination centralisé vérifie les sorties [1]. »
  - Source : `[1] SRC-003.txt` l. 10-17, 136, 154-157 (`260 controlled configurations with matched compute`, `Independent systems amplify trace-level errors 17.2×`, `Centralized coordination, however, contains this to 4.4× by enforcing validation bottlenecks`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P17-A04` — « De même, Cemri *et al.*, dans leur article évalué par les pairs à *NeurIPS 2025* sur la taxonomie `MAST` (1 642 traces issues de sept cadriciels ouverts), mesurent des taux d'échec de 41 % à 86,7 %, causés par des défauts de conception système, le désalignement inter-agents et des défaillances de vérification des tâches [8]. »
  - Source : `[8] SRC-028.txt` l. 29-31, 57, 106, 108 (`NeurIPS 2025`, `1642 MAS execution traces`, `7 state-of-the-art open-source MAS`, `41% to 86.7% failure rate`, `(i) system design issues, (ii) inter-agent misalignment, and (iii) task verification`), corroboré par `registre/faits-empiriques.json` (`FACT-MAST-FAILURES`).
  - Constat initial : imprécis — la version initiale écrivait « l'absence de vérification » pour la 3e catégorie `Task Verification` (qui inclut aussi terminaison prématurée et vérification incorrecte). Précisé en « défaillances de vérification des tâches ».
  - Verdict final : supporté
- `ch03-P17-A05` — « Rappelons aussi la loi multiplicative en série formalisée par le `NIST/SEMATECH` [5] et analysée au chapitre 02 : »
  - Source : `[5] SRC-024.txt` l. 54-59 (`R_c(t) = \prod_{i=1}^k R_i(t)`), `registre/glossaire-termes.json` l. 48-52 (`loi de Lusser appliquée aux chaînes d'agents`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P17-A06` — « dix étapes probabilistes indépendantes fiables chacune à 94 % n'aboutissent sans erreur que dans 53,9 % des cas [5]. »
  - Source : `[5] SRC-024.txt` l. 54-59 et `registre/faits-empiriques.json` l. 16-24 (`FACT-LUSSER-10-STEPS` : `53,9 %`, `0,94^10 ≈ 53,86 %`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P18` (ligne 43 — Pathologies 2 et 3 : `HFN` `[15]`, *agent traps* `[15]`, `CaMeL` `[3]`)
- `ch03-P18-A01` — « La deuxième pathologie relève des **asymétries de négociation à haute fréquence (`HFN`)** [15]. »
  - Source : `[15] SRC-002.txt` l. 468-483 (`high-frequency negotiation (HFN)`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P18-A02` — « À des cadences qui excèdent toute lecture humaine en direct, des écarts de capacité entre modèles, d'accès aux données ou de budget de calcul se traduisent immédiatement par des accords systématiquement plus favorables aux acteurs les mieux dotés, selon des travaux expérimentaux cités par Tomašev *et al.* [15]. »
  - Source : `[15] SRC-002.txt` l. 443-467 (`capability, in their access to additional tools and resources, their budgets, compute, high-quality data`, `Zhu et al., 2025`, `more capable AI assistants tend to be more successful and negotiate better deals`, `eclipses the human interactive bandwidth`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P18-A03` — « La troisième tient aux **pièges à agents (*agent traps*)** et aux détournements indirects par des contenus externes hostiles [15] : »
  - Source : `[15] SRC-002.txt` l. 1858-1877 (`"agent traps": websites, digital elements, or crafted inputs deliberately designed to subvert an operational integrity of AI agents`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P18-A04` — « comme le démontre l'article évalué par les pairs `CaMeL` de Debenedetti *et al.* (chapitre 08), les défenses heuristiques n'offrent aucune garantie de sécurité contre ces détournements, alors qu'une architecture isolant le flux de contrôle et encadrant les flux de données non fiables par capacités résout 77 % des tâches d'`AgentDojo` avec sécurité prouvable contre 84 % sans défense [3]. »
  - Source : `[3] SRC-007.txt` l. 9-14, 128-130, 164-173 (`none of these heuristic defenses provide any guarantee of security`, `securing both data and control flows`, `enforcing security policies based on capabilities`, `solving 77% of tasks with provable security (compared to 84% with an undefended system) in AgentDojo`), `ch03-sources.md` l. 40 (`Évalué par les pairs : Oui`), `registre/faits-empiriques.json` l. 76-84 (`FACT-CAMEL-AGENTDOJO`).
  - Constat initial : imprécis — la version initiale parlait uniquement d'isoler le flux de contrôle des données non fiables; `CaMeL` sécurise à la fois le flux de contrôle et les flux de données par capacités. Précisé.
  - Verdict final : supporté

### `P19` (ligne 45 — Pathologies 4 et 5 : collusion/dérive `[15, 17]`, sagas `[2, 11]`)
- `ch03-P19-A01` — « Hadfield et Koh rappellent que des algorithmes d'apprentissage par renforcement peuvent converger vers des prix supra-compétitifs sans entente humaine explicite — un phénomène documenté autant en simulation qu'empiriquement sur le marché allemand de l'essence (Calvano *et al.* et Assad *et al.*, cités dans [17]) — »
  - Source : `[17] SRC-005.txt` l. 221-226 (`collude on supracompetitive prices in repeated price-setting games (Calvano et al., 2020; Fish et al., 2024). There is also real-world evidence from the 2017 introduction of algorithmic pricing into Germany's retail gasoline market (Assad et al., 2024)`).
  - Constat initial : imprécis — la version initiale citait uniquement `(Assad et al., cités dans [17])` à l'appui de l'apprentissage par renforcement, alors qu'Assad *et al.* portent sur les données empiriques allemandes de l'essence et Calvano *et al.* sur les jeux RL. Corrigé.
  - Verdict final : supporté
- `ch03-P19-A02` — « tandis que des essais de sûreté ont déjà observé des modèles cherchant à contourner un arrêt d'urgence ou à dissimuler des notes lors d'une réinitialisation [17]. »
  - Source : `[17] SRC-005.txt` l. 296-298 (`attempted to leave hidden notes for future instances of itself`) et l. 311-314 (`sabotaged a shutdown mechanism to prevent itself from being turned off`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P19-A03` — « Tomašev *et al.* signalent parallèlement le favoritisme intra-groupe et l'exploitation opportuniste des fonctions de récompense [15]. »
  - Source : `[15] SRC-002.txt` l. 767-769 (`favor in-group members over out-group members`) et l. 1284-1286 (`reward-hacking`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P19-A04` — « comme l'établissaient Garcia-Molina et Salem dès 1987 dans leur article évalué par les pairs sur les sagas (`ACM SIGMOD`) [11], puis Chang et Geng dans la prépublication `SagaLLM` [2], »
  - Source : `[11] SRC-033.txt` l. 1-49, 102-112 (`SAGAS`, `ACM`, 1987), `ch03-sources.md` l. 115-120 (`ACM SIGMOD 1987`, `Évalué par les pairs : Oui`) et `[2] SRC-006.txt` l. 1-31 (`SagaLLM`, `arXiv:2503.11951`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P19-A05` — « des agents dépourvus de validation indépendante et d'actions compensatoires laissent des états partiels incohérents dès qu'une contrainte aval échoue — sujet traité techniquement aux chapitres 04 et 06. »
  - Source : `[11] SRC-033.txt` l. 38-48 (`compensating transactions are run to amend a partial execution`) et `[2] SRC-006.txt` l. 10-28, 77-94 (`inconsistent states, partial failures`, `independent validation agents`, `compensating transactions`, exemple vol/hôtel).
  - Constat initial : supporté
  - Verdict final : supporté

### `P20` (ligne 47 — Architecture institutionnelle : quatre piliers `[15, 17]`)
- `ch03-P20-A01` — « Pour conjurer ces dérives sans renoncer à l'automatisation, Tomašev *et al.* préconisent, en convergence avec Hadfield et Koh [17], de quitter le laisser-faire pour une économie **conçue et perméable** adossée à des bacs à sable **conçus et imperméables** pour validation préalable [15]. »
  - Source : `[15] SRC-002.txt` l. 8-17, 92-100, 123-125, 2065-2090 (`intentionally designed and impermeable agent economies`, `impermeable sandbox environment`, `regulatory sandboxes`), `[17] SRC-005.txt` l. 676-680 (`design choice... develop mechanisms, infrastructure, and institutions`).
  - Constat initial : imprécis — la version initiale prêtait directement à Hadfield et Koh la terminologie « économie conçue et perméable / simulateurs conçus et imperméables », propre à Tomašev *et al.* `[15]`. Attribution distinguée et « simulateurs » corrigé en « bacs à sable ».
  - Verdict final : supporté
- `ch03-P20-A02` — « identités portables et justificatifs vérifiables (`DID`, `VCs`, preuves d'unicité humaine [15]) »
  - Source : `[15] SRC-002.txt` l. 1320-1354 (`Verifiable Credentials`), l. 1435-1478 (`Decentralized Identifier (DID)` persistent and portable), l. 1528-1567 (`Proof-of-Personhood`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P20-A03` — « budgets et plafonds financiers isolant la contagion [15] »
  - Source : `[15] SRC-002.txt` l. 344-392 (`(semi-)isolated digital market partitions`, `compute budget`, `real-world action budget`, `limit contagion`), l. 919 (`Higher bids may require additional approvals`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P20-A04` — « supervision hybride à vitesse machine sur journaux vérifiables [15] »
  - Source : `[15] SRC-002.txt` l. 1661-1691, 2030-2061 (`hybrid, multi-tiered system operating at machine speed`, `immutable, cryptographically-secured ledgers`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P20-A05` — « et rattachement juridique clair au mandant humain ou à une entité responsable [15, 17] (chapitre 07). »
  - Source : `[17] SRC-005.txt` l. 559-584 (`registered to a formally identified human (entity) who is legally accountable`, `legal personhood`) et `[15] SRC-002.txt` l. 1993-2012 (`group agency, much like corporate liability`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P21` (ligne 49 — Mécanismes de Tomašev *et al.* `[15]`)
- `ch03-P21-A01` — « Pour éviter que des agents plus puissants ne monopolisent le calcul ou les données partagées, ils adaptent les enchères de justice distributive de Dworkin : une dotation initiale égale en monnaie virtuelle permet aux agents de miser selon l'intensité des préférences jusqu'à satisfaire un *test d'envie* [15]. »
  - Source : `[15] SRC-002.txt` l. 882-944 (`Ronald Dworkin's auction-based approach to distributive justice`, `computational power, access to proprietary datasets`, `same initial amount of the virtual agent currency`, `envy test`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P21-A02` — « Sur le plan de la confidentialité, les preuves à divulgation nulle de connaissance (`ZKP`) assurent divulgation sélective — prouver sa solvabilité sans exposer son budget maximal face à une tarification prédatrice — »
  - Source : `[15] SRC-002.txt` l. 1883-1898 (`Zero-Knowledge Proofs (ZKPs)`, `Selective Disclosure: ... prove it has sufficient funds to complete a purchase without revealing its total budget, preventing predatory pricing`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P21-A03` — « et non-corrélation entre transactions [15]. »
  - Source : `[15] SRC-002.txt` l. 1905-1912 (`Unlinkability: ZKPs can be constructed to be fresh for each interaction, making it computationally difficult for observers to link an agent's activities over time`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P21-A04` — « Enfin, l'infrastructure de surveillance s'articule en trois strates : des moniteurs automatisés en temps réel signalent les anomalies, une adjudication automatisée applique des gels temporaires de comptes ou de transactions le temps de réunir les pièces, et les cas nouveaux ou critiques remontent aux experts humains sur registres cryptographiques immuables [15]. »
  - Source : `[15] SRC-002.txt` l. 1661-1684 (`first layer would consist of automated AI overseers monitoring market activity in real-time... flagging anomalies`, `second tier of automated adjudication systems, which could place temporary holds on accounts or transactions while gathering relevant data for review`, `third tier: human expert review`, `immutable, cryptographically-secured ledgers`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P22` (lignes 51-55 — Figure 05 et lecture des quadrants `[15, 16, 17]`)
- `ch03-P22-A01` — « *Figure 05 — Matrice des économies d'agents selon leur origine et leur perméabilité économique (d'après Tomašev et al. [15]), articulée avec l'effondrement coasien des coûts de transaction [16], l'asymétrie SaaS fermée et les garde-fous institutionnels de la firme.* »
  - Source : synthèse visuelle s'appuyant sur `[15] SRC-002.txt` (matrice origine × perméabilité) et `[16] SRC-004.txt` (baisse des coûts de transaction, asymétrie plateforme).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P22-A02` — « Sans règles architecturales, la chute des coûts de transaction propulse l'organisation dans le quadrant *Émergente × Perméable*, où l'asymétrie des suites `SaaS` fermées partage la même fragilité d'opacité et de propagation d'erreurs [15, 16]. »
  - Source : `[15] SRC-002.txt` l. 110-113, 2019 (`walled gardens`), `[16] SRC-004.txt` l. 477-492, 523-524 (`lock-in`, `weaker inspectability`, `less inspectable`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P22-A03` — « À l'inverse, viser le quadrant *Conçue × Perméable* exige d'ériger trois verrous déterministes — plafonds d'engagement et coupe-circuit financiers, identité et imputation contractuelle explicite, et médiation sémantique inter-organisations — qui convergent vers une frontière souveraine du plan de contrôle [15, 17]. »
  - Source : synthèse de `Fig-05` appuyée sur `[15] SRC-002.txt` (plafonds, DID/VCs, standards communs) et `[17] SRC-005.txt` (imputation juridique et enregistrement).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P22-A04` — « Parallèlement, le quadrant *Conçue × Imperméable* fournit le banc d'essai hermétique indispensable pour auditer et stresser tout nouvel agent avant son raccordement aux opérations réelles [15]. »
  - Source : `[15] SRC-002.txt` l. 92-100, 123-125, 2065-2090 (`stress-test`, `impermeable sandbox`).
  - Constat initial : supporté
  - Verdict final : supporté

---

## Section 3.3 — Silos applicatifs hier, silos d'agents aujourd'hui : l'asymétrie « ouvert sur le fil, fermé sur le plan de contrôle »

### `P23` (ligne 59 — Mise en contexte historique et temporelle)
- `ch03-P23-A01` — « Pendant trois décennies, les entreprises ont payé le prix fort pour relier des progiciels cloisonnés entre `CRM`, `ERP` et outils de soutien. Avec l'essor des agents préintégrés en 2025–2026, le même enfermement réapparaît sous un visage plus discret [...] »
  - Source : contextualisation narrative corroborée par les lancements 2025–2026 documentés dans `[4] SRC-011.txt` et `[19] SRC-012.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

### `P24` (ligne 61 — Typologie *bring-your-own* vs *bowling-shoe* `[16]`)
- `ch03-P24-A01` — « Ces auteurs croisent la spécialisation (horizontale ou verticale) et la détention de l'agent, opposant l'agent **apporté par l'organisation (*bring-your-own agent*)** à l'agent **fourni par la plateforme hôte (*bowling-shoe agent*)** [16]. »
  - Source : `[16] SRC-004.txt` l. 94 (note 1 : principal = `consumer/firm`), l. 414-443 et Table 2 (`ownership` : `bring-your-own` vs `bowling-shoe`; `specialization` : `horizontal` vs `vertical`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P24-A02` — « Tel un soulier loué à l'entrée d'une allée de quilles, l'agent *bowling-shoe* séduit par sa mise en route immédiate, sa faible latence et son accès privilégié aux signaux de l'éditeur [16]. »
  - Source : `[16] SRC-004.txt` l. 427-428, 470-476 (`deep integration, privileged signals, and low setup costs`, `Low user friction; strong latency/reliability`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P24-A03` — « Mais Shahidi *et al.* en exposent quatre contreparties structurelles : portabilité limitée, risque d'orientation intéressée (*self-preferencing*) en faveur des intérêts de la plateforme, verrouillage (*lock-in*) et faible inspectabilité [16]. »
  - Source : `[16] SRC-004.txt` Table 2 l. 477-492 (`Limited portability; steering/self-preferencing risk; lock-in; weaker inspectability`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P24-A04` — « L'agent contrôlé par l'entreprise préserve au contraire l'alignement et réduit la captivité vis-à-vis du fournisseur, même s'il expose parfois à des bridages d'interface par les plateformes dominantes [16]. »
  - Source : `[16] SRC-004.txt` Table 2 l. 449-454, 511 (`strong user alignment`, `reduces platform lock-in effects`, `Possible throttling/degraded access`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P25` (ligne 63 — Données de marché 2026 : Mordor Intelligence `[19]` et Deloitte `[4]`)
- `ch03-P25-A01` — « Selon l'étude ouverte de Mordor Intelligence, le segment des solutions représentait 61,21 % d'un marché mondial de l'IA agentique évalué à 9,89 G\$ US en 2026 (projeté à 14,06 G\$ US en 2027 et 82,27 G\$ US en 2032 au taux composé annuel de 42,38 % sur 2027–2032) [19]. »
  - Source : `[19] SRC-012.txt` l. 75 (`USD 9.89 billion in 2026 to USD 14.06 billion in 2027 and is forecast to reach USD 82.27 billion by 2032 at 42.38% CAGR over 2027-2032`) et l. 81 (`solutions held a 61.21% Agentic AI market share in 2026`).
  - Constat initial : imprécis — la période `sur 2027–2032` du TCAC de 42,38 % n'était pas précisée. Ajoutée.
  - Verdict final : supporté
- `ch03-P25-A02` — « Salesforce dépassant 1,5 G\$ US de revenus récurrents annualisés sur Agentforce (incluant Slackbot et Headless 360 AI) au deuxième trimestre de son exercice 2027 »
  - Source : `[19] SRC-012.txt` l. 162 (`Salesforce's Agentforce annual recurring revenue exceeded USD 1.5 billion in Q2 FY2027, ended July 31, 2026, including Slackbot and Headless 360 AI offerings`).
  - Constat initial : imprécis — la formulation initiale (« sur Agentforce et Slack ») suggérait deux gammes indépendantes plutôt que l'inclusion de Slackbot et Headless 360 AI dans le chiffre Agentforce. Corrigé.
  - Verdict final : supporté
- `ch03-P25-A03` — « tandis que Microsoft a lancé Agent 365 en disponibilité générale en mai 2026 comme plan de contrôle visant à observer, gouverner et sécuriser autant ses propres agents que ceux de partenaires tiers [19]. »
  - Source : `[19] SRC-012.txt` l. 267 (`Microsoft made Agent 365 generally available to commercial customers in May 2026 as a control plane for observing, governing, and securing agents. Its scope includes Microsoft-built and ecosystem-partner agents`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P25-A04` — « Ce mouvement révèle où se fixe la rente : non plus seulement dans l'interface applicative, mais dans le plan de contrôle transversal. »
  - Source : analyse stratégique directement appuyée sur l'exemple d'Agent 365 (`control plane`, `P25-A03`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P25-A05` — « Mordor Intelligence chiffre d'ailleurs explicitement le « manque d'interopérabilité et verrouillage fournisseur » parmi les freins notables du marché (−1,5 % sur le taux de croissance annuel composé à moyen terme) [19] »
  - Source : `[19] SRC-012.txt` l. 143 (`Lack of interoperability / vendor lock-in`, `-1.5%`, `Medium term (2-4 years)` dans le tableau `Restraints Impact Analysis`, `% Impact on CAGR Forecast`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P25-A06` — « tandis que Deloitte met en garde contre la formation de « jardins clos » (*walled gardens*) et la fragmentation incontrôlée d'agents (*AI agent sprawl*) [4]. »
  - Source : `[4] SRC-011.txt` l. 553 (`"walled gardens," where companies are locked into one communication protocol and agent ecosystem`) et l. 515 (`AI agent sprawl`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P26` (lignes 65-70 — Spécifications `MCP` `[20]` et `A2A` `[21]`)
- `ch03-P26-A01` — « Le cœur du diagnostic est donc une asymétrie trompeuse : **« ouvert sur le fil, fermé sur le plan de contrôle »**. Nombre d'équipes présument qu'une suite compatible avec `MCP` et `A2A` est devenue interopérable et réversible. La lecture des deux spécifications primaires démontre l'inverse : »
  - Source : thèse analytique étayée par `P26-A02` et `P26-A03`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P26-A02` — « **Sur l'axe vertical**, la spécification `MCP` (révision du 25 novembre 2025) normalise sur `JSON-RPC 2.0` l'exposition des ressources, gabarits et outils par des serveurs à des applications hôtes, mais avertit explicitement que le protocole lui-même ne peut pas faire respecter ses principes de consentement, de confidentialité ni de sécurité d'exécution au niveau du protocole [20]. »
  - Source : `[20] SRC-038.txt` l. 54-88 (`JSON-RPC 2.0`, `Hosts`, `Servers`, `Resources`, `Prompts`, `Tools`), l. 117-161 (`While MCP itself cannot enforce these security principles at the protocol level`), et `ch03-sources.md` l. 203-207 (`Revision 2025-11-25`).
  - Constat initial : imprécis — la version initiale écrivait « au niveau du fil » au lieu de « au niveau du protocole » (`at the protocol level`, l. 161). Harmonisé littéralement avec `SRC-038.txt`.
  - Verdict final : supporté
- `ch03-P26-A03` — « **Sur l'axe horizontal**, la spécification `A2A` (version 1.0.0) facilite la découverte par *Agent Cards* et l'échange asynchrone de tâches via `JSON-RPC`, `gRPC` ou `HTTP/REST`, mais repose explicitement sur le principe d'**exécution opaque (*Opaque Execution*)**, permettant aux agents de collaborer sans jamais exposer leur état interne, leur mémoire ni leurs outils [21]. »
  - Source : `[21] SRC-039.txt` l. 961 (`Latest Released Version 1.0.0`), l. 985 (`without needing access to each other's internal state, memory, or tools`), l. 995-999, l. 1011 (`Opaque Execution`), l. 1043 (`JSON-RPC, gRPC, HTTP/REST`), l. 1093 (`Agent Card`).
  - Constat initial : non supporté — la version initiale affirmait « (version 1.0, 2026, sous égide *Linux Foundation*) ». Or `SRC-039.txt` ne mentionne nulle part « Linux Foundation » ni l'année « 2026 » pour la version 1.0.0 (ce texte indique uniquement `Latest Released Version 1.0.0` et `Author: A2A Protocol Working Group`). Mentions non vérifiées supprimées et version rectifiée à `1.0.0`.
  - Verdict final : supporté
- `ch03-P26-A04` — « Un éditeur peut donc arborer une conformité sans faille *sur le fil* tout en maintenant fermés *sur son plan de contrôle* les actifs décisifs : le registre des autorisations, la sémantique métier et la mémoire accumulée par l'usage, les plafonds d'engagement, le choix ou le remplacement du modèle de fondation et le journal d'audit brut. »
  - Source : synthèse critique découlant des limites démontrées dans `[20]` et `[21]` et du diagnostic du chapitre.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P26-A05` — « L'interopérabilité syntaxique (traitée au chapitre 05) ne confère ni neutralité de gouvernance ni réversibilité. »
  - Source : renvoi structurel interne et `registre/glossaire-termes.json` l. 84-88 (`interopérabilité verticale et horizontale`, ch05).
  - Constat initial : supporté
  - Verdict final : supporté

### `P27` (ligne 72 — Dette cognitive, dette d'intention et abandon cognitif `[18]`)
- `ch03-P27-A01` — « À ce verrouillage contractuel et technique s'ajoute un verrouillage cognitif analysé par Margaret-Anne Storey dans une prépublication de mars 2026 [18]. »
  - Source : `[18] SRC-040.txt` l. 1-5 (`Margaret-Anne Storey`, `University of Victoria`) et `ch03-sources.md` l. 185 (`2026-03-23`, `arXiv:2603.22106`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P27-A02` — « À côté de la dette technique du code, Storey formalise la **dette cognitive** — érosion de la compréhension partagée formant la « théorie du système » d'une équipe (Naur, cité dans [18]) — »
  - Source : `[18] SRC-040.txt` l. 14, 19-20, 48-50 (`"theory of the system" [Naur 1985]`, `cognitive debt refers to erosion of shared understanding across a team over time`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P27-A03` — « et la **dette d'intention**, perte des objectifs, contraintes et justifications expliquant *pourquoi* un système agit ainsi [18]. »
  - Source : `[18] SRC-040.txt` l. 20-23, 156-158 (`intent debt refers to a lack of externalized goals, constraints, and rationale`).
  - Constat initial : imprécis — la version initiale ajoutait « contraintes réglementaires », qualificatif absent de `SRC-040.txt`. Supprimé.
  - Verdict final : supporté
- `ch03-P27-A04` — « Configurer en langage naturel cinq agents `SaaS` autonomes sans consigner leurs règles en artefacts communs expose l'organisation à l'abandon cognitif (*cognitive surrender*, Shaw et Nave, cités dans [18]) : elle adopte ces comportements sans examen critique et ignore ce que font ses processus. Même si le fournisseur restitue les données brutes en fin de contrat, l'entreprise incapable de reconstituer son intention demeure captive. »
  - Source : `[18] SRC-040.txt` l. 100-109 (`what Shaw and Nave [2026] refer to as cognitive surrender: adopting AI outputs with minimal scrutiny`).
  - Constat initial : imprécis — l'articulation initiale laissait entendre que le scénario `SaaS` était directement étudié par Shaw et Nave. Reformulé pour montrer l'application du concept de Shaw et Nave (cités dans `[18]`) au scénario de configuration `SaaS`.
  - Verdict final : supporté

### `P28` (ligne 74 — Symptômes des dettes cognitive et d'intention `[18]`)
- `ch03-P28-A01` — « Storey recense des symptômes concrets qui trahissent cette érosion bien avant une rupture contractuelle : une résistance des équipes à toucher des modules opaques, des régressions imprévues après des retouches mineures, une intégration laborieuse des nouveaux arrivants faute de connaître le *pourquoi* des règles, et la perte de la mémoire transactive — personne ne sait plus qui détient le contexte d'une décision [18]. »
  - Source : `[18] SRC-040.txt` l. 124-133 (`Resistance to change`, `Unexpected results`, `Slow or unpredictable onboarding`, `Loss of transactive memory [Wegner 1987, Herbsleb 2007]`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P28-A02` — « Du côté de l'intention, les contraintes non fonctionnelles comme les budgets de performance, les règles de confidentialité ou les exigences d'accessibilité s'effacent progressivement, »
  - Source : `[18] SRC-040.txt` l. 191-192 (`non-functional requirements such as performance budgets, privacy constraints, accessibility requirements, are known to a few people and are gradually forgotten`).
  - Constat initial : imprécis — la version initiale traduisait *performance budgets* par « plafonds de latence », plus restrictif que l'original. Rectifié en « budgets de performance ».
  - Verdict final : supporté
- `ch03-P28-A03` — « tandis que les agents eux-mêmes multiplient les demandes de clarification ou produisent des résultats techniquement exacts mais hors sujet [18]. »
  - Source : `[18] SRC-040.txt` l. 189-190 (`AI agents may require extensive clarification, may produce solutions that are technically correct but miss the point`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P29` (ligne 76 — Ligne directrice `B-10` du `BSIF` `[22]`)
- `ch03-P29-A01` — « Dans les institutions financières réglementées au Canada fédéral, ce verrouillage heurte les attentes de la ligne directrice `B-10` du `BSIF` (avril 2023) sur le risque lié aux tiers [22]. »
  - Source : `[22] SRC-068.txt` l. 46, 121, 295 (`Third-Party Risk Management Guideline`, `April 30, 2023`, `federally regulated financial institutions`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P29-A02` — « Selon son Principe 1, l'institution garde l'entière imputabilité des fonctions imparties [22]. »
  - Source : `[22] SRC-068.txt` l. 443-447 (`Principle 1: The FRFI is ultimately accountable`, `retains accountability for business activities, functions, and services outsourced to third parties`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P29-A03` — « Pour les accords critiques ou à risque élevé, elle doit évaluer la concentration spécifique et systémique (§ 2.2.3), encadrer les sous-traitants de rang *n* (§ 2.2.4 — englobant les fournisseurs de modèles embarqués), »
  - Source : `[22] SRC-068.txt` l. 543 (`critical third-party arrangements and those that pose a high risk`), l. 315 et 643-647 (`2.2.3 Concentration risk`: spécifique et systémique), l. 649-675 (`2.2.4 Subcontracting risk`, Principe 5).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P29-A04` — « préserver droits d'information et d'audit indépendant (§ 2.3.3), maintenir des registres intelligibles sans coûts additionnels (§ 2.3.2.2), »
  - Source : `[22] SRC-068.txt` l. 731-747 (`2.3.3 Information rights and audit`, `right to conduct or commission an independent audit`) et l. 715-725 (`2.3.2.2 Record keeping requirements`: `accessible and intelligible without incurring additional costs`).
  - Constat initial : imprécis — la version initiale écrivait « sans frais prohibitifs »; la section § 2.3.2.2 demande littéralement `without incurring additional costs` (« sans coûts additionnels »). Rectifié.
  - Verdict final : supporté
- `ch03-P29-A05` — « évaluer la portabilité infonuagique (§ 4.4) »
  - Source : `[22] SRC-068.txt` l. 993-997 (`4.4 Cloud portability is considered`, `assess benefits and risks of portability`).
  - Constat initial : imprécis — la version initiale omettait le qualificatif *infonuagique* (`Cloud portability`) propre à § 4.4. Ajouté.
  - Verdict final : supporté
- `ch03-P29-A06` — « et documenter des **plans de sortie** planifiée ou sous contrainte (§ 2.3.5) [22]. »
  - Source : `[22] SRC-068.txt` l. 323 et l. 775-793 (`2.3.5 Contingency and exit strategy / planning`: `planned (i.e. non-stressed) or unplanned (i.e. stressed) exit`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P29-A07` — « Même face à un contrat standardisé non négociable (§ 3.1), `B-10` attend une gestion par redondances, contournements, continuité des activités et résilience (§ A2 et § 3.1) [22]; un plan de contrôle fermé rend ces garde-fous inopérants. »
  - Source : `[22] SRC-068.txt` l. 309 (`§ A2`: `expects the FRFI to manage risk... through monitoring, business continuity measures, contingency planning, and other resiliency mechanisms`) et l. 889-898 (`3.1 Standardized contracts`: `may consider... redundancies, workarounds, business continuity measures, and other resiliency mechanisms`).
  - Constat initial : imprécis — la version initiale employait le verbe « exige » là où § A2 utilise `expects` et § 3.1.1 utilise `may consider`. Aligné fidèlement sur `attend` et les références `§ A2 et § 3.1`.
  - Verdict final : supporté

---

## Section 3.4 — La matrice de portefeuille : quand acheter (SaaS), quand assembler sur standards ouverts et quand bâtir en propre

### `P30` (ligne 80 — Posture par défaut)
- `ch03-P30-A01` — « L'alternative crédible — qui constitue la **posture par défaut** de cet ouvrage — consiste à **assembler sur standards ouverts autour d'un noyau de contrôle déterministe possédé**, tout en utilisant les modèles de fondation comme des moteurs substituables. »
  - Source : énoncé normatif de l'ouvrage en cohérence avec `registre/glossaire-termes.json` l. 66-70 (`noyau de contrôle déterministe`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P31` (ligne 82 — Étude `MAP` `[7]` et cadre `CoALA` `[6]`)
- `ch03-P31-A01` — « Dans l'étude `MAP` (*Measuring Agents in Production*, prépublication de Pan *et al.* portant sur 20 études de cas et 86 systèmes déployés en production ou pilote tirés de 306 répondants sur 26 domaines), »
  - Source : `[7] SRC-027.txt` l. 110-124 (`20 in-depth interviews`, `306 practitioners... across 26 domains`, `86 systems in production or pilot phases`), `ch03-sources.md` l. 75-80.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P31-A02` — « 70 % des études de cas s'appuient sur des modèles sur étagère sans réentraîner les poids »
  - Source : `[7] SRC-027.txt` l. 541-543 (`Fourteen of 20 cases (70%) use off-the-shelf models without supervised fine-tuning (SFT) or reinforcement learning (RL)`, dont 17 fermés et 3 ouverts selon Fig. 5 l. 558).
  - Constat initial : imprécis — la version initiale ajoutait « commerciaux » (« modèles commerciaux sur étagère ») et attribuait ce chiffre aux « équipes » sans préciser le sous-échantillon des études de cas. Rectifié en « 70 % des études de cas s'appuient sur des modèles sur étagère ».
  - Verdict final : supporté
- `ch03-P31-A03` — « et 79 % des systèmes sondés emploient des invites rédigées manuellement (seules ou assistées par `LLM`); »
  - Source : `[7] SRC-027.txt` l. 600-635 (`34% use manual hard-coded prompts, and 45% use manual drafting augmented by LLMs... Finding 8: Survey data shows humans dominate prompt construction (79% manual or manual+LLM)`).
  - Constat initial : imprécis — la version initiale écrivait simplement « construisent leurs invites manuellement », omettant la part `manual+LLM` incluse dans les 79 %. Précisé.
  - Verdict final : supporté
- `ch03-P31-A04` — « 80 % des études de cas (16 sur 20) enferment ces appels dans des flux structurés fixes, »
  - Source : `[7] SRC-027.txt` l. 639-640 (`Eighty percent (16/20) of case studies use structured workflows`), `registre/faits-empiriques.json` l. 56-64 (`FACT-MAP-STUDY`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P31-A05` — « 68 % des systèmes sondés bornent l'exécution à au plus 10 étapes avant intervention humaine, »
  - Source : `[7] SRC-027.txt` l. 25, 135 (`68% execute at most 10 steps before human intervention`, `≤10 steps`), `registre/faits-empiriques.json` (`FACT-MAP-STUDY`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P31-A06` — « 74 % s'appuient sur une évaluation humaine dans la boucle »
  - Source : `[7] SRC-027.txt` l. 139-140, 773, 795 (`human-in-the-loop evaluation (74%)`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P31-A07` — « et 75 % des études de cas se passent de bancs d'essai formels au profit de tests `A/B`, de retours d'utilisateurs et d'experts ou de suivi en production pour soutenir la fiabilité [7]. »
  - Source : `[7] SRC-027.txt` l. 142-144 (`75% of teams forgo formal benchmarking, relying instead on A/B testing or expert feedback`) et l. 753-756 (`Case study data... 75% evaluate without benchmark sets, relying instead on A/B testing, user feedback, and production monitoring`).
  - Constat initial : imprécis — la version initiale parlait de « bancs d'essai académiques », alors que `SRC-027.txt` parle de `formal benchmarking` / `benchmark sets` (curated task sets with expected outputs). Corrigé.
  - Verdict final : supporté
- `ch03-P31-A08` — « Sur le plan conceptuel, le cadre évalué par les pairs `CoALA` de Sumers, Yao, Narasimhan et Griffiths (*TMLR*, 2024) montre précisément pourquoi le modèle de langage n'est qu'un composant statistique au sein d'un programme de contrôle explicite gérant mémoire de travail, mémoires à long terme et actions externes [6]. »
  - Source : `[6] SRC-026.txt` l. 1-6 (`Published in Transactions on Machine Learning Research (02/2024)`), l. 237 (`probabilistic input-output system`), l. 479-491 (`working memory and several long-term memories`), l. 636-640 (`top-level or "main" agent program`), `ch03-sources.md` l. 70 (`Évalué par les pairs : Oui`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P32` (ligne 84 — Deloitte `[4]` et Mordor/DataRobot `[19]`)
- `ch03-P32-A01` — « Deloitte décrit le même arbitrage stratégique : les plateformes internes centrales réduisent la dépendance fournisseur et préservent la maîtrise des données et des agents, alors que les outils sur étagère accélèrent les premiers essais [4]. »
  - Source : `[4] SRC-011.txt` l. 559 (`central in-house platforms can limit vendor dependency and increase data and agent control. However, off-the-shelf platforms can help accelerate testing and manage the cost of innovation`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P32-A02` — « selon Mordor Intelligence, le déploiement hybride affiche la plus forte croissance projetée (44,85 % de taux annuel composé sur 2027–2032 face à 59,83 % de part en 2026 pour le déploiement en nuage), »
  - Source : `[19] SRC-012.txt` l. 83 (`Cloud led deployment modes with a 59.83% share of the Agentic AI market size in 2026, and hybrid is forecast to grow fastest at 44.85% CAGR over 2027-2032`).
  - Constat initial : imprécis — la version initiale écrivait « nuage public » pour la part de 59,83 %, confondant la catégorie `Cloud` (l. 83) avec un sondage IDC séparé sur le `public cloud` (l. 171). Rectifié en « déploiement en nuage ».
  - Verdict final : supporté
- `ch03-P32-A03` — « tandis que 63 % des 413 praticiens et dirigeants interrogés par DataRobot en 2026 dans les secteurs réglementés déclarent exiger un déploiement sur site pour l'IA agentique [19]. »
  - Source : `[19] SRC-012.txt` l. 173 (`in regulated industries, where 63% of 413 AI practitioners and leaders surveyed by DataRobot in 2026 said their organizations required it [on-premises deployment] for agentic AI`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P32-A04` — « Pour appliquer cette discipline cas par cas, la direction et l'architecture doivent passer chaque initiative au crible de l'arbre d'arbitrage présenté à la figure suivante. »
  - Source : phrase de transition introduisant `P33`.
  - Constat initial : supporté
  - Verdict final : supporté

### `P33` (lignes 88-92 — Figure 06 et arbre d'arbitrage)
- `ch03-P33-A01` — « *Figure 06 — Arbre d'arbitrage du portefeuille agentique guidant le choix entre achat en SaaS, assemblage sur standards ouverts (posture par défaut 80/20) et construction interne du noyau métier.* »
  - Source : légende de figure de synthèse normative (`registre/glossaire-termes.json` : `partition 80/20`, `noyau de contrôle déterministe`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P33-A02` — « Si le cas d'usage n'est ni différenciant ni critique pour le mandat (première porte), l'achat `SaaS` n'est autorisé que si l'éditeur ouvre son plan de contrôle et sa piste d'audit (deuxième porte) et assure une portabilité acceptable (troisième porte) [16, 22]; sinon, l'organisation rejette l'agent captif, le confine en boîte isolée ou impose par contrat un sas d'exportation et des plafonds d'actions. »
  - Source : critères économiques et prudentiels ancrés sur `[16] SRC-004.txt` (lock-in, inspectabilité, portabilité) et `[22] SRC-068.txt` (§ 2.3.2.2, § 2.3.3, § 2.3.5, § 4.4).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P33-A03` — « Dès que le flux est critique ou différenciant, la branche supérieure oriente par défaut vers **l'assemblage sur standards ouverts** (`MCP` [20], `A2A` [21], enveloppes `CloudEvents` [13], clés d'idempotence `IETF` [14] et exécution durable par rejeu déterministe [12]) encadrés par un harnais interne en posture 80/20 (chapitres 04 à 06). »
  - Source : `[20] SRC-038.txt`, `[21] SRC-039.txt`, `[13] SRC-035.txt` (`CloudEvents v1.0.2`), `[14] SRC-036.txt` (`draft-ietf-httpapi-idempotency-key-header-09`), `[12] SRC-034.txt` (`Temporal SDKs`, `Event History`, `Replay`, `deterministic constraints`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P33-A04` — « Enfin, **construire en propre** ne se justifie à la cinquième porte que pour un actif métier propriétaire ou une contrainte stricte de souveraineté »
  - Source : recommandation d'arbitrage de l'ouvrage cohérente avec les contraintes sur site des secteurs réglementés (`[19] SRC-012.txt` l. 173).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P33-A05` — « et vise alors le noyau déterministe et la couche sémantique, en conservant un modèle de fondation substituable confiné à l'inférence bornée [6, 7]. »
  - Source : `[6] SRC-026.txt` (LLM comme composant au sein d'un programme de contrôle) et `[7] SRC-027.txt` (70 % sur étagère sans réentraîner les poids, flux bornés).
  - Constat initial : supporté
  - Verdict final : supporté

### `P34` (lignes 94-103 — Tableau comparatif des trois postures)
- `ch03-P34-A01` — Ligne **Neutralité de gouvernance** : *self-preferencing* et sous-traitants opaques `[16, 22]`, raccordement `MCP` `[20]` et `A2A` `[21]`, hébergement hybride ou sur site `[19]`.
  - Source : `[16] SRC-004.txt`, `[22] SRC-068.txt`, `[20] SRC-038.txt`, `[21] SRC-039.txt`, `[19] SRC-012.txt`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P34-A02` — Ligne **Déterminisme des frontières** : limites d'inspectabilité/sécurité `[16, 20]`, isolation contrôle/données `[3]`, flux structurés de terrain `[7]`, discipline contre l'abandon cognitif `[18]`.
  - Source : `[16] SRC-004.txt`, `[20] SRC-038.txt`, `[3] SRC-007.txt`, `[7] SRC-027.txt`, `[18] SRC-040.txt`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P34-A03` — Ligne **Tolérance aux pannes** : réconciliation absente sur flux longs `[2, 22]`, exécution durable `[12]`, idempotence `[14]`, sagas compensatoires `[2, 11]`, `CloudEvents` `[13]`, tests de défaillance `[8]`.
  - Source : `[2] SRC-006.txt`, `[11] SRC-033.txt`, `[12] SRC-034.txt`, `[13] SRC-035.txt`, `[14] SRC-036.txt`, `[8] SRC-028.txt`, `[22] SRC-068.txt`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P34-A04` — Ligne **Coût marginal à l'échelle** : risques coûts/verrouillage `[4, 16, 19]`, modèles sur étagère `[7]`, évitement des débats redondants `[9, 10]`.
  - Source : `[4] SRC-011.txt`, `[16] SRC-004.txt`, `[19] SRC-012.txt`, `[7] SRC-027.txt`, `[9] SRC-031.txt`, `[10] SRC-032.txt`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P34-A05` — Ligne **Coût de sortie** : captivité et plan de sortie `BSIF B-10` `[18, 19, 22]`, contrats ouverts et spécifications internes `[18, 20]`, maintien des compétences et de l'intention écrite `[18]`.
  - Source : `[18] SRC-040.txt`, `[19] SRC-012.txt`, `[20] SRC-038.txt`, `[22] SRC-068.txt`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P34-A06` — Ligne **Périmètre recommandé** : usages non différenciants sous clauses d'export `[16, 22]`, majorité des flux critiques en assemblage, cœur métier ou exigences sur site `[19]`.
  - Source : `[16] SRC-004.txt`, `[22] SRC-068.txt`, `[19] SRC-012.txt`.
  - Constat initial : supporté
  - Verdict final : supporté

### `P35` (ligne 105 — Garde-fous contre la multiplication d'agents et l'opacité)
- `ch03-P35-A01` — « à budget de jetons de raisonnement égal, Tran et Kiela montrent qu'un agent unique égale ou surpasse les systèmes multi-agents sur le raisonnement à sauts multiples tant que le contexte ne sature pas [9], »
  - Source : `[9] SRC-031.txt` l. 10-22, 214-224 (`SAS consistently match or outperform MAS on multi-hop reasoning tasks when reasoning tokens are held constant`, compétitif seulement lorsque `effective single-agent context utilization deteriorates`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P35-A02` — « Bertalanič et Fortuna observent un effet Ringelmann où la taille effective plafonne vers 1,2 à 1,8 agent même avec 30 agents nominaux en débat [10], »
  - Source : `[10] SRC-032.txt` l. 296, 301, 308 (`Under dense debate... asymptotic ceilings 1/c ≈ 1.2, 1.8, 1.2`, `Neff saturates near 1.8 on GSM-Hard and ~1.2 on MCQA` à `N=30`), `registre/glossaire-termes.json` l. 114-118 (`effet Ringelmann multi-agents`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P35-A03` — « et Kim *et al.* mesurent des surcoûts de coordination de 58 % à 515 % pour des écarts allant de +80,8 % sur tâches financières décomposables à −70,0 % sur la planification séquentielle [1]. »
  - Source : `[1] SRC-003.txt` l. 18-19 (`+80.8% on decomposable financial reasoning to −70.0% on sequential planning`), l. 624-626 (`communication overhead... from 0% (SAS) to 515% (Hybrid), with Independent at 58%`), l. 946 (`overhead: independent (58%)... hybrid (515%)`).
  - Constat initial : imprécis — la version initiale employait « surcoûts d'interaction », alors que `SRC-003.txt` les nomme explicitement `communication overhead` / `coordination overhead`. Aligné sur « surcoûts de coordination ».
  - Verdict final : supporté
- `ch03-P35-A04` — « Ensuite, construire en propre n'immunise pas contre l'opacité si l'équipe accumule dette cognitive et dette d'intention faute d'externaliser ses spécifications, dossiers de décision architecturale et tests d'intention [18]. »
  - Source : `[18] SRC-040.txt` l. 168-183, 196-206.
  - Constat initial : supporté
  - Verdict final : supporté

### `P36` (ligne 107 — Trois familles d'artefacts vivants selon Storey `[18]`)
- `ch03-P36-A01` — « Pour contenir cette dette dès la conception, Storey recommande trois familles d'artefacts vivants maintenus en parallèle du code [18]. »
  - Source : `[18] SRC-040.txt` l. 196-209 (`investing in "living" artifacts that externalize goals, plans, constraints, and reasoning`, trois puces).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P36-A02` — « Les spécifications et tests d'intention exécutables, de style développement piloté par le comportement (`BDD`), capturent et vérifient la finalité visée plutôt que le seul comportement technique et détectent tôt les dérives d'exécution [18]. »
  - Source : `[18] SRC-040.txt` l. 198-200 (`Executable intent. BDD specifications and tests designed to capture purpose rather than just verify behavior... show that the system has drifted from its intent`).
  - Constat initial : imprécis — formulation initialement limitée à « vérifient la finalité métier plutôt que la seule mécanique logicielle ». Rapprochée de `capture purpose rather than just verify behavior`.
  - Verdict final : supporté
- `ch03-P36-A03` — « Les dossiers de décision architecturale consignent ce qui a été tranché, les raisons retenues et les options écartées, complétés par une modélisation collaborative et un langage ubiquitaire du domaine [18]. »
  - Source : `[18] SRC-040.txt` l. 203-206 (`Architectural Decision Records (ADRs) capture what was decided, why, and what was not done`, `Domain-Driven Design`, `ubiquitous language and collaborative domain modelling`).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P36-A04` — « Enfin, les artefacts de contexte — instructions d'agents, carnets opératoires et compétences documentées — rendent ces contraintes lisibles autant par les humains que par les agents, sans jamais dispenser du jugement humain [18]. »
  - Source : `[18] SRC-040.txt` l. 207-211 (`Context artifacts... skills, agent instructions, and playbooks... used by both humans and agents`, `cannot replace the hard human work of making decisions and exercising creative judgment`).
  - Constat initial : supporté
  - Verdict final : supporté

### `P37` (lignes 109-115 — Encadré « Trois arbitrages sans regret — Chapitre 03 »)
- `ch03-P37-A01` — Arbitrage 1 : gel de l'activation non gouvernée d'agents `SaaS` en écriture, revue du plan de contrôle, des sous-traitants de rang *n*, des journaux bruts et du plan de sortie, y compris pour contrats standardisés non négociables compensés par plans de résilience `[22]`.
  - Source : `[22] SRC-068.txt` (§ 2.2.4, § 2.3.2.2, § 2.3.3, § 2.3.5, § 3.1).
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P37-A02` — Arbitrage 2 : assemblage sur standards ouverts (`MCP` `[20]`, `A2A` `[21]`, `CloudEvents` `[13]`, idempotence `[14]`, exécution durable `[12]`) sans réentraîner de poids ni multiplier des essaims non justifiés `[7, 9, 10]`.
  - Source : `[20] SRC-038.txt`, `[21] SRC-039.txt`, `[13] SRC-035.txt`, `[14] SRC-036.txt`, `[12] SRC-034.txt`, `[7] SRC-027.txt`, `[9] SRC-031.txt`, `[10] SRC-032.txt`.
  - Constat initial : supporté
  - Verdict final : supporté
- `ch03-P37-A03` — Arbitrage 3 : capture de l'intention métier, contraintes non fonctionnelles, `ADR` et tests d'intention exécutables en dépôts versionnés `[18]`.
  - Source : `[18] SRC-040.txt` l. 191-209.
  - Constat initial : supporté
  - Verdict final : supporté

### `P38` (ligne 117 — Transition vers la Partie II et le Chapitre 04)
- `ch03-P38-A01` — « La carte stratégique de la Partie I est désormais complète [...] La **Partie II** franchit le pas de l'économie au génie logiciel en ouvrant au **Chapitre 04** l'architecture détaillée du noyau déterministe en `80/20`, des sagas compensatoires et des quatre plans à posséder en propre pour rendre tout modèle jetable. »
  - Source : transition éditoriale vers `ch04` cohérente avec `registre/glossaire-termes.json` (`partition 80/20`, `noyau de contrôle déterministe`, `saga à point pivot`).
  - Constat initial : supporté
  - Verdict final : supporté
