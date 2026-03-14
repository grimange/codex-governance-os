# Restriction Analysis

The restrictions recorded in pipeline `096` are now resolved at the pipeline
definition level.

Resolved drift items:

- contract path mismatch
- template path mismatch
- registry-schema overexpectation
- `095` artifact filename mismatch in `096`
- next recommended pipeline numbering drift

Residual note:

- the historical `096` verification bundle remains unchanged by design, because
  this lane normalizes the verification definition rather than rewriting prior
  evidence

That residual note is not an active restriction. It is preservation of
historical evidence.

Result: `RESTRICTIONS_RESOLVED_WITH_HISTORICAL_EVIDENCE_PRESERVED`
