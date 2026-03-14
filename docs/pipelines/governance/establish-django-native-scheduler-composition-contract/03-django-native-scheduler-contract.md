# Django-Native Scheduler Contract

The Django-native scheduler contract admitted in this lane is the direct pair:

- `django + scheduler`

Canonical support requirements:

- framework identity is Django, not a generic Python package, worker, or service
- the canonical scheduler surface is `project/celery.py`
- governed companion surfaces are:
  - `project/scheduler.py`
  - `project/settings.py`
  - `manage.py`
  - `project/urls.py`
  - `project/asgi.py`
- support remains bounded to the direct pair only

Ownership boundary:

- Django owns framework-native scheduler semantics through the governed `project/celery.py` and `project/scheduler.py` surfaces
- the scheduler overlay remains part of the composition contract and continues to contribute its governed scheduler surfaces
- this lane does not admit `django + monorepo + scheduler`
- this lane does not change Laravel-native scheduler support
