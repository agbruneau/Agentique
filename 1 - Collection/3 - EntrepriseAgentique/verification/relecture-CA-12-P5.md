# Relecture dédiée CA-12 — dualité d'usage — reconstitution des passes du 22 juillet 2026 sur les trente-quatre pièces

| Champ | Valeur |
|---|---|
| Critère | **CA-12** ([PRD](../prd/PRD.md) §11) — relecture **distincte de la relecture de conformité**, confiée à un relecteur distinct du rédacteur, sur la seule question : *un lecteur peut-il dériver une attaque de ce texte ?* Le critère exige en outre que **le compte rendu soit déposé sous `verification/` et nommé dans la pièce qu'il couvre** |
| Garde-fou contrôlé | **R-12 du présent volume** ([PRD](../prd/PRD.md) §8.5) — traitement défensif exclusif. ⚠ R-12 est le seul garde-fou du volume **sans motif de balayage** ([PRD](../prd/PRD.md), Annexe A §A.6) : un balayage §A.6 « vert » ne dit rien de lui |
| Date de la reconstitution | **22 juillet 2026**, phase **P5** |
| Objet des passes reconstituées | Les passes de relecture CA-12 conduites le **22 juillet 2026** sur les **34 pièces** de [`monographie/`](../monographie/) |
| ⚠ **Nature de ce document — la borne est en tête parce qu'elle change ce que le document vaut** | **Ce rapport est une RECONSTITUTION. Il n'a pas été rédigé par les passes qu'il décrit.** Il a été établi **après coup**, par ouverture des **journaux que ces passes ont laissés dans les blocs `## Notes` des pièces** et par constat sur l'arbre de travail et sur `git diff`. *Un rapport reconstitué depuis les journaux des pièces contrôlées n'est pas le compte rendu d'un contrôleur distinct* : il rapporte ce que les pièces disent d'elles-mêmes, plus ce que le disque permet d'en vérifier — et rien au-delà. La différence est exactement celle que CA-12 met en jeu, et elle est écrite ici plutôt que passée sous silence |
| Ce que ce document ne fait pas | ⚠ **Il n'atteste la conformité d'aucune pièce à R-12.** Il ne relit aucune pièce sous la lentille de la dualité d'usage : la question « un lecteur peut-il dériver une attaque de ce texte ? » **n'est pas posée ici**. Il consigne des retraits, leur siège et leur état d'application |
| Assujettissement | ⚠ **Le présent fichier est lui-même sous R-12** ([PRD](../prd/PRD.md) §8.5 : R-12 couvre « toute pièce de `verification/` »). Il désigne les passages qu'il discute par leur emplacement plutôt que par leur contenu |
| Comptes rendus CA-12 antérieurs | [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) (21 juillet 2026, pièces) et [`relecture-CA-12-lots.md`](relecture-CA-12-lots.md) (22 juillet 2026, rapports de lot) |

---

## 1. Pourquoi ce document existe, et pourquoi sa forme est elle-même le défaut qu'il consigne

**CA-12 porte deux termes, et le second a été manqué.** Le terme substantiel — la relecture — a été conduit ; le terme procédural — *le compte rendu est déposé sous `verification/` et nommé dans la pièce qu'il couvre* — ne l'a pas été. Constat sur le répertoire, pris avant le dépôt du présent fichier : **deux comptes rendus CA-12 y vivent**, celui du 21 juillet 2026 sur les pièces et celui du 22 juillet 2026 sur les rapports de lot. **Aucun troisième n'existe pour les passes du 22 juillet 2026 sur les trente-quatre pièces.**

Leurs traces vivent **uniquement dans les blocs `## Notes` des pièces qu'elles ont contrôlées**. *La pièce contrôlée rend compte d'elle-même* — et c'est précisément le geste que CA-12 range parmi les non-contrôles lorsqu'il porte sur le contenu.

