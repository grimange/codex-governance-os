# Trend Classification Verification

## Allowed Trend Classes

The history surface defines these bounded classifications:

- `newly established`
- `improving`
- `unchanged`
- `regressing`
- `recalibrated with explanation`

## Rule Verification

The surface explicitly constrains trend assignment to score-based conditions:

- `newly established` only for the first canonical observation
- `improving` only when current score is higher than prior score
- `unchanged` only when current score matches prior score
- `regressing` only when current score is lower than prior score
- `recalibrated with explanation` only when a governance pipeline changes the
  scoring basis and documents the reason

## Current Entry Check

The current single observation uses `newly established`, which is correct
because no prior canonical maturity score exists in repository evidence.

## Result

Trend classification boundaries are explicit, conservative, and deterministic.
