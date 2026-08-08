# Volume III — « L'entreprise agentique : la fabrique de confiance »

📖 **Lire :** [`Monographie.pdf`](Monographie.pdf) (**427 p.**) dans ce dossier.
⚠ **Rédigé de bout en bout, non publiable en l'état** — voir « État » plus bas.

> ⚠ **Dépôt clos et final le 8 août 2026** — décision d'auteur **D-13**
> ([`2 - Compendium/PRD/PRD.md`](../../2%20-%20Compendium/PRD/PRD.md) v0.17 §16). Aucune passe
> n'est plus prévue, sur ce volume ni sur aucun autre du dépôt : ce qui suit décrit un état
> **définitif**. ⚠ *Clore n'est ni terminer ni publier* — rien n'est levé, rien n'est soldé, et
> ce qui restait dû devient un **manque définitif, daté et écrit**.

> **Où vous êtes.** Ce dossier est le **troisième des trois volumes** du corpus, dans le dépôt
> [*Agentique*](../../README.md). Il **prolonge les deux précédents sur leur verrou commun** :
> l'identité non humaine et son exploitation dans la durée. Le Vol. I l'a identifié comme son verrou
> résiduel, le Vol. II l'a laissé en questions ouvertes ; ce volume en fait son objet. Pour l'ordre de
> lecture, les renvois entre volumes et la veille technologique qui les recoupe, commencer par le
> [README du dépôt](../../README.md).

Monographie sur ce qu'une entreprise doit tenir pour que des agents y opèrent **sous mandat
vérifiable** — identité non humaine, délégation vérifiable, maillage d'agents et AgentOps, sous
l'horloge post-quantique. Rédigée en **français canadien**. Le volume hérite de **deux gels
distincts** : juin 2026 (Vol. I) et 16-17 juillet 2026 (Vol. II) ; ses 34 pièces portent le leur au
**21 juillet 2026**.

**Auteur :** André-Guy Bruneau, M. Sc. IT — Juillet 2026

| Champ | Valeur |
|---|---|
| Livrable | **34 pièces rédigées et relues adversarialement** — avant-propos, 28 chapitres en 9 parties, annexes A à E |
| Rendu | [`Monographie.pdf`](Monographie.pdf) **427 p.**, gabarit FESP (troisième copie indépendante du pipeline, créée le 23 juillet 2026) |
| Volumétrie | **160 890 mots réels** pour une cible cumulée de **102 500** — soit **+57,0 %** ; l'écart vient des **bornes rétablies**, non d'un ajout de matière (re-mesure du 24 juillet 2026) |
| Socle factuel propre | **98 entrées** F-01 à F-98 ⚠ dont **F-92 et F-96 portent une dette de vote adversarial** |
| Socle hérité | **33 entrées** — H-01 à H-16 (Vol. II, **niveau conservé**), H-17 à H-33 (Vol. I, **abaissées en [C]**) |
| Lots d'instruction | **15 clos sur 15** — quatorze par instruction aboutie, **L-15 par échec documenté** (filiation livresque retirée, réversible) |
| Garde-fous | **R-01 à R-14** *(deux chiffres — ceux du Vol. II sont R-1 à R-8, un chiffre : ce ne sont pas les mêmes objets)* |
| Conformité | **CA-01 à CA-14** ⚠ **CA-12 (dualité d'usage) n'est tenue sur aucune pièce de la phase P4** ; **16 pièces sur 34 n'en nommaient aucun compte rendu au relevé du 22 juillet 2026**, et **deux l'ont reçu depuis** par les correctifs de la relecture du 24 juillet ([`relecture-revision-2026-07-24.md`](verification/relecture-revision-2026-07-24.md) §1) — le terme procédural reste non clos |
| Dates de gel | **21 juillet 2026** pour les 34 pièces — registre [`monographie/99-registre-gel.md`](monographie/99-registre-gel.md) |
| Revalidation | **22 juillet 2026** ([`verification/revalidation-2026-07-22.md`](verification/revalidation-2026-07-22.md)) : six lignes INCHANGÉ, une INACCESSIBLE (AMF, HTTP 403). Couvre une publication **jusqu'au 21 août 2026** (CA-04) ; au-delà, elle se rejoue |
| Lacunes | **22 documentées** dont **3 closes** — le PRD §10 ne porte « INSTRUITE ET CLOSE » qu'aux entrées 1, 2 et 11 ; la 10 est « instruite, non arbitrée » et la 15 « instruite, **non close** ». Exposées plutôt que comblées |
| Gouvernance | **PRD v1.3** · **TOC v0.8** · **PRDPlan v0.5**, sous [`prd/`](prd/) |

## La thèse

**La confiance ne se décrète pas : elle se fabrique.** L'entreprise qui délègue à des agents
logiciels des tâches engageant sa responsabilité doit se construire sur une **fondation
identitaire** — l'identité non humaine est le nouveau plan de contrôle (*identity as the new control
plane*). La fabrique tient par **trois capacités**, en boucle continue :

