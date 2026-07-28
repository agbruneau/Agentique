# Chapitre 8 — Anatomie : MCP (agent-outil) et A2A (agent-agent)

*Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique.
Second mouvement — la couche protocolaire agentique (ch. 7-11).*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — portes G-1, G-2 et G-3 ouvertes à la rédaction ; rédaction sur instruction d'auteur du 27 juillet 2026. ⚠ **Deux mises à jour postérieures à la rédaction, et la seconde change l'état du volume.** *(1)* **27 juillet 2026** : **G-2 et le volet Livre I de G-1 franchis** (PRD v0.8), **remontées de cette pièce closes**. *(2)* **28 juillet 2026** : **G-3 est FRANCHIE** (PRD v0.14) — le socle consolidé existe, **159 entrées `S-001`…`S-159`** ([`socle-consolide.md`](../PRD/socle-consolide.md) v1.2). ⚠ **Aucune de ces trois portes ne rend la pièce recevable, et le motif se lit en trois temps.** *(a)* Elle a été **écrite avant elles**, et ses énoncés **n'ont pas été ré-résolus contre les identifiants `S-nnn`** — *une porte franchie après coup ne remonte pas le fil des pièces qu'elle conditionnait* : la ré-résolution est **due**, non faite. *(b)* Tant qu'elle n'est pas faite, **aucun énoncé de cette pièce n'est central au sens de CA-IV-01**. *(c)* **CA-IV-11 et CA-IV-13 demeurent insatisfaisables**, D-6 ne fournissant pas de relecteur distinct du rédacteur (PRD §11). |
| **Date de gel** | **27 juillet 2026** — gel unique du compendium, **décision d'auteur D-1 prise** ce jour (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Ce gel n'efface pas ceux des sources**, qui restent portés ci-dessous : il date la reprise de chaque fait périssable à sa source primaire, non la matière elle-même. Deux gels de source : **juin 2026** (Vol. I), **16 juillet 2026** (Vol. II). ⚠ **Ce chapitre portait la péremption la plus courte de toute la somme, elle se comptait en heures, et ELLE EST ADVENUE.** L'anatomie décrite est celle de la **révision 2025-11-25** ; la **révision candidate, gelée le 21 mai 2026, avait sa ratification annoncée pour le 28 juillet 2026** — soit **le lendemain de la date de rédaction de ce chapitre**. **Constat du 28 juillet 2026** : la ratification a eu lieu à la date annoncée (socle consolidé `S-001` ; [registre du volet résiduel de G-1](../PRD/gel-2026-07-28-volet-residuel.md)). ⚠ **La revalidation en bloc des § 8.1 et § 8.2 est donc OUVERTE et NON EXÉCUTÉE** : elle se fait **sur sources primaires extraites**, jamais par retouche de ce texte — *ce chapitre décrit un contrat qui n'est plus le contrat courant, et il le dit plutôt que de se corriger à l'aveugle* |
| **Socle mobilisé** | ⚠ **Le socle consolidé existe depuis le 28 juillet 2026, et cette pièce n'y est PAS encore résolue.** Elle a été rédigée par résolution directe contre le **Vol. I *Monographie* §3.2-3.3 et §2.5.4** — régime **[C]** (PRD §7.1 : la vérification du Vol. I porte sur ses références, non sur le contenu de ses affirmations) — et contre le **Vol. II *Monographie* ch. 2**, aux quatre entrées que le TOC lui assigne : **`F-01`, `F-02`, `F-03`, `F-16` du Vol. II**. Ces quatre entrées **résolvent désormais en `S-001`, `S-002`, `S-003` et `S-013`** du socle consolidé, à **niveau conservé** (les quatre y sont `[A]` à portée générale). ⚠ **La correspondance est établie ici, la ré-résolution ne l'est pas** : *rapprocher deux identifiants n'est pas confronter un énoncé à l'entrée qu'il invoque*, et la matière du Vol. I n'a pour sa part **aucune entrée consolidée** — les dix-sept entrées héritées du Vol. I (`S-143`…`S-159`) ne couvrent pas §3.2-3.3. **Le régime [C] tient donc pour tout ce que ce chapitre tire du Vol. I** |
| **Garde-fous balayés** | ⚠ **Règle de décompte, et les cardinaux ci-dessous ont été re-mesurés sous elle le 28 juillet 2026** : un décompte d'occurrences porte sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — en-tête et note de statut exclus —, et il se re-mesure au commit ; un garde-fou appliqué **sans identifiant écrit** se déclare par son **domaine balayé, sans cardinal**. Vol. II — **réserve F-01 (« cadre d'autorisation », jamais « sécurisé ») : quatre occurrences**, § 8.1.4, § 8.2.2, § 8.3.1 et § 8.6.1, chacune tenue — ⚠ *la formule imposée, elle, est employée au-delà de ces quatre marqueurs, notamment au § 8.7 : la réserve est tenue partout, seul son marqueur est compté ici* ; **R-1 : une occurrence**, § 8.5.1 ; **R-8 (sigle jamais nu) : une occurrence**, § 8.5.1 — le siège de l'encadré est au **ch. 7 § 7.5**, auquel ce chapitre renvoie **sans le reconstruire** ; **métriques auto-déclarées (PRD Vol. II §8.2, règle 1 ; règle transversale au §7.5) — sans identifiant écrit, donc sans cardinal re-mesurable : appliqué au § 8.4.2 et au § 8.6.3**, la première attribuée, la seconde **refusée comme métrique** faute de chiffre, de date et de définition ; s'y ajoute, au § 8.6.1, une **estimation de tiers** attribuée nommément (décision 15 du TOC). R-2 à R-7 : **zéro occurrence**. Vol. III — **R-02 (qualification par ce que la spécification démontre) : trois occurrences**, § 8.1.4, § 8.2.2 et § 8.4.2 ; **R-13 : une occurrence**, § 8.5.1, même que R-8 ; **R-14 : trois occurrences**, § 8.2.3, § 8.6.1 et § 8.7 — ⚠ *le § 8.8, que cet en-tête portait auparavant, est la note de statut : hors domaine de comptage*. R-01, R-03 à R-12 : **zéro occurrence** |
| **Volumétrie cible** | ≈ 10 000 mots de corps (§ 8.1 à § 8.7) — le plus lourd du Livre I, sept sections contre quatre à six ailleurs. ☑ **Décompte publiable depuis le franchissement de G-2** (27 juillet 2026). **Réel : 5 635 mots** de corps, **re-mesurés le 28 juillet 2026** par [`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte du volume — **−43,7 %** de la cible (5 138 mots et −48,6 % à la rédaction ; la passe de relecture a ajouté des constats datés et des bornes de régime, **aucune matière neuve**). ⚠ **L'écart individuel ne se lit pas seul** : la somme des onze cibles dérivées atteint **93 000 mots** pour une enveloppe de Livre de **65 000** — chaque pièce a dérivé sa cible de l'enveloppe sans que personne n'additionne les dérivations. **Le réel du Livre valait 64 750 mots, soit −0,4 % de l'enveloppe, au relevé du 27 juillet 2026** ; ⚠ **il n'est PAS re-mesuré ici** — *un cardinal de Livre mesuré pendant que ses onze pièces sont relues est faux à la seconde où on le publie*, et il se re-mesure au terme de la passe, sur le corpus que le commit produit. C'est la cible dérivée qui était fausse, non la pièce qui est courte. *Un écart se documente ; il ne se corrige ni par amputation ni par gonflement* |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.30, entrée du chapitre 8 — copiée, non re-frappée ; forme inchangée depuis la v0.23)* — « MCP dans les agents, A2A entre les agents » — doctrine de complémentarité **déclarée par le projet A2A** (non un accord des deux projets) qui fournit le premier critère de découpage architectural, sans le contraindre.

⚠ **Trois qualifications de cette thèse sont portées par le plan et tenues ici** : la doctrine est **déclarée**, elle l'est **par une seule des deux parties**, et elle **ne contraint pas**. Chacune est instruite au § 8.6.3.

---

## § 8.1 — MCP comme couche de contrat : problème N×M, primitives, transports

### 8.1.1 Le problème N×M et la critique du slogan

Ce que le protocole agent-outil standardise **n'est pas l'appel d'outil en lui-même** — la façon dont
un modèle émet une invocation relève de l'ingénierie et a été traitée au ch. 4 § 4.4 — mais le
**contrat** entre un client, hébergé par l'hôte agentique, et un serveur, exposé par un fournisseur de
capacités.

Le problème traité est combinatoire et **familier de l'intégration d'entreprise** (ch. 1 § 1.3.1) :
faire dialoguer *N* agents avec *M* outils sans standard impose *N*×*M* intégrations point-à-point ;
une couche de contrat partagée ramène ce coût à *N*+*M*. C'est exactement le geste du modèle de
données canonique (ch. 1 § 1.6.1), transposé à l'axe agent-outil — et il vaut d'être reconnu comme
tel plutôt que présenté comme une nouveauté.

⚠ **Le slogan promotionnel d'un « port universel de l'IA » capture l'ambition, mais reste un objet de
critique légitime, et la critique est précise.** Un port universel **négocie électriquement ses
modes** ; ce protocole, lui, **ne porte pas de couche riche de négociation de capacités ni de
confiance établie** entre les parties. L'appariement est conforme **au transport et au schéma, non au
sens** : un client peut se brancher sur un serveur **sans qu'aucun mécanisme ne garantisse que
l'intention de l'agent corresponde au comportement réel de l'outil**.

*Le contrat est donc réel mais étroit : il fixe la forme de l'échange, pas son interprétation.* C'est
le verrou que le ch. 9 § 9.4 prend pour objet, et la première illustration concrète de la thèse du
ch. 2 — les protocoles agentiques **présupposent** l'accord sémantique et ne le fournissent pas.

### 8.1.2 Architecture et primitives, sous l'angle de la bidirectionnalité négociée

L'architecture repose sur un triangle **hôte / client / serveur** communiquant par appels de procédure
en JSON : l'hôte instancie **un client par serveur connecté**, et chaque serveur expose ses capacités.

L'apport propre à l'analyse d'interopérabilité tient moins à l'inventaire des primitives — outils,
ressources, gabarits d'invite, déjà décrits au ch. 4 § 4.4 — qu'à la **grille de contrôle** qui les
distingue :

| Primitive | Contrôlée par | Ce que cela prescrit |
| --- | --- | --- |
| **Outils** | le **modèle** | c'est le modèle qui décide de les invoquer |
| **Ressources** | l'**application** | l'hôte décide quel contexte injecter |
| **Gabarits d'invite** | l'**utilisateur** | déclenchement explicite |

: Tableau 8.1 — La répartition du contrôle entre primitives : une clause du contrat, non un détail d'implémentation.

⚠ **Cette répartition est elle-même une clause du contrat** : elle prescrit **qui, dans la chaîne, est
autorisé à mettre une primitive en mouvement**. La lire comme un simple classement fonctionnel fait
manquer ce qu'elle porte de gouvernance.

Le trait le plus distinctif au regard d'une API REST classique est l'existence de **primitives
client**, qui **inversent le sens du dialogue** :

- l'**échantillonnage** — le serveur peut demander à l'hôte une complétion du modèle ;
- la **sollicitation** — le serveur peut demander une information structurée manquante, en cours
  d'exécution ;
- les **racines** — l'hôte délimite le périmètre de système de fichiers accessible.

Ces canaux instaurent une interopérabilité **négociée et interactive, bidirectionnelle**, absente du
modèle requête-réponse unidirectionnel. *Le contrat n'est plus un appel et son retour, mais un échange
où le serveur peut, à son tour, interroger l'hôte.*

Lecture de l'auteur — c'est le premier endroit de la somme où un contrat d'interface autorise
explicitement l'appelé à solliciter l'appelant. Le ch. 1 § 1.1.3 posait le contrat comme publication
de ce qu'un système offre et exige ; ici, il devient un **protocole de conversation**. Le socle
établit l'existence des trois primitives client et la direction de leur appel ; il **n'établit ni
cette lecture, ni le caractère inédit qu'elle prête à ce renversement** dans l'histoire des contrats
d'interface. Elle est proposée comme telle.

### 8.1.3 Transports : une trajectoire du couplage vers le découplage

L'histoire des transports **se lit comme une décroissance progressive du couplage**, et c'est
l'illustration la plus nette de l'invariant du Livre dans tout le mouvement.

| Étape | Mécanisme | Couplage résiduel |
| --- | --- | --- |
| **Entrée-sortie standard** | le serveur est un sous-processus local de l'hôte | **fort** — cycle de vie et machine partagés |
| **HTTP à deux points d'accès** | un point pour les requêtes, un pour le flux d'événements | déprécié dès la révision suivante |
| **HTTP diffusable à point unique** | un seul point d'accès | **résiduel** — un identifiant de session épingle un client à une instance |
| **Cœur sans état** *(candidat au gel)* | suppression de la poignée de main et de l'identifiant de session | **aucun** — serveur déployable derrière un répartiteur à tourniquet |

: Tableau 8.2 — La trajectoire des transports : quatre étapes, un couplage qui décroît jusqu'à l'absence d'état partagé.

⚠ **La dernière étape est une cible architecturale, non un acquis déployé.** Elle relevait, au gel,
d'une **révision candidate** ; le § 8.2.1 en donne le statut exact et le constat de bascule qui a
suivi.

### 8.1.4 Une interface d'outillage assortie d'un cadre d'autorisation

⚠ **Formulation imposée, tenue ici et à ses trois autres occurrences marquées (réserve F-01 du
Vol. II) : ce protocole est assorti d'un *cadre d'autorisation*, jamais d'un protocole « sécurisé ».**
La distinction n'est pas de style. Un cadre fournit les mécanismes ; **la sécurité dépend de
l'implémentation qui les met en œuvre**, et le ch. 11 expose ce que le socle nomme comme risques
attachés. Écrire « protocole
sécurisé » attribuerait à la spécification une propriété que seule une mise en œuvre peut porter — et
c'est exactement ce que le garde-fou R-02 du Vol. III proscrit en matière cryptographique.

---

## § 8.2 — Jalons datés, autorisation et sémantique des résultats

### 8.2.1 Les cinq jalons : trajectoire de maturation d'un standard

La succession des révisions constitue une **étude de cas de gouvernance d'un standard** (ch. 1
§ 1.2.2), où chaque jalon ajoute une couche au contrat.

| Révision | Date | Apports majeurs pour le contrat |
| --- | --- | --- |
| **2024-11-05** | 5 nov. 2024 | version initiale ; primitives de base ; transports local et HTTP à deux points d'accès |
| **2025-03-26** | 26 mars 2025 | transport diffusable à point unique ; **cadre** d'autorisation |
| **2025-06-18** | 18 juin 2025 | sorties structurées ; sollicitation ; racines ; serveur qualifié serveur de ressources |
| **2025-11-25** | 25 nov. 2025 | découverte d'identité ; schémas 2020-12 ; tâches asynchrones **expérimentales** |
| **2026-07-28** *(candidate au gel)* | gelée le 21 mai 2026 | cœur sans état ; cadre d'extensions à nommage inversé ; **politique de dépréciation formelle** ; dépréciation de trois primitives et de l'enregistrement dynamique de client |

: Tableau 8.3 — Cinq jalons en moins de deux ans, et un cinquième qui n'était pas acquis au gel.

⚠ **Trois précisions de statut, et la première est la plus importante de tout le chapitre.**

*(a)* **Le cinquième jalon était, à la rédaction, une révision candidate et non une révision
publiée.** Gelée le **21 mai 2026**, sa **ratification était annoncée pour le 28 juillet 2026** ; à la
date de rédaction — le 27 juillet 2026 —, **elle n'était pas ratifiée**, et l'anatomie décrite aux
§ 8.1 et § 8.2 est celle de la **révision 2025-11-25**.

⚠ **Constat postérieur, daté du 28 juillet 2026 : la ratification a eu lieu, à la date même que la
source annonçait.** La page de spécification courante sert désormais la révision `2026-07-28`, et
l'index documentaire du site ne connaît plus la précédente (socle consolidé `S-001`, instruit au
[registre du volet résiduel de G-1](../PRD/gel-2026-07-28-volet-residuel.md)). ⚠ **Ce constat porte
sur la bascule, non sur le contenu de la révision neuve, qui n'a pas été extrait.** *La péremption que
ce chapitre avait datée est advenue* : les § 8.1.3, § 8.2.1, § 8.2.2 et § 8.3.1 se revalident **en
bloc et sur sources primaires**, non par retouche — et ils décrivent, en attendant, l'état arrêté au
gel.

*(b)* **Cette révision porte des changements cassants**, et non seulement des ajouts : suppression de
la poignée de main et de l'identifiant de session, dépréciation de trois primitives, remplacement du
mécanisme d'enregistrement de client. Sa ratification **périme donc l'anatomie en bloc**, et non par
retouches.

*(c)* **La cadence elle-même est un fait d'interopérabilité** : cinq jalons en moins de deux ans
témoignent d'un standard **en maturation rapide**, où la rétrocompatibilité et la dépréciation
deviennent des objets de spécification à part entière. C'est un signe de maturité — et, simultanément,
un coût pour qui doit épingler une version.

> **Perspective recherche.** La densité de révisions millésimées rejoint une critique adressée à
> l'écosystème : *un protocole d'interopérabilité ne vaut que par la stabilité de son contrat dans le
> temps*, et **la profusion de spécifications versionnées par date constitue elle-même une source de
> fragmentation**. Une grille d'analyse sémantique situe ces gains **essentiellement aux niveaux
> technique et syntaxique** — transports, schémas, autorisation. Le niveau sémantique reste **repoussé
> vers la couche applicative** (ch. 9 § 9.4).

### 8.2.2 Autorisation et identité : le serveur comme serveur de ressources

L'autorisation est **un cas d'étagement plutôt que de réinvention** : elle réutilise massivement la
pile d'identité classique posée au ch. 3 § 3.2.

Une révision qualifie le serveur de **serveur de ressources**, en lui imposant la **validation
d'audience** des jetons et la **découverte de ses métadonnées** par des mécanismes normalisés. ⚠ **La
validation d'audience est ici décisive, et sa fonction mérite d'être nommée précisément : elle confine
un jeton à un destinataire déclaré, et prive ainsi de son ressort la classe d'attaque du mandataire
confus** — celle-là même que le ch. 3 § 3.1.1 identifiait comme défaut structurel des architectures
déléguées. C'est l'un des rares endroits du mouvement où un mécanisme protocolaire **prend nommément
pour cible** une classe d'attaque connue ; la fermer reste à la charge de l'implémentation.

Une révision ultérieure ajoute la découverte d'identité, des documents de métadonnées de client, et le
**consentement incrémental** — élargir le périmètre d'accès au fil des besoins plutôt que d'exiger
d'emblée une autorisation large. C'est le moindre privilège du ch. 6 § 6.5.2, porté par le protocole
plutôt que par l'exploitant.

⚠ **Qualification, au sens de R-02 du Vol. III, et rappel de la réserve F-01.** Ce que ce cadre
**démontre** : qu'un jeton présenté est confiné à l'audience déclarée, et que les métadonnées du
serveur sont découvrables par un chemin normalisé. Ce qu'il **ne démontre pas** : que
l'implémentation valide effectivement l'audience, que le serveur est digne de confiance, ni que
l'outil invoqué se comporte comme sa description l'annonce. **Cadre d'autorisation, jamais
« sécurisé ».**

⚠ **Une réserve de statut sur le socle sous-jacent** : le cadre d'autorisation de nouvelle génération
sur lequel s'appuie cette pile **demeure un projet à la date d'arrêt des sources**, la version
antérieure restant la base normative en vigueur. Le ch. 3 § 3.2.1 porte la même réserve, et le **volet
Livre I de la porte G-1 les a instruites toutes deux le 27 juillet 2026**
([`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md), fait 8) : le document **est toujours à l'état de
projet**, désormais daté, et **aucune version normative n'en est issue**. *La réserve n'est pas levée ;
elle est datée* — et c'est le seul effet qu'une instruction à la source pouvait avoir sur un texte qui
n'a pas bougé.

