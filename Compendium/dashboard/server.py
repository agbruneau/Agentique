#!/usr/bin/env python3
"""Serveur HTTP local publiant le dashboard web de progression du Compendium.

Utilisation :
    python -B Compendium/dashboard/server.py --host 127.0.0.1 --port 8765
    python -B Compendium/dashboard/server.py --port 8765 --open
    python -B Compendium/dashboard/server.py --export-json rapport.json
"""

from __future__ import annotations

import argparse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sys
from typing import Any
from urllib.parse import urlparse
import webbrowser

DASHBOARD_DIR = Path(__file__).resolve().parent
DEFAULT_REPO_ROOT = DASHBOARD_DIR.parents[1]

if str(DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(DASHBOARD_DIR))

import parser_plan as pp  # noqa: E402


class CompendiumDashboardServer(ThreadingHTTPServer):
    """Serveur HTTP multi-fil dédié au suivi de progression de ``Compendium/plan.md``."""

    allow_reuse_address = True

    def __init__(
        self,
        server_address: tuple[str, int],
        repo_root: Path,
        plan_path: Path | None = None,
        index_html_path: Path | None = None,
    ) -> None:
        self.repo_root = repo_root.resolve()
        self.plan_path = plan_path.resolve() if plan_path else (self.repo_root / "Compendium" / "plan.md")
        self.index_html_path = (index_html_path or (DASHBOARD_DIR / "index.html")).resolve()
        super().__init__(server_address, DashboardRequestHandler)


class DashboardRequestHandler(BaseHTTPRequestHandler):
    """Gestionnaire HTTP JSON + HTML sans dépendance externe."""

    server: CompendiumDashboardServer

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
        sys.stderr.write(f"[compendium-dashboard] {self.address_string()} - {format % args}\n")

    def _send_bytes(
        self,
        status: int,
        body: bytes,
        content_type: str,
        extra_headers: dict[str, str] | None = None,
    ) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        if extra_headers:
            for k, v in extra_headers.items():
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: int, data: Any) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self._send_bytes(status, body, "application/json; charset=utf-8")

    def do_GET(self) -> None:  # noqa: N802
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path in ("/", "/index.html"):
            if not self.server.index_html_path.is_file():
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "index.html introuvable"})
                return
            html_bytes = self.server.index_html_path.read_bytes()
            self._send_bytes(HTTPStatus.OK, html_bytes, "text/html; charset=utf-8")
            return

        if path == "/api/health":
            self._send_json(
                HTTPStatus.OK,
                {
                    "status": "ok",
                    "host": self.server.server_address[0],
                    "port": self.server.server_address[1],
                    "plan_path": str(self.server.plan_path),
                    "plan_exists": self.server.plan_path.is_file(),
                },
            )
            return

        if path == "/api/dashboard":
            if not self.server.plan_path.is_file():
                self._send_json(HTTPStatus.NOT_FOUND, {"error": f"plan.md introuvable : {self.server.plan_path}"})
                return
            try:
                payload = pp.build_dashboard_payload(self.server.repo_root, self.server.plan_path)
                self._send_json(HTTPStatus.OK, payload)
            except Exception as exc:
                self._send_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})
            return

        if path == "/api/export/csv":
            try:
                payload = pp.build_dashboard_payload(self.server.repo_root, self.server.plan_path)
                csv_bytes = pp.export_units_csv(payload).encode("utf-8")
                self._send_bytes(
                    HTTPStatus.OK,
                    csv_bytes,
                    "text/csv; charset=utf-8",
                    {"Content-Disposition": 'attachment; filename="compendium-progression.csv"'},
                )
            except Exception as exc:
                self._send_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})
            return

        if path == "/api/plan-raw":
            if not self.server.plan_path.is_file():
                self._send_json(HTTPStatus.NOT_FOUND, {"error": "plan.md introuvable"})
                return
            self._send_bytes(HTTPStatus.OK, self.server.plan_path.read_bytes(), "text/plain; charset=utf-8")
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": f"Route inconnue : {path}"})

    def do_POST(self) -> None:  # noqa: N802
        parsed_url = urlparse(self.path)
        if parsed_url.path != "/api/steps/toggle":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": f"Route POST inconnue : {parsed_url.path}"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Content-Length invalide"})
            return

        if length <= 0 or length > 4096:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Taille de requête invalide (1..4096 octets)"})
            return

        try:
            body = json.loads(self.rfile.read(length).decode("utf-8"))
        except Exception:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Corps JSON invalide"})
            return

        if not isinstance(body, dict) or "line_no" not in body or "checked" not in body:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Champs requis : line_no (int) et checked (bool)"})
            return

        line_no = body["line_no"]
        checked = body["checked"]
        if type(line_no) is not int or type(checked) is not bool:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Types invalides : line_no=int et checked=bool requis"})
            return

        try:
            step_res = pp.toggle_plan_step(self.server.plan_path, line_no, checked)
            payload = pp.build_dashboard_payload(self.server.repo_root, self.server.plan_path)
            self._send_json(HTTPStatus.OK, {"ok": True, "step": step_res, "dashboard": payload})
        except ValueError as exc:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
        except Exception as exc:
            self._send_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})


def create_server(
    repo_root: Path = DEFAULT_REPO_ROOT,
    host: str = "127.0.0.1",
    port: int = 8765,
    plan_path: Path | None = None,
) -> CompendiumDashboardServer:
    """Instancie le serveur HTTP prêt à écouter."""
    return CompendiumDashboardServer((host, port), repo_root=repo_root, plan_path=plan_path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dashboard web local de progression du Compendium (plan.md).")
    parser.add_argument("--host", default="127.0.0.1", help="Adresse d'écoute locale (défaut : 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8765, help="Port TCP local (défaut : 8765)")
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT, help="Racine du dépôt Agentique")
    parser.add_argument("--plan", type=Path, default=None, help="Chemin vers plan.md (défaut : Compendium/plan.md)")
    parser.add_argument("--open", action="store_true", help="Ouvrir le navigateur par défaut au démarrage")
    parser.add_argument("--export-json", type=Path, default=None, help="Exporter le snapshot JSON puis quitter")
    args = parser.parse_args(argv)

    if args.export_json is not None:
        payload = pp.build_dashboard_payload(args.repo_root, args.plan)
        args.export_json.parent.mkdir(parents=True, exist_ok=True)
        args.export_json.write_bytes((json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        print(f"Snapshot exporté : {args.export_json}")
        return 0

    srv = create_server(repo_root=args.repo_root, host=args.host, port=args.port, plan_path=args.plan)
    url = f"http://{srv.server_address[0]}:{srv.server_address[1]}"
    print(f"Dashboard Compendium actif sur {url}", flush=True)
    print(f"Source plan.md : {srv.plan_path}", flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur local.", flush=True)
    finally:
        srv.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
