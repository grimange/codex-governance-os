# Normalization Plan

Scoped remediation steps:

1. Update Pipeline `137` frontmatter so the canonical artifact bundle and final
   verdict file are explicitly recorded.
2. Replace the non-existent `tools/governance/gov.py` expectation with the
   existing continuity harness entrypoint.
3. Update the verification commands in Pipeline `137` so they match actual
   executable repository tooling.
4. Make the collision-safe artifact bundle path explicit in the lane body.
5. Preserve the historical restricted verdict from Pipeline `137` without
   rewriting or deleting prior evidence.
6. Register Pipeline `138` as the normalization lane that closed the drift.

Out-of-scope by design:

- adding a new `gov.py` orchestration tool
- reclassifying Pipeline `137` as unrestricted
- changing harness implementation code
- changing continuity verification semantics
