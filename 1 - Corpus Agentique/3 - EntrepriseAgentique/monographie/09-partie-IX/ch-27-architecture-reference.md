# Chapitre 27 — Architecture de référence : la fabrique de confiance et son organisation

| Champ | Valeur |
|---|---|
| Statut | **Gabarit** — aucune rédaction. Valeurs admises : Gabarit / Rédigé (premier jet) / Rédigé et relu adversarialement |
| Date de gel de l'information | — (à renseigner à la rédaction, et reportée au registre `99-registre-gel.md` au **même commit**) |
| Socle mobilisé (PRD §7) | H-29, H-30 (§27.5), H-31 (§27.4) ; spécification : PRD Annexe B |
| Garde-fous à surveiller (PRD §8) | **CA-13** — chaque composant, contrat et correspondance réglementaire tracé au socle **ou** marqué inférence d'auteur ; **CA-07 — §27.4 : construction d'auteur en totalité** ; R-13 ; R-07 |
| Volumétrie cible | ~5500 mots |

> **Thèse ([TOC.md](../../doc/TOC.md))** : les Parties I-VIII se composent en une architecture de référence à trois étages — la fabrique d'identité (émission, registre, vérification, révocation), le maillage qui l'applique (PEP/PDP, passerelles), l'AgentOps qui l'exploite (observabilité, évaluation, incident) — formalisée en ArchiMate (méthode-signature du Vol. I) ; mais l'architecture ne suffit pas : l'entreprise agentique est autant une structure de rôles et une trajectoire de maturité qu'une pile technique, et le chapitre traite les deux à parité.

---

<!-- GOUVERNANCE — bloc à supprimer à la rédaction ; hors décompte de volumétrie (PRDPlan §1.5)
Lot d'instruction : aucun — chapitre de composition (Parties I à VIII) ; §27.4 et §27.5 réaffectées (L-15 clos par échec documenté)
Règle cardinale (PRD §7.0) : ne rien rédiger avant la clôture du lot ci-dessus.
Boucle qualité obligatoire : PRDPlan §5.2 — sept étapes, dont la relecture adversariale
  par un relecteur distinct du rédacteur (CA-14), et l'amendement du socle en premier
  lorsque la faute y siège.
Formulations imposées : PRDPlan §5.5. Motifs de balayage : PRD §A.6.
Escalade : un rédacteur ne corrige jamais le PRD, le TOC ni ce plan — il remonte (PRDPlan §5.3).
-->