### 8.2.3 Vers une sémantique des résultats : sorties structurées et tâches

L'effort pour donner un **sens machine-vérifiable** aux résultats d'outils progresse par étapes : des
**sorties structurées** et des **liens de ressources** permettent à un serveur de renvoyer non plus un
bloc de texte libre mais une **charge utile typée** ; une révision ultérieure adopte un dialecte de
schéma normalisé pour les décrire.

S'y ajoutent les **tâches asynchrones**, ⚠ **expérimentales** : un appel d'outil peut renvoyer un
identifiant de tâche — logique « appeler maintenant, récupérer plus tard » — au lieu d'un résultat
immédiat. Ce mécanisme **se rapproche, sans s'y identifier**, de l'exécution durable de l'intégration
d'entreprise : il gère la longue durée, mais **ne fournit pas les garanties de reprise et
d'idempotence** d'un moteur durable. Le contrat de ces tâches **ne saurait être présenté comme
stable**.

⚠ **Une limite de fond demeure, et elle est la plus importante de la section : un schéma n'est pas une
ontologie.** Un dialecte de schéma contraint la **forme** d'une sortie, **non son interprétation** ; il
ne dit ni ce que les valeurs signifient, ni comment elles se relient à un vocabulaire partagé. Que ce
verrou n'ait pas de réponse protocolaire relève d'une **absence de documentation** au sens de R-14 :
le socle n'en recense aucune, ce qui n'établit pas qu'il n'en existe pas. Le ch. 9 § 9.4 l'instruit.

