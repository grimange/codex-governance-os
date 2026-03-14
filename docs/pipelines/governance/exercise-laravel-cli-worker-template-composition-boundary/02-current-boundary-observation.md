# Current Boundary Observation

## Doctor Output

Command:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
```

Observed result:

- `supported: false`
- `normalized_overlays: ["cli-worker", "laravel"]`
- `reason_code: "explicitly-rejected"`
- `rejection_reason: "incompatible runtime assumptions"`
- `decision_source: "docs/contracts/universal-template-composition-contract.md"`

The doctor surface does not treat the pair as merely absent from the allowlist. It reports an explicit rejection sourced from the certified composition contract.

## Existing Verification Surface

[tests/governance/test_template_composition_post_service_monorepo_protections.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_post_service_monorepo_protections.py) includes `["laravel", "cli-worker"]` in the rejected matrix and verifies three fail-closed properties:

- doctor output remains rejected
- scaffold realization raises `RegistryError`
- runtime or manifest attempts to admit the pair are classified as contract drift

This means the current boundary is already enforced, explained, and protected against silent expansion.
