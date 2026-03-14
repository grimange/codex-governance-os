# Governance Test Coverage

Dedicated capability coverage was added in [test_template_capability_composition.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_capability_composition.py).

The suite verifies:

- the governed capability registry loads successfully
- supported certified pairs remain supported under capability evaluation
- explicit unsupported pairs preserve their canonical rejection reasons
- role collisions block generic incompatible pairs
- required capability drift is detected
- the live capability model preserves the certified matrix