---

## § 8.3 — Conformité, registre, dépréciation et gouvernance

### 8.3.1 Du projet d'éditeur à la fondation : l'appareil de gouvernance

La maturation en standard interopérable passe par un **appareil qui dépasse la spécification**.

Le **registre officiel** fournit un catalogue de serveurs reposant sur un descripteur normalisé et une
**vérification de propriété d'espace de noms** ; il distingue la **découverte** (registre) de la
**distribution** (place de marché) — distinction que le ch. 9 § 9.1 approfondit.

Le versant **conformité** s'appuie sur un cadre dédié et un outil d'inspection, qui **ciblent les
révisions datées**. ⚠ Conformément à la réserve F-01, ces outils valident qu'une implémentation
**respecte une révision** ; ils ne la déclarent pas sécurisée.

La **politique de dépréciation formelle** introduite par la cinquième révision — statuts *actif*,
*déprécié*, *retiré*, assortis d'un préavis d'au moins douze mois entre dépréciation et retrait —
constitue un mécanisme de maturité **comparable à ceux des organismes de normalisation classiques**
(ch. 3 § 3.4.4) : *elle rend l'évolution du contrat prévisible*. C'est, de toutes les nouveautés
annoncées, celle qui intéresse le plus une institution réglementée — et celle dont le ch. 7 § 7.1.5
faisait le troisième terme de l'invariant.

