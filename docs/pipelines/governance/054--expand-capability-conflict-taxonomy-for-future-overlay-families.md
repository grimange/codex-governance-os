---
pipeline_id: "054"
registry_id: governance.templates.expand-capability-conflict-taxonomy-for-future-overlay-families
title: Expand Capability Conflict Taxonomy for Future Overlay Families
stage: governance
type: architecture-hardening
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 054 — Expand Capability Conflict Taxonomy for Future Overlay Families

## Problem Statement

Pipelines 050–053 introduced and validated the **capability-based template composition system** and admitted the first certified triple-overlay composition.

The capability model now governs template compatibility through:

- capability registry
- capability declarations in template manifests
- capability resolution logic
- composition matrix snapshot
- drift detection verification

However, the current rejection logic still relies on a limited set of implicit conflict explanations.

Examples include:

- `cross-framework application collision`
- `missing Laravel worker composition contract`

As the template ecosystem grows, additional overlay families will be introduced, including:

- schedulers
- framework-managed workers
- standalone service runtimes
- CLI entrypoint overlays
- packaging overlays
- language runtimes
- infrastructure orchestration overlays

Without a formal taxonomy for capability conflicts, rejection reasons may become inconsistent or ambiguous.

The governance system must therefore introduce a **formal conflict taxonomy** that classifies capability conflicts using deterministic reason codes.

---

## Governance Objective

Introduce a canonical **Capability Conflict Taxonomy** that:

- classifies capability conflicts using deterministic categories
- standardizes rejection reason codes
- supports future overlay families
- ensures conflict reasoning remains explainable and consistent
- preserves the current certified composition matrix

---

## Governance Scope

This pipeline introduces the following governance components:

- capability conflict taxonomy definition
- canonical conflict reason codes
- capability registry updates
- conflict resolution classification logic
- documentation updates

---

## Capability Conflict Taxonomy

Introduce the following canonical conflict classes.

### Cross-Framework Collision

Occurs when two full application frameworks attempt to occupy the same runtime.

Example:

```
django + laravel
```

Reason code:

```
cross-framework-application-collision
```

---

### Runtime Ownership Collision

Occurs when multiple overlays attempt to control the same runtime environment.

Example:

```
two runtime overlays providing the same language runtime
```

Reason code:

```
runtime-ownership-collision
```

---

### Worker Model Collision

Occurs when incompatible worker orchestration models are combined.

Example:

```
laravel + cli-worker
```

Laravel already provides framework-managed workers.

Reason code:

```
worker-model-collision
```

---

### Entrypoint Surface Collision

Occurs when multiple overlays attempt to define incompatible application entrypoints.

Examples:

```
web framework + standalone CLI runtime
```

Reason code:

```
entrypoint-surface-collision
```

---

### Package vs Application Role Collision

Occurs when a template attempts to act as both a standalone application and a pure package runtime.

Example:

```
framework overlay combined with package-only runtime overlay
```

Reason code:

```
package-application-role-collision
```

---

### Orchestration Role Collision

Occurs when multiple overlays attempt to control project workspace structure.

Example:

```
multiple orchestration overlays defining incompatible project layouts
```

Reason code:

```
workspace-orchestration-collision
```

---

## Capability Registry Update

Update the capability registry to reference the new conflict taxonomy.

File:

```
tools/governance/template_capability_registry.json
```

The registry must support conflict classifications associated with capability rules.

---

## Capability Resolution Engine Update

Update the conflict resolution logic in:

```
tools/governance/composition_contract.py
```

The engine must:

- detect capability conflicts
- map conflicts to the canonical taxonomy
- return deterministic reason codes

Example output:

```
{
  "supported": false,
  "reason_code": "worker-model-collision"
}
```

---

## Scaffold Enforcement

Ensure the scaffold system exposes taxonomy reason codes.

Command:

```
python tools/governance/template_scaffold.py doctor-composition
```

Example rejection output:

```
explicitly-rejected
reason_code: worker-model-collision
```

---

## Documentation Updates

Update template documentation.

File:

```
docs/codex/templates/README.md
```

Document:

- capability conflict taxonomy
- conflict classification behavior
- canonical reason codes

Also update:

```
docs/governance/template-scaffold-contract.md
```

to describe conflict resolution semantics.

---

## Governance Test Coverage

Extend governance tests to verify taxonomy classification.

Example test file:

```
tests/governance/test_template_capability_conflicts.py
```

Tests must verify:

- framework conflicts return `cross-framework-application-collision`
- worker conflicts return `worker-model-collision`
- runtime conflicts return `runtime-ownership-collision`

Existing tests must continue to pass.

---

## Verification Procedure

Run the following commands.

Verify composition matrix:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

Run governance tests:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected results:

```
composition-matrix: OK
All tests pass
Conflict taxonomy loaded successfully
```

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
expand-capability-conflict-taxonomy-for-future-overlay-families/
```

Artifacts:

```
01-problem-statement.md
02-capability-conflict-taxonomy.md
03-conflict-reason-codes.md
04-capability-registry-update.md
05-capability-resolution-update.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
CAPABILITY_CONFLICT_TAXONOMY_EXPANDED_FOR_FUTURE_OVERLAY_FAMILIES
```

Meaning:

- capability conflicts are now classified using a formal taxonomy
- rejection reasoning is deterministic and explainable
- future overlay families can be introduced safely
- the capability-based composition system is hardened for expansion

---

## Governance Impact

After this pipeline:

- capability conflict reasoning becomes standardized
- rejection messages become deterministic and interpretable
- the composition system becomes scalable for future overlay families
- governance enforcement remains consistent as the ecosystem grows

---

## Next Recommended Pipeline

```
055 — Verify Expanded Capability Conflict Taxonomy Preserves Current Composition Matrix
```

This pipeline will verify that introducing the taxonomy does not alter the currently certified template composition behavior.