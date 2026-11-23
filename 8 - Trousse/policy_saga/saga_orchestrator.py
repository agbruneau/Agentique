# SPDX-License-Identifier: MIT
"""Orchestrateur Saga durable : idem-v1, Outbox, pivot et EXIG-ORC-28."""

from __future__ import annotations

from collections.abc import Callable, Sequence
import copy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import StrEnum
import json
from pathlib import Path
import sqlite3
import threading
import time
from typing import Any

from harness_proto.jcs import jcs_sha256_hex


class SagaStatus(StrEnum):
    """Etats durables d'une execution Saga."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    PIVOT_REACHED = "PIVOT_REACHED"
    COMPENSATING = "COMPENSATING"
    COMPLETED = "COMPLETED"
    COMPENSATED = "COMPENSATED"
    HUMAN_ESCALATION = "HUMAN_ESCALATION"


class IdempotencyConflictError(Exception):
    """Erreur HTTP 409 (en cours) ou HTTP 422 (cle reutilisee autre charge)."""

    def __init__(self, http_status: int, detail: str) -> None:
        super().__init__(detail)
        self.http_status = http_status
        self.detail = detail


class SimulatedCrashError(RuntimeError):
    """Plantage determine simule pour tests de reprise Outbox/Saga."""


@dataclass(frozen=True, slots=True)
class SagaStepSpec:
    """Definition d'une etape Saga et de sa compensation inverse."""

    step_id: str
    action_fn: Callable[[dict[str, Any], str], dict[str, Any]]
    compensate_fn: Callable[[dict[str, Any], str], dict[str, Any]] | None = (
        None
    )
    is_pivot: bool = False
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class SagaRunResult:
    """Bilan d'execution ou de reprise d'une Saga."""

    saga_id: str
    task_id: str
    status: SagaStatus
    executed_steps: tuple[str, ...]
    compensated_steps: tuple[str, ...]
    outbox_events: tuple[dict[str, Any], ...]
    escalation_queue: str | None
    state_snapshot: dict[str, Any]


def _utc_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _init_sqlite_conn(db_path: Path | None) -> sqlite3.Connection:
    target = ":memory:" if db_path is None else str(db_path)
    if db_path is not None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(
        target, timeout=30.0, check_same_thread=False, isolation_level=None
    )
    conn.execute("PRAGMA busy_timeout = 15000")
    if db_path is not None:
        conn.execute("PRAGMA journal_mode = WAL")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS idempotency_store ("
        "idem_key TEXT PRIMARY KEY, payload_hash TEXT NOT NULL, "
        "status TEXT NOT NULL, result_json TEXT NOT NULL)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS semantic_locks ("
        "resource_key TEXT PRIMARY KEY, saga_id TEXT NOT NULL, "
        "expires_at REAL NOT NULL)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS sagas ("
        "saga_id TEXT PRIMARY KEY, resource_lock_key TEXT, "
        "state_json TEXT NOT NULL)"
    )
    return conn


# CA-G0-SYNC-BEGIN:G0-EX-CH03-03
def compute_idempotency_key(task_id: str, step_id: str) -> str:
    """Retourne jcs_sha256_hex(['idem-v1', task_id, step_id])."""
    return jcs_sha256_hex(["idem-v1", task_id, step_id])

@dataclass(frozen=True, slots=True)
class CompensationChannel:
    """Canal isole EXIG-ORC-28 immunise (revocation/coupe-circuit)."""
    spiffe_id: str = "spiffe://ent.ca/saga-compensator"
    isolated_budget_cad: Decimal = Decimal("100.00")
    immune_to_agent_revocation: bool = True
    immune_to_gateway_circuit_breaker: bool = True
    def execute_compensation(
        self, step_id: str, comp_fn: Callable[[dict[str, Any], str], dict],
        payload: dict[str, Any], idempotency_key: str, *,
        agent_revoked: bool = False, gateway_open: bool = False,
    ) -> dict[str, Any]:
        if (agent_revoked and not self.immune_to_agent_revocation) or (
            gateway_open and not self.immune_to_gateway_circuit_breaker
        ):
            raise RuntimeError(f"Canal compensation bloque ({step_id})")
        return comp_fn(payload, idempotency_key)

class SagaOrchestrator:
    """Orchestrateur durable avec Outbox, pivot et file humaine."""
    def __init__(
        self, db_path: Path | None = None,
        compensation_channel: CompensationChannel | None = None,
        escalation_queue: str = "file-humaine-prioritaire",
    ) -> None:
        self.db_path, self.escalation_queue = db_path, escalation_queue
        self.compensation_channel = (
            compensation_channel or CompensationChannel())
        self._lock = threading.RLock()
        self._conn = _init_sqlite_conn(db_path)
