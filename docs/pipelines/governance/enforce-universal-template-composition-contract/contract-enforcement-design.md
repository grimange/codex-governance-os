# Contract Enforcement Design

## Centralization Rule

Composition enforcement is centralized in `tools/templates/composition_contract.py`.

## Design Decisions

- Base-only and single-overlay realization are admitted explicitly.
- Multi-overlay composition is allowlisted by the certified matrix.
- Known rejected combinations carry deterministic reasons.
- Unknown multi-overlay combinations default to unsupported.
- Manifest inspection validates both directions:
  - unsupported declared pairs are rejected
  - certified pairs missing from manifests are rejected

## Fail-Closed Behavior

- scaffold realization aborts before writing any files when a composition is unsupported
- manifest inspection returns a non-zero exit code when manifest declarations drift from the certified boundary
- structured JSON failure output is emitted for inspection commands using `--output json`
