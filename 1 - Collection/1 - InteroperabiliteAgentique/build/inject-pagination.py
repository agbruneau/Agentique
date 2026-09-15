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

# 3) Résumé anglais : page « Abstract » entre le Résumé et la table des matières (tâche T7.1 du
#    plan d'exécution, 15 septembre 2026). Traduction du résumé de Monographie.md avec assistance
#    de modèle, non relue par un humain. Il est posé ici et non dans Monographie.md, dont
#    `2 - Compendium/PRD/decompte.sh --verifier` gèle le décompte de mots ; il ne suit donc pas
#    sa source d'elle-même : qui reprend le Résumé reprend ce texte.
ABSTRACT_EN = """\
This monograph builds, in a spiral from the general to the specific, a unified reading of interoperability in the era of artificial intelligence agents. It addresses a dual audience — research (models, formalisms, state of the art, open questions) and the practitioner-architect (standards, protocols, dated implementations) — and holds to a cross-cutting invariant: *decoupling, contract, evolution*. Chapter 1 establishes the theory of information systems interoperability from the standpoint of enterprise integration. Chapter 2 sets out the engineering of agentic systems built on large language models. Chapter 3 brings the two together into an agentic interoperability layer (MCP, A2A, ANP; discovery, semantics, identity, commerce, boundary security). Chapter 4 addresses its deployment at enterprise scale (legacy applications, non-human identities, governance, compliance). Chapter 5 specializes the analysis to the financial domain and its five subdomains, under the pattern of “graduated autonomy under purpose control”. Chapter 6 formalizes the whole into an ArchiMate 4 enterprise architecture *blueprint*. Chapter 7, prospective and a *capstone*, projects the arc of the six chapters onto the 2027-2032 horizon, sorting each statement about the future into **PROGRAMMÉ** (programmed), **PROJETÉ** (projected) and **SPÉCULATIF** (speculative). The documentary base is closed as of June 2026."""
toc = '```{=typst}\n#pagebreak()\n#outline('
assert src.count(toc) == 1
src = src.replace(toc, '# Abstract {.unnumbered}\n\n::: {lang=en}\n' + ABSTRACT_EN + '\n:::\n\n' + toc, 1)

open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(src)
print("injecté ->", sys.argv[2])
