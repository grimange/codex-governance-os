# Implementation Plan

## Implemented Surfaces

- family-level template registry extended for `sub_agent` and `report`
- admitted template registry metadata under `docs/governance/registries/templates/entries/`
- compiled registry index at `docs/governance/registries/templates/index.yaml`
- starter admitted template bodies under `docs/codex/templates/`
- registry loader, validator, resolver, list, and index-build commands in `tools/governance/template_registry.py`
- supporting CLI import fixes in governance tooling entrypoints
- expanded verification coverage in `tests/governance/`

## Seeded Starter Set

- universal pipeline template
- django-specialized verification template
- universal safety rule template
- universal discovery skill template
- universal architecture-specialist sub-agent template
- universal governance summary report template
