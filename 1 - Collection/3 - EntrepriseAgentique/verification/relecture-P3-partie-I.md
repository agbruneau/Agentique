# Relecture adversariale — Partie I (ch. 1 à 4), premier jet

| Champ | Valeur |
|---|---|
| Objet | Les **quatre pièces de la Partie I**, rédigées le 21 juillet 2026 contre le socle (PRD v1.0) |
| Relecteurs | **Quatre, un par pièce, distincts des rédacteurs** (CA-14), chargés de **réfuter trois à cinq affirmations contre le socle** — boucle qualité PRDPlan §5.2, point 5 |
| Verdict | ⚠ **`A_CORRIGER` sur les quatre pièces, sans exception.** **14 réfutations bloquantes**, 13 majeures, 4 mineures |
| État des correctifs | ⚠ **NON APPLIQUÉS.** Le point 6 de la boucle qualité — appliquer les correctifs, et **amender le socle d'abord si la faute y siège** — n'a pas été exécuté. Les quatre pièces restent au statut **« Rédigé (premier jet) »** |

⚠ **Ce document est la trace d'un contrôle, pas un certificat de conformité.** Les quatre chapitres sont dans le dépôt avec leurs défauts, et ce fichier dit lesquels. *Un statut qui ment est pire qu'un statut absent.*

---

## Le défaut dominant, et il est le même aux quatre pièces

**La borne perdue.** Le socle porte des faits bornés — une section nommée, une langue, une date de consultation, une révision — et la prose du chapitre généralise. C'est la faute que chaque relecture de ce projet a attrapée, à chaque phase, sans exception : au socle en P1, dans les synthèses en P2, dans la prose d'ouvrage en P3. *Elle ne se corrige pas une fois : elle se surveille à chaque niveau d'écriture.*

Second défaut, propre à la rédaction : le **niveau forcé**. Une entrée [B] ou [C] citée comme si elle était établie, ou une entrée agrégée dont on retient la partie la plus forte. Le ch. 4 en porte le cas le plus net — le seul verdict « répond » de sa grille repose sur une entrée [B] qui ne documente pas les deux termes exigés par la question.

---

## Chapitre 1 — A_CORRIGER

**Entrées citées** : `F-16`, `F-19`, `F-20`, `F-21`, `F-27`, `F-28`, `F-29`, `F-36`, `H-03`, `H-04`, `H-07`.

### BLOQUANT — « Chez AWS, l'identité d'agent n'est **pas un type d'objet propre** mais une identité de charge de travail (F-

> « Chez AWS, l'identité d'agent n'est **pas un type d'objet propre** mais une identité de charge de travail (F-36). » (§1.1, « Où cette généalogie aboutit en production »)

**Constat.** Niveau forcé + borne perdue, sur trois plans. (1) F-36 agrège `L04-A7` [B], `L04-A8` [B] et `L04-A9` **[C]** — l'énoncé AWS est `L04-A9`, verifié au niveau **[C]** (verification/lot-L-04-annuaires-commerciaux.md, ligne 27 et §F). CA-01 : « Une affirmation tracée vers une entrée [C] n'est pas centrale, ou n'est pas rédigée. » (2) Le contrôle de bornage du lot a corrigé `L04-A9` **deux fois** — « négatif de corpus » et « clause d'exclusivité » — et la formulation retenue **nomme le produit** : « Chez AWS, un mécanisme documenté comparable est Amazon Bedrock AgentCore Identity — la formulation ne revendique ni unicité au sein de l'offre AWS, ni équivalence fonctionnelle ». Le chapitre supprime le nom du produit et rétablit l'universel sur toute l'offre AWS : exactement la clause d'exclusivité que le bornage avait retirée. (3) Le lot déclare en §E : « aucune source primaire datant le statut d'AgentCore Identity n'a pu être ouverte […] L04-A9 décrit donc le mécanisme, jamais son statut » — or la phrase suivante du chapitre fait précisément du tri des statuts son propos (« Annonce, feuille de route, préversion et disponibilité générale documentée sont quatre choses différentes »). Le passage qui pose la discipline de statut est celui qui l'enfreint.

**Correctif.** Rétablir le produit, le niveau et le trou de statut : « Chez AWS, le mécanisme documenté comparable est **Amazon Bedrock AgentCore Identity**, où l'identité d'agent est une identité de charge de travail (*workload identity*) dotée d'attributs propres plutôt qu'un type d'objet distinct (F-36, composante `L04-A9`, **[C]** — repérage, non fait central). ⚠ **Le statut de cette offre n'est pas établi** : le lot L-04 n'a pu ouvrir aucune source primaire le datant ; annonce, préversion et disponibilité générale n'y sont pas départagées. » Remontée à déposer en parallèle : **F-36 est publiée [B] alors que la règle de composition de PRD §7.9 lui impose le niveau le plus faible de ses composantes, soit [C]** — le socle est à amender, pas le chapitre à ajuster seul.

### BLOQUANT — « La pièce la plus ancienne qu'il porte est le RFC 6749, d'octobre 2012 (F-27). » (§1.1, « Avertissement de po

> « La pièce la plus ancienne qu'il porte est le RFC 6749, d'octobre 2012 (F-27). » (§1.1, « Avertissement de portée »)

