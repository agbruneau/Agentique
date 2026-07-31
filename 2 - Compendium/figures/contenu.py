#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble les cinq modules de contenu ; la liste vit dans `spec.py`.

Un module par Livre : le contenu de cent quinze figures ne tient pas dans un
seul fichier lisible, et le decoupage suit celui du volume.
"""
import spec
import contenu1  # noqa: F401
import contenu2  # noqa: F401
import contenu3  # noqa: F401
import contenu4  # noqa: F401
import contenu5  # noqa: F401
import contenu6  # noqa: F401  — le reliquat, sept figures instruites à part

FIGURES = spec.FIGURES
