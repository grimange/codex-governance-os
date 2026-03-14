# Recommended Expansion Order

## Recommended Next Sequence

1. `069 — Establish Laravel Monorepo Scheduler Compound Composition Contract`
2. `070 — Verify Laravel Monorepo Scheduler Compound Composition Remains Non-Drifting`
3. `071 — Establish Django Monorepo Scheduler Compound Composition Contract`
4. `072 — Verify Django Monorepo Scheduler Compound Composition Remains Non-Drifting`

## Ordering Rationale

Laravel should open first because its direct framework-native scheduler contract
has the smaller governed scheduler surface set and its monorepo placement is
already canonical and stable.

Django should follow after Laravel because the Django-native scheduler contract
touches a larger governed surface set and benefits from first proving the
compound placement model on the simpler Laravel side.

## Deferred Work

Do not open worker-oriented framework scheduler compounds in this sequence.

- keep `laravel + cli-worker + scheduler` explicitly rejected
- defer `django + cli-worker + scheduler` until a higher-order framework-worker
  composition model exists
- keep four-overlay framework compounds out of scope until the monorepo-first
  sequence is complete and verified
