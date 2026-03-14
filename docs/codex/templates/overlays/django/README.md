# Django Overlay

This overlay adds Django-oriented runtime shape expectations on top of the universal base scaffold without changing governance core semantics.

When composed with `monorepo`, the canonical Django service placement is `apps/backend/django-service/`.

When composed directly with `scheduler`, the governed Django-native scheduler contract requires `project/celery.py`, `project/scheduler.py`, `project/settings.py`, and `manage.py`.
