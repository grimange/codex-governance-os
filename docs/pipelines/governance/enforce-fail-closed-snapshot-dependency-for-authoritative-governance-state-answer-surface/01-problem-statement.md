# Problem Statement

The authoritative governance state answer surface was established in Pipeline
184 and verified on valid baseline inputs in Pipeline 185, but its fail-closed
behavior remained only an inherited implementation property of shared snapshot
validation.

That left two governance risks:

- the authoritative answer surface did not yet have its own explicit,
  repository-documented fail-closed contract
- the canonical command surface for next-action selection had drifted in
  proposed documentation away from the implemented repository entrypoint

The authoritative governance state answer must be a first-class fail-closed
consumer of `docs/governance/governance-state-snapshot.json`. It must not emit
normal authoritative output when the snapshot is missing, malformed, mismatched,
or already drifted, and it must not regenerate snapshot state for itself.
