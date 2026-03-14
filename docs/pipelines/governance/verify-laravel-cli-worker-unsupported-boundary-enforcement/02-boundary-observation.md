# Boundary Observation

Observed via:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
```

Result:

- `supported: false`
- `normalized_overlays: ["cli-worker", "laravel"]`
- `reason_code: "explicitly-rejected"`
- `rejection_reason: "missing Laravel worker composition contract"`
- `decision_source: "docs/contracts/universal-template-composition-contract.md"`

This confirms the pair is rejected as an explicit policy boundary, not as an unclassified unsupported request.
