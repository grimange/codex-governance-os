# Authority Contract

Pipeline 176 adds `validate_canonical_input_authority()` to enforce:

- canonical-path allowlisting for next-action inputs
- required-surface existence checks
- shadow-surface detection under the repository root
- cross-surface consistency for the roadmap target across roadmap, remediation,
  gaps, and maturity surfaces
- prevention of output generation when authority validation fails

The selector now reads only one authoritative version of each required input
surface.
