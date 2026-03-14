# Laravel Monorepo Placement Contract

The certified Laravel-in-monorepo placement is:

```text
apps/backend/laravel-app/
```

The placement contract is expressed in [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json) as `composition_overrides.monorepo` with:

- `type: laravel-application`
- `placement: apps/backend/laravel-app`
- `repository_structure: monorepo`

Required realized surfaces:

- `apps/backend/laravel-app/composer.json`
- `apps/backend/laravel-app/bootstrap/app.php`
- `apps/backend/laravel-app/config/app.php`
- `apps/backend/laravel-app/routes/web.php`
- `apps/backend/laravel-app/public/index.php`
- `apps/backend/laravel-app/app/Console`
- `apps/backend/laravel-app/app/Http`

Optional realized surfaces:

- `apps/backend/laravel-app/resources`
- `apps/backend/laravel-app/database`

This follows the same deterministic nested-placement model already used by `django + monorepo`.
