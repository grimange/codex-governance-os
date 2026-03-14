---
pipeline_id: "055"
registry_id: governance.templates.verify-expanded-capability-conflict-taxonomy-preserves-current-composition-matrix
title: Verify Expanded Capability Conflict Taxonomy Preserves Current Composition Matrix
stage: verification
type: reverification
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 055 — Verify Expanded Capability Conflict Taxonomy Preserves Current Composition Matrix

## Problem Statement

Pipeline 054 introduced a **formal capability conflict taxonomy** to support scalable template composition governance.

The taxonomy defined canonical conflict classes such as:

- cross-framework-application-collision
- runtime-ownership-collision
- worker-model-collision
- entrypoint-surface-collision
- package-application-role-collision
- workspace-orchestration-collision

The capability resolution engine now maps capability conflicts to these standardized reason codes.

Although this improves rejection clarity and future extensibility, introducing new conflict classification logic may unintentionally alter previously certified composition behavior.

The governance system must therefore verify that the expanded conflict taxonomy **does not modify the currently certified template composition matrix**.

---

## Governance Objective

Confirm that introducing the capability conflict taxonomy preserves the current certified composition outcomes.

Specifically verify that:

- certified compositions remain supported
- unsupported compositions remain rejected
- rejection reason codes now map correctly to the new taxonomy
- scaffold behavior remains deterministic
- the canonical matrix snapshot remains valid
- drift detection continues to succeed

---

## Verification Scope

This pipeline verifies the following governance surfaces:

- capability registry
- capability conflict taxonomy
- composition resolution engine
- scaffold composition enforcement
- template composition matrix snapshot
- governance test suite

---

## Certified Supported Compositions

The following compositions must remain certified.

### Pair Compositions

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

---

### Triple Composition

```
cli-worker + monorepo + python-package
```

Expected classification:

```
certified-multi-overlay
```

---

## Explicit Unsupported Compositions

The following compositions must remain explicitly rejected.

### Laravel worker conflict

```
laravel + cli-worker
```

Expected classification:

```
explicitly-rejected
```

Expected taxonomy reason code:

```
worker-model-collision
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

Expected taxonomy reason code:

```
cross-framework-application-collision
```

---

## Composition Matrix Snapshot Verification

Verify the canonical matrix snapshot.

File:

```
tools/governance/template_composition_matrix.json
```

Confirm the snapshot still includes:

```
["cli-worker", "monorepo", "python-package"]
```

The snapshot must match runtime classification.

---

## Capability Registry Verification

Verify the capability registry loads successfully.

File:

```
tools/governance/template_capability_registry.json
```

Confirm that:

- all capabilities referenced by manifests exist
- conflict taxonomy mappings are present
- registry validation succeeds

---

## Scaffold Composition Verification

Verify scaffold behavior.

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

### Direct Conflict Verification

Verify taxonomy classification.

Run:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker
```

Expected result:

```
explicitly-rejected
reason_code: worker-model-collision
```

Run:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays django laravel
```

Expected result:

```
explicitly-rejected
reason_code: cross-framework-application-collision
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

Tests must confirm:

- certified compositions remain unchanged
- conflict taxonomy reason codes are correctly returned
- matrix verification continues to succeed
- drift detection remains operational

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
verify-expanded-capability-conflict-taxonomy-preserves-current-composition-matrix/
```

Artifacts:

```
01-problem-statement.md
02-certified-composition-verification.md
03-conflict-taxonomy-verification.md
04-capability-registry-validation.md
05-scaffold-verification.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
CAPABILITY_CONFLICT_TAXONOMY_PRESERVES_CERTIFIED_COMPOSITION_MATRIX
```

Meaning:

- the conflict taxonomy introduces no composition drift
- certified compositions remain supported
- unsupported boundaries remain enforced
- taxonomy reason codes are now deterministic
- the template composition system remains stable

---

## Governance Impact

After this pipeline:

- the capability conflict taxonomy becomes a verified governance surface
- rejection reasoning becomes standardized and deterministic
- template composition remains fully stable
- the system is ready to admit new overlay families safely

---

## Next Recommended Pipeline

```
056 — Introduce Scheduler Overlay Capability Family
```

This pipeline will introduce the first new overlay family using the capability taxonomy, validating that future composition expansions can be governed safely.