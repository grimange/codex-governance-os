# Canonical Entrypoint Normalization

Pipeline 185 identified command-surface drift in proposed documentation. The
repository’s implemented canonical entrypoints are:

## Canonical Commands

- next-action inspection:
  `python3 tools/governance/inspect_governance_state.py next-action`
- authoritative governance-state inspection:
  `python3 tools/governance/inspect_governance_state.py authoritative-state`
- snapshot generation as a separate governed operation:
  `python3 tools/governance/inspect_governance_state.py snapshot`

## Normalized Contract

- The repository does not provide a separate
  `tools/governance/select_governance_system_next_action.py` entrypoint.
- Future pipelines and verification lanes should reference the implemented
  `inspect_governance_state.py` subcommands above.
- Snapshot generation remains a distinct command and is not part of the
  authoritative-state execution path.

This normalization preserves repository truth as the authority for command
surfaces.
