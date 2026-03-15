# State Generation Engine

The self-inspection engine generates `docs/governance/governance-system-state.json`
with the following derived fields:

- `governance_maturity_estimate`
- `trend_classification`
- `layers`
- `capabilities`
- `capability_snapshot`
- `bounded_constraints`
- `capability_sources`
- `maturity_sources`
- `evidence_inventory`

The JSON surface is regenerated from repository evidence and is intended to be
the machine-readable governance truth surface used by later introspection and
maturity-computation lanes.
