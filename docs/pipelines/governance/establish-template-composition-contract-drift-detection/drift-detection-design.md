# Drift Detection Design

## Implementation Shape

Pipeline `032` extends `tools/templates/composition_contract.py` with:

- `load_contract_document_matrix(...)`
- `detect_contract_drift(...)`
- structured report types for contract-document and runtime alignment

## Detection Rules

- documented supported multi-overlay pairs must exist in the runtime engine
- runtime-supported multi-overlay pairs must be documented
- documented rejected pairs must exist in the runtime engine rejection set
- runtime-rejected pairs must be documented
- the contract document must retain admitted non-composite rules for `base-only` and single-overlay realization
- manifest inventory drift is folded into the same report so runtime and manifest mismatches are classified together

## Fail-Closed Rule

Any inconsistency produces `CONTRACT_DRIFT_DETECTED` entries in the report and fails verification.
