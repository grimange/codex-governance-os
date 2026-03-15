# Execution Log

Commands executed:

```bash
python tools/governance/inspect_governance_state.py next-action
python tools/governance/inspect_governance_state.py next-action
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Bounded mutation sequence:

1. captured valid baseline on intact snapshot
2. moved `docs/governance/governance-state-snapshot.json` aside and ran selector
3. restored snapshot
4. replaced snapshot with bounded invalid structure and ran selector
5. restored snapshot
6. mutated `docs/governance/governance-system-advancement-roadmap.json` without regenerating snapshot and ran selector
7. restored roadmap
8. marked snapshot `drift_detected: true` and ran selector
9. restored snapshot
10. reran valid baseline and regression suite

Observed evidence:

- valid baseline status:
  - `0`
- valid baseline next-action hash before run:
  - `333eefb5f08215591748949bf4d10f54da8e1a03efde2241e823fb65d5a2aabd`
- valid baseline next-action hash after run:
  - `333eefb5f08215591748949bf4d10f54da8e1a03efde2241e823fb65d5a2aabd`
- missing snapshot status:
  - `1`
- missing snapshot file recreated by selector:
  - `no`
- missing snapshot error:
  - `MISSING_CANONICAL_GOVERNANCE_SURFACE`
- invalid snapshot status:
  - `1`
- invalid snapshot error:
  - `INVALID_GOVERNANCE_STATE_SNAPSHOT`
- mismatch status:
  - `1`
- mismatch error:
  - `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`
- drifted snapshot status:
  - `1`
- drifted snapshot error:
  - `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`
- restored baseline status:
  - `0`
- restored baseline next-action hash:
  - `333eefb5f08215591748949bf4d10f54da8e1a03efde2241e823fb65d5a2aabd`
