# Governance Integration Plan

Integration points established by this lane:

- `tools/governance/portability_scan.py` is the deterministic scan utility
- `tools/governance/preflight.py` is the canonical governance preflight
  entrypoint
- `.codex/AGENTS.md` now instructs governed operators to run the preflight
  command before governed pipeline execution
- `README.md` and `docs/governance/architecture-doctrine.md` expose the
  preflight command as part of the repository's governance tooling model

Current enforcement boundary:

- the repository now has an automated preflight command that blocks violations
- this lane does not claim a separate daemon, CI integration, or automatic
  trigger before every user action
