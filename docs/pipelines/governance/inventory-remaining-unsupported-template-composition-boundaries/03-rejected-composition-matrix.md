# Rejected Composition Matrix

## Summary

Out of `28` total overlay pairs:

- `7` are supported
- `21` are rejected
- `2` of the rejected pairs are already explicit fail-closed boundaries
- `19` are still generic `unsupported` classifications

## Explicitly Rejected Pairs

- `cli-worker + laravel`
  - `reason_code: explicitly-rejected`
  - `rejection_reason: missing Laravel worker composition contract`
- `django + laravel`
  - `reason_code: explicitly-rejected`
  - `rejection_reason: cross-framework application collision`

## Generically Unsupported Pairs

- `cli-worker + django`
- `cli-worker + service`
- `django + node-typescript-service`
- `django + php-package`
- `django + python-package`
- `django + service`
- `laravel + monorepo`
- `laravel + node-typescript-service`
- `laravel + php-package`
- `laravel + python-package`
- `laravel + service`
- `monorepo + php-package`
- `monorepo + python-package`
- `node-typescript-service + php-package`
- `node-typescript-service + python-package`
- `node-typescript-service + service`
- `php-package + python-package`
- `php-package + service`
- `python-package + service`

All generically unsupported pairs currently return:

- `reason_code: unsupported`
- `rejection_reason: not present in certified composition matrix`
