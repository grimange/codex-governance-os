# Verification Scope

## Canonical Entrypoints

Verification used only the normalized repository command surface:

- `python3 tools/governance/inspect_governance_state.py snapshot`
- `python3 tools/governance/inspect_governance_state.py next-action`
- `python3 tools/governance/inspect_governance_state.py authoritative-state`

## Surfaces Verified

- `docs/governance/governance-state-snapshot.json`
- `docs/governance/governance-authoritative-state-answer.json`
- `docs/governance/governance-system-next-action.json`
- `docs/governance/governance-system-state.json`
- `tests/governance/test_governance_system_next_action.py`

## Criteria

1. Baseline authoritative-state output is deterministic on intact snapshot
   inputs.
2. Missing snapshot fails closed and does not regenerate the snapshot.
3. Structurally invalid snapshot fails closed and is not normalized or repaired.
4. Canonical mismatch fails closed with snapshot mismatch evidence.
5. Pre-marked drifted snapshot fails closed and does not emit normal
   authoritative output.
6. Across all negative paths, authoritative-state does not self-regenerate the
   snapshot.
7. After restoration, authoritative-state returns to the exact baseline hash.
8. Targeted and full governance regression suites pass.
