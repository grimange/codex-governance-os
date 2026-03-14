# Fail-Closed Behavior

The verification harness preserves fail-closed handling for reconstructed
session narratives.

If required evidence is missing, contradictory, non-admissible, or ambiguous:

- verification must not speculate
- verification must not infer missing lifecycle transitions
- verification must not smooth registry summaries over absent ledger history
- verification must not let runtime context redefine canonical session truth

Restricted verification is allowed only when the bounded narrative remains
valid, unique, and explicit about its restrictions.

If ambiguity or contradiction prevents a single bounded narrative from being
verified, the result must be `FAILED`.
