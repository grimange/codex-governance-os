# Governance Maturity Scorecard

This scorecard is a derived governance reporting surface for `codex-governance-os`.
It interprets repository governance maturity from the canonical inputs below and
does not mutate them:

- `docs/governance/pipeline-run-ledger.md`
- `docs/governance/pipeline-run-analytics.md`
- `docs/governance/verdict-family-classification-canon.md`

## Source Evidence Snapshot

- Total recorded runs: `60`
- Positive execution-signal families: `37`
  - `IMPLEMENTED`: `3`
  - `ESTABLISHED`: `14`
  - `VERIFIED`: `16`
  - `NORMALIZED`: `4`
- Bounded safety-signal families: `11`
  - `WITH_LIMITATIONS`: `10`
  - `WITH_GAPS`: `1`
  - `RESTRICTED`: `0`
- Backfilled historical runs: `55`
- Explicit unresolved historical gaps: `6`
- Required intelligence surfaces present: `3/3`
  - ledger
  - analytics
  - verdict-family canon

## Scoring Rules

### 1. Governance Execution

Measures how much of recorded governance history lands in execution-positive
families.

Formula:

`(IMPLEMENTED + ESTABLISHED + VERIFIED + NORMALIZED) / total recorded runs`

Score:

`37 / 60 = 61.67%`, rounded to `62%`

Interpretation:

Execution maturity is established but incomplete. Most recorded runs resolve
into positive execution families, but `23` runs still land outside those
families because they are bounded (`WITH_LIMITATIONS`, `WITH_GAPS`) or remain
non-execution `OTHER` verdicts.

### 2. Governance Safety

Measures the share of recorded history that is not currently bounded by
limitation or gap verdict families.

Formula:

`(total recorded runs - (WITH_LIMITATIONS + WITH_GAPS + RESTRICTED)) / total recorded runs`

Score:

`(60 - 11) / 60 = 81.67%`, rounded to `82%`

Interpretation:

Safety maturity is relatively strong because most recorded runs are not bounded
by limitation-oriented verdict families. The remaining `11` bounded runs are
explicit governance risk signals, not hidden debt.

### 3. Governance Coverage

Measures how complete governance memory is for historical pipeline activity.

Formula:

`backfilled historical runs / (backfilled historical runs + explicit unresolved historical gaps)`

Score:

`55 / (55 + 6) = 90.16%`, rounded to `90%`

Interpretation:

Coverage maturity is high but not complete. Repository governance memory is
mostly centralized, yet `6` unresolved historical gaps still bound full
historical completeness.

### 4. Governance Intelligence

Measures whether the repository has the minimum deterministic interpretation
layers required for maturity reporting.

Formula:

`present required intelligence surfaces / 3`

Required surfaces:

- `docs/governance/pipeline-run-ledger.md`
- `docs/governance/pipeline-run-analytics.md`
- `docs/governance/verdict-family-classification-canon.md`

Score:

`3 / 3 = 100%`

Interpretation:

The repository now has the canonical memory surface, derived analytics surface,
and deterministic verdict taxonomy required for repeatable governance maturity
reporting.

## Scorecard Summary

| Dimension | Score | Evidence Basis |
|---|---:|---|
| Governance Execution | `62%` | analytics verdict-family distribution and total recorded runs |
| Governance Safety | `82%` | analytics bounded-family counts and total recorded runs |
| Governance Coverage | `90%` | analytics historical coverage and explicit ledger gaps |
| Governance Intelligence | `100%` | presence of ledger, analytics, and canon inputs |

Overall maturity score:

`(62 + 82 + 90 + 100) / 4 = 83.5%`, rounded to `84%`

## Remaining Governance Gaps

- Historical governance memory still contains `6` explicit unresolved gaps.
- `11` recorded runs remain in bounded verdict families and continue to signal
  governance limitations or incomplete closure.
- `12` runs remain in the analytics `OTHER` family, which means they do not yet
  contribute to the four positive execution families used by this scorecard.

## Current Maturity Reading

The repository has a deterministic governance maturity surface and scores as
materially established. The strongest area is governance intelligence because
the canonical interpretation stack now exists end to end. The main maturity
constraint is not missing scoring infrastructure, but incomplete historical
closure and the remaining bounded run population preserved by the ledger and
analytics surfaces.
