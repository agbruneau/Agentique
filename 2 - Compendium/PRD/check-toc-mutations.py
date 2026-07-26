# -*- coding: utf-8 -*-
"""check-toc-mutations.py — validation par mutation de check-toc.py (Vol. IV).

Pour chaque mutation : copie TOC.md, README.md et check-toc.py dans un
dossier temporaire, applique la faute, exécute le script et exige un échec
portant le contrôle attendu. Préalable vérifié d'abord : le script passe sur
le document intact. Sortie 0 si toutes les mutations sont détectées, 1 sinon.

À exécuter après toute modification de check-toc.py (protocole du CLAUDE.md
du dossier). Versionné pour que la validation soit rejouable depuis le dépôt
— leçon des chemins `Tocs/…` du journal v0.5 du TOC, non rejouables.

⚠ Les motifs `ancien` des mutations sont du contenu : si une passe du TOC les
réécrit, la mutation devient inapplicable et le harnais échoue en le disant —
réancrer le motif sur le texte courant, ne pas supprimer la mutation."""
import io
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC = Path(__file__).resolve().parent


def _src(f):
    """Emplacement réel de chaque fichier : TOC.md et check-toc.py vivent dans PRD/
    (SRC) ; le README (conspectus) vit à la racine du dossier (SRC.parent). Copié
    ensuite à plat dans le dossier temporaire, où check-toc.py les trouve côte à côte."""
    p = SRC / f
    return p if p.exists() else SRC.parent / f

MUTATIONS = [
    # (id, fichier, ancien, nouveau, contrôle attendu)
    # ⚠ Réancrage v0.20 : la condensation à cinq livres et cinquante chapitres a
    # périmé six motifs (M2, M3a, M4, M5, M9b, M13). Réancrés sur le texte courant,
    # jamais supprimés — c'est la règle posée en tête de ce fichier.
    ("M1",  "TOC.md", "### Chapitre 30 —", "### Chapitre 99 —", "C1"),
    ("M2",  "TOC.md", "# LIVRE V — Livrer", "# LIVRE VI — Livrer", "C2"),
    ("M3a", "TOC.md", "~65 000 mots)*", "~70 000 mots)*", "C3"),
    ("M3b", "TOC.md",
     "Sections : généalogie (comptes de service → workload identity)",
     "Sections (~5 000 mots) : généalogie (comptes de service → workload identity)", "C3"),
    ("M4",  "TOC.md", "renvoi ch. 39 (d", "renvoi ch. 58 (d", "C4"),
    ("M5",  "TOC.md", "obligations des Livres III-IV,", "obligations des Livres III-XII,", "C5"),
    ("M6",  "TOC.md", "(Vol. III *TOC* §6.3", "(Vol. III §6.3", "C6"),
    ("M7",  "TOC.md", "Vol. II ***Monographie*** Annexe B (matrice détaillée",
     "Vol. II Annexe B (matrice détaillée", "C7"),
    ("M8",  "TOC.md", "Garde-fou : R-5 du Vol. II.*", "Garde-fou : R-5.*", "C8"),
    ("M9a", "TOC.md", "| §10.7 ", "| §10.77 ", "C9"),
    # M9b teste la seconde branche de C9 — « le chapitre désigné nomme-t-il la
    # lacune ? » — en détournant la cellule du registre vers un chapitre muet.
    # L'ancien motif (retrait de la mention dans le chapitre porteur) ne mord plus
    # depuis la v0.16 : les tables détaillées la répètent, et C9 trouve la copie.
    ("M9b", "TOC.md", "| §10.3               | Frameworks — réduite en P0, ne subsiste que Temporal"
     "                                                                       | ch. 23",
     "| §10.3               | Frameworks — réduite en P0, ne subsiste que Temporal"
     "                                                                       | ch. 2", "C9"),
    ("M10", "TOC.md", "croisement grille × maturité (corpus d'appui — construction d'auteur)",
     "croisement grille × maturité (construction d'auteur)", "C10"),
    # M11a teste le décompte du journal v0.10 ; M11b celui du journal v0.11.
    # ⚠ La branche « la marque de relève est présente dans le chapitre » n'est plus
    # testable par substitution unique : depuis la v0.16, chaque marque figure au
    # moins deux fois par chapitre (entrée + table détaillée), de sorte qu'en
    # retirer une laisse la seconde satisfaire le contrôle. Lacune du harnais,
    # déclarée au journal v0.20 plutôt que masquée par une mutation qui ne mord pas.
    ("M11a", "TOC.md", "**1. Le harnais est un objet que la somme ne nomme nulle part.**",
     "**Première relève — Le harnais est un objet que la somme ne nomme nulle part.**", "C11"),
    ("M11b", "TOC.md", "**6. L'après-agentique se donne des échelles",
     "**Sixième relève — L'après-agentique se donne des échelles", "C11"),
    ("M12", "TOC.md", "*Fusion : Vol. III ch. 12 + Vol. I* Monographie",
     "*Fusion : Vol. III *TOC* §12.1 + Vol. I* Monographie", "C12"),
    ("M13", "TOC.md", "d'un ouvrage à 50 chapitres", "d'un ouvrage à 54 chapitres", "C13"),
    ("M14", "README.md", "**v0.20** (26 juillet 2026)", "**v0.10** (21 juillet 2026)", "C14"),
]


def run_in(tmp):
    return subprocess.run([sys.executable, "check-toc.py"], cwd=tmp,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def main():
    results, ok = [], True
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        intact = base / "intact"
        intact.mkdir()
        for f in ("TOC.md", "README.md", "check-toc.py"):
            shutil.copy(_src(f), intact / f)
        r = run_in(intact)
        if r.returncode != 0:
            print("ÉCHEC PRÉALABLE — le script ne passe pas sur le document intact :")
            print(r.stdout)
            return 1
        results.append(("intact", "PASSE (attendu)", True))

        for mid, fname, old, new, ctrl in MUTATIONS:
            d = base / mid
            d.mkdir()
            for f in ("TOC.md", "README.md", "check-toc.py"):
                shutil.copy(_src(f), d / f)
            target = d / fname
            content = target.read_text(encoding="utf-8")
            if old not in content:
                results.append((mid, f"MUTATION INAPPLICABLE — motif absent : {old[:60]}", False))
                ok = False
                continue
            target.write_text(content.replace(old, new, 1), encoding="utf-8")
            r = run_in(d)
            failed = r.returncode != 0
            tagged = f"[{ctrl}]" in r.stdout
            good = failed and tagged
            ok = ok and good
            verdict = "DÉTECTÉE" if good else ("échec sans le bon contrôle" if failed else "NON DÉTECTÉE")
            results.append((mid, f"{verdict} (attendu {ctrl})", good))

    for mid, verdict, good in results:
        print(f"  {'OK ' if good else 'KO '}{mid:6} {verdict}")
    print("\nBILAN :", "toutes les mutations sont détectées" if ok else "DES MUTATIONS ÉCHAPPENT AU SCRIPT")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
