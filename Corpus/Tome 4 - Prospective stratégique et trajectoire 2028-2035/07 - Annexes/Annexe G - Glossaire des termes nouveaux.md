# Annexe G — Glossaire des termes nouveaux

Cette annexe définit de manière normative les concepts méthodologiques, architecturaux, cryptographiques et réglementaires propres à l’édition 2028-2035 ou précisés par rapport au glossaire du Compendium 2027 (C27, annexe A), ainsi que les termes normalisés issus de l’audit terminologique de 2027. Chaque entrée indique son équivalent technique anglais lorsqu’un standard international l’emploie et renvoie aux chapitres principaux qui l’instrumentent.

## Agilité cryptographique (*cryptographic agility*)

Aptitude architecturale d’un système d’identité, de transport ou d’archivage à remplacer ses algorithmes de chiffrement, d’encapsulation de clés ou de signature numérique — ainsi que ses formats de certificats et ses modules matériels — par configuration et automatisation, sans réécrire la logique applicative des agents ni interrompre la continuité opérationnelle (`M-5`, `M-10`, `CAP-040`).

## Ancre datée ou annoncée (*dated or announced anchor*)

Échéance externe inscrite dans `Master/registre/ancres.json` et l’Annexe A, appuyée sur un texte primaire lu localement (`statut L+`). Elle est dite *datée* lorsqu’une loi sanctionnée, un règlement officiel ou une norme impérative en fixe le jour d’entrée en vigueur, et *annoncée* lorsqu’elle provient d’un projet réglementaire, d’une charte de normalisation ou d’une feuille de route publique non contraignante (`M-1`, `M-3` à `M-5`).

## Antipatron (*anti-pattern*)

Solution d’architecture ou de gouvernance d’apparence commode mais produisant de façon récurrente une défaillance de sécurité, de conformité ou de coût — par exemple partager un jeton statique entre agents, coder en dur des attributs expérimentaux de télémétrie dans le métier ou solliciter une approbation humaine répétitive engendrant une validation réflexe (`M-3`, `M-4`, `M-9`, `M-26`; C27, § 22.5, § 23.9).

## Capacité conditionnelle (*conditional capability*)

Capacité de la carte cible (`CAP-nnn`) dont l’utilité nette dépend de la réalisation d’un ou de deux des scénarios prospectifs (`A`, `B` ou `C`). Elle est conçue dès l’architecture cible mais son déploiement général reste différé jusqu’au franchissement d’un signal de révision identifié (`M-10`, `M-11`, `M-23`).

## Capacité invariante (*invariant capability*)

Capacité de la carte cible (`CAP-nnn`) indispensable à la maîtrise des risques, à la preuve réglementaire et à la réversibilité dans les trois scénarios (`A`, `B` et `C`). L’ensemble des quarante-deux capacités invariantes constitue le socle d’investissement sans regret de l’institution (`M-10`, `M-11`, `M-20`).

## Certificat composite post-quantique (*composite post-quantum certificate*)

Certificat `X.509` normalisé à l’IETF (`RFC 10073`) combinant de façon cryptographiquement indissociable une clé et une signature post-quantiques (`ML-DSA`, `FIPS 204`) avec une clé et une signature classiques (`ECDSA`, `EdDSA` ou `RSA-PSS`). La vérification n’aboutit que si les deux signatures sont valides, prévenant toute attaque par rétrogradation durant la transition 2030-2032 (`M-5`, `CAP-040`).

## Classe de décision (*decision class*)

Échelle normative à six niveaux (`Classe 1` à `Classe 6`) classant toute opération confiée ou proposée à un agent selon sa réversibilité matérielle, son impact juridique ou financier et le fait qu’elle vise ou non une personne physique : lecture sans effet (`Classe 1`), action réversible peu matérielle (`Classe 2`), action matérielle ou coûteuse à renverser (`Classe 3`), action irréversible ou à fort enjeu (`Classe 4`), décision automatisée matérielle visant une personne (`Classe 5`) et modification hors mandat de ses propres permissions, politiques ou journaux (`Classe 6`, toujours interdite) (`M-1`, `M-12`, `M-14` à `M-18`).

## Cloisonnement juridictionnel des substrats d’état (*state-substrate jurisdictional isolation*)

