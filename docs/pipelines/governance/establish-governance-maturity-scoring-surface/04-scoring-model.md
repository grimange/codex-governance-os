# Scoring Model

All scores are bounded to `0-100%` and rounded to the nearest whole percent.

## Governance Execution

Formula:

`(IMPLEMENTED + ESTABLISHED + VERIFIED + NORMALIZED) / total recorded runs`

Calculation:

`(3 + 14 + 16 + 4) / 60 = 37 / 60 = 61.67%`

Rounded score:

`62%`

## Governance Safety

Formula:

`(total recorded runs - (WITH_LIMITATIONS + WITH_GAPS + RESTRICTED)) / total recorded runs`

Calculation:

`(60 - (10 + 1 + 0)) / 60 = 49 / 60 = 81.67%`

Rounded score:

`82%`

## Governance Coverage

Formula:

`backfilled historical runs / (backfilled historical runs + explicit unresolved historical gaps)`

Calculation:

`55 / (55 + 6) = 55 / 61 = 90.16%`

Rounded score:

`90%`

## Governance Intelligence

Formula:

`present required intelligence surfaces / 3`

Calculation:

`3 / 3 = 100%`

Rounded score:

`100%`

## Overall Score

Formula:

`(execution + safety + coverage + intelligence) / 4`

Calculation:

`(62 + 82 + 90 + 100) / 4 = 83.5%`

Rounded score:

`84%`
