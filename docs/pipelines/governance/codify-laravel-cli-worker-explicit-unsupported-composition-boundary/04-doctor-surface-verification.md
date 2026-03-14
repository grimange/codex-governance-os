# Doctor Surface Verification

Command:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
```

Expected diagnostic:

- `supported: false`
- `normalized_overlays: ["cli-worker", "laravel"]`
- `reason_code: "explicitly-rejected"`
- `rejection_reason: "missing Laravel worker composition contract"`

This confirms the doctor surface reports the boundary as an intentional unsupported composition rather than an ambiguous generic failure.
