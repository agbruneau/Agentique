# SPDX-License-Identifier: MIT
"""Validation declarative des manifestes de confinement sans KVM."""

from __future__ import annotations

import ipaddress
from typing import Any
from urllib.parse import urlparse

from jsonschema import Draft202012Validator

IMDS_IPV4: str = "169.254.169.254"

IANA_SPECIAL_CIDRS: tuple[str, ...] = (
    "127.0.0.0/8",
    "10.0.0.0/8",
    "100.64.0.0/10",
    "169.254.0.0/16",
    "172.16.0.0/12",
    "192.168.0.0/16",
    "::1/128",
    "fc00::/7",
    "fe80::/10",
    "::ffff:0:0/96",
    "64:ff9b::/96",
)

_IANA_NETWORKS = tuple(
    ipaddress.ip_network(cidr) for cidr in IANA_SPECIAL_CIDRS
)
_EXTRA_BLOCKED_V4 = ipaddress.ip_network("0.0.0.0/8")
_EXTRA_BLOCKED_V6 = ipaddress.ip_network("::/128")
_IMDS_ADDR = ipaddress.ip_address(IMDS_IPV4)
_BANNED_HOSTS = frozenset(
    {"localhost", "ip6-localhost", "metadata.google.internal"}
)


def _extract_host(entry: str) -> str:
    val = entry.strip()
    if "://" in val:
        parsed = urlparse(val)
        val = parsed.hostname or val
    elif val.startswith("[") and "]" in val:
        val = val[1 : val.index("]")]
    elif val.count(":") == 1:
        val = val.split(":", 1)[0]
    return val.rstrip(".").lower()


def _check_allowlist_entry(entry: str) -> str | None:
    if "*" in entry:
        return f"Joker '*' interdit dans network.allowlist : {entry!r}"
    host = _extract_host(entry)
    if not host or host in _BANNED_HOSTS:
        return f"Hote interne interdit dans network.allowlist : {entry!r}"
    try:
        net = ipaddress.ip_network(host, strict=False)
    except ValueError:
        return None
    if net.version == 4 and _IMDS_ADDR in net:
        return f"IMDS {IMDS_IPV4} interdit dans network.allowlist : {entry}"
    if net.version == 4 and net.overlaps(_EXTRA_BLOCKED_V4):
        return f"Plage reseau 0.0.0.0/8 interdite pour {entry!r}"
    if net.version == 6 and net.overlaps(_EXTRA_BLOCKED_V6):
        return f"Adresse ::/128 interdite pour {entry!r}"
    for special in _IANA_NETWORKS:
        if net.version == special.version and net.overlaps(special):
            return (
                f"Plage IANA speciale interdite ({special}) "
                f"pour {entry!r}"
            )
        if net.version == 6 and isinstance(
            net.network_address, ipaddress.IPv6Address
        ):
            mapped = net.network_address.ipv4_mapped
            if mapped is not None and special.version == 4 and mapped in special:
                return (
                    f"Adresse IPv4 mappee interdite ({special}) "
                    f"pour {entry!r}"
                )
    return None


def _check_blocked_cidrs(blocked_raw: Any, errs: list[str]) -> None:
    if not isinstance(blocked_raw, list):
        return
    parsed_v4: list[ipaddress.IPv4Network] = []
    parsed_v6: list[ipaddress.IPv6Network] = []
    for raw in blocked_raw:
        if not isinstance(raw, str):
            continue
        try:
            net = ipaddress.ip_network(raw.strip(), strict=False)
        except ValueError:
            errs.append(f"CIDR bloque invalide dans blocked_cidrs : {raw!r}")
            continue
        if isinstance(net, ipaddress.IPv4Network):
            parsed_v4.append(net)
        else:
            parsed_v6.append(net)
    for special in _IANA_NETWORKS:
        pool = (
            parsed_v4
            if isinstance(special, ipaddress.IPv4Network)
            else parsed_v6
        )
        if not any(special.subnet_of(b) for b in pool):  # type: ignore[arg-type]
            errs.append(
                f"Plage IANA obligatoire absente de blocked_cidrs : {special}"
            )


def validate_sandbox_manifest(
    manifest: dict[str, Any], schema: dict[str, Any]
) -> list[str]:
    """Valide schema, blocage IMDS + 11 plages IANA, env_secrets == [],
    read_only_root == True, allow_shell == False et delais <= 30/1200/3600."""
    errs = [
        e.message
        for e in sorted(
            Draft202012Validator(schema).iter_errors(manifest),
            key=lambda x: tuple(str(p) for p in x.path),
        )
    ]
    net = manifest.get("network") if isinstance(manifest, dict) else None
    if isinstance(net, dict):
        if net.get("imds_blocked") is not True:
            errs.append("network.imds_blocked doit etre True")
        if net.get("special_iana_blocked") is not True:
            errs.append("network.special_iana_blocked doit etre True")
        _check_blocked_cidrs(net.get("blocked_cidrs"), errs)
        mode = net.get("mode")
        allowlist = net.get("allowlist")
        if isinstance(allowlist, list):
            if mode == "none" and allowlist:
                errs.append(
                    "network.allowlist doit etre vide en mode 'none'"
                )
            for item in allowlist:
                if not isinstance(item, str) or not item.strip():
                    errs.append(f"Entree allowlist invalide : {item!r}")
                    continue
                msg = _check_allowlist_entry(item.strip())
                if msg:
                    errs.append(msg)
    return errs
