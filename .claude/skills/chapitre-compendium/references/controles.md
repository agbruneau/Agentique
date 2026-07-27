# Contrôles — avant de committer une pièce

Trois familles, dans cet ordre. Un contrôle en échec **interdit de pousser** : la consigne de flux du
dépôt (committer tout, pousser sur `main`) supprime l'étape de revue, pas la relecture.

## 1. Contrôles mécaniques de la pièce

```bash
python .claude/skills/chapitre-compendium/scripts/verifier-piece.py \
  "2 - Compendium/Livre I/01-interoperabilite-integration-entreprise"
```

L'argument est le chemin **sans extension** : les deux rendus se contrôlent ensemble, parce que c'est
ensemble qu'ils se versionnent. Huit contrôles, chacun fermant un défaut qu'aucun rendu ne signale :

| | Contrôle | Ce qu'il attrape |
|---|---|---|
| `[1]` | appariement | un rendu manquant, ou un `.html` qui ne renvoie plus vers son `.md` |
| `[2]` | structure HTML | balises déséquilibrées, ancre de navigation sans cible |
| `[3]` | autonomie | police, script, image ou `@import` distants ; balise `canonical` ou `og:` |
| `[4]` | justification | `lang="fr-CA"` retiré, `hyphens: auto` ou `text-align: justify` absents |
| `[5]` | légendes | une table sans légende — elle consomme quand même un numéro |
| `[6]` | en-tête | l'un des cinq champs du PRD §6 omis, ou la thèse absente |
| `[7]` | renvois | un lien relatif sans cible |
| `[8]` | résidus | du Markdown resté littéral dans le rendu — la faute propre au générateur |

⚠ **Ce que le script ne fait pas, et qui reste à la relecture** : la fidélité au TOC, le régime de
preuve, le marquage des inférences, la justesse des renvois « ch. N ». Un script ne lit pas un plan.

⚠ **Ne jamais tuyauter le vérificateur dans un enchaînement `&&`.** `verifier-piece.py … | tail -2 &&
git commit` renvoie le code de sortie de `tail`, **pas celui du contrôle** : un écart signalé à
l'écran laisse passer le commit. La faute a déjà été commise sur le ch. 6, dont le rendu portait un
gras non converti et qui a été poussé quand même. Exécuter le contrôle **seul**, lire sa sortie, puis
committer — ou tester `$?` explicitement.

### Si le script est modifié

Il est du contenu, comme le reste du dépôt : il se valide **par mutation**.

```bash
python .claude/skills/chapitre-compendium/scripts/verifier-piece-mutations.py \
  "2 - Compendium/Livre I/01-interoperabilite-integration-entreprise"
```

Treize mutations, une par classe de faute. Le harnais constate **d'abord** que le contrôle passe sur
la pièce intacte, **puis** que chaque faute est détectée par le bon contrôle. Le premier constat
compte davantage que le second : un script cassé « détecte » toutes les mutations sans rien
contrôler du tout.

*Ce harnais a déjà servi : il a montré que `"hyphens: auto" in html` était satisfait par le seul
`-webkit-hyphens: auto`, de sorte qu'une feuille n'ayant gardé que la forme préfixée passait le
contrôle sans couper les mots dans aucun navigateur moderne. Le motif est désormais ancré.*

## 2. Contrôles du dépôt

À exécuter **même quand on croit n'avoir pas touché à leur domaine** — le piège documenté du ch. 32
est qu'une addition peut périmer un identifiant qu'on n'a pas touché, en rendant mixte un chapitre
qui ne l'était pas.

```bash
python "2 - Compendium/PRD/check-toc.py"   # C1-C15, sortie 0 exigée
python check-veille.py                      # sortie 0 exigée
```

## 3. Regarder la page

Un rendu qui passe les contrôles peut être illisible : valeur CSS invalide, encadré qui déborde,
légende collée au paragraphe suivant. Chromium est présent dans l'environnement.

```bash
BIN=/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # ou : find /opt/pw-browsers -name chrome -type f
"$BIN" --headless --disable-gpu --no-sandbox --hide-scrollbars \
       --window-size=1440,1500 --screenshot=/tmp/apercu.png \
       "file:///chemin/absolu/vers/NN-slug.html"
```

Puis lire l'image. **Trois cadrages suffisent** et couvrent l'essentiel :

1. **La tête** — titre, en-tête à cinq champs, thèse. C'est là que se voient les débordements de
   tableau et les champs trop longs.
2. **Une section de prose avec une table** — vérifie la justification, l'espacement de la légende,
   le défilement horizontal de la table.
3. **Une section portant un `.avert` et un `.encadre`** — vérifie que le marqueur ⚠ ne se dédouble
   pas (le CSS l'ajoute ; l'écrire aussi dans le texte le fait apparaître deux fois).

⚠ **Le défilement par fragment (`…html#s12`) rend mal en mode *headless*** : la capture montre une
bande vide au-dessus du contenu. Pour cadrer une section précise, extraire l'intervalle voulu dans
une copie temporaire plutôt que de compter sur l'ancre.

```python
# Extraire une section dans une copie de travail, pour la capturer seule
import sys
s = open(source, encoding="utf-8").read()
s = s.replace("background-attachment: fixed;", "").replace("scroll-behavior: smooth;", "")
tete = s[: s.index('<header class="titre">')]
extrait = s[s.index('<h3>1.1.1 Définir') : s.index('<h3>1.1.2 Taxonomie')]
open(destination, "w", encoding="utf-8").write(tete + extrait + "</main></div></body></html>")
```

## 4. Le commit

Les deux rendus dans le **même commit**, avec les fichiers de documentation mis à jour s'il y en a.
Message court en français, nommé par livrable :

```
Livre I — chapitre 3 rédigé en .md et .html (brouillon hors portes)
```

Le corps dit ce que la pièce couvre, ce qu'elle enfreint, ce qu'elle ne touche pas, et les contrôles
exécutés **avec leur résultat** — une attestation s'écrit depuis une constatation sur pièce, jamais
depuis un souvenir (CA-IV-14).
