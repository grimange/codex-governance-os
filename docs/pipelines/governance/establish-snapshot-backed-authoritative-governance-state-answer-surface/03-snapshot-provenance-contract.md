# Snapshot Provenance Contract

Pipeline 184 carries the established snapshot provenance contract into the new
answer surface.

Required provenance fields:

- `required_snapshot_input`
- `snapshot_id`
- `snapshot_drift_detected`
- `governance_state_consensus`

Meaning:

- `required_snapshot_input` declares the canonical snapshot authority surface
- `snapshot_id` ties the answer to one immutable governance-state snapshot
- `snapshot_drift_detected` shows whether the answer is bound to drift-free
  current state
- `governance_state_consensus` records that the answer comes from aligned
  canonical governance surfaces under the existing selector authority model
