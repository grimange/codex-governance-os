# Scaffold Generation Expectations

The certified quadruple stack realizes as the deterministic union of the
already governed worker, topology, Python package, and scheduler surfaces.

## Expected Governed Surfaces

- worker surfaces
  - `bin`
  - `jobs`
  - `worker`
- monorepo topology
  - `packages`
  - `services`
  - `shared`
- Python package surfaces
  - `src`
  - `tests`
  - `docs`
- scheduler surfaces
  - `scheduler`
  - `scheduler/schedule.py`
  - `scheduler/scheduler_runtime.py`

## Determinism Rule

There are no new compound override rules in this lane. Determinism comes from:

- stable overlay normalization order
- stable surface sorting before scaffold write
- stable `scaffold-selection.json` payload generation
- already governed deterministic scheduler file rendering

Repeated-run determinism remains a separate verification concern for the
follow-up quadruple verification lane.
