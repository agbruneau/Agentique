#!/usr/bin/env bash
# Reconstruit un PDF FESP depuis un fichier .md source.
#   Usage : bash build/build-pdf.sh [source.md]      (défaut : Monographie.md)
#   Ex.   : bash build/build-pdf.sh "Synthese Monographie.md"
#
# Étapes : (1) pré-rendu des blocs ```mermaid en SVG (mermaid-cli, libellés SVG natifs ;
#          diagrammes larges placés en page paysage avec légende), (2) pagination liminaire
#          (Monographie uniquement), (3) Pandoc -> Typst, (4) compilation Typst.
#
# Prérequis : Pandoc >= 3.1.7, Typst >= 0.12, python3 + pypdf, polices Liberation Sans + DejaVu Sans.
#   Diagrammes : Node >= 18 + @mermaid-js/mermaid-cli (mmdc) + un Chromium.
#   Surcharges optionnelles : MMDC=<chemin mmdc>, PUPPETEER_CONFIG=<config.json>,
#                             DIAGCACHE=<dir de SVG diagram-NN.svg pré-rendus> (réutilisés tels quels).
#   Si mmdc est absent, les diagrammes restent en bloc de code (mode dégradé, sans échec).
set -euo pipefail
export PYTHONUTF8=1   # Windows : sans quoi les sous-processus Python encodent en cp1252 et plantent sur ⚠/flèches.
for _t in pandoc typst python3; do
  command -v "$_t" >/dev/null 2>&1 || { echo "[build] Dépendance manquante : $_t (requis : Pandoc, Typst, python3+pypdf)." >&2; exit 1; }
done
if ! typst fonts 2>/dev/null | grep -qi "liberation sans"; then
  echo "[build] Avertissement : police « Liberation Sans » introuvable ; Typst se rabat sur Arial/DejaVu (repli déclaré au gabarit)." >&2
