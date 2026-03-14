# Test And Reason-Code Plan

Tests added or updated:

- [test_framework_scheduler_unsupported_boundaries.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_framework_scheduler_unsupported_boundaries.py)
- [test_template_scheduler_overlay.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_scheduler_overlay.py)
- [test_template_capability_conflicts.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_capability_conflicts.py)
- [test_template_capability_composition.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_capability_composition.py)
- [test_template_composition_matrix.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_matrix.py)
- [test_template_composition_drift.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_drift.py)

Locked assertions:

- both framework scheduler pairs return `reason_code: explicitly-rejected`
- both framework scheduler pairs return `conflict_code: framework-native-scheduler-required`
- each pair returns its canonical framework-specific rejection reason
- supported scheduler compositions remain certified and unaffected
- matrix snapshot drift is detectable if these explicit boundary reasons change
