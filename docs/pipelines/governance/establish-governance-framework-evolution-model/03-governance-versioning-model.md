# Governance Versioning Model

## Model

- Patch-level governance changes: emergency corrective repairs and equivalent bounded fixes that restore already-intended behavior.
- Minor governance changes: additive compatible extensions and compatible behavioral refinements.
- Major governance changes: breaking governance changes that alter required repository behavior or authority interpretation materially.

## Recording Rule

The repository does not currently use a standalone numeric manifest for governance versions. Version meaning is recorded through:

- doctrine updates
- pipeline artifacts
- registry changes
- explicit promotion and final-verdict language

## Practical Rule

If a future change would require adopters to restructure governance surfaces or reinterpret active pipelines materially, treat it as a major governance evolution event and require explicit migration guidance.
