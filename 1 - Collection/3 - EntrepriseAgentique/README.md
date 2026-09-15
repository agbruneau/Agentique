# Volume III — L'entreprise agentique : la fabrique de confiance

**Lire :** [`Monographie.pdf`](Monographie.pdf) (428 p.) — 34 pièces : avant-propos, 28 chapitres en neuf parties, annexes A à E.

Ce qu'une entreprise doit tenir pour que des agents y opèrent sous mandat vérifiable : identité non humaine, délégation vérifiable,
maillage d'agents et AgentOps, sous l'horloge post-quantique. Thèse : la confiance ne se décrète pas, elle se fabrique — émettre une
identité opposable, l'appliquer au maillage, l'exploiter dans la durée. Le passeport d'agent qui l'émet est une construction de
l'ouvrage, qu'aucune spécification ne porte. Le volume prolonge les [Vol. I](../1%20-%20InteroperabiliteAgentique/) et
[II](../2%20-%20OrchestrationAgentique/) sur leur verrou commun ; ses pièces sont gelées au 21 juillet 2026.

**Statut :** livrable sous réserve déclarée — fixé le 15 septembre 2026 par la décision [D-18](<../../2%20-%20Compendium/PRD/PRD.md#d-18>)
(option DA-3 (a) du plan d'exécution) ; dépôt rouvert le même jour par [D-17](<../../2%20-%20Compendium/PRD/PRD.md#d-17>). Aucun relecteur humain nommé.

> **Réserves de lecture :** les quinze remontées ouvertes, R-G-43 à R-G-57, ni soldées ni levées ; un passage qu'elles touchent se lit en les sachant.
> - dette de vote sur F-92 et F-96 (R-G-44) : la thèse du ch. 26 repose sur deux entrées que le vote adversarial dû n'a pas éprouvées, marquées ⚖ à chaque mobilisation ;
> - texte touché : ch. 27 §27.2, ArchiMate sans socle (R-G-43) · ch. 24 §24.4 sans socle (R-G-45) · ch. 5 §5.4 et ch. 12 §12.4, intitulés de renvoi (R-G-48) · ch. 2, 19, 20 et 22, révision MCP du 28 juillet 2026 et ligne directrice de l'AMF (R-G-57) · sept sièges hérités et quatre verbatim devenus invérifiables (R-G-52, R-G-55) ;
> - critères non prononcés : CA-09 (R-G-46) · CA-10, branche (c) (R-G-54) · CA-12 et ses huit retraits, dont deux révocables (R-G-53, R-G-56) ;
> - plan et appareil : volumétrie (R-G-47) · attestations auto-délivrées et cellules tronquées des rapports de lot (R-G-49, R-G-50) · renvois `doc/` → `prd/` (R-G-51).
>
> Chacune, avec ce qu'elle bloque : [`verification/remontees-gouvernance.md`](verification/remontees-gouvernance.md), qui fait foi.

**Par où entrer :** la partie II, le passeport d'agent et la chaîne de mandat. La gouvernance est sous [`prd/`](prd/) — PRD, qui prime,
TOC, PRDPlan — et les 30 rapports de vérification sous [`verification/`](verification/) : quinze lots d'instruction, onze relectures, deux
revalidations, la confrontation des thèses et le registre des remontées. Deux instruments ne se confondent jamais : les niveaux de
preuve, qui disent ce qu'une affirmation a subi, et le tri programmé / projeté / spéculatif, qui dit ce qu'un énoncé prétend du futur.

**Refaire :** depuis ce dossier, `python build/assemble.py` réunit les 34 pièces en `Monographie.md`, puis
`bash build/build-pdf.sh Monographie.md` recompose le PDF. La chaîne est la troisième copie indépendante du gabarit des Vol. I et II :
un correctif apporté à l'une ne se propage pas aux autres.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — l'état qui a motivé la réserve, la suppression de `verification/` le 8 août 2026 et sa
restauration le 21, les fichiers cités qui ne sont plus au dépôt, les divergences factuelles portées, la chronique des bandeaux de tête.
