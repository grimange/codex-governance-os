# Composition Decision Explainability Design

## Design Rule

Explainability must interpret the certified contract, not create a second policy surface.

## Implementation Shape

- `tools/templates/composition_contract.py` now exposes `explain_template_composition(...)`
- explanation output is derived from the same normalized overlay set and validation decision used by enforcement
- closest supported suggestions are drawn only from the certified multi-overlay matrix

## Explanation Fields

- `requested_overlays`
- `normalized_overlays`
- `supported`
- `decision_source`
- `rejection_reason`
- `closest_supported`
- `reason_code`

## Non-Goal

The explain surface does not admit new compositions and does not override fail-closed enforcement.