1. **Émettre** une identité opposable — le **passeport d'agent** : carte signée, inscription au
   registre gouverné, chaîne de mandat, attestations de conformité ;
2. **Appliquer** cette identité là où elle est vérifiée — le **maillage d'agents** (*agent mesh*)
   comme point d'application des politiques ;
3. **Exploiter** le comportement dans la durée — **AgentOps** : observabilité, évaluation continue,
   cycle de vie, réponse aux incidents.

Le tout sous une contrainte datée : l'**horloge post-quantique**, fenêtre d'action 2026-2029.

⚠ **Le passeport d'agent n'existe dans aucune spécification** : c'est une **construction de
l'ouvrage** (garde-fou R-01), et le volume l'écrit à chaque mobilisation.

## Structure en neuf parties

| Partie | Capacité | Objet |
|---|---|---|
| **I — L'héritage** | — | L'identité machine depuis OAuth 2012, identité de charge de travail (SPIFFE/SPIRE), écart de gouvernance NHI |
| **II — Émettre** | Identité | Le passeport d'agent : carte signée (A2A v1.0), registre, chaîne de mandat, attestations |
| **III — Délégation** | Mandat | Le **problème des deux sauts** : au-delà de deux sauts, aucun mécanisme actuel ne trace la délégation de bout en bout |
| **IV — Menaces** | Défense | Menaces architecturales sur la chaîne d'identité ; absence de réduction de portée entre mandant et mandataire |
| **V — Horloge PQ** | Cryptographie | ML-KEM / ML-DSA (FIPS 203/204) ; crypto-agilité comme exigence de conception |
| **VI — Droit** | Conformité | E-23, AMF, Loi 25 : obligation implicite de registre d'agents et de traçabilité ; droit de révision humaine |
| **VII — Appliquer** | Maillage | Le maillage d'agents comme point d'application des politiques de sécurité |
| **VIII — Exploiter** | AgentOps | Observabilité, évaluation continue, cycle de vie, réponse aux incidents |
| **IX — Blueprint** | Organisation | Modèle de maturité : assistance → copilote → orchestration sous revue → autonomie bornée |

**Six chapitres n'ont aucun lot d'instruction** (ch. 4, 8, 10, 25, 27, 28) : ce sont des **chapitres
de composition**, qui consomment d'autres chapitres plutôt qu'une passe de recherche. Ils sont **plus**
exposés qu'un chapitre de socle, pas moins — sans source à citer, chaque affirmation y est soit tracée
vers un chapitre amont, soit une inférence à marquer.

## État

⚠ **Rédigé ne vaut pas publiable, et c'est le seul énoncé d'état qui compte.** Les 34 pièces sont
rédigées, relues adversarialement et corrigées — **jalon J-5 atteint le 22 juillet 2026** —, et la
phase de finalisation **P5 est CLOSE SANS ÊTRE ACHEVÉE** depuis la clôture du dépôt, le 8 août 2026.
*Trente-quatre pièces rédigées, relues et corrigées font un ouvrage complet, ce qui est autre chose
qu'un ouvrage publiable* — et **la clôture ne l'en rapproche pas** : elle déclare seulement que
personne ne finira P5. ⚠ **Les quinze remontées R-G-43 à R-G-57 et la dette de vote sur F-92 et
F-96 restent donc ouvertes à titre définitif** ; *une dette qu'on cesse de suivre reste une dette.*