⚠ **Combler ce manque par le présent document ne le répare qu'à moitié, et il faut le dire avant de le lire.** Écrire un compte rendu **depuis les journaux des pièces qu'il couvre** revient à faire attester le contrôle par le contrôlé, à un degré de séparation près. Le seul geste qui tiendrait pleinement le critère serait que **chaque passe rende son propre relevé**, ou que les passes soient **rejouées** en déposant leur compte rendu. Ces options sont posées au §7 et **ne sont pas tranchées ici**.

*Ce document vaut donc pour ce qu'il est : une trace récupérée, meilleure que rien, et inférieure à ce que le critère demande.*

## 2. La source, et ce qu'elle permet d'établir

**Trois sources ont été employées, et elles ne se valent pas.**

| Source | Ce qu'elle établit | Ce qu'elle n'établit pas |
|---|---|---|
| **Journal aux `## Notes` de la pièce** — bloc « Relecture dédiée CA-12 » ou déclaration de retrait datée | Ce que la passe déclare avoir retiré, à quel siège, et pour quel motif | Que la passe a eu lieu comme elle le déclare ; que son relecteur était distinct du rédacteur |
| **Constat sur l'arbre de travail** — recherche de la chaîne retirée sur `monographie/` entier | Que la clause n'y subsiste plus vivante | Ce qui aurait dû être retiré et ne l'a pas été |
| **`git diff HEAD`** — comparaison au commit `ea05501` | Le texte exactement supprimé et le texte exactement inséré | Rien sur les passes antérieures au commit |

⚠ **Le périmètre de chaque passe n'est pas constatable, et c'est la borne la plus lourde de cette reconstitution.** L'ordonnancement de la phase déclare **cinq passes** couvrant les trente-quatre pièces. **Aucun journal ne nomme sa passe, ne borne son périmètre, ne date son exécution autrement que par la journée, ni n'identifie son relecteur.** Ce qui se constate est **l'ensemble des pièces portant une intervention**, non la partition de cet ensemble entre cinq passes. *Un cardinal de passes déclaré en amont et non retrouvable en aval ne se recopie pas : il se signale.*

## 3. Ce qui a été retiré — huit sièges, constatés un par un

☑ **Huit retraits ont été rendus le 22 juillet 2026 au titre de CA-12 sur `monographie/`** — cardinal établi par balayage de `monographie/` entier, non repris d'une déclaration de passe. Chacun a été cherché **à son siège**, et la chaîne retirée recherchée sur le répertoire **entier**.

⚠ **Une valeur antérieure est conservée et datée** : [`relecture-CA.md`](relecture-CA.md) §5.2, déposée le même jour, en dénombre **six**. L'écart est de **deux** — l'**avant-propos** et le **ch. 28 §28.3** —, et il n'est pas une erreur de ce rapport-là : les deux retraits y sont absents parce que la table qu'il dresse suit les retraits **annoncés à la passe**, tandis que le présent relevé balaie le répertoire. *Un contrôle qui vérifie une liste ne trouve pas ce qui n'y figure pas.*

