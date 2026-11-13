-- Convertit une unité HTML de l'édition G vers le Markdown du manuscrit.
-- Style aligné sur l'édition C : gras réservé aux amorces, police de code
-- réservée au code (les noms de produits et de normes repassent en texte).

local function ensemble(liste)
  local e = {}
  for mot in liste:gmatch("[^|]+") do e[mot] = true end
  return e
end

-- Noms qui commencent par une minuscule (le reste des minuscules est du code).
local NOMS_MIN = ensemble("agentgateway|x402|vLEI|mTLS|vLLM|dbt|z/OS|llm-d|gVisor|gRPC|eBPF|"
  .. "z/OS Connect|z/OS Connect Enterprise Edition|dbt Semantic Layer|mTLS SPIFFE|"
  .. "art. 18.1|art. 4|kW|kPa|bar|rms|kurtosis|p95|p99|scale-to-zero|iframe|"
  .. "v1.0|v2.1|v2.2|v2.3|v2.4|v4.2|v4.3|garantie|stock|client|priorité SLA|"
  .. "annuler affectation FSM|libérer réservation MM|entrée X → score Y")

-- Noms de produits et de techniques à casse mixte (les autres sont des identifiants).
local NOMS_CASSE = ensemble("OpenSandbox|ServiceNow|OpenTelemetry|OpenEnv|WebMCP|LoRA|WebRTC|"
  .. "DPoP|AgentOps|IoT|WebAuthn|PackML|WebSockets|FinOps|ReAct|OpenAPI|JavaScript|"
  .. "JetStream|SoD|SemVer+Intent|OpenLineage|PromQL|TreeKEM|LangGraph|CrewAI|"
  .. "WebAssembly|AsyncAPI|NetSuite|InfluxDB|SemVer|RxNorm|FalkorDB|AutoGen|"
  .. "CloudEvents|RoCEv2|InfiniBand|MuleSoft|SharePoint|CycloneDX|CaMeL|DevOps|"
  .. "PostgreSQL|RocksDB|LiFePO4|FSoE|LiDAR|QoS|PyPI|QLoRA|RadixAttention")

local function est_nom(s)
  if NOMS_MIN[s] or NOMS_CASSE[s] then return true end
  if s:find("^%u[%w ]* %([%u%d/%-]+%)$") then return true end   -- « IBM i (AS/400) »
  if s:find("^[<>=%-%d,%. ]+ ?%%?$") then return true end       -- valeur chiffrée
  if s:find("[_%(%){}%[%]<>=;%*%$@#\"'\\|~%%%^:]") then return false end
  if s:find("%.%a") then return false end        -- fichier.ext, objet.champ
  if s:find("/%l") then return false end         -- chemin ou méthode
  if s:find("^%-") or s:find("^%l") then return false end
  if not s:find("[ %-/]") and s:find("%l%u") then return false end   -- identifiant
  return true
end

local function sans_gras(inlines)
  return inlines:walk({ Strong = function(el) return el.content end })
end

-- « OpenTelemetry gen_ai.* » : le nom repasse en texte, l'identifiant reste du code.
local function scinde(c)
  local nom, ouvre, ident, ferme = c.text:match("^(%u[%w]+) (%(?)([%l_][%w_%.%*]+)(%)?)$")
  if nom and est_nom(nom) and not est_nom(ident) then
    return { pandoc.Str(nom), pandoc.Space(), pandoc.Str(ouvre), pandoc.Code(ident),
             pandoc.Str(ferme) }
  end
end

-- Le gras ne subsiste qu'en amorce de paragraphe, d'élément de liste ou de cellule.
local function amorce(bloc)
  local c = bloc.content
  if #c == 0 then return bloc end
  local garde = c[1].t == "Span" and c[1].classes:includes("garde")
  if c[1].t == "Strong" then
    local texte = pandoc.utils.stringify(c[1])
    local suite = c[2] and (c[2].t == "Space" or c[2].t == "SoftBreak") and c[3] or c[2]
    garde = #c == 1 or texte:find("[%.:%?!]$") ~= nil
      or (suite ~= nil and suite.t == "Str" and suite.text:find("^[%.:—%(]") ~= nil)
  end
  local reste = pandoc.Inlines({})
  for i = garde and 2 or 1, #c do reste:insert(c[i]) end
  reste = sans_gras(reste)
  if garde then reste:insert(1, c[1]) end
  bloc.content = reste
  return bloc
end

return {
  {
    -- Dans un tableau, le gras en tête de cellule est un libellé : il reste.
    Table = function(t)
      return t:walk({
        Plain = function(b)
          if #b.content > 0 and b.content[1].t == "Strong" then
            b.content[1] = pandoc.Span({ b.content[1] }, pandoc.Attr("", { "garde" }))
            return b
          end
        end,
      })
    end,
  },
  {
    Code = function(c)
      if est_nom(c.text) then return pandoc.Str(c.text) end
      return scinde(c)
    end,
  },
  {
    Para = amorce,
    Plain = amorce,
    Header = function(h)
      h.identifier = ""
      h.classes = {}
      h.attributes = {}
      h.content = h.content:walk({
        Code = function(c) return pandoc.Str(c.text) end,
        Strong = function(s) return s.content end,
      })
      return h
    end,
    CodeBlock = function(cb)
      cb.identifier = ""
      cb.classes = cb.classes:filter(function(c) return c ~= "sourceCode" end)
      return cb
    end,
    Div = function(d)
      if d.classes:includes("sourceCode") then return d.content end   -- enveloppe de bloc de code
      d.identifier = ""
      if d.classes:includes("compendium-box-header") then
        d.classes = { "encadre-titre" }
        return d
      end
      if d.classes:includes("compendium-box") then
        local genre = "note"
        for _, c in ipairs(d.classes) do
          genre = c:match("^box%-(.+)$") or genre
        end
        d.classes = { "encadre", genre }
        return d
      end
    end,
    Figure = function(f)
      local image
      f:walk({ Image = function(i) image = i end })
      if image then
        local legende = pandoc.utils.blocks_to_inlines(f.caption.long)
        return pandoc.Para({ pandoc.Image(legende, image.src, "") })
      end
    end,
    Span = function(sp)
      if sp.classes:includes("garde") then return sp.content end
    end,
    Table = function(t)
      local largeurs = {}
      for _, spec in ipairs(t.colspecs) do
        largeurs[#largeurs + 1] = string.format("%d", math.floor((spec[2] or 0) * 100 + 0.5))
      end
      return {
        pandoc.RawBlock("html", "<!-- colonnes: " .. table.concat(largeurs, " ") .. " -->"),
        t,
      }
    end,
  },
}
