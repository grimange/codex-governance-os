# Canonical Service Monorepo Layout

The certified scaffold result for `service + monorepo` is:

```text
repo-root/
├─ services/
│  └─ service-app/
│     ├─ src/
│     ├─ tests/
│     ├─ pyproject.toml
│     ├─ README.md
│     └─ service_entrypoint/
├─ packages/
├─ shared/
├─ docs/
├─ .codex/
├─ AGENTS.md
└─ README.md
```

Ownership rule:

- monorepo overlay owns repository root, `packages/`, `services/`, and `shared/`
- service overlay owns `services/service-app/`
- governance surfaces remain rooted at repository top level