| # | Siège | Clause retirée | Registre | État constaté | Journal dans la pièce |
|---|---|---|---|---|---|
| 1 | **ch. 7**, `## Notes` | « la pièce ne traite pas de matière offensive » | non-contenu | **retirée** — 0 occurrence vivante ; suppression et remplacement lus sur `git diff` | ⚠ **aucun** |
| 2 | **ch. 8**, `## Notes` | « la pièce ne traite pas de matière offensive » | non-contenu | **retirée** — 0 occurrence vivante ; suppression et remplacement lus sur `git diff` | ⚠ **aucun** |
| 3 | **ch. 10**, `## Notes` | « — **il l'applique** », seconde moitié d'une phrase dont la première refusait de certifier | conformité | **retirée** — 0 occurrence vivante | ☑ daté, clause citée, motif écrit |
| 4 | **ch. 14**, `## Notes` | « elle est la seule de la Partie IV dont la matière est intégralement défensive » | mixte — auto-qualification **et** clause d'exclusivité | **retirée** — 0 occurrence vivante hors de sa citation au journal | ☑ daté, clause citée, **deux** motifs distingués |
| 5 | **ch. 15**, corps **§15.2** | « Conformément au traitement défensif exclusif du volume […] » | conformité | **retirée** du corps | ☑ daté, clause citée, motif écrit, forme de remplacement nommée |
| 6 | **ch. 25**, `## Notes` | « ni séquence, ni charge utile, ni identifiant de vulnérabilité » | non-contenu | **retirée** — 0 occurrence vivante hors de sa citation au journal | ☑ daté, clause citée, motif écrit, **précédent nommé** |
| 7 | **avant-propos**, corps, § « Ce que l'ouvrage ne fait pas » | « **Il ne fournit pas de recette d'exploitation.** », plus l'énumération « n'en reproduit ni charge utile, ni séquence, ni preuve de concept » | non-contenu | **retirée** ; **−8 mots**, 3 955 → **3 947** | ☑ daté, clause citée, **portée et chronologie aggravantes** déclarées, **révocabilité** écrite |
| 8 | **ch. 28**, corps **§28.3** | « et c'est tout ce qui est écrit ici » | non-contenu | **retirée** ; **−8 mots**, 10 996 → **10 988** | ☑ daté, clause citée, circonstance aggravante déclarée, **révocabilité** écrite |

**Les huit relèvent d'une seule famille — l'attestation auto-délivrée —, et aucun élément opératoire n'a été retiré.** Aucun journal ne rapporte de charge utile, de séquence d'exploitation, de preuve de concept ni d'extrait de code offensif.

**Ventilation par registre, recomptée sur la table** : **cinq** portent sur ce que la pièce **ne contient pas** (ch. 7, ch. 8, ch. 25, avant-propos, ch. 28 §28.3) ; **deux** sur la **conformité** que la pièce s'attribue (ch. 10, ch. 15 §15.2) ; **un** est **mixte** (ch. 14). La distinction n'est pas de forme : elle est exactement celle que le §6 met en cause.

### 3.1 Deux retraits ne laissent aucun journal, et c'est un défaut de traçabilité en soi

⚠ **Les ch. 7 et ch. 8 ne portent aucune trace du retrait qu'ils ont subi.** La clause a disparu, le texte de remplacement est en place, et **rien dans la pièce ne dit qu'une passe est intervenue, à quelle date, ni sous quel critère**. Les deux retraits ne sont constatables que par **absence** — et une absence ne se distingue pas, à la lecture de la pièce, d'une clause qui n'aurait jamais été écrite.

Ils ont ici été établis par ouverture de `git diff HEAD` : la ligne supprimée du **ch. 8** portait « […] ; **la pièce ne traite pas de matière offensive**, et le contrôle CA-12 reste à exécuter sur elle […] », celle du **ch. 7** la même clause en fin de bilan de balayage ; l'une et l'autre sont remplacées par la déclaration que le contrôle **n'est pas tenu**. *Le correctif est le bon ; c'est sa trace qui manque.* Sans l'historique git, cette reconstitution n'aurait pas pu les établir — et l'historique git n'est pas le livrable.

**Six retraits sur huit sont donc reconstituables depuis la pièce seule ; deux ne le sont pas.**

### 3.2 Ce que les huit retraits ont en commun — et le raisonnement mérite d'être conservé

**Aucune des huit propositions retirées n'était matériellement fausse.** *Ce qui est proscrit est le geste, non son résultat* — et c'est précisément parce qu'une telle formule est exacte qu'elle est dangereuse : elle installe l'usage d'une clause que le contrôle suivant trouvera fausse ailleurs. Le **ch. 25** le montre à son journal, et le montre mieux que les cinq autres : la clause y était **exacte à son siège et fausse ailleurs**, le ch. 28 §28.3 citant quatre identifiants de vulnérabilité, ce que R-12 autorise expressément.

