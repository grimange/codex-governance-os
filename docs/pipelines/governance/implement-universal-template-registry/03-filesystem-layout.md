# Filesystem Layout

## Implemented Layout

```text
docs/
  governance/
    registries/
      templates/
        index.yaml
        entries/
          pipeline.universal.base.yaml
          verification.universal.base.yaml
          rule.universal.safety.yaml
          skill.universal.discovery.yaml
          subagent.universal.architecture-specialist.yaml
          report.universal.governance-summary.yaml
  codex/
    templates/
      pipelines/
        universal-base.md
      verification/
        universal-base.md
      rules/
        safety.md
      skills/
        discovery.md
      subagents/
        architecture-specialist.md
      reports/
        governance-summary.md
```

Registry metadata and template bodies are now separated under the docs-root governance tree as required by the governing pipeline.