**Constat.** Superlatif portant sur le socle **entier** sans balayage documenté — la famille de fautes que le contrôle de bornage de P2 a corrigée quatorze fois (PRD §7.9, « 14 clauses d'exclusivité »). Et il est faux : **F-53 porte le RFC 5280 (mai 2008) et le RFC 6960 (juin 2013)**, tous deux antérieurs ou contemporains, sur un objet d'identité machine (révocation). Le chapitre se contredit en outre lui-même deux paragraphes plus bas en citant le **RFC 3986 (janvier 2005)** dans la définition SPIFFE-ID. L'énoncé n'est pas décoratif : c'est lui qui justifie l'écart entre le titre (« un demi-siècle ») et la période réellement couverte, donc l'avertissement de portée repose sur un fait non vérifié.

**Correctif.** Remplacer le superlatif de corpus par le fait positif, borné : « La généalogie que le socle documente s'ouvre au RFC 6749, d'octobre 2012 (F-27) ; aucune entrée ne documente les comptes de service, les clés d'API ni les secrets d'atelier logiciel. » Si un superlatif est voulu, il doit porter sa borne et son balayage (« la plus ancienne pièce du socle **relative à la généalogie des identités machines** », après balayage effectif des 78 entrées de §7.8-§7.9).

### BLOQUANT — En-tête de colonne du tableau §1.2 : « **Ce que le socle porte** », dont la troisième ligne est « Un SVID est 

> En-tête de colonne du tableau §1.2 : « **Ce que le socle porte** », dont la troisième ligne est « Un SVID est tenu pour valide dès lors qu'il est signé par une autorité de son domaine de confiance (`L01-A8`) » ; et §1.3 : « **Ce que le socle établit** : la spécification SPIFFE-ID nomme un écart entre émission et usage, portant sur des assertions (`L01-A8`) ».

**Constat.** Affirmation tracée à faux. PRD §7.9 est explicite sur les affirmations de lot non versées : « les autres restent au rapport de leur lot, consultables, mais **ne sont pas au socle et ne peuvent donc pas être citées comme telles** ». Le chapitre les cite précisément comme telles — sous un en-tête « ce que le socle porte » et dans la clause « ce que le socle établit » du marquage CA-07, c'est-à-dire aux deux endroits où le lecteur est censé lire une garantie de socle. L'en-tête de pièce reconnaît pourtant le statut (« retenues par le lot mais non versées au socle ») : la contradiction est interne. Accessoirement, « tenu pour valide **dès lors qu'il est** signé » réintroduit la suffisance exclusive (« par le seul fait que ») que le contrôle de bornage du lot avait retirée de `L01-A8`.

**Correctif.** Ne pas laisser un identifiant de lot occuper la place d'une entrée de socle. Deux voies, l'une ou l'autre, jamais le silence : (a) attendre le versement demandé en note et rédiger contre le F-xx obtenu ; (b) renommer l'en-tête « **Ce que la pièce mobilise, et à quel titre** » et écrire, dans la cellule, « source primaire ouverte et citée hors socle — rapport L-01, `L01-A8` [B] ; **non versée au socle** ». Dans le bloc « Lecture de l'auteur », remplacer « Ce que le socle établit » par « Ce qui est établi par source primaire, hors socle ». Et rétablir la formulation bornée : « un SVID est considéré valide **s'il a été signé** par une autorité de son domaine de confiance ».

### BLOQUANT — « **Ce que cette spécification démontre est une vérification de signature dans un domaine de confiance ; elle 

> « **Ce que cette spécification démontre est une vérification de signature dans un domaine de confiance ; elle ne documente ni une preuve de propriété d'une entité, ni une décision d'autorisation** (R-02 du présent volume). » (§1.1)

**Constat.** R-14 et PRD §8.6 : absence de documentation présentée comme fait négatif. La source même de la phrase — la réserve de `L01-A8` — qualifie explicitement cette absence : « le document […] n'énonce pas explicitement ce que la vérification d'un SVID n'établit pas — **cette dernière absence est de degré 3 (rien trouvé), pas un fait négatif** ». Le chapitre marque le degré partout ailleurs (F-28 « degré 1 », deux « degré 3 » énoncés en toutes lettres en §1.1 et §1.2) et l'omet exactement là où repose l'application de R-02 — c'est-à-dire là où l'omission coûte le plus, puisque cette phrase est déclarée en note comme la seule affirmation centrale hors socle du chapitre.

**Correctif.** Scinder l'énoncé positif de l'absence, et qualifier l'absence : « **Ce que cette spécification démontre est une vérification de signature dans un domaine de confiance** (R-02 du présent volume). **Elle n'énonce pas ce que cette vérification n'établit pas** — ni preuve de propriété d'une entité, ni décision d'autorisation : c'est une **absence de documentation dans le corpus de cet ouvrage, non un fait négatif vérifié** (PRD §8.6, degré 3). » Reporter la même qualification à la note « Verbe rétabli sur R-02 », qui rejoue l'énoncé sans son degré.

### MAJEUR — « Conformément au traitement défensif exclusif du volume (R-12 du présent volume), la mécanique est exposée au

> « Conformément au traitement défensif exclusif du volume (R-12 du présent volume), la mécanique est exposée au niveau du maillon ; **aucune séquence, aucune charge utile, aucune preuve de concept n'est reproduite ici**, et l'exploitation de ce vecteur ne se dérive pas du présent texte. » (§1.2)

**Constat.** CA-12, dernière ligne : « ⚠ **Une attestation “aucune procédure n'y figure” rédigée par le rédacteur lui-même n'est pas un contrôle** : c'est la faute constatée le 21 juillet 2026, où une telle attestation était fausse sur trois passages. » Le chapitre écrit exactement cette attestation, dans le corps de la pièce, sous la signature du rédacteur. CA-12 exige un contrôle « par relecture dédiée, distincte de la relecture de conformité et confiée à un relecteur distinct du rédacteur », dont « le compte rendu est déposé sous `verification/` et nommé dans la pièce qu'il couvre ». Aucun compte rendu de ce type n'est nommé par la pièce.

**Correctif.** Garder la règle, retirer l'attestation : « Conformément au traitement défensif exclusif du volume (R-12 du présent volume), la mécanique est exposée au niveau du maillon — quel élément de la chaîne d'identité cède, et pourquoi. » Puis, en Notes, renvoyer au contrôle réel plutôt que de l'affirmer : « **Contrôle CA-12** : relecture dédiée par un relecteur distinct du rédacteur, compte rendu déposé sous `verification/<nom>.md` » — la ligne ne s'écrit qu'une fois le compte rendu déposé.

### MAJEUR — « Le référentiel qui traite **le plus explicitement** cet écart le formule comme un déplacement de fonction. »

> « Le référentiel qui traite **le plus explicitement** cet écart le formule comme un déplacement de fonction. » (§1.2)

**Constat.** Clause de superlatif comparatif : elle présuppose un classement sur un corpus de référentiels que rien n'a balayé. F-16 et F-20 établissent le contenu et le statut de deux documents ; aucune entrée du socle ne compare des référentiels entre eux, et le lot L-08 ne revendique aucun balayage comparatif. Même famille que les quatorze clauses d'exclusivité corrigées en P2 (PRD §7.9) et que les trois formulations écartées au vote de L-08 (« la seule technique visant spécifiquement A2A »).

**Correctif.** Écrire le fait sans le rang : « Deux pièces du socle formulent cet écart comme un déplacement de fonction. » (puis F-19 et F-20 comme actuellement). Si le rang importe, il exige son balayage et sa borne — sinon il ne s'écrit pas.

### MAJEUR — « **2026 — la mise en RFC est en cours, et elle range l'agent parmi les charges de travail déléguées.** » (§1.

> « **2026 — la mise en RFC est en cours, et elle range l'agent parmi les charges de travail déléguées.** » (§1.1, intertitre gras)

**Constat.** Énoncé prospectif sans tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF (CA-11 : « Tout énoncé prospectif porte son tri »), et il excède sa source. La réserve de `L01-A6` est formelle : « **Aucune date de publication en RFC n'est annoncée pour aucun des sept.** » Le corps du paragraphe est exact — sept brouillons, un seul « Submitted to IESG » — mais l'intertitre généralise ce cas unique en un mouvement d'ensemble (« la mise en RFC est **en cours** »), et l'intertitre est ce que la lecture rapide retient. H-18 [C], seule entrée qui porte l'agenda WIMSE, le classe pour sa part « PROGRAMMÉ **mais sans date d'engagement ferme** ».

**Correctif.** Ramener l'intertitre au relevé et lui donner son tri : « **2026 — un seul des sept documents du groupe est soumis à l'IESG, et l'architecture range l'agent parmi les charges de travail déléguées.** » Ajouter en fin de paragraphe : « ⚠ **PROGRAMMÉ sans date d'engagement** (CA-11) : aucune date de publication en RFC n'est annoncée pour aucun des sept documents relevés. »

### MINEUR — « *Homonymie* : l'expression « plan de contrôle » recouvre dans ce volume **six emplois distincts**, désambigu

> « *Homonymie* : l'expression « plan de contrôle » recouvre dans ce volume **six emplois distincts**, désambiguïsés au ch. 22 §22.1 (R-04 du présent volume) ». (§1.2)

**Constat.** R-04 recense bien six branches, mais ce ne sont pas six emplois de « plan de contrôle » : (a) et (d) portent le sigle **« ACP »**, et (f) porte **« AgentMesh »** (équipes plateforme, cadrage du Vol. IV, §7.4.6). Attribuer les six à la seule expression « plan de contrôle » surcompte l'homonymie et, ce faisant, rend la réserve moins opposable qu'elle ne l'est : le lecteur qui ira au ch. 22 §22.1 n'y trouvera pas six sens de la même expression.

**Correctif.** « *Homonymie* : l'expression relève du garde-fou d'homonymie du volume, qui recense **six branches** — dont le sigle « ACP », le plan de contrôle au sens infrastructure et « AgentMesh » —, désambiguïsées au ch. 22 §22.1 (R-04 du présent volume) ; le socle ne caractérise pas laquelle le rapport vise, et la formule est donc laissée en langue originale. »

### Ce que le relecteur a tenté de réfuter sans y parvenir

Ce que j'ai tenté de réfuter sans y parvenir, point par point, sources ouvertes.\n\n**1. La borne de F-28, cible évidente — elle tient trois fois.** J'ai cherché la généralisation « SCIM ne prévoit pas l'agent ». Le chapitre écrit « la §4 du RFC 7643 », nomme le RFC et la section, rappelle la borne dans le corps (« le balayage porte sur l'énumération des sous-sections de la §4 de ce seul RFC ; il ne dit rien du RFC 7644, rien des extensions de schéma enregistrées ailleurs, rien des profils propriétaires »), la répète dans la cellule du tableau §1.2 (« degré 1, borné aux sous-sections de cette §4 ») et une troisième fois en Notes. Le libellé « au moins deux descriptions d'attributs » reprend exactement la reformulation du contrôle de bornage de `L01-A4` (qui avait retiré une clause d'exclusivité). Et la phrase « Constat de sémantique rédactionnelle, non d'interdiction normative » reproduit la réserve du lot mot pour mot.\n\n**2. H-04 et E-23.** J'ai recompté sur l'entrée : « agentique » = 0, « agent(s) » = 0, « orchestration » = 0, « autonom\\* » = 8, EN et FR, texte intégral — le chapitre reproduit les quatre chaînes et les quatre décomptes sans dérive. La modalité R-06 est tenue au bon endroit (« ce qu'elle formule est **attendu**, jamais exigé »), sans occurrence de « exige » ou « impose ». Les deux syntagmes anglais sont cités entre guillemets et glosés **hors** guillemets, ce que H-04 prescrit explicitement (« le socle ne verse aucun rendu français de ces syntagmes ») ; CA-05 et CA-08 sont respectés.\n\n**3. F-21, la campagne UNC6395.** Les trois dates (8 août, 18 août, 20 août 2025) sont exactes, et le « à au moins le 18 août » — la borne qui empêche de fermer la fenêtre — vient de F-21 lui-même. La restriction de R-08 est reprise dans les termes de la version amendée du 21 juillet 2026, jusqu'à la formule « et de cela seul ».\n\n**4. F-16.** J'ai vérifié le piège que F-16 signale : millésime 2026 et date de publication décembre 2025 sont bien cités **ensemble**, dans la même incise.\n\n**5. CA-10, renvois.** Les sept garde-fous cités portent tous « du présent volume » (R-02, R-03, R-04, R-06, R-08, R-09, R-12) ; le chapitre ne fait aucun renvoi au Vol. I (donc aucun renvoi sans fichier) et ne cite aucune question du Vol. II. Rien à reprendre.\n\n**6. Interdiction du fait central sur entrée [C].** J'ai passé les entrées héritées : le chapitre n'emploie que H-03 ([A, BROUILLON]), H-04 ([A/B mixte]) et H-07 ([B]). H-18 [C] portait l'agenda WIMSE et aurait été la source commode ; le chapitre est allé à la source primaire à la place. La seule contamination [C] passe par F-36 (refutation n° 1), et elle vient du socle, pas de la pièce.\n\n**7. §8.2.3 et l'absence de chiffres NHI.** J'ai balayé le PRD entier pour « ratio », « prolifération », « machines/humaines » : aucune entrée de §7.8 ni de §7.9 ne porte d'ordre de grandeur NHI. Le degré 3 annoncé en §1.2 est exact, et aucun énoncé du chapitre ne dépend d'un chiffre — la thèse tient sans ratio, ce que le garde-fou exigeait.\n\n**8. Marquage CA-07.** Les trois blocs « Lecture de l'auteur » portent le libellé en tête, en gras, suivi de « Ce que le socle établit » **et** de « Ce qu'il n'établit pas » — structure imposée par le quatrième corollaire de §7.0. Le contenu de la clause négative est à chaque fois vérifiable et vrai (aucune source du socle ne met en rapport durée de vie courte et inventaire, ni écart d'assertion et écart d'action).\n\n**9. La divergence CNCF.** J'ai cherché l'arbitrage silencieux entre le 22 et le 23 août 2022 : le chapitre reproduit les deux dates, nomme la page de chacune, signale le 404 du communiqué et déclare la divergence non arbitrée — conforme à la réserve de `L01-A9` et à la règle « signalées, jamais tranchées ».

---

## Chapitre 2 — A_CORRIGER

**Entrées citées** : `F-27`, `F-28`, `F-29`, `F-33`, `F-34`, `F-40`, `F-41`, `F-42`, `H-02`, `H-03`, `H-09`, `H-18`, `H-33`.

