# Pipeline Registry Integrity

## Registry Checks

| Check | Result | Issue Class | Notes |
|-------|--------|-------------|-------|
| registry exists | PASS | informational | `docs/pipelines/registry/pipeline-registry.md` is present. |
| registry structure is valid | PASS | informational | Markdown table structure is readable and consistent. |
| entries correspond to real pipelines | PASS | informational | `000` and `001` both point to existing files. |
| no stale entries | PASS | informational | No registry entry points to a missing pipeline. |
| identifiers match pipeline IDs | PASS | informational | Registered IDs align with pipeline filenames. |
| all active pipelines registered | FAIL | moderate | Pipeline `002` is active in repository practice but absent from the registry. |

## Integrity Assessment

The registry is valid but incomplete. This is a moderate governance issue because the constitution treats registration as mandatory for active pipelines.
