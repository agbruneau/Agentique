-- Composition : les encadrés du manuscrit deviennent des appels #encadre du gabarit.

local function chaine_typst(s)
  return '"' .. s:gsub("\\", "\\\\"):gsub('"', '\\"') .. '"'
end

-- Titres qui ne font que répéter le libellé du genre d'encadré.
local REDONDANTS = { ["Synthèse exécutive"] = true, ["Important"] = true,
                     ["Avertissement"] = true, ["Conseil"] = true, ["Tip"] = true,
                     ["Warning"] = true, ["Note"] = true, ["Attention"] = true }

return {
  {
    Div = function(d)
      if not d.classes:includes("encadre") then return nil end
      local genre = "note"
      for _, c in ipairs(d.classes) do
        if c ~= "encadre" then genre = c end
      end
      local titre = ""
      local corps = pandoc.Blocks({})
      for _, b in ipairs(d.content) do
        if b.t == "Div" and b.classes:includes("encadre-titre") then
          titre = pandoc.utils.stringify(b.content)
        else
          corps:insert(b)
        end
      end
      titre = titre:gsub("^Fil rouge — ", ""):gsub("'", "’")
      if REDONDANTS[titre] then titre = "" end
      local sortie = pandoc.Blocks({})
      sortie:insert(pandoc.RawBlock("typst",
        "#encadre(" .. chaine_typst(genre) .. ", " .. chaine_typst(titre) .. ")["))
      sortie:extend(corps)
      sortie:insert(pandoc.RawBlock("typst", "]"))
      return sortie
    end,
  },
}
