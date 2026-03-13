# Fixture And Test Expansion

## New Supported Fixture Classes

- node-typescript-service
- cli-worker
- node-typescript-service-in-monorepo
- python-cli-worker

## Expanded Verification Surfaces

- `tests/governance/test_template_scaffold.py`
- `tests/governance/test_template_conformance.py`

## Coverage Added

- manifest inventory includes the new overlays
- repository realization proves file and directory surfaces for the new overlays
- overlay compatibility and incompatibility are both tested
- conformance matrix now includes the previously unsupported classes
