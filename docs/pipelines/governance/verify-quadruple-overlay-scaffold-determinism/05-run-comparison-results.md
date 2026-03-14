# Run Comparison Results

## Run Count

- two isolated scaffold realizations within the determinism harness

## Comparison Outcome

- `scaffold-selection.json` payloads matched exactly
- generated file and directory trees hashed identically
- no overlay ordering instability was observed
- no created-surface drift was observed between the two runs

## Result

The certified quadruple-overlay scaffold is deterministic under repeated
generation.

Supporting suite result:

- `python -m unittest tests.governance.test_template_quadruple_overlay_determinism tests.governance.test_quadruple_overlay_composition tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift`
  - `Ran 12 tests ... OK`
