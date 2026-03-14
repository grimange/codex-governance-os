# Scheduler Overlay

This overlay adds scheduler-oriented runtime expectations on top of the universal base scaffold without changing governance core semantics.

It is intended for repositories that need deterministic scheduled execution surfaces such as cron-style jobs, periodic maintenance tasks, or implementation-agnostic scheduler runtimes.

Required generated scheduler files use explicit protected-region markers so generated schedule truth remains drift-detectable while repository-local extensions stay outside the governed region.

Framework-native scheduler contracts currently exist for the direct pairs `laravel + scheduler` and `django + scheduler`, and for the first admitted compound `laravel + monorepo + scheduler`. The Django-native contract uses the scheduler surfaces `project/celery.py` and `project/scheduler.py`. The Laravel monorepo scheduler compound keeps framework-native scheduler authority in the Laravel app while placing those scheduler surfaces under `apps/backend/laravel-app/`.
