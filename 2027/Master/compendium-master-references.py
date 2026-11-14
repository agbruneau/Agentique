"""Vérifie l'intégrité des références, URL et renvois du Compendium maître.

Modes :
    python Master/compendium-master-references.py
        Contrôle hors-ligne : 59 fichiers de Master/manuscrit/, syntaxe des URL,
        concordance [n] <-> ## Sources, interdiction de [n] dans les volets et
        l'ouverture, validité des renvois internes et liens locaux HTML, et
        couverture complète de Master/recherche/audit-references.json.

    python Master/compendium-master-references.py --en-ligne
        Exécute les contrôles hors-ligne puis vérifie en lot l'accessibilité
        HTTP (ThreadPoolExecutor, timeout 12 s) et les métadonnées via les API
        arXiv et Crossref/DOI.

Code de sortie : 0 si tous les contrôles passent, 1 sinon.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import socket
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
MANUSCRIT = os.path.join(ICI, "manuscrit")
FIGURES = os.path.join(MANUSCRIT, "figures")
AUDIT_JSON = os.path.join(ICI, "recherche", "audit-references.json")
HTML_FICHIERS = ("index.html", "Presentation.html")

USER_AGENT = "Compendium2027 RefAudit/1.0 (+https://example.org; contact@example.org)"
TIMEOUT_HTTP = 12
_VERROU_DICT = threading.Lock()
_VERROUS_HOTES: dict[str, threading.Semaphore] = {}


def _semaphore_hote(url: str) -> threading.Semaphore:
    """Limite la concurrence HTTP par nom d'hôte afin d'éviter les 429 en rafale."""
    hote = (urllib.parse.urlparse(url).hostname or "").lower()
    with _VERROU_DICT:
        sem = _VERROUS_HOTES.get(hote)
        if sem is None:
            sem = threading.Semaphore(2)
            _VERROUS_HOTES[hote] = sem
        return sem
MOTS_VIDES_TITRE = {
    "with", "from", "that", "this", "into", "your", "agent", "agents",
    "multi", "using", "system", "systems", "framework", "model", "models",
    "large", "language", "toward", "towards", "based", "beyond", "under",
}
DOMAINES_FICTIFS_EXACT = {
    "localhost", "127.0.0.1", "0.0.0.0", "example.com", "example.org", "example.net",
}
SUFFIXES_FICTIFS = (
    ".example", ".example.com", ".example.org", ".example.net", ".local",
    ".internal", ".localhost", ".boreal.ca", ".acier-laurentides.ca",
)
ANNEXES_ROMAINS_CONTEXTE = {"I", "II", "III", "IV", "V", "X"}
STATUTS_BLOQUANTS_AUDIT = {
    "mort_non_documente", "erreur_factuelle", "erreur_renvoi",
    "source_sans_url", "invalide", "casse", "non_corrige", "a_verifier",
}


class _SuiveurRedirection(urllib.request.HTTPRedirectHandler):
    """Enregistre les codes et cibles de redirection lors d'une requête urllib."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        historique = getattr(req, "_historique_redirections", None)
        if historique is None:
            historique = []
        abs_url = urllib.parse.urljoin(req.full_url, newurl)
        historique.append((code, abs_url))
        nouvelle = super().redirect_request(req, fp, code, msg, headers, newurl)
        if nouvelle is not None:
            nouvelle._historique_redirections = historique
        return nouvelle


def lister_fichiers_manuscrit() -> list[str]:
    """Retourne les 59 noms de fichiers Markdown attendus dans Master/manuscrit/."""
    tous = sorted(f for f in os.listdir(MANUSCRIT) if f.endswith(".md"))
    return tous


def lire_lignes(chemin: str) -> list[str]:
    """Lit un fichier UTF-8 et retourne ses lignes sans saut final."""
    with open(chemin, "r", encoding="utf-8") as fh:
        return fh.read().splitlines()


def est_url_fictive(url: str) -> bool:
    """Indique si une URL relève d'un exemple fictif documentaire."""
    hote = (urllib.parse.urlparse(url).hostname or "").lower()
    if not hote:
        return False
    if hote in DOMAINES_FICTIFS_EXACT or hote == "boreal.ca" or hote == "acier-laurentides.ca":
        return True
    if any(hote.endswith(suf) for suf in SUFFIXES_FICTIFS):
        return True
    if hote.startswith(("acme.", "contoso.", "mon-entreprise.", "my-agent.")):
        return True
    return False


