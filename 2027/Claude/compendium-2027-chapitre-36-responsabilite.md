# Chapitre 36 — Responsabilité

*Question directrice : qui répond des actes d'un agent ?*

> **Version 2 — 11 novembre 2026.** État de référence : article 1714.46 du Code civil de la Californie, en vigueur depuis le 1er janvier 2026; directive (UE) 2024/2853, applicable aux produits mis sur le marché après le 9 décembre 2026; loi type de la CNUDCI sur les contrats automatisés, adoptée le 11 juillet 2024. Les numéros entre crochets renvoient aux sources en fin de chapitre : textes officiels lus [1] à [5], analyses lues [6] à [11], pages de presse et d'entreprise lues [12] et [13], source non lue [14]. Le droit décrit ici n'est pas stabilisé, et ce chapitre n'est pas un avis juridique. Chapitre audité et révisé le 12 novembre 2026.

Un agent commande, répond à un client, paie une facture. Tant qu'il suggérait, une personne décidait et en répondait; dès qu'il agit, ses actes ont des effets juridiques dont quelqu'un doit répondre.

Le droit actuel est net sur un point : il ne reconnaît pas l'agent comme sujet de droit, et la responsabilité remonte toujours à des personnes, physiques ou morales. La répartition entre ces personnes reste ouverte; une note de la Cloud Security Alliance (CSA) du 3 juillet 2026 la juge non résolue devant les tribunaux, les législatures et le marché de l'assurance [6].

La thèse de ce chapitre : en attendant les tribunaux, cette répartition se décide à trois endroits que l'entreprise maîtrise, soit les limites d'autorité qu'elle configure, la preuve qu'elle conserve et les contrats qu'elle signe.

---

## 36.1 L'état du droit : les humains et les entités derrière l'agent

### Pas de personnalité, pas d'excuse

En droit anglais, un système d'IA n'a pas de personnalité juridique et ne peut pas être partie à un contrat; les actes d'un agent sont attribués à la personne qui le déploie [8]. La déclaration finale de la UK Jurisdiction Taskforce (UKJT) sur les dommages causés par l'IA, publiée en 2026 et non contraignante, part du même constat, d'après le résumé d'un cabinet : l'IA n'est pas responsable en tant que telle, et le droit de la négligence comme celui des contrats s'appliquent sans obstacle de principe [11].

La Californie a inscrit la règle dans un texte. L'article 1714.46 de son Code civil, issu du projet de loi AB 316, vise toute action contre un défendeur qui a développé, modifié ou utilisé une IA à laquelle un dommage est imputé : ce défendeur ne peut pas soutenir que l'IA a causé le dommage de façon autonome [1]. Le texte préserve les autres moyens de défense, la preuve relative à la causalité et à la prévisibilité, ainsi que la faute comparée d'autres personnes. Il retire un argument sans créer de régime de responsabilité, et ses trois verbes (développer, modifier, utiliser) visent toute la chaîne, de l'éditeur à l'intégrateur et au déployeur.

Au Canada, la décision *Moffatt c. Air Canada* (2024 BCCRT 149) sert d'illustration : le transporteur a répondu d'une information inexacte donnée par son robot conversationnel, le tribunal ayant écarté l'idée que celui-ci réponde de ses propres actes. Ce résumé repose sur des commentaires [14].

### Un droit en mouvement

Une analyse de Baker McKenzie du 1er juillet 2026 relève que peu de lois et décisions américaines nomment expressément les agents, mais que les principes existants annoncent ce qui sera attendu des entreprises : gouverner, surveiller et expliquer ce que font leurs agents [7].

---

## 36.2 Droit du mandat

### Un piège de vocabulaire

Le mot « agent » désigne en droit anglo-américain le mandataire : une personne qui agit pour une autre, le mandant, et l'engage. Un agent logiciel n'est pas un mandataire en ce sens, faute d'être une personne. Selon le résumé de la déclaration de l'UKJT, la responsabilité du fait d'autrui ne peut pas découler des actes d'une IA, puisqu'elle suppose une personne elle-même responsable; elle peut découler de l'usage négligent qu'une personne fait d'une IA [11]. La version finale ajoute les obligations de protection non délégables, celles d'un employeur ou d'un hôpital, dont le débiteur peut répondre même sans faute.

### Les catégories servent quand même

Les tribunaux et les praticiens raisonnent néanmoins avec deux catégories du mandat [7].

L'**autorité réelle** est ce que le mandant a effectivement permis; il répond des actes accomplis dans ces limites.

