# Conformance Checklist

Each supported fixture was evaluated against the following deterministic checks:

1. base universal contract applies without contradiction
2. overlay, if used, is explicitly declared by the base manifest
3. overlay manifest declares `universal-base` as its base template
4. governance core surfaces are created in the realized fixture
5. overlay required surfaces are created in the realized fixture
6. overlay required surfaces do not redefine governance core surfaces
7. scaffold selection is recorded under `docs/governance/scaffold-selection.json`
8. manifest inventory remains deterministic and machine-readable
9. template-related governance tests pass for the current repository state

Result vocabulary:

- `PASS`
- `UNSUPPORTED_BY_DESIGN`
- `BLOCKED`