def url_syntaxiquement_valide(url: str) -> bool:
    """Valide minimalement la syntaxe d'une URL http(s)://."""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return False
    hote = parsed.hostname
    if not hote or any(c.isspace() for c in url):
        return False
    if hote != "localhost" and "." not in hote:
        return False
    try:
        _ = parsed.port
    except ValueError:
        return False
    if any(c in hote for c in "<>{}[]\"'`\\"):
        return False
    return True


def nettoyer_url_extraite(brut: str) -> str:
    """Retire la ponctuation de phrase en fin d'URL sans casser les parenthèses appariées."""
    u = brut.rstrip(".,;:!?*»”’\\")
    while u.endswith(")") and u.count("(") < u.count(")"):
        u = u[:-1].rstrip(".,;:!?*»”’\\")
    return u


def decouper_sources_chapitre(lignes: list[str]) -> tuple[int | None, int | None]:
    """Retourne les indices (début inclus, fin exclue) de la section ## Sources."""
    debut = None
    for i, ligne in enumerate(lignes):
        if ligne.strip() == "## Sources":
            debut = i
            break
    if debut is None:
        return None, None
    fin = len(lignes)
    for j in range(debut + 1, len(lignes)):
        if re.match(r"^##\s+\S", lignes[j]):
            fin = j
            break
    return debut, fin


def extraire_blocs_manuscrit(fichiers: list[str]) -> dict:
    """Analyse les 59 fichiers pour en extraire cibles, appels, sources et URL."""
    cibles = {
        "chapitres": set(),
        "annexes": set(),
        "sections": set(),
        "extraits": set(),
        "adrs": set(),
        "figures": set(os.listdir(FIGURES)) if os.path.isdir(FIGURES) else set(),
    }
    sources_par_fichier: dict[str, dict[int, dict]] = {}
    appels_par_chapitre: dict[str, set[int]] = {}
    appels_interdits: list[tuple[str, int, str]] = []
    urls_hors_code: list[tuple[str, int, str, str]] = []
    urls_code_publiques: list[tuple[str, int, str]] = []
    urls_syntaxe_invalide: list[tuple[str, int, str]] = []

    for nom in fichiers:
        lignes = lire_lignes(os.path.join(MANUSCRIT, nom))
        m_ch = re.match(r"chapitre-(\d+)-", nom)
        m_an = re.match(r"annexe-([A-H])-", nom)
        est_chapitre = m_ch is not None
        if m_ch:
            cibles["chapitres"].add(int(m_ch.group(1)))
        if m_an:
            cibles["annexes"].add(m_an.group(1))

        deb_src, fin_src = decouper_sources_chapitre(lignes)
        if est_chapitre:
            sources_par_fichier[nom] = {}
            appels_par_chapitre[nom] = set()

        dans_code = False
        dans_volet = False
        for num_l, ligne in enumerate(lignes, 1):
            strip = ligne.strip()
            if strip.startswith("```") or strip.startswith("~~~"):
                dans_code = not dans_code
                continue
            if dans_code:
                for m_u in re.finditer(r"https?://[^\s<>\"'`\]]+", ligne):
                    u = nettoyer_url_extraite(m_u.group(0))
                    if url_syntaxiquement_valide(u) and not est_url_fictive(u):
                        urls_code_publiques.append((nom, num_l, u))
                continue

            if re.match(r"^##(?!#)\s+", strip):
                if "{.volet" in strip or "{ .volet" in strip:
                    dans_volet = True
                elif not (dans_volet and re.match(r"^##\s+\d+\.\d+\b", strip)):
                    dans_volet = False

            # Cibles internes
            m_sec = re.match(r"^#{2,4}\s+(\d+\.\d+|[A-H]\.\d+)\b", strip)
            if m_sec:
                cibles["sections"].add(m_sec.group(1))
            for m_ext in re.finditer(r"(?:^|\*\*|\s)Extrait\s+(\d+\.\d+)(?:\*\*|\s|:|—)", ligne):
                cibles["extraits"].add(m_ext.group(1))
            for m_adr in re.finditer(r"\bADR-(\d{3})\b", ligne):
                cibles["adrs"].add(f"ADR-{m_adr.group(1)}")

            # Extraction des URL hors code
            for m_u in re.finditer(r"https?://[^\s<>\"'`\]]+", ligne):
                u = nettoyer_url_extraite(m_u.group(0))
                if not url_syntaxiquement_valide(u):
                    urls_syntaxe_invalide.append((nom, num_l, u))
                elif not est_url_fictive(u):
                    urls_hors_code.append((nom, num_l, u, ligne))

            # Section ## Sources d'un chapitre
            en_sources = (deb_src is not None and deb_src < num_l - 1 < fin_src)
            if en_sources and est_chapitre:
                m_item = re.match(r"^\s*(\d+)\.\s+(.+)$", ligne)
                if m_item:
                    idx = int(m_item.group(1))
                    urls_ligne = [
                        nettoyer_url_extraite(x)
                        for x in re.findall(r"https?://[^\s<>\"'`\]]+", ligne)
                    ]
                    sources_par_fichier[nom][idx] = {
                        "ligne": num_l,
                        "texte": m_item.group(2),
                        "urls": urls_ligne,
                    }
                continue

            # Appels [n] hors ## Sources et hors code inline
            propre = re.sub(r"`[^`]+`", " ", ligne)
            for m_c in re.finditer(r"(?<!\w)\[(\d+)\](?!\()", propre):
                num_c = int(m_c.group(1))
                if dans_volet or nom == "ouverture.md":
                    appels_interdits.append((nom, num_l, m_c.group(0)))
                elif est_chapitre:
                    appels_par_chapitre[nom].add(num_c)

    return {
        "cibles": cibles,
        "sources": sources_par_fichier,
        "appels": appels_par_chapitre,
        "appels_interdits": appels_interdits,
        "urls_hors_code": urls_hors_code,
        "urls_code_publiques": urls_code_publiques,
        "urls_syntaxe_invalide": urls_syntaxe_invalide,
    }


