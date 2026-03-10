# Remediation Execution

| File Path | Change Summary | Contract Rule Addressed |
|-----------|----------------|-------------------------|
| `docs/pipelines/registry/pipeline-registry.md` | added pipeline `005` as an `ACTIVE` governance pipeline with canonical path | active pipelines must have a registry entry |
| `docs/pipelines/registry/pipeline-registry.md` | added pipeline `006` as an `ACTIVE` governance pipeline in the same change set as remediation execution | activation must be published no later than the same governed change set |

## Execution Notes

- No code, contract text, or runtime configuration changed.
- The implementation correction was limited to the canonical registry state surface to preserve authority boundaries.
