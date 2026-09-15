---
title: "Note de synthèse — veille, revue et état de l'art"
subtitle: "Interopérabilité et Orchestration Agentiques"
author:
  - "Rédaction : Claude Opus 5 (Anthropic), non relue par un humain · pour André-Guy Bruneau · 15 septembre 2026"
lang: fr
region: CA
papersize: us-letter
fontsize: 10pt
linestretch: 0.95
mainfont: "New Computer Modern"
margin:
  x: 117pt
  y: 72pt
section-numbering: "1.1"
abstract-title: "Résumé"
abstract: |
  Cette note condense trois documents du dépôt pour le lecteur qui ne les lira pas en entier : la veille technologique en entreprise (Vol. VI, faits gelés au 15 août 2026), la revue de la littérature académique (Vol. VII, 15 août 2026) et l'état de l'art en services financiers (Vol. VIII, 20 août 2026). Chaque thèse et chaque chiffre y renvoient à la section du volume qui les porte, avec le niveau de preuve que ce volume déclare ; un contrôle versionné vérifie les renvois, les chiffres repris et la clôture de la bibliographie.

  Trois résultats traversent les volumes. La couche d'échange — MCP, A2A, ANP — est adoptée avant d'être normalisée ou sûre, et ce qu'elle n'exprime se comble hors d'elle. Au-delà du premier saut de délégation, le déficit est d'adoption, non d'invention, et aucune trace ne dit aujourd'hui pour qui un agent agit. En institution financière régie, ce n'est pas la pile qui décide mais ce que l'institution peut démontrer, à des dates fermes.

  Synthèse produite par un modèle de langage, non relue par un humain, avant la relecture externe prévue ; quand une décision en dépend, le volume fait foi.
header-includes: |
  ```{=typst}
  // Réglage commun des documents de « 3 - Veille/ ». Il est commenté ligne à ligne
  // dans l'en-tête de « Veille Technologique.md » ; il est repris ici tel que la note
  // de veille SDLC le porte, avec sa correction de `content-to-string` pour
  // l'apostrophe du titre. Un seul ajout, en fin de bloc : la règle des renvois.

  #set page(footer: context {
    let n = counter(page).get().first()
    if n > 1 { align(center)[#text(size: 10pt)[#n]] }
  })

  #set par(spacing: 0.6em, first-line-indent: 1.5em)

  #show strong: it => context {
    if measure(it.body).width < 14em.to-absolute() { it }
    else { text(weight: "regular", it.body) }
  }

  #show heading: set text(hyphenate: false)
  #show heading: set par(justify: false, first-line-indent: 0pt)
  #show heading: set block(sticky: true)

  #show figure.where(kind: table): set text(size: 9pt)
  #show raw.where(block: true): set text(size: 9pt)
  #show figure.caption: set text(size: 9pt)
  #show figure.caption: set par(justify: false, first-line-indent: 0pt)
  #show figure.caption: set block(sticky: true)
  #show figure.caption: set align(left)
  #show figure.caption: it => pad(x: 45pt, it)

  #set table(inset: (x: 5pt, y: 4pt))
  #show table.cell: set par(justify: false, first-line-indent: 0pt, leading: 0.5em)
  #show table.cell: set align(top)

  #show figure: set block(breakable: true, above: 1.4em, below: 1.4em)
  #show raw.where(block: true): set block(above: 1.4em, below: 1.4em)
  #show enum: set block(above: 1.0em, below: 1.0em)
  #show list: set block(above: 1.0em, below: 1.0em)
  #set image(width: 100%)

  #show figure: it => pad(x: -45pt, it)
  #show raw.where(block: true): it => pad(x: -45pt, it)

  #show <refs>: it => {
    set enum(spacing: 1.15em)
    set par(justify: false)
    it
  }

  #let cts-pandoc = content-to-string
  #let content-to-string(c) = {
    if type(c) == content and c.func() == smartquote { if c.double { "\"" } else { "\u{2019}" } }
    else if type(c) == content and c.has("children") { c.children.map(content-to-string).join("") }
    else { cts-pandoc(c) }
  }

  #let conf-pandoc = conf
  #let conf(title: none, subtitle: none, authors: (), date: none,
            abstract: none, abstract-title: none, ..reste, doc) = {
    conf-pandoc(..reste, authors: authors, {
      set document(title: if title != none { content-to-string(title) })
      place(top, float: true, scope: "parent", clearance: 4mm,
            block(below: 1em, width: 100%)[
        #align(center)[
          #block(below: 1.05em)[
            #text(size: 15pt, weight: "bold", hyphenate: false)[#title]
          ]
          #if subtitle != none {
            block(below: 1.35em)[
              #text(size: 12pt, weight: "regular", hyphenate: false)[#subtitle]
            ]
          }
          #if authors != none and authors != () {
            block(below: 0pt)[#authors.map(a => a.name).join(h(1.5em))]
          }
          #if date != none {
            block(above: 0.45em, below: 0pt)[#date]
          }
        ]
        #if abstract != none {
          block(inset: (x: 2em), above: 2.5em)[
            #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
          ]
        }
      ])
      doc
    })
  }

  #show heading.where(level: 1): set text(size: 14pt)
  #show heading.where(level: 1): set block(above: 1.7em, below: 0.6em)
  #show heading.where(level: 2): set text(size: 12.5pt)
  #show heading.where(level: 2): set block(above: 1.6em, below: 0.55em)
  #show heading.where(level: 3): set text(size: 11pt)
  #show heading.where(level: 3): set block(above: 1.5em, below: 0.5em)

  // Les renvois « [VI §9.3, réf. 272 — individuel] » : un corps sous le texte, en
  // gris, pour que l'œil lise la thèse et trouve la preuve sans que l'une masque
  // l'autre. `Python/check-synthese.py` lit la même forme dans la source.
  #show regex("\[(VI|VII|VIII) §[^\]]+\]"): set text(size: 8.5pt, fill: luma(38%))
  ```
abstract-en: &abstract-en |
  This note condenses three documents in the repository for readers who will not read them in full: the enterprise technology watch (Vol. VI, facts frozen as of 15 August 2026), the academic literature review (Vol. VII, 15 August 2026) and the state of the art in financial services (Vol. VIII, 20 August 2026). Every thesis and every figure in it refers to the section of the volume that carries it, with the level of evidence that volume declares; a versioned check verifies the cross-references, the figures carried over and the closure of the bibliography.

  Three results run across the volumes. The exchange layer — MCP, A2A, ANP — is adopted before it is standardized or secure, and what it does not express is filled outside it. Beyond the first delegation hop, the deficit is one of adoption, not of invention, and no trace today says on whose behalf an agent acts. In a regulated financial institution, it is not the stack that decides but what the institution can demonstrate, by firm dates.

  Synthesis produced by a language model, not reviewed by a human, ahead of the planned external review; where a decision depends on it, the volume is authoritative.
include-before:
  - |
    ```{=typst}
    // RÉSUMÉ ANGLAIS — tâche T7.1 du plan d'exécution, posée le 15 septembre 2026.
    // Le texte est le champ `abstract-en` ci-dessus, que l'alias YAML `*abstract-en`
    // rappelle ici : le gabarit de Pandoc ne passe que `abstract` au bloc de titre, et
    // `include-before` est le seul de ses emplacements qui précède la table des matières.
    // Traduction du résumé français avec assistance de modèle, non relue par un humain.
    // ⚠ IL OUVRE LA PAGE QUI SUIT LA PAGE DE TITRE, et non le bas de celle-ci : le bloc
    // de titre est un flottant non sécable, et un résumé anglais posé sous lui ferait
    // porter la mesure de `check-resume.py` sur une ligne de texte courant tombée au
    // hasard contre la marge basse. Même corps, même retrait et même amorce en
    // demi-gras que le résumé français ; `lang: "en"` pour la césure et les guillemets.
    // ⚠ Pandoc sépare les éléments de cette liste par une ligne vide, qui ferait
    // d'« Abstract » un paragraphe à lui seul : `resume-en` retire les sauts de tête.
    // ⚠ CETTE PAGE NE PREND PAS DE FOLIO ET NE DÉCALE PAS CEUX DU DOCUMENT : le compteur
    // y revient à 1, comme sur la page de titre, dont le folio est tu. Les folios que
    // d'autres pièces citent — simulateur et consigne de relecture pour le traité —
    // ne se décalent pas ; seul le rang de page dans le PDF avance d'une unité.
    #pagebreak(weak: true)
    #counter(page).update(1)
    #let resume-en(corps) = {
      let enfants = if corps.has("children") { corps.children } else { (corps,) }
      while enfants.len() > 0 and enfants.first().func() in (parbreak, [ ].func()) {
        enfants = enfants.slice(1)
      }
      block(inset: (x: 2em))[
        #set text(lang: "en", region: none)
        #text(weight: "semibold")[Abstract] #h(1em) #enfants.join()
      ]
    }
    #resume-en[
    ```
  - *abstract-en
  - |
    ```{=typst}
    ]
    ```
  - |
    ```{=typst}
    #set text(size: 11pt)
    ```