La bascule la plus significative reste le **passage du projet d'un éditeur à une fondation neutre**,
en décembre 2025 (ch. 7 § 7.4) : le standard est soustrait au contrôle d'un acteur unique.

### 8.3.2 Registres, passerelles et découverte d'entreprise — versant outillage

⚠ **Cette sous-section traite le versant *outillage* seul.** La **pile protocolaire** est au ch. 9
§ 9.2 ; les **registres gouvernés**, au versant identité et conformité, sont au **ch. 15** (Livre II).
Trois traitements distincts d'un même objet, et le partage est déclaré au plan.

À mesure que les serveurs se multiplient, **la découverte et la gouvernance deviennent des problèmes
d'ingénierie distincts**. L'écosystème dépasse les **dix mille serveurs publics** — ordre de grandeur
qui **change la nature du risque**.

En entreprise, une **passerelle** s'interpose entre les agents et les serveurs pour centraliser
l'authentification, l'autorisation à granularité fine, la journalisation et l'application de
politiques — jouant le rôle qu'une passerelle d'API tient dans l'intégration classique (ch. 1
§ 1.4.3). ⚠ **Cette médiation est aussi une nécessité de sécurité** : un catalogue ouvert de plusieurs
milliers de serveurs constitue **une surface de chaîne d'approvisionnement de premier plan**.

Un serveur peut être **malveillant dès l'origine** ou **le devenir par mise à jour silencieuse**, et
une description d'outil piégée peut détourner l'agent. Ces vecteurs sont analysés au **ch. 11**.

La découverte d'entreprise impose donc une posture de **liste d'admission**, d'**épinglage de
versions** et de **revue des serveurs admis** — par analogie avec la gestion d'un registre d'artefacts
logiciels. *Le contrat d'outil ne suffit pas si sa provenance n'est pas garantie : l'évolution non
maîtrisée d'un serveur est elle-même un risque.*

---

## § 8.4 — A2A v1.0 : la délégation entre pairs

### 8.4.1 Du Contract Net aux patrons transposés

La coordination par appel d'offres **précède de plusieurs décennies** l'ère des grands modèles. Le
**Contract Net** formalisait dès 1980 un cycle d'allocation de tâches entre nœuds d'un solveur
distribué : **annonce → appel d'offres → soumissions → attribution**. Ce schéma a été repris et
standardisé, aux côtés d'un langage de communication à performatifs (ch. 7 § 7.2.1).

Transposé aux essaims d'agents, le patron **reste pertinent** : un coordinateur peut solliciter
plusieurs agents spécialisés et retenir celui dont la réponse, le coût ou la disponibilité conviennent
le mieux.

⚠ **Mais le constat d'état est net, et il se pose sans détour comme il se borne.** À l'état 2024-2026
que la source déclare, **aucun des trois protocoles majeurs examinés ici — agent-outil, agent-agent,
alternative décentralisée — ne normalise un cycle d'enchères complet à la manière historique.** La
négociation y demeure soit **implicite**, portée par le langage naturel dans l'invite, soit **ad
hoc**, codée au cas par cas dans la logique applicative. *Le constat porte sur trois spécifications à
une date ; il ne vaut pas pour l'ensemble des protocoles agentiques.*

La leçon d'adoption de la lignée historique — **l'échec relatif d'un formalisme lourd** (ch. 7
§ 7.2.1) — pèse manifestement sur les choix de conception actuels, qui privilégient des **contrats
minimaux**. C'est un arbitrage assumé, dont le § 8.6.2 mesure le prix.

### 8.4.2 Agent Card signée, modèle de tâche et structure des messages

Le protocole agent-agent constitue la **référence de l'axe horizontal**. Sa version 1.0 en fixe les
structures essentielles.

L'**auto-description** repose sur l'**Agent Card** : un document publié à un emplacement **bien
connu**, conforme à un mécanisme normalisé, qui déclare **l'identité, les capacités et les modalités
d'interaction** de l'agent.

L'unité de travail est la **tâche**, objet à état traversant un cycle de vie défini — soumise, en
cours, requérant une entrée ou une authentification, puis achevée, échouée, annulée ou rejetée. Les
échanges s'articulent autour d'une hiérarchie **message / partie / artefact**.

Trois consolidations de la version 1.0 méritent d'être relevées :

1. la **signature des Agent Cards**, qui lie l'authenticité de la carte **à son domaine d'origine** ;
2. la prise en charge de la **multi-location** ;
3. la **pluralité de liaisons de transport** — JSON sur HTTP, appels de procédure en JSON, appels de
   procédure binaires.

⚠ **La troisième illustre l'argument d'étagement du ch. 7 § 7.1.6** : ce protocole **ne réinvente pas
la couche de transport**, il réemploie la pile classique.

⚠ **Qualification, au sens de R-02 du Vol. III — et la nuance porte sur ce qu'une signature établit.**
Une Agent Card signée **démontre** que la carte a été émise par le détenteur de la clé associée au
domaine déclaré, et qu'elle n'a pas été altérée. Elle **ne démontre pas** que l'agent se comporte
conformément aux capacités qu'il déclare, ni que le domaine est digne de confiance. *Signer une
déclaration l'authentifie ; cela ne la rend pas vraie.* Le ch. 16 rencontrera la même limite sur le
passeport d'agent.

⚠ **Lacune héritée, portée et non comblée** *(PRD du Vol. II §10.9)*. Quatre objets **ne sont pas au
socle** : l'**ancrage de confiance** des Agent Cards signées — c'est-à-dire à quelle autorité remonte
la chaîne —, la **date exacte de la v1.0**, la **multi-location**, et l'**inventaire infonuagique** du
protocole agent-outil (§ 8.7). Ils sont **signalés ici, encadrés, et renvoyés au ch. 49**. Les combler
par une source de moindre qualité serait la faute que la règle du dépôt proscrit. ⚠ **Constat du
28 juillet 2026, qui ne comble rien** : l'instruction du volet résiduel de G-1 a relevé un matériau
touchant la **date de la v1.0** et **ne l'a pas versé au socle**, l'instruction d'une lacune relevant
d'une passe de socle. *Un matériau relevé n'est pas une entrée* : les quatre objets restent hors socle,
et ce chapitre continue de s'en abstenir.

