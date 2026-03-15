# Selector Metadata Verification

The selector was executed twice on canonical state via:

```bash
python tools/governance/inspect_governance_state.py next-action
python tools/governance/inspect_governance_state.py next-action
```

Verified selector metadata in `docs/governance/governance-system-next-action.json`:

- `snapshot_id`:
  - `8f0c678dfb75779f5b2cff1bb55c05fccf9012bb7bede3f0128be99eb0e6c0df`
- `snapshot_drift_detected`:
  - `false`
- `governance_state_consensus`:
  - `true`

Selector output determinism:

- first hash:
  - `af23562fb0b39cc3f0b54cbec145dff26c7202ff9c31dbe8c404a7cf37d172dc`
- second hash:
  - `af23562fb0b39cc3f0b54cbec145dff26c7202ff9c31dbe8c404a7cf37d172dc`
- result:
  - deterministic selector output confirmed
