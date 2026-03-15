# Verification

Positive control provenance observed on the authoritative consumer:

- `required_snapshot_input`:
  - `docs/governance/governance-state-snapshot.json`
- `snapshot_id`:
  - `8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df`
- `snapshot_drift_detected`:
  - `false`
- `governance_state_consensus`:
  - `true`

Regression results:

- command:
  - `python -m unittest discover -s tests/governance -p 'test_*.py'`
- result:
  - `Ran 135 tests in 7.942s`
  - `OK`

Verification conclusion:

- authoritative governance next-action output now fails closed on missing,
  invalid, mismatched, and drifted snapshot conditions and resumes normal
  behavior after canonical restoration.
