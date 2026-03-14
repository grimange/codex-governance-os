# Layer 2 Execution Surface Inventory

This repository does not currently expose a single `gov.py`-style governance
entrypoint. The current Layer 2 execution surface is distributed across the
canonical governance CLIs and their supporting verification suites:

- [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
  - scaffold realization
  - manifest inventory
  - composition doctor surface
  - composition-matrix drift verification
- [template_registry.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_registry.py)
  - admitted-template registry validation, resolution, and listing
- [template_lint.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_lint.py)
  - governed template validation
- [list_templates.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/list_templates.py)
  - repository-level manifest inventory projection
- [pipeline-registry.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/registry/pipeline-registry.md)
  and [pipeline-registry-integrity-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/pipeline-registry-integrity-contract.md)
  - active pipeline authority and discoverability discipline

Supporting execution-verification suites inspected:

- [test_template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_scaffold.py)
- [test_template_composition_surface_consistency.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_surface_consistency.py)
- [test_template_registry.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_registry.py)
- [test_template_composition_drift.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_drift.py)

Result: Layer 2 exists, but as a distributed execution surface rather than a
single unified governance runner.
