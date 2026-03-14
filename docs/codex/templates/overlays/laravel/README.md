# Laravel Overlay

This overlay adds Laravel-oriented runtime shape expectations on top of the universal base scaffold without changing governance core semantics.

When composed with `monorepo`, the canonical Laravel application placement is `apps/backend/laravel-app/`.

When composed directly with `scheduler`, the governed framework-native scheduler contract requires `app/Console/Kernel.php`, `routes/console.php`, and `config/scheduler.php`.