### BLOQUANT — « Transaction Tokens (Txn-Tokens) are designed to maintain and propagate user identity, workload identity and 

> « Transaction Tokens (Txn-Tokens) are designed to maintain and propagate user identity, workload identity and authorization context throughout the Call Chain within a trusted domain during the processing of external requests »

**Constat.** Citation présentée comme verbatim clos et qui ne l'est pas (CA-05). Le texte primaire relevé au lot L-01, sous la citation d'appui de `L01-A5` (verification/lot-L-01-identite-machine-rfc.md), se poursuit : « (e.g. such as API calls) **or requests initiated internally within the Trust Domain.** » La coupe tombe exactement sur la clause qui étend le périmètre du mécanisme aux requêtes initiées *à l'intérieur* du domaine de confiance — c'est-à-dire sur le cas qui intéresse le plus un chapitre traitant de la chaîne d'appels interne. Aucune marque d'élision. Second défaut, du même passage : ce que la citation sert à établir — l'objet des jetons de transaction — n'est porté par aucune entrée du socle. F-29 établit la révision, sa date, sa date d'expiration et son état de procédure, rien d'autre ; l'abrégé est une citation d'appui orpheline du rapport de lot (elle ne soutient aucun membre de `L01-A5`), et PRD §7.9 pose que ce qui reste au rapport « ne peut donc pas être cité comme tel ».

**Correctif.** Rétablir la fin de phrase, ou marquer l'élision : « … during the processing of external requests […] ». Et dissocier les deux appuis : F-29 pour le seul statut ; pour le contenu, soit verser l'abrégé au socle par amendement (§7.9 prévoit ce cas pour `L02-A4` et `L12-A8`), soit écrire « Son abrégé — relevé au lot L-01, non versé au socle — énonce l'objet : … ».

### MAJEUR — | `draft-abbey-scim-agent-extension` | **-00**, 16 octobre 2025 | expiré | *Expired Internet-Draft (individual

> | `draft-abbey-scim-agent-extension` | **-00**, 16 octobre 2025 | expiré | *Expired Internet-Draft (individual)* …

**Constat.** La date d'expiration existe au socle et le chapitre l'efface. H-03 : « le brouillon IETF a expiré le **19 avril 2026** » ; PRD §8.3 la redit (« brouillon SCIM-agents (expiré le 19 avril 2026) »). Or §8.2.6 impose « *Internet-Draft* (avec sa date d'expiration) — dits à chaque mention (R-09) », et l'en-tête du chapitre se l'impose à lui-même : « R-09 (statut pré-normatif : état **et date d'expiration réelle** de chaque *draft*) ». La colonne s'intitule « Expiration » et ne porte qu'un adjectif. Aggravant : le titre de section annonce « quatre statuts, **quatre dates** » alors que le corps n'en écrit que trois — la quatrième est refusée à MCP par prudence assumée (« Le chapitre n'écrit donc aucune date de publication pour cette révision »), et celle-ci est simplement perdue.

**Correctif.** Colonne Expiration : « **19 avril 2026** (H-03) ». Et retitrer §2.2 sur ce que la section tient réellement, p. ex. « quatre statuts, et ce que leurs dates disent ou ne disent pas ».

### MAJEUR — « un texte non ratifié s'adosse à un texte expiré » (§2.3) — repris en §2.4 : « une spécification de laboratoi

> « un texte non ratifié s'adosse à un texte expiré » (§2.3) — repris en §2.4 : « une spécification de laboratoire à l'état de brouillon s'adosse à une extension expirée »

**Constat.** Borne perdue, aux deux endroits exacts où le chapitre tire sa conclusion. H-03 borne expressément la chronologie : l'expiration du 19 avril 2026 tombe « soit **vingt-trois jours après** la publication de la spécification qui s'y adosse ». Au 27 mars 2026, le brouillon désigné était vivant. Ce que le socle établit est un **défaut d'entretien** — F-41 : « la spécification CSA **le cite toujours** dans cette version -00 » — non un adossement initial à un document mort. Les deux formules retenues, dépouillées de leurs dates, laissent lire le second, qui est le reproche le plus lourd et celui que le socle ne porte pas.

**Correctif.** « Une spécification de laboratoire publiée le 27 mars 2026 continue de citer, en juillet 2026, un brouillon expiré le 19 avril suivant — vingt-trois jours après sa propre publication (H-03, F-41). Ce n'est pas un adossement à un texte mort, c'est un adossement non entretenu. »

### MAJEUR — « Les **jetons de transaction** (*transaction tokens*) sont le plus avancé des trois. »

> « Les **jetons de transaction** (*transaction tokens*) sont le plus avancé des trois. »

**Constat.** Classement posé en constat, huit paragraphes avant son marquage. La « Lecture de l'auteur » qui clôt §2.2 déclare elle-même : « Il n'établit aucun ordre de solidité entre eux, ni aucune probabilité d'aboutissement. Le classement implicite qui suit […] est une construction d'auteur. » CA-07 et PRDPlan §5.5 imposent le marqueur « **en tête de l'énoncé** » ; ici il arrive après, et le chapitre a déjà écrit en clair l'énoncé que son propre marqueur désavoue. Un lecteur qui s'arrête au tableau lit « le plus avancé des trois » comme un fait de socle.

**Correctif.** Remplacer par le fait, et rien de plus : « Des trois documents du tableau, `draft-ietf-oauth-transaction-tokens` est le seul adopté par un groupe de travail (F-29). » Le jugement de solidité reste au marqueur, à sa place.

### MAJEUR — « > **État de la connaissance vérifiable — les jetons de transaction.** […] Recherche menée le 21 juillet 2026

> « > **État de la connaissance vérifiable — les jetons de transaction.** […] Recherche menée le 21 juillet 2026 sur les sources primaires : elle établit la révision, sa date, sa date d'expiration et son état de procédure (F-29). Elle ne clôt pas la lacune »

**Constat.** Gabarit forgé hors de la table imposée, sans y être versé. PRDPlan §5.5 n'en prévoit que trois : cas 1 « passe conduite et **infructueuse** » (« En l'absence de source primaire… »), cas 2 « lacune non instruite », cas 3 « source repérée, non extraite ». La lacune 14 relève d'un quatrième état, que PRD §10 nomme lui-même : **« instruite sans être close »** — passe conduite, résultat positif, lacune ouverte. L'encadré est donc une formulation nouvelle pour un cas non prévu, et §5.5 impose alors de « l'ajouter ici **au même commit** ». Rien n'a été ajouté à §5.5.

**Correctif.** Verser au tableau §5.5, dans le même commit, un « cas 4 — passe conduite et fructueuse, lacune non close » dont l'encadré actuel est la forme, puis y renvoyer. Six des quatorze lacunes sont dans cet état (PRD §10) : la forme resservira cinq fois.

### MINEUR — « un `toolAccessList`, qui énumère les outils et serveurs invocables »

> « un `toolAccessList`, qui énumère les outils et serveurs invocables »

**Constat.** Borne perdue sur F-40, qui écrit « le premier énumère les outils et serveurs **MCP** invocables » ; le verbatim du lot (`L05-A3`) est « explicit list of tools and MCP servers the agent is authorized to invoke ». Le champ ne porte pas des serveurs quelconques, et l'ancrage sur MCP est précisément ce qui rattache ce champ au reste du chapitre.

**Correctif.** « un `toolAccessList`, qui énumère les outils et les serveurs MCP que l'agent est autorisé à invoquer (F-40) ».

### MINEUR — | Socle mobilisé (PRD §7) | F-27, F-28, F-29, F-33, F-34, F-40, F-41, F-42 ; H-02, H-03, H-09, H-18 [C], H-33 

> | Socle mobilisé (PRD §7) | F-27, F-28, F-29, F-33, F-34, F-40, F-41, F-42 ; H-02, H-03, H-09, H-18 [C], H-33 |

**Constat.** CA-11 exige que « tout fait porte son niveau [A]/[B]/[C] ». Le chapitre ne porte le niveau que pour H-18, et pour la refuser. F-27 et F-28 — qui portent à eux deux la totalité des §2.1 et §2.3, soit la thèse du chapitre — sont **[B]**, et rien dans le texte ne le dit ; F-29 et F-34 sont [A], F-40, F-41, F-42, F-33 sont [B]. L'asymétrie est ce qui nuit : un lecteur qui voit « [C] » signalé une fois conclut que le reste est d'un niveau qu'on n'a pas besoin de nommer. (Constat non propre à cette pièce — `ch-01-identites-non-humaines.md` ne porte aucun niveau non plus —, ce qui en fait une dette de P4, pas une coquille.)

**Correctif.** Porter le niveau aux entrées centrales à leur première mobilisation : « (F-27, [B]) », « (F-28, [B, degré 1]) », « (F-29, [A]) » ; ou trancher une convention de pièce et l'inscrire à PRDPlan §5.5, puisqu'elle vaudra pour les 34.

### Ce que le relecteur a tenté de réfuter sans y parvenir

Cinq attaques menées sans succès, et deux d'entre elles ont montré la pièce plus prudente que son socle.



1. **« PROGRAMMÉE » appliqué aux expirations du 7 janvier 2027 et du 7 décembre 2026.** J'ai attaqué l'emploi d'un instrument hérité en [C] (H-33) pour requalifier une échéance qui n'est l'engagement de personne. Tient : la réserve de `L05-A7` (verification/lot-L-05-registres.md) écrit mot pour mot « La date du 7 décembre 2026 est l'expiration automatique d'un Internet-Draft (six mois), non un jalon de publication : PROGRAMMÉ au sens mécanique, elle ne dit rien d'une adoption. » Le chapitre reprend cette qualification avec sa source et sa date — CA-11 satisfait, et l'incise « et elle ne dit rien d'une adoption ni d'un calendrier de publication » est la parade même que le lot prescrit.