def verifier_renvois_internes(fichiers: list[str], cibles: dict) -> list[str]:
    """Vérifie tous les renvois internes du manuscrit et les liens locaux HTML."""
    defauts: list[str] = []

    for nom in fichiers:
        lignes = lire_lignes(os.path.join(MANUSCRIT, nom))
        dans_code = False
        for num_l, ligne in enumerate(lignes, 1):
            strip = ligne.strip()
            if strip.startswith("```") or strip.startswith("~~~"):
                dans_code = not dans_code
                continue
            if dans_code:
                continue
            propre = re.sub(r"`[^`]+`", " ", ligne)

            for m in re.finditer(
                r"(?i)\b(?:chapitres?|ch\.)\s+(\d+(?:\s*(?:à|-|–|et|ou)\s*\d+|\s*,\s*\d+(?!\s+(?:partie|sources?|entrées?|URL|pages?|mots?|lignes?|%)))*)",
                propre,
            ):
                for n_s in re.findall(r"\d+", m.group(1)):
                    n = int(n_s)
                    if n not in cibles["chapitres"]:
                        defauts.append(f"{nom}:{num_l} -> renvoi chapitre inexistant : {n} ({m.group(0)})")

            for m in re.finditer(
                r"(?i)\bsections?\s+((?:\d+\.\d+|[A-H]\.\d+)(?:\s*(?:,|et|ou|à|-|–)\s*(?:\d+\.\d+|[A-H]\.\d+))*)(?![.\d])",
                propre,
            ):
                for sec in re.findall(r"\d+\.\d+|[A-H]\.\d+", m.group(1)):
                    if sec not in cibles["sections"]:
                        defauts.append(f"{nom}:{num_l} -> renvoi section inexistante : section {sec}")

            for m in re.finditer(r"\bExtrait\s+(\d+\.\d+)\b", propre):
                ext = m.group(1)
                if ext not in cibles["extraits"]:
                    defauts.append(f"{nom}:{num_l} -> renvoi extrait inexistant : Extrait {ext}")

            for m in re.finditer(r"\bADR-(\d+)\b", propre):
                code = f"ADR-{int(m.group(1)):03d}"
                if len(m.group(1)) != 3 or code not in cibles["adrs"]:
                    defauts.append(f"{nom}:{num_l} -> renvoi ADR inexistant : {m.group(0)}")

            for m in re.finditer(r"\b[Aa]nnexe\s+([A-Z])\b", propre):
                let = m.group(1)
                if let in ANNEXES_ROMAINS_CONTEXTE and m.group(0).startswith("annexe "):
                    continue
                if let not in cibles["annexes"]:
                    defauts.append(f"{nom}:{num_l} -> renvoi annexe inexistante : {m.group(0)}")

            for m in re.finditer(r"figures/([A-Za-z0-9_.\-]+\.svg)", propre):
                fig = m.group(1)
                if fig not in cibles["figures"]:
                    defauts.append(f"{nom}:{num_l} -> figure manquante : figures/{fig}")

    for html_nom in HTML_FICHIERS:
        chemin = os.path.join(RACINE, html_nom)
        if not os.path.exists(chemin):
            defauts.append(f"{html_nom} -> fichier HTML introuvable")
            continue
        contenu = open(chemin, "r", encoding="utf-8").read()
        for m in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', contenu):
            cible = m.group(1).strip()
            if re.match(r"^(?:https?:|mailto:|tel:|data:|javascript:|#)", cible, re.I):
                continue
            rel = cible.split("#", 1)[0].split("?", 1)[0]
            if rel and not os.path.exists(os.path.join(RACINE, rel)):
                defauts.append(f"{html_nom} -> lien local cassé : {cible}")

    return defauts


