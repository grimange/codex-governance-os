# Capability Scoring Model

Pipeline 164 implements the following deterministic domain scoring model:

```text
domain_score = (verified_capabilities / declared_capabilities) * 100
```

Interpretation used in this lane:

- a capability is treated as verified when its registry status is `complete`
- a capability is treated as unverified when it exists in the registry but is
  not yet `complete`
- a capability is treated as invalid state when the maturity domain expects it
  but it is absent from the capability registry

Current computed domain scores:

- `codex_governance_layer`: `100`
- `pipeline_governance`: `100`
- `passive_observation`: `100`
- `autonomous_governance_loop`: `0`
- `multi_agent_governance`: `0`
- `architecture_advisor`: `0`

Current overall system maturity:

- `50`