Séparation technique et contractuelle des six lieux où les données d’une interaction agentique persistent ou transitent — mémoire vive d’inférence, journaux de requêtes, caches de préfixes `KV`, index vectoriels ou graphes, points de reprise d’exécution durable et traces d’observabilité — afin de garantir le respect des règles de résidence des livres, d’évaluation de transfert hors Québec et de maîtrise souveraine des clés (`M-6`, `M-9`, `M-18`, `CAP-032`; C27, § 46.1).

## Coût complet par résultat conforme (*cost per compliant successful outcome*)

Unité de mesure économique et FinOps rapportant la dépense totale d’un flux agentique — jetons d’entrée, de raisonnement et de sortie, réessais, invocations d’outils, garde-fous d’évaluation, stockage probatoire et temps humain de revue — au seul nombre de dossiers menés à terme sans erreur matérielle, sans reprise manuelle corrective ni incident de conformité (`M-7`, `M-24`, `CAP-045`; C27, § 40.5, § 50.7).

## Déclencheur de bascule (*trigger*)

Seuil critique précis attaché à un jalon de surveillance (`SIG-nnn`) dont le franchissement attesté oblige les instances de gouvernance à ouvrir sous trente jours une instruction hors cycle afin d’activer une capacité conditionnelle, de modifier un plafond d’autonomie ou de réorienter une initiative avant d’atteindre le seuil d’insuffisance du plan (`M-1`, `M-23`, `M-25`).

## Délégation à portée atténuée (*attenuated delegation*)

Mécanisme cryptographique par lequel chaque saut successif entre un utilisateur humain, un agent orchestrateur et un sous-agent réduit monotoniquement l’ensemble des outils invocables, des ressources accessibles, des plafonds monétaires et de la durée de validité du jeton (`RFC 8693`), interdisant toute escalade latérale de privilèges (`M-4`, `M-5`, `M-10`, `CAP-036`; C27, § 30.2).

## Délégué confus (*confused deputy*)

Vulnérabilité structurelle dans laquelle un agent légitime disposant de permissions étendues sur des systèmes internes est manipulé — notamment par injection indirecte dans un document, un courriel ou une réponse d’outil — pour exécuter une action valide techniquement mais contraire au mandat et aux droits de l’initiateur réel de la requête (`M-3`, `M-4`, `M-6`, `CAP-036`, `CAP-038`; C27, § 30.1, § 31.4).

## Demande de tirage (*pull request*)

Unité formelle et tracée de proposition de modification de code, de politique codifiée, de schéma d’outil ou de compétence procédurale soumise à des contrôles automatisés et à l’approbation indépendante d’une identité distincte de son auteur, garantissant la séparation des tâches exigée par la ligne directrice `B-13` du BSIF avant toute mise en production (`M-3`, `M-10`, `CAP-052`; C27, § 47.1).

## Exécution durable (*durable execution*)

Modèle d’orchestration persistant de manière déterministe l’historique d’événements et les **points de contrôle** d’une tâche de longue durée afin qu’après une panne matérielle, une attente d’approbation humaine de plusieurs jours ou un redémarrage réseau, le flux reprenne exactement à l’étape interrompue sans réexécuter les effets de bord déjà produits (`M-6`, `M-10`, `M-13`, `CAP-008`; C27, § 18.2).

## Fédération selon la gravité des données (*data-gravity federation*)

Patron d’intégration multi-plateformes consistant à laisser un agent spécialisé s’exécuter au plus près du système d’enregistrement où résident massivement les données métier, tout en imposant la traversée du plan de contrôle possédé par l’institution pour l’identité, l’autorisation déterministe et la journalisation d’audit (`M-9`, `M-10`, `M-18`, `CAP-013`; C27, § 27.2, § 27.4).

## Harnais de contrôle agentique (*AI harnessing*)

Enveloppe logicielle déterministe externe au modèle — comprenant passerelles d’outils, listes blanches, moteurs de politiques, bornes budgétaires, filtres d’entrées-sorties et coupe-circuits — qui contraint mécaniquement ce qu’un agent peut percevoir et exécuter, conformément à la terminologie introduite par le bulletin du BSIF de juillet 2026 (`M-3`, `M-9`, `M-10`, `CAP-007`, `CAP-022`).