### 3.3 Trois sièges de la même classe ont été traités ailleurs, et sous un autre critère

**Constat sur pièce, hors du périmètre des passes du 22 juillet.** La même clause — l'attestation auto-délivrée du rédacteur sur R-12 — a été retirée de **trois pièces supplémentaires le 21 juillet 2026**, non par la passe CA-12 mais par leur **relecture adversariale CA-14** :

| Siège | Rang de la réfutation | Gravité déclarée | Formule retirée |
|---|---|---|---|
| **ch. 1 §1.2** | l'une des trois majeures | **MAJEUR** | « aucune séquence, aucune charge utile, aucune preuve de concept n'est reproduite ici » |
| **ch. 17** | n° 7 | **MAJEUR** | « cette pièce ne traite pas de matière offensive, et aucune attestation contraire n'y figure » |
| **ch. 19** | n° 7 | Mineure | « la pièce ne traite aucune matière offensive » |

⚠ **Les trois journaux invoquent CA-12 comme motif du retrait, alors que la lentille exercée était CA-14.** Le résultat est bon ; le **rattachement de critère** ne l'est pas, et la même classe se trouve ainsi comptée sous deux critères selon la passe qui l'a rencontrée. ⚠ **Une conséquence en découle sur les cardinaux** : le retrait du **ch. 1 §1.2** ne figure pas au résultat de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md), qui annonce **un** retrait — celui du ch. 15 §15.3. Les deux énoncés sont exacts à leur périmètre, et leur somme n'est pas lisible sans les distinguer. **Signalé, non corrigé** — cela relèverait des pièces et d'un rapport antérieur, hors du mandat de celui-ci.

**Bilan de la classe sur l'ensemble du volume, sièges recomptés un par un** : **quatorze retraits** — **un** le 21 juillet par CA-12 (ch. 15 §15.3), **trois** le 21 juillet par CA-14 sur motif CA-12 (ch. 1 §1.2, ch. 17, ch. 19), **huit** le 22 juillet par les passes reconstituées ici, **deux** le 22 juillet par CA-12 sur les rapports de lot (L-09 §E point 5, L-10 §E point 7). ⚠ **Ce bilan ne dit pas que la classe est épuisée** : il dit combien d'occurrences ont été vues. *Le ch. 28 et l'avant-propos ont été rédigés **après** le retrait du 21 juillet au ch. 1 §1.2 et ont réintroduit la même forme — une passe corrige les occurrences qu'elle voit d'une classe, non la classe.*

## 4. Ce qui a été conservé, et pourquoi

*Consigné parce qu'une relecture qui ne rapporte que ses trouvailles ne permet pas de juger de sa profondeur.*

**Six des huit sièges déclarent ce que le retrait a laissé en place ; les ch. 7 et ch. 8 n'en disent rien.**

| Pièce | Ce qui est conservé, selon le journal | Motif écrit |
|---|---|---|
| **ch. 10** | le refus de certifier, et l'attribution du contrôle à un relecteur distinct | Ce sont l'énoncé de la règle et le renvoi au contrôle ; seule l'attestation qui les suivait est retirée. **Aucun retrait au corps** |
| **ch. 14** | la description de la matière du chapitre | Elle se vérifie sur le §14.1. Seules la qualification que la pièce faisait d'elle-même au regard de R-12 et la **clause d'exclusivité** sur les quatre pièces de la Partie IV sont retirées — cette dernière n'étant portée par aucun compte rendu, celui du 21 juillet ne comparant pas les pièces entre elles |
| **ch. 15** | l'énoncé de la règle et le constat qu'il porte, dans la forme retenue au §15.3 par la passe du 21 juillet 2026 | La forme de remplacement est **reprise d'un précédent**, non réinventée : « le traitement défensif du volume tient l'exposé au niveau du maillon » |
| **ch. 25** | les deux passages décrivant une mécanique d'attaque (§25.2), tenus au niveau du maillon et rattachés à leur entrée de socle | Seule la clause qui **certifiait** ce que ces passages ne contenaient pas est retirée |
| **avant-propos** | le renvoi à R-12 et **la réserve sur le périmètre incomplet du compte rendu** | La proposition-titre et l'énumération d'absences sont remplacées par **l'énoncé du régime au registre du fait** — ce que la Partie IV décrit, non ce qu'elle s'abstient de décrire |
| **ch. 28** | l'identification du maillon et le renvoi à R-12 | Seul le membre final — « et c'est tout ce qui est écrit ici » — est retiré |

