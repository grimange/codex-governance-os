# Problem Statement

Pipelines `134` and `135` established and verified canonical multi-session
continuity scenarios, but the repository still lacked an executable harness
capable of evaluating them deterministically.

Pipeline `136` closes that gap by implementing a read-only governance tool
that:

- loads the canonical scenario fixtures
- classifies admissible continuity evidence
- enforces strict per-session isolation
- emits machine-readable evaluation results
