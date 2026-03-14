# Current Boundary Observation

Observed via:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
```

Current result:

- `supported: false`
- `normalized_overlays: ["laravel", "monorepo"]`
- `reason_code: "unsupported"`
- `rejection_reason: "not present in certified composition matrix"`
- `decision_source: "docs/contracts/universal-template-composition-contract.md"`

This is a generic unsupported decision, not an explicit fail-closed boundary. The doctor surface also reports nearby supported compositions:

- `django + monorepo`
- `service + monorepo`
- `node-typescript-service + monorepo`
- `cli-worker + monorepo`

That adjacency matters because it implies the monorepo side of the composition model is already governed and reusable.
