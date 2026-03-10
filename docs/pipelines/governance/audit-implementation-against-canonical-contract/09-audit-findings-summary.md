# Audit Findings Summary

## Compliant Areas

- The authority stack is explicit and coherent across `AGENTS.md`, `.codex/AGENTS.md`, doctrine, contract, and registry.
- Registered pipeline entries are structurally valid, non-duplicated, and point to real files.
- The registry is still treated as a discoverability surface rather than a source of procedural truth.
- Placeholder category roots are not being misrepresented as active pipelines.

## Partial Compliance

- Active-pipeline state ownership is correct, but the update discipline is inconsistent.
- Lifecycle vocabulary is only partially aligned because several active definitions still say `PROPOSED`.
- The registry provides most active governance coverage, but not all of it.

## Major Violations

- Pipeline `005` is operationally active during this audit and is absent from `docs/pipelines/registry/pipeline-registry.md`.
- Same-change-set activation discipline is not being met for the current pipeline execution.

## Ambiguous Surfaces

- `006` and `007` are concrete pipeline definitions but this audit found no direct evidence that they are already operationally active.

## Legacy Influence

- Transitional tolerance for `PROPOSED` labels and delayed registry updates persists from earlier governance work and still affects current behavior.

## Overall Compliance Posture

The implementation is partially compliant. The subsystem design and registered entries conform to the contract, but current operational practice still violates the contract's core rule that active pipelines must be published in the registry without delay.
