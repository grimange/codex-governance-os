# Verification Test Design

Pipeline `031` adds `tests/governance/test_template_composition_surface_consistency.py`.

The test suite verifies:

- supported compositions produce matching `requested_overlays`, `normalized_overlays`, `supported`, `reason_code`, and `decision_source` between the contract engine and doctor surface
- supported scaffold realization preserves the same normalized overlay set in `scaffold-selection.json`
- rejected compositions produce matching normalized overlays, support decision, reason code, rejection reason, and decision source between contract, doctor, and scaffold rejection output
- `list-manifests` and `list_templates` emit the same failure payload when manifest drift introduces an unsupported composition

The suite treats any divergence as a hard verification failure.
