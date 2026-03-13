# Docs Root Governance Policy

The `docs/` directory is the authoritative root for all governance and Codex-related files in this repository.

Operational consequences:

- new governance or Codex assets should be authored under `docs/` unless a higher-authority exception is documented
- governance tooling should resolve docs-root locations first and treat root-level legacy paths as non-canonical
- operators should begin governance, pipeline, registry, template, and evidence discovery from `docs/`

Canonical routing after this pipeline:

- governance doctrine: `docs/governance/`
- canonical template family definitions: `docs/governance/templates/`
- admitted template registries: `docs/governance/registries/templates/`
- admitted template bodies: `docs/codex/templates/`
- pipeline definitions and execution artifacts: `docs/pipelines/`