⚠ **Métrique auto-déclarée, attribuée** : le franchissement d'un seuil de **plus de 150 organisations
de soutien** en avril 2026 est **rapporté par la Linux Foundation**, qui gère le protocole. Le socle
qualifie lui-même « organisation de soutien » de **notion non définie**, et la réserve du ch. 7 § 7.6
s'applique intégralement — *soutien n'est pas production*.

### 8.4.3 Délégation de tâches et collaboration inter-cadriciels

La valeur propre de ce protocole réside dans la **délégation** : un agent client confie une tâche à un
agent distant — relevant d'un autre cadriciel, d'un autre fournisseur, **voire d'une autre
organisation** — qui exécute le travail et renvoie des artefacts.

Le mécanisme franchit ainsi la **frontière organisationnelle**, c'est-à-dire **le niveau le plus élevé
de l'interopérabilité conceptuelle** (ch. 1 § 1.1.2) : deux systèmes développés indépendamment
collaborent **sans intégration préalable**, sur la seule base du contrat exposé par la carte et du
cycle de vie de la tâche.

⚠ **Une caractéristique de conception mérite d'être soulignée parce qu'elle est contre-intuitive :
l'opacité voulue.** L'agent distant **n'expose ni son raisonnement interne, ni les outils qu'il
mobilise, ni son modèle sous-jacent** ; il ne présente qu'une interface de tâche et ses résultats.

Cette opacité est **le pendant agentique du découplage** : elle protège l'autonomie et la
confidentialité du fournisseur **tout en garantissant la substituabilité** de l'agent délégataire
derrière son contrat. Elle marque aussi la frontière avec l'axe vertical : *là où un serveur d'outils
expose des capacités à contrôler finement par le client, un agent expose une capacité encapsulée à
déléguer en bloc.*

Lecture de l'auteur — cette opacité est une force pour le découplage et une difficulté pour tout ce
que le Livre III exigera. Un exploitant tenu de démontrer devant un tiers **ce qui s'est passé** ne
peut pas produire l'état d'un traitement qu'il a délégué en bloc à un agent opaque. Le socle n'établit
pas cette tension ; elle est proposée comme lecture, et le ch. 29 l'instruit.

---

## § 8.5 — L'ACP protocolaire, l'alternative décentralisée et l'état de la standardisation

### 8.5.1 La convergence par fusion — mécanique

> ⚠ **SIÈGE DE LA MÉCANIQUE DE LA FUSION POUR TOUTE LA SOMME.** Elle est **posée ici une seule
> fois** ; sa **portée de risque** siège au **ch. 10 § 10.5**. Aucun autre chapitre ne refait l'un ni
> l'autre — l'abstention est contrôlée par `PRD/check-sieges.py`.

⚠ **Partage déclaré avec le ch. 10 (décision 2 du TOC).** La **mécanique** de la convergence se traite
**ici**, sur la source du Vol. I ; la **portée de risque** de cette fusion se traite **au ch. 10
§ 10.5**, sur la source du Vol. II. *Ni l'un ni l'autre ne reconstruit ce que porte son voisin* — et ce
partage est l'un des deux écarts que la révision v0.17 du plan a soldés, l'objet ayant été revendiqué
par les deux chapitres.

⚠ **Convention de nomenclature, rappelée ici comme à chaque occurrence (R-8 du Vol. II, R-13 du
Vol. III).** L'**ACP protocolaire** désigne l'*Agent Communication Protocol* d'un centre de recherche
et de son projet ouvert, sur l'axe agent-agent — **à ne pas confondre** avec l'**ACP commercial**, sur
l'axe du commerce, traité au ch. 10 § 10.3.2. **Le siège de l'encadré des quatre branches est au
ch. 7 § 7.5** ; il n'est pas reconstruit ici.

Conçu au début de 2025, l'ACP protocolaire reposait sur une approche **résolument classique** : une
interface REST sur HTTP, des messages multipartites, des modes synchrone et asynchrone, et une
découverte **fonctionnant même hors ligne**.

**Sa trajectoire constitue l'enseignement central de cette sous-section.** Le 29 août 2025, il **a
rejoint le protocole agent-agent** sous l'égide de la fondation, accompagné de **guides de
migration**. Plutôt qu'une concurrence prolongée entre standards homologues — qui aurait fragmenté
l'écosystème et **reproduit la dispersion qu'avait connue le monde des services web** —, l'industrie a
opté pour une **convergence par fusion**.

Cette issue, où un protocole **se fond dans un autre** sous une fondation neutre, illustre un mode de
**standardisation par consolidation institutionnelle**. Elle conforte la proposition du ch. 7 § 7.4 :
la neutralité de gouvernance agit comme **mécanisme anti-fragmentation**.

⚠ **Garde-fou R-1 du Vol. II** : **l'ACP protocolaire n'est pas un standard vivant.** Son
développement actif a cessé ; il ne subsiste qu'à travers le protocole absorbant et des adaptateurs.

### 8.5.2 L'alternative décentralisée

⚠ **Un écart de titre est assumé et déclaré par le plan.** Le protocole décentralisé arrive dans ce
chapitre **par l'intervalle** de sa ligne Fusion, et il **n'est pas nommé au titre** — lequel reste
« MCP (agent-outil) et A2A (agent-agent) ». Retoucher ce titre déplacerait — **selon le plan** — un
renvoi **cité en clair dans huit chapitres**, et cet objet y est traité **comme un tiers comparé, non
comme un objet du même rang**. L'écart est déclaré, non oublié : c'est la même classe que le § 1.2 du
ch. 1, couvert par l'intervalle sans être glosé au titre.

Ce protocole emprunte une voie **résolument distincte** : décentralisée, pair-à-pair. Son architecture
s'organise en **trois couches** :

- à la base, une couche d'**identité** fondée sur des **identifiants décentralisés**, déclinés dans
  une méthode propre, assortie de chiffrement et d'une authentification par signatures de message ;
- au sommet, une couche de **protocole applicatif** ;
- entre les deux, **l'élément le plus original** : un **négociateur de méta-protocole**, capable de
  négocier dynamiquement **le protocole d'échange lui-même**, à l'exécution.

La sémantique des messages s'appuie sur des formats du Web sémantique (ch. 2 § 2.3.1).

⚠ **Cette négociation de méta-protocole constitue la réponse la plus aboutie au problème de la
négociation de capacités**, en cela qu'elle relève du **niveau dynamique** du modèle LCIM (ch. 7
§ 7.1.3) — celui où *le protocole lui-même devient objet d'accord à l'exécution*.

Sa **maturité reste néanmoins conditionnée** à celle de l'infrastructure d'identité décentralisée
sous-jacente, dont l'adoption à large échelle **n'est pas attendue avant 2027 environ** — projection à
traiter comme telle, non comme un fait daté.

### 8.5.3 Comparaison et état de la standardisation

