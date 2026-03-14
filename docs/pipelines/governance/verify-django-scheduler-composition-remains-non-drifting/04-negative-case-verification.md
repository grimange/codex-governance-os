# Negative Case Verification

## Explicit Unsupported Compound Case

Verified fail-closed result:

- `django + monorepo + scheduler`
- `supported: false`
- `reason_code: unsupported`
- `rejection_reason: not present in certified composition matrix`

This satisfies the lane requirement that compound combinations remain closed
unless intentionally admitted by a later lane.

## Incomplete Or Partial Django Scheduler Evidence

The direct test suite continues to enforce the authoritative surface set through
real scaffold generation and contract checks rather than only documentation
claims. That means partial or malformed Django scheduler support would break:

- manifest compatibility expectations in [django.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/django.json)
- generated-surface assertions in [test_django_native_scheduler_composition.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_django_native_scheduler_composition.py)
- matrix drift checks in [test_template_composition_drift.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_drift.py)

## Unchanged Control Case

`laravel + scheduler` remained supported with `reason_code:
certified-multi-overlay`, confirming that Django verification did not regress
the earlier Laravel-native scheduler contract.
