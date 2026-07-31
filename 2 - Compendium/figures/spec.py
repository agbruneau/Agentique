#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Déclaration commune aux cinq modules de contenu.

⚠ RIEN QUI NE SOIT DANS LE TEXTE. Chaque entrée porte le `source` d'où son
contenu est tiré, et les figures dérivées d'un tableau en reprennent les
libellés à la lettre. Une figure qui ajoute une information au chapitre n'est
pas une figure du volume : c'est un énoncé sans siège.

⚠ CHAQUE ENTRÉE PORTE SA RÉSERVE. C'est la signature du volume — la figure dit
aussi ce qu'elle refuse de laisser croire. `dessine.rendu()` refuse une entrée
sans réserve, et ce refus est délibéré.

⚠ LE RANG D'UNE FIGURE EST CELUI DE SA SECTION. Cinq sections en portent deux ;
elles se distinguent par un suffixe de lettre — « Figure 31.1a », « 31.1b ».
"""

FIGURES = []

# Ancre commune : la note de statut ferme le corps de toute pièce. Une figure
# qui appartient a la DERNIERE section d'un chapitre se pose devant elle.
NOTE = r"^## § \d+\.\d+ — Note de statut"


def f(ch, rang, nom, legende, alt, source, ancre, type, reserve, data):
    FIGURES.append(dict(ch=ch, rang=rang, nom=nom, legende=legende, alt=alt,
                        source=source, ancre=ancre, type=type,
                        reserve=reserve, data=data))
