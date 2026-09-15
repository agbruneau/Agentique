#!/usr/bin/env python3
"""Le contrôle propre au Vol. I — que ce volume n'avait pas jusqu'au 15 septembre 2026.

L'évaluation académique du 15 septembre 2026 le relevait (fiche du Vol. I, faiblesse a) :
« aucun script ne garde ce volume : ni appariement des citations, ni pagination, ni parité
de rendu ». Ce fichier est ce qui les garde (tâche T6.5 du plan d'exécution). ⚠ Il mesure
la forme ; il ne juge pas le propos.

Trois contrôles :
  [1] PAGINATION — le PDF versionné a le nombre de pages que le README du volume publie
      sur sa ligne « Lire » ; compté à deux sources qui doivent concorder, le `/Count` du
      nœud `/Pages` et les objets `/Type /Page`.
  [2] APPARIEMENT — chaque notice des sept bibliographies de `Monographie.md` (rubrique
      « Bibliographie générale ») est retrouvée dans le corps rédigé — de l'introduction à
      la conclusion, et l'Annexe B — par l'une de trois clés : l'auteur ou l'organisme suivi
      de l'année à 160 signes près ; un identifiant stable (RFC, DOI, arXiv, norme ISO/IEC,
      acte « AAAA/NNNN ») ; un jeton distinctif du titre (casse interne, lettres et chiffres,
      sigle d'au moins trois capitales). Sont exemptées les notices que la bibliographie
      déclare elle-même « contexte non cité », et celles du REGISTRE ci-dessous.
  [3] PARITÉ — le PDF versionné est CELUI que `build/build-pdf.sh` rend aujourd'hui, comparé
      à l'octet hors des champs d'horodatage ; la chaîne complète est exigée — Pandoc, Typst,
      `mmdc` (mermaid-cli) et un bash qui ne soit pas le lanceur WSL —, sans quoi il se
      déclare NON MESURÉ plutôt que de passer en silence.

⚠ CE QUE [2] NE FAIT PAS. Il va de la notice au corps, pas du corps à la notice : le volume
cite en auteur-année, et le motif « (Nom, AAAA) » rendait, mesuré le 15 septembre 2026,
135 candidats sans notice sur 1 003 citations, faux positifs en tête (« (AI Act, 2021) »,
« (CVE-2025-6514, 2025) »). Un contrôle qui crie à tort finit désactivé ; celui-ci ne le fait
donc pas, et le dit. ⚠ Et ses clés sont des heuristiques : une notice dont un jeton de titre
revient ailleurs dans le corps passe pour citée. Le harnais `check-vol1-mutations.py` prouve
qu'une notice orpheline ordinaire est vue, pas que toutes le seraient.

⚠ LE REGISTRE N'EST PAS UNE TOLÉRANCE QUI GRANDIT. Il fige les 55 notices que les trois clés
ne retrouvent pas au 15 septembre 2026, volume clos (D-13) : les apparier exigerait de
reprendre le texte. Une notice nouvelle hors registre fait échouer [2] ; une notice du
registre devenue appariée, ou disparue, le fait échouer aussi — le registre ne peut que
rétrécir, et il se met à jour à la main, en le disant.

Usage : python Python/check-vol1.py [--sans-parite]   -> 0 si tout tient, 1 sinon.
Se lance de n'importe quel répertoire ; `VOL1_RACINE` déplace le dossier mesuré, ce dont le
harnais se sert. `--registre` imprime les notices non appariées sous la forme du registre.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zlib
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(os.environ.get("VOL1_RACINE", Path(__file__).resolve().parent.parent))
SRC = RACINE / "Monographie.md"
PDF = RACINE / "Monographie.pdf"
README = RACINE / "README.md"
BUILD = RACINE / "build" / "build-pdf.sh"

fail = []


def ok(n, nom, verdict, detail):
    print(f"  [{n}] {nom:12}: {detail} -> {'OK' if verdict else 'ECHEC'}")
    return verdict


# ------------------------------------------------------------------ [1] pagination

def pages(octets: bytes):
    """(/Count du nœud /Pages, nombre d'objets /Type /Page) — cf. check-traite.py."""
    d = octets
    if not re.search(rb"/Type\s*/Pages", d) and b"/ObjStm" in d:
        for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", d, re.S):
            try:
                d += zlib.decompress(m.group(1))
            except zlib.error:
                pass
    compte = [int(x) for x in re.findall(rb"/Type\s*/Pages.*?/Count\s+(\d+)", d, re.S)]
    return (max(compte) if compte else None), len(re.findall(rb"/Type\s*/Page(?![a-zA-Z])", d))


def pagination(readme: str):
    octets = PDF.read_bytes()
    n, objets = pages(octets)
    m = re.search(r"\*\*Lire :\*\*.*?\((\d[\d\s]*) p\.\)", readme)
    publie = int(re.sub(r"\D", "", m.group(1))) if m else None
    createur = re.search(rb"/Creator\s*\(([^)]*)\)", octets)
    createur = createur.group(1).decode("latin-1") if createur else "?"
    verdict = n is not None and n == objets and n == publie
    if n is None or n != objets:
        fail.append(f"pagination — /Count {n} contre {objets} objets /Type/Page : arbre de pages incohérent")
    if publie is None:
        fail.append("pagination — forme « **Lire :** … (N p.) » introuvable au README")
    elif n != publie:
        fail.append(f"pagination — le README publie {publie} p., le PDF en compte {n}")
    return ok(1, "pagination", verdict, f"{n} pages, README {publie} ; /Creator {createur}")


# ----------------------------------------------------------------- [2] appariement

REGISTRE = """
ch. 1 | Bray, T.; Paoli, J.; Sperberg-McQueen, C. M.; Maler, E.; Yergeau, F. (Eds.) (2008). *Exten
ch. 1 | The Open Group (X/Open) (1991). *Distributed Transaction Processing: The XA Specification*
ch. 1 | Apache Kafka project (2025). *Apache Kafka 4.0.0 Release Announcement*, 18 mars 2025. http
ch. 1 | Gaia-X European Association for Data and Cloud AISBL (2025). *Gaia-X Architecture Document
ch. 1 | Cadence Workflow (Uber) (2026). *Cadence: Distributed, Scalable, Durable Orchestration Eng
ch. 1 | Connect RPC Authors (Buf, CNCF) (2025). *The Connect Protocol*. https://connectrpc.com/doc
ch. 1 | gRPC Authors (CNCF) (2025). *Core concepts, architecture and lifecycle*. https://grpc.io/d
ch. 1 | Richardson, C. (s.d.). *Pattern: Transactional outbox*. microservices.io. https://microser
ch. 1 | Stoplight (stoplightio) (2024). *Spectral: Open-Source API Description Linter*. https://gi
ch. 2 | Meta AI (Security team) (2025). *Agents Rule of Two: A Practical Approach to AI Agent Secu
ch. 2 | METR (Model Evaluation & Threat Research) (2025). *Recent Frontier Models Are Reward Hacki
ch. 2 | Anthropic (Appel, R.; Tamkin, A.; et al.) (2026). *The Anthropic Economic Index report: Ec
ch. 2 | OpenAI (Preparedness ; avec les auteurs de SWE-bench) (2024a). *Introducing SWE-bench Veri
ch. 3 | MCP maintainers (Anthropic, OpenAI, GitHub, Block, communauté) (2025). *MCP Specification
ch. 3 | MCP Core Maintainers (OpenAI, Anthropic) avec le UI Community Working Group (créateurs MCP
ch. 3 | OpenAI (puis Agentic AI Foundation / Linux Foundation) (2025). *AGENTS.md — format ouvert
ch. 3 | IETF (Kasselman, P., Defakto Security ; Lombardo, J., AWS ; Rosomakho, Y., Zscaler ; Campb
ch. 3 | Unit 42 (Palo Alto Networks) (2025). *New Prompt Injection Attack Vectors Through MCP Samp
ch. 4 | Board of Governors of the Federal Reserve System, OCC & FDIC (2011). *Supervisory Guidance
ch. 4 | Amazon Web Services (2025). *Multi-Agent Collaboration — Agentic AI Patterns and Workflows
ch. 4 | Amazon Web Services (2023). *Cedar — langage et moteur d'autorisation open source (Apache
ch. 4 | CData Software (2025). *Introducing CData MCP Servers: AI Access to Enterprise Data* (modè
ch. 4 | Credo AI (2025). *Credo AI — AI Governance Platform ; AI Agent Registry* (inventaire d'age
ch. 4 | CyberArk Software (2024). *Sécurité des identités machine (acquisition de Venafi)*. Finali
ch. 4 | Docker, Inc. (2025). *Docker MCP Catalog & Toolkit* (registre de serveurs MCP en images OC
ch. 4 | DreamFactory Software (2025). *How to Set Up an MCP Server for Legacy Databases* (Oracle,
ch. 4 | Google LLC (Kurian, T.) (2025). *Gemini at Work 2025: Introducing Gemini Enterprise*. blog
ch. 4 | LangChain (langchain-ai/agent-inbox) (2025). *Agent Inbox — An Inbox UX for Human-in-the-L
ch. 4 | mcp-gateway-registry (projet open source) (2025). *mcp-gateway-registry — passerelle et re
ch. 4 | Restate (restatedev) (2025). *Restate Documentation — Durable Agents* (journal durable ; i
ch. 4 | Futurum Group (Ashley, M.) (2026). *Futurum Agent Control Plane Framework: A Reference Mod
ch. 4 | JPMorgan Chase (couverture CNBC, Son, H.) (2025). *Here's JPMorgan Chase's Blueprint to Be
ch. 4 | Rubrik Zero Labs (enquête Wakefield Research, 1 625 décideurs) (2025). *The Identity Crisi
ch. 5 | Peng, X., Qian, L., Wang, Y., Xiang, R. et al. (2025). *MultiFinBen: Benchmarking Large La
ch. 5 | Yang, H., Liu, X.-Y. & Wang, C. D. (2023). *FinGPT: Open-Source Financial Large Language M
ch. 5 | CFPB (2022). *Consumer Financial Protection Circular 2022-03: Adverse Action Notification
ch. 5 | U.S. Department of the Treasury (2024). *Managing Artificial Intelligence-Specific Cyberse
ch. 5 | U.S. Department of the Treasury (2024). *Request for Information on Uses, Opportunities, a
ch. 5 | AMF (Québec) (2015). *Integrated Risk Management Guideline (gestion intégrée des risques).
ch. 5 | FCAC/ACFC — Parlement du Canada (2001). *Financial Consumer Agency of Canada Act (Loi sur
ch. 5 | FS-ISAC, AI Risk Working Group (2024). *Suite de 6 livres blancs sur l'IA (Adversarial AI
ch. 5 | Addepar (couv. WealthManagement.com) (2026). *Addepar Launches Addison AI for Natural Lang
ch. 5 | Commonwealth Bank of Australia / Anthropic (2025). *CommBank expands strategic partnership
ch. 5 | Morningstar, Inc. (2023). *Mo, an AI Chatbot Powered by Morningstar Intelligence Engine, D
ch. 5 | Temenos AG (2025). *Temenos Launches AI-Powered Money Movement & Management Platform at Si
ch. 5 | Thought Machine (couv. FinTech Futures) (2021). *Thought Machine wins major core banking d
ch. 5 | Tractable Ltd. (2026). *Tractable — AI for accident & disaster recovery (computer-vision d
ch. 5 | Zinnia (2026). *Zinnia Announces Collaboration with Snowflake to Deliver Real-Time Insuran
ch. 5 | Civil Resolution Tribunal of British Columbia (2024). *Moffatt v. Air Canada.* 2024 BCCRT
ch. 5 | Crisanto, J. C., Leuterio, C. B., Prenio, J. & Yong, J. / BIS–FSI (2024). *Regulating AI i
ch. 5 | Ministère des Finances Canada / Department of Finance Canada (2025). *Budget 2025: Canada'
ch. 5 | Shift Technology (2026). *Agentic AI is the future, and the future is now (insurance fraud
ch. 5 | Finastra (2026). *How Agentic AI Is Revolutionizing Retail Banking / Delivering the Autono
ch. 7 | W3C Verifiable Credentials Working Group (2026). *Verifiable Credentials Working Group Cha
ch. 7 | Commission européenne (DG CNECT) (2025). *The AI Continent Action Plan.* Communication COM
""".strip().splitlines()

NOTICE = re.compile(
    r"^(?:[^()]|\([^()]*\)){2,300}?\((?:[^()]*?[;,] ?)?((?:19|20)\d{2})[a-z]?(?:[-–/]\d{2,4})?"
    r"(?:\s*[;,][^()]*)?\)\s*[.:]"
    r"|^(?:[^()]|\([^()]*\)){2,300}?\(s\. ?d\.\)\s*\.")
# Sigles et termes trop fréquents pour désigner une notice à eux seuls.
COMMUNS = set("api apis llm llms mcp a2a http https json xml url uri iso iec ieee nist w3c ietf "
              "rfc oauth owasp aws ibm eu ue usa oecd ocde".split())


def plat(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def decouper(t: str):
    """(corps rédigé, {chapitre: texte de sa bibliographie})."""
    debut_bib = t.index("\n# Bibliographie générale")
    fin_bib = t.index("\n# Annexe A")
    corps = t[t.index("\n# Introduction"):debut_bib] + t[t.index("\n# Annexe B"):]
    morceaux = re.split(r"\n## Chapitre (\d) —", t[debut_bib:fin_bib])[1:]
    return corps, {morceaux[i]: morceaux[i + 1] for i in range(0, len(morceaux), 2)}


def notices(bib: str):
    """Les items de liste qui ont la forme d'une notice : auteur, puis « (année). »."""
    return [s for s in (it.replace("**", "") for it in re.findall(r"(?m)^[-*] (.+)$", bib)) if NOTICE.match(s)]


def citee(s: str, corps: str) -> bool:
    m = NOTICE.match(s)
    tete, an = s[:m.end()], m.group(1)
    auteur = re.split(r"\s*\((?:[^()]*?[;,] ?)?(?:(?:19|20)\d{2}|s\. ?d\.)", tete)[0]
    noms = {re.sub(r"^(?:(?:The|La|Le|Les)\s+|L')", "", re.split(r"[,;]| — | / | & | et ", auteur)[0].strip())}
    noms |= set(re.findall(r"\(([^()]{2,40})\)", auteur))  # sigle entre parenthèses : (OMG)
    if an:
        for nom in noms:
            pn = plat(nom)[:30].strip()
            if len(pn) >= 2 and any(an in corps[a.start():a.start() + 160]
                                    for a in re.finditer(r"\b" + re.escape(pn), corps)):
                return True
    ids = {"rfc " + x for x in re.findall(r"RFC\s*(\d{3,5})", s)}
    ids |= {x.lower().rstrip(".") for x in re.findall(r"\b10\.\d{4,9}/[^\s,;)]+", s)}
    ids |= set(re.findall(r"\b(\d{4}\.\d{4,5})(?:v\d)?\b", s))
    ids |= set(re.findall(r"\b((?:19|20)\d{2}/\d{2,5})\b", s))
    ids |= set(re.findall(r"\b(?:ISO|IEC)[/ A-Za-z]*?(\d{4,5}(?:-\d+)?)", s))
    if any(k.lower() in corps for k in ids):
        return True
    titre = re.search(r"\*([^*]{3,})\*", s)
    titre = titre.group(1) if titre else ""
    # la tête du titre, avant « — », « : », « ( » ou le point : cité en toutes lettres
    tete_titre = plat(re.split(r" — |: | \(|\. ", titre)[0]).strip(" .")
    if len(tete_titre) >= 12 and " " in tete_titre and tete_titre in corps:
        return True
    for w in re.findall(r"[A-Za-z0-9][\w\-.]*\w", titre):
        distinctif = (re.search(r"[a-z][A-Z]", w) or (re.search(r"\d", w) and re.search(r"[A-Za-z]", w))
                      or (re.fullmatch(r"[A-Z0-9\-]{3,}", w) and len(re.findall(r"[A-Z]", w)) >= 2))
        if distinctif and plat(w) not in COMMUNS and \
                re.search(r"(?<![\w-])" + re.escape(plat(w)) + r"(?![\w-])", corps):
            return True
    return False


def cle(chapitre: str, s: str) -> str:
    return f"ch. {chapitre} | {re.sub(r'\s+', ' ', s)[:90].rstrip()}"


def appariement(t: str):
    corps, bibs = decouper(t)
    corps = plat(corps)
    total = exemptees = 0
    non_appariees = []
    for ch in sorted(bibs):
        for s in notices(bibs[ch]):
            total += 1
            if "contexte non cit" in s:
                exemptees += 1
            elif not citee(s, corps):
                non_appariees.append(cle(ch, s))
    if "--registre" in sys.argv:
        print("\n".join(non_appariees))
    registre = set(REGISTRE)
    orphelines = [k for k in non_appariees if k not in registre]
    perimees = sorted(registre - set(non_appariees))
    for k in orphelines:
        fail.append(f"appariement — notice que le corps ne cite pas : {k}")
    for k in perimees:
        fail.append(f"appariement — registre périmé, notice appariée ou disparue : {k} — la retirer du REGISTRE")
    verdict = len(bibs) == 7 and not orphelines and not perimees
    if len(bibs) != 7:
        fail.append(f"appariement — {len(bibs)} bibliographies de chapitre au lieu de sept")
    return ok(2, "appariement", verdict,
              f"{len(bibs)} bibliographies, {total} notices : {total - exemptees - len(non_appariees)} retrouvées "
              f"au corps, {exemptees} « contexte non cité », {len(non_appariees)} au registre du "
              f"15 septembre 2026 ({len(REGISTRE)} inscrites)")


# ---------------------------------------------------------------------- [3] parité

# Les champs qui changent d'un rendu à l'autre de la même source — ceux de check-traite.py et
# de check-article.py, positions du xref comprises. Mesuré le 15 septembre 2026 : deux rendus
# du Vol. I par la même chaîne ne diffèrent que là.
VOLATILS = [
    (rb"/(Creation|Mod)Date\s*\([^)]*\)", rb"/\1Date()"),
    (rb"/ID\s*\[[^\]]*\]", rb"/ID[]"),
    (rb"<xmp:(ModifyDate|CreateDate|MetadataDate)>[^<]*</xmp:\1>", rb"<xmp:\1></xmp:\1>"),
    (rb"<xmpMM:InstanceID>[^<]*</xmpMM:InstanceID>", rb"<xmpMM:InstanceID></xmpMM:InstanceID>"),
    (rb"(?m)^\d{10} (\d{5} [nf])", rb"0000000000 \1"),
    (rb"startxref\s+\d+", rb"startxref"),
]


def sans_horodatage(octets: bytes) -> bytes:
    for motif, remplacement in VOLATILS:
        octets = re.sub(motif, remplacement, octets)
    return octets


def bash_posix():
    """Le bash qui lance build-pdf.sh — jamais `System32\\bash.exe`, le lanceur WSL."""
    b = shutil.which("bash")
    return None if b is None or "system32" in b.lower() else b


def parite():
    manque = [o for o in ("pandoc", "typst", "mmdc") if shutil.which(o) is None]
    bash = bash_posix()
    if manque or bash is None:
        print(f"  [3] parité      : chaîne incomplète ({', '.join(manque + ([] if bash else ['bash POSIX']))}) -> NON MESURÉ")
        print("      Le rendu versionné n'est donc PAS opposé à sa source. Il faut Pandoc, Typst, mermaid-cli")
        print("      et un Chromium, et les polices du poste d'auteur que le PDF embarque (Arial, Segoe UI Symbol…).")
        return True
    with tempfile.TemporaryDirectory(prefix="parite-vol1-") as tmp:
        essai = Path(tmp) / "essai.pdf"
        r = subprocess.run([bash, BUILD.as_posix()], cwd=RACINE, capture_output=True, text=True,
                           encoding="utf-8", errors="replace",
                           env=dict(os.environ, OUT_PDF=essai.as_posix(), PYTHONUTF8="1"))
        journal = (r.stdout or "") + (r.stderr or "")
        if "mode degrade" in journal:
            print("  [3] parité      : mermaid-cli n'a pas rendu tous les diagrammes (mode dégradé) -> NON MESURÉ")
            return True
        if r.returncode != 0 or not essai.exists():
            fail.append(f"parité — la chaîne ne compose plus la source : {journal.strip()[-300:]}")
            return ok(3, "parité", False, "rendu impossible")
        a, b = sans_horodatage(PDF.read_bytes()), sans_horodatage(essai.read_bytes())
    if a == b:
        return ok(3, "parité", True, f"{len(a)} octets hors horodatage, refait à l'identique")
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
    fail.append(f"parité — {PDF.name} n'est pas le rendu de {SRC.name} : première divergence à l'octet {i} "
                f"({len(a)} versionnés, {len(b)} refaits). Rendre avant de conclure — ou polices d'un autre poste")
    return ok(3, "parité", False, "le PDF versionné n'est pas celui que la source rend")


def main():
    for p in (SRC, PDF, README, BUILD):
        if not p.exists():
            print(f"introuvable : {p}")
            return 1
    print(f"Contrôle du Vol. I — {RACINE.name}")
    pagination(README.read_text(encoding="utf-8"))
    appariement(SRC.read_text(encoding="utf-8"))
    if "--sans-parite" in sys.argv:
        print("  [3] parité      : SAUTÉ sur demande (--sans-parite) -> NON MESURÉ")
    else:
        parite()
    if fail:
        print("\nECHEC :")
        for f in fail:
            print("  -", f)
        return 1
    print("\nTous les contrôles passent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
