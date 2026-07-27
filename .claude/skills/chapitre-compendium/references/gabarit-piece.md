# Gabarit d'une pièce — le `.md` source

Squelette à copier puis à remplir. Les blocs entre `<< … >>` sont des points de substitution ; les
lignes en *italique commenté* expliquent ce que le bloc refuse, et **ne se recopient pas** dans la
pièce.

Le fichier se nomme `NN-slug.md` sous `2 - Compendium/Livre <N>/` — `NN` sur deux chiffres, `slug` en
minuscules sans accents ni espaces, dérivé du titre (`01-interoperabilite-integration-entreprise`).

---

````markdown
# Chapitre << N >> — << titre exact repris du TOC, sans le reformuler >>

*Livre << N >> — << titre du livre >>.
<< Premier | Second | … >> mouvement — << nom du mouvement >> (ch. << a >>-<< b >>).*

| Champ | Valeur |
|---|---|
| **Statut** | << « Rédigé » — ou « **Brouillon de rédaction, non publiable** », avec le motif : quelles portes sont ouvertes, sur quelle instruction et à quelle date. Si la règle cardinale du PRD §5 est enfreinte, la citer et la déclarer enfreinte, en renvoyant à la note de statut. >> |
| **Date de gel** | << « Aucune » tant que D-1 n'est pas prise. Nommer le gel de la source consommée — juin 2026 (Vol. I), 16-17 juillet 2026 (Vol. II), 21 juillet 2026 (Vol. III) — **en précisant qu'il n'est pas le gel de la somme et ne peut en tenir lieu**. >> |
| **Socle mobilisé** | << Contre quoi les énoncés résolvent réellement, et à quel régime. Tant que G-3 est ouverte : « aucune entrée du socle consolidé », l'Annexe B n'existant pas. Nommer la source et son régime d'héritage ([C] pour le Vol. I, niveau conservé pour les Vol. II et III), puis en tirer la conséquence sur CA-IV-01. >> |
| **Garde-fous balayés** | << Les deux séries, nommées par volume, **y compris les zéros**. Signaler les faux amis (« plan de contrôle » pré-agentique ≠ « control plane » de R-13). Compter les occurrences réelles de ceux qui s'appliquent, et dire où elles sont. >> |
| **Volumétrie cible** | << Enveloppe **dérivée** de celle du Livre, avec sa dérivation écrite ; puis le rappel que tant que G-2 est ouverte, aucun décompte n'est publiable. >> |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v<< version >>, entrée du chapitre << N >>)* — << thèse verbatim, sans reformulation >>

---

## § << N >>.0 — << titre de la section d'ouverture >>

<< Poser l'objet, le parti pris, et **ce que le chapitre ne traite pas** — les sorties de périmètre
de la table de couverture, nommées au moment où le lecteur les attendrait, pour qu'on ne les prenne
pas pour un oubli. >>

### << N >>.0.1 << titre de sous-section, repris de la table détaillée >>

<< Prose. >>

## § << N >>.1 — << … >>

<< Une section `##` par entrée `#### § N.M` de la table détaillée du TOC, dans l'ordre exact.
Les sous-sections `###` et `####` suivent les puces de la table. Ne pas réordonner : la table
déplie la ligne Fusion, et l'ordre porte l'argument. >>

> **Perspective recherche.** << Formalismes, résultats d'impossibilité, fronts ouverts. Reconduit du
> Vol. I dans le Livre I ; cesse au Livre III. >>

> **Mise en œuvre.** << Normes datées, outillage, déploiement. >>

⚠ << Avertissement : ce que la lecture rapide efface, ce qu'une passe ultérieure « corrigerait » à
tort, ou ce qui relève d'un degré 3 de R-14. >>

<< Lecture de l'auteur — construction d'auteur, suivie de ce que le socle établit et n'établit pas
(CA-IV-07). >>

## § << N >>.<< dernier >> — Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur, conformément à la
table détaillée du TOC.*

<< Nommer les legs, un par chapitre destinataire : ce que ce chapitre pose **une seule fois** et que
les chapitres aval citeront sans le reconstruire. C'est l'économie qui justifie la refonte des trois
volumes en un ouvrage — la rendre explicite ici évite qu'un chapitre aval l'annule sans le savoir. >>

---

## § << N+1 >> — Note de statut *(hors plan — à retirer à la publication)*

<< Ce bloc n'existe que si la pièce est écrite hors portes. Il n'est pas au TOC. >>

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée, conformément à la règle d'escalade du PRD (Annexe A) :
*un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il remonte.*

**Ce qui est enfreint.** << Quelles portes, quelle règle, sur quelle instruction, à quelle date. >>

1. **Aucun énoncé n'est central au sens de CA-IV-01.** << Pourquoi, et ce qu'il faudrait pour le
   devenir. >>
2. **Aucun décompte n'est publiable** (G-2). << … >>
3. **Les renvois « ch. N » sont des renvois de plan, non de texte.** << Lister les chapitres cibles
   non rédigés ; rappeler qu'ils se re-vérifieront contre le texte. >>
4. **Remontées ouvertes** : << `R-IV-NN` — objet, caractère bloquant, chapitre bloqué le cas
   échéant. >>

**Ce qui n'est pas enfreint.** << Structure suivie, table de couverture respectée y compris ses
sorties de périmètre et ses coupes assumées, garde-fous balayés, inférences marquées. Cette liste
dit au relecteur ce qu'il n'a pas besoin de revérifier. >>
````

---

## Ce que le gabarit ne dit pas, et qu'il faut décider

- **Le nombre de sections `##`** vient de la table détaillée du TOC, pas de ce gabarit. Certaines
  entrées ouvrent à `§ N.0`, d'autres à `§ N.1` — suivre la table.
- **Les tables** portent toutes une légende (`: Tableau N.M — …`) et se numérotent dans l'ordre
  d'apparition.
- **La section de synthèse** n'existe que si la table détaillée en prévoit une. Quand elle existe,
  elle se déclare construction d'éditeur.
- **Les encadrés** sont reconduits dans le Livre I et cessent au Livre III. Ne pas les imposer à une
  matière réglementaire qui ne s'y prête pas.
