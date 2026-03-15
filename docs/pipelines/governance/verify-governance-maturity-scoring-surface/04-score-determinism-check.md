# Score Determinism Check

## Published Inputs

- total recorded runs: `60`
- `IMPLEMENTED`: `3`
- `ESTABLISHED`: `14`
- `VERIFIED`: `16`
- `NORMALIZED`: `4`
- `WITH_LIMITATIONS`: `10`
- `WITH_GAPS`: `1`
- `RESTRICTED`: `0`
- backfilled historical runs: `55`
- explicit unresolved historical gaps: `6`
- required intelligence surfaces present: `3`

## Recomputed Scores

### Governance Execution

`(3 + 14 + 16 + 4) / 60 = 37 / 60 = 61.67%`, rounded to `62%`

### Governance Safety

`(60 - (10 + 1 + 0)) / 60 = 49 / 60 = 81.67%`, rounded to `82%`

### Governance Coverage

`55 / (55 + 6) = 55 / 61 = 90.16%`, rounded to `90%`

### Governance Intelligence

`3 / 3 = 100%`

### Overall Maturity

`(62 + 82 + 90 + 100) / 4 = 83.5%`, rounded to `84%`

## Determinism Result

The published `84%` maturity reading is reproducible from the scorecard's
documented method and declared governance inputs. No subjective interpolation is
required to recompute the score.
