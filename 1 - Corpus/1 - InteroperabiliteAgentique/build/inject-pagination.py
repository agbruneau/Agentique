import sys
src = open(sys.argv[1], encoding='utf-8').read()

# 1) Numérotation romaine à partir du Résumé (pages liminaires)
roman = '```{=typst}\n#set page(numbering: "i")\n```\n\n'
assert '# Résumé {.unnumbered}' in src
src = src.replace('# Résumé {.unnumbered}', roman + '# Résumé {.unnumbered}', 1)

# 2) Numérotation arabe (reset à 1) à partir de l'Introduction
arabic = '```{=typst}\n#pagebreak(weak: true)\n#set page(numbering: "1")\n#counter(page).update(1)\n```\n\n'
assert '\n# Introduction\n' in src
src = src.replace('\n# Introduction\n', '\n' + arabic + '# Introduction\n', 1)

open(sys.argv[2], 'w', encoding='utf-8').write(src)
print("injecté ->", sys.argv[2])
