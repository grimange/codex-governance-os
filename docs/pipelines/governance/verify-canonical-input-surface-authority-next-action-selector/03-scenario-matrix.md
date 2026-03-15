# Scenario Matrix

## Scenario 1 — Valid Canonical State

Observed result:

- selector exited `0`
- repeated output hash matched:
  `e9426ae4658cde81f6c2465538bac21b9ae10b1c8439ee98497586328ce8adb5`

Status:

- pass

## Scenario 2 — Missing Canonical Surface

Injected condition:

- temporarily removed `docs/governance/governance-system-gaps.json`

Observed result:

- exit status `1`
- error code: `MISSING_CANONICAL_GOVERNANCE_SURFACE`
- next-action output hash unchanged

Status:

- pass

## Scenario 3 — Shadow Surface Injection

Injected condition:

- created `backup/governance-system-advancement-roadmap.json`

Observed result:

- exit status `1`
- error code: `SHADOW_GOVERNANCE_SURFACE_DETECTED`
- next-action output hash unchanged

Status:

- pass

## Scenario 4 — Cross-Surface Inconsistency

Injected condition:

- changed roadmap `recommended_next_target` from `multi_agent_governance` to
  `architecture_advisor`

Observed result:

- selector exited `0`
- selector regenerated `docs/governance/governance-system-next-action.json`

Status:

- fail

## Scenario 5 — Multiple Candidate Inputs

Injected condition:

- created `docs/governance/governance-system-advancement-roadmap-copy.json`

Observed result:

- selector exited `0`
- no authority error emitted

Status:

- fail