---

# Statut de cette note {-}

Cette note a été rédigée le 15 septembre 2026 par un agent de modèle, Claude Opus 5 (Anthropic), sous la consigne de l'auteur du dépôt ; **aucun humain ne l'a relue**, et les trois volumes qu'elle résume n'ont, eux non plus, aucun relecteur humain [CONTRIB]. Elle précède la relecture humaine externe que prévoit la phase 5 du plan d'exécution de l'évaluation académique, et ne tient lieu d'aucune de ses conclusions [PLAN]. Elle résume sans rien ajouter : aucun fait, aucun chiffre, aucun rapprochement entre volumes qui ne soit écrit dans l'un d'eux, et aucun niveau de preuve plus élevé que celui que le volume déclare. Ses faits sont gelés aux dates des volumes — 15 août 2026 pour la veille et la revue, 20 août 2026 pour l'état de l'art —, non à la sienne.

Elle se refait depuis le dépôt seul, par `python Python/check-synthese.py --rendre` lancé depuis `3 - Veille/` ; le même script, sans argument, la contrôle.

```{=typst}
#pagebreak(weak: true)
```

# Mode d'emploi

**En une séance.** La section 2 donne l'essentiel en une page. Les sections 3, 4 et 5 reprennent chacune un volume ; la section 6 dit ce que les volumes se corrigent l'un à l'autre, la section 7 rassemble les questions ouvertes, la section 8 les limites qu'ils déclarent, la section 9 les chiffres porteurs et l'endroit où les vérifier. Aucun prérequis ; les sigles sont développés au tableau qui clôt cette section.

**Les renvois.** Chaque affirmation se ferme sur un renvoi entre crochets, composé en petit gris : `[VI §9.3, réf. 272 — individuel]` se lit « Vol. VI, section 9.3 ; notice 272 de sa bibliographie ; niveau de preuve déclaré : individuel ». Le numéro de section est celui qu'imprime le PDF du volume et que portent ses signets ; la notice, quand elle est donnée, mène à la source primaire. Un renvoi couvre le texte qui le précède jusqu'au renvoi antérieur. Le contrôle vérifie que chaque section citée existe, que chaque chiffre du passage couvert figure dans la section citée, et que chaque notice citée est au volume sous ce numéro.

**Vérifier une affirmation.** Ouvrir le PDF du volume, atteindre la section par ses signets, y chercher le chiffre ou la formule ; pour la source primaire, suivre la notice citée dans la bibliographie du volume — les notices reprises figurent en fin de note, chacune avec un fragment qui l'identifie.

**Les niveaux de preuve.** Aucun volume n'a de relecteur humain ; leurs niveaux mesurent donc des régimes de vérification par instances de modèle, et la note les reprend sans les convertir.

| Étiquette | Volume | Ce que le volume déclare |
|:--------------|:------|:------------------------------------------------------------|
| pipeline | VI | fait du corps établi par les passes de juillet : réfutation adverse sur les énoncés les plus exposés, contre-vérification individuelle sinon — le haut du document, §4.6 à §4.13 (VI §2.2, VI §10) |
| individuel | VI, VIII | contre-vérification individuelle sur source primaire, sans ronde adverse : passes des 8 et 15 août de la veille ; régime de l'état de l'art (VIII §2.1) |
| secondaire | VI, VIII | source primaire inaccessible, énoncé porté par une source secondaire nommée |
| compagnon | VI, VIII | fait repris d'un autre volume du même auteur, sans re-vérification |
| inférence | VI, VIII | lecture, rapprochement ou qualification que le volume marque lui-même comme tels |
| recommandation | VI, VIII | ce que le volume recommande en son nom |
| attestée · autodéclarée · sans revue | VII ; VI et VIII en second terme | régime de publication de la pièce citée, lu à sa notice ; le plus faible l'emporte quand plusieurs pièces sont citées ; la revue n'a rien répliqué (VII §2.3). Pour la veille et l'état de l'art, il suit le régime de vérification quand la notice citée est une prépublication arXiv : « individuel, sans revue » — à régime égal, étiquette égale |
| corpus | VII | recensement ou analyse du corpus de la revue, non estimation du champ (VII §2.3) |
| déclaration | tous | ce que le volume dit de sa propre méthode ou de ses limites |
| question | tous | question ouverte que le volume formule |

: Les étiquettes de niveau de preuve des renvois, et la déclaration de chaque volume dont elles procèdent.

**Les notes de lecture.** Là où deux passages d'un même volume ne portent pas le même chiffre, la note le signale en le citant, sans arbitrer.

| Sigle | Développement |
|:--------------------|:------------------------------------------------------------------|
| MCP · A2A · ANP | *Model Context Protocol* (agent et outils) · *Agent2Agent* (délégation entre agents) · *Agent Network Protocol* (découverte en réseau ouvert) |
| AP2 · x402 | *Agent Payments Protocol* (autorisation par mandats signés) · protocole de règlement par le code HTTP 402 |
| OASF · SDK | *Open Agentic Schema Framework* · trousse de développement logiciel |
| BPMN · DMN · XES | *Business Process Model and Notation* · *Decision Model and Notation* · *eXtensible Event Stream* |
| SPIFFE · WIMSE | identité de charge de travail, et son groupe de travail à l'IETF |
| DAWN · DMSC | groupes de l'IETF chartés en juin 2026 : découverte d'agents ; collaboration multi-agents sécurisée |
| IETF · W3C · NIST | *Internet Engineering Task Force* · *World Wide Web Consortium* · *National Institute of Standards and Technology* |
| BSIF · AMF · OCRI | Bureau du surintendant des institutions financières · Autorité des marchés financiers · Organisme canadien de réglementation des investissements |
| ACFC · CANAFE | Agence de la consommation en matière financière du Canada · Centre d'analyse des opérations et déclarations financières du Canada |
| B-10 · E-21 · E-23 | lignes directrices du BSIF : risque lié aux tiers · risque opérationnel et résilience · risque de modélisation |
| RTR | *Real-Time Rail*, le rail de paiement en temps réel de Paiements Canada |
| PRISMA · TLA+ | protocole de revue systématique · langage de spécification formelle |

: Les sigles de la note, développés comme les volumes les emploient.

# L'essentiel en une page

1. **Pas de norme.** MCP, A2A et ANP forment une pile complémentaire et adoptée ; aucun n'est une norme *de jure*, et leurs suites de conformité ne sont pas opposables [VI §4.5 — individuel · VI §5.5 — individuel].
2. **Un écart mesuré.** L'adoption précède l'assurance : un audit dynamique de 414 serveurs MCP publics, prépublication non révisée par les pairs, relève 91,8 % de serveurs sans authentification OAuth [VI §7.1, réf. 272 — individuel, sans revue].
3. **Hors de la pile.** Paiements, sémantique, confiance : chaque couche que la pile laisse implicite se comble en périmètre, et le déficit d'interopérabilité ouverte se déplace sans se résorber [VI §9.5 — individuel · VI §14 — individuel].
4. **L'agent enveloppé.** Le cadre déterministe invoque les agents, jamais l'inverse ; les propriétés que le droit exige sont celles de l'orchestration, non des protocoles [VI §9.6 — inférence · VI §4.11 — pipeline].
5. **Un déficit d'adoption.** Au moins douze brouillons de chaîne de délégation à l'IETF — un plancher, non un inventaire —, aucun adopté [VI §7.7 — individuel] ; la revue y aboutit par la littérature : proposer est dépassé, normaliser ne tient pas [VII §15.1, réf. 77, 76, 85 — sans revue].
6. **Aucun mandat tracé.** Aucun attribut d'observabilité agentique ne décrit un mandat [VI §4.13 — individuel] ; et des traces identiques admettent des assignations de mandat incompatibles [VII §15.3, réf. 84 — sans revue].
7. **Un corpus à son régime.** Sur 189 pièces arXiv, 145 — 77 % — ne présentent aucun signe de revue par les pairs à leur notice ; le chiffre vaut pour le corpus, non pour le champ [VII §3.1 — corpus].
8. **La pile ne décide pas.** En institution régie : trois surveillants, trois qualifications d'une même exécution d'agent, et un attribut décisif — l'identité de l'appelant — qu'aucun protocole ne rend opposable [VIII §4.2 — individuel].
9. **La preuve par le système.** Le droit canadien de la preuve demande la fiabilité du système qui enregistre, là où les brouillons investissent dans la signature de chaque saut [VIII §7.7.1, réf. 185 — inférence].
10. **Un calendrier fermé.** E-23 du BSIF et la ligne directrice de l'AMF sur l'IA entrent en vigueur le même jour, le 1er mai 2027 ; avec E-21 et la ligne directrice sur les tiers, aucune de ces quatre échéances n'exige quoi que ce soit des agents, et toutes les quatre s'appliqueront à eux [VIII §9.12 — individuel].

