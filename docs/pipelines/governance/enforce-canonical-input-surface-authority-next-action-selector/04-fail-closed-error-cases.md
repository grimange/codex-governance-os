# Fail-Closed Error Cases

Pipeline 176 now emits structured failures for these authority violations:

- `MISSING_CANONICAL_GOVERNANCE_SURFACE`
- `SHADOW_GOVERNANCE_SURFACE_DETECTED`
- `NON_CANONICAL_GOVERNANCE_INPUT_SOURCE`
- `GOVERNANCE_STATE_SURFACE_INCONSISTENCY`
- `UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET`

All error payloads are machine-readable and include the canonical allowlist of
selector input surfaces.
