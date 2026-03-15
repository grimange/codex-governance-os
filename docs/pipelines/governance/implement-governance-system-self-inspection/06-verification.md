# Verification

Verification conditions for Pipeline 162 are now implementable:

1. `tools/governance/inspect_governance_state.py` exists.
2. `docs/governance/governance-system-state.json` matches the generated JSON
   shape used by the tool.
3. The tool reads canonical governance registry, progress, execution-map, and
   introspection surfaces only.
4. The tool reports alignment issues instead of silently masking drift.
5. The tool does not modify capability definitions or maturity scoring logic.

Pipeline 162 establishes the implementation surface. Manual execution of the CLI
is deferred to Pipeline 163 verification.
