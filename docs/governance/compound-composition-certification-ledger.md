# Compound Composition Certification Ledger

## Purpose

This ledger is the canonical governance surface for certified compound
composition and fail-closed triple-overlay boundary classification in the
universal template scaffold.

## Scope

This ledger governs only compound overlay composition with three or more
overlays. Pairwise support and explicit pairwise rejection remain governed by
[universal-template-composition-contract.md](../contracts/universal-template-composition-contract.md).

## Certified Compound Compositions

- `cli-worker + monorepo + python-package + scheduler`
- `cli-worker + monorepo + python-package`
- `cli-worker + monorepo + scheduler`
- `cli-worker + python-package + scheduler`
- `laravel + monorepo + scheduler`

## Fail-Closed Triple-Overlay Boundaries

- `django + monorepo + scheduler`
- `django + cli-worker + scheduler`
- `laravel + cli-worker + scheduler`

## Canonical Rules

- only compound compositions listed under `Certified Compound Compositions` are certified
- compound compositions listed under `Fail-Closed Triple-Overlay Boundaries` must remain rejected until a later governance lane changes their status
- unknown triple-overlay combinations fail closed by default
- pairwise support does not imply compound support
- most-specific compound override resolution must remain deterministic and fail closed when ambiguous
