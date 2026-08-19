## Ouverture — mise en contexte

Ce rapport est **dérivé**. Sa seule matière est ce que les sept livrables du dépôt portent déjà : il
n'ouvre aucune source primaire, ne verse aucun fait neuf, n'écrit dans aucun livrable, ne solde
aucune dette et ne franchit aucune porte. Le `README.md` de la racine pose ce régime à sa section
« Les sept livrables », avec sa conséquence : *synthétiser n'est ni réviser ni publier*.

Cette ouverture fait donc deux choses, et pas une de plus. Elle pose d'abord le **cadre de lecture**
sur lequel les sept livrables se situent — six niveaux, un invariant, une clause de renversement
(§ 1 à 3) —, puis le **régime de preuve** dont chaque énoncé du rapport hérite : les quatre régimes
qui se croisent, les sept gels qui ne coïncident pas, la clôture qui les fige (§ 4 à 6). Le tableau
qui les croise ferme l'ouverture (§ 7). ⚠ Aucune de ces deux moitiés n'est réparable en aval : le
cadre n'est porté par aucun livrable, et le régime ne s'améliore jamais en descendant.

**Convention de renvoi, tenue dans tout le rapport.** Un renvoi nomme le document auquel il
appartient : `compendium, ch. 8 § 8.1.1` — le numéro de chapitre du compendium suffisant à situer le
Livre —, `veille, § 4.1`, `revue, § *titre de section*` ou `revue [84]`, `§1.2 du traité`,
`PRD §16 du compendium`, `§8.3 du PRD du simulateur`. Un renvoi qui ne nomme aucun document désigne
le présent rapport : `ch. 3 § 3.9` en vise un autre chapitre, `§ 1.8 de ce chapitre` une section du
chapitre courant. Les numéros de section se recoupent d'un document à l'autre, et c'est le seul
motif de cette convention.

### 1. Le cadre : six niveaux, un invariant, une clause de renversement

Le cadre de lecture de ce rapport tient sur une page. `5 - Recension/OnePager.html` — fichier unique
et autonome, sans source markdown, sans chaîne de rendu, sans dépendance externe et sans contrôle —
expose une échelle de maturité de l'interopérabilité et de l'orchestration agentiques
d'entreprise en six niveaux numérotés 1 à 6, sous-titrée *« De l'intégration déterministe au
maillage agentique : six niveaux, un invariant, une clause de renversement »*, et cadrée
explicitement sur l'architecture d'entreprise en services financiers. Son bandeau de progression
nomme ce que l'échelle fait croître : **l'abstraction, l'imputabilité et l'autonomie d'exécution**.

Ce rapport en reprend le contenu à ses propres pages — le **schéma** des six paliers ci-dessous, le
**diagramme** de la rupture au § 2 —, de sorte que le cadre se lise ici sans recourir au fichier. La
reprise n'y ajoute aucun palier, aucun libellé et aucun exemple : ⚠ *la page reste seule source de ce
qu'elle avance, et ce qu'elle avance n'est adossé à aucun livrable* (§ 3).

