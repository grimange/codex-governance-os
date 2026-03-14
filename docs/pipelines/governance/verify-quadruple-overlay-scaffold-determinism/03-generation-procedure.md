# Generation Procedure

The determinism check uses the scaffold runtime twice against isolated temporary
directories:

1. Realize `universal-base` with overlays `cli-worker`, `monorepo`,
   `python-package`, and `scheduler`.
2. Capture the generated `docs/governance/scaffold-selection.json` payload.
3. Hash the full generated directory tree, including file content and path
   ordering.
4. Repeat the same realization in a second temporary directory.
5. Compare selection payload equality and full-tree hash equality.

The lane also re-runs the matrix verifier so scaffold behavior remains aligned
with the certified composition contract.
