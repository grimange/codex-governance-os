# Verification Scope

## Canonical Surfaces Verified

- `docs/governance/governance-authoritative-state-answer.json`
- `docs/governance/governance-state-snapshot.json`
- `docs/governance/governance-system-next-action.json`
- `docs/governance/governance-system-state.json`
- `docs/governance/governance-system-maturity.json`
- `docs/governance/governance-system-gaps.json`
- `docs/governance/governance-system-gap-remediation-plan.json`
- `docs/governance/governance-system-advancement-roadmap.json`
- `tools/governance/inspect_governance_state.py`
- `tests/governance/test_governance_system_next_action.py`

## Verification Criteria

1. Repeated authoritative-state execution on unchanged canonical inputs produces
   byte-identical JSON and the same file hash.
2. The authoritative answer includes:
   - `required_snapshot_input`
   - `snapshot_id`
   - `snapshot_drift_detected`
   - `governance_state_consensus`
3. The embedded `recommended_next_action` payload matches the standalone
   authoritative selector output.
4. A bounded reversible mutation to a snapshot-tracked canonical input causes
   the authoritative-state command to change behavior and fail closed with
   snapshot mismatch evidence when the snapshot is not regenerated.
5. Restoring the mutated canonical input restores the exact baseline hashes for
   the authoritative answer, selector output, and snapshot.
6. The governance regression suite passes after verification.

## Boundary

The proposed pipeline text names
`tools/governance/select_governance_system_next_action.py`, but repository state
does not contain that file. The implemented authoritative selector entrypoint is
`python3 tools/governance/inspect_governance_state.py next-action`, which was
used for this verification because repository state is the higher authority.
