# Execution Log

## Preflight

Command:

```bash
python3 tools/governance/preflight.py
```

Observed result:

```text
governance_preflight
check: portability_reference_scan
decision: PASS
scope: active_governed_surfaces
scanned_files: 251
violations: 0
exceptions: 39
```

## Baseline Setup

Commands:

```bash
python3 tools/governance/inspect_governance_state.py snapshot
python3 tools/governance/inspect_governance_state.py next-action
python3 tools/governance/inspect_governance_state.py authoritative-state
sha256sum docs/governance/governance-authoritative-state-answer.json \
  docs/governance/governance-system-next-action.json \
  docs/governance/governance-state-snapshot.json
```

Observed hashes:

- authoritative answer:
  `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`
- selector:
  `333eefb5f08215591748949bf4d10f54da8e1a03efde2241e823fb65d5a2aabd`
- snapshot:
  `7ddb7c3a3c637ecd8f5690232b2075481155acf44c0af6e8438be0a7a07870c5`

Baseline provenance observed in the authoritative answer:

- `required_snapshot_input`:
  `docs/governance/governance-state-snapshot.json`
- `snapshot_id`:
  `8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df`
- `snapshot_drift_detected`:
  `false`
- `governance_state_consensus`:
  `true`

## Baseline Determinism

Command:

```bash
python3 tools/governance/inspect_governance_state.py authoritative-state
```

Observed result:

- repeat authoritative hash matched baseline exactly:
  `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`
- `cmp` against baseline returned exit `0`

## Negative Path: Missing Snapshot

Procedure:

- move `docs/governance/governance-state-snapshot.json` to a temporary path
- run `authoritative-state`
- confirm the snapshot file does not reappear during the run
- restore the snapshot file

Observed result:

```json
{
  "status": "error",
  "error_code": "MISSING_CANONICAL_GOVERNANCE_SURFACE",
  "message": "Required canonical governance surface is missing: docs/governance/governance-state-snapshot.json",
  "allowed_surfaces": [
    "docs/governance/governance-state-snapshot.json",
    "docs/governance/governance-system-state.json",
    "docs/governance/governance-system-maturity.json",
    "docs/governance/governance-system-gaps.json",
    "docs/governance/governance-system-gap-remediation-plan.json",
    "docs/governance/governance-system-advancement-roadmap.json"
  ]
}
```

- command exit:
  `1`
- snapshot existed after run:
  `false`

## Negative Path: Structurally Invalid Snapshot

Procedure:

- back up the snapshot
- replace it with `{"snapshot_id":"broken"}`
- run `authoritative-state`
- confirm the invalid snapshot is not rewritten to canonical content during the run
- restore the snapshot

Observed result:

```json
{
  "status": "error",
  "error_code": "INVALID_GOVERNANCE_STATE_SNAPSHOT",
  "message": "Governance state snapshot is missing required fields: drift_detected, surfaces",
  "allowed_surfaces": [
    "docs/governance/governance-state-snapshot.json",
    "docs/governance/governance-system-state.json",
    "docs/governance/governance-system-maturity.json",
    "docs/governance/governance-system-gaps.json",
    "docs/governance/governance-system-gap-remediation-plan.json",
    "docs/governance/governance-system-advancement-roadmap.json"
  ]
}
```

- command exit:
  `1`
- snapshot repaired during run:
  `false`

## Negative Path: Canonical Mismatch

Procedure:

- mutate `docs/governance/governance-system-state.json`
  (`trend_classification: p187_mismatch_probe`)
- do not regenerate the snapshot
- run `authoritative-state`
- restore the canonical state file

Observed result:

```json
{
  "status": "error",
  "error_code": "GOVERNANCE_STATE_SNAPSHOT_MISMATCH",
  "message": "Governance state snapshot does not match current canonical governance surfaces",
  "allowed_surfaces": [
    "docs/governance/governance-state-snapshot.json",
    "docs/governance/governance-system-state.json",
    "docs/governance/governance-system-maturity.json",
    "docs/governance/governance-system-gaps.json",
    "docs/governance/governance-system-gap-remediation-plan.json",
    "docs/governance/governance-system-advancement-roadmap.json"
  ]
}
```

- command exit:
  `1`

## Negative Path: Pre-Marked Drifted Snapshot

Procedure:

- back up the snapshot
- set `drift_detected: true`
- run `authoritative-state`
- confirm the snapshot is not repaired during the run
- restore the snapshot

Observed result:

```json
{
  "status": "error",
  "error_code": "GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED",
  "message": "Governance state snapshot is marked drifted and cannot authorize current-state answers",
  "allowed_surfaces": [
    "docs/governance/governance-state-snapshot.json",
    "docs/governance/governance-system-state.json",
    "docs/governance/governance-system-maturity.json",
    "docs/governance/governance-system-gaps.json",
    "docs/governance/governance-system-gap-remediation-plan.json",
    "docs/governance/governance-system-advancement-roadmap.json"
  ]
}
```

- command exit:
  `1`
- snapshot repaired during run:
  `false`

## Restoration Stability

Command:

```bash
python3 tools/governance/inspect_governance_state.py authoritative-state
```

Observed result:

- authoritative hash after restoration:
  `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`
- snapshot hash after restoration:
  `7ddb7c3a3c637ecd8f5690232b2075481155acf44c0af6e8438be0a7a07870c5`
- `cmp` against baseline:
  - authoritative:
    exit `0`
  - snapshot:
    exit `0`

## Regression Results

Targeted command:

```bash
python3 -m pytest tests/governance/test_governance_system_next_action.py
```

Observed result:

```text
18 passed in 0.16s
```

Full-suite command:

```bash
python3 -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed result:

```text
Ran 135 tests in 8.171s

OK
```