L'**autorité apparente** naît quand les paroles ou la conduite du mandant amènent un tiers à croire raisonnablement que l'agent est autorisé. Le mandant peut alors être lié par un acte qu'il n'avait pas permis.

Browne Jacobson note que le cadre suppose une intention et un contrôle humains, et quand un système agit de façon imprévisible, il devient malaisé de dire s'il est resté dans les limites de son autorité [8].

### Traduction en architecture

Ce qui suit est une déduction. L'autorité réelle d'un agent logiciel est ce qui est configuré : portées, politiques, mandats signés (chapitres 10 et 30). Son autorité apparente est ce que le tiers perçoit : le canal, la marque, la carte d'agent, l'absence de limite annoncée. Le risque juridique loge dans l'écart. Un agent qui peut techniquement plus que le permis, et dont rien n'annonce les limites, fabrique de l'autorité apparente. D'où la recommandation de Baker McKenzie : définir et documenter les limites d'autorité de chaque agent, y compris les permissions et les identifiants qui lui sont remis [7].

### Deux cas à surveiller

**Le fournisseur comme mandataire.** Dans *Mobley v. Workday*, selon la CSA, le tribunal a écarté une première théorie mais retenu celle qui fait de l'éditeur d'un logiciel de sélection de candidats le mandataire des employeurs qui s'en servent [6]. Si cette lecture se confirme, un fournisseur de plateforme peut répondre directement envers les tiers, pas seulement envers son client.

**La permission de l'utilisateur ne suffit pas toujours.** Une grande plateforme de commerce en ligne a poursuivi le développeur d'un agent de navigation qui accédait à des comptes clients. Le tribunal de district a accordé une injonction préliminaire fondée sur la loi fédérale sur la fraude informatique, en retenant à ce stade qu'un agent n'hérite pas nécessairement de l'autorisation de son utilisateur; l'injonction a été suspendue en attendant l'appel [7]. L'accès d'un agent au système d'un tiers relève donc aussi de ce que ce tiers autorise (chapitres 9 et 29).

La CSA doute que ces doctrines s'appliquent telles quelles aux systèmes multi-agents [6].

---

## 36.3 Formation des contrats

### La validité est acquise depuis longtemps

Le droit américain admet depuis un quart de siècle qu'un contrat conclu par un programme est valide. La loi fédérale E-SIGN prévoit qu'un contrat ne peut pas être privé d'effet du seul fait que sa formation a fait intervenir un ou plusieurs *electronic agents*, à une condition : que l'action de l'agent soit juridiquement attribuable à la personne à lier [3]. La loi uniforme UETA, lue ici dans sa version californienne, va plus loin : un contrat peut naître de l'interaction des agents électroniques des parties, même si personne n'a connu ni examiné leurs actions ou les termes convenus [4].

Sur le plan international, la CNUDCI a adopté le 11 juillet 2024 une loi type sur les contrats automatisés [5]. Elle reconnaît l'automatisation dans la formation et l'exécution des contrats, pose des règles d'attribution des sorties d'un système automatisé, propose une règle facultative pour les résultats inattendus et interdit d'user d'un tel système pour éluder d'autres exigences légales. C'est un modèle pour les législateurs, non un texte applicable; la page lue ne nomme aucun État qui l'ait repris.

La validité ne dispense donc pas d'établir pour qui l'agent agissait, et dans quelles limites (section 36.2).

### Le vrai problème est l'erreur

Ces textes ont été écrits pour une automatisation déterministe. Browne Jacobson distingue l'échange de données informatisé, outil passif qui exécute des règles fixées par des humains, de l'IA agentique, qui décide [8]. Trois difficultés en découlent en droit anglais.

- L'approche objective de l'intention couvre l'offre d'un agent qui opère dans des paramètres fixés par des personnes décidées à contracter.
- Une transaction entièrement autonome entre deux agents pose la question de l'accord réel : la bataille des formulaires devient une bataille d'algorithmes.
- L'erreur unilatérale n'annule en principe le contrat que si l'autre partie la connaissait, ce qui s'établit mal entre systèmes autonomes.

Par déduction, une entreprise doit tenir pour probable qu'elle sera liée par ce que son agent accepte, y compris par erreur. Les limites se posent donc avant l'engagement : contraintes dans le mandat (chapitre 10), approbation humaine au-delà d'un seuil (chapitre 22). La loi type de la CNUDCI ouvre une seconde voie, puisqu'elle laisse les parties régir par accord l'usage des systèmes automatisés [5] : un contrat-cadre peut dire quels messages d'agent engagent, et comment une erreur se corrige.