# La veille technologique (Vol. VI)

La veille dresse l'état du champ déployé — spécifications, dépôts, communiqués, textes réglementaires — au 15 août 2026, en quatre questions : quels protocoles, sous quelle gouvernance, avec quel écart entre adoption et sécurité, et quelles couches laissées implicites [VI §1 — déclaration].

## La couche d'échange : complémentaire, adoptée, non normalisée

Trois protocoles structurent l'interopérabilité agentique, chacun sur son interface : MCP entre l'agent et ses outils, A2A entre agents mutuellement opaques, ANP pour la découverte en réseau ouvert. Ils forment les étages d'une même pile, non des rivaux, et leur maturité suit la proximité du système d'information [VI §4.5 — individuel]. Au 15 août 2026, aucun protocole d'interopérabilité agentique n'est une norme *de jure* [VI §5 — individuel]. Les fondations gouvernent du code, non un statut de norme ; des suites de conformité existent pour MCP et A2A, mais elles sont gouvernées par les projets mêmes qu'elles vérifient, et aucune ne délivre d'attestation opposable [VI §5.5 — individuel]. Les enceintes de normalisation n'ont rien produit qui change ce constat : au W3C, le groupe communautaire porteur d'ANP compte 263 participants et aucune activité depuis juin 2025, celui sur l'identité d'agents 43 participants et aucun livrable ; au NIST, six mois après le lancement de son initiative sur les agents, le compte des livrables est nul [VI §5 — individuel].

La couche bouge par rupture. La révision `2026-07-28` de MCP, la plus substantielle depuis l'ajout de l'autorisation, retire les sessions de niveau protocole et la reprise de flux, et rompt la compatibilité avec les clients antérieurs ; elle s'accompagne du premier engagement daté d'un protocole de la couche commune sur sa propre évolution : douze mois avant tout retrait, quatre-vingt-dix jours sur risque de sécurité actif [VI §4.1, réf. 252 — individuel]. A2A, lui, n'a rien publié depuis le correctif `v1.0.1` du 28 mai 2026 : deux protocoles complémentaires vivent sur des horloges de gouvernance divergentes, sans coordination de leurs calendriers [VI §4.2 — individuel].

## L'adoption précède l'assurance

Le 31 juillet 2026, un audit dynamique de 414 serveurs MCP publics relève 68 vulnérabilités à l'exécution et 91,8 % de serveurs sans authentification OAuth : pour la veille, l'écart entre adoption et sécurité cesse d'être une inférence, il est mesuré sur parc réel. La mesure est une prépublication arXiv, sans attestation de publication à sa notice [VI §7.1, réf. 272 — individuel, sans revue]. Côté adoption, les deux publications primaires du 28 juillet 2026 mesurent la même grandeur et divergent d'un quart — près d'un demi-milliard de téléchargements mensuels de SDK selon le projet, plus de 400 millions selon Anthropic —, sans périmètre ni méthode exposés ni audit [VI §6.3, réf. 269, 270 — individuel]. *Note de lecture* : le sommaire exécutif de la même édition rattache les 400 millions, et les plus de 950 serveurs du répertoire, à la notice du billet du projet ; le §6.3 donne l'un et l'autre au billet d'Anthropic, et le demi-milliard au projet [VI §6.3, réf. 269, 270 — individuel]. Le registre officiel, paginé exhaustivement par la veille le 15 août 2026, compte 21 767 enregistrements de dernière version : des déclarations d'éditeur, non des serveurs vérifiés en exploitation [VI §6.3, réf. 340 — individuel].

Un sondage de la Cloud Security Alliance (n = 418), à lire avec son commanditaire, rapporte 82 % d'organisations ayant découvert des « agents fantômes » et 21 % seulement dotées d'un processus formel de mise hors service [VI §7.1, réf. 110 — individuel]. Des trois projections d'analystes que portait la veille, une seule survit à sa source : Gartner (juin 2025) prévoit l'annulation de plus de 40 % des projets d'IA agentique d'ici fin 2027 [VI §12.2, réf. 80 — individuel]. Les « 1 300 milliards de dollars » de 2029 chiffrent la dépense totale en intelligence artificielle, non la dépense agentique, et les 70 % d'entreprises consolidées d'ici 2030 n'ont aucune publication primaire [VI §12.2, réf. 82 — individuel].

Le seul franchissement de périmètre organisationnel documenté de bout en bout par ses trois parties, en juillet 2026, n'est pas une interopérabilité voulue [VI §6.4 — individuel]. C'est un échec de confinement pendant l'évaluation d'un fournisseur, dont les effets ont atteint la production d'un tiers non partie à l'évaluation ; parmi les indicateurs relevés figurent des artefacts de journaux hallucinés : la trace produite dans le périmètre de l'agent n'était pas seulement falsifiable, elle a été fabriquée [VI §7.1 — individuel].

## Ce que la pile n'exprime se comble hors d'elle

Chacune des sept couches orthogonales que la veille examine aux §4.6 à §4.13 — événements, trafic, paiements, sémantique, confiance, orchestration des processus, exploitation — dispose d'au moins un porteur candidat ; l'orchestration des agents eux-mêmes n'en a aucun, et n'est portée que par des cadriciels et des exécutifs de fournisseur [VI §4.14 — individuel]. Sur ce front, une taxonomie construite sur 150 traces annotées et validée sur plus de 1 600 traces de sept cadriciels range les défaillances des systèmes multi-agents en quatorze modes et trois catégories, dont aucune n'est de capacité du modèle : un système multi-agents défaille par son agencement [VI §4.14, réf. 260 — individuel, sans revue]. Le transfert entre agents du SDK le plus diffusé est un appel d'outil qui livre par défaut à l'agent receveur l'intégralité de l'historique, l'opposé du moindre privilège [VI §4.14 — individuel]. Toute fonction que la couche commune n'exprime pas se comble à côté d'elle, chaque brique réintroduisant le périmètre que les protocoles promettaient de supprimer [VI §9.5 — individuel].

Trois couches l'illustrent. **Paiements** : AP2, donné à la FIDO Alliance le 28 avril 2026, n'enregistre aucun commit sur sa branche principale depuis le 29 avril 2026 ; x402, opérationnel en fondation à quarante membres depuis le 14 juillet 2026, publie entre le 29 juillet et le 13 août 2026 cinq correctifs de sécurité dont aucun ne fait l'objet d'un avis formel [VI §4.8 — individuel]. **Sémantique** : aucun vocabulaire de capacités commun ne relie MCP, A2A, ANP et les registres commerciaux ; OASF est l'unique taxonomie normalisée publiée, et son adoption ne dépasse pas AGNTCY [VI §4.9 — individuel]. **Confiance** : l'identité d'agent a trois incarnations en production — charge de travail SPIFFE chez Google, justificatifs vérifiables chez AGNTCY, annuaire d'entreprise chez Microsoft —, ni convertibles ni reliées par un document de correspondance [VI §4.10 — pipeline] ; au 15 août 2026, les deux groupes agentiques de l'IETF chartés en juin, DAWN et DMSC, portent vingt-sept brouillons et n'en ont adopté aucun [VI §4.10, réf. 159 — individuel].

## L'agent enveloppé

L'orchestration des processus d'affaires est la seule région de la pile normalisée *de jure* : ISO/CEI 19510:2013 équivaut à BPMN 2.0.1, une révision en retrait de la version courante 2.0.2 de l'OMG ; les journaux d'événements relèvent de la norme IEEE 1849 révisée en 2023 ; la décision dispose d'un kit de conformité public de 3 391 cas de test [VI §4.11 — pipeline]. Le moteur de processus se fait client des protocoles agentiques, jamais l'inverse : il consomme MCP et A2A comme contrats externes, et la sémantique de processus reste au moteur [VI §4.11 — pipeline]. Aucun substrat d'exécution durable n'offre d'*exactly-once* distribué de bout en bout : les effets externes restent *at-least-once*, à charge d'idempotence, et ni MCP ni A2A ne définissent de sémantique de livraison ou de reprise [VI §4.11.1 — pipeline]. Le droit sectoriel exige exactement les propriétés natives de l'orchestration : ce ne sont pas les protocoles qui rendront un processus agentique conforme, c'est la couche qui l'enveloppe [VI §4.11.5 — pipeline].

D'où la thèse de la veille, qu'elle signale comme lecture : l'agent d'entreprise fiable de 2026 est enveloppé — flot durable, décisions réglementées déléguées à des points de décision externalisés, supervision humaine modélisée, traces capitalisées pour l'audit —, le cadre déterministe invoquant les agents, jamais l'inverse. Chaque élément existe chez un fournisseur au moins ; aucun n'est interopérable entre eux [VI §9.6 — inférence]. Aux fournisseurs, la veille propose trois questions : le statut exact de chaque connecteur, la portée des garanties d'exécution, et ce qui sort au départ [VI §9.6 — recommandation].