2. **« le registre porte la mention type selon laquelle un *Internet-Draft* n'est ni endossé par l'IETF ni doté d'un statut formel dans le processus de normalisation ».** J'ai attaqué l'ajout, F-41 ne portant que « non endossé par l'IETF ». Tient : c'est la reformulation de bornage de `L05-A5`, verbatim, y compris le mot décisif — « **mention type** », qui interdit de lire l'énoncé comme un jugement porté sur ce brouillon-là plutôt que comme le pied de page que Datatracker affiche sur tous.



3. **Les quatre verbatims de RFC 6749 et RFC 7643 en §2.1 et §2.3**, qui excèdent tous ce que F-27 et F-28 reproduisent. Tient : les quatre sont les citations primaires consignées sous `L01-A1`, `L01-A2` et `L01-A4`, affirmations toutes versées à F-27 et F-28, et PRD §7.8 désigne les rapports de `verification/` comme porteurs de la traçabilité verbatim. Confrontation caractère par caractère : identiques (à la ponctuation finale près, avalée par les guillemets français). L'extraction partielle de `employeeNumber` — « assigned to a person, typically based on order of hire », qui coupe « or association with an organization » — est celle du lot lui-même, et F-28 coupe plus court encore : la pièce est ici **plus fidèle que son socle**, non moins.



4. **La parenthèse de borne du §2.1** — « *le socle rattache cette seconde phrase au flux de la §4.1 et non à un numéro de sous-section, le rendu du texte ayant varié entre deux interrogations* ». J'ai cherché une borne inventée. Tient : elle reproduit la réserve de `L01-A2` et le troisième échec de source consigné au lot (« L'outil de rendu l'a rattachée tantôt à l'étape (B) du flux de la section 4.1, tantôt à la section 4.1.2, sans stabilité entre deux interrogations »). Rien n'obligeait le chapitre à exposer cette instabilité au lecteur.



5. **Le traitement de la révision MCP.** J'ai cherché une date écrite ou suggérée. Tient : « est **annoncée au brouillon** ; la revalidation du 21 juillet 2026 en confirme la substance et **ne confirme pas la date** », puis « Le chapitre n'écrit donc aucune date de publication pour cette révision » — exactement la consigne de PRD §8.3 (« Les ch. 2 et 22 écrivent "annoncé au brouillon", jamais "publié le 28 juillet 2026" (R-09) »). Même constat pour les trois degrés d'absence du §2.4 : F-28 en degré 1, F-41/F-42 en degré 2, H-02 muet sur le texte OIDC en degré 3, la formule imposée §8.6 reprise mot pour mot ; et pour la clôture, qui rend la formulation R-01 sans écart.

---

## Chapitre 3 — A_CORRIGER

**Entrées citées** : `F-30`, `F-31`, `F-32`, `F-49`, `F-50`, `H-18`, `H-20`, `H-33`.

### BLOQUANT — « Elles sont donc citées ici sous la forme **(L-02, `L02-Ax`)**, distincte des identifiants de socle, et leur 

> « Elles sont donc citées ici sous la forme **(L-02, `L02-Ax`)**, distincte des identifiants de socle, et leur versement est remonté au cadrage plutôt qu'opéré par le rédacteur (PRDPlan §5.3). »

**Constat.** Le tableau de §3.1 — les quatre stades du W3C, matière centrale du chapitre et de sa thèse — repose intégralement sur `L02-A1` à `L02-A4`, et le décompte des 254 participants sur `L02-A5`. Aucune de ces cinq affirmations n'est une entrée du socle : les seules entrées L-02 versées sont F-30 (←L02-A6), F-31 (←L02-A8) et F-32 (←L02-A9). Le PRD §7.9 est explicite sur les affirmations non versées : « les autres restent au rapport de leur lot, consultables, mais **ne sont pas au socle** et ne peuvent donc pas être citées comme telles », et pour `L02-A4` nommément : « à verser par amendement du socle à la première rédaction qui en aura besoin, **jamais dans la pièce seule** ». Le chapitre fait exactement l'inverse : il les porte dans la pièce seule et se dispense de l'amendement. CA-01 exige en outre une entrée du socle **ou** une source primaire nouvelle ; or le chapitre ne cite jamais les URL primaires du W3C (elles existent pourtant au §F du rapport L-02) — il cite le rapport de lot, qui n'est ni l'un ni l'autre.

**Correctif.** Verser F-79 à F-83 au PRD §7.9 (reprenant `L02-A1`…`L02-A5` dans leur forme corrigée par le contrôle de bornage) **au même commit** que le chapitre, et retracer le tableau et le §3.3 vers ces identifiants. À défaut : citer chaque stade sur sa source primaire nommée (URL et date de consultation du rapport L-02), ce qui satisfait la seconde branche de CA-01, et retirer la notation (L-02, `L02-Ax`).

### BLOQUANT — « … et leur versement est remonté au cadrage plutôt qu'opéré par le rédacteur (PRDPlan §5.3). »

> « … et leur versement est remonté au cadrage plutôt qu'opéré par le rédacteur (PRDPlan §5.3). »

**Constat.** L'attestation est fausse sur pièce. `verification/remontees-gouvernance.md` ne porte que R-G-01 à R-G-04, toutes closes, aucune ne concernant L-02 ni le versement de `L02-A1`…`L02-A5` : aucune remontée n'a été ouverte. Et le PRDPlan §5.3, invoqué comme fondement, dit le contraire de ce qu'on lui fait dire : « une remontée n'a de valeur que si elle est **tranchée avant la pièce qui en dépend** […] Une remontée marquée « bloquant pour le ch. N » **interdit de lancer le ch. N** tant qu'elle n'est pas tranchée. » Le chapitre s'autorise donc à être écrit par la règle même qui l'interdisait. C'est la faute que CA-14 vise : une attestation rédigée depuis le souvenir de l'avoir faite. Deuxième trace : le registre `99-registre-gel.md` porte encore le ch. 3 au statut « Gabarit », alors que l'en-tête annonce « Rédigé (premier jet) » et un report « au **même commit** ».

**Correctif.** Ouvrir la remontée R-G-05 dans `verification/remontees-gouvernance.md` (objet : versement de `L02-A1`…`L02-A5`, qualification de niveau — arbitrée par l'instance d'exécution de phase, §5.3), la trancher, puis rédiger. Mettre à jour la ligne 4 du registre de gel au même commit. Retirer toute mention d'une remontée tant qu'elle n'est pas consignée.

### BLOQUANT — « … et **aucune entrée « Proposed Recommendation » ni « Recommendation » n'y figure** — fait négatif **VÉRIFIÉ

> « … et **aucune entrée « Proposed Recommendation » ni « Recommendation » n'y figure** — fait négatif **VÉRIFIÉ** au sens du PRD §8.6, borné à cette page d'historique et à elle seule, et à cette date (L-02, `L02-A4`, affirmation votée 3-0). »

**Constat.** Deux excès. **(a) Degré rétabli après correction.** Le contrôle de bornage du lot L-02 (§C) inscrit `L02-A4` en faute « **degré injustifié** » et retient une reformulation qui parle d'un « relevé de liste » des versions publiées, non d'un balayage de texte. Le chapitre remet le degré 1 (« fait négatif VÉRIFIÉ ») que le contrôle avait retiré, sans signaler la correction. **(b) Exclusion perdue.** Le balayage du rapport précise les chaînes cherchées : « « Proposed Recommendation », « Recommendation » **(hors « Candidate Recommendation Snapshot »)** ». Le chapitre supprime la parenthèse ; lu littéralement, il affirme qu'aucune entrée « Recommendation » ne figure sur une page dont il vient de dire qu'elle porte un *Candidate Recommendation Snapshot*. La borne du socle est perdue, et l'énoncé se contredit.

**Correctif.** Écrire : « le relevé de la liste des versions publiées, consultée ce jour-là, fait apparaître seize entrées, du *First Public Working Draft* du 28 janvier 2025 au *Candidate Recommendation Snapshot* du 5 mars 2026, et **aucune entrée étiquetée « Proposed Recommendation » ni « Recommendation »** — hors le *Candidate Recommendation Snapshot* lui-même. Le relevé porte sur cette liste et sur elle seule, à cette date. » Retirer « fait négatif VÉRIFIÉ » et la référence au degré 1 tant que le degré n'a pas été réarbitré.

### BLOQUANT — « Une revue de la Bank of Japan du 10 avril 2026, **citée à la même entrée**, situe l'emploi des accréditation

> « Une revue de la Bank of Japan du 10 avril 2026, **citée à la même entrée**, situe l'emploi des accréditations vérifiables en finance au registre de l'exploration plutôt que du déploiement ; »

**Constat.** Tracé à faux. La phrase précédente pose « (F-32) », donc « la même entrée » désigne F-32. Or F-32 s'écrit en entier : « Un précédent institutionnel existe hors du champ agentique : le cadre de gouvernance de l'écosystème vLEI de la GLEIF (version du 25 mars 2026) s'adosse à KERI et se déclare conforme aux recommandations de la Trust over IP Foundation. *(L02-A9.)* » — aucune mention de la Bank of Japan, ni de l'exploration, ni du déploiement. Cette matière vit dans la **réserve** de `L02-A9` au rapport de lot, c'est-à-dire hors socle (PRD §7.9 : « ne peuvent donc pas être citées comme telles »). S'y ajoute une fragilité de source que le chapitre expose sans en tirer la conséquence : le texte intégral n'ayant pas été extrait, la qualification « exploration plutôt que déploiement » repose sur la page de présentation.

**Correctif.** Remplacer « citée à la même entrée » par « relevée au rapport du lot L-02 en réserve de `L02-A9`, hors socle », et rétrograder l'énoncé : « une revue de la Bank of Japan du 10 avril 2026 dont seule la page de présentation a pu être lue — son texte intégral n'ayant pas été extrait — y situe l'emploi des accréditations vérifiables en finance au registre de l'exploration ; la qualification n'est donc pas portée ici comme fait » (gabarit de lacune, cas 3, PRDPlan §5.5).

