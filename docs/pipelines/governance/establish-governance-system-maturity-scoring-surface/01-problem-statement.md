# Problem Statement

The governance system now exposes deterministic state through
`docs/governance/governance-system-state.json`, but it still lacks a separate
machine-readable maturity signal that scores governance domains, records
fail-closed blockers, and recommends next pipeline movement.

Without that scoring surface, the repository can inspect state but cannot answer
system-level maturity in a deterministic, machine-readable form.
