# Negative-Path Test Matrix

| Case | Setup | Expected Result | Observed Result | Status |
| --- | --- | --- | --- | --- |
| Valid baseline | Run `authoritative-state` twice on intact canonical state | Identical payload and hash; provenance fields present | baseline hash `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`; repeat hash identical; `cmp` exit `0` | VERIFIED |
| Missing snapshot | Temporarily move `docs/governance/governance-state-snapshot.json` out of place | Hard block; snapshot not regenerated | error `MISSING_CANONICAL_GOVERNANCE_SURFACE`; command exit `1`; snapshot existence check after run returned false | VERIFIED |
| Invalid snapshot | Replace snapshot with `{"snapshot_id":"broken"}` | Hard block; no normalization or repair | error `INVALID_GOVERNANCE_STATE_SNAPSHOT`; command exit `1`; mutated snapshot remained different from backup during run | VERIFIED |
| Canonical mismatch | Mutate `docs/governance/governance-system-state.json` without regenerating snapshot | Hard block with mismatch evidence | error `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`; command exit `1` | VERIFIED |
| Drifted snapshot | Mark `drift_detected: true` in snapshot | Hard block; no authoritative output | error `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`; command exit `1`; mutated snapshot remained different from backup during run | VERIFIED |
| No self-regeneration | Observe all negative-path cases | Snapshot is never recreated or repaired by `authoritative-state` | no scenario recreated missing snapshot or rewrote invalid/drifted snapshot to canonical state | VERIFIED |
| Restoration stability | Restore canonical state and rerun `authoritative-state` | Original baseline hash restored exactly | authoritative hash returned to `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`; snapshot hash returned to `7ddb7c3a3c637ecd8f5690232b2075481155acf44c0af6e8438be0a7a07870c5`; `cmp` exits `0` | VERIFIED |
| Targeted regression | Run `python3 -m pytest tests/governance/test_governance_system_next_action.py` | Targeted authoritative-state and selector tests pass | `18 passed in 0.16s` | VERIFIED |
| Full regression | Run `python3 -m unittest discover -s tests/governance -p 'test_*.py'` | Full suite passes | `Ran 135 tests in 8.171s` and `OK` | VERIFIED |