fi
DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${1:-$DIR/Monographie.md}"
case "$SRC" in /*) ;; *) SRC="$DIR/$SRC";; esac
BASE="$(basename "$SRC" .md)"
OUT="$DIR/$BASE.pdf"
TPL="$DIR/build/fesp.template"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT   # nettoyage des SVG/typ intermédiaires (sauf DIAGCACHE, séparé).
MMDC="${MMDC:-$(command -v mmdc || true)}"
# Windows/Git-bash : le subprocess Python ne peut pas exécuter le shim sans extension `mmdc`
# (échoue en WinError 193) ; préférer le shim `mmdc.cmd` quand il existe à côté.
if [ -n "$MMDC" ] && [ -f "$MMDC.cmd" ]; then MMDC="$MMDC.cmd"; fi
PUP="${PUPPETEER_CONFIG:-}"
CACHE="${DIAGCACHE:-}"
# Windows : un mmdc installé sans Chromium (PUPPETEER_SKIP_DOWNLOAD) exige un navigateur
# système ; sans config Puppeteer fournie, en générer une (chemin en slashes pour un JSON
# valide) vers un Chrome/Edge local. Sur Linux/mac ces chemins n'existent pas → inchangé.
if [ -z "$PUP" ] && [ -n "$MMDC" ]; then
  for _b in "/c/Program Files/Google/Chrome/Application/chrome.exe" \
            "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
            "/c/Program Files/Microsoft/Edge/Application/msedge.exe" \
            "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"; do
    if [ -f "$_b" ]; then
      _bw="$(cygpath -m "$_b" 2>/dev/null || echo "$_b")"
      printf '{"executablePath":"%s","args":["--no-sandbox"]}' "$_bw" > "$TMP/pup.json"
      PUP="$(cygpath -m "$TMP/pup.json" 2>/dev/null || echo "$TMP/pup.json")"
      break
    fi
  done
fi

# (1) Pré-rendu Mermaid -> SVG (texte natif) + mise en page (paysage si large).
python3 - "$SRC" "$TMP" "$MMDC" "$PUP" "$CACHE" > "$TMP/mm.md" <<'PY'
import os, re, shutil, subprocess, sys, time
src, tmp, mmdc, pup, cache = sys.argv[1:6]
conf = os.path.join(tmp, "mmconf.json")
open(conf, "w").write('{"htmlLabels":false,"flowchart":{"htmlLabels":false,"useMaxWidth":false},'
                      '"sequence":{"useMaxWidth":false},"themeVariables":{"fontFamily":"DejaVu Sans"}}')
text = open(src, encoding="utf-8").read()
items = []
def stash(m):
    items.append((m.group(1), m.group(3))); return f"\x00MMD{len(items)-1}\x00"
text = re.sub(r"```mermaid\n(.*?)```(\n+(\*\*Figure[^\n]*))?", stash, text, flags=re.S)
def render(i, code):
    svg = os.path.join(tmp, f"diagram-{i:02d}.svg")
    if cache and os.path.exists(os.path.join(cache, f"diagram-{i:02d}.svg")):
        shutil.copy(os.path.join(cache, f"diagram-{i:02d}.svg"), svg); return svg
    if not mmdc: return None
    mmd = os.path.join(tmp, f"diagram-{i:02d}.mmd"); open(mmd, "w", encoding="utf-8").write(code)
    cmd = [mmdc, "-i", mmd, "-o", svg, "-c", conf, "-b", "white"]
    if pup: cmd += ["-p", pup]
    last = ""
    for _ in range(3):                           # réessai : démarrage Chromium parfois transitoire
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=120)
            if r.returncode == 0 and os.path.exists(svg): return svg
            last = (r.stderr or b"").decode(errors="replace")[-200:]
        except Exception as e:
            last = str(e)
        time.sleep(1.0)
    sys.stderr.write(f"[build] mmdc a echoue sur diagram-{i:02d} : {last}\n"); return None
def aspect(svg):
    try:
        m = re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ([\d.]+)"', open(svg, encoding="utf-8").read())
        w, h = float(m.group(1)), float(m.group(2)); return (w / h) if h else 1.0
    except Exception: return 1.0
def sanitize(cap):
    if not cap: return ""
    c = re.sub(r'`([^`]*)`', r'\1', cap); c = c.replace('**', '').replace('*', '')
    c = re.sub(r'<<([^>]*)>>', r'«\1»', c)
    for ch in ['\\', '#', '@', '[', ']']: c = c.replace(ch, '\\' + ch)
    return c.strip()
def repl(m):
    i = int(m.group(1)); code, cap = items[i]; svg = render(i, code)
    if not svg:
        sys.stderr.write(f"[build] diagram-{i:02d} laisse en bloc de code (mode degrade)\n")
        return "```text\n" + code + "```" + (("\n\n" + cap) if cap else "")
    f = os.path.basename(svg)
    if aspect(svg) >= 1.7:                        # large -> page paysage dédiée
        cs = sanitize(cap)
        return (f'```{{=typst}}\n#pagebreak(weak: true)\n#page(flipped: true, margin: 1.4cm)[\n'
                f'#v(1fr)\n#align(center, image("{f}", width: 100%))\n#v(0.7em)\n'
                f'#align(center, text(size: 8.5pt, style: "italic")[{cs}])\n#v(1fr)\n]\n```')
    img = (f'```{{=typst}}\n#v(0.3em)\n#align(center, image("{f}", width: 90%))\n#v(0.1em)\n```')
    return img + (("\n\n" + cap) if cap else "")
text = re.sub(r"\x00MMD(\d+)\x00", repl, text)
sys.stdout.write(text)
PY

# (2) Pagination liminaire (romain -> arabe) — propre à la monographie.
if [ "$BASE" = "Monographie" ]; then
  python3 "$DIR/build/inject-pagination.py" "$TMP/mm.md" "$TMP/inj.md"
else
  cp "$TMP/mm.md" "$TMP/inj.md"
fi

# (3) Pandoc -> Typst.
pandoc "$TMP/inj.md" -f markdown-raw_html --template="$TPL" -t typst -o "$TMP/doc.typ"
sed -i 's/align(center)\[#table/align(left)[#table/g' "$TMP/doc.typ"

# (4) Compilation Typst (SVG dans $TMP -> --root $TMP).
typst compile --root "$TMP" "$TMP/doc.typ" "$OUT"
# Compteur de pages : le Python Windows n'ouvre pas un chemin MSYS `/c/...` -> convertir, et
# ne jamais faire échouer le build (set -e) si pypdf est absent ou le chemin illisible.
OUT_NATIVE="$(cygpath -w "$OUT" 2>/dev/null || echo "$OUT")"
echo "Rendu : $OUT ($(python3 -c "import sys;from pypdf import PdfReader;print(len(PdfReader(sys.argv[1]).pages))" "$OUT_NATIVE" 2>/dev/null || echo '?') pages)"
