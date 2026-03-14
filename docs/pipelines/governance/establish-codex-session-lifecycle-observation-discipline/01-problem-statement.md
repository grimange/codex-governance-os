# Problem Statement

The repository already defines the canonical Layer 6 session state machine,
session registry, execution ledger, admission rules, handoff discipline, and
runtime-boundary evidence model.

What remained implicit was the doctrine for how future runtime lifecycle
transitions should be observed and normalized into those canonical surfaces.

Pipeline `115` closes that gap by defining one observation discipline that:

- preserves the existing lifecycle-state canon
- keeps `session_id` authoritative
- maps observed lifecycle evidence into canonical registry and ledger fields
- remains runtime-neutral and documentation-only

This lane does not introduce runtime instrumentation or a competing event
schema.
