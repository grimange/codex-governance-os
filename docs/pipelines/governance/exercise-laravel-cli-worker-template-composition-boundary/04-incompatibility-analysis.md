# Incompatibility Analysis

## Direct Manifest Conflict

The pair is not presently composable at the manifest layer:

- `laravel.json` declares no compatible overlays
- `cli-worker.json` does not list `laravel`

That alone blocks admission, but the deeper issue is not just missing declarations.

## Runtime Model Mismatch

Laravel is modeled here as an application/service overlay with root ownership concentrated around:

- `app/`
- `bootstrap/`
- `routes/`
- `config/`
- the implied Laravel command surface centered on `artisan`

CLI-worker is modeled as a primary execution overlay with ownership concentrated around:

- `bin/`
- `jobs/`
- `worker/`
- optional queue and scheduler surfaces

The current universal template system treats a supported pair as one of:

- a straightforward additive surface merge, or
- a composition with an explicit override describing deterministic placement and ownership

`laravel + cli-worker` has neither.

## Root Ownership And Entrypoint Ambiguity

To make this pair supportable, the scaffold would need to answer questions that are currently unspecified:

- Is the worker invoked through Laravel itself, such as a bounded `php artisan ...` command?
- Does `bin/` remain a first-class root surface, or does Laravel own command dispatch entirely through `artisan`?
- Does `jobs/worker` map into Laravel queue infrastructure, or into a parallel worker runtime beside the framework?
- Which overlay owns runtime bootstrap, dependency shape, and process lifecycle?

Those are not cosmetic scaffold questions. They define the composition contract.

## Why Existing Supported Pairs Are Different

Current supported `cli-worker` pairs all have cleaner ownership boundaries:

- `cli-worker + python-package`
  - package surfaces plus CLI/worker surfaces can coexist without framework-root collision
- `cli-worker + php-package`
  - package layout admits CLI surfaces without a competing framework application root
- `cli-worker + node-typescript-service`
  - service and worker surfaces share a script/package-managed process model
- `cli-worker + monorepo`
  - monorepo provides segregation by placement

Laravel does not currently offer an equivalent composition override or segregated placement model.

## Supportability Assessment

A future Laravel worker integration is possible in principle, but only if the repository first defines a Laravel-specific worker contract such as:

- Laravel-owned worker execution through `artisan`
- deterministic placement for queue/worker surfaces inside the Laravel application
- explicit mapping of `bin/jobs/worker` expectations onto Laravel queue and command primitives

Without that new contract, admitting the pair would weaken the current invariant that supported compositions have deterministic ownership and scaffold semantics.
