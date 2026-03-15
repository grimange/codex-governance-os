# Verification Plan

Verification for Pipeline 188 should confirm:

1. `python3 tools/governance/inspect_governance_state.py authoritative-state`
   emits the converged control-plane payload successfully.
2. repeated authoritative-state execution on unchanged inputs produces
   identical output and identical hash.
3. `control_plane_surface_role` is present and equals
   `canonical_governance_control_plane`.
4. `authoritative_next_action` is present and equals the standalone selector
   payload from `python3 tools/governance/inspect_governance_state.py next-action`.
5. `recommended_next_action` remains present as a compatibility alias and
   equals `authoritative_next_action`.
6. provenance fields remain intact:
   - `required_snapshot_input`
   - `snapshot_id`
   - `snapshot_drift_detected`
   - `governance_state_consensus`
7. governance maturity, progression stage, blockers, gap state, and trend
   classification remain stable.
8. governance regression tests pass.
