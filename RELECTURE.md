# Relecture humaine externe — consigne

*Établie le 15 septembre 2026 : tâche T5.1 du [plan d'exécution](<Plan d'exécution — évaluation académique.md>), pour
la part qui ne dépend d'aucun tiers. Elle répond à la condition bloquante B1 et à la critique de fond n° 1 de
l'[évaluation du même jour](<Évaluation académique.md>). Rédigée par un agent de modèle (Claude Opus 5, bâtisseur M6
de la boucle du 15 septembre 2026) ; aucun humain ne l'a relue. **Rien n'est envoyé à cette date : les relecteurs ne
sont pas nommés** — décision d'auteur DA-4, non tranchée —, et chaque case que cela laisse vide le dit.*

**En bref, pour le relecteur.** Vous recevez une pièce et une liste d'énoncés centraux, chacun avec ses pages. Votre
tâche est de les **réfuter** : pour chaque objection, la page, le passage, et ce qui le contredit. Ce que vous avez lu
**sans** parvenir à le réfuter, écrivez-le aussi : c'est cela, et non votre silence, qui permet de marquer une entrée
**[H]**. Votre rapport sera versé tel quel, sous votre nom, dans un dépôt public. Gabarit en [annexe](#annexe--gabarit-du-rapport).

## 1. Pourquoi une relecture humaine

Aucune pièce du dépôt n'a été relue par un humain autre que son auteur : leur vérification déclarée a été conduite
par des agents de modèle de langage ([`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) : relecteurs humains, aucun). Le niveau de
preuve le plus élevé des Vol. II à IV était le vote unanime de trois de ces instances. Depuis le 15 septembre 2026, ce
niveau s'appelle **[A-i]** et n'est plus le premier : le sommet revient à **[H]**, *lu et non réfuté par un relecteur humain nommé*, qu'aucune entrée ne porte encore.

| Niveau | Ce qu'il établit | Ce qu'il n'établit pas |
|---|---|---|
| **[H]** | une personne nommée, qui répond de ce qu'elle signe, a cherché à réfuter l'entrée, source ouverte, sans y parvenir | que l'entrée est vraie ; ce qu'un autre relecteur conclurait ; quoi que ce soit d'une version modifiée depuis sa lecture |
| **[A-i]**, anciennement [A] | trois instances de modèle ont tenté de réfuter l'entrée, aucune n'y est parvenue | que ces tentatives sont indépendantes ; qu'un humain a lu |
| **[B]** | la source primaire a été lue et citée | qu'une réfutation a été tentée |
| **[C]** | une source est identifiée, non extraite | le contenu ; une entrée [C] ne porte jamais un fait central |

Définition et conditions d'attribution : [PRD du Vol. II, §7, chapeau](<1 - Collection/2 - OrchestrationAgentique/prd/PRD.md>),
qui en est le siège pour les Vol. II, III et IV. Exposé pour le lecteur : annexe A de la monographie du Vol. II, §A.9
([source](<1 - Collection/2 - OrchestrationAgentique/monographie/90-annexes/annexe-a-methodologie.md>)). Le Vol. II
remis est antérieur à la réforme : **« [A] » s'y lit [A-i]**, « [A/B mixte] » s'y lit « [A-i/B mixte] ». ✎ *Vrai du PDF
de `7ad9e44`. Celui que la tâche T7.1 a recomposé le même jour porte la réforme dans sa note d'avant-propos et son annexe A ;
ses chapitres gardent « [A] », qui s'y lit toujours [A-i].*

## 2. Qui relit quoi

Le plan propose deux relecteurs, un par pièce. Ni les noms, ni le budget, ni les délais ne sont décidés.

| | Relecteur 1 | Relecteur 2 |
|---|---|---|
| Profil proposé (plan, DA-4) | spécialiste des systèmes répartis | juriste du droit financier canadien |
| Pièce | **Vol. V** — *Traité sur les systèmes multiagents en essaim*, 4ᵉ éd., 2 septembre 2026 | **Vol. II** — *Orchestration agentique en écosystème d'entreprise de services financiers au Canada*, Partie III, ch. 9 à 13 |
| Pages | p. 3 à 130 (texte), p. 131 à 143 (références, à consulter) | p. 85 à 155 |
| Date de gel de l'information | 2 septembre 2026 (édition) | 16-17 juillet 2026 |
| Nom, fonction, affiliation | *à nommer — DA-4* | *à nommer — DA-4* |
| Budget ou honoraires | *à fixer — DA-4* | *à fixer — DA-4* |
| Délai de remise | *à convenir à l'envoi* ; le plan compte 4 à 8 semaines | *idem* |

**Indépendance.** Ne peut relire : l'auteur, ni quiconque a contribué à la pièce. Doivent être **déclarés** — non exclus
d'office, l'auteur décide avant l'envoi et la déclaration est publiée avec le rapport : tout lien avec l'auteur (parenté,
emploi, codirection, publication commune) ; tout lien avec Anthropic, éditeur des modèles qui ont assisté la rédaction et la
vérification des pièces, et dont une campagne de mesures fonde le ch. 8 du traité ; tout lien avec une institution ou un éditeur que la
pièce lue traite comme objet central — pour le Vol. II, le BSIF, l'AMF, les ACVM, IBM ; pour le traité, les
fournisseurs de courtiers de messages et de modèles qu'il nomme.

**Relecture nommée.** [H] exige un nom. Une relecture anonyme reste possible et utile ; elle ne donne pas [H]. Dites-le
avant de commencer.

## 3. Le dossier remis

Vérifiez chaque fichier à son empreinte SHA-256 avant de lire : `certutil -hashfile <fichier> SHA256` (Windows),
`shasum -a 256 <fichier>` (macOS), `sha256sum <fichier>` (Linux). Si elle diffère de celle du registre (§8), ne lisez
pas : écrivez à l'auteur.

| Fichier | Pour | Ce qu'il est |
|---|---|---|
| `4 - Essais/1 - Traité/Traité.pdf` | relecteur 1 | 143 p. **Le folio imprimé est la page du PDF.** ✎ *Recomposé le 15 septembre 2026 après `7ad9e44` (résumé anglais, tâche T7.1) : 144 p., la page 2 du PDF porte l'Abstract sans folio ; dès la page 3, folio imprimé = page du PDF − 1. Les folios cités ici ne bougent pas.* |
| `1 - Collection/2 - OrchestrationAgentique/Monographie.pdf` | relecteur 2 | 387 p. **Folio imprimé = page du PDF − 8** (liminaires en chiffres romains) : les p. 85 à 155 sont les pages 93 à 163 du PDF. Son annexe A (p. 332 à 338) est antérieure à la réforme des niveaux. ✎ *Recomposé le même jour après `7ad9e44` (page « Abstract », tâche T7.1) : 390 p., folio imprimé = page du PDF − 9, les p. 85 à 155 sont les pages 94 à 164 ; l'annexe A court des p. 332 à 340 et porte la réforme.* |
| `1 - Collection/2 - OrchestrationAgentique/prd/PRD.md`, §7 | relecteur 2, facultatif | le socle factuel : chaque entrée F-xx citée en note des chapitres, avec niveau, sources et réserves (Markdown, lisible comme texte) |
| `RELECTURE.md`, la présente consigne | les deux | — |

Empreintes au commit `7ad9e44` — à revérifier le jour de l'envoi et à reporter au registre :

```
f0d81e82c8ceff4d2056f15e6e21867efead8144bdcc2df9eba07168b18dea79  4 - Essais/1 - Traité/Traité.pdf
7b477e6b3225a2e63659ba6f2524ddcc6012d544b08c32a4101fe73cfc31914b  1 - Collection/2 - OrchestrationAgentique/Monographie.pdf
```

✎ *Empreintes des deux rendus recomposés le 15 septembre 2026 (tâche T7.1), sur l'arbre qui suit `fc33db1`, non commités à l'écriture — à revérifier de même :*

```
9788edb3863bbf5929cb63b040f2b73aa183b21a0da6cc1787a9eb57f04583c6  4 - Essais/1 - Traité/Traité.pdf
afb93f59c0d0f3fe4dcdb1d0ec2c7189b399260d1220df3df33bb7cc8c0e9614  1 - Collection/2 - OrchestrationAgentique/Monographie.pdf
```

## 4. Quoi lire, quoi chercher à réfuter

Lisez les pages indiquées en entier. Les énoncés ci-dessous sont ceux que la pièce donne elle-même pour centraux,
résumés sans rien y ajouter ; ils ne bornent pas votre lecture, ils disent où une réfutation porte le plus loin.
Reprenez leurs identifiants dans votre rapport.

Ce qui compte comme réfutation :

| Nature | Ce que vous montrez |
|---|---|
| **fait** | un fait, une date, un chiffre est faux **à la date de gel** de la pièce |
| **péremption** | il était exact à la date de gel et ne l'est plus — l'issue sera une redatation, non une correction |
| **source** | la source citée ne dit pas ce que la pièce lui fait dire : contenu, portée, statut (projet, final, arbitré ou non) |
| **inférence** | la conclusion ne suit pas de ce qui la porte, ou l'excède |
| **omission** | un texte, une source, un résultat contraire que la pièce ignore et qui change l'énoncé |
| **calcul** | une erreur de calcul, de preuve ou de transposition d'un résultat |
| **droit** | une qualification juridique erronée — la pièce déclare n'émettre aucun avis juridique, ce qui ne l'en dispense pas |

Ne sont pas demandés : la langue, le style, la mise en page, les coquilles qui ne changent pas le sens.

### 4.1 Traité — relecteur 1

| Id | Énoncé central | Pages | Appuis cités |
|---|---|---|---|
| T-1 | Au-delà de quelques dizaines d'agents, sous défaillances partielles, le coût du consensus explicite croît plus vite que sa valeur ; la coordination gagne à passer par un substrat événementiel partagé, un journal — transposition de la stigmergie. La thèse est un déplacement du point partagé, non sa suppression | 1 (résumé), 3-4, ch. 1 (5-22) | [1] à [5] |
| T-2 | Loi universelle de scalabilité transposée : dès que κ > 0, la capacité a un maximum, au-delà duquel le débit régresse — une régression, pas un plafond ; le point de retournement chiffré n'est qu'une illustration arithmétique | 23-24, 128 | [3] |
| T-3 | Les programmes sans coordination sont exactement ceux qui s'expriment en logique monotone : le substrat est supérieur où la décision est révocable, inférieur où un invariant global doit tenir à tout instant | 4, 24-25 | [6] |
| T-4 | Borne de retard du consensus de moyenne transposée au journal : sujet lu par tous, Δ(G) = n − 1, τ < π/(4(n − 1)), budget de retard qui décroît en 1/n | 40-44, dont 42 | [29], [36] |
| T-5 | La vérification paramétrée est Π⁰₂-complète, pas même semi-décidable ; « lire sans consommer » tombe du côté décidable | 45-49, dont 47 ; 128 | [63], [64] |
| T-6 | Les bornes probabilistes supposent tirage uniforme et fautes indépendantes ; la corrélation des fautes les invalide sans signal ; première mesure, φ = 0,916 | 59, 61-66, 128 | [116], [121] |
| T-7 | La frontière gagne un second axe, population décorrélée contre population conforme, et sept énoncés du livre portent une dette d'indépendance — sur une source unique, sans comité de lecture | 5, 117-127 | [119] |
| T-8 | Un agent et un système externe ne peuvent rendre commun qu'un effet a eu lieu exactement une fois ; seul recours, l'idempotence de l'effet, hors de l'essaim | 129 ; 24-25, 64-66, 95 | [110] |
| T-9 | Verdict contraire à la thèse : pour les systèmes de petite à moyenne échelle (n < 200), une solution centralisée par diffusion est vraisemblablement le meilleur choix | 77, 130 | [95] |

Le traité ne porte pas l'échelle des niveaux de preuve : ses énoncés s'appuient sur des références numérotées, non sur un
socle F-xx. Le §6 dit ce que devient un énoncé lu et non réfuté.

### 4.2 Vol. II, ch. 9 à 13 — relecteur 2

Niveaux des entrées au 15 septembre 2026, lus au [PRD du Vol. II, §7](<1 - Collection/2 - OrchestrationAgentique/prd/PRD.md>).

| Id | Énoncé central | Pages | Entrées du socle |
|---|---|---|---|
| V-1 | E-23 du BSIF inclut expressément les méthodes d'IA et d'apprentissage automatique dans « modèle » et anticipe les modèles à apprentissage et décision autonomes, sans employer « agentique », « agents » ni « orchestration » (vérification mécanique, textes anglais et français). Que l'IA agentique soit couverte est une inférence de cinq analystes juridiques, rapportée sans être endossée ; E-23 est fondée sur des principes — ses attentes sont « attendues », non « exigées » | 86-95, 99-100 | F-09 [A-i/B mixte] |
| V-2 | Le rapport conjoint BSIF-ACFC du 24 septembre 2024 : adoption de l'IA de ~30 % (2019) à ~50 % (2023), ~70 % *projetés* pour 2026 sur enquête auto-déclarée ; la causalité entrées-sorties des systèmes d'IA y est dite souvent indéterminable | 96-98 | F-10 [A-i] |
| V-3 | C-27 est mort au feuilleton le 6 janvier 2025 et la LIAD ne sera pas ravivée telle quelle ; C-36 est une réforme de la protection des renseignements personnels portant des volets d'IA, non une loi sur l'IA ; le Canada reste sans régime fédéral contraignant propre à l'IA, et la couverture passe par des instruments sectoriels | 101-108 | F-24 [B] |
| V-4 | La ligne directrice de l'AMF sur l'IA, finale le 30 mars 2026, entre en vigueur le 1er mai 2027, le jour d'E-23 ; son contenu n'est pas au socle, et l'ouvrage n'en dérive aucune contrainte | 109-110, 119 | F-25 [A-i] |
| V-5 | L'art. 12.1 de la Loi 25, en vigueur depuis le 22 septembre 2023, attache trois obligations à la décision « fondée exclusivement sur un traitement automatisé » : informer, expliquer sur demande raisons, facteurs et paramètres, offrir la révision par un membre du personnel. Son déclencheur est une propriété d'architecture, l'exclusivité — lecture de l'auteur | 111-120 | F-27 [B] |
| V-6 | L'avis ACVM 11-348 du 5 décembre 2024 : les lois existantes s'appliquent aux systèmes d'IA, l'avis « ne crée ni ne modifie aucune exigence », et sa définition inclut des niveaux variables d'autonomie et d'adaptativité après déploiement — accroche directe pour l'agentique, selon le socle | 121-130 | F-26 [B] |
| V-7 | Sur les onze entrées de la table du §13.1, neuf produisent une contrainte d'architecture et la ligne directrice de l'AMF aucune : la table mesure ce que le socle a extrait, non l'exigence des textes. L'encadrement déterministe des processus réglementés réunit trois sources non indépendantes, dont l'application au Canada n'est pas établie ; sous l'art. 12.1, l'imputabilité pèse sur l'entreprise qui rend la décision | 131-155 | F-09, F-25, F-26, F-27 ; F-36, F-37, F-46 [B] |

## 5. Comment rendre

1. **Un rapport par pièce**, en Markdown ou en texte brut, sur le gabarit en annexe. Un PDF est accepté ; un PDF
   seulement annoté en marge ne l'est pas, parce qu'il faudrait le transcrire, et toute transcription est une édition.
2. **Chaque renvoi** porte la pièce et le folio imprimé — « Traité, p. 42 », « Vol. II, p. 131 » —, la section si
   elle aide, et le passage visé entre guillemets, trois lignes au plus.
3. **Une objection vise un passage.** Numérotez-les O-1, O-2… ; donnez l'énoncé central touché (T-n, V-n, ou aucun),
   la nature (§4), la réfutation, **la pièce qui l'appuie** avec sa localisation (article, paragraphe, page,
   équation), la gravité — *bloquante* : l'énoncé central tombe ; *majeure* : il tient sous une réserve qui doit
   être écrite ; *mineure* : erreur locale, sans effet sur l'énoncé — et ce qui lèverait l'objection. Une objection sans
   pièce à l'appui est versée comme remarque, et son issue le dira.
4. **La section « Lu, non réfuté » est obligatoire.** Une ligne par énoncé T-n ou V-n que vous avez lu sans le
   réfuter, avec les sources que vous avez ouvertes. Pour le Vol. II, une entrée ne passe en [H] que si vous avez ouvert
   la source qu'elle cite : sans cette colonne, rien ne peut être marqué.
5. **« Non lu, hors compétence »** : dites ce que vous n'avez pas lu ou ne pouvez juger. Le chapitre 13
   croise le droit et l'architecture des processus d'affaires (F-36, F-37, F-46) : dire ce qu'on ne peut juger vaut mieux que se taire.
6. **Modèles de langage.** Des agents de modèle ont assisté la rédaction de ces pièces et en ont conduit la
   vérification ; c'est ce que votre lecture doit compléter. N'en employez aucun pour lire les pièces, chercher les
   réfutations ou rédiger le rapport. Si vous en employez un à autre chose — traduction, recherche documentaire —, dites où ; une objection ou une lecture dont un modèle a fait la part
   décisive est versée, et ne compte pas pour [H].
7. **Questions en cours de lecture** : par écrit, à l'auteur. Questions et réponses sont versées avec le rapport, pour
   qu'aucune orientation de la lecture ne reste hors du dossier.
8. **Déclaration et signature** (fin du gabarit) : indépendance, outils, consentement à la publication sous votre nom,
   **licence** du rapport. La licence du dépôt, CC BY 4.0, ne couvre pas les œuvres de tiers ([`LICENSE`](LICENSE)) :
   votre rapport reste votre œuvre. Il est proposé de le placer vous-même sous CC BY 4.0, vous en restant titulaire.
9. **Envoi** par courriel à l'auteur, depuis l'adresse sous laquelle vous signez ; le courriel est la trace de la remise.

## 6. Ce que devient le rapport

Engagements de l'auteur, à tenir envers les deux relecteurs (tâches T5.2 à T5.4 du plan) :

1. **Versé sans édition** sous `verification/relecture-externe-<nom>-<date>.md` de la pièce lue —
   `4 - Essais/1 - Traité/verification/` ou `1 - Collection/2 - OrchestrationAgentique/verification/`. `<nom>` : nom de
   famille en minuscules, sans accents, espaces en traits d'union ; `<date>` : date de signature, `AAAA-MM-JJ`. Un
   rapport PDF garde son format, même nom en `.pdf`. Ni correction, ni coupe, ni reformatage, ni transcription, par
   l'auteur ou par un agent — seule la normalisation des fins de ligne que `.gitattributes` impose au commit. L'empreinte
   du fichier reçu est au message du commit, et les questions-réponses du §5 sont versées à côté.
2. **Chaque objection reçoit une issue écrite**, dans `verification/issues-relecture-externe-<nom>-<date>.md` :
   *retenue* — avec le commit de la correction ; *refusée* — avec le motif ; *hors périmètre* — avec le motif. Le
   fichier vous est envoyé.
3. **Second tour, court** : les corrections des objections retenues vous sont soumises, et seulement elles ; votre
   réponse est versée sous `…-second-tour.md`. Aucune demande nouvelle n'y est attendue.
4. **Niveaux** — Vol. II : une entrée passe en [H] aux conditions du [PRD, §7](<1 - Collection/2 - OrchestrationAgentique/prd/PRD.md>)
   — rangée par vous parmi le lu non réfuté, source ouverte, inchangée depuis votre lecture ; une entrée corrigée sur
   votre objection n'y passe qu'au second tour. Le traité n'a pas d'échelle : un énoncé T-n lu et non réfuté est
   consigné au fichier d'issues ; la forme sous laquelle le texte du traité le portera est une décision d'auteur, non
   prise à cette date.
5. **Attribution** : vous êtes nommé à [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md), avec la pièce, le rôle et la date.
6. **Retrait** : un rapport versé peut sortir de l'arbre à votre demande ; il reste dans l'historique git, que le dépôt
   ne réécrit pas — ses renvois de commit sont des faits datés. Sachez-le avant de signer.

## 7. À l'auteur — avant l'envoi

- [ ] Trancher DA-4 : deux noms, fonctions, affiliations, budget, délai ; remplir le §2.
- [ ] Recevoir les déclarations d'indépendance **avant** l'envoi, et décider des liens déclarés.
- [ ] Rejouer le §9 le jour de l'envoi : si un PDF a changé depuis `7ad9e44`, mettre à jour le §3 et revérifier les
      pages des §4.1 et §4.2.
- [ ] Committer la consigne ; porter au registre le commit remis et les empreintes des pièces.
- [ ] Envoyer à chacun : la consigne, sa pièce et, au relecteur 2, le PRD du Vol. II.
- [ ] Porter au registre l'accusé de réception daté de chacun — critère d'acceptation de T5.1.

## 8. Registre d'envoi

La seule section de cette page qui change après l'envoi.

| | Relecteur 1 | Relecteur 2 |
|---|---|---|
| Nom | — | — |
| Commit de la consigne remise | — | — |
| Empreinte SHA-256 de la pièce remise | — | — |
| Envoi : date, canal | — | — |
| Accusé de réception : date | — | — |
| Échéance convenue | — | — |
| Rapport reçu : date, empreinte | — | — |
| Versé au commit | — | — |
| Issues envoyées : date | — | — |
| Second tour clos : date | — | — |

## 9. Rejouer

Depuis la racine du dépôt, en Git Bash.

```bash
sha256sum "4 - Essais/1 - Traité/Traité.pdf" "1 - Collection/2 - OrchestrationAgentique/Monographie.pdf"
python - <<'EOF'   # attendu : 3→3, 130→130, 143→143 ; 93→85, 94→86, 163→155
import pymupdf
for pdf, pages in [("4 - Essais/1 - Traité/Traité.pdf", (3, 130, 143)),
                   ("1 - Collection/2 - OrchestrationAgentique/Monographie.pdf", (93, 94, 163))]:
    d = pymupdf.open(pdf)
    for n in pages:
        p = d[n - 1]
        pied = [b[4].strip() for b in p.get_text("blocks") if b[1] > p.rect.height - 80]
        print(pdf, "page PDF", n, "-> folio", pied[-1] if pied else "-")
EOF
python Python/check-renvois.py
```

✎ *Sur les rendus recomposés le 15 septembre 2026 (tâche T7.1), les pages à passer sont (4, 131, 144) et (94, 95, 164) ; attendu : 4→3, 131→130, 144→143 ; 94→85, 95→86, 164→155.*

## Annexe — gabarit du rapport

À copier dans un fichier neuf. Les lignes entre chevrons se remplacent ; aucune section ne se supprime — une section
sans contenu porte « néant ».

```markdown
# Rapport de relecture externe — <Traité, 4ᵉ éd. | Vol. II, ch. 9 à 13>

| Champ | Valeur |
|---|---|
| Relecteur | <prénom nom>, <fonction>, <affiliation> |
| Compétence au regard de la pièce | <deux lignes> |
| Pièce lue | <nom du fichier> — SHA-256 <empreinte vérifiée> |
| Consigne reçue | RELECTURE.md, commit <…> |
| Paquet reçu le | <AAAA-MM-JJ> |
| Pages lues | <folios imprimés> |
| Lecture | du <AAAA-MM-JJ> au <AAAA-MM-JJ>, <n> heures |
| Outils | <…> ; modèles de langage : <aucun | lesquels, pour quoi, où> |
| Liens déclarés | <aucun | lesquels> (consigne, §2) |
| Licence du rapport | <CC BY 4.0, titulaire : prénom nom | autre> |

## 1. Méthode

<Ce que vous avez lu, dans quel ordre, quelles sources vous avez ouvertes, ce que vous avez recalculé.>

## 2. Objections

### O-1
- Renvoi : <Traité | Vol. II>, p. <n>, § <…>
- Passage visé : « <trois lignes au plus> »
- Énoncé central touché : <T-n | V-n | aucun>
- Nature : <fait | péremption | source | inférence | omission | calcul | droit>
- Réfutation : <…>
- Pièce à l'appui : <référence complète — article, paragraphe, page, équation>
- Gravité : <bloquante | majeure | mineure>
- Ce qui lèverait l'objection : <…>

## 3. Lu, non réfuté

| Énoncé (T-n, V-n) ou passage | Pages lues | Sources ouvertes | Remarque |
|---|---|---|---|
| <V-3> | <101-108> | <projet de loi C-36, LEGISinfo, consulté le …> | <…> |

## 4. Non lu, ou hors compétence

<…>

## 5. Remarques générales

<Ce qui ne vise pas un passage. Versé, sans effet sur les niveaux.>

## 6. Déclaration et signature

Je déclare avoir lu moi-même les pages indiquées et rédigé moi-même ce rapport ; les liens et les outils déclarés
ci-dessus sont complets. J'accepte qu'il soit versé sans modification, sous mon nom, dans le dépôt public de l'auteur,
sous la licence indiquée, et je sais qu'il restera dans l'historique git.

<prénom nom> — <AAAA-MM-JJ> — <signature, ou « transmis par courriel du AAAA-MM-JJ depuis l'adresse … »>
```
