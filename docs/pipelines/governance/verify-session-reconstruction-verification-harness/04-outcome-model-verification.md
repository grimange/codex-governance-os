# Outcome Model Verification

The harness canon defines one explicit bounded outcome model:

- `VERIFIED`
- `VERIFIED_WITH_RESTRICTIONS`
- `FAILED`

Verification findings:

- the output-classification section lists only these three outcomes
- each outcome is bounded by explicit conditions
- `VERIFIED_WITH_RESTRICTIONS` is constrained to cases where the narrative
  remains unique, valid, and explicit about restrictions
- the canon explicitly forbids using restricted verification to excuse:
  - invented events
  - invalid lifecycle transitions
  - unresolved precedence violations
  - unresolved ambiguity
- no additional implicit or soft-success outcome was found

## Classification

- bounded outcome model present: `VERIFIED`
- implicit additional outcomes present: `NOT OBSERVED`
- unrestricted downgrade semantics present: `NOT OBSERVED`
