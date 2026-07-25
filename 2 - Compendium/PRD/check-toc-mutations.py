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
    ("M1",  "TOC.md", "### Chapitre 30 —", "### Chapitre 99 —", "C1"),
    ("M2",  "TOC.md", "# LIVRE X —", "# LIVRE XI —", "C2"),
    ("M3a", "TOC.md", "~40 000 mots)*", "~45 000 mots)*", "C3"),
    ("M3b", "TOC.md",
     "Sections : généalogie (comptes de service → workload identity)",
     "Sections (~5 000 mots) : généalogie (comptes de service → workload identity)", "C3"),
    ("M4",  "TOC.md", "renvoi ch. 56", "renvoi ch. 58", "C4"),
    ("M5",  "TOC.md", "obligations des Livres V-VII", "obligations des Livres V-XII", "C5"),
    ("M6",  "TOC.md", "(Vol. III *TOC* §6.3", "(Vol. III §6.3", "C6"),
    ("M7",  "TOC.md", "Vol. II ***Monographie*** Annexe B (matrice détaillée",
     "Vol. II Annexe B (matrice détaillée", "C7"),
    ("M8",  "TOC.md", "Garde-fou : R-5 du Vol. II.*", "Garde-fou : R-5.*", "C8"),
    ("M9a", "TOC.md", "| §10.7 ", "| §10.77 ", "C9"),
    ("M9b", "TOC.md", "**Lacune héritée portée : PRD Vol. II §10.2** — réduite",
     "**Lacune héritée portée** — réduite", "C9"),
    ("M10", "TOC.md", "croisement grille × maturité (corpus d'appui — construction d'auteur)",
     "croisement grille × maturité (construction d'auteur)", "C10"),
    ("M11a", "TOC.md", "⚠ **relève v0.11 — la généralisation de la pile a un nom de scène",
     "⚠ **note — la généralisation de la pile a un nom de scène", "C11"),
    ("M11b", "TOC.md", "**6. L'après-agentique se donne des échelles",
     "**Sixième relève — L'après-agentique se donne des échelles", "C11"),
    ("M12", "TOC.md", "*Fusion : Vol. III ch. 12 + Vol. I* Monographie",
     "*Fusion : Vol. III *TOC* §12.1 + Vol. I* Monographie", "C12"),
    ("M13", "TOC.md", "d'un ouvrage à 57 chapitres", "d'un ouvrage à 54 chapitres", "C13"),
    ("M14", "README.md", "**v0.14** (23 juillet 2026)", "**v0.10** (21 juillet 2026)", "C14"),
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
