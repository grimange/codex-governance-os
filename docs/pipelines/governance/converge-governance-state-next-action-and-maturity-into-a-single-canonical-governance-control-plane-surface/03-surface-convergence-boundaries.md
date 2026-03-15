# Surface Convergence Boundaries

This pipeline uses a bounded additive convergence model rather than a breaking
schema replacement.

Convergence rules:

- `docs/governance/governance-authoritative-state-answer.json` is the primary
  governance control-plane endpoint
- `docs/governance/governance-system-next-action.json` remains a supporting
  surface that must stay selector-consistent with the embedded control-plane
  next-action payload
- `docs/governance/governance-state-snapshot.json` remains the required
  provenance and authority input surface

Boundaries preserved:

- no change to snapshot fail-closed enforcement
- no change to selector generation logic
- no removal of `recommended_next_action` in this lane

Compatibility boundary:

- `authoritative_next_action` was added as the canonical converged field
- `recommended_next_action` remains as an alias to avoid breaking existing
  consumers and verification lanes immediately

This keeps the convergence change small while still making the control-plane
surface explicit and top-level.
