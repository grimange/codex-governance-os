# Governance Framework Overview

## Layers

- Governance doctrine layer: reusable rules in `docs/governance/` define lifecycle, artifact, naming, terminology, and skill-selection behavior.
- Universal skills layer: reusable operational skills provide discovery, audit, doctrine, contract, remediation, verification, registry, and bootstrap workflows.
- Pipeline lifecycle layer: pipeline definitions under `docs/pipelines/governance/` define ordered phases, outputs, and decisions.
- Bootstrap layer: `docs/bootstrap/` explains inheritance, override, minimal setup, and example repository layout.

## Operating Model

The framework works by combining:

- doctrine for rules
- skills for repeatable procedures
- pipelines for deterministic execution
- artifacts for durable evidence

Local repositories inherit the generic baseline, then add repository-specific doctrine, contracts, pipelines, and optional local skills as needed.

## Practical Interpretation

- Small repositories usually use the bootstrap, discovery, doctrine, and readiness surfaces first.
- Larger repositories continue into contract, audit, remediation, verification, and promotion workflows once explicit subsystem governance is needed.
- The framework stays domain-neutral because it governs repository process rather than a specific runtime architecture.