## Identité légale d’organisation vérifiable (*verifiable organizational identity*)

Attestation cryptographique normalisée — telle que le justificatif `vLEI` encadré par la fondation `GLEIF` ou les justificatifs vérifiables `W3C VC v2.0` — permettant à un agent engagé dans une transaction inter-entreprises de prouver l’existence juridique de la personne morale qui le mandate ainsi que les limites exactes de son pouvoir de représentation (`M-4`, `M-5`, `M-10`, `CAP-041`).

## Identité non humaine parrainée (*sponsored non-human identity*)

Identité cryptographique unique attribuée à une classe ou instance d’agent, distincte de tout compte utilisateur humain et dépourvue de secret statique partagé, mais rattachée dans le registre central à un responsable humain nominatif qui répond de son cycle de vie, de sa portée et de sa révocation (`M-3`, `M-10`, `CAP-035`; C27, § 29.2).

## Jalon de surveillance (*signpost*)

Indicateur factuel observable périodiquement dans les publications réglementaires, les dépôts de standardisation, les avis cryptographiques ou la télémétrie interne afin de suivre l’évolution des incertitudes entourant le plan directeur avant le déclenchement d’une révision (`M-1`, `M-25`).

## Journal de transparence immuable (*append-only transparency log*)

Registre probatoire structuré en arbre de Merkle cryptographique — selon l’architecture `SCITT` (`RFC 9943`) — dans lequel toute entrée ajoutée ne peut être ni altérée ni supprimée rétroactivement sans invalider la racine signée, assurant l’intégrité vérifiable des versions de modèles, de schémas et de pistes d’audit (`M-4`, `M-5`, `CAP-049`).

## Mémoire bi-temporelle (*bi-temporal memory*)

Architecture de mémoire persistante distinguant systématiquement deux axes de temps pour chaque fait stocké — la période de validité métier du fait dans le monde réel et l’horodatage exact où le système en a eu connaissance — afin de reconstituer fidèlement lors d’un audit ou d’un litige ce que l’agent savait au moment précis d’une décision passée tout en permettant l’oubli sélectif conforme à la Loi 25 (`M-6`, `M-10`, `CAP-019`).

## Noyau possédé (*owned control plane*)

Ensemble des composants d’architecture dont l’institution financière conserve la maîtrise directe des schémas, des politiques, des clés et des journaux — registre d’inventaire, émission d’identités non humaines, moteur de décision de politique hors modèle, passerelle d’outils, collecteur de traces et archive probatoire — indépendamment des fournisseurs de modèles ou de suites applicatives (`M-1`, `M-9`, `M-11`, `M-18`).

## OPC UA (*Open Platform Communications Unified Architecture*)

Famille de standards industriels d’échange sécurisé et de modélisation sémantique machine-à-machine employée à la périphérie opérationnelle et cyberphysique pour exposer des mesures de capteurs ou d’équipements sans accorder d’accès direct en écriture aux automates (`M-4`, `CAP-028`; C27, § 28.2).

## Parcours adaptatifs dynamiques (*Dynamic Adaptive Policy Pathways — DAPP*)

Méthode de planification sous incertitude profonde élaborée par Haasnoot, Warren et Kwakkel consistant à engager immédiatement les actions sans regret d’un **plan initial**, à identifier les seuils d’insuffisance de chaque trajectoire et à prépositionner des branches conditionnelles activées sur signaux précoces (`M-1`, `M-8`, `M-23`, `M-25`).

## Plan initial (*initial / base plan*)

Ensemble cohérent d’engagements immédiats du Palier 1 (2028-2029) concentré sur la construction du noyau possédé et des capacités invariantes, conçu pour ne fermer prématurément aucune option face aux scénarios A, B et C (`M-1`, `M-20`, `M-23`, `M-25`).

## Point de contrôle (*checkpoint*)

Double acception technique et gouvernance normalisée : en exécution durable, sauvegarde atomique et sérialisée de l’état d’un flux permettant une reprise exacte après interruption; en supervision humaine, barrière synchrone suspendant l’exécution avant une action de Classe 3, 4 ou 5 jusqu’à la validation explicite et signée d’un préposé habilité liée aux paramètres exacts de l’acte (`M-3`, `M-6`, `M-10`, `CAP-002`, `CAP-008`).

