# Determinism Harness Definition

The dedicated harness for this lane is:

- [test_template_quadruple_overlay_determinism.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_quadruple_overlay_determinism.py)

## Harness Rules

- realize the certified quadruple stack twice
- compare `scaffold-selection.json` payloads byte-for-byte after JSON load
- hash the full generated tree for each run
- assert the two hashes are identical

The hashing strategy mirrors the existing triple-overlay determinism harness so
quadruple verification uses the same evidence model.
