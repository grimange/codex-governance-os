# Governance Verdict Family Classification Canon

This canon governs how governance final verdict strings are mapped into verdict families for analytics and reporting.

## Purpose

The repository contains historical final verdict strings that are not uniform enough for informal grouping.

This document makes classification deterministic so all analytics and future interpretation use one canonical mapping.

## Canonical Family Set

- `VERIFIED`
- `ESTABLISHED`
- `NORMALIZED`
- `IMPLEMENTED`
- `WITH_LIMITATIONS`
- `WITH_GAPS`
- `RESTRICTED`
- `OTHER`

## Deterministic Mapping Rules

Apply the first matching rule in order:

1. If the verdict string contains `_WITH_GAPS`, family is `WITH_GAPS`.
2. If the verdict string matches `_WITH_(LIMITATIONS|LIMITATION|RESTRICTION|RESTRICTIONS)`, family is `WITH_LIMITATIONS`.
3. If the verdict string contains token `NORMALIZED`, family is `NORMALIZED`.
4. If the verdict string contains `VERIFIED`, family is `VERIFIED`.
5. If the verdict string contains token `ESTABLISHED`, family is `ESTABLISHED`.
6. If the verdict string contains `_IMPLEMENTED`, family is `IMPLEMENTED`.
7. If the verdict string contains `_RESTRICTED`, family is `RESTRICTED`.
8. Otherwise family is `OTHER`.

## Analytics Rule

`docs/governance/pipeline-run-analytics.md` must derive verdict-family counts by applying this canon directly to every `pipeline_run_ledger.md` final verdict.