⚠ **Aucune tentative de dérivation n'est rapportée par les journaux du 22 juillet 2026.** Les deux passes antérieures en consignaient chacune une, avec son échec. *L'absence d'une telle tentative n'est pas l'échec d'une tentative : c'est une profondeur de contrôle qui n'est pas documentée.*

## 5. Ce que la couverture laisse — décompte re-mesuré

**Le second terme de CA-12 — « nommé dans la pièce qu'il couvre » — est tenu par 18 pièces sur 34.** Relevé conduit sur les **35 fichiers** de `monographie/` (34 pièces plus le registre de gel), fichier par fichier, par recherche du nom des deux comptes rendus déposés :

- **18 pièces** nomment au moins un compte rendu CA-12 ; **deux d'entre elles** — ch. 17 et ch. 18 — nomment en outre [`relecture-CA-12-lots.md`](relecture-CA-12-lots.md) ;
- **16 pièces n'en nomment aucun** : avant-propos, ch. 3, ch. 6, **ch. 7**, ch. 11, ch. 16, ch. 21, ch. 22, ch. 23, ch. 24, ch. 26, ch. 27, ch. 28, annexe B, annexe C, annexe D ;
- le **registre de gel** nomme les deux, mais il est un document de contrôle et non une pièce.

⚠ **Dix des seize sont des pièces de P4** — avant-propos, ch. 22, 23, 24, 26, 27, 28, annexes B, C, D —, que la passe du 21 juillet 2026 ne couvrait pas et pour lesquelles **aucun compte rendu n'avait été déposé depuis**. Les six autres sont des pièces du tronc.

⚠ **Le ch. 7 est le cas le plus défavorable du périmètre, et il cumule les deux manques** : il a subi un retrait, **il n'en porte aucun journal**, et **il ne nomme aucun compte rendu CA-12**. À la lecture de la pièce seule, rien n'indique qu'un contrôle de dualité d'usage l'ait jamais touchée.

☑ **Le dépôt du présent fichier ne corrige pas ce second terme.** Nommer ce rapport dans les trente-quatre pièces est un geste d'édition sur `monographie/`, **hors du mandat de la passe qui l'écrit** ; il est porté au §7.

## 6. La frontière du critère a bougé entre deux passes, et aucun arbitrage général ne l'a fixée

**C'est le constat le plus lourd de cette reconstitution, et il porte sur le critère, non sur les pièces.**

