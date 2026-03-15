# Problem Statement

Pipelines 184 through 187 established, hardened, and verified the authoritative
governance state answer surface. Even so, governance consumers could still
observe more than one output surface:

- `docs/governance/governance-authoritative-state-answer.json`
- `docs/governance/governance-system-next-action.json`

The authoritative answer already composed maturity, blockers, progression, and
next-action data, but the repository had not yet explicitly elevated that
surface into the single canonical governance control-plane endpoint.

Without convergence, downstream automation and reporting could still treat the
selector output as a peer surface rather than a subordinate supporting surface.
