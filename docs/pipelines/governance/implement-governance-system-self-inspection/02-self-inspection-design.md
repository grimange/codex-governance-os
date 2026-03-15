# Self-Inspection Design

Pipeline 162 implements:

- `tools/governance/inspect_governance_state.py`

The tool:

- reads canonical governance state, capability, and maturity surfaces
- derives governance layer state from `docs/governance/governance-system-state.md`
- derives capability state from `docs/governance/governance-capability-registry.md`
- derives capability snapshots from `docs/governance/governance-capability-progress.md`
- validates consistency against `docs/governance/governance-capability-execution-map.md`
- regenerates `docs/governance/governance-system-state.json`

This design keeps the machine-readable state surface evidence-backed and
repository-local.
