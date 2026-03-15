# Verification Plan

Future verification of Pipeline 172 should confirm:

1. `python tools/governance/inspect_governance_state.py next-action` executes
   successfully.
2. `docs/governance/governance-system-next-action.json` is produced.
3. repeated CLI execution produces deterministic output.
4. `target_domain` matches the roadmap `recommended_next_target`.
5. the selected action classification matches the remediation strategy.
6. the selector remains evidence-scoped and fail-closed.
