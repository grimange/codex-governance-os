# Canon Integrity Check

## Inputs Inspected

- `docs/governance/session-reconstruction-case-verification-model.md`
- `docs/governance/session-reconstruction-verification-harness.md`
- `docs/governance/codex-session-reconstruction-rules.md`

## Findings

- The case-model canon defines each reconstruction case as a bounded
  evaluation package for one canonical `session_id`.
- The canon explicitly prohibits combining evidence from multiple governed
  sessions into one evaluation unit.
- The case-model canon requires explicit declaration of:
  - reconstruction scope
  - verification objective
  - evaluation timestamp
  - evaluator context
  - evidence sources
  - assumptions, inference boundaries, and ambiguity markers when needed
- The canon introduces no runtime execution tooling, automated reconstruction,
  or governance mutation authority.
- The canon remains a documentation-level structure model for harness inputs
  rather than a replacement evaluation engine.

## Classification

- single-session anchoring preserved: `VERIFIED`
- bounded case structure present: `VERIFIED`
- multi-session aggregation permitted: `NOT OBSERVED`
- runtime authority introduced: `NOT OBSERVED`
- governance mutation authority introduced: `NOT OBSERVED`
