# Governance Execution Flow Map

The current governed execution flow is:

1. repository doctrine and contracts define authority, evidence, and fail-closed
   boundaries
2. registry and manifest truth are loaded through canonical tooling
3. execution commands validate or explain state before acting
4. unsupported or drifting states return structured failure instead of silent
   continuation
5. governance tests verify cross-surface consistency and drift detection

Representative command flows:

- `python tools/governance/template_scaffold.py doctor-composition --overlays ...`
  - routes composition interpretation through canonical contract logic
- `python tools/governance/template_scaffold.py verify-composition-matrix --output json`
  - validates runtime/manifests/docs/snapshot agreement
- `python tools/governance/template_scaffold.py list-manifests --output json`
  - projects admitted manifest state and fails closed on inventory drift
- `python tools/templates/list_templates.py --output json`
  - projects repository template inventory and aligns with manifest validation
- `python tools/governance/template_registry.py validate`
  - verifies registry entry integrity for admitted templates

Result: execution routing is canonical within the implemented template-governance
domain.
