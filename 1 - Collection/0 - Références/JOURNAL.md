# Journal — `1 - Collection/0 - Références/`

Ce fichier reçoit, sans un mot changé, la page d'accueil de ce dossier telle qu'elle était écrite au commit `5cdb5bb` du
15 septembre 2026 : la chronique datée — clôtures, réouvertures, redatations, corrections de corrections — et tout ce qui
l'entourait, tables et cartes comprises. Un chiffre y vaut à la date qui l'accompagne ; un présent, au jour où il a été écrit ;
un « ci-dessous » ou un « en tête », à la page d'où il vient.

Seules les cibles de lien ont bougé, et seulement celles qui seraient mortes : elles visent ce qui existe depuis ce dossier.
Le texte d'origine se relit par `git show 5cdb5bb:"1 - Collection/0 - Références/README.md"`. Trois dossiers ont changé de nom le 5 septembre 2026 — `3 - Traité/` est
`4 - Essais/1 - Traité/`, `4 - Veille/` est `3 - Veille/`, `6 - Article/` est `4 - Essais/2 - Article/` — et un chemin écrit
avant cette date garde son ancien nom. L'état courant est à [`README.md`](README.md) ; une passe nouvelle s'ajoute à la fin de ce fichier,
datée, et rien de ce qui précède ne s'y corrige.

| Page reçue | Lignes | Sections |
|---|---|---|
| [`README.md`](#page-readme) | 50 | [Ce qui reste au dépôt](#ce-qui-reste-au-dépôt) · [Ce qui est sorti de l'arbre le 21 août 2026, et pourquoi](#ce-qui-est-sorti-de-larbre-le-21-août-2026-et-pourquoi) |

<a id="page-readme"></a>

---

*Page reçue : `README.md`, 50 lignes au commit `5cdb5bb`.*

# `0 - Références/` — ce que ce dossier porte, et ce qu'il ne porte plus

*Dossier de **pièces déposées**, non de sources instruites : **aucun document du dépôt ne cite
aucune de ces quatre pièces**. Le régime a longtemps manqué ; il est écrit ici, le 21 août 2026.*
⚠ *Le dossier en portait quatre à cette date ; **il n'en porte plus qu'une depuis le 25 août 2026** —
le mémoire de l'auteur.*

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

☑ **Les cinq fichiers sont donc sortis de l'index git, non détruits.** Ils sont restés sur le disque
de l'auteur, ignorés par [`.gitignore`](../../.gitignore), et **restent dans l'historique git** — où
la licence de la racine ne s'étend pas et n'a jamais été applicable.

⚠⚠ **ET LES COPIES AU DISQUE ONT ÉTÉ EFFACÉES LE 25 AOÛT 2026, SUR INSTRUCTION D'AUTEUR** — les
trois ouvrages d'ici et les deux articles arXiv de `2 - OrchestrationAgentique/prd/`, **38 281 125
octets**. ☑ *L'historique git est désormais **la seule copie**, et la commande ci-dessous la seule
façon de les relire.* ⚠ **Ce que l'effacement ne change pas** : ni le régime de licence, ni les
faits **F-36** et **F-37**, ni un seul renvoi du corps — *ce qui disparaît est une copie de
travail, jamais une citation.* Pour les relire :

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
