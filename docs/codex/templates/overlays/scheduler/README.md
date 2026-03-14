# Scheduler Overlay

This overlay adds scheduler-oriented runtime expectations on top of the universal base scaffold without changing governance core semantics.

It is intended for repositories that need deterministic scheduled execution surfaces such as cron-style jobs, periodic maintenance tasks, or implementation-agnostic scheduler runtimes.

Required generated scheduler files use explicit protected-region markers so generated schedule truth remains drift-detectable while repository-local extensions stay outside the governed region.

Framework-native scheduler contracts currently exist for the direct pairs `laravel + scheduler` and `django + scheduler`. The Django-native contract uses the scheduler surfaces `project/celery.py` and `project/scheduler.py` rather than relying only on the generic Python scheduler files used by the standalone scheduler overlay.
