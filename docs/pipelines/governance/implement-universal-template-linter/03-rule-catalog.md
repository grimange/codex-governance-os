# Rule Catalog

## Implemented Canonical Rules

| rule id | severity | summary |
|---------|----------|---------|
| `UTL-001` | error | template must declare or resolve to a recognized class |
| `UTL-002` | error | required frontmatter keys must be present |
| `UTL-003` | error | canonical naming and title alignment must hold |
| `UTL-004` | error | required sections must exist exactly once and in canonical order |
| `UTL-005` | error | unresolved placeholder tokens are blocked unless explicitly allowed |
| `UTL-006` | error | universal templates must not leak repo-specific assumptions |
| `UTL-007` | error | contradictory draft/final semantics are blocked |
| `UTL-008` | warning | safe normalizations are recorded when applied |
| `UTL-009` | error | deterministic output is required and verified by tests |
| `UTL-010` | error | every lint failure must include actionable remediation guidance |

Each emitted failure now carries rule id, severity, path, message, and remediation text.
