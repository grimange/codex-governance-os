# Monorepo Overlay

This overlay adds monorepo-oriented runtime shape expectations on top of the universal base scaffold without changing governance core semantics.

When composed with `laravel`, the canonical application placement is `apps/backend/laravel-app/` under the repository root.

When composed with `laravel` and `scheduler`, the compound contract keeps scheduler authority in Laravel-native framework surfaces while placing those surfaces under `apps/backend/laravel-app/`.

When composed with `django`, the canonical service placement is `apps/backend/django-service/` under the repository root.

When composed with `service`, the canonical service placement is `services/service-app/` under the repository root.
