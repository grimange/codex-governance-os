# Governance Maturity Trend Tracking

This document is the canonical temporal governance maturity surface for
`codex-governance-os`.

It records historical maturity observations derived from the canonical current
scorecard and supporting verification artifacts. It does not replace
`docs/governance/governance-maturity-scorecard.md`, which remains the canonical
current-state surface.

## Current Reading

- Latest observation date: `2026-03-15`
- Latest maturity score: `84%`
- Latest prior score: `none`
- Latest delta: `none`
- Latest trend classification: `newly established`
- Latest evidence basis:
  - `docs/governance/governance-maturity-scorecard.md`
  - `docs/pipelines/governance/verify-governance-maturity-scoring-surface/07-final-verdict.md`

## Historical Record

### Observation 1

- Observation Date: `2026-03-15`
- Maturity Score: `84%`
- Prior Score: `none`
- Delta: `none`
- Trend: `newly established`
- Evidence Basis:
  - Pipeline 149 scorecard establishment
  - Pipeline 150 verification outcome
  - `docs/governance/governance-maturity-scorecard.md`
  - `docs/pipelines/governance/verify-governance-maturity-scoring-surface/07-final-verdict.md`
- Notes:
  - This is the first canonical maturity history entry in repository state.
  - The score is taken from the established and verified maturity scorecard.
  - No earlier canonical maturity reading exists in repository evidence, so no
    prior score or trend delta is asserted.
  - Interpretation depth is limited until additional maturity-affecting
    governance events produce later observations.

## Trend Interpretation Rules

- `newly established`
  - use when the first canonical maturity observation is recorded and no prior
    evidence-backed score exists
- `improving`
  - use only when the current score is higher than the prior recorded score
- `unchanged`
  - use only when the current score matches the prior recorded score
- `regressing`
  - use only when the current score is lower than the prior recorded score
- `recalibrated with explanation`
  - use only when the scoring model or canonical interpretation basis changes
    through a recorded governance pipeline and the change is explicitly
    documented

Trend labels describe observed score movement only. They do not imply long-term
stability, irreversible maturity gain, or unsupported causality.

## Known Limitations

- Only one canonical maturity observation currently exists.
- Trend direction beyond `newly established` cannot yet be inferred from a
  single record.
- The current trend surface depends on future governance pipelines to append new
  observations when maturity-affecting evidence changes.
- The scorecard remains bounded by explicit unresolved historical gaps and
  limitation-family runs already documented in the current maturity surface.

## Change Recording Discipline

Add a new maturity history entry only when one or more of the following occur:

- a new governance maturity score is established
- a verified governance pipeline materially changes maturity-relevant capability
  coverage
- a structural blocker affecting maturity is explicitly closed
- the scoring model is formally recalibrated through a governance pipeline

Do not add a new entry for:

- cosmetic document edits
- repeated restatement of the same score without a governance event
- unsupported intuition about maturity movement
- unverified claims of improvement or regression

Prior history entries are append-only and must not be silently rewritten.
