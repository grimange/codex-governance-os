# Verification

Verified outcomes for Pipeline 187:

1. `python3 tools/governance/inspect_governance_state.py authoritative-state`
   emits deterministic authoritative output on valid snapshot-backed inputs.
2. Provenance fields remain present on valid baseline output:
   - `required_snapshot_input=docs/governance/governance-state-snapshot.json`
   - `snapshot_id=8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df`
   - `snapshot_drift_detected=false`
   - `governance_state_consensus=true`
3. Missing snapshot fails closed with
   `MISSING_CANONICAL_GOVERNANCE_SURFACE`.
4. Structurally invalid snapshot fails closed with
   `INVALID_GOVERNANCE_STATE_SNAPSHOT`.
5. Canonical mismatch fails closed with
   `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`.
6. Pre-marked drifted snapshot fails closed with
   `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`.
7. Across all negative paths, the authoritative-state command does not
   regenerate or repair the snapshot for itself.
8. After restoration, authoritative-state returned to the exact baseline hash
   `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`.
9. Regression checks passed:
   - targeted `pytest`: `18 passed in 0.16s`
   - full governance suite: `Ran 135 tests in 8.171s`, `OK`

Verification classification:

- baseline determinism:
  VERIFIED
- missing snapshot hard block:
  VERIFIED
- invalid snapshot hard block:
  VERIFIED
- canonical mismatch hard block:
  VERIFIED
- drifted snapshot hard block:
  VERIFIED
- no self-regeneration:
  VERIFIED
- restoration stability:
  VERIFIED
- regression safety:
  VERIFIED
