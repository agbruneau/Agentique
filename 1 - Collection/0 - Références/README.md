# `0 - Références/` — ce que ce dossier porte, et ce qu'il ne porte plus

*Dossier de **pièces déposées**, non de sources instruites : **aucun document du dépôt ne cite
aucune de ces quatre pièces**. Le régime a longtemps manqué ; il est écrit ici, le 21 août 2026.*

## Ce qui reste au dépôt

| Fichier | Ce que c'est | Régime |
|---|---|---|
| `1997 - Mémoire Maitrise.pdf` | Le mémoire de maîtrise de l'auteur, 1997 | ☑ **Œuvre de l'auteur** — couverte par le [`LICENSE`](../../LICENSE) de la racine, CC BY 4.0 depuis le 21 août 2026 |

## Ce qui est sorti de l'arbre le 21 août 2026, et pourquoi

⚠ **Trois ouvrages de tiers y étaient versionnés depuis le 8 août 2026** — **36,6 Mo, 3 130 pages**
—, et **deux articles arXiv** dormaient sous
[`2 - OrchestrationAgentique/prd/`](../2%20-%20OrchestrationAgentique/prd/). *Le dépôt n'avait alors
aucune licence : le droit d'auteur par défaut s'appliquait, et l'anomalie restait latente.* **Poser
une licence CC BY 4.0 à la racine l'a rendue opposable** — cette licence couvre nominalement tout ce
que l'arbre porte, et l'auteur ne peut pas concéder ce qui n'est pas à lui.

☑ **Les cinq fichiers sont donc sortis de l'index git, non détruits.** Ils restent sur le disque de
l'auteur, ignorés par [`.gitignore`](../../.gitignore), et **restent dans l'historique git** — où
la licence de la racine ne s'étend pas et n'a jamais été applicable. Pour les relire :

```bash
git show 'd786adb:1 - Collection/0 - Références/2003 - Enterprise Integration Patterns.pdf' > eip.pdf
```

*Un clone du dépôt ne les recevra plus ; c'est exactement ce qui est voulu.*

| Ouvrage | Titulaire | Où le lire |
|---|---|---|
| **Enterprise Integration Patterns** — Gregor Hohpe, Bobby Woolf, 2003 | Addison-Wesley / Pearson | <https://www.enterpriseintegrationpatterns.com/> — le catalogue des 65 patrons est en libre accès chez l'auteur ; le livre, non |
| **Distributed Systems: Principles and Paradigms** — Andrew S. Tanenbaum, Maarten van Steen, 2ᵉ éd., 2007 | Pearson | <https://www.distributed-systems.net/> — van Steen et Tanenbaum y diffusent gratuitement la **3ᵉ édition** (2017), qui remplace celle-ci |
| **Systems Engineering Body of Knowledge (SEBoK)**, v2026 | INCOSE / IEEE / Stevens Institute — **CC BY-NC-SA 3.0**, incompatible avec la CC BY 4.0 de ce dépôt | <https://sebokwiki.org/> — le corps entier est en ligne, à jour, et le PDF versionné en était une capture |
| **Agentic Business Process Management: A Research Manifesto** — Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber *et al.*, 2026 — **fait F-36 du Vol. II** | Auteurs / *Information Systems* | arXiv:2603.18916 ; version journal *Information Systems* **140**, 102738 (2026), **à privilégier en citation** |
| **Design and Implementation of Agentic Orchestrations and Orchestration of Agents** — Rinderle-Ma, Mangler, Loebbecke, Voigt, Klievtsova, Ehrendorfer, 2026 — **fait F-37 du Vol. II** | Auteurs (TU München) | arXiv:2606.31518 — **préprint** : le Vol. II en cite le cadre, jamais les chiffres |

⚠ **Ce que la sortie ne change pas** : les faits **F-36** et **F-37** du socle du Vol. II sont
inchangés, leurs notices portent déjà leur source à l'identifiant arXiv, et **rien du corps d'aucun
volume ne dépendait du fichier**. *Ce qui sort est la copie, jamais la citation.*
