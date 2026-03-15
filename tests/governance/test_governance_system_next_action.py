from __future__ import annotations

import importlib.util
import json
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[2] / "tools" / "governance" / "inspect_governance_state.py"


def load_module():
    spec = importlib.util.spec_from_file_location("inspect_governance_state", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def base_payloads():
    roadmap = {
        "generated_by": "inspect_governance_state.py",
        "roadmap_version": "1.0",
        "current_maturity_snapshot": {
            "verified_domains": ["codex_governance_layer"],
            "unverified_domains": ["architecture_advisor", "autonomous_governance_loop"],
            "invalid_domains": ["multi_agent_governance"],
        },
        "advancement_stages": [
            {"stage": 1, "focus": "state_normalization", "targets": ["multi_agent_governance"]},
            {
                "stage": 2,
                "focus": "capability_expansion",
                "targets": ["architecture_advisor", "autonomous_governance_loop"],
            },
        ],
        "blockers_to_full_maturity": [
            "multi_agent_governance",
            "architecture_advisor",
            "autonomous_governance_loop",
        ],
        "recommended_next_target": "multi_agent_governance",
        "sources": [],
    }
    remediation = {
        "generated_by": "inspect_governance_state.py",
        "planner_version": "1.0",
        "remediation_plan": [
            {
                "domain": "multi_agent_governance",
                "current_status": "INVALID_STATE",
                "remediation_strategy": "state_normalization",
                "required_evidence": [],
                "recommended_action": "normalize multi_agent_governance registry and capability state",
                "suggested_pipeline": "establish-role-scoped-codex-sub-agent-specialization",
                "priority": "CRITICAL",
                "dependency_order": 1,
                "promotion_target": "VERIFIED",
            },
            {
                "domain": "architecture_advisor",
                "current_status": "UNVERIFIED",
                "remediation_strategy": "capability_completion",
                "required_evidence": [],
                "recommended_action": "complete and verify architecture_advisor",
                "suggested_pipeline": "unknown",
                "priority": "HIGH",
                "dependency_order": 2,
                "promotion_target": "VERIFIED",
            },
        ],
        "sources": [],
    }
    gaps = {
        "overall_gap_state": "GAPS_PRESENT",
        "detected_gaps": [
            {
                "gap_id": "multi_agent_governance-invalid-state",
                "domain": "multi_agent_governance",
                "classification": "INVALID_STATE",
            },
            {
                "gap_id": "architecture_advisor-unverified",
                "domain": "architecture_advisor",
                "classification": "UNVERIFIED",
            },
        ],
    }
    maturity = {
        "overall_maturity": 50,
        "domain_classifications": {
            "codex_governance_layer": "VERIFIED",
            "multi_agent_governance": "INVALID_STATE",
            "architecture_advisor": "UNVERIFIED",
        },
    }
    return roadmap, remediation, gaps, maturity


def setup_paths(tmp_path: Path, monkeypatch):
    module = load_module()
    roadmap, remediation, gaps, maturity = base_payloads()

    roadmap_path = tmp_path / "roadmap.json"
    remediation_path = tmp_path / "remediation.json"
    gaps_path = tmp_path / "gaps.json"
    maturity_path = tmp_path / "maturity.json"
    output_path = tmp_path / "next-action.json"

    write_json(roadmap_path, roadmap)
    write_json(remediation_path, remediation)
    write_json(gaps_path, gaps)
    write_json(maturity_path, maturity)

    monkeypatch.setattr(module, "SYSTEM_ADVANCEMENT_ROADMAP_JSON", roadmap_path)
    monkeypatch.setattr(module, "SYSTEM_GAP_REMEDIATION_PLAN_JSON", remediation_path)
    monkeypatch.setattr(module, "SYSTEM_GAPS_JSON", gaps_path)
    monkeypatch.setattr(module, "SYSTEM_MATURITY_JSON", maturity_path)
    monkeypatch.setattr(module, "SYSTEM_NEXT_ACTION_JSON", output_path)
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)

    return module, roadmap_path, remediation_path, gaps_path, maturity_path, output_path


def test_valid_canonical_roadmap_target_exits_zero_and_emits_output(tmp_path, monkeypatch):
    module, _, _, _, _, output_path = setup_paths(tmp_path, monkeypatch)

    status = module.run_next_action_selector()

    assert status == 0
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["target_domain"] == "multi_agent_governance"
    assert payload["recommended_action_type"] == "state_normalization"


def test_invalid_recommended_next_target_fails_closed(tmp_path, monkeypatch, capsys):
    module, roadmap_path, _, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    payload = json.loads(roadmap_path.read_text(encoding="utf-8"))
    payload["recommended_next_target"] = "invalid_governance_target"
    write_json(roadmap_path, payload)

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET" in err


def test_missing_recommended_next_target_fails_closed(tmp_path, monkeypatch, capsys):
    module, roadmap_path, _, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    payload = json.loads(roadmap_path.read_text(encoding="utf-8"))
    payload["recommended_next_target"] = None
    write_json(roadmap_path, payload)

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET" in err


def test_target_absent_from_remediation_plan_fails_closed(tmp_path, monkeypatch, capsys):
    module, _, remediation_path, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    payload = json.loads(remediation_path.read_text(encoding="utf-8"))
    payload["remediation_plan"] = payload["remediation_plan"][1:]
    write_json(remediation_path, payload)

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "GOVERNANCE_STATE_SURFACE_INCONSISTENCY" in err


def test_gap_roadmap_mismatch_fails_closed(tmp_path, monkeypatch, capsys):
    module, _, _, gaps_path, _, output_path = setup_paths(tmp_path, monkeypatch)
    payload = json.loads(gaps_path.read_text(encoding="utf-8"))
    payload["detected_gaps"] = [payload["detected_gaps"][1]]
    write_json(gaps_path, payload)

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "GOVERNANCE_STATE_SURFACE_INCONSISTENCY" in err


def test_missing_canonical_surface_fails_closed(tmp_path, monkeypatch, capsys):
    module, _, remediation_path, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    remediation_path.unlink()

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "MISSING_CANONICAL_GOVERNANCE_SURFACE" in err


def test_shadow_surface_detection_fails_closed(tmp_path, monkeypatch, capsys):
    module, roadmap_path, _, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    shadow_dir = tmp_path / "backup"
    shadow_dir.mkdir()
    write_json(shadow_dir / roadmap_path.name, {"shadow": True})

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "SHADOW_GOVERNANCE_SURFACE_DETECTED" in err


def test_target_consensus_violation_fails_closed(tmp_path, monkeypatch, capsys):
    module, roadmap_path, _, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    payload = json.loads(roadmap_path.read_text(encoding="utf-8"))
    payload["recommended_next_target"] = "architecture_advisor"
    write_json(roadmap_path, payload)

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION" in err


def test_ambiguous_surface_candidate_detection_fails_closed(tmp_path, monkeypatch, capsys):
    module, roadmap_path, _, _, _, output_path = setup_paths(tmp_path, monkeypatch)
    ambiguous_path = roadmap_path.with_name(f"{roadmap_path.stem}-copy.json")
    write_json(ambiguous_path, {"shadow": True})

    status = module.run_next_action_selector()

    assert status == 1
    assert not output_path.exists()
    err = capsys.readouterr().err
    assert "AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED" in err
