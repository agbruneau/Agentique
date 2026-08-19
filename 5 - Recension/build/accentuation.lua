--[[ Regle d'accentuation du compendium — filtre Pandoc (31 juillet 2026)

Releve sur le `compendium.pdf` de la veille : 34,7 % des caracteres du texte
courant en gras (mediane de 39,0 % par chapitre, de 5,3 % a 65,2 %), et 4 395
« ⚠ » sur 1 096 pages — quatre par page, sur 1 009 d'entre elles. A ces densites
ni l'un ni l'autre ne signale : le gras est une texture, et le marqueur, en plus
d'etre partout, est HORS FAMILLE (Segoe UI Symbol dans un texte en Constantia).

La regle separe trois choses que le corpus confond sous une seule graisse, et le
critere de la deuxieme est FOURNI PAR L'AUTEUR — c'est le ⚠ qu'il pose devant :

  ⚠ + gras, 1re de sa sous-section -> ITALIQUE, et le ⚠ tombe. C'est l'accent
                     de clause en usage typographique.
  ⚠ + gras, les suivantes          -> ROMAIN, par le budget ci-dessous.
  gras <= 3 mots  -> GRAS CONSERVE. C'est un terme ; le gras le denote.
  gras >  3 mots  -> ROMAIN. Une proposition non signalee n'a pas besoin de
                     relief : la syntaxe la porte.
  ⚠ isole         -> tombe. La phrase qui le suivait reste entiere.

⚠ LE BUDGET D'UNE SAILLANCE PAR SOUS-SECTION EST UNE MESURE, et il a corrige un
premier etat de la regle. Sans lui — toute proposition signalee passant a
l'italique —, le rendu donnait 4,1 % de gras et 32,4 % D'ITALIQUE : la texture
avait change de graisse, pas disparu, et un tiers d'un volume en italique se lit
plus mal que le gras qu'il remplacait. Le ⚠ n'est pas rare : il porte 5 280
propositions, 11,7 % du corps markdown. Le budget en retient une par
sous-section — la premiere, faute de critere qui distingue les autres.
  Ne pas le retirer sans REMESURER la part d'italique sur le PDF.

⚠ POURQUOI UN FILTRE ET NON UNE SUBSTITUTION SUR LE MARKDOWN. Trois etats
successifs de cette regle l'ont tentee en expressions rationnelles, et les trois
ont laisse des asterisques EN CLAIR dans le PDF (44, puis 18, puis 4 sites). Le
motif est indecidable au niveau du texte : `*A **B***` est un gras dans un
italique, `**A *B***` un italique dans un gras, et les deux s'ecrivent avec les
memes six caracteres. Seul l'arbre les distingue — ici, un `Strong` dans un
`Emph` ou l'inverse. Ne pas revenir a une substitution textuelle.

⚠ ELLE NE S'APPLIQUE QU'AUX CINQUANTE PIECES. Dans `annexe-bibliographie.md`,
le ⚠ n'est pas une emphase mais un DRAPEAU pose sur une reference (« ⚠ à
re-vérifier à la rédaction », 460 occurrences), et le gras y distingue des
entrees entre elles. Le filtre s'arrete donc au marqueur `#ouverture-annexe()`
que `assemble.py` pose devant les deux annexes.

⚠ Le seuil de trois mots est MECANIQUE : il compte des mots, il ne sait pas ce
qu'est un terme. Une passe d'auteur tranche au cas par cas, et elle se fait DANS
LES PIECES — retirer un `**` a la source est la seule facon d'en sortir un
passage.

⚠ ☑ ET ✎ SURVIVENT AU PDF, ET C'EST VOULU. La regle ne vise que le ⚠, et le
motif qui la fonde est une DENSITE, non une famille de fontes : quatre marqueurs
par page sur 1 009 pages, 5 280 propositions signalees, 11,7 % du corps — a ce
regime, le ⚠ ne signale plus rien. Les deux autres marqueurs de la recension
sont a un tout autre ordre : six ☑ et trois ✎ pour 127 pages, un par quatorze
pages. Ils portent chacun un etat que la prose ne redit pas — ☑ « reverifie a la
source », ✎ « corrige contre une edition anterieure » — et ils sont assez rares
pour que le lecteur les compte. Les retirer couterait l'information sans rien
rendre en lisibilite. ⚠ Si leur nombre venait a croitre d'un ordre de grandeur,
c'est la MESURE qui trancherait, pas cette note.
]]

local budget = true      -- une saillance a depenser, rendue a chaque titre
local annexe = false     -- passe l'ouverture d'annexe, le filtre se retire

local MARQUE = "⚠"

-- Un gras de trois mots ou moins est un terme, et il reste gras.
local function est_terme(strong)
  local n = 0
  for _ in pandoc.utils.stringify(strong.content):gmatch("%S+") do n = n + 1 end
  return n <= 3
end

-- Rend TOUJOURS une liste : `extend` la consomme telle quelle des deux cotes.
local function degrade(strong)
  if budget then
    budget = false
    return pandoc.List({pandoc.Emph(strong.content)})
  end
  return strong.content          -- rendu au romain
end

-- ⚠ LE PARCOURS EST PILOTE ICI, ET PAS PAR DES FONCTIONS `Header` / `RawBlock`
-- laissees a l'ordre de visite de Pandoc. Un premier etat les posait ainsi, et
-- la borne d'annexe n'a jamais pris : le filtre a vide les 460 drapeaux de la
-- bibliographie avec le reste. Un `Pandoc` qui itere `doc.blocks` lui-meme rend
-- l'ordre explicite — la borne se pose avant le bloc suivant, pas apres.
function Pandoc(doc)
  local sortie = pandoc.List({})
  for _, bloc in ipairs(doc.blocks) do
    if bloc.t == "RawBlock" and bloc.text:find("ouverture%-annexe") then
      annexe = true
    elseif bloc.t == "Header" then
      budget = true
    end
    if annexe then
      sortie:insert(bloc)
    else
      sortie:insert(pandoc.walk_block(bloc, {Inlines = accentue}))
    end
  end
  return pandoc.Pandoc(sortie, doc.meta)
end

function accentue(inl)
  local sortie, i = pandoc.List({}), 1
  while i <= #inl do
    local el = inl[i]
    if el.t == "Str" and el.text:find(MARQUE) then
      -- Le marqueur tombe ; ce qui reste du jeton, s'il reste quelque chose,
      -- est du texte d'auteur (« (⚠ », « ⚠, ») et se conserve.
      local reste = el.text:gsub(MARQUE, "")
      if reste ~= "" then sortie:insert(pandoc.Str(reste)) end
      -- La cible du marqueur peut etre separee de lui par une espace.
      local j = i + 1
      while inl[j] and inl[j].t == "Space" do j = j + 1 end
      if inl[j] and inl[j].t == "Strong" then
        sortie:extend(degrade(inl[j]))
        i = j + 1
      else
        -- ⚠ devant un italique, ou devant rien : seul le marqueur tombe.
        i = i + 1
        if reste == "" and inl[i] and inl[i].t == "Space" then i = i + 1 end
      end
    elseif el.t == "Strong" and not est_terme(el) then
      sortie:extend(el.content)
      i = i + 1
    else
      sortie:insert(el)
      i = i + 1
    end
  end
  return sortie
end
