# Compound Realization Model

## Resolver Rule

Compound scaffold realization now uses a most-specific override rule:

1. gather all matching overlay override keys whose required companion overlays
   are present
2. select the matching override with the greatest specificity
3. fail closed if more than one override exists at the same specificity

This replaces the earlier effective limitation where only the first pairwise
override could apply.

## Laravel Compound Override

The Laravel manifest now defines an explicit `monorepo+scheduler` compound
override in [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json).

That override defines:

- `placement: apps/backend/laravel-app`
- `scheduler_surface: apps/backend/laravel-app/app/Console/Kernel.php`
- the placed companion surfaces
  - `apps/backend/laravel-app/routes/console.php`
  - `apps/backend/laravel-app/config/scheduler.php`

## Ownership Boundary

- `monorepo` owns topology and root placement
- `laravel` owns framework identity and scheduler truth
- `scheduler` continues to contribute the generic scheduler overlay surfaces
  without taking ownership of the Laravel-native scheduler contract
