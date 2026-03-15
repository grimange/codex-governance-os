# Required Snapshot Dependency Model

Pipeline 182 establishes this dependency rule:

- `docs/governance/governance-state-snapshot.json` is the required canonical
  state envelope for authoritative current-state consumption.
- Supported authoritative consumers must carry snapshot provenance.
- Missing or invalid snapshot linkage prevents an authoritative current-state
  answer.

Mandatory propagated provenance for supported authoritative consumers:

- `required_snapshot_input`
- `snapshot_id`
- `snapshot_drift_detected`
- `governance_state_consensus`

Current implementation scope:

- `docs/governance/governance-system-next-action.json`