## Porte de passage (*stage gate*)

Point de vérification formel (`POR-nnn`) conditionnant la sortie d’un palier ou l’élévation du plafond d’autonomie d’un domaine d’affaires à au moins une preuve matérielle vérifiable indépendamment des simples déclarations projet (`M-20` à `M-22`, `M-24`).

## Portée autonome d’agent (*agent task horizon / autonomy span*)

Durée et nombre d’étapes interdépendantes qu’un agent accomplit en production à un niveau élevé de fiabilité (typiquement 80 % ou 95 % et au-delà) sans intervention humaine corrective; traitée dans l’ouvrage comme une variable transversale distincte du plafond brut mesuré à 50 % sur bancs d’essai (`M-2`, `M-6`, `M-8`).

## Preuve de possession applicative (*application-layer proof of possession*)

Mécanisme cryptographique — tel que `DPoP` (`RFC 9449`) ou `mTLS` — liant un jeton d’accès ou de délégation à la clé privée détenue par l’agent émetteur afin qu’un jeton exfiltré dans un journal ou sur le réseau demeure inutilisable par un tiers (`M-4`, `M-5`, `CAP-036`).

## Proposition d’exigence sectorielle (*sectoral requirement proposition*)

Prescription nouvelle (`PEX-nnn`) formulée aux chapitres `M-14` à `M-18` pour traduire en contrainte d’architecture vérifiable une obligation légale ou prudentielle propre à la banque, à la gestion de patrimoine, à l’assurance de personnes, à l’assurance de dommages ou au groupe diversifié (`M-1`, `M-14` à `M-18`, Annexe C et Annexe D).

## Réessayable (*retryable*)

Propriété d’une étape d’orchestration ou d’un appel d’outil conçu avec clé d’idempotence et gestion explicite des erreurs transitoires afin de pouvoir être relancé automatiquement après délai d’expiration ou panne partielle sans dupliquer une écriture financière, un virement ou une notification client (`M-6`, `M-10`, `CAP-008`, `CAP-009`; C27, § 18.3).

## Règle du maillon le plus faible (*weakest-link maturity rule*)

Règle méthodologique d’évaluation de la maturité selon laquelle le stade atteint par un domaine d’affaires (`0` à `4`) ne dépasse jamais le niveau du critère le moins avancé parmi sa connectivité technique, son identité et sa sécurité, son observabilité et sa gouvernance réglementaire (`M-2`, `M-12`, `M-19`; C27, § 43.1).

## Scénario sans probabilité (*non-probabilistic scenario*)

Futur cohérent et contrasté (`Scénario A — Socle étendu`, `Scénario B — Archipel`, `Scénario C — Blocs`) utilisé sous incertitude profonde pour éprouver la solidité de l’architecture cible sans lui affecter de poids probabiliste arbitraire (`M-1`, `M-8`, `M-11`).

## Seuil d’insuffisance (*adaptation tipping point*)

Condition réglementaire, cryptographique, économique ou opérationnelle à partir de laquelle une option d’architecture ou un plafond d’autonomie en vigueur cesse d’atteindre ses objectifs de conformité ou de performance et impose le basculement vers une branche alternative (`M-1`, `M-23`, `M-25`).

## Streamable HTTP

Mode de transport sans état introduit et consolidé par le protocole `MCP` (révision `2026-07-28`), permettant d’acheminer sur HTTP standard aussi bien des réponses unitaires que des flux continus d’événements et de notifications serveur sans imposer l’entretien permanent de connexions couplées `HTTP+SSE` (`M-2`, `M-4`, `CAP-022`; C27, § 5.2, § 5.3).

## Sur-horodatage probatoire (*cryptographic re-timestamping*)

Opération périodique consistant à encapsuler et re-signer avec un algorithme post-quantique robuste — notamment `SLH-DSA` (`FIPS 205`, fondé sur les fonctions de hachage) ou un certificat composite — la racine d’un journal d’audit antérieur avant que l’algorithme classique initial ne devienne vulnérable, prolongeant sans rupture sa force probante légale jusqu’en 2035 et au-delà (`M-5`, `M-21`, `CAP-040`, `CAP-049`).
