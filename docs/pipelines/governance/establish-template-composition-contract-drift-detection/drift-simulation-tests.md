# Drift Simulation Tests

Pipeline `032` added the following simulations in `tests/governance/test_template_composition_contract_drift.py`:

## Contract Document Drift

- copy the certified contract to a temporary file
- inject an extra rejected pair: `django + cli-worker`
- run `detect_contract_drift(...)`
- expect `CONTRACT_DRIFT_DETECTED: contract documents rejection missing from runtime cli-worker + django`

## Manifest Drift

- copy the manifest inventory to a temporary directory
- edit `laravel.json` to declare compatibility with `cli-worker`
- run `detect_contract_drift(...)`
- expect `CONTRACT_DRIFT_DETECTED` with the unsupported manifest composition message

## Live Alignment

- load the current contract document and live manifest inventory
- verify that the drift report is valid in the committed repository state
