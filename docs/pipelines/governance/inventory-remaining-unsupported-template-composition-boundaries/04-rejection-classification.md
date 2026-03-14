# Rejection Classification

## Explicit Unsupported Boundary

- `cli-worker + laravel`
  - classified explicitly because pipeline `040` codified the missing Laravel worker composition contract
- `django + laravel`
  - classified explicitly because the pair represents a direct cross-framework application collision

## Missing Composition Contract

These pairs look potentially designable, but they currently lack deterministic ownership and placement rules:

- `cli-worker + django`
  - no Django-specific worker/runtime integration contract
- `cli-worker + service`
  - no governed service-plus-worker coordination contract
- `laravel + monorepo`
  - no Laravel-in-monorepo placement and ownership contract
- `monorepo + php-package`
  - no package-in-monorepo placement contract
- `monorepo + python-package`
  - no package-in-monorepo placement contract

## Structural Incompatibility

These pairs currently look like direct shape conflicts rather than omitted allowlist entries:

- `django + service`
- `laravel + service`
- `laravel + node-typescript-service`
- `node-typescript-service + service`
- `php-package + python-package`
- `php-package + service`
- `python-package + service`
- `django + laravel`

The common pattern is competing ownership of the application or service root, or cross-language/runtime collision without a natural bounded merge model.

## Low-Value Or Ambiguous Missing Compatibility Declaration

These pairs are unsupported but do not currently justify immediate pipeline investment:

- `django + node-typescript-service`
- `django + php-package`
- `django + python-package`
- `laravel + php-package`
- `laravel + python-package`
- `node-typescript-service + php-package`
- `node-typescript-service + python-package`

They are better treated as unadmitted combinations until a concrete runtime model is proposed. At present there is no evidence they should be promoted, and no manifest declares them as near-ready.