### MAJEUR — « … un cadre d'architecture européen porte, sur la complétude du modèle de données du W3C comme format d'attes

> « … un cadre d'architecture européen porte, sur la complétude du modèle de données du W3C comme format d'attestation et sur les formats à prendre en charge, une matière directement pertinente pour une section consacrée aux profils d'interopérabilité. […] Le contenu de cet élément n'est donc ni cité ni employé ici »

**Constat.** Contradiction interne, et fuite de contenu. Dire que le document porte « sur **la complétude** du modèle de données du W3C **comme format d'attestation** » transmet la substance même de la note que le lot a refusé de convertir en affirmation (« W3C VCDM is not a complete specification of an attestation format »), au moment précis où le chapitre déclare ne pas l'employer. Le motif du refus — version et date attestées par la seule URL — vaut pour cette information comme pour le verbatim. Le lecteur retient que la complétude du VCDM est en cause, sur la foi d'un document dont on ignore la version.

**Correctif.** Neutraliser la description : « un cadre d'architecture européen porte une matière directement pertinente pour une section consacrée aux profils d'interopérabilité ». Ne nommer ni l'objet de sa note ni le sens de sa portée tant que sa version n'est pas attestée sur pièce.

### MAJEUR — « … modèle de données 2.1 en *Candidate Recommendation* à l'horizon 2027, interface de cycle de vie en Recomma

> « … modèle de données 2.1 en *Candidate Recommendation* à l'horizon 2027, interface de cycle de vie en Recommandation en 2028, `did:webvh` v1.0, *Web Bot Auth*, ANS v2 (`Monographie.md` §7.4.2). »

**Constat.** CA-11 exige que **tout** énoncé prospectif porte son tri PROGRAMMÉ / PROJETÉ / SPÉCULATIF. Le chapitre applique le tri à l'aboutissement de la 2.1 (SPÉCULATIF) mais laisse sans tri les deux échéances datées reprises de H-18 — 2027 et 2028 —, qui sont pourtant les seules dates futures du chapitre. La réserve fournie (« un agenda est un repérage […] H-18 étant en [C] ») porte sur le **niveau de preuve**, pas sur le **statut prospectif** : le PRD §7.1 pose que les deux instruments sont orthogonaux et « jamais l'un pour l'autre ». Accessoirement, H-18 écrit « **API** de cycle de vie » là où le chapitre écrit « **interface** de cycle de vie ».

**Correctif.** Ajouter le tri au même endroit : « … à l'horizon 2027 et une **API** de cycle de vie en Recommandation en 2028 — échéances **PROJETÉES**, portées par un agenda du Vol. I sans engagement daté du W3C (H-33) ». Rétablir « API ». Le [C] reste dit en plus, non à la place.

### MAJEUR — « … sa page de participants affichait **254 participants non-présidents** au relevé du 21 juillet 2026 (L-02, 

> « … sa page de participants affichait **254 participants non-présidents** au relevé du 21 juillet 2026 (L-02, `L02-A5`). […] La page du groupe porte du reste sa propre réserve, en langue originale : « W3C's hosting of this group does not imply endorsement of the activities. » »

**Constat.** Le contrôle de bornage du lot a corrigé `L02-A5` pour faute « **statut non dit** », et la forme retenue insère précisément la clause manquante : « statut qui, selon les règles de publication du W3C, **ne place ses travaux ni sur la voie des normes ni au rang de norme du W3C** ». Le chapitre ne la reprend pas et lui substitue le désaveu d'*endorsement*, qui n'est pas le même énoncé : ne pas cautionner une activité n'est pas la placer hors voie normative. R-09 impose la distinction « à chaque mention » — et le chapitre s'en réclame lui-même trois paragraphes plus haut. La règle générale posée en ouverture de §3.3 ne dispense pas de la mention.

**Correctif.** Insérer la clause corrigée à la mention : « Le premier, ***AI Agent Protocol Community Group***, existe depuis le 8 mai 2025 — statut qui, selon les règles de publication du W3C, ne place ses travaux ni sur la voie des normes ni au rang de norme du W3C (L-02, `L02-A5`) ; sa mission déclarée… ». Conserver la citation d'*endorsement* en surplus.

### MINEUR — | *Verifiable Credentials Data Model* v2.1 | ***Working Draft*** (brouillon de travail) | 11 mai 2026 |

> | *Verifiable Credentials Data Model* v2.1 | ***Working Draft*** (brouillon de travail) | 11 mai 2026 |

**Constat.** CA-08 et le registre du PRD §4 imposent l'ordre inverse : terme français d'abord, « terminologie technique anglaise **entre parenthèses** et en italique à la première occurrence ». La première occurrence du couple, dans le tableau de §3.1, met l'anglais en vedette et le français en glose. Le corps du chapitre applique ensuite la bonne forme (« brouillon de travail (*Working Draft*) », ligne 32) — c'est donc bien le tableau qui est en défaut, et c'est lui qui vient en premier.

**Correctif.** Dans la colonne « Stade au 21 juillet 2026 » : « **brouillon de travail** (*Working Draft*) ». Aligner de même « instantané de recommandation candidate (*Candidate Recommendation Snapshot*) » ou, si l'on garde le terme anglais nu comme nom de stade normatif, le déclarer une fois pour toutes en note du tableau.

### Ce que le relecteur a tenté de réfuter sans y parvenir

Ce que j'ai tenté de casser sans y parvenir, point par point.



**CA-10 (renvois) — testé exhaustivement, rien à prendre.** Les cinq renvois au Vol. I nomment tous leur fichier (`Monographie.md` §7.4.2, §7.3.2, §5.5.4) ; les cinq renvois de garde-fou nomment tous le volume (« R-09 du présent volume », idem R-01, R-02, R-05, R-14), ce qui écarte la confusion R-01/R-1. Aucune question du Vol. II n'est citée, donc le piège d'homonymie Q1-Q5 entre ch. 16 et ch. 21 ne s'ouvre pas. J'ai cherché un « §7.4 » ou un « §11.6 » non qualifié : il n'y en a pas.



**R-02 — l'attaque évidente échoue par construction.** J'ai balayé « garantit », « prouve », « atteste », « sécurise » appliqués à un mécanisme : zéro. Mieux, le chapitre se prive d'avance du terrain de la faute en établissant que le lot n'a extrait aucune mécanique cryptographique — ce que le §E du rapport L-02 confirme mot pour mot. On ne peut pas qualifier par la promesse ce qu'on a déclaré n'avoir pas lu.



**R-01 — la formule est celle de PRDPlan §5.5, en substance.** « Le passeport d'agent ne figure dans aucune spécification à date : c'est un objet de synthèse construit par cet ouvrage » reprend la forme imposée, avec les quatre pièces et le siège unique au ch. 8. Rien à redire non plus sur le constat tiré de H-18 (le syntagme figure au titre de §7.4.2 sans être défini ni réemployé) : H-18 le porte tel quel.



**R-14 et §8.6, degré 3 — trois emplois, trois fois la formule imposée.** §3.1 (contenu technique du VCDM/DID), §3.2 (profils DIF), §3.4 (déploiement financier) : chacun écrit « absence de documentation dans le corpus de cet ouvrage, non un fait négatif vérifié », et §3.4 ajoute explicitement que l'énoncé « aucune banque n'emploie ces mécanismes » n'est pas soutenu. C'est la réserve exacte du rapport de lot.



