# SPDX-License-Identifier: MIT
"""Suite pytest TDD des 10 scenarios deterministes de fautes EXIG-ORC-20."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import pytest

from policy_saga.saga_orchestrator import (
    CompensationChannel,
    SagaOrchestrator,
    SagaStatus,
    SagaStepSpec,
    SimulatedCrashError,
    compute_idempotency_key,
)

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"


def _load_saga_schema() -> dict[str, Any]:
    return json.loads(
        (SCHEMAS_DIR / "saga_state.schema.json").read_text(encoding="utf-8")
    )


def test_fault_01_step_t2_compensates_c1(tmp_path: Path) -> None:
    """1. Echec force a T2 -> compensation C1 en ordre inverse."""
    log: list[str] = []
    orch = SagaOrchestrator(db_path=tmp_path / "f01.sqlite")
    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, k: log.append(f"exec:T1:{k[:8]}") or {"ok": 1},
            compensate_fn=lambda _p, k: (
                log.append(f"comp:C1:{k[:8]}") or {"c": 1}
            ),
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                RuntimeError("T2 failure")
            ),
            compensate_fn=lambda _p, _k: {"c": 2},
        ),
        SagaStepSpec(
            step_id="T3",
            action_fn=lambda _p, _k: log.append("exec:T3") or {"ok": 3},
            compensate_fn=None,
        ),
    ]
    res = orch.execute_saga("saga-01", "task-01", "lock-res-01", steps)
    assert res.status == SagaStatus.COMPENSATED
    assert res.compensated_steps == ("T1",)
    assert any(item.startswith("comp:C1:") for item in log)
    assert "exec:T3" not in log
    Draft202012Validator(_load_saga_schema()).validate(res.state_snapshot)


def test_fault_02_crash_after_outbox_resumes(tmp_path: Path) -> None:
    """2. Crash simule apres ecriture Outbox -> reprise sans perte/doublon."""
    calls: list[str] = []
    orch = SagaOrchestrator(db_path=tmp_path / "f02.sqlite")
    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: calls.append("T1") or {"done": 1},
            compensate_fn=lambda _p, _k: {"c": 1},
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: calls.append("T2") or {"done": 2},
            compensate_fn=lambda _p, _k: {"c": 2},
        ),
    ]
    with pytest.raises(SimulatedCrashError):
        orch.execute_saga(
            "saga-02",
            "task-02",
            "lock-res-02",
            steps,
            simulate_crash_after_outbox_step="T2",
        )
    assert calls == ["T1"]

    resumed = SagaOrchestrator(db_path=tmp_path / "f02.sqlite").resume_saga(
        "saga-02", steps
    )
    assert resumed.status == SagaStatus.COMPLETED
    assert calls == ["T1", "T2"]  # T1 non reexecute, T2 execute une fois
    assert all(ev["dispatched"] for ev in resumed.outbox_events)
    Draft202012Validator(_load_saga_schema()).validate(resumed.state_snapshot)


def test_fault_03_lost_response_idempotent_replay(tmp_path: Path) -> None:
    """3. Effet aval realise mais reponse perdue -> rejeu idem-v1 deduplique."""
    downstream_effects = 0
    memo: dict[str, dict[str, Any]] = {}

    def downstream_call(
        payload: dict[str, Any], idem_key: str
    ) -> dict[str, Any]:
        nonlocal downstream_effects
        if idem_key not in memo:
            downstream_effects += 1
            memo[idem_key] = {"bc_id": "BC-001", "payload": payload}
        return memo[idem_key]

    orch = SagaOrchestrator(db_path=tmp_path / "f03.sqlite")
    k1 = compute_idempotency_key("task-03", "T1")
    k2 = compute_idempotency_key("task-03", "T1")
    assert k1 == k2 and len(k1) == 64

    r1 = orch.submit_step_idempotent("task-03", "T1", {"sku": "PRD-1"})
    eff1 = downstream_call(r1, k1)
    r2 = orch.submit_step_idempotent("task-03", "T1", {"sku": "PRD-1"})
    eff2 = downstream_call(r2, k2)
    assert downstream_effects == 1
    assert eff1 == eff2


def test_fault_04_late_response_rejected_after_compensation(
    tmp_path: Path,
) -> None:
    """4. Reponse tardive apres bascule compensation -> rejetee."""
    orch = SagaOrchestrator(db_path=tmp_path / "f04.sqlite")
    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: {"ok": 1},
            compensate_fn=lambda _p, _k: {"undone": 1},
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                TimeoutError("T2 timed out")
            ),
            compensate_fn=lambda _p, _k: {"undone": 2},
        ),
    ]
    res = orch.execute_saga("saga-04", "task-04", "lock-res-04", steps)
    assert res.status == SagaStatus.COMPENSATED
    accepted = orch.receive_late_step_response(
        "saga-04", "T2", {"status": "late_commit"}
    )
    assert accepted is False
    assert orch.get_state("saga-04")["status"] == SagaStatus.COMPENSATED
    Draft202012Validator(_load_saga_schema()).validate(
        orch.get_state("saga-04")
    )


def test_fault_05_concurrent_sagas_semantic_lock(tmp_path: Path) -> None:
    """5. Deux sagas concurrentes sur meme ressource -> serialisation/rejet."""
    orch = SagaOrchestrator(db_path=tmp_path / "f05.sqlite")
    assert (
        orch.acquire_semantic_lock("dossier-8841", "saga-A", ttl_s=60) is True
    )
    assert (
        orch.acquire_semantic_lock("dossier-8841", "saga-B", ttl_s=60) is False
    )
    orch.release_semantic_lock("dossier-8841", "saga-A")
    assert (
        orch.acquire_semantic_lock("dossier-8841", "saga-B", ttl_s=60) is True
    )


def test_fault_06_pivot_blocks_backward_compensation(tmp_path: Path) -> None:
    """6. Echec apres point pivot T3 -> aucune compensation arriere T1..T3."""
    comp_called: list[str] = []
    orch = SagaOrchestrator(db_path=tmp_path / "f06.sqlite")
    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: {"ok": 1},
            compensate_fn=lambda _p, _k: comp_called.append("C1") or {"c": 1},
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: {"ok": 2},
            compensate_fn=lambda _p, _k: comp_called.append("C2") or {"c": 2},
        ),
        SagaStepSpec(
            step_id="T3",
            action_fn=lambda _p, _k: {"pivot": True},
            compensate_fn=None,
            is_pivot=True,
        ),
        SagaStepSpec(
            step_id="T4",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                RuntimeError("T4 post-pivot error")
            ),
            compensate_fn=None,
        ),
    ]
    res = orch.execute_saga("saga-06", "task-06", "lock-res-06", steps)
    assert comp_called == []
    assert res.compensated_steps == ()
    assert res.status in {
        SagaStatus.PIVOT_REACHED,
        SagaStatus.HUMAN_ESCALATION,
    }
    assert res.state_snapshot["pivot_reached"] is True
    Draft202012Validator(_load_saga_schema()).validate(res.state_snapshot)


def test_fault_07_double_compensation_strictly_idempotent(
    tmp_path: Path,
) -> None:
    """7. Double execution forcee de chaque C_k -> strictement idempotente."""
    comp_count = {"C1": 0}
    orch = SagaOrchestrator(db_path=tmp_path / "f07.sqlite")

    def c1_fn(_p: dict[str, Any], _k: str) -> dict[str, Any]:
        comp_count["C1"] += 1
        return {"compensated": True}

    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: {"ok": 1},
            compensate_fn=c1_fn,
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                RuntimeError("boom")
            ),
        ),
    ]
    res1 = orch.execute_saga("saga-07", "task-07", "lock-res-07", steps)
    res2 = orch.resume_saga("saga-07", steps)
    assert res1.status == SagaStatus.COMPENSATED
    assert res2.status == SagaStatus.COMPENSATED
    assert comp_count["C1"] == 1


def test_fault_08_two_comp_failures_escalate(tmp_path: Path) -> None:
    """8. Double echec consecutif de C_k -> file humaine EXIG-ORC-18."""
    attempts = {"C1": 0}
    orch = SagaOrchestrator(
        db_path=tmp_path / "f08.sqlite",
        escalation_queue="file-humaine-prioritaire",
    )

    def failing_comp(_p: dict[str, Any], _k: str) -> dict[str, Any]:
        attempts["C1"] += 1
        raise RuntimeError("ERP compensation error")

    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: {"ok": 1},
            compensate_fn=failing_comp,
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                RuntimeError("trigger comp")
            ),
        ),
    ]
    res = orch.execute_saga("saga-08", "task-08", "lock-res-08", steps)
    assert attempts["C1"] == 2
    assert res.status == SagaStatus.HUMAN_ESCALATION
    assert res.escalation_queue == "file-humaine-prioritaire"
    Draft202012Validator(_load_saga_schema()).validate(res.state_snapshot)


def test_fault_09_crash_mid_compensation_resumes_cleanly(
    tmp_path: Path,
) -> None:
    """9. Crash en milieu de compensation -> reprise jusqu'a completude."""
    comp_log: list[str] = []
    orch = SagaOrchestrator(db_path=tmp_path / "f09.sqlite")
    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: {"ok": 1},
            compensate_fn=lambda _p, _k: comp_log.append("C1") or {"c": 1},
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: {"ok": 2},
            compensate_fn=lambda _p, _k: comp_log.append("C2") or {"c": 2},
        ),
        SagaStepSpec(
            step_id="T3",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                RuntimeError("T3 fail")
            ),
        ),
    ]
    with pytest.raises(SimulatedCrashError):
        orch.execute_saga(
            "saga-09",
            "task-09",
            "lock-res-09",
            steps,
            simulate_crash_mid_comp_step="T1",
        )
    assert comp_log == ["C2"]

    resumed = SagaOrchestrator(db_path=tmp_path / "f09.sqlite").resume_saga(
        "saga-09", steps
    )
    assert resumed.status == SagaStatus.COMPENSATED
    assert comp_log == ["C2", "C1"]
    Draft202012Validator(_load_saga_schema()).validate(resumed.state_snapshot)


