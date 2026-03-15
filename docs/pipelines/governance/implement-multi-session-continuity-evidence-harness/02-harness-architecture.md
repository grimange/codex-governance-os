# Harness Architecture

The implemented harness lives under `tools/governance/session_continuity/`
with a CLI entrypoint at `tools/governance/continuity_harness.py`.

Implemented components:

- `session_loader.py`
  - loads and parses the canonical scenario Markdown fixtures
- `continuity_chain_builder.py`
  - derives deterministic continuity-chain inputs and evidence types
- `continuity_classifier.py`
  - maps evidence and boundary conditions to continuity classifications and
    machine verdicts
- `continuity_evaluator.py`
  - evaluates all loaded scenarios in one deterministic pass

The harness is observational only and does not mutate repository state.
