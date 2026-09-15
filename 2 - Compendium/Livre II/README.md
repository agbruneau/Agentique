# Livre II — Faire confiance : identité, délégation et fabrique de confiance

Le deuxième des cinq Livres du [Vol. IV](../README.md) : dix chapitres sur la capacité d'émettre une identité opposable, avec ses
versants hostile (ch. 19-20) et post-quantique (ch. 21). Chaque pièce existe en `.md`, la source qui fait foi et seule à porter
l'appareil, et en `.html`, page autonome qui se lit hors ligne. Le cahier des charges de chaque chapitre est son entrée au
[`TOC.md`](../PRD/TOC.md), qui prime.

**Statut :** archive de travail, hors compte des livrables — le Vol. IV entier, par la décision [D-18](../PRD/PRD.md#d-18) du
15 septembre 2026. Les dix pièces sont rédigées et arbitrées hors portes, brouillon non publiable ; aucun énoncé n'y est central au
sens de CA-IV-01.

| Ch. | Pièce | Plan |
|---|---|---|
| 12 | [L'héritage et les standards étirés : un demi-siècle d'identités non humaines, puis OAuth, OIDC et SCIM face à l'agent](12-heritage-standards-etires.md) · [html](12-heritage-standards-etires.html) | émettre |
| 13 | [L'identité décentralisée : VC, DID et la promesse du portable](13-identite-decentralisee-vc-did.md) · [html](13-identite-decentralisee-vc-did.html) | émettre |
| 14 | [La grille des cinq questions](14-grille-cinq-questions.md) · [html](14-grille-cinq-questions.html) | émettre |
| 15 | [Émettre : Agent Card signée, annuaires, registres gouvernés](15-emettre-carte-annuaires-registres.md) · [html](15-emettre-carte-annuaires-registres.html) | émettre |
| 16 | [Le passeport d'agent : synthèse d'un objet encore virtuel](16-passeport-agent.md) · [html](16-passeport-agent.html) | émettre |
| 17 | [La chaîne de mandat et le problème des deux sauts](17-chaine-mandat-deux-sauts.md) · [html](17-chaine-mandat-deux-sauts.html) | émettre |
| 18 | [Know Your Agent : la vérification d'agent tiers inter-domaines](18-know-your-agent.md) · [html](18-know-your-agent.html) | émettre |
| 19 | [Taxonomie des attaques d'identité et de délégation](19-taxonomie-attaques-identite-delegation.md) · [html](19-taxonomie-attaques-identite-delegation.html) | confiance hostile |
| 20 | [Usurpation, révocation et boucle défensive : du *rug-pull* à l'*agentic SOC*](20-usurpation-revocation-boucle-defensive.md) · [html](20-usurpation-revocation-boucle-defensive.html) | confiance hostile |
| 21 | [L'horloge post-quantique : menace sur la pile identitaire, crypto-agilité et dette de migration](21-horloge-post-quantique.md) · [html](21-horloge-post-quantique.html) | horloge post-quantique |

Volumétrie : 68 743 mots de corps, mesurés par [`decompte.sh`](../PRD/decompte.sh) et reportés ici par `reporter-volumetrie.py`, pour une
enveloppe de Livre de 50 000 au TOC, soit +37,5 %.

**Par où entrer :** le ch. 14, la grille des cinq questions — qui es-tu, qui t'a créé, pour qui agis-tu, que peux-tu faire, qui en
répond —, instrument de lecture de tout mécanisme d'identité ; puis le passeport d'agent (ch. 16) et la chaîne de mandat (ch. 17).

**Refaire et vérifier :** depuis `2 - Compendium/`, `python build/rendre-piece.py "Livre II/<pièce>.md"` régénère un `.html`, qui ne
s'édite jamais à la main, et `python build/verifier-piece.py` l'oppose à sa source ; les contrôles du volume sont à sa
[page d'accueil](../README.md).

**Journal :** [la page de ce Livre au journal du volume](../JOURNAL.md#page-livre-ii) — clôture et arrêt, volumétrie datée, sièges
marqués pour la somme, remontées soldées le 27 juillet 2026, passe de correction du 28 et règle de comptage des en-têtes.
