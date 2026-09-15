# 3 - Veille — mesurer le champ

Quatre documents publiés et l'appareil qui les contrôle. La [veille technologique](Veille%20Technologique.md) dit ce que le monde déployé
fait, sur spécifications, dépôts et textes réglementaires ; la [revue de littérature](Revue%20de%20litt%C3%A9rature.md) dit ce que la
littérature académique sait, et à quel régime de preuve. La [note de veille SDLC](Note-veille-SDLC-agentique.md) instruit une source
unique, un entretien ; la [note de synthèse](Note%20de%20synth%C3%A8se.md) condense la veille, la revue et l'[état de l'art](../5%20-%20Recension/).

| Document | Rendu | Gel ou rédaction | Statut, fixé le 15 septembre 2026 par [D-18](../2%20-%20Compendium/PRD/PRD.md#d-18) |
|---|---|---|---|
| Vol. VI — *Veille technologique en entreprise* | [PDF](Veille%20Technologique.pdf), 145 p., 342 références | 15 août 2026 | livrable |
| Vol. VII — *Revue de la littérature académique* | [PDF](Revue%20de%20litt%C3%A9rature.pdf), 60 p., 192 références | 15 août 2026 | livrable |
| *La transformation du cycle de vie du développement logiciel à l'ère des agents* | [PDF](Note-veille-SDLC-agentique.pdf), 50 p. | 27 août 2026 | publiée, hors livrables : source unique, bibliographie non appariée |
| *Note de synthèse — veille, revue et état de l'art* | [PDF](Note%20de%20synth%C3%A8se.pdf), 22 p. | 15 septembre 2026 | publiée, hors livrables : rédigée par un modèle de langage, non relue par un humain |

Dépôt rouvert le 15 septembre 2026 par [D-17](../2%20-%20Compendium/PRD/PRD.md#d-17) ; aucun des quatre n'a de relecteur humain nommé.

**Par où entrer :** la note de synthèse pour l'essentiel, chaque affirmation renvoyée à sa section et au niveau de preuve que le volume
déclare ; la veille pour l'état du champ, sa section 13 rendant compte des volumes du corpus ; la revue pour ce qui a franchi un comité —
12 pièces attestées et 145 sans signe de revue à leur notice, sur 189 arXiv : un plafond du non-arbitré, non une part du champ.

**Refaire :** depuis ce dossier, `bash build/build-pdf.sh` recompose la veille et la revue, `veille` ou `revue` pour une seule, et mesure
leur page de titre ; la note SDLC n'est pas au script et se refait par
`pandoc "Note-veille-SDLC-agentique.md" --pdf-engine=typst --toc -o "Note-veille-SDLC-agentique.pdf"` ;
`python Python/check-synthese.py --rendre` recompose la note de synthèse.

**Vérifier :** `python Python/check-veille.py` et `python Python/check-revue.py` opposent chaque livrable à ses renvois, à ses cardinaux et
à sa bibliographie ; `python Python/check-synthese.py` confronte la note de synthèse à ses trois sources, et son harnais
`python Python/check-synthese-mutations.py` prouve qu'il voit ses fautes ; `python Python/check-resume.py <pdf>` mesure la page de titre
d'un rendu. Aucun contrôle de source ne tient la note SDLC, et aucune pagination n'est opposée à une cible hors la note de synthèse.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — naissance et renommages du dossier, collisions de titres et leur levée, chaînes de rendu, ce que
chaque contrôle a vu et manqué, relevés datés et réserves.