L'état à la mi-2026 se laisse résumer par la confrontation de trois familles : le protocole
agent-agent, **stable et largement adopté**, occupe le centre de gravité de l'axe horizontal ; l'ACP
protocolaire y est **désormais fusionné** ; l'alternative décentralisée demeure **plus expérimentale
et tributaire** de son socle d'identité.

Au-delà des trois protocoles, **plusieurs forums travaillent à coordonner l'ensemble** — groupes
communautaires de normalisation du Web, projets de spécification à l'organisme des protocoles
d'Internet, initiatives de fondation autour d'un langage de définition d'agent.

⚠ **Une perspective doit être maniée au conditionnel, et l'avertissement est explicite dans la
source** : une **spécification conjointe** rapprochant formellement l'axe vertical et l'axe horizontal
**est attendue, et le socle n'en recense aucun projet public** à la date d'arrêt — *ce qui n'établit
pas qu'il n'en existe pas.* **Toute affirmation sur son contenu ou son calendrier relève de la
projection.**

---

## § 8.6 — La frontière : une complémentarité déclarée, et par qui

### 8.6.1 Limites et modes d'échec de l'axe vertical

Le contrat agent-outil présente des modes d'échec **qui lui sont propres** et tiennent à la nature
**lue-par-le-modèle** de ses descriptions :

- **l'empoisonnement d'outils** — injecter des instructions malveillantes dans la **description** d'un
  outil, ingérée par le modèle **comme si elle émanait d'une source de confiance** ;
- **le mandataire confus et le vol de jeton** — exploiter une autorisation mal confinée, ce à quoi
  répond précisément la validation d'audience (§ 8.2.2) ;
- **l'absence de versionnement sémantique des outils** — *le contrat ne signale pas qu'un outil a
  changé de comportement* ;
- **une découverte pauvre**, qui ne permet pas un appariement fin entre tâche et outil (ch. 9 § 9.1).

Le troisième point mérite d'être souligné : c'est **l'évolution**, troisième terme de l'invariant, qui
manque ici. Un schéma stable peut recouvrir un comportement changé, et rien ne le signale.

⚠ **Deux faits datés, et une qualification contestée qu'il faut rapporter comme telle. Les parties se
nomment : une attribution anonymisée n'est pas une attribution.** La **Cloud Security Alliance** a fait
le point sur l'accumulation de vulnérabilités dans une note de 2026 ; une divulgation d'**OX Security**
(avril 2026) a **estimé à environ 200 000 le nombre d'instances exposées** par un comportement de
transport par défaut. ⚠ **La qualification de ce comportement comme « défaut de conception » demeure
contestée**, **Anthropic** le tenant pour **un choix intentionnel documenté**. La somme **rapporte le
désaccord et ne le tranche pas** — et le chiffre demeure **une estimation d'un tiers, attribuée à
chaque occurrence à celui qui la produit**. Que ce désaccord n'ait pas été arbitré publiquement relève
d'une **absence de documentation** au sens de R-14.

⚠ Et la réserve F-01 tient jusque dans la description des échecs : ce sont des **risques attachés à un
cadre d'autorisation**, non la démonstration qu'un protocole « sécurisé » aurait failli.

### 8.6.2 Modes d'échec propres à l'axe horizontal

La coordination agent-agent se déploie **sur un spectre**. À une extrémité, la **négociation
implicite**, portée par le langage naturel dans l'invite — elle **domine la pratique**, au prix d'une
**absence de garantie vérifiable** sur l'accord conclu. À l'autre, la **négociation explicite** — plus
rigoureuse, **peu déployée**.

Cette gradation détermine les modes d'échec :

- un **transport syntaxiquement valide n'exclut pas un désaccord sémantique** sur l'intention : deux
  agents peuvent « s'entendre » sur des messages bien formés tout en **interprétant divergemment la
  tâche** ;
- la délégation introduit ses pathologies — **boucles et interblocages** lorsque des agents se
  renvoient indéfiniment une tâche, **ambiguïté des capacités annoncées**, **perte de l'engagement**
  en cours de chaîne ;
- multiplier les arêtes du graphe d'interaction **élargit d'autant la surface d'attaque**.

Ces défaillances, **irréductibles à un agent isolé**, sont caractéristiques des systèmes composés, et
le **ch. 11** en donne la taxonomie unifiée.

> **Perspective recherche.** Les protocoles à **engagements sociaux observables** (ch. 7 § 7.2.1)
> offrent une réponse théorique à la non-vérifiabilité de la sémantique mentaliste, en ancrant
> l'accord dans des **engagements publics** plutôt que dans des états mentaux supposés — pont direct
> vers les contrats comportementaux probabilistes du ch. 7 § 7.1.5. La nécessité, pour les systèmes
> multi-agents, de **poser des questions de clarification** plutôt que de présumer l'accord est étayée
> empiriquement.

### 8.6.3 « Dans les agents, entre les agents » : une doctrine déclarée par une partie

Reste la doctrine qui donne son titre au chapitre et porte sa thèse.

Elle est **explicite** : le protocole agent-agent se déclare **complémentaire du protocole agent-outil
et non un remplacement**. La répartition est énoncée sans ambiguïté — *l'un pour l'intégration des
outils et du contexte au niveau de l'agent individuel, l'autre pour la communication et la
coordination entre agents* —, et se résume dans la formule « **dans les agents, entre les agents** ».

⚠ **Deux précisions d'attribution s'imposent, et elles sont le cœur de cette section.**

**Première : cette doctrine est celle du projet agent-agent.** Le socle la trace **au site de ce
protocole**, dans l'annonce de sa version 1.0. Elle **n'est pas un accord conjoint publié par les deux
projets**, et la somme **ne dispose d'aucune source établissant que l'autre projet l'a endossée dans
ces termes**. Cela n'en diminue pas la valeur — une déclaration publique de non-remplacement est un
engagement que les spécifications ultérieures pourront confirmer ou démentir — **mais cela en fixe le
statut : une position déclarée par une partie, non un traité entre deux parties.**

**Seconde : la formule « de nombreux systèmes utilisent les deux » n'est pas une métrique.** Elle
n'est ni chiffrée, ni datée, ni définie, et **elle émane du même projet**. Elle établit que la
combinaison est **prévue et revendiquée par les mainteneurs** ; elle n'établit **aucun volume de
déploiement**. ⚠ Le lecteur reconnaîtra ici la réserve centrale du ch. 7 § 7.6 — *le soutien déclaré
ne vaut pas déploiement* — **dans une variante plus discrète, et pour cela plus insidieuse**.

⚠ **Précision de régime, datée du 28 juillet 2026, et elle porte sur la forme de la trace, non sur son
fond.** L'instruction à la source primaire **confirme la doctrine** et **échoue à retrouver le
verbatim** que le socle citait, à une adresse qui ne résout plus (`S-013`). *Le fond est attesté, la
citation littérale ne l'est pas* — ce chapitre rend donc la doctrine en français et **ne la reproduit
entre guillemets nulle part**.

Ces réserves posées, reste à dire ce que la doctrine vaut. Lecture de l'auteur — **sa valeur n'est pas
descriptive mais prescriptive**. Elle fournit un **critère de découpage** — l'accès aux outils d'un
côté, la délégation entre agents de l'autre —, et un critère de découpage est ce dont **manque
cruellement une organisation qui débute**. Le socle établit la doctrine et son attribution ; il
**n'établit ni cette valeur prescriptive, ni le besoin qu'elle prétend combler**.

