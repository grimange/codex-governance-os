# Verification Plan

Pipeline 187 should verify the enforced contract through the implemented
canonical entrypoints.

## Positive Control

1. Run:
   `python3 tools/governance/inspect_governance_state.py authoritative-state`
2. Confirm the canonical authoritative answer is emitted successfully on valid
   snapshot-backed state.
3. Re-run on unchanged inputs and confirm deterministic output.

## Negative Paths

1. Missing snapshot:
   remove `docs/governance/governance-state-snapshot.json` temporarily and
   confirm `authoritative-state` fails closed without recreating the file.
2. Invalid snapshot:
   replace the snapshot with malformed or incomplete JSON and confirm
   `INVALID_GOVERNANCE_STATE_SNAPSHOT`.
3. Snapshot mismatch:
   mutate a snapshot-tracked canonical input without regenerating the snapshot
   and confirm `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`.
4. Drifted snapshot:
   mark `drift_detected: true` in the snapshot and confirm
   `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`.

## Command-Surface Verification

1. Confirm verification and documentation reference:
   - `python3 tools/governance/inspect_governance_state.py next-action`
   - `python3 tools/governance/inspect_governance_state.py authoritative-state`
2. Confirm no verification step relies on a non-existent standalone selector
   script.

## Regression Verification

Run:

```bash
python3 -m unittest discover -s tests/governance -p 'test_*.py'
```

Confirm the governance suite passes after the hardening changes.