def verifier_audit_json(fichiers: list[str], donnees: dict) -> tuple[list[str], dict]:
    """Vérifie l'existence, la couverture et l'état de audit-references.json."""
    defauts: list[str] = []
    if not os.path.exists(AUDIT_JSON):
        return [f"Fichier absent : {AUDIT_JSON}"], {}

    try:
        with open(AUDIT_JSON, "r", encoding="utf-8") as fh:
            audit = json.load(fh)
    except Exception as exc:
        return [f"JSON invalide dans audit-references.json : {exc}"], {}

    for cle in ("metadata", "resume", "entrees"):
        if cle not in audit:
            defauts.append(f"Clé manquante dans audit-references.json : {cle}")
    if defauts:
        return defauts, audit

    entrees = audit.get("entrees", [])
    fichiers_audit = {e.get("fichier") for e in entrees if e.get("fichier")}
    attendus = set(fichiers)
    manquants = sorted(attendus - fichiers_audit)
    inconnus = sorted(fichiers_audit - attendus)
    if manquants:
        defauts.append(f"Fichiers absents d'audit-references.json : {', '.join(manquants)}")
    if inconnus:
        defauts.append(f"Fichiers inconnus dans audit-references.json : {', '.join(inconnus)}")

    paires_audit = {(e.get("fichier"), e.get("url")) for e in entrees if e.get("fichier") and e.get("url")}
    for nom, num_l, url, _ in donnees["urls_hors_code"]:
        if (nom, url) not in paires_audit:
            defauts.append(f"URL absente d'audit-references.json : {nom}:{num_l} {url}")
    for nom, num_l, url in donnees["urls_code_publiques"]:
        if (nom, url) not in paires_audit:
            defauts.append(f"URL bloc de code absente d'audit-references.json : {nom}:{num_l} {url}")

    ouvertes = audit.get("resume", {}).get("anomalies_bloquantes_ouvertes", -1)
    if ouvertes != 0:
        defauts.append(f"anomalies_bloquantes_ouvertes={ouvertes} (attendu 0)")

    for idx, e in enumerate(entrees):
        st = (e.get("statut_consolide") or "").lower()
        if st in STATUTS_BLOQUANTS_AUDIT:
            defauts.append(f"Entrée bloquante non résolue #{idx} ({e.get('fichier')}): {st}")

    return defauts, audit


def verifier_hors_ligne(fichiers: list[str]) -> tuple[list[str], dict, dict]:
    """Exécute tous les contrôles hors-ligne et affiche le résultat."""
    echecs: list[str] = []

    def rapport(nom: str, defauts: list[str], detail: str = "") -> None:
        if defauts:
            echecs.append(nom)
            print(f"[ECHEC] {nom} ({len(defauts)} défaut(s))")
            for d in defauts[:20]:
                print(f"  - {d}")
            if len(defauts) > 20:
                print(f"  ... et {len(defauts) - 20} autre(s)")
        else:
            suf = f" ({detail})" if detail else ""
            print(f"[OK] {nom}{suf}")

    defauts_inv = []
    if len(fichiers) != 59:
        defauts_inv.append(f"59 fichiers attendus dans Master/manuscrit/, trouvé {len(fichiers)}")
    rapport("Inventaire Master/manuscrit", defauts_inv, f"{len(fichiers)} fichiers")

    donnees = extraire_blocs_manuscrit(fichiers)

    defauts_url_src = [
        f"{nom}:{num_l} -> URL syntaxiquement invalide : {u}"
        for nom, num_l, u in donnees["urls_syntaxe_invalide"]
    ]
    total_sources = 0
    for nom, srcs in sorted(donnees["sources"].items()):
        attendus = list(range(1, len(srcs) + 1))
        if sorted(srcs) != attendus:
            defauts_url_src.append(f"{nom} -> numérotation ## Sources discontinue : {sorted(srcs)}")
        for idx, info in srcs.items():
            total_sources += 1
            if not info["urls"]:
                defauts_url_src.append(f"{nom}:{info['ligne']} -> source [{idx}] sans URL http(s)")
    rapport(
        "Sources numérotées et syntaxe des URL",
        defauts_url_src,
        f"{total_sources} sources de chapitres, {len(donnees['urls_hors_code'])} occurrences URL hors code",
    )

    defauts_conc: list[str] = []
    for nom, srcs in sorted(donnees["sources"].items()):
        appels = donnees["appels"].get(nom, set())
        cles_src = set(srcs.keys())
        sans_source = sorted(appels - cles_src)
        orphelines = sorted(cles_src - appels)
        if sans_source:
            defauts_conc.append(f"{nom} -> appels [n] sans entrée ## Sources : {sans_source}")
        if orphelines:
            defauts_conc.append(f"{nom} -> sources non citées dans le texte : {orphelines}")
    for nom, num_l, appel in donnees["appels_interdits"]:
        defauts_conc.append(f"{nom}:{num_l} -> appel interdit dans volet ou ouverture : {appel}")
    rapport("Concordance [n] <-> ## Sources et volets/ouverture", defauts_conc, "50 chapitres + volets + ouverture")

    defauts_renvois = verifier_renvois_internes(fichiers, donnees["cibles"])
    rapport(
        "Renvois internes et liens locaux HTML",
        defauts_renvois,
        f"{len(donnees['cibles']['sections'])} sections, {len(donnees['cibles']['extraits'])} extraits, {len(donnees['cibles']['adrs'])} ADR",
    )

    defauts_audit, audit = verifier_audit_json(fichiers, donnees)
    rapport(
        "Audit consolidé audit-references.json",
        defauts_audit,
        f"{len(audit.get('entrees', []))} entrées" if audit else "",
    )

    return echecs, donnees, audit


