# Laravel Monorepo Scheduler Contract

## Canonical Supported Triplet

`laravel + monorepo + scheduler`

## Canonical Placement

Laravel application root:

- `apps/backend/laravel-app/`

Laravel-native scheduler evidence set:

- `apps/backend/laravel-app/app/Console/Kernel.php`
- `apps/backend/laravel-app/routes/console.php`
- `apps/backend/laravel-app/config/scheduler.php`

Generic scheduler overlay surfaces remain:

- `scheduler/schedule.py`
- `scheduler/scheduler_runtime.py`

## Contract Validity Conditions

The compound is valid only when:

- the Laravel app is placed at `apps/backend/laravel-app/`
- the Laravel-native scheduler surfaces are placed under that app root
- the triplet is explicitly admitted by runtime, matrix snapshot, and docs
- the scaffold resolver chooses the compound override deterministically

## Fail-Closed Conditions

The compound must fail closed when:

- Laravel scheduler surfaces are present but not placed under the monorepo app root
- a competing same-specificity compound override exists
- `django + monorepo + scheduler` or worker-oriented framework compounds are
  inferred from this admission
- documentation or matrix claims outpace runtime behavior
