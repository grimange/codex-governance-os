# Verification Scope

Pipeline 179 verifies:

- `tools/governance/inspect_governance_state.py`
- `validate_governance_target_consensus()`
- `detect_ambiguous_governance_surface_candidates()`
- `validate_canonical_input_authority()`
- `next-action` selector mode

Primary output under verification:

- `docs/governance/governance-system-next-action.json`

Canonical inputs under test:

- `docs/governance/governance-system-state.json`
- `docs/governance/governance-system-maturity.json`
- `docs/governance/governance-system-gaps.json`
- `docs/governance/governance-system-gap-remediation-plan.json`
- `docs/governance/governance-system-advancement-roadmap.json`