def _normaliser_sans_trivialite(url: str) -> str:
    """Normalise www., slash final, suffixe .html et fragment pour distinguer les redirections réelles."""
    p = urllib.parse.urlparse(url.strip())
    hote = (p.hostname or "").lower()
    if hote.startswith("www."):
        hote = hote[4:]
    chemin = p.path or "/"
    if chemin != "/" and chemin.endswith("/"):
        chemin = chemin[:-1]
    if chemin.endswith(".html"):
        chemin = chemin[:-5]
    return urllib.parse.urlunparse((p.scheme.lower(), hote, chemin, p.params, p.query, ""))


def _tester_url_http(url: str) -> dict:
    """Effectue une requête HTTP GET avec suivi des redirections et retry sur 429/503."""
    opener = urllib.request.build_opener(_SuiveurRedirection())
    sem = _semaphore_hote(url)
    for tentative in range(2):
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            },
        )
        req._historique_redirections = []
        try:
            with sem, opener.open(req, timeout=TIMEOUT_HTTP) as resp:
                historique = getattr(req, "_historique_redirections", [])
                corps = resp.read(2048).decode("utf-8", errors="ignore")
                final_url = resp.geturl()
                est_todayoj = (
                    "eur-lex.europa.eu" in url
                    and ("TodayOJ" in final_url or "awsWaf" in corps or len(corps.strip()) == 0)
                )
                return {
                    "url": url,
                    "statut": resp.status,
                    "url_finale": final_url,
                    "historique": historique,
                    "todayoj": est_todayoj,
                    "erreur": None,
                }
        except urllib.error.HTTPError as exc:
            historique = getattr(req, "_historique_redirections", [])
            if exc.code in (429, 503) and tentative == 0:
                time.sleep(2.5)
                continue
            return {
                "url": url,
                "statut": exc.code,
                "url_finale": exc.geturl() or url,
                "historique": historique,
                "todayoj": False,
                "erreur": str(exc),
            }
        except Exception as exc:
            return {
                "url": url,
                "statut": 0,
                "url_finale": url,
                "historique": [],
                "todayoj": False,
                "erreur": repr(exc),
            }
    return {"url": url, "statut": 429, "url_finale": url, "historique": [], "todayoj": False, "erreur": "HTTP 429"}


def _normaliser_texte(texte: str) -> str:
    """Supprime accents et casse pour comparer titres/noms d'auteurs."""
    decomposed = unicodedata.normalize("NFKD", texte)
    return "".join(c for c in decomposed if not unicodedata.combining(c)).lower()


