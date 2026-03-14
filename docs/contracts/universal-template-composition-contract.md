# Universal Template Composition Contract

## Purpose

This contract defines the certified overlay composition boundary for the universal Codex template scaffold.

## Scope

This contract governs:

- which overlay combinations are certified as supported
- which overlay combinations are explicitly fail-closed
- how composition truth is reconciled across manifests, scaffold logic, docs, and tests
- what changes are required before the composition boundary may expand

## Authority Model

Composition truth is determined in this order:

1. `tools/governance/template_scaffold.py`
2. `docs/codex/templates/manifests/*.json`
3. this contract
4. conformance and composition tests under `tests/governance/`

If those surfaces disagree, the repository is in contract drift until a remediation lane restores alignment.

## Canonical Rule

Universal template composition is allowlisted and fail-closed.

No overlay combination is supported unless it is admitted by scaffold compatibility logic, declared in manifests, documented in the certified matrix, and covered by governance verification.

Base-only realization and single-overlay realization remain admitted when the overlay is part of the canonical overlay inventory. The certified matrix below governs multi-overlay composition.

## Certified Supported Multi-Overlay Matrix

The currently certified combinations are:

- base-only
- `cli-worker + monorepo + python-package + scheduler`
- `django + scheduler`
- `django + monorepo`
- `laravel + monorepo`
- `laravel + monorepo + scheduler`
- `service + monorepo`
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + monorepo + scheduler`
- `cli-worker + monorepo + python-package`
- `cli-worker + python-package`
- `cli-worker + python-package + scheduler`
- `cli-worker + scheduler`
- `cli-worker + php-package`
- `laravel + scheduler`
- `monorepo + scheduler`
- `python-package + scheduler`

These combinations are certified because scaffold realization, manifest declarations, repository docs, and governance tests align on the same result.

`cli-worker + monorepo + python-package + scheduler` is the first governed quadruple-overlay contract. It extends the already certified worker, topology, package, and scheduler compounds without introducing a new ownership role, so the generated scaffold remains the deterministic union of those governed surfaces under the existing fail-closed composition model.

## Admitted Non-Composite Realizations

The following remain valid outside the multi-overlay matrix:

- base-only
- a single admitted overlay applied to `universal-base`
- `scheduler` as a certified admitted single-overlay realization

Single-overlay realization is governed by the admitted overlay inventory under `docs/codex/templates/manifests/` and is not treated as a multi-overlay expansion.

## Certified Fail-Closed Boundary

The following combinations are explicitly not supported and must remain rejected unless a future governance lane broadens the contract:

- `laravel + cli-worker`
- `laravel + django`

Representative rejection cases must remain covered by governance verification so unsupported behavior cannot expand silently.

`laravel + cli-worker` is explicitly rejected because the repository does not define a Laravel-specific worker composition contract for application-root ownership, worker lifecycle, and command dispatch coordination.

`django + scheduler` is now admitted only through a Django-native scheduler composition contract. That support is limited to the direct pair and requires the canonical Django scheduler surface at `project/celery.py` together with the governed companion surfaces `project/scheduler.py`, `project/settings.py`, and `manage.py`. It does not imply broader framework-native scheduler support or automatic admission of `django + monorepo + scheduler`.

`laravel + scheduler` is now admitted only through the first framework-native scheduler contract. That support is limited to the direct pair and requires the canonical Laravel scheduler surface at `app/Console/Kernel.php` together with the governed companion surfaces `routes/console.php` and `config/scheduler.php`.

`laravel + monorepo + scheduler` is now admitted only through the Laravel monorepo scheduler compound contract. Under that contract, Laravel-native scheduler truth remains framework-owned, but the governed Laravel scheduler surfaces are placed under `apps/backend/laravel-app/`, with the canonical scheduler surface at `apps/backend/laravel-app/app/Console/Kernel.php` and companion surfaces at `apps/backend/laravel-app/routes/console.php` and `apps/backend/laravel-app/config/scheduler.php`.

## Overlay Compatibility Rules

- `django` may compose only with `monorepo` and `scheduler`
- `service` may compose only with `monorepo`
- `laravel` may compose only with `monorepo` and `scheduler`
- `monorepo` may compose only with `laravel`, `django`, `service`, `node-typescript-service`, and `cli-worker`
- `monorepo` may compose only with `laravel`, `django`, `service`, `node-typescript-service`, `cli-worker`, and `scheduler`
- `cli-worker` may compose only with `python-package`, `php-package`, `node-typescript-service`, `monorepo`, and `scheduler`
- `python-package` may compose only with `cli-worker` and `scheduler`
- `scheduler` may compose only with `cli-worker`, `django`, `laravel`, `monorepo`, and `python-package`
- `node-typescript-service` may compose only with `monorepo` and `cli-worker`
- certified triple-overlay composition may be admitted through governed capability compatibility when it is explicitly listed in the certified matrix
- certified quadruple-overlay composition may be admitted only when it is explicitly listed in the certified matrix and ledger
- framework-native scheduler triple-overlay composition is not implied by pairwise support; each admitted triplet requires its own governed compound contract
- overlays not listed in a compatible pair are non-composable by default
- the base scaffold may be realized without overlays

## Drift Detection Rules

- manifest compatibility changes must update this contract in the same change set
- scaffold compatibility logic must not admit any combination absent from the certified matrix
- docs under `docs/codex/templates/` and `docs/governance/` must not advertise unsupported combinations as supported
- tests must cover every certified supported combination and representative fail-closed combinations
- any proposal to add a new supported combination requires a documented governance lane with verification evidence

## Verification Surfaces

The minimum verification surface for this contract is:

- `tests/governance/test_template_composition_matrix.py`
- `tests/governance/test_template_conformance.py`
- `python tools/governance/template_scaffold.py list-manifests --output json`
- `python tools/templates/list_templates.py --output json`

## Change Control

This contract may be changed only through a documented governance pipeline that:

1. explains why the boundary is changing
2. updates manifests and scaffold compatibility logic
3. updates repository docs
4. extends verification coverage
5. records an explicit certification or promotion verdict