## Émettre, appliquer, exploiter

La confiance agentique se lit en trois temps. Émettre une identité est le mieux servi ; l'appliquer dispose de mécanismes réels, passerelles et points de décision, au prix du périmètre et sans statut de norme ; l'exploiter — vérifier que le comportement d'aujourd'hui tient encore le mandat d'hier — est le moins servi. Le déficit suit l'ordre inverse de celui dans lequel le marché investit [VI §9.7 — individuel].

Sur l'exploitation, le relevé exhaustif du registre d'OpenTelemetry au 15 août 2026 compte soixante-trois attributs `gen_ai.*`, tous au statut *Development* — un niveau qui « ne devrait pas être utilisé en production » —, dont aucun ne décrit une chaîne de délégation, un mandat ou une autorisation ; huit propositions visent ce manque, aucune n'est fusionnée [VI §4.13 — individuel]. Tracer un appel n'est pas tracer une délégation [VI §4.13 — individuel].

Sur la délégation, le relevé du 15 août 2026 dénombre douze brouillons individuels de chaîne de délégation déposés à l'IETF, du 25 mars au 7 août 2026, tous « not endorsed by the IETF » : aucun mécanisme normalisé ne maintient de traçabilité opposable au-delà de deux sauts, et le déficit n'est pas d'invention mais d'adoption. La veille borne elle-même la portée de ce fait : il est établi, non vérifié, par un balayage par mot-clé et non exhaustif du registre de l'IETF, et les douze sont un plancher, non un inventaire [VI §7.7 — individuel]. *Note de lecture* : le sommaire exécutif et le §9.7 de la même édition parlent encore de « trois brouillons » IETF [VI §9.7 — individuel] ; le décompte de douze est celui du relevé détaillé [VI §7.7 — individuel]. La révocation est le mécanisme le moins spécifié de la pile : trois brouillons la traitent par trois modèles de propagation irréconciliables, dont un exclut la cascade, et 21 % seulement des organisations ont un processus formel de mise hors service [VI §7.8 — individuel]. Aucun mécanisme vérifié ne répond aux cinq questions de la grille — qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en répond —, et la troisième est la plus vide [VI §7.6 — individuel].

## Le calendrier réglementaire

L'article 50 du règlement européen sur l'IA, marquage compris, s'applique depuis le 2 août 2026 ; le 2 décembre 2026 n'est qu'un délai de grâce, pour l'article 50(2) et les seuls systèmes antérieurs. Le règlement (UE) 2026/1744 reporte le haut risque au 2 décembre 2027 pour l'annexe III et au 2 août 2028 pour l'annexe I [VI §8.1, réf. 254 — individuel]. Les lignes directrices de la Commission du 20 juillet 2026 rangent les agents sous l'article 50(1) et exigent qu'ils déclarent leur nature artificielle et la personne pour le compte de laquelle ils agissent — instrument non contraignant [VI §8.1, réf. 336 — individuel].

Au Canada, E-23 du BSIF, finale le 11 septembre 2025, entre en vigueur le 1er mai 2027, échéance vérifiée en source primaire [VI §8.4, réf. 209 — individuel]. La ligne directrice de l'AMF sur l'IA entrerait en vigueur le même jour, mais le domaine du régulateur refuse la consultation automatisée (HTTP 403) : tout énoncé AMF de la veille est au conditionnel [VI §8.4 — secondaire]. L'article 12.1 de la Loi 25 ne prescrit aucun degré d'autonomie : il se déclenche quand la décision est fondée exclusivement sur un traitement automatisé et impose alors l'information, les observations devant un membre du personnel en mesure de réviser, et la restitution sur demande des principaux facteurs et paramètres [VI §8.4, réf. 212 — secondaire]. Le bulletin du BSIF du 13 juillet 2026 nomme le chaînage d'outils et attend des identités non humaines uniques sous moindre privilège, au registre des saines pratiques non contraignantes [VI §8.4, réf. 274 — individuel]. La monographie compagnon croise trois protocoles et cinq corpus de textes canadiens : quinze croisements, six rapprochements tous marqués comme inférences d'auteur, aucun lien documenté par source primaire [VI §8.4, réf. 218 — compagnon].

L'horloge cryptographique court aussi : le brouillon initial NIST IR 8547, toujours sans version finale, déprécie les algorithmes classiques à 112 bits vers 2030 et les retire après 2035, et A2A `v1.0.0` ne mentionne aucun algorithme post-quantique [VI §7.4 — individuel · VI §7.10 — individuel]. Pour la veille, toutes les bornes datées — grappe réglementaire jusqu'en 2028, échéance canadienne du 1er mai 2027, échéance cryptographique — pointent vers un même impératif, une couche normalisée d'identité, de traçabilité et d'autorisation des agents ; reste à savoir qui en fournira la forme canonique [VI §12.5 — individuel].

## Ce que la veille dit de sa propre fiabilité

La veille distingue un régime fort — trois vérificateurs indépendants chargés de réfuter chaque énoncé en retournant aux sources primaires — d'un régime faible de contre-vérification individuelle ; les passes du 8 et du 15 août 2026, dont la seconde date l'édition, n'ont comporté aucune ronde adverse [VI §2 — déclaration]. L'audit du 8 août a rouvert une à une les 269 entrées de la bibliographie antérieure : 179 confirmées, 54 corrigées, 30 non reconfirmables, 6 auto-citations, aucune introuvable [VI §2.2 — déclaration]. En dix jours de fenêtre, six énoncés porteurs de l'édition précédente ont été réfutés sur source primaire, dont deux sur le calendrier réglementaire [VI §14 — déclaration]. Ses limites : une littérature primaire faite de prépublications non révisées, des métriques d'adoption auto-déclarées, et des corpus compagnons du même auteur qui comptent pour un seul témoignage [VI §10 — déclaration].

# La revue de la littérature (Vol. VII)

La revue pose une question en deux parties : que la littérature académique établit-elle réellement sur l'interopérabilité et l'orchestration agentiques en entreprise, et à quel régime de preuve ? La seconde partie commande la première [VII §1.1 — déclaration].

## La forme du corpus avant son contenu

Le corpus compte 192 entrées, dont 189 déposées sur arXiv, chaque notice ayant été reprise à l'interface du dépôt le 15 août 2026 ; il n'y a aucune réplication, et les décomptes sont un recensement du corpus retenu, non une estimation du champ [VII §2 — déclaration]. Sur les 189 pièces arXiv, douze portent une attestation de publication dans leur notice, soit 6 % ; trente-deux annoncent une acceptation dans le seul champ de commentaire ; les 145 restantes, soit 77 %, ne présentent aucun signe de revue par les pairs [VII §3.1 — corpus]. 63 % des pièces arXiv ont été déposées en 2026, et plus de la moitié n'a jamais été révisée [VII §3.1 — corpus].

Le chiffre porte sur ce corpus lu au critère de la notice. Une passe de contrôle sur DBLP, Crossref et OpenAlex trouve de la littérature arbitrée hors arXiv sur les quatre fronts que le corpus donnait pour vides ; refait sur sept entrées classées sans revue, le même test en trouve quatre publiées : 145 est un plafond du non-arbitré, douze un plancher de l'arbitré [VII §17 — corpus].

## Un défaut de fond unique

Les dix fronts convergent sur un énoncé qu'aucun ne porte seul : rien, dans les piles examinées, ne sépare ce qui est autorisé de ce qui est seulement présent [VII §14.1 — corpus]. Sur le contenu, 9,93 % de paires description/code incohérentes sur 2 214 serveurs réels, 97,1 % de descriptions d'outils portant au moins un défaut, 37,2 % seulement d'applications imposant une approbation bloquante avant exécution d'outil [VII §4.1, réf. 55, 53, 54 — sans revue]. Sur l'autorité, 40,55 % de 7 973 serveurs MCP distants exposent des outils sans aucune authentification [VII §6.1, réf. 81 — sans revue]. Sur l'effet, ce que produit le modèle doit rester une proposition : la frontière de règlement est déplacée hors du retour d'outil, et un contrôle d'admission déterministe rend l'état engagé indépendant de la compétence du proposant [VII §10.1, réf. 126, 127 — sans revue].

## Ce qu'établissent les fronts, et à quel régime

**Sécurité.** Les scores de défense obtenus sur bancs statiques ne survivent pas à l'adversaire adaptatif : une défense mesurée à 0 % de succès d'attaque en statique remonte à 28 % au global et à 64 % sur les tâches où l'action est déléguée à du contenu contrôlé par l'attaquant [VII §5.1, réf. 71 — sans revue]. **Identité.** La convergence la plus forte du corpus porte sur l'atténuation : l'autorité doit décroître à chaque saut, et le jeton porteur relayé tel quel est unanimement tenu pour le mauvais primitif [VII §6.1, réf. 83, 76, 77 — sans revue].

