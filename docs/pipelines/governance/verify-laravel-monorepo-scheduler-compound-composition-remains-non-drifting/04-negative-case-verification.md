# Negative Case Verification

## Unsupported Compound Preservation

Verified fail-closed result:

- `django + monorepo + scheduler`
- `supported: false`
- `reason_code: unsupported`
- `rejection_reason: not present in certified composition matrix`

## Compound Resolver Safety

The scaffold resolver remains fail-closed for ambiguous compound override
resolution. This behavior is covered by
[test_template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_scaffold.py),
which asserts `RegistryError` for same-specificity conflicting compound
overrides.

## Unchanged Worker Boundary

Worker-oriented framework scheduler compounds were not broadened by this lane.
They remain outside the certified matrix and must not be inferred from the new
Laravel monorepo triplet.
