# Canonical Output Example

Current canonical control-plane output example from
`docs/governance/governance-authoritative-state-answer.json`:

```json
{
  "generated_by": "inspect_governance_state.py",
  "answer_version": "1.0",
  "control_plane_version": "1.0",
  "control_plane_surface_role": "canonical_governance_control_plane",
  "required_snapshot_input": "docs/governance/governance-state-snapshot.json",
  "snapshot_id": "8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df",
  "snapshot_drift_detected": false,
  "governance_state_consensus": true,
  "governance_maturity": {
    "overall_system_maturity": 50,
    "governance_maturity_reference": 84
  },
  "governance_blockers": [
    "multi_agent_governance",
    "architecture_advisor",
    "autonomous_governance_loop"
  ],
  "governance_progression_stage": {
    "stage": 1,
    "focus": "state_normalization",
    "targets": [
      "multi_agent_governance"
    ]
  },
  "governance_gap_state": "GAPS_PRESENT",
  "governance_trend_classification": "newly_established",
  "authoritative_next_action": {
    "generated_by": "inspect_governance_state.py",
    "selector_version": "1.0",
    "required_snapshot_input": "docs/governance/governance-state-snapshot.json",
    "snapshot_id": "8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df",
    "snapshot_drift_detected": false,
    "governance_state_consensus": true,
    "recommended_action_type": "state_normalization",
    "target_domain": "multi_agent_governance",
    "reason": "INVALID_STATE governance domain must be normalized before other capability advancement",
    "derived_from": "docs/governance/governance-system-advancement-roadmap.json",
    "current_status": "INVALID_STATE",
    "suggested_pipeline": "establish-role-scoped-codex-sub-agent-specialization"
  }
}
```

Compatibility note:

- `recommended_next_action` is also present in the live output and currently
  equals `authoritative_next_action`.
