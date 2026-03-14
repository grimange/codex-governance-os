# Fail-Closed Boundary Model

The governed fail-closed model for triple overlays is now:

- certified triplets listed in the ledger may resolve successfully
- listed fail-closed triple boundaries must remain rejected
- unknown triple combinations fail closed by default
- pairwise support is insufficient evidence for compound admission

This keeps compound behavior explicit and prevents silent broadening through
incremental overlay additions.
