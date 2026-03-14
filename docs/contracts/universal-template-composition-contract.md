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
- `django + monorepo`
- `laravel + monorepo`
- `service + monorepo`
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + python-package`
- `cli-worker + php-package`

These combinations are certified because scaffold realization, manifest declarations, repository docs, and governance tests align on the same result.

## Admitted Non-Composite Realizations

The following remain valid outside the multi-overlay matrix:

- base-only
- a single admitted overlay applied to `universal-base`

Single-overlay realization is governed by the admitted overlay inventory under `docs/codex/templates/manifests/` and is not treated as a multi-overlay expansion.

## Certified Fail-Closed Boundary

The following combinations are explicitly not supported and must remain rejected unless a future governance lane broadens the contract:

- `laravel + cli-worker`
- `laravel + django`

Representative rejection cases must remain covered by governance verification so unsupported behavior cannot expand silently.

`laravel + cli-worker` is explicitly rejected because the repository does not define a Laravel-specific worker composition contract for application-root ownership, worker lifecycle, and command dispatch coordination.

## Overlay Compatibility Rules

- `django` may compose only with `monorepo`
- `service` may compose only with `monorepo`
- `laravel` may compose only with `monorepo`
- `monorepo` may compose only with `laravel`, `django`, `service`, `node-typescript-service`, and `cli-worker`
- `cli-worker` may compose only with `python-package`, `php-package`, `node-typescript-service`, and `monorepo`
- `node-typescript-service` may compose only with `monorepo` and `cli-worker`
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