def _verifier_arxiv_lot(occ_urls: list[tuple[str, int, str, str]]) -> tuple[list[str], list[str], int]:
    """Vérifie tous les IDs arXiv via l'API officielle export.arxiv.org."""
    par_id: dict[str, list[tuple[str, int, str]]] = {}
    for nom, num_l, url, ligne in occ_urls:
        m = re.search(r"https?://(?:export\.)?arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
        if m:
            par_id.setdefault(m.group(1), []).append((nom, num_l, ligne))

    if not par_id:
        return [], [], 0

    ids = sorted(par_id)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    meta: dict[str, dict] = {}
    erreurs: list[str] = []
    for i in range(0, len(ids), 50):
        lot = ",".join(ids[i:i + 50])
        api_url = f"https://export.arxiv.org/api/query?id_list={lot}&max_results=100"
        try:
            req = urllib.request.Request(api_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                racine = ET.fromstring(resp.read())
            for entree in racine.findall("atom:entry", ns):
                id_txt = entree.findtext("atom:id", "", ns)
                m = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?$", id_txt)
                if not m:
                    continue
                titre = re.sub(r"\s+", " ", entree.findtext("atom:title", "", ns)).strip()
                auteurs = [a.findtext("atom:name", "", ns).strip() for a in entree.findall("atom:author", ns)]
                meta[m.group(1)] = {"titre": titre, "auteurs": auteurs}
        except Exception as exc:
            erreurs.append(f"Erreur API arXiv (lot {i // 50 + 1}) : {exc}")

    manquants = sorted(set(ids) - set(meta))
    for aid in manquants:
        erreurs.append(f"Identifiant arXiv introuvable via API : {aid} @ {par_id[aid][0][:2]}")

    derives: list[str] = []
    for aid, refs in sorted(par_id.items()):
        info = meta.get(aid)
        if not info or not info["titre"]:
            continue
        titre_norm = _normaliser_texte(info["titre"])
        mots_titre = [
            w for w in re.findall(r"[a-z0-9]{4,}", titre_norm)
            if w not in MOTS_VIDES_TITRE
        ][:6]
        if len(mots_titre) < 2:
            mots_titre = re.findall(r"[a-z0-9]{2,}", titre_norm)[:6]
        noms_auteurs = [
            _normaliser_texte(a.split()[-1])
            for a in info["auteurs"][:3]
            if a.split()
        ]
        for nom, num_l, ligne in refs:
            if "non lues" in ligne.lower() or re.search(rf"\[arXiv\s+{re.escape(aid)}(?:v\d+)?\]\(", ligne):
                continue
            norm_ligne = _normaliser_texte(ligne)
            chevauchement = sum(1 for w in mots_titre if w in norm_ligne)
            auteur_ok = any(
                len(na) >= 2 and re.search(rf"\b{re.escape(na)}\b", norm_ligne)
                for na in noms_auteurs
            )
            if chevauchement == 0 and not auteur_ok:
                derives.append(
                    f"arXiv {aid} ({nom}:{num_l}) : auteur/titre distant de '{info['auteurs'][0] if info['auteurs'] else '?'} — {info['titre'][:60]}'"
                )
    return erreurs, derives, len(ids)


def _interroger_un_doi(doi: str) -> dict:
    """Interroge doi.org/api/handles et Crossref avec repli modéré sur 429."""
    handle_ok = False
    handle_statut = 0
    hurl = "https://doi.org/api/handles/" + urllib.parse.quote(doi, safe="/")
    try:
        with urllib.request.urlopen(urllib.request.Request(hurl, headers={"User-Agent": USER_AGENT}), timeout=TIMEOUT_HTTP) as r:
            d = json.loads(r.read().decode("utf-8"))
            handle_ok = d.get("responseCode") == 1
            handle_statut = 200 if handle_ok else 404
    except urllib.error.HTTPError as exc:
        handle_statut = exc.code
    except Exception:
        handle_statut = 0

    curl = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    cr_statut = 0
    titre = ""
    auteurs: list[str] = []
    for tentative in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(curl, headers={"User-Agent": USER_AGENT}), timeout=TIMEOUT_HTTP) as r:
                msg = json.loads(r.read().decode("utf-8"))["message"]
                cr_statut = 200
                titre = (msg.get("title") or [""])[0]
                auteurs = [x.get("family", "") for x in (msg.get("author") or [])[:3]]
                break
        except urllib.error.HTTPError as exc:
            cr_statut = exc.code
            if exc.code == 429 and tentative == 0:
                time.sleep(0.8)
                continue
            break
        except Exception:
            cr_statut = 0
            break

    return {
        "doi": doi,
        "handle_ok": handle_ok,
        "handle_statut": handle_statut,
        "crossref_statut": cr_statut,
        "titre": titre,
        "auteurs": auteurs,
    }


def _verifier_doi_lot(occ_urls: list[tuple[str, int, str, str]]) -> tuple[list[str], list[str], dict[str, dict]]:
    """Vérifie tous les DOI via doi.org/api/handles et Crossref."""
    par_doi: dict[str, list[tuple[str, int, str]]] = {}
    for nom, num_l, url, ligne in occ_urls:
        m = re.search(r"https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/[^\s<>\"'`\]]+)", url)
        if m:
            doi = nettoyer_url_extraite(m.group(1))
            par_doi.setdefault(doi, []).append((nom, num_l, ligne))

    if not par_doi:
        return [], [], {}

    resultats: dict[str, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for res in pool.map(_interroger_un_doi, sorted(par_doi)):
            resultats[res["doi"]] = res

    erreurs: list[str] = []
    derives: list[str] = []
    for doi, res in sorted(resultats.items()):
        if not res["handle_ok"] and res["crossref_statut"] != 200:
            erreurs.append(
                f"DOI introuvable ({doi}) : handle={res['handle_statut']}, crossref={res['crossref_statut']} @ {par_doi[doi][0][:2]}"
            )
            continue
        if res["crossref_statut"] == 200 and res["titre"]:
            titre_norm = _normaliser_texte(res["titre"])
            mots = [
                w for w in re.findall(r"[a-z0-9]{4,}", titre_norm)
                if w not in MOTS_VIDES_TITRE
            ][:6]
            if len(mots) < 2:
                mots = re.findall(r"[a-z0-9]{2,}", titre_norm)[:6]
            noms_auteurs = [_normaliser_texte(a) for a in res["auteurs"][:3] if a]
            for nom, num_l, ligne in par_doi[doi]:
                norm_l = _normaliser_texte(ligne)
                ov = sum(1 for w in mots if w in norm_l)
                auteur_ok = any(
                    len(na) >= 2 and re.search(rf"\b{re.escape(na)}\b", norm_l)
                    for na in noms_auteurs
                )
                if ov == 0 and not auteur_ok:
                    derives.append(
                        f"DOI {doi} ({nom}:{num_l}) : métadonnée Crossref '{res['auteurs'][:1]} — {res['titre'][:60]}' sans recouvrement"
                    )
    return erreurs, derives, resultats


def verifier_en_ligne(donnees: dict, audit: dict) -> list[str]:
    """Vérifie en lot les URL publiques, redirections permanentes, arXiv et Crossref."""
    echecs: list[str] = []
    occ = donnees["urls_hors_code"]
    par_url: dict[str, list[tuple[str, int]]] = {}
    for nom, num_l, url, _ in occ:
        par_url.setdefault(url, []).append((nom, num_l))

    statuts_audit: dict[str, set[str]] = {}
    for e in audit.get("entrees", []):
        u = e.get("url")
        if u:
            statuts_audit.setdefault(u, set()).add(e.get("statut_consolide") or "")

    print(f"\n[EN LIGNE] Test HTTP en lot de {len(par_url)} URL distinctes (timeout={TIMEOUT_HTTP}s)...")
    http_res: dict[str, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        for res in pool.map(_tester_url_http, sorted(par_url)):
            http_res[res["url"]] = res

    err_doi, der_doi, res_doi = _verifier_doi_lot(occ)
    err_arx, der_arx, nb_arx = _verifier_arxiv_lot(occ)

    morts_nouveaux: list[str] = []
    morts_documentes: list[str] = []
    erreurs_5xx: list[str] = []
    restreints_documentes: list[str] = []
    restreints_nouveaux: list[str] = []
    redir_nouvelles: list[str] = []
    redir_connues = 0

    for url, res in sorted(http_res.items()):
        st = res["statut"]
        audit_st = statuts_audit.get(url, set())
        est_restreint_audit = bool(audit_st & {"acces_restreint", "corrige_acces_restreint", "mort_documente"})
        m_doi = re.search(r"https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/[^\s<>\"'`\]]+)", url)
        doi_valide = False
        if m_doi:
            d = nettoyer_url_extraite(m_doi.group(1))
            doi_valide = res_doi.get(d, {}).get("handle_ok", False)

        # Classification HTTP
        if st in (404, 410) or (st == 0 and not _est_timeout(res["erreur"])):
            if "mort_documente" in audit_st:
                morts_documentes.append(f"{url} ({st}) @ {par_url[url]}")
            elif doi_valide and ("acces_restreint" in audit_st or "SSLError" in (res["erreur"] or "")):
                restreints_documentes.append(f"{url} (DOI OK, TLS/cible éditeur restreinte : {res['erreur']})")
            else:
                morts_nouveaux.append(f"{url} -> {st} {res['erreur']} @ {par_url[url]}")
            continue

        if st >= 500:
            if est_restreint_audit:
                restreints_documentes.append(f"{url} (HTTP {st}, déjà documenté)")
            else:
                erreurs_5xx.append(f"{url} -> HTTP {st} @ {par_url[url]}")
            continue

        if st in (403, 429, 202) or (st == 0 and _est_timeout(res["erreur"])) or res["todayoj"]:
            raison = "TodayOJ" if res["todayoj"] else f"HTTP {st}" if st else "timeout"
            if est_restreint_audit or doi_valide:
                restreints_documentes.append(f"{url} ({raison})")
            else:
                restreints_nouveaux.append(f"{url} -> {raison} (audit={sorted(audit_st)}) @ {par_url[url]}")
            continue

        # Redirections permanentes non triviales (301/308)
        codes_perm = [c for c, _ in res["historique"] if c in (301, 308)]
        if codes_perm and not m_doi:
            m_arx_o = re.match(r"^https?://(?:www\.)?arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?/?$", url)
            m_arx_f = re.match(r"^https?://(?:www\.)?arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?/?$", res["url_finale"])
            if m_arx_o and m_arx_f and m_arx_o.groups() == m_arx_f.groups():
                continue
            if _normaliser_sans_trivialite(url) != _normaliser_sans_trivialite(res["url_finale"]):
                if "valide_redirection" in audit_st:
                    redir_connues += 1
                else:
                    redir_nouvelles.append(
                        f"{url} -> {res['url_finale']} ({codes_perm}) @ {par_url[url]}"
                    )

    if morts_nouveaux:
        echecs.append("Nouveaux liens morts (HTTP)")
        print(f"[ECHEC] Nouveaux liens morts ({len(morts_nouveaux)})")
        for x in morts_nouveaux:
            print(f"  - {x}")
    else:
        print(f"[OK] Aucun nouveau lien mort ({len(morts_documentes)} mort documenté reconnu)")

    if erreurs_5xx:
        echecs.append("Erreurs serveur HTTP 5xx")
        print(f"[ECHEC] Erreurs serveur HTTP 5xx ({len(erreurs_5xx)})")
        for x in erreurs_5xx:
            print(f"  - {x}")
    else:
        print("[OK] Aucune erreur serveur HTTP 5xx non documentée")

    if redir_nouvelles:
        echecs.append("Redirections permanentes non mises à jour")
        print(f"[ECHEC] Nouvelles redirections permanentes ({len(redir_nouvelles)})")
        for x in redir_nouvelles:
            print(f"  - {x}")
    else:
        print(f"[OK] Redirections permanentes ({redir_connues} déjà documentées comme valide_redirection)")

    derives = err_arx + der_arx + err_doi + der_doi
    if derives:
        echecs.append("Dérive ou erreur arXiv/Crossref")
        print(f"[ECHEC] API arXiv / Crossref-DOI ({len(derives)} anomalie(s))")
        for x in derives:
            print(f"  - {x}")
    else:
        print(f"[OK] API arXiv ({nb_arx} ID) et Crossref/DOI ({len(res_doi)} DOI)")

    if restreints_nouveaux:
        print(f"[AVERT] Nouveaux accès restreints / anti-bot non documentés dans l'audit ({len(restreints_nouveaux)})")
        for x in restreints_nouveaux:
            print(f"  - {x}")
    print(f"[INFO] Accès restreints / anti-bot / TLS éditeur documentés ou DOI vivants : {len(restreints_documentes)}")
    return echecs


def _est_timeout(erreur: str | None) -> bool:
    """Détecte si une erreur réseau vient d'un délai dépassé."""
    if not erreur:
        return False
    bas = erreur.lower()
    return isinstance(erreur, socket.timeout) or "timed out" in bas or "timeout" in bas


def main() -> int:
    """Point d'entrée CLI."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Contrôle des références du Compendium 2027.")
    parser.add_argument(
        "--en-ligne",
        action="store_true",
        help="Réexécute aussi les vérifications HTTP, arXiv et Crossref sur les URL publiques.",
    )
    args = parser.parse_args()

    fichiers = lister_fichiers_manuscrit()
    echecs, donnees, audit = verifier_hors_ligne(fichiers)

    if args.en_ligne:
        if audit:
            echecs.extend(verifier_en_ligne(donnees, audit))
        else:
            echecs.append("Contrôle en ligne impossible sans audit-references.json")

    if echecs:
        print(f"\nÉCHEC : {len(echecs)} contrôle(s) en erreur ({', '.join(echecs)}).")
        return 1

    print("\nTous les contrôles de références passent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