**Multi-agents.** Le rendement du multi-agent est non monotone : sur six bancs et 245 caractéristiques, l'agent unique gagne dans environ 43,3 % des cas [VII §7.1, réf. 95 — sans revue]. Et la redondance d'un collectif est surcréditée dès que ses agents partagent un modèle : deux instances d'un même modèle échouent ensemble sur 90,0 % des missions où l'une échoue, sur 18 000 missions notées par du code déterministe [VII §13.1, réf. 180 — sans revue]. **Évaluation.** Sur trois bancs ouverts de traces d'agents, l'effet propre de l'agent explique moins de 3 % de la variance totale, l'interaction agent × tâche de 7 à 23 % : un classement d'agents ne classe pas des capacités, il classe des spécialisations [VII §8.1, réf. 190 — sans revue].

**Paiements.** Aucune pièce ne mesure de transaction réelle à valeur réelle sur une pile de paiement agentique en exploitation : tout énoncé sur le comportement des agents payeurs repose sur de la simulation [VII §9.3 — corpus]. **Gouvernance.** Dans ce corpus, la supervision humaine n'est démontrée nulle part comme contrôle effectif [VII §11.1 — corpus]. Côté droit, une pièce attestée établit que le règlement européen la charge de corriger le biais d'automatisation sans base empirique attestant qu'elle y parvient [VII §11.1, réf. 143 — attestée].

## L'instrument de mesure est le maillon faible

Sur 64 611 serveurs uniques, les scanners qui déclarent 96,89 % des serveurs « à risque » présentent moins de 50 % de vrais positifs à la validation manuelle et se contredisent entre eux [VII §4.2, réf. 51 — sans revue]. La meilleure attribution automatique de défaillance trouve l'agent fautif dans 53,5 % des cas et l'étape décisive dans 14,2 % [VII §7.1, réf. 88 — autodéclarée]. Sur les 123 pièces des dix fronts, 67 — 54 % — rapportent la performance d'un artefact de leurs propres auteurs : ce corpus s'auto-arbitre à moitié [VII §14.3 — corpus].

## Les désaccords réels, et ce qui les arbitrerait

La revue nomme un désaccord réel par front, avec l'expérience qui le trancherait ; en voici la moitié [VII §14.3 — corpus].

| Front | Désaccord | Ce qui l'arbitrerait |
|:----------|:--------------------------------------|:------------------------|
| Multi-agents | marge réelle du multi-agent, contre non-avantage à dix fois le prix [VII §14.3 — corpus] | un réglage égalisé sur les deux bras |
| Évaluation | juge automatique quasi humain, ou plafond démontré [VII §14.3 — corpus] | un juge indépendant, des étiquettes humaines |
| Processus | suspendre l'effet jusqu'à certitude, ou l'émettre et le réviser [VII §14.3 — corpus] | la part d'actions irréversibles en flux réel |
| Gouvernance | règlement européen opérationnalisable, ou inadéquat ; prémisse d'autonomie contestée [VII §14.3 — corpus] | un message confronté aux articles 12, 14 et 26 |
| Web agentique | identification coopérative, ou détection imposée [VII §14.3 — corpus] | la conformité d'agents non coopératifs |

: Désaccords relevés par la revue, un par front, avec ce qui les arbitrerait.

## Trois énoncés de la veille mis à l'épreuve

**« Au-delà de deux sauts de délégation, aucun mécanisme normalisé ne maintient de traçabilité opposable. »** Proposer est dépassé : une chaîne où chaque saut est signé se vérifie hors ligne. Prouver est partagé : une vérification en TLA+ sur 2,7 M d'états établit le rétrécissement d'autorité, mais juge la préservation d'intention pratiquement infaisable. Normaliser ne tient pas : la vérification formelle des spécifications relève 35 lacunes et 30 défaillances nées de la seule composition. L'obstacle est de normalisation et d'instrumentation, non d'invention [VII §15.1, réf. 77, 76, 85 — sans revue].

**« L'arrimage entre orchestration installée et pile agentique est unilatéral. »** Exact sur le déploiement, faux sur la littérature : quatre formalismes conçus pour les agents existent depuis fin 2024 ; ce qui manque est l'adoption, et la dissymétrie est industrielle, non scientifique [VII §15.2, réf. 133, 137, 134, 131 — sans revue].

**« Aucun attribut du socle d'observabilité agentique ne décrit une chaîne de mandat. »** Confirmé par une seconde voie : des traces identiques admettent plusieurs assignations de mandat incompatibles, de sorte que l'exécution déléguée n'est pas identifiable [VII §15.3, réf. 84 — sans revue]. Sur une suite gelée de 5 280 épisodes, une invite constitutionnelle et un garde à provenance produisent l'un et l'autre 0 violation sur 384 ; ils ne se séparent qu'en scénarios de blanchiment appariés, 22 épisodes sur 96 contre 0 sur 96. Le déficit est de liaison, non de vocabulaire, et la revue tient ce verdict pour une position appuyée par une mesure de portée étroite [VII §15.3, réf. 192 — sans revue].

## Ce que personne ne mesure

Aucun front ne compte ses échantillons en organisations, en déploiements ni en incidents observés : il n'existe aucun taux de base [VII §16 — corpus]. Personne ne mesure une propriété de bout en bout franchissant une frontière réelle, ni de protocole à protocole, ni d'organisation à organisation [VII §16 — corpus]. Personne ne mesure non plus la conformité d'exécution d'un agent à un modèle de processus [VII §10.3 — corpus].

# L'état de l'art en services financiers (Vol. VIII)

L'état de l'art demande si ce qui vaut pour l'entreprise vaut pour une coopérative financière canadienne régie, faits arrêtés au 20 août 2026, sous un régime de vérification individuelle sans ronde adverse, les faits protocolaires étant repris du corpus compagnon [VIII §1 — déclaration · VIII §2.1 — déclaration].

## La pile n'est pas ce qui décide

Trois surveillants se partagent le périmètre : l'AMF pour les caisses, la Fédération et certaines filiales d'assurance ; le BSIF pour l'assurance de dommages, la garde de valeurs et les services fiduciaires ; l'OCRI pour le courtage. Une exécution d'agent porte donc trois qualifications selon l'entité qui l'invoque, et le fait qui décide — l'identité de l'appelant — est l'attribut qu'aucun des trois protocoles ne rend opposable [VIII §4.2 — individuel]. B-10 inclut explicitement sociétés affiliées et filiales dans les ententes de tiers, sans exemption ni allègement ; une plateforme agentique mutualisée exploitée par la Fédération est une entente de tiers pour l'entité fédérale qui la consomme et un actif interne pour la caisse : le même serveur MCP est deux objets réglementaires [VIII §4.3, réf. 25 — individuel]. La thèse générale de l'écart entre adoption et assurance a sa version canadienne chiffrée. Deux campagnes indépendantes sur des serveurs MCP publics, toutes deux des prépublications non révisées, convergent sur l'absence d'authentification — 40,55 % de 7 973 serveurs distants, 91,8 % de 414 serveurs audités —, et 41,6 % des serveurs confirmés disparaissent en trois jours : une population d'outils qui s'évapore ainsi est structurellement incompatible avec un inventaire [VIII §10.2, réf. 129, 15 — individuel, sans revue]. Côté institutions, le rapport conjoint du BSIF et de l'ACFC relève environ 50 % d'institutions financières fédérales utilisant l'IA en 2023 et 70 % attendues en 2026, la gestion du risque accusant du retard sur l'adoption [VIII §10.2 — individuel]. Aucune ligne du récapitulatif des écarts entre entreprise générique et coopérative régie ne porte sur un protocole : ce n'est pas le choix de la pile qui décide [VIII §4.10 — individuel]. La structure fédérée fait même passer à l'intérieur du périmètre du groupe une frontière qui est, en droit, inter-organisationnelle : l'état de l'art y voit, par une inférence qu'il déclare, un banc d'essai inter-organisationnel dont les concurrents intégrés ne disposent pas [VIII §10.4 — inférence].

## Le modèle est régi, la chaîne ne l'est pas

E-23, finale le 11 septembre 2025 et en vigueur le 1er mai 2027, définit le modèle de façon à englober les méthodes d'IA et exige un inventaire d'entreprise permanent ; les mots « agent », « agentique » et « orchestration » n'y figurent pas [VIII §4.4, réf. 28 — individuel]. Un agent n'est pas un objet stable — un modèle, des outils, un contexte et un mandat, dont trois termes sur quatre peuvent changer sans qu'aucune version ne bouge — : aucun texte ne définit l'unité d'inventaire qu'il faudrait, et la contrainte s'applique deux fois, sous deux autorités [VIII §4.4 — individuel]. Le bulletin du BSIF de juillet 2026 est le seul texte du régulateur prudentiel canadien qui décrive la chaîne plutôt que le modèle — identités non humaines uniques, moindre privilège, points d'approbation, journalisation —, au registre non contraignant des saines pratiques [VIII §4.4, réf. 29 — individuel]. Au total, l'état de l'art relève dix endroits où aucun texte ne dit ce qu'il advient ; entre autres, aucun texte qui lie une institution canadienne n'exige que l'agent dise pour le compte de qui il agit, aucune taxonomie d'incident ne couvre l'action d'un agent hors mandat, et aucun coût de capital n'est attaché à l'autonomie [VIII §9.11 — individuel].

