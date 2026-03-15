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

## Consensus-Violation Failure

Observed structured error:

```json
{
  "status": "error",
  "error_code": "GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION",
  "message": "Canonical governance surfaces disagree on recommended next target."
}
```

## Ambiguous-Candidate Failure

Observed structured error:

```json
{
  "status": "error",
  "error_code": "AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED",
  "message": "Ambiguous governance surface candidate detected: docs/governance/governance-system-advancement-roadmap-backup.json"
}
```
