# Drift Detection Design

Initial drift handling is detect-and-record only.

Pipeline 180 records:

- `previous_snapshot_id`
- `drift_detected`

Drift semantics:

- if no prior snapshot manifest exists, `previous_snapshot_id` is `null` and
  `drift_detected` is `false`
- if the prior `snapshot_id` matches the newly computed snapshot, drift is not
  detected
- if the prior `snapshot_id` differs, drift is detected and recorded in the new
  snapshot manifest and selector output

This design preserves deterministic execution while creating an auditable seam
for stronger protected-drift enforcement in a later pipeline.
