# Remediation Strategy Classification

Pipeline 168 currently emits these remediation strategies:

- `state_normalization`
  - used when the domain is `INVALID_STATE`
- `capability_completion`
  - used when the domain is `UNVERIFIED`

The planner does not emit unsupported strategy types when repository evidence
does not require them.
