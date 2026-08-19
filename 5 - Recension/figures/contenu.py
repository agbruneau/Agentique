#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contenu des deux figures de l'ouverture du rapport de l'art, et leur rendu.

    python "5 - Recension/figures/contenu.py"        # écrit les SVG dans figures/
    python "5 - Recension/figures/contenu.py" --md   # réémet les lignes Markdown

⚠ RIEN QUI NE SOIT AU § 1 ET AU § 2 DE L'OUVERTURE. Les deux figures sont
l'appareil de ces deux sections — les six paliers par la question que chacun
règle, puis la rupture entre le cinquième et le sixième. Chaque libellé se lit
mot pour mot dans le corps ; une figure qui étofferait le texte produirait un
énoncé sans siège.

⚠ CHAQUE ENTRÉE PORTE SA RÉSERVE — ce que la figure refuse de laisser croire. Ici
la réserve dit toujours la même chose en substance : l'échelle est l'appareil de
lecture de ce rapport, aucun livrable ne l'énonce, et deux de ses six paliers ne
se trouvent sous ces noms nulle part dans le dépôt. `dessine.rendu` refuse une
entrée sans réserve.
"""
import sys

import dessine as d

FIGURES = []


def f(rang, nom, legende, alt, source, type, reserve, data):
    FIGURES.append(dict(rang=rang, nom=nom, legende=legende, alt=alt,
                        source=source, type=type, reserve=reserve, data=data))


# ================================================== Ouverture — le cadre
f("0.1", "f-00-1-echelle",
  "L'appareil de lecture du rapport : six paliers, chacun par la question qu'il règle, et ce que "
  "l'échelle fait croître, présuppose et omet.",
  "Pile de six paliers, du technique a l'agentique, chacun portant la question qu'il regle, avec "
  "ce que l'echelle fait croitre, sa regle de lecture, son invariant et le palier qu'elle omet.",
  "Ouverture § 1 du présent rapport.",
  "pile",
  "Cette échelle est l'appareil de lecture de ce rapport et rien d'autre : aucun livrable ne "
  "l'énonce, aucun ne s'y situe lui-même, et le placement des sept livrables au tableau 0.1 est "
  "une lecture. Ses quatre premiers paliers sont les quatre couches du NEIF telles que le Vol. I "
  "les expose, mais numérotées en sens inverse ; les paliers 5 et 6 sont des ajouts qu'aucun "
  "livrable ne nomme sous ces titres.",
  dict(inverse=True,
       couches=[
           ("1", "Technique",
            "« Le message arrive-t-il intact ? » — transport sécurisé, sans interpréter le "
            "contenu. MQ, Kafka, gRPC, mTLS."),
           ("2", "Sémantique",
            "« Le même mot a-t-il le même sens des deux côtés ? » — modèles canoniques, "
            "registres de schémas. BIAN, ISO 20022."),
           ("3", "Organisationnel",
            "« Qui fait quoi, dans quel ordre, jusqu'où ? » — processus et chorégraphie "
            "événementielle. Patron Saga."),
           ("4", "Juridique",
            "« Qui répond de l'acte, devant quel texte ? » — preuve, non-répudiation, résidence "
            "des données. Loi 25, BSIF E-23."),
           ("5", "Politique",
            "« Qui décide de la règle et l'arbitre ? » — contrats de données, SLA, imputabilité. "
            "PEP/PDP."),
           ("6", "Agentique",
            "« Que reste-t-il du contrat si l'exécutant décide ? » — intention négociée. A2A, "
            "MCP, Agent Cards."),
       ],
       notes=[
           ("CE QUE L'ÉCHELLE FAIT CROÎTRE",
            "L'abstraction de ce qui est échangé, l'imputabilité de ce qui est décidé, "
            "l'autonomie d'exécution de ce qui agit."),
           ("COMMENT ELLE SE LIT",
            "Chaque palier présuppose ceux du dessous et n'en garantit aucun : un palier tenu "
            "n'entraîne jamais le suivant."),
           ("INVARIANT TRANSVERSAL",
            "Découplage ── contrat ── évolution, repris mot pour mot du Vol. I. Trois termes ; la "
            "somme en compte quatre, le quatrième étant l'exploitation."),
           ("LE PALIER QUI MANQUE",
            "Le syntaxique. La pile canonique du Vol. I en compte quatre, et c'est là que le "
            "compendium situe MCP et A2A — qui présupposent l'accord sémantique sans le "
            "produire."),
       ]))

f("0.2", "f-00-2-rupture",
  "La rupture entre le cinquième palier et le sixième : ce qui se vérifie avant l'exécution, et ce "
  "qui ne s'observe que pendant.",
  "Deux panneaux comparant l'integration deterministe des paliers 1 a 5 et la gouvernance "
  "probabiliste du palier 6.",
  "Ouverture § 2 du présent rapport.",
  "paire",
  "Le déplacement est de nature et non de degré, mais l'échelle porte sa propre exception : la "
  "clause de renversement interdit l'autonomie agentique directe partout où une compensation "
  "financière temps réel s'impose, et le sixième palier n'est donc pas la destination de "
  "l'échelle. La clause appartient au cadre de ce rapport et n'est portée par aucun livrable du "
  "dépôt. Et le régime que le traité décrit — coordonner par le milieu, non par accord — n'a de "
  "case dans ni l'un ni l'autre panneau.",
  dict(titre_g="NIVEAUX 1 À 5 — INTÉGRATION DÉTERMINISTE",
       titre_d="NIVEAU 6 — GOUVERNANCE PROBABILISTE ET ADAPTATIVE",
       accent_d=True,
       gauche=("Des contrats statiques et vérifiables", [
           "La contractualisation est écrite avant l'exécution : schéma au registre, contrat de "
           "données, SLA arbitré en comitologie.",
           "Le contrat se vérifie AVANT l'exécution — c'est exactement ce qu'une vérification "
           "statique atteint.",
           "L'imputabilité est attribuée par le plan de contrôle institutionnel, aux points "
           "d'application de politiques.",
       ], "Ce qu'il tient : un engagement opposable, vérifiable avant que rien ne s'exécute."),
       droite=("Une contractualisation négociée", [
           "La contractualisation devient dynamique, par négociation contextuelle d'objectifs "
           "entre agents (A2A, MCP).",
           "L'intention ne s'observe que PENDANT l'exécution — d'où l'impératif de "
           "vérification à l'exécution.",
           "Le prix en est déclaré : surcoût d'observabilité (AgentOps) pour confiner le "
           "non-déterminisme.",
       ], "Ce qu'il tient : une intention exécutée, dont la conformité ne se constate qu'après.")))


def main():
    lignes = []
    for fig in FIGURES:
        c, h = getattr(d, fig["type"])(**fig["data"])
        d.rendu(fig["nom"], c, h, fig["alt"], fig["source"], fig["reserve"])
        lignes.append(f'![**Figure {fig["rang"]}** — {fig["legende"]}]'
                      f'(figures/{fig["nom"]}.svg)')
    if "--md" in sys.argv:
        print("\n\n".join(lignes))
    else:
        print(f"{len(FIGURES)} figures écrites dans {d.RACINE}")


if __name__ == "__main__":
    main()
