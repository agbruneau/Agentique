# Annexe A — Méthodologie de constitution du socle

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet, après relecture adversariale — 17 juill. 2026, relecteur distinct du rédacteur) |
| Date de gel de l'information | 17 juillet 2026 — faits chauds revalidés le jour même à leurs sources primaires (`verification/revalidation-2026-07-17.md`, P4.1 : aucun amendement matériel requis) |
| Socle mobilisé (PRD §7) | PRD Annexe A (méthode, passes, incident) ; PRD §7 chapeau (taxonomie des niveaux de preuve, numérotation, cardinal du socle) ; F-09 (épisode de marquage), F-26, F-27 (vérifications directes), F-35, F-46 (faits négatifs vérifiés ; F-46 aussi pour l'épisode « indépendantes »), F-36, F-37 (§10.10 — source unique), F-38 à F-46 (compléments hors passes), F-47, F-48 ([B/C mixte]) ; `verification/revalidation-2026-07-16.md` (passe P0) et `verification/revalidation-2026-07-17.md` (passe P4.1) |
| Garde-fous à surveiller (PRD §8) | §8.2 (attribution) ; **réserve F-09** (« attendu », jamais « exigé » ; jamais « fiche de modèle ») ; **§8.4** (neutralité fournisseur — IBM cité ici comme cas d'instanciation documenté) ; PRDPlan §4.4 (« Absence de documentation ≠ fait négatif vérifié » ; marqueur « Lecture de l'auteur ») |
| Volumétrie cible | ~1500 mots |

> **Thèse ([TOC.md](../../TOC.md))** : reprise lisible de la méthode de constitution du socle — passes de recherche, votes adversariaux, niveaux de preuve, incident et reprise —, pour que le lecteur puisse juger de ce que chaque affirmation de l'ouvrage porte, et de ce qu'elle ne porte pas.

---

Un ouvrage qui affirme doit dire comment il sait. Cette annexe expose la méthode par laquelle le socle factuel de cet ouvrage a été constitué, ce que ses niveaux de preuve signifient concrètement, et — la partie la plus utile — ce qu'elle ne garantit pas. Elle est écrite pour un lecteur qui n'a pas accès au cahier des charges du projet et n'a pas à en connaître.

## A.1 Ce qu'est le socle

Le socle est un corpus d'entrées numérotées `F-xx`. Chacune porte une affirmation, ses sources, son niveau de preuve et ses réserves. Toute affirmation factuelle centrale de l'ouvrage est adossée à l'une d'elles — c'est ce que signifient les identifiants qui parsèment les notes des vingt-quatre chapitres[^1].

Le socle compte **quarante-six entrées**, sous des identifiants allant de F-01 à F-48. La numérotation est discontinue et l'assume : **F-12, F-13 et F-14 ne sont pas attribués** — ces affirmations ont été fusionnées à des doublons sémantiques lors de la synthèse, et un identifiant déjà cité en référence croisée ne se renumérote pas. S'y ajoute une entrée dérivée, F-23b. Quarante-cinq identifiants attribués, plus un : quarante-six[^1].

## A.2 Trois passes, et ce qu'un vote adversarial veut dire

Le socle a été constitué en juillet 2026 par trois passes successives d'un harnais de recherche multi-agents. Chaque passe suit cinq étapes : décomposition en cinq angles (six pour la passe 3) ; recherche parallèle par angle ; extraction d'**affirmations falsifiables** des meilleures sources, avec déduplication des URL ; **vérification adversariale** — trois juges par affirmation, réfutation acquise à deux voix sur trois ; synthèse, fusion des doublons et classement par confiance[^2].

| Passe | Agents | Sources | Affirmations extraites | Soumises au vote | Confirmées | Réfutées |
|---|---|---|---|---|---|---|
| 1 (large) | 105 | 23 | 115 | 25 | 22 | 3 |
| 2 (comblement) | 107 | 25 | 124 | 25 | 25 | 0 |
| 3 (résiduelle, avec reprise) | 112 | 29 | 145 | 25 | 22 | 3 |
| **Total** | **324** | **77** | **384** | **75** | **69** | **6** |

Le chiffre à retenir n'est pas 324, ni même 69 : c'est **75 sur 384**. Le vote à trois juges coûte cher — un plafond budgétaire l'a borné aux quelque vingt-cinq affirmations les plus importantes de chaque passe. Les trois cent neuf autres n'ont pas été rejetées : elles n'ont pas été soumises à ce contrôle, et n'entrent donc pas au socle au niveau le plus élevé[^2].

## A.3 Les niveaux de preuve : [A] > [B] > [C]

Trois niveaux, dans un ordre strict[^3].

- **[A]** — l'affirmation a passé le **vote adversarial à 3-0** : trois juges ont cherché à la réfuter, aucun n'y est parvenu. C'est le niveau le plus élevé du socle.
- **[B]** — la **source primaire a été lue et extraite avec citation**, ou consultée directement, **sans vote adversarial**. L'affirmation est adossée au texte ; elle n'a pas été contestée.
- **[C]** — **repérage documentaire** : la source primaire est identifiée, son contenu n'a pas été extrait. Une entrée [C] **ne porte jamais un fait central** ; elle signale une piste, pas un acquis.

L'ordre est contre-intuitif, et il commande tout le reste. Une lecture directe d'un texte officiel vaut **moins** qu'un vote 3-0 — non que le texte officiel soit douteux, mais parce que la lecture n'a été relue par personne, quand l'affirmation votée a essuyé trois tentatives de réfutation. **Lecture de l'auteur** : le niveau ne mesure pas la qualité de la source ; il mesure **ce que l'affirmation a subi**. Le socle établit l'ordre et ce que chaque niveau exige ; cette manière de le résumer est une glose, pas une formule du PRD.

## A.4 L'incident de la passe 3, et sa trace durable

La première exécution de la passe 3 a été **interrompue à mi-vérification** par une limite de session : cinquante-six votes en erreur, synthèse échouée. La passe a été reprise par relecture du cache — les agents ayant réussi ont rejoué leurs résultats à l'identique — et s'est achevée sans erreur (112 sur 112)[^4].

La reprise a sauvé la passe, non son plan de vérification. **Les angles 3 à 6 de la passe 3 n'ont pas atteint le vote adversarial** : valeurs mobilières, Loi 25, institutions financières canadiennes hors socle initial, frameworks d'orchestration. C'est pourquoi les entrées **F-26 et suivantes portent leur niveau individuellement**, et pourquoi une part notable des Parties **II, III et V** repose sur du [B] ou du [C] plutôt que sur du [A][^4]. La Partie IV est le contre-exemple exact, et il vaut d'être dit : l'incident l'a épargnée — ses entrées porteuses sont **toutes [A]**[^4]. Entre l'interruption et la reprise, deux faits réglementaires porteurs ont été vérifiés directement à leur source officielle — l'article 12.1 de la Loi 25 sur LégisQuébec et l'avis 11-348 des ACVM sur osc.ca —, ce qui les établit au niveau [B][^5].

Trois compléments hors passes ont ensuite enrichi le socle, dont deux entièrement au niveau [B] : deux articles académiques lus intégralement (F-36, F-37) ; quatre recherches ciblées sur le portefeuille d'intégration instancié en Partie VII (F-38 à F-46). Le troisième est une passe d'élévations **partielles** — le 16 juillet 2026, neuf recherches, explicitement **sans vote adversarial**, « meilleur effort borné » d'une passe par lacune : elle a produit deux entrées **[B/C mixte]** (F-47, F-48), dont les résidus restent [C], et des échecs d'élévation restés [C] eux aussi (§A.6)[^6].

## A.5 Les épisodes F-09 et F-46 : ce que la méthode attrape

Le 16 juillet 2026, le texte intégral de la ligne directrice E-23 du BSIF a été lu et extrait, en anglais et en français, et ses exigences opératoires versées à l'entrée F-09. L'opération a été consignée comme une **« élévation [C]→[B] »**. Elle était **doublement fausse** : l'entrée n'avait jamais été [C] — ses faits issus des passes 1-2 étaient [A] —, et [B] est **sous** [A] dans la taxonomie ci-dessus. Une extraction de source primaire ne « relève » pas une entrée déjà votée 3-0 : elle l'**enrichit d'un contenu de niveau inférieur**. La faute a été relevée par la rédaction du chapitre 18, et l'entrée porte désormais le marquage **[A/B mixte]**, ses deux strates distinguées ligne à ligne[^7].

La même extraction a réfuté deux formulations que le projet portait depuis l'origine : E-23 est **fondée sur des principes** et rédigée au conditionnel (« *should* ») — d'où « **attendu** par E-23 », jamais « exigé » ; et elle n'emploie nulle part « fiche de modèle » (*model card*), zéro occurrence dans les deux langues — c'était prêter au régulateur un vocabulaire qui n'est pas le sien. La correction a dû être répercutée sur dix chapitres[^7].

Le même dispositif a fait une seconde prise, de la même classe. L'entrée F-46 portait que trois sources **indépendantes** convergeaient sur l'encadrement déterministe — argument d'autant plus fort qu'il reposait sur cette indépendance. Le socle la réfutait lui-même : la même chercheuse cosigne F-36 et F-37, et IBM Research figure parmi les auteurs de F-36 quand IBM publie F-46. L'adjectif a été **retiré** du PRD. Deux convergences fabriquées, deux fois attrapées — non par une intuition, mais parce que le socle était assez explicite sur ses propres sources pour se contredire[^7b].

Ces épisodes sont le meilleur argument de cette annexe, et ce n'est pas un paradoxe. La méthode n'a pas empêché les fautes : elle les a rendues **détectables** — chaque entrée porte son niveau et ses sources, chaque chapitre est relu contre le socle par un relecteur distinct de son rédacteur, et un rédacteur ne corrige jamais le socle : il remonte l'écart.

## A.6 Les échecs d'élévation, exposés plutôt que comblés

Une passe de recherche peut échouer. La règle du projet est alors de le dire, non de combler.

Le cas documenté est celui du lien entre une solution de messagerie financière et la norme ISO 20022. La passe du 16 juillet 2026 a confirmé que le produit est actif et que le lien existe — mais par la seule citation d'un ouvrage de référence de 2016, soit le niveau de preuve de l'entrée qu'il s'agissait d'élever ; la documentation courante refuse l'accès aux outils automatisés. **L'entrée reste [C]**, la lacune est exposée au chapitre 24, et une relecture humaine est recommandée avant publication[^8]. Deux autres élévations ont échoué de même et sont restées [C] : un facteur de risque déclaré au rapport annuel d'une banque, une famille d'agents chez un assureur[^8]. Aucune n'a été comblée par une source secondaire.

## A.7 Ce que la méthode ne garantit pas

Sept limites, énoncées sans atténuation. La première est la plus lourde, et c'est celle qu'un auteur a le moins envie d'écrire.

1. **La charpente conceptuelle de trois parties sur sept repose sur une source unique.** La taxonomie OO1–OO4, qui structure les Parties II, VI et VII, vient d'un **préprint v1 non révisé par les pairs**, sans reproduction indépendante ni application documentée à un processus d'institution financière — le PRD l'inscrit lui-même en lacune ouverte. Ce n'est pas une réserve de détail : c'est l'ossature de l'argument architectural de l'ouvrage qui tient à un seul article, dont les auteurs déclarent eux-mêmes des menaces à la validité. Les chiffres empiriques de cette source sont cités comme illustration, jamais comme preuve ; le cadre conceptuel, lui, porte l'ouvrage[^12b].
2. **Le socle est borné par ce qui a été lu.** Quand cet ouvrage écrit « le socle ne documente pas X », il énonce une **absence de documentation dans son propre corpus**, non un fait négatif vérifié. L'expression « **fait négatif vérifié** » est réservée aux cas où l'absence a été établie par balayage documenté : aucun standard technique désigné dans le cadre bancaire (F-35) ; aucune occurrence d'« agentique », « agent » ou « orchestration » dans E-23 (F-09) ; aucune architecture agentique sectorielle chez l'éditeur du cas d'instanciation (F-46). La distinction décide de ce qu'une institution peut inscrire dans un dossier de diligence raisonnable[^9].
3. **« Confirmé » ne veut pas dire « vrai »**, mais : corroboré par les sources citées, à la date indiquée — ni garanti pérenne, ni indépendant de ces sources. La méthode vérifie qu'une source **dit** X, pas que X est vrai : les métriques auto-déclarées — d'institutions, d'éditeurs, de fondations, d'études d'analystes commandées — restent auto-déclarées après vérification, d'où leur attribution nominative à chaque occurrence dans tout l'ouvrage[^10].
4. **Le vote 3-0 n'a couvert qu'une fraction des affirmations** (§A.2), et l'incident de la passe 3 a privé du vote des pans entiers du domaine réglementaire et institutionnel (§A.4).
5. **Des sources primaires sont restées inaccessibles** aux outils : pages refusant les robots, contenus rendus par script, fichiers trop volumineux. Le recoupement par miroirs est documenté à chaque fois, mais reste un pis-aller[^10].
6. **Le projet s'est trompé, trois fois documentées, et rien ne dit que ce soit tout.** Une **hallucination** a été détectée et écartée en cours de passe — un résumé de recherche affirmait l'existence d'un paquet logiciel qu'aucune source primaire ne corroborait[^11] ; et **deux convergences fabriquées** ont été attrapées, toutes deux dans la même classe d'erreur — une élévation de F-09 annoncée à l'envers de la taxonomie (§A.5), et l'« indépendance » des trois sources de F-46, que le socle réfutait lui-même (§A.5). Les trois ont été prises. Rien n'établit que ce soit le compte complet : ce qui est démontré, c'est que le dispositif attrape des fautes de ce genre, pas qu'il les attrape toutes.
7. **Le socle est daté.** C'est l'objet de la section suivante.

## A.8 La date de gel, et la péremption par morceaux

Chaque chapitre porte une **date de gel de l'information**. Elle ne dit ni quand le chapitre a été écrit, ni quand le lecteur le lit : elle dit **jusqu'à quelle date ses sources ont été consultées**. Au-delà, l'ouvrage ne sait rien.

La conséquence est plus intéressante que la convention. Le domaine évolue par trimestres, mais pas partout au même rythme : une chronologie protocolaire vieillit d'une révision de spécification à l'autre, quand un article de loi en vigueur depuis 2023 ne bouge pas. **L'ouvrage ne se périme donc pas d'un bloc : il se périme par morceaux, à des rythmes différents.** Le registre des dates de gel figure en `99-registre-gel.md` ; les conditions d'une revalidation sont traitées au chapitre 24[^12].

Une date de gel qui ne serait pas vérifiée ne vaudrait rien, et il faut donc dire ce qui la porte. Deux **passes de revalidation** ont rouvert les sources sur les faits déclarés sensibles au temps : le 16 juillet 2026 (neuf recherches ciblées), puis le 17 juillet 2026 — **revalidation finale avant publication**, huit faits chauds revérifiés à leurs sources primaires, verdict **« aucun amendement matériel requis »**. C'est cette seconde passe qui autorise la date de gel portée par cette annexe et par la chronologie de l'annexe C. Une passe qui ne trouve rien n'est pas une passe inutile : c'est la seule qui permette d'écrire une date sans la supposer[^13].

**Lecture de l'auteur** — ce que cette méthode achète n'est pas la certitude ; c'est la **traçabilité de l'incertitude**. Pour chaque affirmation, le lecteur peut savoir ce qui la porte, à quel niveau, à quelle date, et jusqu'où elle porte. C'est moins que ce que le ton d'un ouvrage de référence laisse d'ordinaire entendre. C'est tout ce qu'un corpus daté peut honnêtement offrir.

---

## Notes

[^1]: PRD §7, chapeau (taxonomie des niveaux de preuve ; « numérotation discontinue assumée » — F-12 à F-14 non attribués, fusions lors de la synthèse ; non-renumérotation des identifiants existants) ; PRD §11, **CA-1** (traçabilité). Le total est celui que **PRD §7 publie désormais lui-même** — « Cardinal du socle — recompté le 17 juillet 2026 : le socle compte 46 entrées » —, avec sa commande de recomptage et l'avertissement sur le piège du cardinal dérivé d'une borne d'identifiants : F-01 à F-11 = 11 ; F-15 à F-48 = 34 ; plus F-23b = **46**. Recompté ici contre cette source le 17 juillet 2026.

[^2]: PRD Annexe A (protocole des trois passes et tableau des volumes) ; en-tête du PRD (corpus : 77 sources, 384 affirmations extraites, 69 confirmées 3-0, 6 réfutées). Les totaux du tableau ci-dessus sont la somme des trois lignes de PRD Annexe A, recalculée le 17 juillet 2026.

[^3]: PRD §7, chapeau — **définit** les trois niveaux ([A], [B], [C]) sans les ordonner ; PRD §10, clause finale (« les entrées de niveau [C] ne peuvent porter un fait central sans élévation préalable »). **L'ordre strict [A] > [B] > [C] est établi par F-09**, non par le chapeau : « [B] est **sous** [A] », l'extraction primaire enrichissant une entrée votée « d'un contenu de niveau **inférieur** dans la taxonomie §7 » (PRD §7.3, rectification du 16 juill. 2026 ; repris à CLAUDE.md).

[^4]: PRD Annexe A, « Incident de la passe 3 » (56 votes en erreur, reprise sur cache, 112/112) et « Limites » (les angles 3 à 6 de la passe 3 n'ont pas atteint le vote adversarial et sont couverts par extraction primaire [B] ou repérage [C]) ; PRD §7, chapeau (« les niveaux des entrées F-26 et suivantes sont indiqués individuellement »). **Cartographie des angles privés de vote sur les parties (PRD §6)** : ACVM et Loi 25 → Partie III (F-26, F-27) ; BMO/CIBC/BNC/Sun Life/Intact → Partie V (F-47, F-48) ; LangGraph/CrewAI/Temporal/Confluent → **Partie II** (F-32, F-33). **Partie IV épargnée** : son socle (F-11, F-23, F-28, F-29, F-34, F-35 — PRD §6) est intégralement [A], F-28/F-29/F-34/F-35 par marquage explicite, F-11 et F-23 par la phrase de portée générale du chapeau de §7 (« les entrées F-01 à F-25 sont toutes de niveau [A] », F-09 excepté).

[^5]: PRD §7.3, **F-27** (art. 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé, texte officiel consulté sur legisquebec.gouv.qc.ca) et **F-26** (avis ACVM 11-348, consulté sur osc.ca) — niveau [B] par consultation directe, PRD Annexe A.

[^6]: PRD Annexe A, compléments v1.1 (deux articles académiques lus en texte intégral — PRD §7.7, **F-36** et **F-37**), v1.2 (quatre recherches ciblées sur sources primaires — PRD §7.8, **F-38 à F-46**) et P0 (neuf recherches ciblées, sans vote adversarial) ; PRDPlan §2 (règle du « meilleur effort borné ») ; rapport `verification/revalidation-2026-07-16.md`. **Neutralité fournisseur (PRD §8.4)** : le portefeuille documenté en F-38 à F-46 est un **cas d'instanciation documenté par sources primaires**, jamais une recommandation.

[^7]: PRD §7.3, **F-09** — entrée **[A/B mixte]**, marquage rectifié le 16 juillet 2026 ; strate [A] : faits des passes 1-2 (vote 3-0) ; strate [B] : exigences opératoires extraites du texte intégral d'E-23 (osfi-bsif.gc.ca, versions EN et FR) et lettre d'accompagnement du 11 septembre 2025. Détection par la rédaction du chapitre 18 : PRDPlan §1.4, lignes « ch. 18 » et « Correction de la cascade F-09 » (étendue réelle : dix chapitres). Formulations imposées (« attendu » vs « exigé » ; « documentation de modèle » et « inventaire » plutôt que « fiche de modèle ») : PRDPlan §4.4.

[^7b]: PRD §7.8, **F-46** — adjectif « indépendantes » **retiré au PRD v1.5** (16 juill. 2026, retours de P2), « réfuté par le socle lui-même » : Rinderle-Ma cosigne F-36 et F-37 ; IBM Research est parmi les auteurs de F-36 et IBM publie F-46. Détection : relecture adversariale de P2 (105 réfutations bloquantes sur 16 chapitres) ; PRD, table de version (v1.5).

[^8]: `verification/revalidation-2026-07-16.md`, P0.2 n° 4 (échec d'élévation documenté — le lien n'est confirmé que par un ouvrage de référence de 2016, de même niveau de preuve que l'entrée à élever ; documentation courante inaccessible aux outils, 403) et P0.2 n° 1 et n° 2 (résidus [C] : facteur de risque matériel au rapport annuel 2025 de BMO — **F-47** ; agents d'adhésion, de relevés fiscaux et de réclamations chez Sun Life — **F-48**) ; PRD §10.2 et §10.6 ; PRDPlan §2 (« l'échec d'élévation ne bloque pas la suite »).

[^9]: PRDPlan §4.4, ligne « **Absence de documentation ≠ fait négatif vérifié** » (formule de distinction imposée) ; faits négatifs établis par balayage documenté : PRD §7.4 **F-35** (recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI », « OAuth » dans les textes officiels : zéro occurrence), §7.3 **F-09** (vérification négative mécanique sur le texte intégral EN et FR : « agentique »/« agentic » = 0, « agent(s) » = 0, « orchestration » = 0 ; « autonom\* » = 8), §7.8 **F-46** (aucune architecture agentique sectorielle publiée — vérifié introuvable sur les deux canaux de l'éditeur).

[^10]: PRD Annexe A, « Limites » (« "confirmé" signifie corroboré par les sources citées à la date indiquée, pas garanti pérenne ») ; PRD §8.2 (règles d'attribution des métriques auto-déclarées et des études d'analystes commandées) ; PRD §13 (risque « sources primaires inaccessibles aux robots (403/JS) » et sa mitigation par doubles références documentées).

[^11]: `verification/revalidation-2026-07-16.md`, « Limites de cette passe » — hallucination détectée et écartée, non retenue au PRD.

[^12b]: PRD **§10.10**, lacune ouverte le 16 juill. 2026 : « la **taxonomie OO1–OO4, qui structure les Parties II, VI et VII**, repose sur **une source unique**, préprint v1 non révisé par les pairs, sans reproduction indépendante ni application documentée à un processus d'institution financière » ; PRD §7.7, **F-37** (Rinderle-Ma, Mangler et al., arXiv:2606.31518v1, 30 juin 2026 — réserves déclarées par les auteurs : expériences initiales, prompts non comparés, facteurs confondants ; « citer le cadre conceptuel comme référence, les chiffres comme illustration seulement »).

[^12]: PRD §8.3 (sensibilité temporelle : « chaque chapitre porte une date de gel de l'information ») ; PRD §11, **CA-4** (datation) ; PRDPlan §4.2 (boucle qualité — date de gel à la rédaction, registre à la fusion) ; registre complet : `monographie/99-registre-gel.md` ; conditions de revalidation : chapitre 24.

[^13]: `verification/revalidation-2026-07-16.md` (P0.1/P0.2, neuf recherches ciblées) et `verification/revalidation-2026-07-17.md` (**P4.1, revalidation temporelle finale avant publication** — périmètre : faits chauds de PRD §8.3 et points ouverts du registre de gel ; méthode : consultation directe des sources primaires, une passe, sans vote adversarial ; verdict : **« PRD amendé : Non — aucun amendement matériel requis »**) ; PRDPlan §3, ligne P4.1. Le rapport note lui-même que « la stabilité générale constatée est le résultat attendu ; aucune évolution n'a été recherchée pour justifier la passe ».

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 17 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait — voir auto-contrôle ci-dessous
     3. Balayage garde-fous ...... fait — voir ci-dessous
     4. Relecture adversariale ... FAITE (17 juill. 2026, relecteur distinct du rédacteur). Neuf constats
                                   appliqués : note [^1] fausse (le PRD §7 énonce désormais son cardinal) ;
                                   « tous au niveau [B] » contredit par F-47/F-48 [B/C mixte] ; « Parties III
                                   à V » → « II, III et V » (la Partie IV est intégralement [A]) ; §A.7
                                   taisait §10.10 et l'épisode F-46 ; asymétrie sur la relecture ; « 13 notes »
                                   → 12 ; décompte de mots sur commande périmée ; sourçage de l'ordre strict ;
                                   P4.1 non citée. ⚠ Le §A.5 affirmait au lecteur que « chaque chapitre est
                                   relu par un relecteur distinct », contrôle dont CETTE annexe était exemptée
                                   — l'exemption n'étant déclarée qu'ici, invisible au lecteur. L'asymétrie
                                   est levée par le fait, pas par une reformulation.
     5. Commit + registre de gel . à faire par le parent (annexe, pas chapitre : le registre `99-registre-gel.md`
                                   ne comporte à ce jour que des lignes de chapitres — voir gouvernance (G5))

     PASSE CORRECTIVE — AUDIT DU 17 JUILL. 2026 (`audit.md`, constat m-40), relecteur distinct :
       · UN constat, appliqué : le décompte de mots attesté en (c) était **faux de 3** (2043 certifié,
         2046 mesuré). Cause identifiée par l'audit et confirmée ici : le corps a été modifié APRÈS
         la mesure, dans le même commit (titre §A.5 « L'épisode F-09 » → « Les épisodes F-09 et
         F-46 »), sans re-mesure. Corrigés du même coup : les deux cardinaux DÉRIVÉS du chiffre faux
         — l'écart de la relecture (+460 → **+463**) et la demande G4 au TOC (« 2 043 » → **2 046**).
       · Aucune modification du CORPS : la valeur mesurée est donc inchangée à 2046 après cette
         passe, et c'est ce chiffre — mesuré en dernier, sur l'état livré — qui est porté ci-dessous.
       · Date de gel INCHANGÉE (17 juillet 2026) : la passe ne rouvre aucune source.

===============================================================================
(a) AUTO-CONTRÔLE DE TRAÇABILITÉ (CA-1, CA-3, CA-5)
===============================================================================

Aucune affirmation factuelle sans trace : **15 notes** (recomptées à la relecture du 17 juill. 2026 —
15 définitions, 15 appariées, bijection vérifiée), toutes renvoyant au PRD (Annexe A, §7, §8, §10, §11, §13),
à PRDPlan (§1.4, §2, §3, §4.2, §4.4) ou aux rapports `verification/revalidation-2026-07-16.md` et
`verification/revalidation-2026-07-17.md`. Aucune source externe nouvelle n'est introduite par cette annexe :
elle ne fait que rendre lisible ce que le PRD établit.
  ⚠ Le premier jet de ce bloc annonçait « 13 notes » pour **12** réelles (12 définitions, 12 appels, bijection
  correcte — seul le cardinal était faux). Le bloc qui certifie les cardinaux portait donc lui-même un cardinal
  faux, et il ne figurait pas dans sa propre liste de recomptes ci-dessous. Trois notes ont été ajoutées par la
  relecture ([^7b] épisode F-46 ; [^12b] lacune §10.10 ; [^13] passe P4.1) : 12 + 3 = **15**.
  Commande : grep -cE '^\[\^[0-9a-z]+\]:' FICHIER -> 15 ; appels distincts hors définitions -> 15.

CARDINAUX — tous recomptés le 17 juillet 2026 contre leur source, aucun repris de mémoire ni du brief :
  · « quarante-six entrées » ...... RECOMPTÉ sur PRD §7 : F-01..F-11 = 11 ; F-15..F-48 = 34 ; + F-23b = 46.
                                    Commande : grep -cE '^\- \*\*F-(0[1-9]|1[01]) ' PRD.md          -> 11
                                               grep -cE '^\- \*\*F-(1[5-9]|[2-4][0-9]) ' PRD.md     -> 34
                                               grep -cE '^\- \*\*F-23b' PRD.md                       -> 1
                                    ⚠ LE BRIEF ANNONÇAIT 48 — CHIFFRE FAUX, NON REPRIS. Voir gouvernance (G1).
  · 324 / 77 / 384 / 75 / 69 / 6 .. RECALCULÉS depuis le tableau de PRD Annexe A (105+107+112 ; 23+25+29 ;
                                    115+124+145 ; 25×3 ; 22+25+22 ; 3+0+3). Concordent avec l'en-tête du PRD.
  · « trois cent neuf » ............ 384 − 75 = 309. Dérivé, recompté.
  · 56 votes en erreur / 112 sur 112 / cinq étapes / cinq angles (six pour la passe 3) / trois juges / 2 sur 3
                                    ... tous lus dans PRD Annexe A, non dérivés.
  · « dix chapitres » (cascade F-09)  PRDPlan §1.4, ligne « Correction de la cascade F-09 » — cité, non recompté
                                    (le PRDPlan énonce lui-même « 10 chapitres, pas 6 »).
  · « vingt-quatre chapitres » ..... TOC.md / PRDPlan §1.4.
  · « Sept limites » (§A.7) ........ RECOMPTÉ après relecture : 7 items numérotés (la source unique de la
                                    taxonomie OO1–OO4 — §10.10 — ajoutée en tête). Trajectoire de ce cardinal :
                                    « Sept » au premier jet (faux), « Six » après fusion des items 2 et 3
                                    (juste), « Sept » de nouveau depuis l'ajout (juste). ✔
  · « Trois compléments hors passes » recompté : v1.1 (articles), v1.2 (portefeuille), P0 (revalidation). ✔
                                    ⚠ Le cardinal est juste, la QUALIFICATION ne l'était pas : « tous au
                                    niveau [B] » est faux du troisième — P0 a produit F-47 et F-48 en
                                    **[B/C mixte]** (vérifié au PRD §7.5 le 17 juill. 2026) et des échecs
                                    d'élévation restés [C] (§A.6, que l'annexe racontait deux paragraphes plus
                                    loin en se contredisant). Corrigé : « dont deux entièrement au niveau [B] ».
  · « deux convergences fabriquées » (§A.7 item 6) : F-09 (élévation annoncée à l'envers de la taxonomie) et
                                    F-46 (« indépendantes » retiré au PRD v1.5). 2. ✔ Avec l'hallucination
                                    de [^11] : « trois fois documentées ». ✔
  · « Trois niveaux » (§A.3) ....... PRD §7 chapeau. ✔
  · « deux formulations réfutées » .. PRD §7 F-09 + PRDPlan §1.4 P0.5 (« should » ; « fiche de modèle »). ✔
  · « Deux autres élévations » (§A.6) revalidation P0.2 n° 1 (BMO) et n° 2 (Sun Life) — 2. ✔

CA-5 (bilinguisme) : un seul terme anglais mobilisé, « fiche de modèle (*model card*) », attesté verbatim au
socle (F-09). Aucune traduction inventée — conformément à PRD §10.9 (« aucune traduction à inventer »), les
termes dont le socle n'établit pas l'original anglais ne sont pas anglicisés ici. Citations en langue originale :
« *should* », « *model card* ».

===============================================================================
(b) POINTS DE GOUVERNANCE REMONTÉS AU PARENT (non corrigés par moi — PRDPlan §4.2, règle d'escalade)
===============================================================================

G1. ✔ **ACCOMPLI — DÉCOMPTE DU SOCLE : 46, PAS 48.** Le brief de rédaction annonçait « 48 entrées ».
    L'annexe a écrit **46** et demandé que le PRD publie son propre total. **PRD §7 le porte désormais**
    (v1.8, 17 juill. 2026) : « Cardinal du socle — recompté le 17 juillet 2026 : le socle compte 46
    entrées », avec la commande de recomptage ET l'avertissement sur le piège (« ne jamais dériver le
    cardinal d'une borne d'identifiants » — le total et le plus haut identifiant ont coïncidé jusqu'en P0,
    ce qui rendait l'erreur indétectable). Le PRD note que **deux rédactions l'ont signalé
    indépendamment**. La note [^1] renvoie maintenant à ce cardinal publié, au lieu d'affirmer que le PRD
    ne l'énonce pas — ce qui était devenu faux. PLUS RIEN À DEMANDER.

G2. ✔ **ACCOMPLI — CLAUDE.md rectifié.** Il écrivait « entrées **F-01 à F-46** », ignorant F-47 et F-48.
    Il porte désormais « Socle factuel (§7, **46 entrées — identifiants F-01 à F-48**, F-12 à F-14 non
    attribués, plus F-23b) », l'ordre **[A] > [B] > [C]** explicite, la règle « une extraction primaire
    n'élève pas une entrée déjà votée 3-0 » et l'avertissement sur le cardinal dérivé. Vérifié le
    17 juill. 2026. PLUS RIEN À DEMANDER.

G3. **PRD Annexe A ne dit pas ce que la rédaction a appris.** L'Annexe A du PRD est un journal de méthode
    d'avant la rédaction : elle ignore (i) l'épisode de marquage de F-09 (consigné en §7.3 et PRDPlan §1.4,
    pas en Annexe A), (ii) la règle « une extraction primaire n'élève pas une entrée votée 3-0 » — qui est
    pourtant une **règle de méthode**, à sa place naturelle en Annexe A plutôt que noyée dans une entrée.
    → Action suggérée : ajouter à PRD Annexe A un paragraphe « Corollaire de la taxonomie » énonçant la règle
      une fois pour toutes. NON FAIT PAR MOI.

G4. ✔ **ACCOMPLI — volumétrie des annexes portée au TOC.** Le tableau des annexes de **TOC v1.4** porte
    désormais une colonne de volumétrie (cible → mesure), et sa note (3) tranche le fond : le bloc
    « Annexes A–D » est budgété à 6 000 mots au total ; **la ventilation par annexe (~1 500) « n'existait
    que dans les gabarits et n'a jamais eu force de cible »** ; « un écart se documente, il ne se corrige
    pas par amputation d'une réserve » (PRDPlan §1.1). La demande est honorée et l'arbitrage rendu.
    ⚠ RESTE, ET CE N'EST PAS À CETTE ANNEXE DE LE CORRIGER : la ligne « Annexe A » du TOC porte
    « ~1 500 → **1 689** (+12,6 %) », chiffre issu de la commande `sed` maison, périmée — voir (c). Mesure
    de référence : **1 583** avant relecture, **2 046 après** (chiffre re-mesuré le 17 juill. 2026 —
    cette demande portait « 2 043 », dérivé de l'attestation fausse du constat m-40 : une demande de
    rectification chiffrée est du contenu, elle se re-mesure comme le reste).
    → DEMANDE : rectifier la ligne (version++).

G5. **Le registre de gel n'a pas de ligne d'annexe.** `99-registre-gel.md` est structuré « une ligne par
    chapitre fusionné » (PRDPlan §4.2.5). Or les annexes portent elles aussi une date de gel (celle-ci :
    17 juill. 2026) et la même exigence CA-4 (« chaque chapitre porte sa date de gel »).
    → Action suggérée : trancher — soit le registre accueille les 4 annexes + l'avant-propos (et son en-tête
      le dit), soit CA-4 est explicitement borné aux 24 chapitres. En l'état, l'annexe A est gelée mais
      non enregistrable sans forcer le gabarit du registre. NON FAIT PAR MOI.

G6. ✔ **ACCOMPLI — PRDPlan §1.4 rectifié.** Il annonçait « 29 unités de rédaction ; 0 rédigée, 1 amorcée »
    quand le même tableau portait ☑ sur les 24 chapitres. Il porte désormais (revérifié le 17 juill. 2026) :
    « 24 chapitres + avant-propos + 4 annexes = **29 unités** ; **24 rédigées**, **4 en cours** (annexes
    A, B, C, D), **1 à faire** (avant-propos) », avec l'aveu explicite : « Un statut qui ment est pire qu'un
    statut absent : c'est la règle de ce tableau, et il l'a lui-même enfreinte pendant deux phases. »
    PLUS RIEN À DEMANDER.

G7. ✔ **FAIT — relecture adversariale exécutée** le 17 juill. 2026 par un relecteur distinct du rédacteur
    (PRDPlan §4.2.4), avec exactement les cibles annoncées ici : le §A.7 et le décompte de G1. Neuf constats,
    tous appliqués — détail en tête de ce bloc. Deux tenaient à ce que l'annexe **taisait** plutôt qu'à ce
    qu'elle affirmait (§10.10 ; l'épisode F-46) : une annexe de méthode se juge autant sur ses silences.

===============================================================================
(c) DÉCOMPTE DE MOTS
===============================================================================

Commande de référence, SEULE AUTORITÉ (PRDPlan §4.2, fixée le 17 juill. 2026) — exécutée, non estimée :

  awk '/^---$/{f=1;next} /^## Notes/{exit} /^<!--/{exit} f' monographie/90-annexes/annexe-a-methodologie.md \
    | tr -s '[:space:]' '\n' | grep -cE '[[:alnum:]]'

  Résultat : **2046 mots** (fichier tel que livré, après les correctifs de la relecture adversariale,
  RE-MESURÉ le 17 juill. 2026 sur l'état courant — audit du 17 juill. 2026, constat m-40).
  Mesure du même corps AVANT ces correctifs : **1583**. Cible indicative du gabarit : ~1 500.

  Honnêteté du décompte (le point compte plus que le chiffre) :
   · Ce bloc a publié DEUX commandes fausses de suite sur le même corps. (i) Le premier jet annonçait
     « 1497 mots » AVANT exécution, sur une commande `sed` dont la borne de fin ne matchait aucune ligne :
     la plage courait jusqu'à EOF et retournait 3664. Le chiffre annoncé était une invention. (ii) Sa
     correction — « 1689 mots, +12,6 % » — était mesurée, mais avec une commande **maison** : `wc -w`
     comptait les marqueurs Markdown collés et les `|` du tableau de §A.2. La vraie mesure du même corps
     était **1583 (+5,5 %)**, soit un écart deux fois moindre. La leçon tirée alors — « un décompte
     s'exécute, il ne s'estime pas » — était juste ; la commande ne l'était pas. Il y manquait le second
     versant : un décompte s'exécute **avec la commande qui fait autorité**, pas avec la sienne. Depuis le
     17 juill. 2026, PRDPlan §4.2 en fixe une, et déclare les commandes maison périmées.
   · **TROISIÈME chiffre faux sur le même corps, et le pire des trois** (audit du 17 juill. 2026,
     constat m-40). Ce bloc a certifié « **2043** mots » là où la commande de référence en mesure
     **2046**. Cette fois la commande était la bonne et la mesure avait été exécutée : c'est le
     FICHIER qui a bougé après elle. Le titre de §A.5 est passé de « L'épisode F-09 » à « Les
     épisodes F-09 et F-46 » — et le corps a suivi — dans le MÊME commit, sans re-mesure. Les deux
     premières fautes portaient sur la commande ; celle-ci porte sur son MOMENT. Une mesure n'est
     pas un acquis : elle date du texte qu'elle a lu, et toute retouche postérieure la périme.
     Le chiffre ci-dessus est re-mesuré sur l'état courant, après les corrections de cette passe.
     La leçon est complète, et elle a coûté trois passages : un décompte s'exécute (i), avec la
     commande qui fait autorité (ii), **et en dernier** (iii).
   · **L'« arbitrage à confirmer » du premier jet — couper §A.2 si la cible est ferme — est sans objet**,
     deux fois : il portait sur un écart mesuré faux, et TOC v1.4 a depuis déclaré la ventilation ~1 500
     sans force de cible (G4).
   · L'écart s'est creusé, et c'est le résultat attendu : les correctifs de la relecture **ajoutent** de la
     substance (+463 mots — la source unique de la taxonomie OO1–OO4, l'épisode F-46, la passe P4.1 ;
     2046 − 1583, recalculé le 17 juill. 2026 : l'écart était annoncé à +460, dérivé du 2043 faux). Trois
     ajouts qui portent des limites et des prises du dispositif, c.-à-d. la valeur propre de cette annexe.
     PRDPlan §4.2 : « un écart se documente, il ne se corrige pas par amputation ». Il est documenté ici, et
     remonté au TOC (G4). Calibrage : ch. 21 et ch. 24 sont à +10 % ; cette annexe est au-delà, et l'assume.
-->
