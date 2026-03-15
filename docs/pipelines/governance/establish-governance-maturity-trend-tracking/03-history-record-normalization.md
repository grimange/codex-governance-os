# History Record Normalization

Each maturity history entry uses the same normalized fields:

- Observation Date
- Maturity Score
- Prior Score
- Delta
- Trend
- Evidence Basis
- Notes

## Initial Record Policy

If only one canonical maturity reading exists, the first entry must:

- use the verified current maturity score
- set `Prior Score` to `none`
- set `Delta` to `none`
- use trend classification `newly established`
- explain that no earlier canonical maturity observation exists

## Append-Only Rule

History entries are additive. Later observations append new entries rather than
rewriting prior state.
