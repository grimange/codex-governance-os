# Problem Statement

Layer 6 session governance already defines how governed session truth is
reconstructed from the registry, ledger, state machine, lifecycle observation,
runtime-boundary evidence, and interpretation model.

What remained implicit was how to verify that a claimed reconstructed session
narrative actually obeys those authorities.

Pipeline `124` closes that gap by establishing one doctrine-level verification
harness that:

- validates reconstructed narratives without reconstructing them
- preserves Layer 6 authority precedence
- checks state-machine conformance and ledger consistency
- requires one deterministic bounded narrative per evidence set
- fails closed when evidence is missing, contradictory, or ambiguous
