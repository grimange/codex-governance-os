# Control-Plane Surface Model

The canonical governance control-plane surface is:

- `docs/governance/governance-authoritative-state-answer.json`

Current converged model fields:

- `generated_by`
- `answer_version`
- `control_plane_version`
- `control_plane_surface_role`
- `required_snapshot_input`
- `snapshot_id`
- `snapshot_drift_detected`
- `governance_state_consensus`
- `governance_maturity`
- `governance_blockers`
- `governance_progression_stage`
- `governance_gap_state`
- `governance_trend_classification`
- `authoritative_next_action`
- `recommended_next_action`
- `sources`

Control-plane semantics:

- `control_plane_surface_role` marks the surface as
  `canonical_governance_control_plane`
- `authoritative_next_action` is the canonical embedded next-action field for
  the converged control-plane model
- `recommended_next_action` remains present as a compatibility alias to the same
  payload during convergence
- `governance_maturity`, blockers, progression, gap state, and trend
  classification remain snapshot-derived and top-level

Supporting surfaces remain valid but subordinate:

- `docs/governance/governance-system-next-action.json`
- `docs/governance/governance-state-snapshot.json`
