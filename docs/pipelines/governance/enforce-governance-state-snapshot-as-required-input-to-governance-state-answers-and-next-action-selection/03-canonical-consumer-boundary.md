# Canonical Consumer Boundary

Authoritative current-state consumer currently implemented in repository code:

- `docs/governance/governance-system-next-action.json`
  - produced by `python tools/governance/inspect_governance_state.py next-action`
  - now requires a valid `docs/governance/governance-state-snapshot.json`

Direct-read exceptions retained as non-authoritative or infrastructure-only:

- snapshot generation via `python tools/governance/inspect_governance_state.py snapshot`
- verification harnesses under `tests/governance/`
- canonical source-surface generation commands that establish the snapshot input
  set itself

Boundary rule:

- authoritative next-action selection may validate raw canonical surfaces
  against the snapshot, but it may not silently bypass the snapshot contract and
  emit a normal current-state answer without a valid snapshot input.