Le décalage tient en trois lignes : ce qui oblige ne nomme pas l'agent ; ce qui nomme l'agent n'oblige pas ; ce qui exécute l'agent n'exprime ni l'un ni l'autre [VIII §10.1 — individuel].

## Les échéances, dans leur ordre réel

La séquence est inverse de celle qu'on suppose : la continuité oblige avant l'inventaire [VIII §4.5 — individuel].

| Date | Instrument | Ce qui compte pour un agent |
|:------------|:------------------------|:--------------------------------------|
| 24 août 2026 | règlement administratif du RTR, DORS/2026-133 | un message de paiement ne peut être ni modifié ni révoqué après émission [VIII §8.5, réf. 115 — individuel] |
| 1er sept. 2026 | E-21 (BSIF), conformité complète visée | opérations critiques cartographiées de bout en bout, dépendances aux tiers comprises [VIII §4.5, réf. 26 — individuel] |
| 1er avril 2027 | ligne directrice de l'AMF sur les tiers | ententes intragroupes visées ; relevée sur la page officielle, PDF normatif inaccessible [VIII §4.3 — individuel] |
| 1er mai 2027 | E-23 (BSIF) et ligne directrice de l'AMF sur l'IA, le même jour | inventaire des modèles ; imputabilité d'un dirigeant pour les systèmes d'IA [VIII §9.12 — individuel] |
| au plus tôt 28 juil. 2027 | politique de cycle de vie de MCP | premier retrait possible d'une fonctionnalité dépréciée, engagement non opposable [VIII §12.1 — individuel] |
| 2 déc. 2027 et 2 août 2028 | règlement européen, haut risque | obligations des annexes III et I, reportées [VIII §12.1 — individuel] ; leur portée sur les agents n'est pas établie par l'état de l'art [VIII §9.12 — individuel] |

: Les échéances qui bornent la fenêtre d'une coopérative financière régie, dans l'ordre où elles tombent.

Des quatre échéances que l'état de l'art place en tête du calendrier d'une institution québécoise — E-21, la ligne directrice sur les tiers, E-23 et la ligne directrice sur l'IA —, aucune n'exige quoi que ce soit au sujet des agents, et toutes les quatre s'appliqueront à eux [VIII §9.12 — individuel]. Les autres lignes ne sont pas de même nature : le règlement du RTR vise le message de paiement [VIII §8.5, réf. 115 — individuel] ; la politique de cycle de vie de MCP est un engagement du projet, non opposable [VIII §12.1 — individuel] ; et la portée du haut risque européen sur les agents n'est pas établie [VIII §9.12 — individuel].

## Le rail irrévocable, et l'opération à moitié exécutée

Lynx est un système de règlement brut en temps réel où « once settled, a payment is final and irrevocable » : il n'existe pas de transaction compensatoire au-dessus de Lynx, et le point d'approbation doit précéder l'effet [VIII §4.6, réf. 36 — individuel]. Au Canada, en août 2026, aucune voie légitime n'existe par laquelle un agent tiers initierait un paiement au nom d'un client : l'open banking est en lecture seule, aucune règle publiée n'admet d'initiateur non humain sur le RTR, la loi sur les cryptoactifs stables n'est pas en vigueur [VIII §10.5 — individuel].

La révision `2026-07-28` de MCP a retiré la reprise de flux et la redélivrance, fait d'une déconnexion du client une annulation, et oblige le client à réémettre sous un nouvel identifiant : un agent qui appelle directement un serveur MCP, sans étape durable interposée, ne peut pas répondre après un incident réseau à la question « le débit a-t-il eu lieu » [VIII §8.4 — individuel]. L'historique d'exécution des substrats durables vit 90 jours au mieux chez Step Functions *Standard* et 3 jours par défaut chez Temporal auto-hébergé, quand la loi sur le recyclage des produits de la criminalité impose de conserver les relevés au moins cinq ans et de les produire dans les trente jours : l'historique d'un moteur d'exécution durable n'est pas une piste d'audit réglementaire [VIII §8.3 — individuel]. *Note de lecture* : la section écrit « quatre-vingt-dix jours au mieux » pour l'ensemble des substrats, mais la notice qu'elle cite pour Temporal auto-hébergé donne, à partir de la version `v1.18`, un maximum non borné ; le plafond de 90 jours vaut pour Step Functions *Standard* et Temporal Cloud [VIII §8.3, réf. 205, 208, 209 — individuel].

## La preuve plutôt que la signature

Au 20 août 2026, douze brouillons individuels traitent de la chaîne de délégation, tous « not endorsed by the IETF », et le groupe OAuth ne porte aucun document de groupe consacré aux agents : le déficit n'est pas d'invention, il est d'adoption [VIII §7.4.2 — individuel]. Le mécanisme le plus avancé dans la filière de normalisation qui réponde à « pour qui agis-tu » est le jeton de transaction du groupe OAuth, en dernier appel de groupe : déployable à l'intérieur d'un domaine de confiance, mais immuable, donc sans atténuation par saut, et incapable de franchir la frontière organisationnelle [VIII §7.4.1, réf. 159 — individuel].

La *Loi sur la preuve au Canada* demande que la fiabilité du système d'archivage électronique soit démontrée (art. 31.2) et la présume quand l'enregistrement se fait dans le cours ordinaire des affaires : la totalité des douze brouillons investit dans la signature de l'artefact, le régime de preuve canadien dans la fiabilité du système d'enregistrement [VIII §7.7.1, réf. 185 — inférence]. En droit québécois, une chaîne de mandat n'a pas besoin d'être normalisée pour être opposable — le lien peut être établi par tout procédé qui maintient l'intégrité (art. 38 et 39 de la loi sur le cadre juridique des technologies de l'information) ; ce qui manque est un mécanisme qu'une contrepartie puisse vérifier de façon interopérable [VIII §7.7.2, réf. 188 — individuel].

Lu par l'état de l'art, le Code civil fait d'un agent logiciel non un mandataire mais un instrument, chaque saut étant imputé à l'institution — lecture qu'aucune décision, position de l'Autorité ni doctrine québécoise n'a tranchée [VIII §7.4.4, réf. 187 — inférence]. Et la révocation d'un mandat n'est pas opposable au tiers de bonne foi qui l'ignorait (art. 2162) : la révocation en cascade confine le dommage, elle n'annule pas l'opération, et aucune source technique ne propose la sémantique de compensation qu'il faudrait [VIII §7.5, réf. 187 — inférence].

L'institution assujettie n'arrive pas pour autant les mains vides devant l'admission d'un agent tiers. Depuis le 1er octobre 2025, elle peut faire vérifier l'identité d'une personne par un agent ou mandataire à trois conditions cumulatives — une entente écrite préalable, les méthodes qu'elle aurait dû employer elle-même, et celles que le règlement prescrivait au moment de la vérification ; l'état de l'art y lit, par une extension qu'il déclare inférence, un patron d'admission d'agent tiers déjà opposable [VIII §7.6 — inférence].

## La supervision humaine, hypothèse contredite

Trois instruments applicables convergent vers l'humain dans la boucle ; la littérature arbitrée ne soutient pas l'hypothèse qu'il corrige la machine, et se contredit sur le sens de l'effet : lorsque le soutien algorithmique erroné précède le jugement, 36,8 % de décisions exactes contre 66,2 % lorsque le jugement précède le soutien, quand une étude de terrain chez des praticiens formés conclut en sens contraire [VIII §10.3 — individuel]. L'état de l'art ne tranche pas la contradiction et en tire deux gestes : ne pas exposer la recommandation avant la consigne du réviseur sur les dossiers à fort impact, et instrumenter le taux d'infirmation [VIII §10.3 — recommandation].

## Sept arbitrages datés, cinq suspendus

L'architecture qui survit à l'examen rend démontrable devant un tiers la chaîne allant du mandat du client à l'effet produit : un cadre d'exécution déterministe qui invoque les agents, des protocoles ouverts à la frontière seulement, une identité non humaine unique par agent, un journal probatoire dont la propriété n'est pas déléguée au fournisseur, et des points d'approbation placés avant l'effet irréversible [VIII §11.1 — recommandation].

