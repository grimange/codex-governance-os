# Verification Plan

## Commands Run

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/governance/template_registry.py validate
python tools/governance/template_registry.py build-index
python tools/governance/template_registry.py resolve --template-id pipeline.universal.base
python tools/governance/template_registry.py resolve --family verification --kind base --stack django --mode verification
python tools/governance/template_registry.py list --status active
```

## Verified Behaviors

- valid entry set admits successfully
- malformed or missing-body entries fail admission
- duplicate active resolution keys are blocked
- compiled index is deterministic
- exact resolution works
- agnostic fallback requires explicit opt-in
- restricted templates are blocked without policy allowance
- deprecated templates require explicit opt-in
- archived templates never resolve