⚠ **Mais un critère n'est pas une contrainte, et c'est le troisième terme de la thèse.** Rien, dans
les protocoles eux-mêmes tels que le socle les documente, **n'empêche une équipe de faire transiter
par des appels d'outils ce qui est en réalité une délégation entre agents**, ou l'inverse. *La
frontière entre les deux axes est une décision d'architecture que l'organisation doit prendre,
documenter et défendre — elle n'est pas donnée par la technique.*

⚠ **Et la frontière est floue en pratique — constat de la source, arrêté à juin 2026, non une
opinion** : les **tâches asynchrones** de l'axe vertical (§ 8.2.3) **empiètent sur le terrain de la
délégation** de l'axe horizontal — recouvrement **postérieur** aux revues d'interopérabilité de
l'écosystème, qui ne pouvaient donc pas en tenir compte. Mieux vaut retenir un **critère de choix
pragmatique** qu'une frontière nette : *l'axe vertical lorsqu'on consomme une capacité bien délimitée
sous le contrôle de l'hôte ; l'axe horizontal lorsqu'on délègue une tâche à un acteur opaque et
autonome.*

⚠ **Il serait enfin malhonnête de laisser croire que cette doctrine est le seul découpage
disponible.** Le socle en documente **au moins deux autres** : une feuille de route séquentielle
antérieure, **dont le ch. 7 § 7.3 a montré que la deuxième étape est devenue obsolète comme
prescription** ; et le positionnement d'une couche d'infrastructure articulant l'espace **par les
couches plutôt que par les axes**, que le ch. 10 § 10.2 examine. Que ces découpages soient moins
commodes ou datés est défendable ; **qu'ils n'existent pas ne l'est pas.**

---

## § 8.7 — Les intégrations infonuagiques : lire le statut, pas la présence

Un protocole ouvert **ne vaut, pour une institution, que par les plateformes qui l'implémentent**. Sur
ce point, le socle documente l'axe horizontal avec précision — ⚠ **et il faut d'abord relever une
asymétrie : cette précision ne porte que sur lui.**

L'état documenté au printemps 2026 est le suivant. Chez un premier fournisseur, le protocole est
intégré à une plateforme d'atelier en **préversion**, et à un produit d'assistant en **disponibilité
générale depuis avril 2026**. Chez un deuxième, l'intégration est portée par un environnement
d'exécution d'agents. Chez le troisième, elle est **d'origine**, le protocole y étant né.

⚠ **Ces statuts sont documentés par des sources d'avril 2026, et l'instruction du 28 juillet 2026 ne
les a rouverts qu'à moitié** (socle consolidé `S-003`). **Les deux statuts du premier fournisseur
tiennent** : la plateforme d'atelier porte toujours sa mention de préversion, le produit d'assistant
n'en porte aucune. **Le volet du deuxième fournisseur n'a pas été consulté.** *Une confirmation
partielle n'est pas une confirmation* — l'inventaire reste borné à ce qui a été rouvert, et le reste
demeure à la date de sa source.

Cet inventaire dit **deux choses**.

**La première** : les trois grands fournisseurs d'infonuagique public implémentent le protocole, et
les trois **siègent au comité de pilotage technique** (ch. 7 § 7.4.1). Lecture de l'auteur — le socle
établit les intégrations et la composition du comité ; **la convergence qu'on y lit, et son caractère
peu commun dans un marché disputé, est une inférence d'architecture**, non un fait documenté.

**La seconde est plus utile encore à qui prépare un dossier : les statuts diffèrent, et c'est la
différence qui compte.** Une **préversion** et une **disponibilité générale** n'engagent pas le
fournisseur au même degré. Lecture de l'auteur — ⚠ le socle établit **les statuts**, **pas ce qu'ils
emportent** : la somme ne documente ni les garanties de service attachées à chaque statut, ni leur
réception par une seconde ligne de défense. Ce qui en découle tient en une consigne : *l'architecte
prudent lit le statut avant de lire la marque.*

⚠ **Il faut enfin nommer une limite de ce chapitre plutôt que la laisser se combler par le silence.**
Le socle fournit cet inventaire pour l'axe horizontal ; **il ne fournit pas d'inventaire équivalent,
plateforme par plateforme et statut par statut, pour l'axe vertical**. Ce qu'il documente de ce
dernier se trouve du côté des **cadriciels d'orchestration**, et relève du ch. 23.

⚠ **L'absence d'un inventaire infonuagique de l'axe vertical dans le socle n'établit pas l'absence
d'un tel support** : elle établit que **la somme ne peut pas en dresser la carte**. C'est, au sens de
R-14 du Vol. III, une **absence de documentation** — degré 3, qui n'autorise aucune conclusion. *La
distinction est celle entre ce qui n'existe pas et ce qui n'a pas été vérifié ; la somme s'astreint à
ne jamais la franchir.*

---

## § 8.8 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui a été enfreint à la rédaction** — portes **G-1**, **G-2** et **G-3** ouvertes ; instruction
d'auteur du 27 juillet 2026. Conséquences habituelles : aucun énoncé central au sens de CA-IV-01,
aucun décompte publiable, renvois de plan et non de texte.

⚠ **Deux de ces trois conséquences sont tombées depuis, et la troisième ne tombe pas.** *(1)* Le
**décompte est publiable** depuis G-2 (27 juillet 2026) ; il est porté au champ *Volumétrie cible*.
*(2)* Les **renvois sont devenus des renvois de texte** : les cinquante chapitres existent en brouillon
depuis le 27 juillet 2026, et les huit cibles de cette pièce — ch. 9, 10, 11, 15, 16, 23, 29 et 49 —
sont rédigées. Leurs **numéros de section résolvent** contre le texte ; ⚠ **le fond de ce qu'ils
promettent n'a pas été re-vérifié** par cette passe, qui n'ouvre qu'une pièce. *(3)* ⚠ **La première ne
tombe pas** : G-3 est franchie depuis le 28 juillet 2026, mais **cette pièce n'a pas été ré-résolue
contre le socle consolidé** — *aucun énoncé n'est central au sens de CA-IV-01*, et il ne le deviendra
pas d'un franchissement dont la pièce n'a pas été relue.

**Remontée ouverte par ce chapitre — et c'est la plus urgente de tout le Livre I :**

- **R-IV-10 — non bloquante, mais d'échéance immédiate.** La **révision candidate** du protocole
  agent-outil avait sa **ratification annoncée pour le 28 juillet 2026**, soit **le lendemain de la
  rédaction de ce chapitre**. Elle porte des **changements cassants** : cœur sans état, dépréciation
  de trois primitives, remplacement du mécanisme d'enregistrement de client. **Si elle est ratifiée,
  les § 8.1.3, § 8.2.1, § 8.2.2 et § 8.3.1 sont à revalider en bloc**, sources primaires à extraire —
  et non à retoucher. ⚠ **Elle l'a été le 28 juillet 2026** : voir la clôture ci-dessous.

  Le chapitre a paré ce risque de la seule manière défendable : **en déclarant que l'anatomie décrite
  est celle de la révision 2025-11-25**, et en portant le statut de candidate à chacune de ses
  mentions. ⚠ **Il ne l'a pas anticipée** : décrire comme acquis un contrat non ratifié aurait été la
  faute exacte que le régime de preuve de la somme proscrit. *Une révision annoncée pour demain reste
  une révision annoncée.*

