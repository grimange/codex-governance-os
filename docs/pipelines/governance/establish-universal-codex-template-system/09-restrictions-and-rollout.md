# Restrictions And Rollout

## Restrictions Preserved

- no silent repository-wide rewrites
- no weakening overlays
- no bypass of fail-closed semantics
- no claim that all historical governance artifacts already conform
- no claim of multi-stack safety beyond the implemented deterministic tests

## Rollout Model

The implemented system remains in advisory-then-enforcing mode:

1. registry, linter, and scaffold exist
2. current verification proves deterministic baseline behavior
3. future verification lanes across representative fixtures must run before hard enforcement
