# Chapitre 8 — L'identité et les registres d'agents

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-07, F-08 ; F-01, F-09, F-25, F-36 (renvois) |
| Garde-fous à surveiller (PRD §8) | **R-2** (aucun registre centralisé Entra vérifié), **R-3** (la spécification CSA s'appuie sur SPIFFE/SPIRE comme fondation ; l'exigence stricte n'est pas établie), **§8.2.5** (statuts pré-normatifs : brouillon de labs, brouillon IETF expiré) |
| Volumétrie cible | ~2400 mots |

> **Thèse ([TOC.md](../../TOC.md))** : l'identité des agents s'ancre dans les standards existants (OAuth/OIDC, SCIM) ; le registre d'agents gouverné devient la pièce maîtresse de la conformité à venir.

---

Un agent qui appelle un système d'entreprise le fait sous une identité. La question n'est jamais de savoir s'il en possède une — il en possède nécessairement une, ne serait-ce que celle du compte technique sous lequel son processus s'exécute. La question est de savoir si cette identité lui est *propre*, si elle est *administrable*, et si le journal qu'elle produit permet, six mois plus tard, de répondre à un vérificateur qui demande qui a décidé quoi. Les chapitres précédents ont décrit ce qui fait agir les agents ; celui-ci décrit ce qui permet de les nommer, de les inventorier et de borner ce qu'ils peuvent atteindre.

Deux objets structurent le domaine à la date de gel du présent chapitre, et ils ne sont pas du même ordre. Le premier est un produit disponible, gouverné par un éditeur, en disponibilité générale (*general availability*) chez ses clients. Le second est une spécification de registre, publiée par un organisme sectoriel, à l'état de brouillon. Le premier ancre l'identité des agents dans des standards ratifiés — en les étendant. Le second ancre le profil de l'agent dans un standard ratifié — par une extension qui ne l'est pas. Ce chapitre soutient que ce décalage n'est pas un détail de calendrier : il est la caractéristique déterminante du domaine, et il commande la prudence de l'architecte qui doit en dépendre d'ici l'entrée en vigueur du 1er mai 2027[^7].

## 8.1 Entra Agent ID : l'identité d'agent comme objet d'annuaire

Microsoft Entra Agent ID est passé en disponibilité générale vers avril-mai 2026, pour l'ensemble des clients Entra[^1]. Il livre deux capacités : la création et la gestion d'**identités d'agents** (*agent identity*) — une identité propre attribuée à un agent, distincte de celle d'un utilisateur — et la gestion de *blueprints*. Ses fondations sont explicitement des standards existants : OAuth 2.0 pour l'autorisation, OpenID Connect pour l'authentification. Deux familles de scénarios sont documentées : *app-only* et délégués[^1].

Pour un architecte d'entreprise, la portée de cette annonce est considérable, et elle mérite d'être formulée sans emphase. Faire de l'agent un objet d'annuaire, c'est le faire entrer dans les processus de gestion des identités et des accès qui existent déjà dans l'institution : provisionnement, revue périodique des accès, révocation. Ce n'est pas une capacité nouvelle en soi — c'est l'extension d'une capacité éprouvée à une catégorie de sujets qui, jusque-là, se dissimulaient derrière des comptes techniques partagés.

La gestion de *blueprints* que le socle documente aux côtés des identités[^1] appelle une précision, car le terme est celui de l'éditeur et le socle n'en livre pas la définition : il les énumère aux côtés des identités d'agents, sans en préciser la nature[^1]. Ce que cet ouvrage peut en dire s'arrête là. On se gardera d'y projeter les fonctions d'un registre — c'est précisément l'écueil que la section 8.4 signale.

**Lecture de l'auteur** : la distinction entre les scénarios *app-only* et délégués est, pour une institution financière, la plus lourde de conséquences. Elle détermine si la piste d'audit d'une action désigne un mandant humain identifié ou l'agent seul. Le socle établit que ces deux familles de scénarios existent et qu'elles reposent sur OAuth 2.0 et OpenID Connect[^1] ; il n'établit ni que l'une soit préférable à l'autre, ni ce que les régulateurs canadiens en attendront. Le lien entre ce choix technique et l'imputabilité exigée par le cadre canadien est traité au chapitre 13 ; il n'est pas anticipé ici.

Deux réserves doivent accompagner toute mention de cette disponibilité générale, et elles sont au socle. La première est que la disponibilité générale ne recouvre pas l'ensemble du dispositif : des sous-fonctionnalités demeurent en préversion[^1]. La seconde est d'ordre commercial et pèse sur le dossier d'investissement : les fonctions de sécurité étendues relèvent de licences additionnelles — Entra ID P1/P2, Microsoft 365 E5, Agent 365[^1]. Autrement dit, la capacité de base d'attribuer une identité à un agent est ouverte à tous les clients Entra ; les fonctions de sécurité étendues relèvent de licences additionnelles que le socle ne détaille pas. L'architecte qui présente Entra Agent ID comme « disponible » à son comité d'investissement doit préciser laquelle des deux propositions il défend.

Reste la réserve la plus importante pour la thèse de ce chapitre. Il serait commode d'écrire qu'Entra Agent ID n'est que l'application de RFC existants à un nouveau type de sujet. Le socle l'interdit : les flux d'obtention de jeton pour le compte d'autrui (*on-behalf-of*) et de jeton d'agent (*agent token*) **étendent** les RFC — le dispositif ne doit pas être présenté comme du « pur RFC »[^1].

**Lecture de l'auteur** : le socle établit que ces flux étendent les RFC et interdit de présenter le dispositif comme du « pur RFC »[^1] ; il n'établit rien sur les conséquences de cette extension. La portée que l'auteur lui prête est la suivante — un mécanisme conforme à un RFC ratifié est vérifiable contre un texte public, tandis qu'un mécanisme qui étend un RFC est un mécanisme d'éditeur, dont la pérennité et l'interopérabilité engagent la responsabilité de cet éditeur. À ce compte, l'ancrage dans les standards existants que la thèse du présent chapitre affirme est réel mais partiel : il est un point de départ, non une garantie de portabilité.

## 8.2 La spécification CSA « Agent Registry » : le registre comme objet de gouvernance

La Cloud Security Alliance a publié le **27 mars 2026**, par l'entremise de CSA Labs, une spécification de registre d'agents (*agent registry*)[^2]. Son statut doit être énoncé à chaque mention : la spécification « Agent Registry » de la Cloud Security Alliance, à l'état de **brouillon** de CSA Labs au 16 juillet 2026 — travaux émergents, non une norme ratifiée[^5].

Ce brouillon décrit un cadre de registres d'agents d'entreprise faisant autorité, articulé autour de quatre fonctions : inventaire, découverte, cycle de vie et conformité[^2]. L'énumération mérite qu'on s'y arrête, car aucun de ces quatre termes n'appartient au vocabulaire de l'infrastructure : le socle documente ici un objet dont les fonctions déclarées sont des fonctions de gouvernance.

**Lecture de l'auteur** : le rapprochement entre ces quatre fonctions et les objets qu'un programme de gestion du risque de modèle manipule est une **inférence d'auteur**. Le socle établit les quatre fonctions du registre[^2] ; il ne les relie à aucune exigence réglementaire, et aucune de ses sources ne rattache la spécification CSA à un tel programme[^7]. Sous cette réserve, l'auteur lit le registre d'agents non comme un annuaire technique, mais comme un instrument de contrôle interne.

Le profil d'agent qu'il définit est ancré dans une extension de **SCIM 2.0** (*System for Cross-domain Identity Management*), c'est-à-dire dans le RFC 7643, complété par le brouillon IETF `draft-abbey-scim-agent-extension-00` porté par Okta[^2]. De ce profil, le socle documente deux champs obligatoires, qui portent l'essentiel de la valeur d'architecture : `toolAccessList`, liste explicite des outils et des serveurs MCP (*Model Context Protocol*) autorisés pour l'agent[^6], et `permissionBoundaries`, qui borne les privilèges de l'agent selon le principe du moindre privilège[^2].

Il faut peser ce que signifie rendre ces deux champs **obligatoires** dans un profil d'identité. Cela revient à poser que l'on ne peut pas enregistrer un agent sans déclarer, de façon explicite et lisible par machine, l'ensemble des outils qu'il peut atteindre et les bornes de ce qu'il peut faire. La déclaration cesse d'être une documentation d'accompagnement pour devenir une condition d'existence de l'agent dans l'annuaire.

**Lecture de l'auteur** : pour une institution qui devrait produire l'inventaire de ses systèmes autonomes et démontrer que chacun est borné, ces deux champs seraient directement exploitables. Le socle documente les champs et leur caractère obligatoire dans le profil[^2] ; il n'établit aucune obligation réglementaire d'inventaire — la question relève des chapitres 9 et 11.

**Lecture de l'auteur** : `permissionBoundaries` occupe, dans l'ordre de l'identité, la place que le chapitre 6 lit — comme lecture d'auteur, elle aussi — sous le *frame* opérationnel (*operational frame*) dans l'ordre du processus. La précaution n'est pas de style : le manifeste APM distingue ce frame du frame normatif sans le caractériser, et n'applique le terme à aucun objet de ce genre ; ce qu'il présente comme une frontière de sécurité, c'est l'opérationnalisation **locale** des frames, sans les qualifier d'opérationnels (voir ch. 6)[^8]. Le rapprochement est une lecture de l'auteur : aucune source du socle ne relie la spécification CSA aux travaux APM, et les deux objets relèvent de communautés distinctes. Ce que le socle établit, c'est la convergence des mécanismes, non celle des auteurs.

Une affirmation doit enfin être écartée : celle d'une identité SPIFFE obligatoire. Rien au socle n'établit que la spécification CSA — brouillon de labs[^5] — exigerait une telle identité : ni `agentId` sous forme d'URI SPIFFE, ni SVID. Elle **s'appuie sur** SPIFFE/SPIRE comme fondation ; l'exigence stricte **n'est pas établie**[^4]. L'écart entre ces deux formulations décide de la portée d'une décision d'architecture : un substrat d'identité sur lequel une spécification s'appuie laisse ouvert le choix de l'architecte, une exigence stricte le fermerait. Aucun dossier de conception ne devrait tenir la seconde lecture pour acquise.

## 8.3 La trajectoire IETF : un ancrage dont le point d'ancrage a expiré

L'ancrage SCIM du profil d'agent appelle un examen de son propre calendrier, et cet examen est instructif.

Le brouillon IETF `draft-abbey-scim-agent-extension-00` a **expiré le 19 avril 2026** ; une consolidation est en cours, rattachée aux travaux de l'IETF 125[^2]. La chronologie mérite d'être posée explicitement, parce qu'elle se lit mal de mémoire. La spécification CSA a été publiée le 27 mars 2026 ; le brouillon sur lequel son profil d'agent est ancré a expiré vingt-trois jours plus tard, le 19 avril 2026. À la date de gel du présent chapitre, le 16 juillet 2026, il s'est écoulé près de trois mois depuis cette expiration, et un peu moins de quatre mois depuis la publication de la spécification elle-même.

Il ne faut ni dramatiser ni minimiser ce constat. Le socle documente une consolidation en cours[^2] : l'expiration d'un brouillon individuel n'est pas l'abandon d'un travail, et rien dans le socle n'autorise à écrire que la trajectoire SCIM pour les agents serait compromise. Mais rien n'autorise davantage à écrire qu'elle serait acquise. Ces travaux sont émergents et doivent être cités comme tels, jamais comme des normes[^5].

La conséquence pratique est double. Un architecte peut légitimement retenir aujourd'hui les deux champs obligatoires du profil CSA comme mécanismes de conception — ils sont documentés, précis et immédiatement transposables. Il ne peut pas, en revanche, engager son institution sur leur stabilité syntaxique : un brouillon en consolidation est un texte dont les identifiants de champ peuvent changer. La lecture prudente consiste donc à emprunter à ce brouillon sa *structure* — la déclaration explicite des outils atteignables et des bornes de privilège — sans traiter sa *forme* comme un contrat d'interopérabilité. C'est une lecture de l'auteur, et elle ne vaut que jusqu'à la prochaine revalidation.

Le résultat mérite d'être formulé sans détour, car il nuance la thèse du chapitre autant qu'il la confirme. L'ancrage du registre d'agents dans les standards existants est double, et ses deux moitiés n'ont pas le même statut. La moitié inférieure — SCIM 2.0, RFC 7643 — est un standard ratifié, stable et public. La moitié supérieure — l'extension qui décrit ce qu'est un agent — est un brouillon individuel expiré, repris par une spécification qui est elle-même un brouillon de labs. L'édifice repose sur du solide ; ce qui, dans cet édifice, décrit spécifiquement les agents ne l'est pas encore.

## 8.4 Ce qui n'existe pas encore

Un chapitre sur l'identité des agents rendrait un mauvais service à son lecteur s'il ne consacrait pas une section à ce que le socle ne porte pas. Deux affirmations, en particulier, sont assez plausibles pour qu'un dossier d'architecture les reprenne sans les vérifier — les passes de vérification du socle les ont l'une et l'autre écartées.

> **Affirmations écartées — garde-fous R-2 et R-3**
>
> **(1) Un registre d'agents centralisé administré dans Entra.** Entra Agent ID comporterait un registre d'agents centralisé, administré depuis le centre d'administration Entra : les passes de vérification du socle (PRD §8.1) n'ont pas confirmé cette affirmation. Elle est **non vérifiée**, et le présent ouvrage s'en tient à ce que la documentation de l'éditeur établit — des identités d'agents et des *blueprints*[^3]. La question reste ouverte ; le vocabulaire de ce chapitre est réglé sur cette réserve, et aucune inférence n'est proposée ici.
>
> **(2) Une identité SPIFFE obligatoire dans la spécification CSA.** La spécification — brouillon de labs au 16 juillet 2026[^5] — s'appuie sur SPIFFE/SPIRE comme fondation ; l'exigence stricte d'un `agentId` en URI SPIFFE ou d'un SVID **n'est pas établie**[^4]. En l'absence de source primaire l'attestant, la question reste ouverte ; aucune inférence n'est proposée ici.
>
> Ces deux points ne figurent pas parmi les lacunes recensées au PRD §10 ; ils relèvent des garde-fous R-2 et R-3, et sont exposés ici au titre de la section que la table des matières assigne au chapitre.

À ces deux réserves nommées s'en ajoute une troisième, plus structurelle. Le socle ne documente **aucune norme ratifiée de registre d'agents**, à quelque niveau que ce soit. Ce qu'il documente, c'est un produit d'éditeur en disponibilité générale mais dont les flux étendent les RFC[^1], une spécification sectorielle à l'état de brouillon[^2], et une extension IETF expirée en cours de consolidation[^2]. Un architecte qui chercherait aujourd'hui, pour son dossier de conformité, la norme d'identité et de registre des agents ne la trouverait pas : elle n'existe pas.

Cette absence n'est pas une raison d'attendre — c'est même l'inverse. La ligne directrice E-23 du BSIF et la ligne directrice sur l'intelligence artificielle de l'AMF entrent l'une et l'autre en vigueur le **1er mai 2027**[^7], soit un peu plus de neuf mois après la date de gel du présent chapitre. C'est la raison pour laquelle la thèse de ce chapitre porte sur le registre *gouverné* et non sur le registre *normalisé* : ce que ces deux textes demandent effectivement relève des chapitres 9 et 11, seuls fondés à l'établir, et le socle ne les relie ni à Entra Agent ID ni à la spécification CSA[^7].

**Lecture de l'auteur** : le socle documente une consolidation en cours, sans calendrier[^2]. L'auteur n'anticipe pas de norme de registre d'agents ratifiée d'ici le 1er mai 2027, mais le socle ne permet ni de l'affirmer ni de l'exclure. La fonction précède ici la norme — c'est un constat sur l'état des travaux à la date de gel, non une prévision que le socle autoriserait.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, l'identité d'agent est sortie du domaine expérimental : elle est disponible en disponibilité générale chez un éditeur majeur depuis le printemps 2026, adossée à OAuth 2.0 et à OpenID Connect[^1]. **Deuxièmement**, le registre d'agents a trouvé sa forme conceptuelle — inventaire, découverte, cycle de vie, conformité — et deux mécanismes concrets, `toolAccessList` et `permissionBoundaries`, obligatoires dans le profil que la spécification CSA propose[^2]. **Troisièmement**, aucun de ces deux acquis n'est une norme : l'un étend les RFC sur lesquels il repose[^1], l'autre est un brouillon ancré sur un brouillon expiré[^2][^5].

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas qu'Entra Agent ID comporte un registre centralisé — cette affirmation n'est pas vérifiée[^3]. Il ne dit pas que la spécification CSA — brouillon de labs[^5] — exigerait une identité SPIFFE : elle s'appuie sur SPIFFE/SPIRE, et l'exigence stricte n'est pas établie[^4]. Il ne dit pas que ces mécanismes suffisent à satisfaire une exigence réglementaire canadienne : aucune source du socle ne relie l'un ou l'autre à E-23 ou à la ligne directrice de l'AMF, et la Partie III est seule fondée à établir ce que ces textes demandent. Il ne dit rien, enfin, de la sécurité des interactions que ces identités autorisent : borner ce qu'un agent *peut* atteindre ne préjuge en rien de la robustesse des outils qu'il atteint, dont le chapitre 4 traite.

La thèse tient, à une nuance près qu'il faut assumer : l'identité des agents s'ancre bien dans les standards existants, mais par des extensions qui n'en sont pas encore. C'est le registre d'agents *gouverné*, et non la normalisation de sa description, que ce chapitre retient comme pièce maîtresse — ce que la conformité exigera au 1er mai 2027[^7] relevant des chapitres 9 et 11.

---

## Notes

[^1]: PRD §7.2, **F-07** (niveau [A]). Source primaire : Microsoft Learn, documentation Entra Agent ID (mise à jour de juin 2026). **Réserves F-07** : des sous-fonctionnalités demeurent en préversion ; les fonctions de sécurité étendues relèvent de licences additionnelles (Entra ID P1/P2, Microsoft 365 E5, Agent 365) ; les flux *on-behalf-of* et de jeton d'agent **étendent** les RFC — le dispositif ne doit pas être présenté comme du « pur RFC ». La date de disponibilité générale est donnée par le socle comme approximative (~avril-mai 2026) et n'est reprise ici qu'à ce degré de précision.

[^2]: PRD §7.2, **F-08** (niveau [A] — statut de la spécification : **BROUILLON**). Sources primaires : labs.cloudsecurityalliance.org (spécification « Agent Registry », 27 mars 2026) ; datatracker.ietf.org (`draft-abbey-scim-agent-extension-00`, Okta, expiré le 19 avril 2026 ; consolidation en cours, IETF 125). **Réserves F-08** : brouillon de labs, non une norme ratifiée. Ancrage SCIM 2.0 : RFC 7643.

[^3]: PRD §8.1, garde-fou **R-2**. Affirmation non vérifiée : « Entra Agent ID inclut un registre d'agents centralisé administré via le centre d'administration Entra ». Forme imposée : parler d'identités et de *blueprints*, jamais de « registre centralisé ». Forme du glossaire : `monographie/90-annexes/annexe-d-glossaire.md` §D.4.

[^4]: PRD §8.1, garde-fou **R-3**. Affirmation non établie : « la spécification CSA impose une identité SPIFFE obligatoire (`agentId` en URI SPIFFE, SVID) ». Réalité à écrire : la spécification **s'appuie sur** SPIFFE/SPIRE comme fondation ; l'exigence stricte n'est pas établie.

[^5]: PRD §8.2.5 (statuts pré-normatifs) ; formulation imposée par PRDPlan §4.4 (« statut pré-normatif ») : spécification CSA = brouillon de labs ; brouillon IETF SCIM-agents expiré, consolidation en cours — travaux émergents, jamais des normes.

[^6]: PRD §7.1, **F-01** (niveau [A]) — renvoi. Serveurs MCP (*Model Context Protocol*) : interface client-serveur JSON-RPC 2.0 pour l'invocation d'outils, assortie d'un cadre d'autorisation fondé sur OAuth. **Réserve F-01** : dire « cadre d'autorisation », jamais « sécurisé » (voir ch. 2 et ch. 4).

[^7]: PRD §7.3, **F-09** (**[A/B mixte]** — l'entrée porte deux strates de preuve, et **seul un fait de strate [A] est mobilisé ici** : la date d'entrée en vigueur ; le marquage individuel d'une entrée prime la phrase de portée générale du chapeau de §7) et **F-25** (**[A]**) — renvois. Sources primaires : osfi-bsif.gc.ca (ligne directrice E-23, version finale du 11 septembre 2025, en vigueur le 1er mai 2027) ; lautorite.qc.ca (ligne directrice sur l'IA, finale depuis le 30 mars 2026, en vigueur le 1er mai 2027). Ces deux entrées ne sont mobilisées ici que pour **la date d'entrée en vigueur commune**. Que le socle ne relie ni Entra Agent ID ni la spécification CSA à ces textes est une **absence de documentation dans le corpus de cet ouvrage**, non un fait négatif vérifié : F-09 et F-25 ne se prononcent pas sur ces objets (PRDPlan §4.4, « trois degrés d'absence » — c'est ici le troisième, le socle muet ; le premier degré suppose un balayage de texte documenté, le deuxième une réserve explicite d'absence de lien). Leur **contenu** et leur **portée** relèvent des chapitres 9 et 11 : le présent chapitre n'énonce aucune exigence qu'ils poseraient. Rappel §8.2.4 : la couverture agentique d'E-23 est une **inférence d'analystes juridiques** — jamais « le BSIF exige pour l'IA agentique ». **Réserve F-25** : ne jamais écrire « en attente » ni « en projet ».

