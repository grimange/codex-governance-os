# Verification Method

The governance harness performs this sequence for each certified triplet:

1. realize scaffold in temp directory `A`
2. realize scaffold in temp directory `B`
3. compare `scaffold-selection.json` payloads for exact equality
4. hash both generated trees and compare the hashes

The determinism test is implemented in
[test_template_triple_overlay_determinism.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_triple_overlay_determinism.py).
