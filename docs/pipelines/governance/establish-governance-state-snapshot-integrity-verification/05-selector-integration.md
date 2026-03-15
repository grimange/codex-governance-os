# Selector Integration

Pipeline 180 updates the next-action selector so that selector execution:

1. validates canonical governance input authority
2. computes the current governance-state snapshot
3. compares against the previous snapshot manifest when present
4. records the resulting `snapshot_id` in
   `docs/governance/governance-system-next-action.json`

Current canonical selector metadata:

- `snapshot_id`:
  - `6f7f70632592360b7e35c29590f71782944138010b51dd1ef4b3e9654852dc80`
- `governance_state_consensus`:
  - `true`
- `snapshot_drift_detected`:
  - `false`
