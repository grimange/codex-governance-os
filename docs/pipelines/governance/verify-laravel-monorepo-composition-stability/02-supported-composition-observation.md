# Supported Composition Observation

Observed via:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
```

Observed result:

- `supported: true`
- `normalized_overlays: ["laravel", "monorepo"]`
- `reason_code: "certified-multi-overlay"`
- `decision_source: "docs/contracts/universal-template-composition-contract.md"`

This confirms the newly admitted pair is recognized by the doctor surface as a certified supported composition.