**Le 21 juillet 2026**, [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §5 examine l'annonce de régime du **ch. 12** — « chaque entrée nomme le maillon et la raison pour laquelle il cède, cite l'identifiant de vulnérabilité ou l'incident, **et s'arrête là** » —, la retient pour retrait, puis **la conserve** avec un motif écrit : elle appartient au registre de ce que le chapitre *fait*, non à celui de ce que son contenu *a été vérifié ne pas contenir*. Le compte rendu déclare la forme « discutable » et ouvre une remontée demandant au cadrage de statuer.

**Le 22 juillet 2026**, les passes reconstituées ici retirent **cinq propositions relevant de ce même registre** — celles qui portent sur ce que la pièce **ne contient pas** : ch. 7, ch. 8, ch. 25, avant-propos et ch. 28 §28.3 ; une sixième, au ch. 14, y participe pour moitié. Les deux autres retraits — ch. 10 et ch. 15 §15.2 — portent sur la **conformité** que la pièce s'attribue, forme que les deux lectures proscrivent également.

☑ **Deux des huit journaux ont vu la difficulté et l'ont écrite avant que ce rapport ne l'établisse.** L'avant-propos et le ch. 28 déclarent en toutes lettres que *« la frontière entre l'annonce de régime — admise le 21 juillet — et l'attestation d'observance — proscrite le 22 — n'a jamais été arbitrée »*, rendent leur correctif **« sous la lecture stricte du 22 juillet, retenue comme l'option la plus réversible »**, et le déclarent **révocable si l'auteur retient l'autre lecture**. Leur motif est solide et mérite d'être conservé : *un retrait se révoque par l'historique de version ; une attestation laissée en place ne se révoque pas.*

⚠ **La remontée du 21 juillet a été arbitrée, et son report n'a pas été opéré — les deux points sont constatés sur pièce, et le second est celui qui coûte.** [`remontees-gouvernance.md`](remontees-gouvernance.md), **R-G-33**, point 3 de l'arbitrage du 21 juillet 2026, prescrit : *« La forme d'annonce du ch. 12 est harmonisée sur celle des ch. 13 et 15 : le membre "et s'arrête là" est retiré »*, avec pour motif que *« la forme la plus sûre est celle qui ne dit rien de ce que la pièce a été vérifiée ne pas contenir »*. La section « Report » de la même remontée porte : **« ⚠ Non fait à la date de la présente consignation. »**

☑ **Constat du 22 juillet 2026** : le **ch. 12 porte toujours « et s'arrête là »** — occurrence unique, à l'ouverture du chapitre, vérifiée sur le fichier.

**Il en résulte une asymétrie qui n'est imputable à aucune passe prise isolément** : la seule occurrence dont le retrait ait été **expressément arbitré** subsiste, tandis que cinq propositions du même registre, qu'aucun arbitrage ne nommait, ont été retirées. *Un arbitrage rendu et non reporté ne laisse pas les choses en l'état : il laisse la règle s'appliquer partout sauf là où elle a été écrite.*

⚠ **Et l'arbitrage de R-G-33 est resté local — ce qui rend exacte, mais fragile, la formule des deux journaux.** R-G-33 tranche **une occurrence**, dans **une pièce** ; il n'écrit de frontière générale ni au PRD §8.5, ni au PRD §11, ni à §A.5. La formule « la frontière n'a jamais été arbitrée » est donc **exacte lorsqu'elle vise la règle générale**, et **fausse si on la lit comme visant la forme du ch. 12**, qui a bien été arbitrée le 21 juillet 2026. *Distinguer les deux n'est pas une subtilité : c'est la différence entre une question ouverte et un report non fait.* C'est cette absence de frontière **écrite au cadrage** qui a permis à deux passes d'exercer deux lectures du même critère à un jour d'intervalle. **Ouvert sous [R-G-53](remontees-gouvernance.md), réservé à l'auteur.**

## 7. Remontées ouvertes — aucune n'est opérée par la présente passe ([PRDPlan](../prd/PRDPlan.md) §5.3)

1. **Statuer sur la frontière du critère** (§6) — et, dans les trois branches possibles, **clore explicitement la remontée n° 2 de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §7**, dont l'arbitrage R-G-33 point 3 n'a pas été reporté. → **[R-G-53](remontees-gouvernance.md)**, auteur.
2. **Tenir le terme procédural de CA-12, ou l'amender.** Le présent rapport ne le tient qu'à moitié : il est **déposé**, il n'est **nommé dans aucune pièce**, et il est **reconstitué** plutôt que rendu par les passes. Les trois options sont posées à [`relecture-CA.md`](relecture-CA.md) §8 option B. ⚠ **Cette question n'a pas d'entrée propre au [registre](remontees-gouvernance.md)** : son inscription est déclarée due par [`relecture-CA.md`](relecture-CA.md) §6 point 1 et **n'est pas opérée ici**, la présente passe n'ayant ouvert que les cinq remontées **R-G-53** à **R-G-57**. *Le signaler coûte une phrase ; le taire laisserait le manque le plus lourd du critère sans siège.*
3. **Doter les ch. 7 et ch. 8 d'un journal de retrait** (§3.1), ou déclarer qu'un retrait sans journal est admissible. **Geste d'édition sur `monographie/`, hors du mandat de cette passe.**
4. **Trancher le rattachement de critère des retraits du ch. 17 et du ch. 19** (§3.3) : une même classe comptée sous CA-12 par une passe et sous CA-14 par une autre rend tout bilan de classe non comparable.
5. **Exécuter le contrôle de migration rapport → pièce.** Voir le §8, point 5 : l'énoncé absolu du compte rendu du 22 juillet 2026 sur les rapports de lot a été borné par la présente passe, mais **le contrôle général demeure dû**.

## 8. Ce que ce rapport ne dit pas

*Une passe qui ne borne pas son périmètre laisse croire qu'elle l'a couvert.*

1. **Il n'atteste la conformité d'aucune pièce à R-12**, et il n'atteste pas la sienne. **Aucune pièce n'a été relue sous la lentille de la dualité d'usage par la présente passe** : la question « un lecteur peut-il dériver une attaque de ce texte ? » n'y est pas posée une seule fois.
2. **Il n'a pas été rédigé par les passes qu'il décrit.** Il est reconstitué depuis leurs journaux et depuis le disque. *Il rapporte ce que les pièces déclarent d'elles-mêmes ; le critère demande le contraire.*
3. **Le périmètre de chacune des cinq passes déclarées n'est pas constatable** (§2). Ce qui est établi est l'ensemble des sièges touchés, non leur répartition, ni la couverture que chaque passe revendiquait, ni ce qu'elle a lu sans rien retirer.
4. **La distinction rédacteur / relecteur n'est constatable sur aucun fichier** — réserve 1 de **R-G-19**, non levée. Aucune conclusion n'en est tirée dans un sens ni dans l'autre.
5. **Aucun contrôle de migration rapport → pièce n'a été conduit par la présente passe.** ⚠ Un contrôle de cette nature **a existé**, borné : [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §4, entrée 6, établit que le verbatim tronqué à la relecture P1.4 **n'a pas migré** vers les pièces, pour le seul objet du verbatim et le seul siège du ch. 13 §13.1. **Le contrôle à titre général demeure dû**, et cette passe ne l'a pas conduit.
6. **Les huit retraits sont constatés appliqués ; rien n'établit qu'ils étaient les seuls dus.** Établir qu'aucune charge utile ne subsiste dans les trente-quatre pièces exigerait une relecture intégrale sous la lentille de R-12, **qui n'a eu lieu pour aucune pièce de P4** et qui demeure bornée, pour le tronc, aux quatre pièces intégrales et quatre sections du 21 juillet 2026.
7. **Aucune source primaire n'a été rouverte**, et **aucun rapport de lot n'a été ouvert** par cette passe.
8. **Aucune pièce, aucun rapport de lot et aucun document de gouvernance n'a été modifié par cette passe**, hors la correction d'un énoncé absolu de [`relecture-CA-12-lots.md`](relecture-CA-12-lots.md) §8 point 4 et l'inscription des remontées du §7 au registre.
9. **Le présent contrôle ne vaut qu'à sa date.** Toute reprise d'une pièce rouvre la question pour elle, et *une pièce relue ne le reste pas*.