[^8]: PRD §7.7, **F-36** (niveau [B]) — renvoi. Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al., « Agentic Business Process Management: A Research Manifesto », *Information Systems* 140, 102738 (2026) / arXiv:2603.18916. Le manifeste présente l'opérationnalisation **locale** des *frames* comme une frontière de sécurité et de confidentialité. Le rapprochement avec `permissionBoundaries` est une **inférence d'auteur** : aucune source du socle ne relie la spécification CSA aux travaux APM. Développement : ch. 6.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; ~2 530 mots de corps après relecture — premier jet
                                   2 367-2 400 selon compteur, + 166 mots nets de correctifs ; cible 2 400 ±10 %
                                   = 2 160-2 640 : dans la tolérance, aucun resserrement requis. Remesuré au
                                   17 juillet 2026 après la passe de conformité (point 6 ci-dessous, + 39 mots) :
                                   **2 638 mots** par la commande de décompte publiée au bloc du ch. 6 — dans la
                                   tolérance, à 2 mots du plafond. Toute reprise ultérieure de ce chapitre devra
                                   resserrer avant d'ajouter.)
     2. Traçabilité (CA-1, CA-5) . fait (8 notes ; renvois F-01/F-09/F-25/F-36 marqués comme tels en note ;
                                   termes anglais entre parenthèses et en italique à la 1re occurrence :
                                   general availability, agent identity, blueprints, agent registry, SCIM, MCP,
                                   on-behalf-of, agent token, operational frame [ajouté en relecture — CA-5])
     3. Balayage garde-fous ...... fait (motifs PRDPlan §4.3 : « registre centralisé|Entra.*registre » -> R-2 traité
                                   en encadré §8.4 et en conclusion ; « SPIFFE|SVID » -> R-3, formule « s'appuie sur »
                                   partout — le verbe « imposer » est désormais absent du chapitre, y compris nié ;
                                   « CSA|SCIM|IETF » -> §8.2.5, statut pré-normatif énoncé à chaque mention, y compris
                                   dans l'encadré §8.4 (2) et en conclusion (ajouté en relecture) ; « sécuris » ->
                                   réserve F-01 respectée (note 6) ; « E-23 » -> §8.2.4 : aucune couverture agentique
                                   affirmée, et — après relecture — aucune exigence de contenu non plus ; seule la date
                                   d'entrée en vigueur est reprise (note 7), le contenu étant renvoyé aux ch. 9 et 11 ;
                                   R-8 : aucune occurrence de « ACP » ni de « control plane » dans le chapitre)
     4. Relecture adversariale ... fait (deux relecteurs indépendants, 16 juillet 2026 : 5 constats bloquants et
                                   16 réserves — tous fondés, tous appliqués. Ce que la relecture a réfuté :
                                   a) §8.4 posait DEUX exigences réglementaires comme des faits (« les institutions
                                      devront néanmoins produire leurs inventaires » ; « ce que les régulateurs
                                      canadiens exigeront [...] porte sur la maîtrise démontrable des systèmes »),
                                      sans note ni marquage, en s'autorisant d'une Partie III non rédigée
                                      (« la Partie III l'établit ») — alors que le socle ne porte que la DATE (F-09,
                                      F-25) et que la couverture agentique d'E-23 n'est qu'une inférence d'analystes.
                                      Le chapitre se contredisait deux fois (§8.1 « il n'est pas anticipé ici » ;
                                      conclusion « la Partie III est seule fondée »). Corrigé : contenu renvoyé aux
                                      ch. 9 et 11 ; obligation d'inventaire supprimée partout.
                                   b) §8.2 rapprochait les quatre fonctions du registre et le programme de gestion du
                                      risque de modèle SANS marquage — or PRD Annexe B.3 range ce même rapprochement
                                      en « Inférence d'auteur ». Corrigé : intertitre « Lecture de l'auteur », forme
                                      PRDPlan §4.4 (cas général — sans « ne revendique aucune conformité », réservé
                                      au fait négatif établi E-23/B-13).
                                   c) §8.2 écrivait « la spécification CSA n'IMPOSE pas d'identité SPIFFE — pas de
                                      SVID exigé » : conversion d'une absence de preuve en preuve d'absence, contraire
                                      à R-3 (« l'exigence stricte n'est pas établie ») et au §4.3 (« jamais impose »).
                                      Le chapitre se contredisait 20 lignes plus loin (encadré §8.4 (2), correct).
                                      Corrigé : « rien au socle n'établit que... » + « n'est pas établie ».
                                   d) Le présent commentaire d'auto-contrôle CERTIFIAIT À TORT (lignes « E-23 » et
                                      « impose ») ce que le corps du texte violait — les deux lignes sont rectifiées
                                      ci-dessus. Leçon : un auto-contrôle qui se contente de répéter la règle ne
                                      vaut rien ; il doit citer le passage qui la satisfait.
                                   e) Réserves appliquées : citation verbatim du TOC rétablie (« le registre D'AGENTS
                                      gouverné », en-tête et conclusion) ; définition inventée des « blueprints »
                                      supprimée ; surlecture des licences Entra ramenée aux termes de F-07 ;
                                      exhaustivité inventée des champs du profil CSA (« Deux champs [...] sont
                                      obligatoires ») ouverte ; faits sociologiques sans source (« il est fréquemment
                                      avancé », « circulent avec assez d'assurance ») rattachés aux passes de
                                      vérification ; comparatif orphelin « des deux » supprimé ; raisonnement RFC de
                                      §8.1 marqué « Lecture de l'auteur » ; « operational frame » glosé (CA-5) ;
                                      encadré §8.4 RENOMMÉ « Affirmations écartées — garde-fous R-2 et R-3 » : il
                                      empruntait le titre « État de la connaissance vérifiable » réservé par §4.4 aux
                                      lacunes §10 sans en porter la substance (le chapitre admettait lui-même que ces
                                      deux points ne sont pas des lacunes §10) ; « la question reste ouverte » ajouté
                                      au point (1).
                                   Aucun constat écarté.)
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     6. Passe de conformité ...... fait (17 juillet 2026 — audit global, constats m-13 et m-14 ; date de gel
                                   INCHANGÉE au 16 juillet 2026 : aucune information nouvelle n'entre.
                                   m-13 (§8.2) : « ce que le manifeste APM APPELLE un frame opérationnel »
                                       prêtait au manifeste un geste qu'il ne fait pas. F-36 (apport 4) porte
                                       l'opérationnalisation locale DES FRAMES, sans les qualifier
                                       d'opérationnels ; le frame opérationnel n'est pas caractérisé au socle
                                       (PRD §10.10a : « seul le frame normatif est caractérisé »), et le ch. 6
                                       tient cette discipline strictement — il marque sa propre glose
                                       devoir-être/pouvoir-faire « Lecture de l'auteur ». Le rapprochement reste
                                       licite comme lecture d'auteur : c'est le VERBE qui fautait. Reformulé —
                                       le chapitre ne fait plus nommer le manifeste, il adosse sa lecture à
                                       celle, marquée, du ch. 6, et dit ce que le manifeste ne fait pas. La note
                                       [^8] était fidèle : intacte.
                                   m-14 (note [^7]) : deux défauts distincts, tous deux fondés.
                                       (a) « F-09 et F-25 (niveau [A]) » à plat — F-09 est [A/B mixte] au
                                       PRD §7.3 et « le marquage individuel prime toujours » (chapeau §7). Le
                                       contenu mobilisé (date d'entrée en vigueur) relève bien de la strate [A] :
                                       pas de faute de fond, mais l'étiquette globale reproduisait exactement le
                                       piège que le PRD documente nommément (ch. 18, 16 juill. 2026). Étiquette
                                       rectifiée, strate mobilisée dite.
                                       (b) « le fait négatif qu'elles portent » pour la non-liaison à Entra/CSA —
                                       c'est une ABSENCE DE DOCUMENTATION : F-09 et F-25 ne se prononcent pas sur
                                       ces objets. Formule de distinction de PRDPlan §4.4 employée, et le degré
                                       nommé (ligne « Trois degrés d'absence », tranchée le 17 juill. 2026 :
                                       vérifié > établi > absence de documentation — ce cas est le troisième).
                                       F-09 porte bien un fait négatif VÉRIFIÉ, mais sur le texte d'E-23
                                       (« agentique »/« agent »/« orchestration » = 0), jamais sur Entra ni CSA :
                                       c'est la confusion que la note induisait. Le corps (l. 79, 87) était
                                       correct : non touché.)

     Arithmétique posée (règle : aucun calcul sans ses termes) :
     - 27 mars 2026 -> 19 avril 2026 = 4 j (fin mars) + 19 j = 23 jours (§8.3)
     - 19 avril 2026 -> 16 juillet 2026 = 2 mois 27 j -> « près de trois mois » (§8.3)
     - 27 mars 2026 -> 16 juillet 2026 = 3 mois 19 j -> « un peu moins de quatre mois » (§8.3)
     - 16 juillet 2026 -> 1er mai 2027 = 9 mois 15 j -> « un peu plus de neuf mois » (§8.4)

     Point de revalidation (P4.1) : consolidation IETF 125 du brouillon SCIM-agents (F-08) et statut de la
     spécification CSA (brouillon au 16 juillet 2026) — postérieurs à la date de gel, à re-vérifier.
-->
