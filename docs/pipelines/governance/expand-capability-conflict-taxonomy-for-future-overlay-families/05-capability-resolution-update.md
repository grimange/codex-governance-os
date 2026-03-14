# Capability Resolution Update

Runtime classification was updated in [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py) and surfaced through [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py).

The engine now:

- maps explicit unsupported boundaries to canonical conflict codes
- maps role collisions to taxonomy classifications
- maps duplicate governed runtime claims to taxonomy classifications
- exposes `conflict_code` in doctor output while preserving the existing top-level decision class

This preserves the current matrix and rejection reasons while making conflict semantics deterministic.