**Ce qui a été fait.** Phases P0 à P4 closes ; revalidation temporelle finale (P5.1) et rejeu
exhaustif des motifs de balayage (P5.2) conduits le 22 juillet 2026 ; réalignement des porteurs de
décomptes (P5.3) ; pipeline de rendu créé le 23 juillet 2026 (P5.4) et PDF réassemblé le 24 ; relecture
de révision complémentaire le 24 juillet 2026. **30 rapports** sous [`verification/`](verification/)
— 15 rapports de lot, 11 relectures, 2 revalidations, la confrontation des thèses et le registre des
remontées. ⚠ **Aucun des trois contrôles de P5 ne vaut certificat.**

**Ce qui reste ouvert, et le restera** — le détail vit au registre
[`verification/remontees-gouvernance.md`](verification/remontees-gouvernance.md) :

- **Quinze remontées de gouvernance ouvertes** — R-G-43 à R-G-57 — dont plusieurs siègent au PRD ou au
  TOC plutôt que dans une pièce : leur arbitrage rouvrirait du texte tenu pour fait, **sur les
  trente-quatre pièces** ;
- **douze arbitrages tranchés par délégation demeurent révocables** ;
- ⚠ **la dette de vote sur F-92 et F-96 n'est pas résorbée** (R-G-44) : les deux entrées **fondent le
  ch. 26**, et la parade tenue est un marqueur ⚖ à chaque mobilisation — *une parade n'est pas une
  résorption* ;
- **le §24.4 demeure sans socle** (R-G-45), avec son encadré de lacune ;
- **le grain de CA-09 n'est pas tranché** (R-G-46), et **8 pièces sur 13** de la phase P4 n'ont pas subi
  ce contrôle ;
- ⚠ **la distinction rédacteur / relecteur n'est pas constatable sur disque** (réserve 1 de R-G-19, non
  levée).

⚠ **Le statut non publiable ne dépend d'aucune page qui le déclare.** La **note d'état** que le PDF
portait en page 2 a été **retirée le 24 juillet 2026** sur demande de l'auteur : la page de titre est
directement suivie du résumé. Le statut tient aux remontées ouvertes et à la dette de vote, qui ne sont
pas des attributs du rendu.

## Fichiers cités qui ne sont plus au dépôt — consignés, non corrigés

Deux corpus que ce volume cite ont été retirés du dépôt, hors de sa charge éditoriale :

| Corpus retiré | Date | Commit | Ce que ce volume y perd |
|---|---|---|---|
| `Synthese Monographie.md` (Vol. I et II) | 22 juillet 2026 | `fd8f1be` | **100 occurrences sur 26 fichiers** (mesure ancrée au commit) ; sièges verbatim de H-27 à H-32 et de la formule de non-compositionnalité |
| `Borealis-Go/` (démonstrateur, Vol. I) | 25 juillet 2026 | `60f57f6` | **6 occurrences sur 5 fichiers** — ch. 28, assemblage, PRD, TOC, confrontation des thèses |

⚠ **Les citations ne sont pas fautives : elles ne sont plus vérifiables.** *Un renvoi exact vers un
fichier absent reste exact ; il cesse seulement d'être opposable.* **Ne pas restaurer ces fichiers, ne
pas réécrire les citations** — on ne corrige pas le livrable d'autrui. Le fait est remonté à l'auteur
(R-G-52) et n'est pas arbitré ici.

## Divergences factuelles portées par ce volume — signalées, jamais tranchées

Deux faits datés divergent d'un livrable du dépôt à l'autre. Le PRD §7.5 en est la source de vérité
pour la durée de rédaction ; le volume les **porte**, il ne les arbitre pas :

- **Gouvernance d'AP2** — Vol. I et veille : transfert à la FIDO Alliance le 28 avril 2026, donné pour
  établi. Vol. II (gel postérieur) : aucun transfert documenté, rangé parmi les **ignorances
  déclarées**. → ch. 9, lot L-06. ⚠ **L'arbitrage par chronologie est interdit** : le volume le plus
  récent est ici le plus réservé.