# CA-G0-SYNC-END:G0-EX-CH03-03

    def close(self) -> None:
        """Ferme proprement la connexion SQLite."""
        with self._lock:
            self._conn.close()

    def __enter__(self) -> SagaOrchestrator:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def _run_tx(self, fn: Callable[[], Any]) -> Any:
        with self._lock:
            self._conn.execute("BEGIN IMMEDIATE")
            try:
                res = fn()
                self._conn.execute("COMMIT")
                return res
            except Exception:
                self._conn.execute("ROLLBACK")
                raise

    def _save_state(
        self, state: dict[str, Any], resource_lock_key: str | None = None
    ) -> None:
        state["updated_at"] = _utc_iso()
        serialized = json.dumps(state, ensure_ascii=False)

        def _op() -> None:
            if resource_lock_key is None:
                row = self._conn.execute(
                    "SELECT resource_lock_key FROM sagas WHERE saga_id = ?",
                    (state["saga_id"],),
                ).fetchone()
                lock_key = row[0] if row is not None else None
            else:
                lock_key = resource_lock_key
            self._conn.execute(
                "INSERT OR REPLACE INTO sagas "
                "(saga_id, resource_lock_key, state_json) VALUES (?, ?, ?)",
                (state["saga_id"], lock_key, serialized),
            )

        self._run_tx(_op)

    def _load_state_and_lock(
        self, saga_id: str
    ) -> tuple[dict[str, Any], str | None]:
        with self._lock:
            row = self._conn.execute(
                "SELECT state_json, resource_lock_key "
                "FROM sagas WHERE saga_id = ?",
                (saga_id,),
            ).fetchone()
        if row is None:
            raise KeyError(f"Saga inconnue : {saga_id}")
        return json.loads(row[0]), row[1]

    def _load_state(self, saga_id: str) -> dict[str, Any]:
        state, _ = self._load_state_and_lock(saga_id)
        return state

    def _to_result(self, state: dict[str, Any]) -> SagaRunResult:
        executed = tuple(
            s["step_id"]
            for s in state["steps"]
            if s["status"] in ("EXECUTED", "COMPENSATED")
        )
        compensated = tuple(
            s["step_id"]
            for s in reversed(state["steps"])
            if s["status"] == "COMPENSATED"
        )
        return SagaRunResult(
            saga_id=state["saga_id"],
            task_id=state["task_id"],
            status=SagaStatus(state["status"]),
            executed_steps=executed,
            compensated_steps=compensated,
            outbox_events=tuple(copy.deepcopy(state["outbox"])),
            escalation_queue=state["escalation_queue"],
            state_snapshot=copy.deepcopy(state),
        )

    def _run_compensation(
        self,
        state: dict[str, Any],
        steps_by_id: dict[str, SagaStepSpec],
        *,
        simulate_crash_mid_comp_step: str | None = None,
        agent_revoked: bool = False,
        gateway_circuit_open: bool = False,
    ) -> SagaRunResult:
        state["status"] = SagaStatus.COMPENSATING.value
        self._save_state(state)
        for st in reversed(state["steps"]):
            if st["status"] != "EXECUTED":
                continue
            spec = steps_by_id.get(st["step_id"])
            if spec is None or spec.compensate_fn is None:
                continue
            if simulate_crash_mid_comp_step == st["step_id"]:
                self._save_state(state)
                raise SimulatedCrashError(
                    f"Crash simule avant compensation {st['step_id']}"
                )
            ok_comp = False
            while st["compensation_attempts"] < 2:
                st["compensation_attempts"] += 1
                try:
                    self.compensation_channel.execute_compensation(
                        st["step_id"],
                        spec.compensate_fn,
                        copy.deepcopy(spec.payload),
                        st["idempotency_key"],
                        agent_revoked=agent_revoked,
                        gateway_open=gateway_circuit_open,
                    )
                    st["status"] = "COMPENSATED"
                    ok_comp = True
                    self._save_state(state)
                    break
                except Exception:
                    self._save_state(state)
            if not ok_comp:
                st["status"] = "ESCALATED"
                state["status"] = SagaStatus.HUMAN_ESCALATION.value
                state["escalation_queue"] = self.escalation_queue
                self._save_state(state)
                return self._to_result(state)
        state["status"] = SagaStatus.COMPENSATED.value
        self._save_state(state)
        return self._to_result(state)

    def _drive_saga(
        self,
        state: dict[str, Any],
        steps: Sequence[SagaStepSpec],
        *,
        simulate_crash_after_outbox_step: str | None = None,
        simulate_crash_mid_comp_step: str | None = None,
        agent_revoked: bool = False,
        gateway_circuit_open: bool = False,
    ) -> SagaRunResult:
        steps_by_id = {s.step_id: s for s in steps}
        cur_status = SagaStatus(state["status"])
        if cur_status in (
            SagaStatus.COMPLETED,
            SagaStatus.COMPENSATED,
            SagaStatus.PIVOT_REACHED,
            SagaStatus.HUMAN_ESCALATION,
        ):
            return self._to_result(state)
        if cur_status == SagaStatus.COMPENSATING:
            return self._run_compensation(
                state,
                steps_by_id,
                simulate_crash_mid_comp_step=simulate_crash_mid_comp_step,
                agent_revoked=agent_revoked,
                gateway_circuit_open=gateway_circuit_open,
            )

        for idx, st in enumerate(state["steps"]):
            if st["status"] == "EXECUTED":
                continue
            spec = steps_by_id[st["step_id"]]
            state["current_step_index"] = idx
            ev = next(
                (e for e in state["outbox"] if e["step_id"] == st["step_id"]),
                None,
            )
            if ev is None:
                ev = {
                    "event_id": f"{state['saga_id']}:{st['step_id']}",
                    "step_id": st["step_id"],
                    "idempotency_key": st["idempotency_key"],
                    "dispatched": False,
                }
                state["outbox"].append(ev)
                self._save_state(state)
            if simulate_crash_after_outbox_step == st["step_id"]:
                raise SimulatedCrashError(
                    f"Crash simule apres Outbox {st['step_id']}"
                )
            try:
                spec.action_fn(copy.deepcopy(spec.payload), st["idempotency_key"])
            except Exception:
                st["status"] = "FAILED"
                if state["pivot_reached"]:
                    state["status"] = SagaStatus.PIVOT_REACHED.value
                    state["escalation_queue"] = self.escalation_queue
                    self._save_state(state)
                    return self._to_result(state)
                return self._run_compensation(
                    state,
                    steps_by_id,
                    simulate_crash_mid_comp_step=simulate_crash_mid_comp_step,
                    agent_revoked=agent_revoked,
                    gateway_circuit_open=gateway_circuit_open,
                )
            ev["dispatched"] = True
            st["status"] = "EXECUTED"
            if spec.is_pivot:
                state["pivot_reached"] = True
                state["pivot_step_id"] = st["step_id"]
            self._save_state(state)

        state["status"] = SagaStatus.COMPLETED.value
        self._save_state(state)
        return self._to_result(state)

    def execute_saga(
        self,
        saga_id: str,
        task_id: str,
        resource_lock_key: str,
        steps: Sequence[SagaStepSpec],
        *,
        simulate_crash_after_outbox_step: str | None = None,
        simulate_crash_mid_comp_step: str | None = None,
        agent_revoked: bool = False,
        gateway_circuit_open: bool = False,
    ) -> SagaRunResult:
        """Execute une Saga en appliquant Outbox, pivot et compensation."""
        if not steps:
            raise ValueError("steps ne doit pas etre vide")
        step_ids = [s.step_id for s in steps]
        if len(set(step_ids)) != len(step_ids):
            raise ValueError("step_id duplique dans steps")
        if not self.acquire_semantic_lock(resource_lock_key, saga_id):
            raise IdempotencyConflictError(
                409, f"Verrou semantique occupe pour {resource_lock_key}"
            )
        state: dict[str, Any] = {
            "saga_id": saga_id,
            "task_id": task_id,
            "status": SagaStatus.RUNNING.value,
            "pivot_step_id": None,
            "pivot_reached": False,
            "current_step_index": 0,
            "steps": [
                {
                    "step_id": s.step_id,
                    "idempotency_key": compute_idempotency_key(
                        task_id, s.step_id
                    ),
                    "status": "PENDING",
                    "compensation_attempts": 0,
                    "is_pivot": s.is_pivot,
                }
                for s in steps
            ],
            "outbox": [],
            "compensation_channel_id": self.compensation_channel.spiffe_id,
            "escalation_queue": None,
            "updated_at": _utc_iso(),
        }
        self._save_state(state, resource_lock_key=resource_lock_key)
        try:
            res = self._drive_saga(
                state,
                steps,
                simulate_crash_after_outbox_step=(
                    simulate_crash_after_outbox_step
                ),
                simulate_crash_mid_comp_step=simulate_crash_mid_comp_step,
                agent_revoked=agent_revoked,
                gateway_circuit_open=gateway_circuit_open,
            )
            self.release_semantic_lock(resource_lock_key, saga_id)
            return res
        except SimulatedCrashError:
            raise
        except Exception:
            self.release_semantic_lock(resource_lock_key, saga_id)
            raise

    def resume_saga(
        self,
        saga_id: str,
        steps: Sequence[SagaStepSpec],
        *,
        agent_revoked: bool = False,
        gateway_circuit_open: bool = False,
    ) -> SagaRunResult:
        """Reprend durablement une Saga interrompue sans doublon."""
        state, lock_key = self._load_state_and_lock(saga_id)
        res = self._drive_saga(
            state,
            steps,
            agent_revoked=agent_revoked,
            gateway_circuit_open=gateway_circuit_open,
        )
        if lock_key:
            self.release_semantic_lock(lock_key, saga_id)
        return res

    def submit_step_idempotent(
        self,
        task_id: str,
        step_id: str,
        payload: dict[str, Any],
        *,
        in_progress: bool = False,
    ) -> dict[str, Any]:
        """Enregistre ou rejoue une etape; leve 409 ou 422 si conflit."""
        idem_key = compute_idempotency_key(task_id, step_id)
        payload_hash = jcs_sha256_hex(payload)
        if in_progress:
            raise IdempotencyConflictError(
                409, f"Execution concurrente en cours pour {idem_key}"
            )

        def _op() -> dict[str, Any]:
            row = self._conn.execute(
                "SELECT payload_hash, status, result_json "
                "FROM idempotency_store WHERE idem_key = ?",
                (idem_key,),
            ).fetchone()
            if row is not None:
                old_hash, status, res_json = row
                if status == "IN_PROGRESS":
                    raise IdempotencyConflictError(409, "Etape deja en cours")
                if old_hash != payload_hash:
                    raise IdempotencyConflictError(
                        422,
                        "Cle d'idempotence reutilisee avec charge differente",
                    )
                return json.loads(res_json)
            res = copy.deepcopy(payload)
            self._conn.execute(
                "INSERT INTO idempotency_store "
                "(idem_key, payload_hash, status, result_json) "
                "VALUES (?, ?, ?, ?)",
                (idem_key, payload_hash, "COMPLETED", json.dumps(res)),
            )
            return res

        return self._run_tx(_op)

    def receive_late_step_response(
        self, saga_id: str, step_id: str, late_result: dict[str, Any]
    ) -> bool:
        """Rejette toute reponse tardive recue apres decision de compenser."""
        _ = late_result
        state = self._load_state(saga_id)
        if state["status"] in (
            SagaStatus.COMPLETED.value,
            SagaStatus.COMPENSATING.value,
            SagaStatus.COMPENSATED.value,
            SagaStatus.HUMAN_ESCALATION.value,
            SagaStatus.PIVOT_REACHED.value,
        ):
            return False
        st = next((s for s in state["steps"] if s["step_id"] == step_id), None)
        if st is None or st["status"] in ("FAILED", "COMPENSATED", "EXECUTED"):
            return False
        return True

    def acquire_semantic_lock(
        self, resource_key: str, saga_id: str, ttl_s: int = 300
    ) -> bool:
        """Acquiert un verrou semantique borne ou retourne False si occupe."""
        now = time.time()

        def _op() -> bool:
            row = self._conn.execute(
                "SELECT saga_id, expires_at FROM semantic_locks "
                "WHERE resource_key = ?",
                (resource_key,),
            ).fetchone()
            if row is not None:
                owner, expires_at = row
                if owner != saga_id and float(expires_at) > now:
                    return False
            self._conn.execute(
                "INSERT OR REPLACE INTO semantic_locks "
                "(resource_key, saga_id, expires_at) VALUES (?, ?, ?)",
                (resource_key, saga_id, now + ttl_s),
            )
            return True

        return bool(self._run_tx(_op))

    def release_semantic_lock(self, resource_key: str, saga_id: str) -> None:
        """Libere le verrou semantique detenu par saga_id."""

        def _op() -> None:
            self._conn.execute(
                "DELETE FROM semantic_locks "
                "WHERE resource_key = ? AND saga_id = ?",
                (resource_key, saga_id),
            )

        self._run_tx(_op)

    def get_state(self, saga_id: str) -> dict[str, Any]:
        """Retourne l'etat conforme a schemas/saga_state.schema.json."""
        return self._load_state(saga_id)
