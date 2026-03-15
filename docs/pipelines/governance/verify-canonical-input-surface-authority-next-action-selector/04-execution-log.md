# Execution Log

## Valid-State Determinism

Commands executed:

```bash
python tools/governance/inspect_governance_state.py next-action
sha256sum docs/governance/governance-system-next-action.json
python tools/governance/inspect_governance_state.py next-action
sha256sum docs/governance/governance-system-next-action.json
```

Observed result:

- both runs succeeded
- both hashes matched

## Missing-Surface Failure

Observed structured error:

```json
{
  "status": "error",
  "error_code": "MISSING_CANONICAL_GOVERNANCE_SURFACE",
  "message": "Required canonical governance surface is missing: docs/governance/governance-system-gaps.json"
}
```

## Shadow-Surface Failure

Observed structured error:

```json
{
  "status": "error",
  "error_code": "SHADOW_GOVERNANCE_SURFACE_DETECTED",
  "message": "Shadow governance surface detected for governance-system-advancement-roadmap.json: backup/governance-system-advancement-roadmap.json"
}
```

## Cross-Surface Inconsistency Outcome

Observed result:

- selector regenerated next-action output
- exit status remained `0`

## Multiple-Candidate Outcome

Observed result:

- selector regenerated next-action output
- exit status remained `0`
