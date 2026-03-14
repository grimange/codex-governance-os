# Governance Test Coverage

Dedicated drift-verification coverage was added in [test_template_composition_drift.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_drift.py).

It verifies:

- the live snapshot matches runtime and manifest surfaces
- snapshot drift is detected when an unsupported supported-pair is injected
- rejection-reason drift is detected when the snapshot reason is changed
- the CLI verifier reports success for the live repository state

This complements the existing contract drift, matrix, and surface-consistency suites rather than replacing them.
