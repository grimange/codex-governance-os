# Canonical Django Monorepo Layout

The certified scaffold result for `django + monorepo` is:

```text
repo-root/
├─ apps/
│  └─ backend/
│     └─ django-service/
│        ├─ manage.py
│        ├─ pyproject.toml
│        ├─ requirements.txt
│        ├─ project/
│        │  ├─ settings.py
│        │  ├─ urls.py
│        │  └─ asgi.py
│        └─ app_modules/
├─ packages/
├─ services/
├─ shared/
├─ docs/
├─ .codex/
├─ AGENTS.md
└─ README.md
```

Ownership rule:

- monorepo overlay owns repository root, `packages/`, `services/`, and `shared/`
- django overlay owns `apps/backend/django-service/`
- governance surfaces remain at repository root