- **Date de la ligne directrice IA de l'AMF** — Vol. II : 30 mars 2026 (avec dette de vérification
  déclarée). Veille : 7 avril 2026. → ch. 19. L'entrée en vigueur au **1er mai 2027** est, elle,
  concordante.

⚠ Le fichier `commun/faits-partages.md`, qu'un cadrage antérieur annonçait comme source unique de
vérité pour ces faits, **n'existe pas et ne sera pas créé** (décision, PRD §7.5) : chaque volume porte
ses propres faits datés.

## Structure du dossier

```
README.md                    ← ce fichier (présentation du volume)
prd/                         gouvernance, par ordre d'autorité
  PRD.md                       v1.3 — contenu, héritage du socle, garde-fous, critères (prime)
  TOC.md                       v0.8 — autorité sur le découpage (28 chapitres, 9 parties, 34 pièces)
  PRDPlan.md                   v0.5 — plan d'exécution (phases P0 à P5)
monographie/                 34 pièces rédigées + 99-registre-gel.md
verification/                30 rapports (lots, relectures, revalidations, remontées)
build/                       pipeline FESP (troisième copie) + assemble.py
Monographie.md / .pdf        assemblage des 34 pièces et son rendu (427 p.)
```

## Régénérer le PDF

Après toute modification des pièces, **depuis ce dossier** :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf (427 p.)
```

⚠ **Le pipeline est la troisième copie indépendante du FESP** (Vol. I → Vol. II → ici) : **un correctif
apporté à l'un ne se propage pas aux autres.** **Règle permanente :** régénérer et versionner le `.pdf`
avec le `.md` — jamais la source seule.

☑ **`assemble.py` rebase les liens relatifs des pièces depuis le 8 août 2026.** Une pièce de
`monographie/08-partie-VIII/` renvoie à `../../verification/lot-L-14-observabilite.md` ; concaténée dans
`Monographie.md`, à la racine du volume, cette cible ne résolvait plus. Le script réécrit chaque cible
relative depuis le répertoire de la pièce — **19 renvois morts de moins dans `Monographie.md`**, aucune
ligne de prose touchée. ⚠ **Le `.pdf` versionné précède ce correctif** : il porte encore les anciennes
cibles, et se régénérera à la prochaine passe de rendu.

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf`, polices Liberation Sans et DejaVu
Sans. Le script exporte lui-même `PYTHONUTF8=1` (nécessaire sous Windows).

## Avertissements

- **Aucun avis juridique ni conseil d'investissement.** L'ouvrage rapporte des textes et en propose des
  lectures d'architecture qui engagent son auteur seul.
- **Aucune recommandation de fournisseur.** Entra Agent ID, passerelles MCP, offres de maillage : ce
  sont des **cas d'instanciation documentés**. ⚠ *Annonce, disponibilité générale, feuille de route et
  préversion sont quatre choses différentes.*
- **Deux instruments épistémiques, jamais l'un pour l'autre** (CA-11) : les niveaux **[A]/[B]/[C]** —
  ce que l'affirmation a subi — et le tri **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** — ce que l'énoncé
  prétend sur le futur. Un fait peut être [B] **et** PROJETÉ.
- **Trois degrés d'absence, jamais confondus** (§8.6) : fait négatif **VÉRIFIÉ** > fait négatif
  **ÉTABLI** > **absence de documentation**. Jamais « le socle ne documente pas X, donc X n'existe
  pas » (R-14).
- **Dualité d'usage** (R-12) : la Partie IV décrit la mécanique des attaques au niveau architectural,
  cite les identifiants, **n'en reproduit aucun**.
- **Vingt-deux lacunes** exposées plutôt que comblées. Aucune n'est comblée par une source de moindre
  qualité.
- **Assistance par agents.** Ce travail a été produit avec l'assistance de pipelines de recherche
  multi-agents, selon les méthodes de vérification décrites dans l'ouvrage ; la responsabilité
  éditoriale est celle de l'auteur.
