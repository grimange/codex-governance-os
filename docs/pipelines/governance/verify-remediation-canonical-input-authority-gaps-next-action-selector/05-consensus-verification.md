# Consensus Verification

Injected mutation:

- roadmap `recommended_next_target` changed from `multi_agent_governance` to
  `architecture_advisor`

Expected behavior:

- selector exits non-zero
- selector emits
  `GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION`
- selector does not rewrite canonical output

Observed behavior:

- selector exited `1`
- selector emitted the expected machine-readable error
- canonical next-action output hash remained unchanged

Result:

- cross-surface target consensus enforcement is now verified