def test_fault_10_isolated_compensation_channel(tmp_path: Path) -> None:
    """10. Agent revoque + coupe-circuit -> succes via CompensationChannel."""
    channel = CompensationChannel()
    assert channel.spiffe_id == "spiffe://ent.ca/saga-compensator"
    assert channel.immune_to_agent_revocation is True
    assert channel.immune_to_gateway_circuit_breaker is True
    direct = channel.execute_compensation(
        "T0", lambda p, k: {"via": channel.spiffe_id, "k": k}, {}, "k-test"
    )
    assert direct["via"] == "spiffe://ent.ca/saga-compensator"

    orch = SagaOrchestrator(
        db_path=tmp_path / "f10.sqlite",
        compensation_channel=channel,
    )
    steps = [
        SagaStepSpec(
            step_id="T1",
            action_fn=lambda _p, _k: {"ok": 1},
            compensate_fn=lambda _p, _k: {"via": channel.spiffe_id},
        ),
        SagaStepSpec(
            step_id="T2",
            action_fn=lambda _p, _k: (_ for _ in ()).throw(
                RuntimeError("T2 abort")
            ),
        ),
    ]
    res = orch.execute_saga(
        "saga-10",
        "task-10",
        "lock-res-10",
        steps,
        agent_revoked=True,
        gateway_circuit_open=True,
    )
    assert res.status == SagaStatus.COMPENSATED
    assert res.compensated_steps == ("T1",)
    assert (
        res.state_snapshot["compensation_channel_id"]
        == "spiffe://ent.ca/saga-compensator"
    )
    Draft202012Validator(_load_saga_schema()).validate(res.state_snapshot)


def test_saga_all_10_deterministic_faults(tmp_path: Path) -> None:
    """Agrege la verification des 10 scenarios EXIG-ORC-20."""
    for idx in range(1, 11):
        sub = tmp_path / f"sub-{idx:02d}"
        sub.mkdir()
        if idx == 1:
            test_fault_01_step_t2_compensates_c1(sub)
        elif idx == 2:
            test_fault_02_crash_after_outbox_resumes(sub)
        elif idx == 3:
            test_fault_03_lost_response_idempotent_replay(sub)
        elif idx == 4:
            test_fault_04_late_response_rejected_after_compensation(sub)
        elif idx == 5:
            test_fault_05_concurrent_sagas_semantic_lock(sub)
        elif idx == 6:
            test_fault_06_pivot_blocks_backward_compensation(sub)
        elif idx == 7:
            test_fault_07_double_compensation_strictly_idempotent(sub)
        elif idx == 8:
            test_fault_08_two_comp_failures_escalate(sub)
        elif idx == 9:
            test_fault_09_crash_mid_compensation_resumes_cleanly(sub)
        elif idx == 10:
            test_fault_10_isolated_compensation_channel(sub)
