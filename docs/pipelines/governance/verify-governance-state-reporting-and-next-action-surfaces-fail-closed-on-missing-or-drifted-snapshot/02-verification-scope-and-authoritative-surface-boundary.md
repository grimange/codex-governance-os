# Verification Scope and Authoritative Surface Boundary

Verified authoritative current-state consumer:

- `docs/governance/governance-system-next-action.json`
  - command: `python tools/governance/inspect_governance_state.py next-action`

Verified required snapshot authority surface:

- `docs/governance/governance-state-snapshot.json`

Excluded from authoritative verification boundary:

- snapshot generation mode
- intermediate canonical generation surfaces
- diagnostic and verification harnesses

Reason for boundary:

- Pipeline 182 bound code-level snapshot enforcement only to the authoritative
  next-action consumer. Other governance surfaces remain source or intermediate
  generation surfaces rather than independent authoritative current-state answer
  endpoints.