---

## 36.4 Responsabilité du fait des produits

### La directive européenne de 2024

La directive (UE) 2024/2853 remplace la directive de 1985, abrogée avec effet au 9 décembre 2026. Les États membres doivent la transposer au plus tard à cette date, et elle s'applique aux produits mis sur le marché ou mis en service après [2]. Ce régime de responsabilité sans faute est le plus structurant pour un éditeur d'agents.

| Disposition | Contenu | Portée pour un système d'agents |
|---|---|---|
| Art. 4 et considérants | Le logiciel est un produit, quel que soit son mode de fourniture; un considérant assimile le fournisseur d'un système d'IA à un fabricant | Un agent distribué commercialement entre dans le champ |
| Art. 7 | Défectuosité appréciée selon la sécurité légitimement attendue; facteurs : capacité d'apprendre après la mise sur le marché, cybersécurité | Le comportement acquis en exploitation compte |
| Art. 9 et 10 | Divulgation de preuves; défectuosité présumée si le défendeur ne divulgue pas, causalité présumée dans certains cas | Journaux et documentation deviennent un moyen de défense |
| Art. 11 | Pas d'exonération quand le défaut tient, sous le contrôle du fabricant, à un logiciel, à une mise à jour ou à l'absence de mise à jour de sécurité | L'état du produit à sa sortie ne protège pas |
| Art. 6 | Dommages couverts : décès, lésions corporelles, biens non exclusivement professionnels, données à usage non professionnel | Les pertes entre entreprises restent hors champ |

Le logiciel libre fourni hors de toute activité commerciale est exclu (art. 2). La directive protège des personnes physiques : une entreprise qui subit une perte commerciale du fait d'un agent acheté n'y trouve pas de recours : seul son contrat la protège (section 36.6). En revanche, une entreprise qui met un agent à la disposition de consommateurs européens s'expose comme fabricant, avec une preuve allégée pour la victime.

La directive distincte sur la responsabilité en matière d'IA, qui devait traiter la faute, a été retirée par la Commission en 2025, selon la CSA, qui date cette décision de février [6]. La faute relève donc du droit de chaque État membre.

### Aux États-Unis

Il n'existe pas de texte équivalent. La qualification de produit se joue devant les tribunaux : dans *Garcia v. Character Technologies*, une application conversationnelle a été traitée comme un produit à un stade préliminaire, selon la CSA, qui range cette décision parmi les non définitives [6]. Un règlement a toutefois été annoncé en janvier 2026 [12] : cette qualification ne sera vraisemblablement pas éprouvée en appel. Les obligations réglementaires sont au chapitre 35.

---

## 36.5 Assurance

« Assurance » désigne ici la couverture financière d'un sinistre, non la démonstration de conformité du chapitre 32.

Le marché se resserre. Verisk, éditeur des formulaires ISO qu'utilisent les assureurs américains, propose trois avenants d'exclusion de l'IA générative, d'après sa description dans la presse spécialisée [10] :

- **CG 40 47** exclut les dommages corporels, les dommages matériels et les préjudices personnels et publicitaires liés à l'IA générative;
- **CG 40 48** limite l'exclusion aux préjudices personnels et publicitaires;
- **CG 35 08** exclut les dommages corporels et matériels de la couverture des produits et des opérations terminées.

La CSA situe en janvier 2026 l'introduction de l'exclusion d'ISO [6]. Des exclusions propres à certains assureurs s'y ajoutent : celle de Berkley, introduite en 2025 et qualifiée d'absolue, porte sur la responsabilité des administrateurs et dirigeants, professionnelle et fiduciaire [10]. La CSA nomme d'autres grands assureurs et conclut à la fin de la couverture « silencieuse », celle qui jouait sans exclusion expresse : une entreprise risque de s'assurer elle-même par défaut [6]. Une avocate citée par la même revue prévoit l'adoption rapide d'exclusions dans la plupart des branches, certains assureurs pouvant plutôt tarifer le risque par une surprime [10].

Des produits de responsabilité propres à l'IA apparaissent, selon la CSA [6]. AIUC, qui maintient la certification AIUC-1 (chapitre 32), se dit entreprise de normes et d'assurance; sa page d'accueil ne précise ni les garanties ni l'assureur qui les porte [13].

Trois précautions en découlent, les deux dernières par déduction.

