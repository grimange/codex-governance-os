---
pipeline: 029
title: Enforce Universal Template Composition Contract at Scaffold and Admission Time
registry_id: governance.templates.enforce-universal-template-composition-contract
stage: enforcement
governance_layer: codex-governance-os
classification: GOVERNANCE_ENFORCEMENT
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 023
  - 027
  - 028
---

# 029 — Enforce Universal Template Composition Contract at Scaffold and Admission Time

## 1. Problem Statement

Pipeline 028 certified the **Universal Template Composition Contract** and established the
canonical supported composition matrix.

However, the contract currently exists primarily as:

- documentation
- verification tests
- scaffold realization sweeps

Without enforcement at runtime boundaries, unsupported compositions could still appear through:

- direct manifest editing
- future template tooling drift
- scaffold invocation bypassing verification lanes
- partial overlay injection

This pipeline converts the **composition contract into an executable enforcement boundary**.

The system must fail closed when unsupported template overlay combinations are requested.

---

## 2. Governance Objective

Ensure that **all template composition occurs strictly within the certified matrix** defined in:

```
docs/codex/templates/universal-template-composition-contract.md
```

Unsupported overlay combinations must be **rejected deterministically and consistently**
across all governance and scaffold surfaces.

---

## 3. Certified Composition Matrix

The currently certified **supported compositions** are:

| Composition | Status |
|--------------|--------|
| base-only | supported |
| node-typescript-service + monorepo | supported |
| node-typescript-service + cli-worker | supported |
| cli-worker + monorepo | supported |
| cli-worker + python-package | supported |
| cli-worker + php-package | supported |

---

## 4. Explicit Fail-Closed Boundary

The following combinations must **always be rejected**:

| Composition | Reason |
|--------------|--------|
| laravel + cli-worker | incompatible runtime assumptions |
| django + monorepo | unsupported composition model |
| service + monorepo | scaffold structure conflict |
| laravel + django | cross-framework application collision |

These boundaries must remain **explicitly enforced**.

---

## 5. Enforcement Surfaces

The contract must be enforced at the following runtime surfaces.

### 5.1 Scaffold Generation

When invoking:

```
python tools/governance/template_scaffold.py scaffold
```

the scaffold generator must:

1. Resolve requested overlays.
2. Normalize the overlay set.
3. Validate against the certified matrix.

If unsupported:

- the scaffold must abort
- the system must emit a deterministic rejection message
- no files may be generated

Example rejection:

```
ERROR: unsupported template composition
requested: laravel + cli-worker
allowed: see universal-template-composition-contract.md
```

---

### 5.2 Manifest Admission

When a manifest is loaded or inspected via:

```
template_scaffold.py list-manifests
```

or equivalent governance tooling, the system must:

- validate the declared composition
- reject invalid combinations
- produce structured failure output.

---

### 5.3 Governance Verification

Governance verification commands must also enforce the contract.

Examples:

```
python tools/templates/list_templates.py
python tools/governance/template_scaffold.py list-manifests
```

If a manifest violates the contract:

- verification must fail
- the repository must be classified as **NON-CONFORMANT**.

---

## 6. Implementation Strategy

The enforcement logic should be centralized in a **single contract resolver module**.

Suggested location:

```
tools/templates/composition_contract.py
```

Responsibilities:

- load the canonical composition contract
- normalize overlay combinations
- determine if a composition is supported
- emit deterministic failure reasons.

Suggested function:

```
validate_template_composition(overlays: list[str]) -> ValidationResult
```

ValidationResult should include:

- supported: bool
- normalized_composition
- rejection_reason

All scaffold and governance tooling must call this function.

---

## 7. Fail-Closed Design Requirement

The system must **default to rejection**.

If a composition cannot be resolved or classified:

```
status = UNSUPPORTED
```

This prevents accidental expansion of the supported matrix.

Only explicit updates to the **composition contract** may extend support.

---

## 8. Artifact Bundle

Artifacts for this pipeline must be recorded under:

```
docs/pipelines/governance/enforce-universal-template-composition-contract/
```

Required artifacts:

1. problem-statement.md
2. enforcement-surface-inventory.md
3. contract-enforcement-design.md
4. implementation-summary.md
5. verification-log.md
6. supported-vs-rejected-matrix.md
7. final-verdict.md

---

## 9. Verification Procedure

Run governance and template verification commands.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected result:

```
Ran XX tests ... OK
```

Then validate scaffold and manifest inspection:

```
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
```

The outputs must match the certified matrix.

---

## 10. Expected Outcome

After this pipeline:

- unsupported compositions cannot be scaffolded
- manifests cannot silently violate the contract
- governance tooling consistently enforces the certified matrix
- template composition becomes a **hard governance boundary**

---

## 11. Final Verdict

Expected verdict:

```
UNIVERSAL_TEMPLATE_COMPOSITION_CONTRACT_ENFORCED_FAIL_CLOSED
```

This confirms that the composition contract is now:

- canonical
- executable
- fail-closed
- governance-enforced