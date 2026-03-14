# Supportability Decision

`LARAVEL_CLI_WORKER_COMPOSITION_EXPLICITLY_UNSUPPORTED`

## Decision Basis

The current rejection should remain explicit and fail-closed.

This is not just a missing compatibility declaration. The pair lacks a bounded composition model for:

- entrypoint ownership
- command-surface ownership
- worker lifecycle ownership
- directory placement and scaffold semantics

## What Would Need To Exist Before Support Work

If the repository later chooses to pursue support, the follow-on implementation lane would need to define a new Laravel-specific worker composition contract before any manifest admission:

- Laravel worker execution model, likely centered on `artisan`
- deterministic placement for worker surfaces inside a Laravel repository
- replacement or remapping rules for `bin`, `jobs`, and `worker`
- verification coverage proving contract, manifests, scaffold, docs, and tests all agree

That is a new composition design effort, not a small compatibility patch.

## Governance Consequence

The correct next lane, if any, is to codify the boundary explicitly rather than implement support immediately.
