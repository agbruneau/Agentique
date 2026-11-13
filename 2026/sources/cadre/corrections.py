"""Correctifs de la revue contradictoire du 3 novembre 2026, appliqués au corps recomposé.

Le corps du Cadre n'a pas de source éditable : il est relu dans l'édition d'origine
(construire_pdf.py, ORIGINE). Les correctifs de la revue du 3 novembre 2026 sont faits à
leur place, dans le HTML que corps() produit, et consignés à l'annexe H
(actualisation-2026-11.html, section H.6).

Les correctifs sont rangés par tranche du document dans correctifs/NN_*.py. Chaque module
définit CORRECTIONS, une liste de (passage d'origine, passage corrigé, constats), et
JOURNAL, une liste de (localisation, nature du correctif, constats) pour l'annexe.
Chaque passage d'origine doit figurer une fois exactement dans le corps au moment où le
correctif s'applique : un passage absent ou ambigu arrête la composition.

Contrôle d'un module sans recomposer : python corrections.py corps.html
(corps.html : sortie de construire_pdf.py --html extrait.html, fichier extrait.corps.html).
"""
import importlib.util, pathlib, sys

ICI = pathlib.Path(__file__).resolve().parent
DOSSIER = ICI / 'correctifs'


_CACHE = []


def modules():
    """Modules de correctifs, chargés une fois : les JOURNAL que remplissent les transformer
    restent visibles de journal() après corriger()."""
    if not _CACHE:
        for f in sorted(DOSSIER.glob('[0-9][0-9]_*.py')):
            spec = importlib.util.spec_from_file_location(f.stem, f)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            _CACHE.append((f.stem, m))
    yield from _CACHE


def corriger(s, strict=True):
    """Applique les correctifs; rend le texte corrigé et la liste des passages remplacés."""
    retires, erreurs = [], []
    for nom, m in modules():
        for i, c in enumerate(m.CORRECTIONS):
            ancien, nouveau = c[0], c[1]
            n = s.count(ancien)
            if n != 1:
                erreurs.append(f'{nom}[{i}] : passage trouvé {n} fois : {ancien[:100]!r}')
                continue
            s = s.replace(ancien, nouveau)
            retires.append(ancien)
        # transformation calculée sur le corps déjà corrigé (p. ex. le registre de l'annexe D)
        if hasattr(m, 'transformer'):
            s, r = m.transformer(s)
            retires.extend(r)
    if erreurs and strict:
        raise AssertionError('correctifs non appliqués :\n' + '\n'.join(erreurs))
    return (s, retires) if strict else (s, retires, erreurs)


def journal():
    for nom, m in modules():
        yield from getattr(m, 'JOURNAL', [])


if __name__ == '__main__':
    corps = pathlib.Path(sys.argv[1]).read_text(encoding='utf8')
    s, retires, erreurs = corriger(corps, strict=False)
    print(f'{len(retires)} correctifs appliqués, {len(erreurs)} en échec')
    for e in erreurs:
        print(e)
    sys.exit(1 if erreurs else 0)