| Arbitrage | Recommandation de l'état de l'art | Échéance |
|:----------------|:----------------------------------------|:-----------|
| A1 Frontière d'outils | passerelle interne obligatoire, sans exception [VIII §11.2 — recommandation] | 31 déc. 2026 |
| A2 Identité d'agent | identité non humaine unique, mandat porté hors bande ; le seul arbitrage qui ne se rattrape pas rétroactivement [VIII §11.2 — recommandation] | 31 déc. 2026 |
| A3 Patron d'orchestration | hiérarchique, augmenté de cache, routage et reprise [VIII §11.2 — recommandation] | 31 mars 2027 |
| A4 Cœur ou frontières | cœur consolidé dans le périmètre régi, protocoles aux frontières [VIII §11.2 — recommandation] | 30 juin 2027 |
| A5 Décider ou recommander | choisir par la mesure du taux d'infirmation [VIII §11.2 — recommandation] | 30 sept. 2027 |
| A6 Journal probatoire | registre de mandat en ajout seul, sous contrôle de l'institution [VIII §11.2 — recommandation] | 31 déc. 2026 |
| A7 Agilité cryptographique | interdire les conceptions figées, ne pas migrer maintenant [VIII §11.2 — recommandation] | 31 déc. 2026 |

: Les arbitrages datés de l'état de l'art et leur échéance de décision.

Cinq arbitrages restent suspendus, chacun avec le signal qui le rouvre ; le premier, le paiement agentique, l'est tant que quatre verrous restent fermés simultanément [VIII §11.3 — recommandation].

# Ce que les volumes se disent entre eux

La veille et la revue ne se valident pas l'une l'autre, et la revue le dit : la veille dit ce que le monde déployé fait, la revue ce que la littérature sait, et les deux exercices ne répondent pas à la même question [VII §1.2 — déclaration]. L'état de l'art cite ses devanciers à régime différencié — la veille pour les faits protocolaires, de gouvernance et de sécurité, la revue pour l'état de la littérature et la mesure de sa fragilité —, jamais pour une obligation opposable [VIII §2.3 — déclaration].

La revue a soumis trois énoncés de la veille à la littérature : deux en sortent modifiés — le déficit de délégation est d'adoption et non d'invention, la dissymétrie entre agents et formalismes de processus est industrielle et non scientifique —, et le troisième est confirmé par une seconde voie, plus sévère [VII §15 — corpus].

L'état de l'art corrige à son tour l'énoncé porteur de la veille sur les deux sauts : la partie juridique tombe, puisqu'une chaîne de mandat opposable en droit québécois n'a pas besoin d'être normalisée ; la partie technique et contractuelle tient [VIII §7.7.2 — individuel]. Il met aussi à jour le relevé de la veille : soixante-trois attributs `gen_ai.*` le 15 août, soixante-douze le 20 août 2026, les neuf ajoutés portant tous sur la comptabilité des jetons, et aucun des soixante-douze ne décrit un mandat [VIII §8.8 — individuel].

Sur la ligne directrice de l'AMF sur l'IA, la veille retient une finalisation au 7 avril 2026 et déclare cette date non reconfirmée en source primaire [VI §13.6 — secondaire] ; l'état de l'art établit une couverture de mars 2026 et une fiche d'avril 2026, et laisse la date d'annonce ni confirmée ni infirmée [VIII §14 — individuel].

Les volumes partagent un auteur, et la veille le range au premier rang de ses limites : deux textes du même auteur qui se confirment ne constituent pas une réplication indépendante [VI §13.7 — déclaration].

# Questions ouvertes

Chaque volume donne la liste complète de ses questions à la section citée ; celles-ci sont parmi les plus directement testables.

1. Laquelle des familles d'identité — OAuth et OIDC, identités décentralisées, SPIFFE et WIMSE — s'imposera, et lequel des brouillons de chaîne à N sauts sera adopté, et quand [VI §11, QO 2 — question] ?
2. L'enveloppe d'orchestration suffira-t-elle à la conformité sectorielle, ou faudra-t-il des propriétés vérifiables dans les protocoles [VI §11, QO 13 — question] ?
3. Les conventions d'observabilité d'OpenTelemetry pour l'IA générative, sans version publiée ni échéancier, seront-elles stables avant 2027 [VI §11, QO 17 — question] ?
4. L'exigence de révision humaine est documentée ; son efficacité ne l'est nulle part [VI §11, QO 22 — question].
5. L'écosystème du protocole le plus adopté absorbera-t-il la rupture du 28 juillet 2026 dans sa fenêtre de douze mois [VI §11, QO 23 — question] ?
6. Quelle fraction des agents en service subit une tentative d'injection, et à quel taux d'aboutissement [VII §16 — question] ?
7. Pour une tâche qui passe d'A2A à MCP entre deux organisations en exploitation, quels taux d'échec, quelle latence ajoutée, quelle perte sémantique [VII §16 — question] ?
8. Qu'est-ce qu'E-23 compte comme un modèle lorsqu'un agent est fait d'un modèle, d'un jeu d'outils, d'un contexte et d'un mandat modifiables entre deux exécutions [VIII §13, QO 1 — question] ?
9. À partir de quel taux d'infirmation une révision humaine cesse-t-elle d'être significative au sens du critère québécois [VIII §13, QO 2 — question] ?
10. Les identités non humaines que le BSIF attend sont-elles uniques par agent logique, par instance d'exécution ou par mandat [VIII §13, QO 5 — question] ?
11. Une règle d'exploitation du RTR traitera-t-elle l'initiation par un mandataire non humain, et sous quel régime de responsabilité [VIII §13, QO 6 — question] ?
12. Que révoque-t-on lorsqu'un mandat est retiré après qu'un agent a produit un effet irrévocable [VIII §13, QO 14 — question] ?
13. Quels *fitness* et quelle précision pour une trace d'agent alignée contre un modèle de processus [VII §16 — question] ?
14. Qui répond d'une transaction agentique non autorisée — émetteur, acquéreur, marchand ou fournisseur d'agent ? Aucune pièce du corpus ne modélise cette répartition [VII §9.3 — question].

# Limites que les volumes déclarent

Ni la revue ni l'état de l'art ne mesurent de déploiement. La revue rapporte ce que les pièces revendiquent, sans réplication [VII §2.3 — déclaration] ; l'état de l'art ne mesure aucun déploiement agentique dans une institution financière canadienne, et aucune source consultée n'établit qu'une coopérative financière canadienne en exploite un en production sur un processus régi [VIII §14 — déclaration].

Le régulateur québécois refuse la consultation automatisée (HTTP 403) : la veille ne tient ses énoncés AMF qu'au conditionnel [VI §10 — déclaration] ; l'état de l'art n'a atteint le texte de la ligne directrice sur l'IA que par un service tiers d'extraction non reproductible, et marque chaque énoncé AMF à l'endroit où il s'en sert [VIII §14 — déclaration].

Ni la veille ni la revue ne sont des revues systématiques au sens PRISMA [VI §2.3 — déclaration · VII §2.3 — déclaration]. Leurs objets se périment vite : la veille a vu un décompte exact à son gel devenir faux dix jours plus tard [VI §2.3 — déclaration] ; la revue mesure une vitesse de péremption de son corpus qui se compte en semaines [VII §18 — déclaration].

Leur portée, enfin, est bornée. L'état de l'art n'examine au niveau de l'exécution que le métier bancaire, par l'ordre de paiement ; l'assurance de dommages, l'assurance de personne et la gestion de patrimoine n'y figurent qu'à titre d'entités du périmètre supervisé et de champs d'application des lignes directrices [VIII §14 — déclaration]. Le biais anglophone de la revue reste entier [VII §17 — déclaration].

# Les chiffres porteurs, et où les vérifier

Chaque ligne reprend un chiffre des sections précédentes, avec ce qu'il mesure et sa portée ; le renvoi est celui du passage qui le porte.

