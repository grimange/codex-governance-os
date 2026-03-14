# Scaffold And Matrix Impact Analysis

## Matrix Clarity

The matrix can express monorepo compounds cleanly because each candidate is a
single explicit three-overlay admission:

- `laravel + monorepo + scheduler`
- `django + monorepo + scheduler`

This does not require hidden conditional rules if each compound is admitted
individually.

## Scaffold Precondition

The current scaffold engine is not yet sufficient for these compounds as-is.

Evidence:

- [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
  resolves at most one `composition_override` per overlay at realization time
- framework manifests currently define separate pairwise overrides for
  `scheduler` and `monorepo`

That means a three-overlay framework compound cannot yet merge:

- monorepo placement
- framework-native scheduler surfaces

without a new explicit compound contract or richer override-merging logic.

## Conclusion

Monorepo compounds are supportable, but not by matrix admission alone. A follow-up
implementation lane must:

1. define the canonical placed framework-native scheduler surfaces under the
   monorepo root
2. extend scaffold realization to support deterministic compound override
   behavior
3. add tests that verify both placement and scheduler authority together

Worker compounds would require more than this. They would need a new ownership
model explaining how framework entrypoints, worker runtime, and scheduler
authority coexist without conflict.
