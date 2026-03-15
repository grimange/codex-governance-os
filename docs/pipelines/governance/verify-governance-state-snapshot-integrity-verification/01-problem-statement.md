# Problem Statement

Pipeline 180 established deterministic governance-state snapshot generation and
added snapshot metadata to the governance next-action selector, but that
mechanism was not yet trusted until verified against repository state.

Pipeline 181 verifies deterministic snapshot identity, canonical surface hash
coverage, drift detection behavior, selector metadata emission, selector output
stability, and regression safety.