| Chiffre | Ce qu'il mesure, et sa portée | Où le vérifier |
|:---------------------|:----------------------------------------------------|:---------------------------|
| 414 · 68 · 91,8 % | serveurs MCP publics audités à l'exécution ; vulnérabilités relevées ; part sans authentification OAuth — audit du 31 juillet 2026, prépublication non révisée | [VI §7.1, réf. 272 — individuel, sans revue] |
| 40,55 % de 7 973 | serveurs MCP distants exposant des outils sans aucune authentification | [VII §6.1, réf. 81 — sans revue] |
| 41,6 % en trois jours | serveurs confirmés disparus entre deux passes de mesure ; même prépublication non révisée | [VIII §10.2, réf. 15 — individuel, sans revue] |
| 21 767 | enregistrements de dernière version au registre MCP officiel, le 15 août 2026 ; déclarations d'éditeur, non serveurs vérifiés | [VI §6.3, réf. 340 — individuel] |
| 63, puis 72 | attributs `gen_ai.*` d'OpenTelemetry au 15 puis au 20 août 2026, tous au statut de développement, aucun sur le mandat | [VI §4.13 — individuel · VIII §8.8 — individuel] |
| douze au moins, aucun adopté | brouillons individuels de chaîne de délégation à l'IETF ; un plancher établi par balayage par mot-clé, non un inventaire | [VI §7.7 — individuel · VIII §7.4.2 — individuel] |
| vingt-sept, aucun adopté | brouillons portés par les groupes DAWN et DMSC au 15 août 2026 | [VI §4.10, réf. 159 — individuel] |
| 21 % (n = 418) | organisations dotées d'un processus formel de mise hors service des agents ; sondage commandité | [VI §7.1, réf. 110 — individuel] |
| plus de 40 % | projets d'IA agentique annulés d'ici fin 2027 ; prévision de Gartner, juin 2025 | [VI §12.2, réf. 80 — individuel] |
| 145 sur 189 · 77 % | pièces arXiv du corpus sans signe de revue par les pairs à leur notice ; plafond du non-arbitré, non part du champ | [VII §3.1 — corpus] |
| 67 sur 123 · 54 % | pièces des dix fronts qui évaluent un artefact de leurs propres auteurs | [VII §14.3 — corpus] |
| 96,89 % | serveurs déclarés « à risque » par des scanners à moins de 50 % de vrais positifs | [VII §4.2, réf. 51 — sans revue] |
| 53,5 % · 14,2 % | attribution automatique de la défaillance : agent fautif, étape décisive | [VII §7.1, réf. 88 — autodéclarée] |
| 90,0 % sur 18 000 missions | co-défaillance de deux instances d'un même modèle | [VII §13.1, réf. 180 — sans revue] |
| 22 sur 96 contre 0 sur 96 | violations admises par un garde lisant l'autorité dans l'état local, contre application par provenance, en scénarios de blanchiment | [VII §15.3, réf. 192 — sans revue] |
| 3 391 | cas de test du kit de conformité public de DMN, adossé à une norme, là où les suites de MCP et d'A2A ne sont que d'écosystème | [VI §4.11.3 — pipeline] |
| 90 jours · 3 jours · cinq ans | rétention d'historique d'exécution : au plus chez Step Functions *Standard* et Temporal Cloud ; par défaut chez Temporal auto-hébergé, dont le maximum n'est pas borné depuis `v1.18` ; contre conservation exigée des relevés | [VIII §8.3 — individuel] |
| 66,2 % contre 36,8 % | décisions exactes selon que le jugement précède ou suit le soutien algorithmique erroné | [VIII §10.3 — individuel] |
| 50 % puis 70 % | institutions financières fédérales utilisant l'IA en 2023, et attendues en 2026 | [VIII §10.2 — individuel] |
| quinze croisements | protocoles croisés avec des textes canadiens dans la monographie compagnon : aucun lien documenté | [VI §8.4, réf. 218 — compagnon] |
| 269 = 179 + 54 + 30 + 6 | références rouvertes par l'audit du 8 août 2026 : confirmées, corrigées, non reconfirmables, auto-citations ; aucune introuvable | [VI §2.2 — déclaration] |

: Les chiffres porteurs des volumes, leur portée et le passage qui les porte.

# Références {-}

**Documents synthétisés et pièces d'appareil**

- **[VI]** A.-G. Bruneau. *Veille technologique en entreprise — Interopérabilité et Orchestration Agentiques*. Édition du 15 août 2026. `3 - Veille/Veille Technologique.pdf`, source `Veille Technologique.md`. Corpus de l'auteur, auto-publié, non arbitré.
- **[VII]** A.-G. Bruneau. *Revue de la littérature académique — Interopérabilité et Orchestration Agentiques*. Édition du 15 août 2026. `3 - Veille/Revue de littérature.pdf`, source `Revue de littérature.md`. Corpus de l'auteur, auto-publié, non arbitré.
- **[VIII]** A.-G. Bruneau. *État de l'art en services financiers — Interopérabilité et Orchestration Agentiques*. Faits arrêtés au 20 août 2026. `5 - Recension/État de l'art — services financiers.pdf`, source du même nom en `.md`. Corpus de l'auteur, auto-publié, non arbitré.
- **[CONTRIB]** *Contributions — qui a fait quoi, pièce par pièce*. `CONTRIBUTIONS.md`, à la racine du dépôt, déclaration du 15 septembre 2026.
- **[PLAN]** *Plan d'exécution — mise en œuvre de l'évaluation académique du 15 septembre 2026*. `Plan d'exécution — évaluation académique.md`, à la racine du dépôt ; phase 5, relecture humaine externe.

**Notices reprises des volumes** — chacune sous le numéro qu'elle porte dans la bibliographie du volume, avec un fragment de la notice ; la source primaire est à l'adresse que la notice donne.

- **VI [80]** « Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 »
- **VI [82]** « Agentic AI to Dominate IT Budget Expansion Over Next Five Years, Exceeding 26% of Worldwide IT Spending, and $1.3 Trillion in 2029 »
- **VI [110]** « New Cloud Security Alliance Survey Reveals 82% of Enterprises Have Unknown AI Agents in Their Environments »
- **VI [159]** « BoF requests » et pages de documents des groupes chartés
- **VI [209]** « Ligne directrice E-23 — Gestion du risque de modélisation »
- **VI [212]** « Décision fondée exclusivement sur un traitement automatisé »
- **VI [218]** « L'autonomie encadrée — interopérabilité et orchestration agentique dans les services financiers canadiens (état des lieux 2024-2026) »
- **VI [252]** « Key Changes » — journal des changements de la révision 2026-07-28
- **VI [254]** Règlement (UE) 2026/1744 du 8 juillet 2026
- **VI [260]** « Why Do Multi-Agent LLM Systems Fail? »
- **VI [269]** « close to half-a-billion downloads a month »
- **VI [270]** « surpassed 400M monthly SDK downloads, a 4x increase this year »
- **VI [272]** Audit dynamique de 414 serveurs MCP publics
- **VI [274]** Bulletin « Generative and Agentic AI »
- **VI [336]** « Guidelines on the implementation of the transparency obligations for certain AI systems under Article 50 of the AI Act »
- **VI [340]** Registre officiel — API publique `GET /v0/servers`
- **VII [51]** « Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability »
- **VII [53]** « Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions »
- **VII [54]** « An Empirical Study of Model Context Protocol Applications »
- **VII [55]** « Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications »
- **VII [71]** « AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents »
- **VII [76]** « SentinelAgent: Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems »
- **VII [77]** « HDP: A Lightweight Cryptographic Protocol for Human Delegation Provenance in Agentic AI Systems »
- **VII [81]** « A First Measurement Study on Authentication Security in Real-World Remote MCP Servers »
- **VII [83]** « Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI »
- **VII [84]** « Observability for Delegated Execution in Agentic AI Systems »
- **VII [85]** « Formal Security Analysis of Agent Protocol Composition »
- **VII [88]** « Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems »
- **VII [95]** « When Does Multi-Agent Collaboration Help? An Entropy Perspective »
- **VII [126]** « Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows »
- **VII [127]** « Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows »
- **VII [131]** « Neuro-Symbolic Agents for Regulated Process Automation: Challenges and Research Agenda »
- **VII [133]** « Towards Modeling Human-Agentic Collaborative Workflows: A BPMN Extension »
- **VII [134]** « Specifying AI-SDLC Processes: A Protocol Language for Human-Agent Boundaries »
- **VII [137]** « Hybrid AI for Explainable and Accurate Conversational Agents in eGovernment »
- **VII [143]** « Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI »
- **VII [180]** « Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence »
- **VII [190]** « Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations »
- **VII [192]** « Multi-Agent AI Safety as an Institutional Design Problem »
- **VIII [15]** « Exposed by Design: A Dynamic Security Assessment of Internet-Facing MCP Servers at Scale »
- **VIII [25]** « Third-Party Risk Management Guideline » — ligne directrice **B-10**
- **VIII [26]** « Operational Risk Management and Resilience Guideline » — ligne directrice **E-21**
- **VIII [28]** « Guideline E-23 — Model Risk Management (2027) »
- **VIII [29]** « Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security, and Operational Resilience »
- **VIII [36]** « An Overview of Lynx, Canada's High-Value Payment System »
- **VIII [115]** « Règlement administratif n° 10 de l'Association canadienne des paiements — STIR », DORS/2026-133
- **VIII [129]** « A First Measurement Study on Authentication Security in Real-World Remote MCP Servers »
- **VIII [159]** « Transaction Tokens »
- **VIII [205]** « Choosing workflow type in Step Functions »
- **VIII [208]** « Temporal Service » — documentation, section *Retention Period*
- **VIII [209]** « Namespaces » — documentation Temporal Cloud
- **VIII [185]** *Loi sur la preuve au Canada*, L.R.C. (1985), ch. C-5, art. 31.1 à 31.8
- **VIII [187]** *Code civil du Québec*, RLRQ c. CCQ-1991, chapitre neuvième « Du mandat »
- **VIII [188]** *Loi concernant le cadre juridique des technologies de l'information*, RLRQ c. C-1.1
