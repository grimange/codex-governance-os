# Tooling Implementation

## Implemented Tools

| tool | path | responsibility |
|------|------|----------------|
| registry loader | `tools/governance/template_registry.py` | load and validate the canonical template registry deterministically |
| template linter | `tools/governance/template_lint.py` | verify frontmatter, required sections, section order, overlay compatibility, and anti-weakening constraints |
| scaffold tool | `tools/governance/template_scaffold.py` | generate deterministic governed artifacts from template families and overlays |

## Tooling Notes

- The scaffold tool validates its own output by invoking the linter before returning success.
- The registry uses JSON-compatible YAML so the implementation remains stdlib-only.
- Advisory-then-enforcing rollout remains explicit; repository-wide enforcement is not enabled by this pipeline.
