#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La porte de fraicheur de l'empaquetage web, que rien ne tenait.

⚠ CE CONTROLE EXISTE PARCE QUE LE DEFAUT S'EST PRODUIT, ET QUE LE DOSSIER
L'AVAIT ECRIT SANS POUVOIR L'EMPECHER. Le `README.md` (§ « 2. L'interface web »)
et le `CLAUDE.md` publient un couple de chiffres — module brut et module
compresse, pour NF-08 — en le declarant valide « jusqu'a la prochaine edition de
`crates/sim-viz/` ». La regle est juste ; elle n'etait tenue par personne. Le
banc du 17 aout 2026 a trouve l'empaquetage vieux de DEUX revisions de
l'interface — un module qui ne contenait aucun des changements du 14 aout —,
puis son propre correctif perime d'une revision en DOUZE MINUTES.

*Un chiffre ecrit sans la commande qui le produit se perime sans que rien ne le
signale* — c'est la lecon que le §0.2 du PRD tire de sa campagne, et le present
fichier en est l'application au seul poste qui l'echappait encore.

DEUX MODES, ET LE SECOND EXISTE PARCE QUE LE PREMIER A CRIE AU LOUP
-------------------------------------------------------------------
  1. **Le contenu — c'est LE verdict.** Le module est refait dans un dossier
     jetable et compare OCTET A OCTET a celui de `web/`.
  2. **Les dates**, qui ne servent qu'a EXPLIQUER un ecart et a replier quand la
     chaine manque. ⚠ *Elles ne peuvent pas etre un verdict* : ecrire dans le
     module met sa date a jour, de sorte qu'un module altere a la main
     n'aurait plus aucune source posterieure a lui. La premiere version de ce
     fichier en faisait un prealable au mode 1, et la mutation du 2 septembre
     2026 l'a prise en defaut — *un controle qu'on satisfait en touchant le
     fichier qu'il surveille ne surveille pas ce fichier.*

⚠ **Le second a ete ajoute le jour meme de la mise en service du premier, et par
sa faute.** Le 2 septembre 2026, le mode par dates a declare l'empaquetage
perime : `crates/sim-viz/src/lib.rs` etait bien posterieur au module. Refait, le
module est sorti **identique a l'octet** — le seul changement du commit
incrimine, `7a1b7f2` du 25 aout 2026, portait sur **deux lignes de commentaire
de documentation**, qui ne produisent aucun code. *Une date posterieure dit
qu'on ne sait pas ; elle ne dit pas qu'on a tort, et un controle qui confond les
deux se fait desactiver a la troisieme fausse alerte.*

☑ **La construction WASM s'est revelee REPRODUCTIBLE A L'OCTET a cette
occasion**, ce que le dossier n'avait jamais mesure — deux constructions de la
meme source par la meme chaine donnent le meme module, empreinte comprise. C'est
ce qui rend le mode 2 possible ; sans cette propriete, il n'aurait rien pu
conclure.

CE QUE CE CONTROLE NE MESURE PAS. Ni ce que le module fait, ni la PARITE
natif/WASM — c'est le banc `bancs/parite-wasm` qui la mesure, et il doit etre
rejoue apres tout reempaquetage reel.

⚠ SUR UN DEPOT FRAIS, LE MODULE EST ABSENT : `web/sim_viz_bg.wasm` n'est pas
versionne (`.gitignore`), etant un produit. Le controle le DIT plutot que de
conclure a la fraicheur, et sort 0 — exiger sa presence rendrait ce fichier
rouge chez tout lecteur qui n'a jamais construit l'interface.

Usage : python Python/check-empaquetage.py [--dates-seules]
        -> 0 si le module est a jour ou legitimement absent ; 1 s'il est perime
           ou si la fraicheur reste INDETERMINEE.
        `--dates-seules` s'arrete au mode 1, pour l'iteration rapide.
        Le mode 2 exige `cargo`, `wasm-bindgen`, la cible
        `wasm32-unknown-unknown` et `CARGO_TARGET_DIR` pose hors de OneDrive.
Se lance de n'importe quel repertoire : les defauts se resolvent contre
l'emplacement du script, jamais contre le repertoire courant.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(os.environ.get('TRAITE_RACINE', Path(__file__).resolve().parent.parent))
MODULE = RACINE / 'web' / 'sim_viz_bg.wasm'
GLU = RACINE / 'web' / 'sim_viz.js'
SOURCES = RACINE / 'crates' / 'sim-viz'

# La commande qui repare, citee telle qu'elle est ecrite au README et a
# DEVELOPPEMENT.md. ⚠ Ce qui se cite d'ici est la LIGNE, jamais le nombre.
REMEDE = (
    'cargo build -p sim-viz --release --lib --target wasm32-unknown-unknown \\\n'
    '  && wasm-bindgen --target web --no-typescript --out-dir web \\\n'
    '     "$CARGO_TARGET_DIR/wasm32-unknown-unknown/release/sim_viz.wasm"'
)


def refaire(dossier: Path):
    """Reconstruit le module dans un dossier jetable, et rend son chemin.

    ⚠ N'ECRIT JAMAIS DANS `web/` : un controle qui repare ce qu'il mesure ne
    mesure plus rien. La construction va dans `CARGO_TARGET_DIR` comme toute
    autre, et `wasm-bindgen` ecrit a cote, hors du depot.
    """
    cible = os.environ.get('CARGO_TARGET_DIR')
    if not cible:
        return None, ('CARGO_TARGET_DIR n\'est pas pose — la construction irait dans le '
                      '`target/` du depot, ou l\'edition de liens echoue (voir le README)')
    r = subprocess.run(['cargo', 'build', '-p', 'sim-viz', '--release', '--lib',
                        '--target', 'wasm32-unknown-unknown'],
                       cwd=RACINE, capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    if r.returncode != 0:
        return None, 'la construction WASM a echoue : ' + (r.stderr or '').strip()[-300:]
    brut = Path(cible) / 'wasm32-unknown-unknown' / 'release' / 'sim_viz.wasm'
    if not brut.exists():
        return None, f'construction faite, mais {brut} est absent'
    r = subprocess.run(['wasm-bindgen', '--target', 'web', '--no-typescript',
                        '--out-dir', str(dossier), str(brut)],
                       cwd=RACINE, capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    if r.returncode != 0:
        return None, 'wasm-bindgen a echoue : ' + (r.stderr or '').strip()[-300:]
    refait = dossier / 'sim_viz_bg.wasm'
    return (refait, None) if refait.exists() else (None, 'wasm-bindgen n\'a pas ecrit le module')


def contenu(module: Path):
    """Le module versionne est-il CELUI que les sources produisent aujourd'hui ?

    ⚠ CE MODE EXISTE PARCE QUE LE MODE PAR DATES A CRIE AU LOUP LE JOUR DE SA
    MISE EN SERVICE. Le 2 septembre 2026, il a declare l'empaquetage perime :
    une source de `sim-viz` etait bien posterieure au module. Refait, le module
    est sorti **identique a l'octet** — le seul changement du commit incrimine
    portait sur **deux lignes de commentaire de documentation**, qui ne
    produisent aucun code. *Une date posterieure dit qu'on ne SAIT pas ; elle ne
    dit pas qu'on a tort, et un controle qui confond les deux se fait desactiver
    a la troisieme fausse alerte.*

    La construction s'est revelee reproductible a l'octet a cette occasion, ce
    que le dossier n'avait jamais mesure : c'est ce qui rend ce mode possible.
    Il coute une trentaine de secondes et la cible `wasm32-unknown-unknown`.
    """
    with tempfile.TemporaryDirectory(prefix='fraicheur-wasm-') as tmp:
        refait, erreur = refaire(Path(tmp))
        if erreur:
            return None, erreur
        a, b = module.read_bytes(), refait.read_bytes()
    return (a == b), (f'{len(a)} octets versionnes contre {len(b)} refaits' if a != b
                      else f'{len(a)} octets, identiques a l\'octet')

def main():
    print('Porte de fraicheur — empaquetage web / crates/sim-viz')

    if not SOURCES.is_dir():
        print(f'  introuvable : {SOURCES}')
        return 1

    sources = sorted(SOURCES.rglob('*.rs')) + [SOURCES / 'Cargo.toml']
    sources = [s for s in sources if s.exists()]
    if not sources:
        print('  aucune source dans crates/sim-viz -> controle inapplicable')
        return 1

    if not MODULE.exists():
        # ⚠ PAS un echec, et le motif est au `.gitignore` : le module est un
        # PRODUIT, exclu du suivi de version. Sur un depot frais il n'existe
        # pas, et exiger sa presence rendrait ce controle rouge chez tout
        # lecteur qui n'a jamais construit l'interface.
        print(f'  module absent ({MODULE.relative_to(RACINE).as_posix()}) -> NON MESURE')
        print("  Il n'est pas versionne (.gitignore) : sur un depot frais, c'est l'etat normal.")
        print('  Les chiffres NF-08 publies au README ne decrivent alors AUCUN fichier present.')
        return 0

    posterieures = [s for s in sources if s.stat().st_mtime > MODULE.stat().st_mtime]
    if posterieures:
        print(f'  indice : {len(posterieures)} source(s) posterieure(s) au module —')
        for s in posterieures:
            print(f'    {s.relative_to(RACINE).as_posix()}')

    # ⚠ LE VERDICT EST LE CONTENU, JAMAIS LES DATES, et la seconde mutation du
    # 2 septembre 2026 dit pourquoi : le mode par dates etait d'abord un
    # PREALABLE au mode par contenu, de sorte qu'un module altere a la main
    # passait — ecrire dedans met sa date a jour, donc plus aucune source ne lui
    # est posterieure, donc on ne comparait rien. *Un controle qu'on satisfait
    # en touchant le fichier qu'il surveille ne surveille pas ce fichier.* Les
    # dates ne servent plus qu'a EXPLIQUER un ecart, et a replier quand la
    # chaine manque.
    if '--dates-seules' in sys.argv:
        etat = 'INDETERMINE' if posterieures else 'aucune source posterieure'
        print(f'  -> {etat} (--dates-seules) : le contenu n\'est pas compare.')
        return 1 if posterieures else 0
    if shutil.which('cargo') is None or shutil.which('wasm-bindgen') is None:
        print("  -> INDETERMINE : cargo et/ou wasm-bindgen absents, le contenu n'est pas")
        print("     comparable. Le module PEUT etre a jour ; rien ici ne l'etablit.")
        return 1

    print('  Refait pour comparaison (une trentaine de secondes)...')
    egal, detail = contenu(MODULE)
    if egal is None:
        print(f'  -> INDETERMINE : {detail}')
        return 1
    if egal:
        glu = GLU.stat().st_size if GLU.exists() else 0
        print(f'  -> A JOUR : {detail} ; glu {glu} octets.')
        if posterieures:
            print('     Les sources posterieures ne changent donc PAS le module produit —')
            print('     commentaire, documentation, ou code sans effet sur la sortie.')
        print("  ⚠ La PARITE natif/WASM, elle, n'est pas mesuree ici : bancs/parite-wasm.")
        return 0
    print(f'  -> ECHEC : {detail}.')
    print('  Le module versionne n\'est pas celui que les sources produisent, et les chiffres')
    print('  NF-08 publies au README et au CLAUDE.md decrivent une autre construction.')
    print('  Refaire, reporter les deux chiffres avec leur date, et rejouer bancs/parite-wasm :')
    print('')
    for ligne in REMEDE.split('\n'):
        print('    ' + ligne)
    return 1


if __name__ == '__main__':
    sys.exit(main())
