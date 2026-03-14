# Quadruple Composition Contract

## Certified Supported Stack

`cli-worker + monorepo + python-package + scheduler`

## Canonical Surface Expectations

The governed scaffold must include at minimum:

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

## Contract Rule

The quadruple is supported only when admitted by:

- the certified runtime matrix
- the compound certification ledger
- scaffold realization logic
- governance test coverage

Pairwise and triple support are necessary but not sufficient evidence on their
own.