1. **Vérifier chaque police au renouvellement.** Les avenants sont facultatifs. La CSA recommande de vérifier les attestations et d'associer le courtier [6].
2. **Lire la définition.** Qu'un acte d'agent tombe sous l'exclusion dépend de la définition de l'IA générative dans l'avenant, non lue ici.
3. **Regarder la police du fournisseur.** Une indemnité contractuelle ne vaut que si celui qui la doit peut la payer.

---

## 36.6 Clauses à négocier

### Le point de départ est défavorable

Une analyse de Clifford Chance du 10 février 2026 décrit des contrats technologiques conçus pour des logiciels passifs [9] : service fourni tel quel, sans garantie d'exactitude; plafond souvent égal aux frais payés; pertes de profits et dommages indirects exclus; indemnités qui couvrent rarement le préjudice d'un tiers, comme une commande erronée; conformité réglementaire à la charge du client, alors que le fournisseur contrôle une part du comportement de l'agent. Le cabinet en conclut que, dans bien des contrats, le client supporte le risque des actes de l'agent. La CSA pose le même diagnostic [6].

### Ce qu'il faut obtenir

Chaque clause a un pendant technique sans lequel elle ne peut être ni appliquée ni prouvée.

| Clause | Objet | Contrôle correspondant |
|---|---|---|
| Limites d'autorité [6][7][9] | Ce que l'agent peut engager, plafonds, actions interdites | Portées et politiques (chapitre 30) |
| Seuils d'escalade humaine [6][9] | Actions à conséquence juridique, financière ou réglementaire soumises à approbation | Humain dans la boucle (chapitre 22) |
| Arrêt et suspension [6][9] | Qui peut arrêter l'agent, dans quel délai, avec quelle responsabilité | Exploitation (chapitre 34) |
| Journaux et traces de décision [6][9] | Accès, conservation, coopération en cas d'enquête | Observabilité (chapitre 33) |
| Plafonds et indemnités [6][9] | Plafonds proportionnés au risque; préjudices de tiers couverts | — |
| Qualité des données [6] | Qui répond des données fournies à l'agent | Données prêtes pour les agents (chapitre 15) |
| Conformité [9] | Au minimum, un contrat qui permet au client de remplir ses propres obligations | Cadres applicables (chapitre 35) |
| Résultat facturé | Définition, vérification et droit d'audit d'un prix au résultat | Mesure par le client (chapitre 40) |

Clifford Chance prévient que ces demandes sont difficiles à obtenir pour un outil standard [9]. Le levier est alors la configuration : restreindre l'agent aux actions réversibles et de faible portée, ce qui réduit l'exposition que le contrat ne couvre pas.

### Entre entreprises dont les agents se parlent

Les protocoles produisent de la preuve et s'arrêtent là : AP2 exclut la résolution des litiges, et aucun protocole ne répartit la perte (chapitre 10). Quand deux organisations laissent leurs agents traiter ensemble, la confiance initiale reste une affaire d'entente bilatérale (chapitre 29); le vLEI vise à prouver quelle personne morale et quel représentant engagent, sans format publié pour les agents (chapitre 45). Cette entente peut prendre la forme du contrat-cadre évoqué en 36.3, qui fixe aussi quelles preuves font foi; c'est une déduction, non une pratique documentée.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Autorité de l'agent | Limites écrites par agent, alignées sur les portées techniques | Agent purement consultatif, sans capacité d'agir |
| Engagements contractuels par agent | Approbation humaine au-delà d'un seuil de montant ou de risque | Achats répétitifs de faible valeur sous mandat étroit |
| Accès aux systèmes de tiers | Vérifier l'autorisation du tiers, non seulement celle de l'utilisateur | Interface que le tiers ouvre expressément aux agents |
| Preuve | Journaux et traces conservés, exploitables en litige | — |
| Offre d'agents en Europe | Se traiter comme fabricant au sens de la directive de 2024 | Usage strictement interne |
| Contrats fournisseurs | Clauses propres aux agents : autorité, journaux, arrêt, indemnités | Outil standard non négociable : réduire la portée de l'agent |
| Assurance | Revue des exclusions IA à chaque renouvellement | — |
| Agents de deux organisations | Contrat-cadre sur l'engagement, la preuve et l'erreur | Échanges sans effet juridique |

---

## Points à retenir

