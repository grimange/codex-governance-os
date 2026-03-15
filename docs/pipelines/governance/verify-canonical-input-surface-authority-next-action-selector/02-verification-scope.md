# Verification Scope

Pipeline 177 verifies:

- `tools/governance/inspect_governance_state.py`
- `validate_canonical_input_authority()`
- `next-action` selector mode
- `docs/governance/governance-system-next-action.json`

Repository-truth canonical inputs under test:

- `docs/governance/governance-system-state.json`
- `docs/governance/governance-system-maturity.json`
- `docs/governance/governance-system-gaps.json`
- `docs/governance/governance-system-gap-remediation-plan.json`
- `docs/governance/governance-system-advancement-roadmap.json`

Note:

- the pipeline prose uses shorter aliases such as `governance-roadmap.json`
- verification follows the actual canonical repository file names above
