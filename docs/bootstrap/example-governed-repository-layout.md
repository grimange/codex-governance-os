# Example Governed Repository Layout

This example shows a generic repository after adopting the template baseline and then adding local project-specific governance surfaces.

```text
project/
├── AGENTS.md
├── .codex/
│   ├── AGENTS.md
│   └── skills/
│       └── <local-skill>/
│           └── SKILL.md
├── docs/
│   ├── bootstrap/
│   │   ├── governed-project-bootstrap.md
│   │   ├── skill-inheritance-model.md
│   │   ├── local-override-model.md
│   │   ├── minimal-setup-checklist.md
│   │   └── example-governed-repository-layout.md
│   ├── governance/
│   │   ├── architecture-doctrine.md
│   │   ├── governance-lifecycle.md
│   │   ├── skill-invocation-standard.md
│   │   └── universal-skills-index.md
│   ├── contracts/
│   │   └── <local-contract>.md
│   └── pipelines/
│       ├── governance/
│       │   ├── 000--initialize-governed-project.md
│       │   ├── 001--discover-existing-architecture-and-establish-doctrine.md
│       │   ├── 002--audit-repository-governance-readiness.md
│       │   └── <local-governance-pipeline>.md
│       ├── registry/
│       │   └── pipeline-registry.md
│       └── <category>/
│           └── <pipeline-artifact-folder>/
└── skills/
    └── <inherited-universal-skill-library>
```

## Layout Interpretation

- `skills/` represents the inherited universal skill library supplied by the template.
- `.codex/skills/` is reserved for local specialization and should remain smaller than the inherited universal surface.
- `docs/bootstrap/` stays generic and explains adoption, inheritance, and override rules.
- `docs/governance/` contains reusable doctrine and the local architecture doctrine.
- `docs/contracts/` and local pipeline folders grow only after discovery and later governance work justify them.
