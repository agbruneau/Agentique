-- Filtre pandoc (HTML -> Typst) commun aux livrables du corpus.
-- 1. Largeur des colonnes : proportionnelle au texte de chaque colonne, bornée par
--    son mot le plus long, pour que les colonnes courtes (Id, p., §) restent étroites.
-- 2. Div « fiche » : la table des rubriques devient un appel #fiche(...) du gabarit.
-- 3. Div data-typst : remplacé par l'appel Typst indiqué (figure propre au document).

local stringify = pandoc.utils.stringify

-- Identifiants à traits d'union (EXIG-AMF-05, AMF-R-04, CRE-IA-2026-01-QC, 2026-10-31) :
-- mis en boîte pour ne jamais se couper en fin de ligne. Un mot composé ordinaire
-- (mi-mars, peut-être) n'a ni chiffre ni deux majuscules et reste sécable. Une
-- adresse ou un chemin (contient « / ») n'est pas mis en boîte : il déborderait.
local boites

function Str(s)
  -- Apostrophe en tête de mot (« MSR ’26 », « (NSDI ’20) ») : pandoc l'écrit « ' », que
  -- Typst, en français, compose en guillemet ouvrant (« MSR “26 »). Elle passe en caractère
  -- littéral, que les guillemets intelligents de Typst ne touchent pas.
  local a, b = s.text:find("^[%(%[]?’")
  if a then
    local out = {}
    if b > #"’" then table.insert(out, pandoc.Str(s.text:sub(1, b - #"’"))) end
    table.insert(out, pandoc.RawInline("typst", "’"))
    if b < #s.text then
      local reste = pandoc.Str(s.text:sub(b + 1))
      for _, x in ipairs(boites(reste) or { reste }) do table.insert(out, x) end
    end
    return out
  end
  return boites(s)
end

boites = function(s)
  local t = s.text
  if t:find("/") then return nil end
  local a, b = t:find("[%w][%w%.]*%-[%w%-%.]*%w")
  if not a then return nil end
  local id = t:sub(a, b)
  local _, maj = id:gsub("%u", "")
  if not (id:find("%d") or maj >= 2) then return nil end
  local out = {}
  if a > 1 then table.insert(out, pandoc.Str(t:sub(1, a - 1))) end
  table.insert(out, pandoc.RawInline("typst", "#{box[" .. id .. "]}"))
  if b < #t then
    local reste = Str(pandoc.Str(t:sub(b + 1)))
    if reste then for _, x in ipairs(reste) do table.insert(out, x) end
    else table.insert(out, pandoc.Str(t:sub(b + 1))) end
  end
  return out
end

local function cell_text(cell)
  return stringify(cell.contents or cell)
end

local function each_row(tbl, fn)
  for _, row in ipairs(tbl.head.rows) do fn(row, true) end
  for _, body in ipairs(tbl.bodies) do
    for _, row in ipairs(body.body) do fn(row, false) end
  end
end

function Table(tbl)
  local n = #tbl.colspecs
  local total, longest, rows = {}, {}, 0
  for i = 1, n do total[i], longest[i] = 0, 0 end
  each_row(tbl, function(row, is_head)
    if not is_head then rows = rows + 1 end
    for i, cell in ipairs(row.cells) do
      local t = cell_text(cell)
      if not is_head then total[i] = total[i] + utf8.len(t) end
      for w in t:gmatch("%S+") do
        -- une adresse ou un chemin se coupe après « / », « . » ou « - » : seul son
        -- plus long segment compte
        if w:find("/") then
          for seg in w:gmatch("[^/%.%-]+") do longest[i] = math.max(longest[i], utf8.len(seg) + 1) end
        else
          longest[i] = math.max(longest[i], utf8.len(w))
        end
      end
    end
  end)
  -- Plancher : le mot le plus long tient sur une ligne (≈ 5,6 pt par signe en
  -- 8 pt, 12 pt de marges internes, sur 468 pt de justification). Au-delà, les
  -- colonnes se partagent la place selon leur longueur moyenne, amortie (^0,75).
  local plancher, poids = {}, {}
  for i = 1, n do
    plancher[i] = (longest[i] * 5.6 + 12) / 468
    poids[i] = (total[i] / math.max(rows, 1)) ^ 0.75 + 1
  end
  local fixe, frac = {}, {}
  local planchers = 0
  for i = 1, n do planchers = planchers + plancher[i] end
  if planchers >= 1 then
    -- les planchers ne tiennent pas ensemble : on les réduit en proportion
    for i = 1, n do tbl.colspecs[i][2] = plancher[i] / planchers end
    return tbl
  end
  repeat
    local reste, somme, change = 1, 0, false
    for i = 1, n do
      if fixe[i] then reste = reste - plancher[i] else somme = somme + poids[i] end
    end
    for i = 1, n do
      if not fixe[i] then
        frac[i] = reste * poids[i] / somme
        if frac[i] < plancher[i] then fixe[i], change = true, true end
      else
        frac[i] = plancher[i]
      end
    end
  until not change
  for i = 1, n do tbl.colspecs[i][2] = frac[i] end
  return tbl
end

local function typst(blocks)
  return pandoc.write(pandoc.Pandoc(blocks), "typst"):gsub("%s+$", "")
end

function Link(el)
  el.target = el.target:gsub("\u{200b}", "")
  local t = stringify(el.content):gsub("\u{200b}", "")
  if t ~= "" and not t:find("%s") and t:find("/") and (t == el.target or (#el.content == 1 and el.content[1].t == "Str")) then
    el.content = { pandoc.Str(t) }
  end
  return el
end

function Span(sp)
  if sp.identifier ~= "" then
    local lbl = pandoc.RawInline("typst", "#metadata(none)<" .. sp.identifier .. ">")
    if #sp.content == 0 then return lbl end
    sp.identifier = ""
    if #sp.classes == 0 and #sp.attributes == 0 then
      local out = { lbl }
      for _, x in ipairs(sp.content) do table.insert(out, x) end
      return out
    end
    return { lbl, sp }
  end
end

function Div(div)
  -- <div data-typst="expr()"> : appel Typst propre au document (figure redessinée…)
  local expr = div.attributes["typst"] or div.attributes["data-typst"]
  if expr then
    return pandoc.RawBlock("typst", "#" .. expr)
  end
  if div.classes:includes("fiche") then
    local tbl = div.content[1]
    local items = {}
    for _, body in ipairs(tbl.bodies) do
      for _, row in ipairs(body.body) do
        for _, cell in ipairs(row.cells) do
          table.insert(items, "[" .. typst(cell.contents) .. "]")
        end
      end
    end
    return pandoc.RawBlock("typst", "#fiche(" .. table.concat(items, ", ") .. ")")
  end
  if div.identifier ~= "" and not (
      div.identifier == "references" or
      div.identifier:find("^exig%-") or
      div.identifier:find("^exigtete%-") or
      div.identifier:find("^encadre%-") or
      div.identifier:find("^pourquoi%-")) then
    if #div.content >= 1 and (div.content[1].t == "Plain" or div.content[1].t == "Para") then
      local lbl = pandoc.RawInline("typst", "#metadata(none)<" .. div.identifier .. ">")
      table.insert(div.content[1].content, 1, lbl)
      div.identifier = ""
      if #div.classes == 0 and #div.attributes == 0 then
        return div.content
      end
    end
  end
end

-- Les largeurs se calculent avant la mise en boîte des identifiants (une boîte
-- Typst brute n'a plus de texte pour stringify).
return { { Link = Link, Table = Table }, { Str = Str, Span = Span, Div = Div } }
