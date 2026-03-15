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
scanned_files: 249
violations: 0
exceptions: 39
```

## Baseline Generation

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
- selector output:
  `333eefb5f08215591748949bf4d10f54da8e1a03efde2241e823fb65d5a2aabd`
- snapshot:
  `7ddb7c3a3c637ecd8f5690232b2075481155acf44c0af6e8438be0a7a07870c5`

Provenance fields observed in the authoritative answer:

- `required_snapshot_input`:
  `docs/governance/governance-state-snapshot.json`
- `snapshot_id`:
  `8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df`
- `snapshot_drift_detected`:
  `false`
- `governance_state_consensus`:
  `true`

## Determinism Re-Run

Commands:

```bash
python3 tools/governance/inspect_governance_state.py authoritative-state
python3 tools/governance/inspect_governance_state.py next-action
sha256sum docs/governance/governance-authoritative-state-answer.json \
  /tmp/p185-authoritative-baseline.json \
  docs/governance/governance-system-next-action.json \
  /tmp/p185-next-action-baseline.json
cmp -s docs/governance/governance-authoritative-state-answer.json /tmp/p185-authoritative-baseline.json
cmp -s docs/governance/governance-system-next-action.json /tmp/p185-next-action-baseline.json
```

Observed result:

- authoritative answer repeat hash matched baseline exactly
- selector repeat hash matched baseline exactly
- both `cmp` checks returned exit `0`

## Selector Consistency Comparison

Comparison result between
`docs/governance/governance-authoritative-state-answer.json` and
`docs/governance/governance-system-next-action.json`:

- payload equality:
  `true`
- target-domain equality:
  `true`
- status equality:
  `true`
- reason equality:
  `true`
- snapshot-id equality:
  `true`
- normalized embedded selector hash:
  `fb520dc048ccf86fe3a8c160d3385171e3cb60b48947cde0b0d27a3bbff93d97`
- normalized standalone selector hash:
  `fb520dc048ccf86fe3a8c160d3385171e3cb60b48947cde0b0d27a3bbff93d97`

## Mutation Sensitivity

Bounded reversible mutation applied to
`docs/governance/governance-system-state.json`:

- before:
  `trend_classification: newly_established`
- temporary mutation:
  `trend_classification: mutation_test_transient`

Command executed without regenerating the snapshot:

```bash
python3 tools/governance/inspect_governance_state.py authoritative-state
```

Observed fail-closed result:

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

## Restoration Stability

The temporary mutation was reverted so that
`trend_classification` returned to `newly_established`.

Commands:

```bash
python3 tools/governance/inspect_governance_state.py authoritative-state
python3 tools/governance/inspect_governance_state.py next-action
sha256sum docs/governance/governance-authoritative-state-answer.json \
  /tmp/p185-authoritative-baseline.json \
  docs/governance/governance-system-next-action.json \
  /tmp/p185-next-action-baseline.json \
  docs/governance/governance-state-snapshot.json \
  /tmp/p185-snapshot-baseline.json
cmp -s docs/governance/governance-authoritative-state-answer.json /tmp/p185-authoritative-baseline.json
cmp -s docs/governance/governance-system-next-action.json /tmp/p185-next-action-baseline.json
cmp -s docs/governance/governance-state-snapshot.json /tmp/p185-snapshot-baseline.json
```

Observed result:

- authoritative answer hash restored to
  `6f2b9943bab1e2d91f27400e32ecb210ce1174c291a24997e9efef6ea8d490d1`
- selector hash restored to
  `333eefb5f08215591748949bf4d10f54da8e1a03efde2241e823fb65d5a2aabd`
- snapshot hash remained
  `7ddb7c3a3c637ecd8f5690232b2075481155acf44c0af6e8438be0a7a07870c5`
- all three `cmp` checks returned exit `0`

## Regression Suite

Command:

```bash
python3 -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed result:

```text
Ran 135 tests in 7.657s

OK
```