**CA-03 et §8.2 — l'attribution du 254 tient.** Occurrence unique, formule d'attribution en substance, et la lecture correcte (« un décompte d'inscrits n'est pas une mesure d'adoption ») là où la faute attendue aurait été d'en faire un indicateur de traction.



**F-31 [C] — le corollaire 1 est respecté.** J'ai cherché à montrer que le chapitre fait porter sa thèse d'adoption à une entrée [C] : il ne le fait pas, il le dit (« elle ne porte pas le propos de la section, et le chapitre ne lui fait rien porter ») et reproduit les deux bornes du socle — le relevé porte sur des intitulés, non sur la nature des organisations ; une suite de tests ne recense que ses volontaires.



**Bornes déclaratives de §3.3 — les trois sont là, et la plus coûteuse aussi.** L'interdiction explicite du rapport de lot (« ne jamais écrire que les Community Groups agentiques du W3C sont au nombre de trois ») est reprise en italique comme règle, le quatrième groupe repéré-non-ouvert est signalé, et `L02-A7`, écartée 2 réfutations sur 3, est nommée comme écartée et non reprise — y compris sous forme allusive, ce que j'ai vérifié ligne à ligne.



**Les six échecs de source sont tous portés**, et la norme ISO vLEI est correctement refusée comme n'étant établie que par une source secondaire — c'était le point où un rédacteur pressé aurait comblé la lacune.

---

## Chapitre 4 — A_CORRIGER

**Entrées citées** : `F-01`, `F-02`, `F-03`, `F-04`, `F-05`, `F-06`, `F-07`, `F-08`, `F-09`, `F-11`, `F-14`, `F-15`, `F-19`, `F-21`, `F-33`, `F-34`, `F-35`, `F-36`, `F-37`, `F-38`, `F-39`, `F-40`, `F-41`, `F-42`, `F-43`, `F-47`, `F-48`, `F-50`, `F-55`, `H-02`, `H-03`, `H-31`.

### BLOQUANT — les flux *on-behalf-of* et de jeton d'agent **étendent les RFC** — le dispositif ne se présente jamais comme d

> les flux *on-behalf-of* et de jeton d'agent **étendent les RFC** — le dispositif ne se présente jamais comme du « pur RFC » (H-02)

**Constat.** H-02 ne porte pas ce fait : sa réserve est une consigne au rédacteur — « ne jamais présenter le dispositif comme du "pur RFC" ». Le chapitre en inverse le sujet et en fait un constat sur la communication de l'éditeur (« le dispositif ne se présente jamais comme… »), c'est-à-dire une affirmation factuelle sur la documentation d'un fournisseur qu'aucune entrée, propre ou héritée, n'établit — et qui, de surcroît, est un négatif de corpus non balayé. L'entrée citée ne dit pas cela.

**Correctif.** « les flux *on-behalf-of* et de jeton d'agent **étendent les RFC** — le socle interdit de présenter le dispositif comme du « pur RFC » (H-02) ». Retirer toute assertion sur ce que l'éditeur dit ou ne dit pas de son propre dispositif.

### BLOQUANT — un identifiant vérifiable dont la révocation est interdite d'usage sans être outillée (F-07)

> un identifiant vérifiable dont la révocation est interdite d'usage sans être outillée (F-07)

**Constat.** Borne perdue, et c'est précisément celle que F-07 signale par un ⚠ : « L'interdiction porte sur la **clé**, non sur la **carte**. » Le verbatim de la spécification est « Expired or revoked **keys** MUST NOT be used for verification ». En faisant porter l'interdiction sur « un identifiant », le §4.4 déplace la prescription de la clé de signature vers la carte/l'identifiant d'agent — le glissement exact que l'entrée met en garde contre. Le §4.2 tient pourtant la distinction correctement ; elle est perdue à la conclusion du chapitre, là où elle sert de chute.

**Correctif.** « un identifiant vérifiable dont la clé de signature ne peut être ni expirée ni révoquée en usage, sans qu'aucun moyen ne permette d'établir ce statut (F-07) ».

### BLOQUANT — Sur **Q-B**, **répond** […] La provenance remonte donc à une autorité d'émission dont l'ancrage est documenté 

> Sur **Q-B**, **répond** […] La provenance remonte donc à une autorité d'émission dont l'ancrage est documenté — dans les bornes de son domaine.

**Constat.** Triple défaut sur le seul verdict plein du chapitre. (a) Niveau forcé : F-36 est **[B]** (extraction sans vote) et porte à elle seule le seul « répond » de la grille, présenté sans réserve. (b) Affirmation non tracée : F-36 documente un mécanisme de matérialisation (identité SPIFFE, X.509 de 24 h, GA du 22 avril 2026, *auth manager* en préversion à la même date ; chez l'autre fournisseur, identité de charge de travail) — il ne documente **ni la chaîne de provenance jusqu'à une autorité d'émission, ni son ancrage de confiance**, qui sont les deux termes qu'exige Q-B (PRD Annexe C §C.1). « l'ancrage est documenté » est une inférence, non marquée. (c) Contradiction interne : la phrase annonce « le verdict variant d'un produit à l'autre dans une même famille », puis le tableau rend **un seul** verdict pour la ligne « Annuaires commerciaux » — ce que la règle d'emploi 1 (par mécanisme, pas par produit) n'autorise pas à agréger.

**Correctif.** Rendre le verdict « répond partiellement », scinder par mécanisme et se tenir à F-36 : « Chez un fournisseur, l'identité d'agent repose sur une identité SPIFFE matérialisée par des certificats X.509 de vingt-quatre heures, GA datée du 22 avril 2026, son gestionnaire d'authentification demeurant en préversion à la même date ; chez un autre, l'identité d'agent n'est pas un type d'objet propre mais une identité de charge de travail (F-36, [B]). **Lecture de l'auteur** — ce que le socle établit : le mécanisme de matérialisation. Ce qu'il n'établit pas : l'ancrage de confiance de l'autorité d'émission, second terme de Q-B ; le verdict reste partiel. » Corriger la cellule du tableau en conséquence.

### BLOQUANT — | **Registres gouvernés** | partiellement — états prescrits sans délai de propagation (H-03, F-38) |

> | **Registres gouvernés** | partiellement — états prescrits sans délai de propagation (H-03, F-38) |

**Constat.** Tracé à faux, et le chapitre s'auto-contredit. H-03 porte l'ancrage SCIM 2.0, les quatre volets et les champs obligatoires ; F-38 porte le seul statut « White Paper | 2026-03-27 | Status: draft ». **Ni l'un ni l'autre ne mentionne les quatre états ni l'absence de délai de propagation** : cette substance vient exclusivement de F-55, entrée **[C]**. Le corps du texte l'écrit lui-même — « F-55 […] corrobore le verdict, elle ne le porte pas — celui-ci repose sur H-03 et F-38 » — mais le libellé retenu pour la cellule *est* le contenu de F-55. Un fait central se retrouve donc porté par une [C] sous la signature de deux autres entrées (CA-01 : « Une affirmation tracée vers une entrée [C] n'est pas centrale, ou n'est pas rédigée » ; CA-14 : l'attestation se constate sur pièce).

**Correctif.** Libeller la cellule sur ce que H-03 et F-38 portent réellement : « partiellement — identifiant spécifié et administrable, brouillon de labs (H-03, F-38) », et laisser au corps la mention explicite que les quatre états et l'absence de budget de fraîcheur ne sont corroborés que par F-55 [C], sans entrer dans le verdict.

### BLOQUANT — aucune proposition d'admission inter-domaines n'est ratifiée ni adoptée (F-50)

> aucune proposition d'admission inter-domaines n'est ratifiée ni adoptée (F-50)

**Constat.** Borne perdue sur trois axes à la fois. F-50 est **[B, degré 2]** et énumère ce qu'elle couvre : la spécification donnée à la DIF, « non ratifiée **au 22 juin 2026** » ; **les deux** *Internet-Drafts* consultés ; le CG W3C correspondant. Le chapitre supprime la date, supprime l'énumération, et remplace l'objet du socle (propositions d'identité d'agent consultées) par une catégorie nouvelle — « admission inter-domaines » — que F-50 ne délimite nulle part. Le résultat est un quantificateur universel non daté sur un corpus non balayé, soit exactement la « clause d'exclusivité, affirmation universelle déguisée » que le PRD §7.8 dit avoir tuée quatorze fois au vote.

**Correctif.** « aucune des propositions consultées n'était ratifiée ni adoptée — spécification à la DIF non ratifiée **au 22 juin 2026**, deux *Internet-Drafts* en soumission individuelle non adoptés, CG W3C sans rapport ni brouillon publié (F-50, [B], degré 2) ».

### MAJEUR — Rien ne le rattrape au niveau du projet : le `SECURITY.md` du dépôt tient en deux phrases

> Rien ne le rattrape au niveau du projet : le `SECURITY.md` du dépôt tient en deux phrases

**Constat.** Négatif de corpus en tête de phrase. F-08 porte un ⚠ dédié : son titre initial, « Aucune gouvernance des clés publiée », a été corrigé à la relecture P1.4 parce qu'il « restaurait au socle la substance de `L03-A4-04`, **écartée 3-0** » — « Ce que le balayage couvre, c'est un fichier ; l'entrée ne dit que cela. » F-11 est bornée de même à `GOVERNANCE.md`. Le chapitre borne correctement chacune des deux preuves, puis les chapeaute d'une affirmation qui porte sur « le projet » entier : l'énoncé écarté au vote est réintroduit comme thèse, les faits bornés servant d'appui.

**Correctif.** « Deux documents du projet ont été balayés, et ni l'un ni l'autre ne rattrape l'ancrage : le `SECURITY.md` … (F-08, degré 1, borné à ce fichier) ; la charte de gouvernance n'attribue à aucun organe une responsabilité de gestion des clés (F-11). Le reste du corpus du projet n'a pas été balayé : absence de documentation, non fait négatif vérifié. »

### MAJEUR — l'instance qui a compilé le livre blanc de référence place hors de son périmètre le développement de tout prot

> l'instance qui a compilé le livre blanc de référence place hors de son périmètre le développement de tout protocole normatif d'identité d'agent (F-48, degré 2, reprise dans la substance)

**Constat.** La moitié de l'entrée est retirée, et c'est celle qui nuance. F-48 se termine par « **et renvoie ce travail à un groupe de travail** ». Omise, l'exclusion devient un renoncement institutionnel là où le socle décrit un aiguillage. Le chapitre s'en sert pour appuyer le verrou du KYA — c'est le sens même du fait qui change. Accessoirement, le verbatim de la charte est « Development of any global standards protocols related to AI Agents & Identity » : « global » disparaît, et « tout protocole normatif » élargit encore.

**Correctif.** « l'instance qui a compilé le livre blanc de référence place hors de son périmètre le développement de protocoles de normalisation mondiaux liés à l'identité des agents, **et renvoie ce travail à un groupe de travail** (F-48, [A], degré 2, reprise dans la substance) ».

### MAJEUR — la disponibilité générale du principal de ces produits est datée d'avril 2026 par les notes de version de son 

> la disponibilité générale du principal de ces produits est datée d'avril 2026 par les notes de version de son éditeur (F-33)

**Constat.** Attribution supprimée. F-33 nomme Entra Agent ID ; F-36 nomme Google Cloud et AWS ; F-37 nomme Microsoft Graph v1.0. Le chapitre anonymise systématiquement — « le principal de ces produits », « son éditeur », « Chez un fournisseur », « chez un autre », « la réserve d'éditeur ». Le §8.4 (1) impose l'inverse : « chaque capacité est **attribuée à la documentation de l'éditeur**, avec sa date et son statut ». Un statut GA/préversion non attribué nominativement n'est pas revalidable au gel suivant, et la neutralité fournisseur est une interdiction de recommander, non une interdiction de nommer.

**Correctif.** Nommer les éditeurs et les surfaces d'API tels que les entrées les portent (Entra Agent ID / F-33 ; `agentIdentityBlueprint` de Microsoft Graph v1.0 / F-37 ; Google Cloud IAM et AWS / F-36), en conservant les formulations de statut déjà présentes — l'attribution nominative satisfait §8.4 sans introduire aucune formulation de supériorité.

### Ce que le relecteur a tenté de réfuter sans y parvenir

Ce que j'ai tenté de casser et qui a résisté, contrôle par contrôle.



**Le décompte du §4.2.** Recompté cellule par cellule, sans reprendre le chiffre du texte : ligne carte = 1 partiel + 1 « ne répond pas » + 3 vides ; ligne annuaires = 3 partiels + 1 « répond » + 1 vide ; ligne registres = 2 partiels + 3 vides. Total 8 verdicts (1 + 1 + 6) et 7 vides, somme 15. Les trois cardinaux annoncés sont exacts.



**La citation de H-31 (§4.4).** Comparée mot à mot au PRD §7.3 : « un agent ne doit jamais exécuter une action irréversible sans garde-fou structurel ; la règle est la préparation par l'agent et la *release* humaine sur l'action irréversible » est littérale, ponctuation comprise. J'ai aussi soupçonné trois énoncés voisins d'être des ajouts d'auteur — l'indexation « sur le produit matérialité × réversibilité, non sur la capacité brute du modèle », « la graduation L0-L3 indexe deux de ses niveaux sur les mêmes critères », « Seuls le cardinal et la numérotation discriminent » : les trois figurent dans H-31 (le second sous la forme « le tableau de (c) indexe L1 et L2 sur les mêmes critères »). Aucun n'est fabriqué.



**R-13.** Les trois échelles sont citées à la forme imposée par PRDPlan §5.5, les quatre éléments présents pour chacune : quatre paliers non numérotés (`Monographie.md` §5.0.2, siège §5.1.1), continuum six niveaux 0-5 (`Monographie.md` §2.2.4, désignations au tableau 3 de `Synthese Monographie.md` §4.2), graduation L0-L3 (`Chapitres/Annexe B - Architecture de Solutions.md` §1.3). « Copilote » n'apparaît jamais seul — vérifié sur les cinq occurrences du fichier.



**Le régime de H-31 comme entrée [C] non élevable.** J'ai cherché à faire tomber tout le §4.4 par CA-01. Il tient : §A.5 autorise explicitement qu'« une construction d'auteur de ce volume peut s'y adosser », et le chapitre le déclare, marque la section en totalité et écrit « Le croisement qui suit ne peut donc rien établir ; il ordonne ». Conforme.



**F-19 (§4.3).** Citation anglaise reprise caractère pour caractère, en langue originale (CA-08), niveau [A] annoncé et exact.



**R-01 (§4.3).** « Le passeport d'agent ne figure dans aucune spécification à date : c'est un objet de synthèse construit par cet ouvrage » — reprise de la formulation imposée, avec les quatre pièces et la mention « sur le papier ».



**Les axes du Vol. I (§4.1).** J'ai voulu les qualifier d'affirmation non tracée, faute d'entrée H-xx les portant. Refus : le PRD §6.2 (ligne de spécification du ch. 4) et le TOC §4.1 portent la formulation à l'identique, avec le même renvoi qualifié `Synthese Monographie.md` §11.2, et le chapitre les déclare inspiration et non dérivation — l'énoncé n'est donc pas central au sens de CA-01.



**La chaîne carte signée du §4.2** (F-01 à F-09, F-11). Chaque clause correspond à son entrée : les quatorze champs, la procédure en six étapes, MAY/SHOULD, le champ `signatures` exclu du contenu signé, la re-canonicalisation par le vérificateur. La distinction clé/carte de F-07 y est correctement tenue — elle n'est perdue qu'au §4.4.



**Les renvois (CA-10).** Tous les renvois au Vol. I nomment leur fichier ; la parenthèse du §4.2 qualifie explicitement le volume des garde-fous (« R-14 du présent volume […] à ne pas confondre avec les R-1 à R-8 du Vol. II »). Aucun renvoi non qualifié trouvé.



**R-14 et les trois degrés.** Le vocabulaire imposé est employé correctement partout : degré 1 pour F-05, F-06, F-08, F-03, F-39 ; degré 2 pour F-35, F-41, F-42, F-43, F-48 ; degré 3 nommé et formulé à la lettre du §8.6 pour les sept cases vides. Aucune absence de documentation présentée en fait négatif.

---

## Remontées de gouvernance ouvertes par la rédaction

⚠ **Les rédacteurs ont remonté sans corriger, conformément à PRDPlan §5.3.** Elles sont **ouvertes**, non tranchées :

- **ch. 1** — Bornage L-01 fautif sur R-02 : la correction de bornage de `L01-A8` a remplacé « communique » (rendu littéral de la spécification SPIFFE-ID, « the mechanism through which a workload communicates its identity ») par « atteste » — verbe explicitement proscrit par R-02 du présent volume (PRDPlan §5.5). Le chapitre écrit « communique » et déclare l'écart en Notes ; le rapport de lot n'est PAS corrigé (PRDPlan §5.3).
- **ch. 1** — Six affirmations de L-01 retenues par le lot mais non versées au socle §7.9 : `L01-A2`, `L01-A4`, `L01-A6`, `L01-A7`, `L01-A8`, `L01-A9` (SPIFFE-ID et son critère de validité, graduation CNCF, les sept drafts WIMSE, la clause « AI intermediaries are a special case of delegated workloads »). §7.9 n'a versé de L-01 que F-27, F-28, F-29 — or toute la branche « identité de charge de travail » de la généalogie du ch. 1 repose sur elles. Versement demandé avant la relecture adversariale.
- **ch. 1** — Régime de citation non arbitré : §7.9 écrit que les affirmations non versées « ne peuvent donc pas être citées comme telles », alors que CA-01 admet « une source primaire nouvelle de qualité équivalente ». Le chapitre les cite par identifiant de lot, en le déclarant. L'arbitrage appartient au PRD, pas au rédacteur.
- **ch. 1** — Thèse et découpage du ch. 1 au TOC en avance sur le socle : la thèse nomme comptes de service, certificats X.509, clés d'API et secrets d'atelier logiciel — aucune entrée ne les documente ; le §1.2 annonce « ratio identités machines/humaines » et « prolifération des secrets » — aucun chiffre vérifié au socle, et L-01 déclare n'avoir cherché aucune métrique. Soit un lot instruit ce passif, soit la thèse et l'intitulé de §1.2 sont reformulés au TOC (version++).
- **ch. 1** — Registre de gel non mis à jour : l'en-tête de pièce impose le report de la date de gel dans `monographie/99-registre-gel.md` au même commit (CA-04). Non fait ici — hors périmètre de la rédaction de la pièce seule.
- **ch. 2** — RFC 6749 §4.4 (mode d'octroi par justificatifs de client) : relevée et citable par le lot L-01, qui la déclare lui-même « le complément le plus direct de L01-A2 pour le chapitre 2 », mais NON versée au socle (§7.9 ne porte que F-27, F-28, F-29 pour L-01). Le §2.1 a dû la traiter en absence de documentation au lieu de s'y adosser. À verser par amendement du socle.
- **ch. 2** — L01-A6 et L01-A7 (les sept Internet-Drafts du groupe WIMSE avec révisions, dates et expirations au 21 juillet 2026 ; §3.4.11 de draft-ietf-wimse-arch-08 rangeant les intermédiaires d'IA parmi les charges de travail déléguées) non versées au socle. WIMSE n'est donc mobilisable que par H-18, entrée [C] au gel de juin 2026 qui cite encore la révision -07. Le chapitre n'a pu que signaler l'entrée sans s'y adosser — matière directe du §2.2, à verser.
- **ch. 2** — Le titre du chapitre, fixé au TOC, nomme OIDC ; aucune entrée du socle ne porte le corps des spécifications OpenID Connect (seul H-02 le mentionne au titre d'un produit qui s'en réclame). §2.4 le déclare en absence de documentation. Arbitrage à l'auteur : instruire un lot OIDC, ou amender le titre au TOC (version++, autorité du découpage).
- **ch. 2** — Divergence de formulation au socle sur l'expiration de draft-abbey-scim-agent-extension : H-03 écrit « le brouillon IETF a expiré le 19 avril 2026 », F-41 porte « unique version -00 du 16 octobre 2025 » et le rapport L-05 relève au datatracker une dernière mise à jour au 19 avril 2026. Les deux formulations coexistent sans harmonisation ; le chapitre écrit celle de F-41 et ne tranche pas.
- **ch. 2** — Piège de renvoi relevé par le rapport L-05 (réserve de L05-A5) et non porté au socle : le datatracker héberge une seconde fiche `draft-scim-agent-extension` (sans préfixe d'auteur), même titre, mêmes auteurs, version -00 du 11 octobre 2025, également expirée. Un renvoi non qualifié désigne deux objets. Le chapitre nomme le brouillon en entier à chaque citation, mais la règle mériterait d'être consignée au PRD au même titre que les autres pièges de renvoi.
- **ch. 2** — L01-A8 et L01-A9 (spécification SPIFFE-ID, statut « Stable » ; maturité CNCF « Graduated » et sa divergence de date d'un jour entre les deux pages de la CNCF) non versées au socle. Matière du ch. 1, signalée ici pour la cohérence de la Partie I : le ch. 1 rencontrera le même mur.
- **ch. 3** — Socle incomplet, bloquant pour ce chapitre : cinq affirmations du rapport L-02 ne sont versées dans aucune entrée F-xx — `L02-A1` (VC DM 2.0, Recommandation du 15 mai 2025), `L02-A2` (v2.1, Working Draft du 11 mai 2026), `L02-A3` (DID v1.0, Recommandation du 19 juillet 2022, errata), `L02-A4` (DID v1.1, Candidate Recommendation Snapshot du 5 mars 2026, votée 3-0), `L02-A5` (AI Agent Protocol CG, 8 mai 2025, 254 participants). Le PRD §7.9 n'en nomme qu'une (`L02-A4`) et prescrit son versement « à la première rédaction qui en aura besoin » ; les quatre autres sont dans le même cas et ne sont pas nommées. Tout le §3.1 repose sur elles. Versement à opérer au socle avant la relecture adversariale — non fait ici (PRDPlan §5.3).
- **ch. 3** — Coquille probable au PRD §7.9 : l'entrée F-30 renvoie à « (F-33) » pour la réserve « aucun rapport ni brouillon publié à la date de consultation » ; F-33 est la GA d'Entra Agent ID (lot L-04). La cible plausible est H-33 (tri prospectif). Non corrigé.
- **ch. 3** — Titre de section du TOC v0.5 en surpromesse : « 3.1 VC Data Model et DID Core : ce que les recommandations établissent » annonce un contenu que le lot L-02 n'a pas extrait — seuls les stades l'ont été. Le chapitre déclare l'écart dans son texte plutôt que de le combler. Relève du découpage, donc de l'auteur (PRDPlan §5.3).
- **ch. 3** — §3.2 sans socle : le périmètre déclaré de L-02 (PRD §7.6) nomme la DIF parmi ses sources, et le rapport du lot ne porte aucune affirmation à son sujet. La section est écrite comme lacune de couverture, adossée à F-49 et F-50 (lot L-07, siège ch. 11), qui ne portent pas sur les profils d'interopérabilité. Décision à prendre : lot complémentaire, ou révision du découpage de §3.2.
- **ch. 3** — Élément relevé et délibérément non converti en affirmation par L-02 (cadre d'architecture du portefeuille européen d'identité numérique, chemin versionné 2.3.0) : matière directement pertinente pour §3.2 et §3.4, écartée parce que version et date ne sont attestées que par l'URL. Le chapitre en signale l'existence sans en reprendre le contenu. À instruire.
- **ch. 3** — Registre de gel `monographie/99-registre-gel.md` à renseigner au même commit que ce chapitre (date de gel : 21 juillet 2026, volumétrie réelle 3080 mots contre 2750 de cible, écart +12,0 % documenté et non corrigé — PRDPlan §5.2 point 7). Non fait ici.
- **ch. 4** — Le TOC formule la thèse du chapitre comme un fait négatif de corpus — « aucun mécanisme de 2026 ne répond aux cinq » —, c'est-à-dire la forme même que le PRD §8.6 et R-14 proscrivent. Le chapitre la traite en hypothèse falsifiable, borne sa portée aux mécanismes réellement instruits et le déclare en §4.2 ; la reformulation de la ligne de thèse au TOC (version++) n'a PAS été faite ici — un rédacteur ne corrige ni le TOC ni le PRD (PRDPlan §5.3).
- **ch. 4** — Aucune entrée du socle ne porte `Synthese Monographie.md` §11.2 (la grille par axes du Vol. I : découverte, sémantique, identité et confiance, gouvernance des frontières). Le PRD §6.2 et le TOC la désignent directement, sans entrée H-xx. Le chapitre l'emploie exclusivement en inspiration marquée, jamais en fait central, mais la traçabilité repose ici sur les documents de cadrage et non sur le socle. À trancher : créer une entrée héritée [C] pour §11.2, ou déclarer l'exception au PRD §7.3.
- **ch. 4** — Volumétrie : 3376 mots (commande PRDPlan §1.5) contre une cible de ~2750, soit +22,8 % ; 3128 hors tableaux. Écart documenté et NON corrigé par amputation, après trois passes de compression : les quinze cases de grille sur trois mécanismes portent chacune leur borne (niveau, degré d'absence, statut pré-normatif), et couper davantage supprimerait des bornes. Décision de cadrage requise : relever la cible du ch. 4 au TOC, ou ramener l'application-témoin à deux mécanismes.
- **ch. 4** — Le registre de gel `monographie/99-registre-gel.md` n'a pas été renseigné par ce travail. La date de gel du 21 juillet 2026 est à y reporter au même commit que la pièce (CA-04).
- **ch. 4** — CA-14 non satisfait : la relecture adversariale par un relecteur distinct du rédacteur n'a pas eu lieu. Le statut « Rédigé (premier jet) » le porte, mais l'étape reste due avant tout passage à « Rédigé et relu adversarialement ».
- **ch. 4** — F-55 est une entrée [C] et porte le seul élément documenté du régime d'états de révocation des registres gouvernés (quatre états, aucun délai de propagation). Elle est employée ici en corroboration seulement. Si le ch. 7 en a besoin comme fait central, une élévation préalable est requise (CA-01).

⚠ **La plus structurante** : plusieurs affirmations retenues par les lots n'ont pas été versées au socle §7.9, et ce sont précisément celles dont la Partie I avait besoin. *Le socle a été constitué avant que la rédaction ne dise ce dont elle avait besoin ; c'est l'ordre normal, et c'est pourquoi il produit ce genre de manque.*

## Ce que les chapitres déclarent ne pas pouvoir écrire

**Ch. 1** — Deux lacunes déclarées dans le chapitre, toutes deux au degré 3 de PRD §8.6 (absence de documentation, non fait négatif vérifié). (1) La généalogie antérieure à 2012 : la pièce la plus ancienne du socle est le RFC 6749 d'octobre 2012 ; comptes de service, clés d'API et secrets d'atelier logiciel sont nommés sans être décrits — le titre annonce un demi-siècle, le socle n'en documente pas le quart, et le chapitre l'écrit en avertissement de portée avant la première ligne de généalogie. (2) Tout ordre de grandeur de prolifération : aucun ratio identités machines/humaines, aucune mesure de prolifération des secrets, aucune métrique d'adoption ou de déploiement — L-01 déclare n'en avoir cherché aucune, pour aucun de ses objets. La thèse du chapitre est donc portée par un incident public daté à l'échelle (F-21) et par la distinction NHI / identité d'agent (F-20), et aucun de ses énoncés ne dépend d'un chiffre.

**Ch. 2** — Cinq manques, tous déclarés dans le chapitre plutôt que comblés. (1) Le mode d'octroi par justificatifs de client de RFC 6749 §4.4 — le pendant technique direct du constat de §2.1 : déclaré en absence de documentation dans le corpus de l'ouvrage (PRD §8.6, degré 3), avec renvoi à l'amendement du socle. (2) OpenID Connect, nommé au titre du chapitre : le socle n'en porte pas le corps ; déclaré en absence de documentation au §2.4, et l'écart entre le titre et le socle est signalé. (3) WIMSE : entrée H-18 en [C] — une entrée [C] ne porte jamais un fait central — et relevé récent non versé au socle ; le §2.2 le signale et ne s'y adosse pas. (4) RFC 7644, le protocole SCIM, non ouvert par le lot L-01 : borne portée explicitement au §2.3 et rappelée au §2.4, de sorte que le fait négatif de F-28 reste borné à l'énumération des sous-sections de la §4 de RFC 7643 telle que consultée le 21 juillet 2026. (5) La date de la révision majeure de MCP : la revalidation du 21 juillet 2026 confirme la substance au brouillon et ne confirme pas la date (PRD §8.3) — le chapitre n'écrit aucune date de publication. La lacune 14 (jetons de transaction) est portée en encadré au gabarit « passe conduite » : instruite par F-29, non close, la question restant ouverte faute de RFC et de date de publication annoncée.

**Ch. 3** — Le socle ne porte que le STADE des quatre documents du W3C, jamais leur contenu : ni modèle de données, ni mécanismes de preuve, ni méthodes de résolution n'ont été extraits (absence de documentation, degré 3). Le chapitre ne peut donc dériver aucune exigence d'architecture ni aucune qualification cryptographique (R-02). Manquent en outre : (a) tout fait sur les profils d'interopérabilité de la DIF, pourtant au périmètre déclaré de L-02 — §3.2 est une lacune de couverture assumée ; (b) toute source primaire documentant un établissement financier réglementé nommément désigné exploitant des VC W3C ou des DID en production — degré 3, et non un fait négatif : l'énoncé « aucune banque n'emploie ces mécanismes » reste interdit (R-14) ; (c) le contenu des documents produits par les Community Groups agentiques, dont aucun n'a été ouvert par le lot ; (d) tout inventaire exhaustif des Community Groups du W3C — trois groupes lus, un quatrième repéré non ouvert, d'où l'interdiction d'écrire qu'ils sont trois ; (e) six échecs de source consignés (fiche ISO du vLEI en 403, glossaire vLEI en 404, deux accès au cadre EUDI, texte intégral de la BoJ Review non extractible, section du Community and Business Group Process non restituée), chacun retirant une possibilité d'affirmation au chapitre. Enfin, F-31 étant en [C], le relevé d'interopérabilité n'entre qu'en illustration et ne porte pas le propos de §3.4 (CA-01).

**Ch. 4** — Sept cases sur quinze restent vides au degré 3, et c'est le résultat le plus net de l'application-témoin. (1) Q-C, Q-D et Q-E de la carte d'agent signée : aucun balayage du lot L-03 ne porte sur ce que la carte exprime du mandat, des bornes de privilège ou de l'imputabilité — le socle documente exhaustivement la signature, la clé et la validité, et rien d'autre. (2) Q-E des trois mécanismes sans exception : aucune entrée du socle ne documente une chaîne d'imputabilité remontant jusqu'à une personne ou une entité juridique. Q-E est la question la moins instruite de la grille, et le chapitre le déclare plutôt que de la combler par inférence. (3) Q-B et Q-C des registres gouvernés : le socle instruit l'ancrage normatif du dispositif (brouillon IETF expiré, consolidation renvoyée) mais pas la chaîne de provenance de l'agent inscrit. (4) « Interrogeable à l'instant t » (Q-C) n'est établi pour aucun des trois mécanismes : le mandat s'exprime (F-47, H-02), son interrogation à l'instant t n'est documentée nulle part. (5) Le croisement de la §4.4 n'a aucun appui de socle : le corpus d'appui retiré n'a laissé aucun modèle de maturité à confronter, et H-31 est [C] non élevable — le socle ne permettait donc d'écrire ni une comparaison de modèles, ni une correspondance maturité ↔ exigences établie, seulement un ordonnancement d'auteur explicitement marqué.

