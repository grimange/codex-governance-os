# Remediation Planning Model

Pipeline 168 converts each detected gap into one remediation entry with:

- `domain`
- `current_status`
- `remediation_strategy`
- `required_evidence`
- `recommended_action`
- `suggested_pipeline`
- `priority`
- `dependency_order`
- `promotion_target`

Ordering model:

1. `INVALID_STATE` gaps first
2. `UNVERIFIED` gaps next
3. stable lexical ordering within the same classification

This preserves deterministic output and dependency-respecting remediation
sequencing.
