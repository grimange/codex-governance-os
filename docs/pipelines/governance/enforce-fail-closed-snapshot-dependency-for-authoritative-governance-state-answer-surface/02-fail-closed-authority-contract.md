# Fail-Closed Authority Contract

The authoritative governance state answer surface is authoritative only when all
of the following are true:

- `docs/governance/governance-state-snapshot.json` exists
- the snapshot contains the required fields `snapshot_id`, `drift_detected`, and
  `surfaces`
- the snapshot surface hashes match the current canonical governed surfaces
- the snapshot is not already marked drifted
- canonical governance input authority checks pass for the state, maturity,
  gaps, remediation-plan, and roadmap surfaces

Blocked conditions for the authoritative answer surface are:

- missing snapshot
- structurally invalid snapshot
- snapshot mismatch against canonical surfaces
- drifted snapshot
- canonical-input authority or consensus violations

Machine-readable failure family:

- `MISSING_CANONICAL_GOVERNANCE_SURFACE`
- `INVALID_GOVERNANCE_STATE_SNAPSHOT`
- `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`
- `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`
- existing canonical-input authority and consensus violations

Prohibited behavior:

- silent raw-source fallback
- self-regeneration of the snapshot during authoritative-state execution
- emitting a normal authoritative governance-state answer when the snapshot
  contract is broken

Authoritative output is emitted only after `validate_canonical_input_authority()`
passes.
