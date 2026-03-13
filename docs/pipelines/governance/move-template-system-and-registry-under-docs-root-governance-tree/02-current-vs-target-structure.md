# Current Vs Target Structure

## Previous Structure

```text
repo-root/
  docs/
    governance/
      templates/
  registry/
    templates/
      index.yaml
      entries/
  templates/
    pipelines/
    verification/
    rules/
    skills/
    subagents/
    reports/
```

## Target Structure

```text
repo-root/
  docs/
    governance/
      templates/
      registries/
        templates/
          index.yaml
          entries/
    codex/
      templates/
        pipelines/
        verification/
        rules/
        skills/
        subagents/
        reports/
```

The target keeps canonical family doctrine in `docs/governance/templates/`, moves admitted registry state into `docs/governance/registries/templates/`, and moves admitted template bodies into `docs/codex/templates/`.
