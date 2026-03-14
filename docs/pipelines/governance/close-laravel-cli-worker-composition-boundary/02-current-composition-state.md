# Current Composition State

The live doctor surface reports:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
```

Observed state:

- `supported: false`
- `reason_code: explicitly-rejected`
- `rejection_reason: missing Laravel worker composition contract`
- `decision_source: docs/contracts/universal-template-composition-contract.md`

Manifest inventory remains fail-closed:

- [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json) does not declare `cli-worker`
- [cli-worker.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/cli-worker.json) does not declare `laravel`
