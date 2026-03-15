# Final Verdict

Verdict: `GOVERNANCE_SYSTEM_NEXT_ACTION_SELECTOR_FAIL_CLOSED_RESOLUTION_ENFORCED`

## Summary

- Enforced fail-closed roadmap resolution in
  `tools/governance/inspect_governance_state.py`.
- Prevented `docs/governance/governance-system-next-action.json` from being
  written when roadmap target resolution fails.
- Added stable machine-readable failure output for unresolved roadmap targets.
- Preserved deterministic valid-state selector behavior.
- Added regression tests covering valid and invalid roadmap resolution paths.
