---
pipeline_id: "051"
registry_id: governance.templates.verify-capability-registry-preserves-certified-composition-matrix
title: Verify Capability Registry Preserves Certified Composition Matrix
stage: verification
type: reverification
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 051 — Verify Capability Registry Preserves Certified Composition Matrix

## Problem Statement

Pipeline 050 introduced a capability-based template composition architecture.

Key new governance surfaces were introduced:

- `template_capability_registry.json`
- capability declarations in template manifests
- capability validation logic in `composition_contract.py`
- runtime enforcement through `template_scaffold.py`
- governance test coverage for capability resolution

The capability model enables universal template composition while preserving the existing certified matrix.

However, introducing a new composition engine creates a risk:

The capability resolution logic might unintentionally alter existing composition behavior.

The governance system must therefore perform a dedicated verification to confirm that the capability registry preserves the currently certified template composition matrix.

---

## Governance Objective

Verify that the capability registry and resolution engine produce **exactly the same composition outcomes** as the previously certified matrix.

This verification confirms that:

- supported compositions remain supported
- unsupported compositions remain rejected
- canonical rejection reasons remain consistent
- the capability system introduces no behavioral drift

---

## Verification Scope

This pipeline verifies the following governance surfaces:

- template capability registry
- template manifest capability declarations
- capability resolution logic
- scaffold composition enforcement
- governance composition tests
- canonical matrix snapshot

---

## Certified Supported Compositions

The following compositions must remain supported.

```
laravel + monorepo
service + monorepo
cli-worker + monorepo
cli-worker + python-package
```

Expected classification:

```
certified-multi-overlay
```

The capability resolution engine must return the same classification.

---

## Explicit Unsupported Compositions

The following compositions must remain rejected.

### Laravel worker conflict

```
laravel + cli-worker
```

Expected classification:

```
explicitly-rejected
```

Canonical reason:

```
missing Laravel worker composition contract
```

---

### Cross-framework conflict

```
django + laravel
```

Expected classification:

```
explicitly-rejected
```

Canonical reason:

```
cross-framework application collision
```

---

## Capability Registry Verification

Verify the capability registry loads successfully.

File:

```
tools/governance/template_capability_registry.json
```

Confirm that:

- the capability registry parses correctly
- declared capabilities match manifest capability declarations
- no undefined capabilities are referenced

---

## Manifest Capability Verification

Verify template manifests declare valid capability metadata.

Example manifest location:

```
docs/codex/templates/manifests/
```

Each manifest must satisfy:

- declared capabilities exist in the capability registry
- `provides`, `requires`, and `conflicts` fields are valid
- no capability collisions occur in certified compositions

---

## Capability Resolution Verification

Verify the runtime capability resolution engine.

File:

```
tools/governance/composition_contract.py
```

Confirm that:

- required capabilities are satisfied
- conflicts are detected
- composition roles do not collide
- certified compositions remain allowed
- unsupported compositions remain rejected

---

## Scaffold Enforcement Verification

Verify scaffold behavior remains correct.

Run:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

Expected output:

```
composition-matrix: OK
```

JSON output:

```
{"valid": true, "errors": []}
```

---

## Governance Test Suite

Run governance tests.

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected result:

```
All tests pass
```

The following tests must validate capability preservation:

```
test_template_capability_composition.py
test_template_composition_matrix.py
test_template_composition_drift.py
```

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
verify-capability-registry-preserves-certified-composition-matrix/
```

Artifacts:

```
01-problem-statement.md
02-certified-composition-verification.md
03-unsupported-boundary-verification.md
04-capability-registry-validation.md
05-capability-resolution-verification.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
CAPABILITY_REGISTRY_PRESERVES_CERTIFIED_TEMPLATE_COMPOSITION_MATRIX
```

Meaning:

- the capability registry introduces no composition drift
- certified template compositions remain preserved
- unsupported boundaries remain enforced
- the capability system is safe to expand

---

## Governance Impact

After this pipeline:

- the capability registry becomes a verified authority surface
- capability-based composition is proven to preserve existing governance contracts
- future overlays can safely rely on capability declarations
- the template composition system transitions fully to capability-driven architecture

---

## Next Recommended Pipeline

```
052 — Admit First Capability-Composed Triple Overlay
```

This pipeline will introduce the first three-overlay composition using the new capability model, proving that the system now supports scalable universal template composition.