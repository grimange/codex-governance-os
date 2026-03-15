# Repository Truth Comparison

## Tooling Assumptions Versus Repository Truth

Pre-normalization mismatch:

- Pipeline `137` named `tools/governance/gov.py`
- repository truth exposes `tools/governance/continuity_harness.py` and
  `tools/governance/preflight.py`
- repository truth does not include `tools/governance/gov.py`

Post-normalization alignment:

- Pipeline `137` now references only existing repository tools
- the lane remains executable through direct bounded commands instead of a
  non-existent unified entrypoint

## Artifact Path Assumptions Versus Repository Truth

Pre-normalization mismatch:

- Pipeline `137` shared the same title stem as Pipeline `133`
- title-stem reuse made a default artifact path ambiguous

Repository truth established during restricted verification:

- Pipeline `137` executed using the distinct artifact bundle path
  `docs/pipelines/governance/verify-multi-session-continuity-evidence-harness-implementation/`

Post-normalization alignment:

- Pipeline `137` now records that collision-safe path directly in both
  frontmatter and body text
- the registry continues to point to that same canonical path

## Semantic Boundary Check

No normalization changed:

- continuity scenario semantics
- harness classification behavior
- evidence thresholds
- verification-only scope

The remediation is documentation-structural and routing-structural only.
