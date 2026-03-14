# Test Harness

The lane adds a dedicated determinism suite:

- [test_template_triple_overlay_determinism.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_triple_overlay_determinism.py)

The harness:

- realizes each certified triplet twice
- compares the serialized scaffold-selection payloads directly
- computes a stable SHA-256 hash over the generated tree
- asserts identical results across both runs

This turns triple-overlay determinism into an explicit regression contract.
