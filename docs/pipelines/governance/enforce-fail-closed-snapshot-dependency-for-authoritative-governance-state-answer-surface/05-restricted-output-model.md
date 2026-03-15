# Restricted Output Model

This implementation does not introduce a degraded or restricted non-authoritative
payload model.

Chosen behavior:

- hard block on broken snapshot dependency

Operational semantics:

- `authoritative_output_available` is effectively `false` whenever the command
  exits with a machine-readable error payload
- `restriction_reason` is carried by `error_code` and `message`
- normal authoritative governance-state output is unavailable until the snapshot
  authority contract is restored

Examples of blocked outcomes:

- `MISSING_CANONICAL_GOVERNANCE_SURFACE`
- `INVALID_GOVERNANCE_STATE_SNAPSHOT`
- `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`
- `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`

This preserves a single clear rule: broken snapshot dependency yields no normal
authoritative governance-state answer.
