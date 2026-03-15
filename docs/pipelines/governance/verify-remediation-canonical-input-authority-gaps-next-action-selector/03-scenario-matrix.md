# Scenario Matrix

## Scenario 1 — Valid Canonical Governance State

Observed result:

- selector exited `0`
- repeated output hash matched:
  `e9426ae4658cde81f6c2465538bac21b9ae10b1c8439ee98497586328ce8adb5`

Status:

- pass

## Scenario 2 — Cross-Surface Target Consensus Violation

Injected condition:

- changed roadmap `recommended_next_target` to `architecture_advisor`

Observed result:

- exit status `1`
- error code: `GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION`
- next-action hash unchanged

Status:

- pass

## Scenario 3 — Alternate-Named Governance Surface Candidate

Injected condition:

- created `governance-system-advancement-roadmap-copy.json`
- created `governance-system-advancement-roadmap-backup.json`
- created `governance-system-advancement-roadmap-old.json`
- created `governance-system-advancement-roadmap-draft.json`

Observed result:

- exit status `1`
- error code: `AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED`
- next-action hash unchanged

Status:

- pass