![**Figure 0.1** — Le cadre de lecture du rapport : six niveaux d'interopérabilité et d'orchestration agentiques, l'invariant qui les traverse, et l'exception que l'échelle porte contre son propre sommet.](figures/f-00-1-echelle.svg)

**Niveau 1 — Technique.** *Transport et connectivité physique.* La liaison matérielle, logicielle et
protocolaire qui achemine des flux binaires de façon sécurisée et intègre, sans interprétation
métier du contenu acheminé. Exemple porté par la page : une passerelle asynchrone entre files
transactionnelles (IBM MQ) et dorsale événementielle distribuée (Kafka, gRPC avec mTLS).

**Niveau 2 — Sémantique.** *Modèles canoniques et registres de schémas.* La préservation du sens
univoque des structures échangées, par ontologies de domaine, dictionnaires et schémas partagés.
Exemple : harmonisation bancaire et assurantielle par modèle canonique (BIAN, ACORD, ISO 20022)
validé en registre de schémas (Avro, Protobuf).

**Niveau 3 — Chorégraphique.** *Processus métier et chorégraphie événementielle.* L'alignement des
processus d'affaires, des frontières de responsabilité et de l'ordonnancement des flux de valeur
entre unités et partenaires. Exemple : chorégraphie Saga en architecture événementielle sur le
règlement d'un sinistre.

**Niveau 4 — Juridique.** *Souveraineté, imputabilité et conformité.* La valeur probante des
transactions, la non-répudiation, la résidence territoriale des données. Exemple : encadrement des
transferts de renseignements personnels et journalisation du consentement sous la Loi 25 (Québec),
BSIF E-23, RGPD.

**Niveau 5 — Politique.** *Plan de contrôle, contrats de données et arbitrage.* La verticalisation
du plan de contrôle institutionnel, la formalisation des contrats de données, l'arbitrage des SLA et
**l'attribution de l'imputabilité**. Exemple : comitologie inter-domaines régissant le cycle de vie
des interfaces, les pénalités d'indisponibilité et les points d'application de politiques (PEP/PDP).

**Niveau 6 — Agentique.** *Intention déclarative et coordination A2A/MCP.* La coordination
**adaptative et probabiliste** entre agents autonomes qui découvrent des outils et **négocient des
protocoles** pour exécuter des intentions. Exemple : maillage d'agents où un agent d'arbitrage
négocie en temps réel avec des agents de souscription, via *Agent Cards* signées et passerelle d'IA.

**L'invariant transversal**, porté en bandeau sous les six paliers, est à trois termes :
**découplage ── contrat ── évolution**.

### 2. Pourquoi le sixième palier change de nature

La page ne présente pas le niveau 6 comme une marche de plus. Elle en fait une **rupture de
paradigme** : les niveaux 1 à 5 garantissent une intégration **déterministe**, régie par des
**contrats statiques et vérifiables** ; le niveau 6 introduit une gouvernance **probabiliste et
adaptative**, où la contractualisation devient dynamique par négociation contextuelle
d'objectifs. Le déplacement est de nature, pas de degré : *un contrat de niveau 5 se vérifie avant
l'exécution ; une intention de niveau 6 ne s'observe que pendant.*

La page en tire le prix, et il est double. **Compromis** : surcoût d'observabilité (*AgentOps*) et
impératif de *runtime verification* pour confiner le non-déterminisme. **Clause de renversement** :
*tout système sous contrainte de compensation financière temps réel — rails Lynx, RTR — doit
interdire l'autonomie agentique directe et maintenir une contractualisation déterministe de
niveau 5.* L'échelle porte donc sa propre exception, et le sixième niveau n'est pas sa
destination.

![**Figure 0.2** — La rupture que la page situe entre le cinquième palier et le sixième : ce qui se vérifie avant l'exécution, et ce qui ne s'observe que pendant.](figures/f-00-2-rupture.svg)

### 3. Ce que le cadre doit au dépôt, et ce qu'il ne lui doit pas

Cette page ne cite aucun livrable et aucun livrable ne la cite. Sa filiation est réelle mais
écrite nulle part dans un livrable, et c'est le `README.md` de la racine qui l'établit, à sa section
« Les sept livrables » : ses quatre premiers niveaux sont les quatre couches du *New European
Interoperability Framework* telles que le Vol. I les expose (`1 - Corpus/1 -
InteroperabiliteAgentique/Chapitres/Chapitre 1 - Interoperabilite.md` §1.2.1.1), et son bandeau
transversal reprend mot pour mot l'invariant du Vol. I. ⚠ Ses niveaux 5 et 6 sont des ajouts :
*aucun livrable du dépôt ne porte, sous ces noms, un palier « politique » ni un palier « agentique »
dans une échelle numérotée.* Le tenir-sur-une-page est constaté au rendu, jamais vérifié ; aucune
porte ne l'oppose à rien. *(Le `README.md` décrit la page à la racine du dépôt ; elle vit sous
`5 - Recension/` sur l'arbre courant — même fichier, dossier changé.)*

Quatre écarts entre le cadre et les livrables doivent être posés maintenant, parce que le rapport
les rencontrera au travail.

*(a)* L'ordre est inversé. Le NEIF, tel que le Vol. I l'expose au §1.2.1.1, énumère ses quatre
couches **juridique, organisationnelle, sémantique, technique** ; la page les numérote en sens
contraire, de 1 (technique) à 4 (juridique). Mêmes quatre couches, exposition retournée : la
numérotation appartient à la page, pas à sa source.

*(b)* Le palier syntaxique manque, et il portait le constat le plus lourd. La pile canonique du
Vol. I §1.1.2.1 — *« Technique, syntaxique, sémantique, organisationnel »*, reprise à l'identique au
ch. 1 §1.1.2 du compendium — compte **quatre** paliers, non trois. C'est sur le **syntaxique** que le
compendium pose
ce qu'il appelle le constat le plus important de son Livre I : *MCP et A2A opèrent au niveau
syntaxique et, partiellement, technique ; ils ne fournissent aucun mécanisme d'accord sémantique,
qu'ils **présupposent***. L'échelle à six niveaux n'a pas de case pour ce constat : elle fait
passer les protocoles agentiques du niveau 1 au niveau 6 sans le palier où le compendium les situe.
*Réserve nommée, non levée — et l'énoncé du compendium reste de surcroît celui d'un brouillon non
publiable.*

*(c)* L'invariant du bandeau compte trois termes ; celui de la somme en compte quatre.
`2 - Compendium/README.md` pose l'invariant hérité du Vol. I à **quatre** termes — découplage,
contrat, évolution, **exploitation** —, le quatrième posé à l'avant-propos et refermé au Livre IV
(ch. 38-40) ; le ch. 1 §1.0.2 du compendium déclare en toutes lettres n'en éprouver que trois, *le
quatrième n'ayant pas d'objet faute d'agent à exploiter*. Une échelle qui culmine à un palier agentique
porte donc un bandeau où manque précisément le terme que l'exploitation agentique instruit.

*(d)* C'est une quatrième échelle à six niveaux dans un dépôt qui en compte déjà trois. La parade
**R-13** du Vol. III impose de nommer toute échelle par son fichier, sa section, son cardinal et sa
numérotation, au motif que trois échelles coexistent au Vol. I en partageant leurs libellés — dont
un continuum à six niveaux numérotés 0 à 5 (`Monographie.md` §2.2.4). *Le cardinal est le même
que celui de la page, la numérotation ne l'est pas.* La discipline **R-13** ne s'applique pas ici et
aucun contrôle ne la rejoue (`README.md` racine). Ce rapport la tient malgré tout, et désigne son
cadre par ses quatre marques : `5 - Recension/OnePager.html`, page unique sans section, six
niveaux, numérotés 1 à 6.

### 4. Aucun énoncé de ce rapport n'a de provenance propre

Chaque énoncé hérite du régime de preuve du livrable qui le porte, jamais d'un meilleur. La règle
est celle que le `README.md` de la racine écrit pour ce rapport, et elle tient ici lieu d'appareil de
vérification à elle seule. Les quatre régimes qui se croisent dans les pages qui suivent :

- Le compendium (Vol. IV) est un brouillon non publiable, et il le déclare pièce par pièce. Ses
  cinquante chapitres sont rédigés **hors portes** ; aucun de leurs énoncés n'est central au sens
  de **CA-IV-01** ; **CA-IV-11 et CA-IV-13** demeurent dérogés, non satisfaits, faute de relecteur
  distinct du rédacteur (`2 - Compendium/README.md`, champs *Statut de révision* et *Statut
  éditorial* ; `2 - Compendium/PRD/PRD.md` §16). La matière héritée du Vol. I y entre en **[C]** —
  *vérification portant sur les références, non sur le contenu des affirmations* (PRD §7.1 du compendium).
- La veille technologique déclare deux régimes et dit lequel s'applique où. Le **régime fort** —
  trois vérificateurs indépendants chargés de *réfuter* — couvre les sections de fond ; le **régime
  faible** — contre-vérification individuelle sur source primaire, sans ronde adverse — couvre le
  reste. ⚠ Les trois passes d'août 2026 n'ont aucune ronde adverse, et l'édition du 15 août écrit
  que son régime le plus fort **reste plus faible** que celui des rondes à trois votants de juillet
  2026 (`4 - Veille/Veille Technologique.md`, § *Protocole de revue*, § *Limites de la méthode*).
- La revue de littérature mesure son propre corpus avant d'en rapporter le contenu. Sur
  **189 pièces déposées sur arXiv** — 192 entrées au total —, douze portent une attestation de
  publication en notice, trente-deux annoncent une acceptation au seul champ de commentaire libre,
  et cent quarante-cinq ne présentent aucun signe de revue par les pairs
  (`4 - Veille/Revue de littérature.md`, résumé et § *Physionomie du corpus*). ⚠ Une passe de
  contre-épreuve du 15 août 2026 les borne dans les deux sens : 145 est un plafond du
  non-arbitré, 12 un plancher de l'arbitré (`4 - Veille/README.md`, § *Réserves*).
- Le traité est le seul livrable dont les énoncés soient rejoués par du code, et la mesure en
  réfute trois. `stigmergie-lab`, sous `3 - Traité/`, consigne **cinq écarts** : trois
  contredisent un énoncé du traité, deux sont des constats de mesure qui ne contredisent rien
  (`3 - Traité/README.md`). *Seul contrepoids interne du rapport, et il ne couvre qu'un livrable sur
  sept.*

### 5. Les sept gels ne coïncident pas, et l'écart vaut dix semaines

Un rapport dérivé ne peut être plus récent que ses sources, ni avoir **une** date. Les sept
livrables portent sept gels distincts, chacun écrit dans son propre livrable :

| Livrable | Gel de l'information | Où il est écrit |
|---|---|---|
| Vol. I — *Interopérabilité agentique* | **juin 2026** | `1 - Corpus/1 - InteroperabiliteAgentique/README.md` — « socle documentaire arrêté à juin 2026 » |
| Vol. II — *Orchestration agentique* | **16 juillet 2026** (22 pièces) · **17 juillet 2026** (7 pièces) | `1 - Corpus/2 - OrchestrationAgentique/README.md`, champ *Gel de l'information* |
| Vol. III — *L'entreprise agentique* | **21 juillet 2026** pour ses 34 pièces ; il **hérite** en outre de deux gels — juin 2026 (Vol. I) et 16-17 juillet 2026 (Vol. II) | `1 - Corpus/3 - EntrepriseAgentique/README.md`, champ *Dates de gel* et registre `monographie/99-registre-gel.md` |
| Vol. IV — *Compendium* | **27 juillet 2026**, gel unique par décision d'auteur **D-1** ; volet des faits levé le 28 juillet 2026 | `README.md` racine, tableau des sept livrables ; registres `2 - Compendium/PRD/gel-2026-07-27.md` et `gel-2026-07-28-volet-residuel.md` |
| Veille technologique | **15 août 2026** | en-tête de `4 - Veille/Veille Technologique.md` et `4 - Veille/README.md` |
| Revue de littérature | **15 août 2026** | en-tête de `4 - Veille/Revue de littérature.md` et `4 - Veille/README.md` |
| Traité — *Systèmes multiagents en essaim* | **15 août 2026**, troisième édition | ligne *date* de l'en-tête de `3 - Traité/Traité.md` ; `3 - Traité/README.md` |

: Tableau 0.1 — Les sept gels, chacun repris au livrable qui le porte.

Dix semaines séparent le plus ancien du plus récent. Mettre en regard le Vol. I et la veille,
c'est comparer juin 2026 à août 2026 : *quand les deux divergent, ce n'est pas une contradiction,
c'est un écart de gel*, et ce rapport le nomme plutôt que d'arbitrer.

⚠ Une divergence interne au dépôt porte précisément sur ces dates. Le tableau des sept livrables
du `README.md` de la racine donne encore la veille au **8 août 2026**, la revue au **9 août** et le
traité au **10 août**, alors que le même fichier écrit plus haut que les gels vont « de juin 2026
pour le Vol. I au 15 août 2026 pour la veille, la revue et la troisième édition du traité ». Ce
rapport résout contre le livrable, jamais contre le README. *Constat porté, correction non faite —
le dépôt est clos.*

### 6. Le dépôt est clos par D-13, et la clôture a été rouverte

Décision d'auteur **D-13**, prise le 8 août 2026 au titre de D-6, enregistrée au `PRD.md` **v0.17**
§16 du compendium. Elle clôt la passe de révision qu'avait ouverte D-11 le 30 juillet, sans
exécuter son domaine résiduel, et elle clôt le dépôt entier : *plus aucune passe n'est prévue — ni
de rédaction, ni de révision, ni d'appareil —, sur ce volume comme sur les quatre autres livrables*
(PRD §16.1 du compendium). Ce qu'elle ne fait pas est écrit au même endroit : elle ne franchit aucune porte,
n'élève aucune entrée de socle, ne rend aucun énoncé central et ne périme pas les
sources — les Vol. I, II et III font foi (PRD §16.4 du compendium). Et la règle qui commande la lecture de tout
ce rapport : *une dette qu'on cesse de suivre reste une dette ; elle change seulement de nom, et le
nom qu'elle prend ici est **manque définitif*** (PRD §16.1 du compendium).

Deux livrables sont postérieurs à cette clôture et l'ont rouverte pour eux seuls. La veille
technologique et la revue de littérature ont été rouvertes et re-vérifiées à l'édition du 15 août
2026 — les 303 références que la veille portait au 8 août et les 176 que la revue portait au
9 août reprises à leur source primaire, la re-vérification produisant plus de corrections que
d'ajouts ; le `4 - Veille/README.md` l'écrit, la dit *intégrale*, et en borne la portée : *« La
clôture reste en vigueur pour les quatre volumes ; rien de ce dossier ne la lève. »*

⚠ Ces deux cardinaux sont ceux des éditions antérieures ; les livrables du 15 août en portent 342
et 192 (tableau 0.2). *Intégralement* laisse donc dehors 39 références de la veille et 16 pièces
de la revue, versées à la reprise elle-même. Les deux couples vivent dans le même `README.md` de
dossier, et c'est la règle posée plus haut qui les départage — *résoudre contre le livrable, jamais
contre le README*. ☑ La revue
couvre ses seize, et le dit : *« déposées entre le 9 et le 13 août 2026 [177-192] »*, retenues au
même critère que la passe neuve, et les 189 notices arXiv du corpus — *« les 173 du premier relevé
et les seize entrées depuis »* — ont été interrogées le 15 août à la même interface
(`4 - Veille/Revue de littérature.md`, § *Constitution du corpus*, § *Régime de vérification*).
⚠ La veille, non — et son propre texte réduit encore la portée du mot : la passe du 15 août ne
rouvre pas la bibliographie entière, mais les seules **sources vivantes**, et son annexe de
traçabilité énumère ce qui n'a été rouvert *« ni au premier ni au second tour »* — trente entrées
d'identité et de post-quantique, dix-sept à dix-neuf d'orchestration, cinq du corpus protocolaire,
sept plateformes d'entreprise —, sous un régime qu'elle nomme *« repris de l'édition antérieure sans
revérification »* (`4 - Veille/Veille Technologique.md`, § *Protocole de revue* ; annexe de
traçabilité, § *Régime de la vérification*). Aucun cardinal n'y est donné pour ce que la passe du
15 août a couvert, et rien n'y est dit des 39 références neuves. *Le dépôt ne permet donc pas de
dire quelle part du corpus de la veille le régime le plus fort du 15 août atteint ; il permet de dire
que ce n'est pas la totalité.*

Ce ne sont pas les seules réouvertures : la section
d'état du `README.md` de la racine s'intitule « CLOS le 8 août 2026, rouvert six fois depuis »,
et le `2 - Compendium/README.md` en déclare une, le 9 août 2026, pour l'appareil de rendu seul —
PDF recomposé à mille pages exactement, sans qu'une seule des cinquante pièces soit touchée.
*Recomposer n'est pas récrire ; re-vérifier deux livrables n'est pas rouvrir quatre volumes ; et ce
rapport, qui ne fait ni l'un ni l'autre, ne rouvre rien.*

---

### 7. Les sept livrables sur ce cadre

Le placement ci-dessous est une **lecture du présent rapport**, non un énoncé d'un livrable : aucun
des sept ne se situe lui-même sur cette échelle, et la page ne les nomme pas.

| Livrable | Niveaux travaillés | Régime de preuve | Gel |
|---|---|---|---|
| **Vol. I** — *Interopérabilité agentique* (569 p., 7 chapitres + ADS en Annexe B) | 1 à 3, **et le cadre lui-même** — la pile, les quatre couches, l'invariant | Formalisme d'ingénierie (ArchiMate, ADS « Boréalis ») ; ⚠ **ses faits entrent en [C]** au compendium — vérification portant sur les références, non sur le contenu | juin 2026 |
| **Vol. II** — *Orchestration agentique* (387 p., 29 pièces) | **4**, et l'amorce du 5 — E-23, AMF, Loi 25, ACVM, Lynx/RTR | Socle F-01…F-48 (46 entrées), niveaux **[A]/[B]/[C]**, grille CA-1…CA-8 ; publié, millésime `mono-v1.0` | 16-17 juillet 2026 |
| **Vol. III** — *L'entreprise agentique* (427 p., 34 pièces) | **5 et 6** — identité non humaine, maillage, exploitation | Socle propre de 98 entrées, double héritage codifié, CA-01…CA-14 ; ⚠ non publiable et il le déclare : quinze remontées R-G-43 à R-G-57 ouvertes, dette de vote sur F-92 et F-96, phase P5 close sans être achevée | pièces au 21 juillet 2026 (hérite de juin et de 16-17 juillet) |
| **Vol. IV** — *Compendium* (1 000 p., 50 chapitres, 5 Livres) | les six à la fois, au régime le plus faible du dépôt | Rédigé **hors portes** ; brouillon non publiable ; aucun énoncé central au sens de **CA-IV-01** ; CA-IV-11 et CA-IV-13 non satisfaits ; socle consolidé de 159 entrées ; clos par **D-13** | 27 juillet 2026 (D-1) ; volet des faits levé le 28 juillet |
| **Veille technologique** (141 p., 342 réf.) | **6**, plus les sept couches implicites qui retombent sur 1 à 5 | Deux régimes déclarés — fort (trois votants réfutateurs) et faible ; les passes d'août 2026 n'ont aucune ronde adverse, et le plus fort de l'édition du 15 août reste **plus faible** que ceux de juillet | 15 août 2026 |
| **Revue de littérature** (53 p., 192 réf., dix fronts) | **6** — ce que la littérature en sait, et ce qu'elle ne traite pas | 12 attestées, 32 autodéclarées, 145 sans revue sur 189 pièces arXiv ; plafond et plancher déclarés par la revue elle-même | 15 août 2026 |
| **Traité** — *Systèmes multiagents en essaim* (8 chapitres, 24 sections, 123 notices) | **6 par l'autre route** — coordonner par le milieu, non par accord | Chaque mécanisme sous son modèle de panne, son hypothèse de synchronisme et son coût en messages et en tours ; ☑ le seul livrable rejoué par du code — `stigmergie-lab`, 428 tests — et trois de ses énoncés y sont réfutés par la mesure | 15 août 2026, troisième édition |

: Tableau 0.2 — Les sept livrables situés sur le cadre, avec le régime dont chacun fait hériter ce rapport.

Trois remarques closent cette ouverture, et chacune commande un chapitre.

La première porte sur le niveau 4. C'est le seul palier dont un livrable instruise la matière au
grain du droit — le Vol. II, sur socle daté et à niveaux de preuve nommés — et c'est aussi celui où
la veille a renvoyé au corpus deux corrections de fond que les volumes ne recevront pas : la
lecture de l'article 12.1 de la Loi 25 et celle de l'avis ACVM 11-348 (`4 - Veille/README.md`,
§ *Ce que chacun rend à l'autre*). ⚠ *Le lecteur qui cite le Vol. II sur ces deux points cite un
énoncé que la veille a réfuté* — et le dépôt étant clos, l'écart reste.

La deuxième porte sur la clause de renversement. Elle nomme Lynx et le RTR, objets que le
compendium instruit à son Livre III ch. 33 — *Lynx accompli, RTR **visé** au T4 2026, quatre cibles
successives, à attribuer et jamais à affirmer au futur catégorique*. ⚠ La clause elle-même n'est
portée par aucun livrable : elle appartient à la page, qui ne cite rien. Ce rapport la reprend
comme cadre de lecture, non comme énoncé établi.

La troisième porte sur le traité, et c'est le cas que l'échelle ne tient pas. Le niveau 6 de la
page est **négocié** : des agents découvrent des outils et s'accordent sur des protocoles. La thèse
du traité est l'inverse — *déplacer la coordination dans le milieu, et payer ce que le déplacement
coûte* : dès que la population dépasse quelques dizaines d'agents et que les défaillances partielles
deviennent l'état normal, le coût du consensus explicite croît plus vite que sa valeur, et les
agents déposent et lisent des traces au lieu de négocier des décisions. L'échelle n'a qu'un
palier agentique, et il a la forme de la négociation ; le régime que le traité décrit n'y a pas de
case. Le traité, du reste, ne cite aucun autre livrable et aucun ne le cite — il est, avec la
page elle-même, l'un des deux objets du dépôt sans lien entrant ni sortant. *Le chapitre qui lui est
consacré travaille donc hors du cadre que cette ouverture pose, et le déclare en tête.*