**Une observation de méthode, sans remontée.** Ce chapitre est celui où la **réserve F-01** du Vol. II
mord le plus — **quatre occurrences marquées** au sens de la décision 16 du TOC, et la formule tenue
au-delà de ses marqueurs —, et la répétition est délibérée. La formulation « cadre d'autorisation,
jamais sécurisé » n'est pas une précaution de langage : elle sépare **ce qu'une spécification
fournit** de **ce qu'une implémentation garantit**, et c'est la même distinction que R-02 du Vol. III
impose en matière cryptographique. Les deux garde-fous, venus de volumes différents, disent la même
chose. ⚠ **La fusion que cette observation appelait n'a pas eu lieu** : G-3 a été franchie le
28 juillet 2026 **sans que les deux séries héritées soient rapprochées**, et elles restent citées
préfixées de leur volume.

**Ce qui n'est pas enfreint.** La structure suit la table détaillée (§ 8.1 à § 8.7). La table de
couverture est respectée, dont **l'arrivée du Vol. I *Monographie* §2.5.4 depuis le ch. 4** — déclarée
aux deux bouts — et la sortie du Vol. I *Monographie* §3.6 vers le Livre II. Les **deux écarts que la
v0.17 du plan a soldés sont tenus** : le **partage déclaré** sur la fusion de l'ACP protocolaire —
mécanique ici, portée de risque au ch. 10 — et l'**écart de titre assumé** sur le protocole
décentralisé, nommé à la liste de sections sans retoucher un titre que le plan déclare cité en clair
dans huit chapitres. Le **siège de l'encadré R-8 reste au ch. 7 § 7.5** : ce chapitre y renvoie et **ne
le reconstruit pas**, et le **siège de la mécanique de la fusion, posé ici au § 8.5.1**, ne recouvre
pas la portée de risque qui siège au ch. 10 § 10.5. La **lacune héritée du PRD Vol. II §10.9 est
portée, encadrée et non comblée**. R-1, R-8, R-13, R-02 et R-14 sont tenus à toutes leurs occurrences.

**Deux applications du régime des métriques auto-déclarées, et elles ne sont pas de même nature.** Au
§ 8.4.2, le décompte d'organisations de soutien est **attribué à l'organisme qui le publie** et assorti
de la réserve *soutien n'est pas production*. Au § 8.6.3, la formule « de nombreux systèmes utilisent
les deux » est **refusée comme métrique** — ni chiffrée, ni datée, ni définie. *Refuser une formule au
rang de métrique n'est pas l'attribuer : c'est constater qu'il n'y a rien à attribuer.* S'y ajoute, au
§ 8.6.1, une **estimation d'un tiers** attribuée nommément à celui qui la produit (décision 15 du TOC :
l'attribution ne s'anonymise jamais).

---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-10 — close par le franchissement de G-1 (volet Livre I) : la réserve est confirmée, et
  l'échéance est désormais datée au lieu d'être ouverte.** Constat à la source primaire le 27 juillet
  2026 (registre du gel, fait 11) : la révision est **toujours candidate**, verrouillée depuis le
  21 mai 2026, et sa publication finale est fixée au **28 juillet 2026**. Le chapitre est donc
  **exact à sa date**, et périmé le lendemain. ⚠ **Le gel unique ne s'avance pas d'un jour pour
  absorber l'événement** — *une révision annoncée pour demain reste une révision annoncée* : les
  § 8.1.3, § 8.2.1, § 8.2.2 et § 8.3.1 sont à **revalider en bloc dès le 28 juillet 2026**, sources
  primaires à extraire et non à retoucher. La portée du changement est relevée au registre du gel
  pour que la revalidation sache quoi chercher.
- ⚠ **Un contrôle de méthode a été payé sur cette pièce, et il vaut d'être connu.** Le billet
  d'annonce de la révision décrit un *durcissement* du mécanisme d'enregistrement de client et ne
  mentionne aucune dépréciation ; le **journal des changements de la spécification** la porte
  explicitement, au profit de documents de métadonnées d'identifiant client. L'énoncé de cette pièce
  — « dépréciation … de l'enregistrement dynamique de client » — est **exact**, et une correction
  fondée sur le seul billet d'annonce l'aurait **cassé**. *Une source secondaire qui résume une
  source normative n'en est pas un substitut, même quand elle émane du même émetteur.*

⚠ **Ce que la clôture ne changeait pas, à sa date.** La porte **G-3** demeurait ouverte : le socle
consolidé comptait **zéro entrée**, l'Annexe B n'existait pas, et **aucun énoncé de cette pièce n'était
central au sens de CA-IV-01**. *Zéro remontée ouverte ne veut pas dire pièce recevable — cela veut dire
qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée.*

---

### Passe de relecture — 28 juillet 2026

⚠ **Hors plan comme ce qui précède, et se retire avec.** Trois faits datés du 28 juillet 2026 touchent
cette pièce, et **aucun ne la rend recevable**.

- ⚠ **La péremption annoncée par R-IV-10 EST ADVENUE, à la date même.** La révision est publiée : la
  page de spécification courante la sert, l'index documentaire du site ne connaît plus la précédente
  (socle consolidé `S-001`, registre du volet résiduel de G-1). *Le chapitre était exact à sa date, et
  il ne l'est plus à celle-ci pour ce qu'il décrit du contrat courant.* ⚠ **La revalidation en bloc des
  § 8.1.3, § 8.2.1, § 8.2.2 et § 8.3.1 est OUVERTE et NON EXÉCUTÉE** : elle appelle une extraction de
  la révision neuve à sa source, qu'aucune passe n'a conduite — *constater une bascule n'est pas lire
  le texte qui a basculé*. La relecture s'est donc bornée à **dater la péremption**, sans réécrire une
  anatomie qu'elle ne peut pas vérifier.
- **La porte G-3 est franchie et le socle consolidé existe** — 159 entrées, dont les quatre du Vol. II
  que le TOC assigne à ce chapitre (`S-001`, `S-002`, `S-003`, `S-013`). ⚠ **La correspondance est
  portée à l'en-tête ; la ré-résolution des énoncés contre ces entrées reste DUE**, et elle est hors du
  mandat d'une passe de relecture qui n'ouvre qu'une pièce. *Une porte franchie après coup ne relit pas
  les pièces qu'elle conditionnait.*
- **Les cardinaux et les attributions de la pièce ont été re-mesurés sous les décisions 15 et 16 du
  TOC.** Trois écarts d'appareil sont corrigés : la réserve F-01 était annoncée à six occurrences pour
  **quatre marqueurs**, les métriques auto-déclarées à trois pour **deux applications de nature
  différente**, et l'estimation du § 8.6.1 était présentée comme « attribuée à sa source » **sans que
  la source soit nommée** — ce que la décision 15 proscrit expressément.

⚠ **Ce que rien de tout cela ne change.** **CA-IV-11 et CA-IV-13 demeurent insatisfaisables**, D-6 ne
fournissant pas de relecteur distinct du rédacteur, et **G-4 conditionne encore la collation de fond**.
Cette pièce reste un **brouillon non publiable**. *Zéro remontée ouverte ne veut pas dire pièce
recevable — cela veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée.*
