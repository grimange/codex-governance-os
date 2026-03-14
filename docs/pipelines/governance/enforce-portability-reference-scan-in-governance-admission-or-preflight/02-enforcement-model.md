# Enforcement Model

The repository now uses a deterministic portability scan implemented in
`tools/governance/portability_scan.py`.

Canonical enforcement path:

1. run `python tools/governance/preflight.py`
2. preflight executes the active governed-surface portability scan
3. any classified violation returns a non-zero exit code
4. governed execution must treat that result as a fail-closed preflight block

The preflight entrypoint is the repository's documented governance preflight
surface. This lane does not claim invisible background automation beyond that
entrypoint.