- L'agent n'est pas un sujet de droit. La responsabilité remonte aux personnes qui le développent, le modifient, le fournissent ou l'utilisent.
- L'argument de l'autonomie ne protège pas. La Californie l'a écarté par un texte; les analyses lues vont dans le même sens ailleurs.
- La répartition entre ces personnes n'est pas fixée; les décisions disponibles sont préliminaires.
- L'autorité réelle d'un agent est ce qui est configuré; son autorité apparente, ce que le tiers perçoit. Le risque est dans l'écart.
- Un contrat formé par des agents est valide depuis longtemps. La difficulté est l'erreur, que le droit anglais, selon l'analyse lue, laisse largement à la charge de celui dont l'agent s'est trompé.
- La directive européenne de 2024 traite le logiciel comme un produit et allège la preuve pour la victime. Elle ne couvre pas les pertes entre entreprises.
- Les exclusions de l'IA gagnent les polices courantes; la couverture se vérifie police par police.
- Les contrats standards laissent le risque au client. Chaque clause à obtenir suppose un contrôle technique qui la rend applicable et prouvable.

---

## Sources

Textes officiels lus le 11 novembre 2026 :

1. [Code civil de la Californie, art. 1714.46](https://california.public.law/codes/civil_code_section_1714.46) — reproduction; site officiel inaccessible.
2. [Directive (UE) 2024/2853 — EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:L_202402853)
3. [15 U.S.C. § 7001(h), E-SIGN — Legal Information Institute](https://www.law.cornell.edu/uscode/text/15/7001)
4. [Code civil de la Californie, art. 1633.14 (UETA)](https://california.public.law/codes/civil_code_section_1633.14) — reproduction.
5. [CNUDCI — loi type sur les contrats automatisés](https://uncitral.un.org/en/mlac) — page de présentation.

Analyses lues le même jour :

6. [CSA — Agentic AI Liability, 3 juillet 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-ai-liability-legal-risk-20260703-c/)
7. [Baker McKenzie — Legal Accountability for AI Agents, 1er juillet 2026](https://www.bakermckenzie.com/en/insight/publications/2026/06/united-states-legal-accountability-for-ai-agents)
8. [Browne Jacobson — agentic AI et droit anglais des contrats, 13 janvier 2026](https://www.brownejacobson.com/insights/the-impact-of-agentic-ai-on-english-contract-law)
9. [Clifford Chance — The liability gap, 10 février 2026](https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2026/02/agentic-ai-and-the-liability-gap-your-contracts-may-not-cover.html)
10. [Insurance Journal — exclusions de l'IA, 17 août 2026](https://www.insurancejournal.com/magazines/mag-features/2026/08/17/881424.htm)
11. [Mishcon de Reya — déclaration finale de l'UKJT, 13 août 2026](https://www.mishcon.com/news/ai-and-liability-ukjt-publishes-its-final-statement)

Pages lues le 12 novembre 2026, pendant l'audit :

12. [CNN, via KTVZ — règlement des poursuites contre Character.AI et Google, 7 janvier 2026](https://ktvz.com/money/cnn-business-consumer/2026/01/07/character-ai-and-google-agree-to-settle-lawsuits-over-teen-mental-health-harms-and-suicides/)
13. [AIUC — page d'accueil](https://www.aiuc.com/)

Source non lue :

14. [*Moffatt c. Air Canada*, 2024 BCCRT 149](https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html) — accès refusé.

## Limites de ce chapitre

- Aucune décision de justice n'a été lue. *Moffatt*, *Mobley*, *Garcia* et l'injonction sur l'agent de navigation sont rapportés d'après des analyses; le règlement de *Garcia* est connu par la presse, sans ses termes ni son approbation judiciaire, et la note de la CSA, postérieure, l'ignore.
- AB 316 et l'UKJT : texte officiel inaccessible et déclaration connue par le résumé d'un cabinet. L'entrée en vigueur au 1er janvier 2026 vient de la CSA et de traceurs législatifs.
- Le retrait de la directive sur la responsabilité en matière d'IA, et sa date, reposent sur la CSA.
- EUR-Lex n'a pas pu être relu à l'audit; le rattachement à un considérant de l'assimilation du fournisseur d'IA au fabricant relève de la connaissance générale.
- Les avenants de Verisk sont connus par une paraphrase rapportée par la presse, l'offre d'AIUC par sa seule page d'accueil. Aucune police propre à l'IA n'a été examinée, et aucun chiffre de marché n'est repris.
- Le rôle des formulaires ISO, l'adoption d'UETA hors de la Californie et le sens du mot « agent » en common law relèvent de la connaissance générale. La loi type de la CNUDCI est décrite d'après sa page de présentation.
- Le mandat du Code civil du Québec et les lois provinciales sur le commerce électronique n'ont pas été lus; le cadre canadien est au chapitre 38.
