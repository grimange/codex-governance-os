---
pipeline: 032
title: Establish Template Composition Contract Drift Detection
registry_id: governance.templates.establish-template-composition-contract-drift-detection
stage: protection
governance_layer: codex-governance-os
classification: GOVERNANCE_PROTECTION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 027
  - 028
  - 029
  - 030
  - 031
---

# 032 — Establish Template Composition Contract Drift Detection

## 1. Problem Statement

The Universal Template Composition governance subsystem is now fully established:

- **027** — Composition matrix verified  
- **028** — Canonical composition contract certified  
- **029** — Runtime enforcement implemented  
- **030** — Explainability / doctor surface added  
- **031** — Cross-surface decision consistency verified  

At this stage the contract is correct and stable.

However, the system remains vulnerable to **contract drift** if future changes introduce inconsistencies between:

- the canonical contract document  
- the contract engine implementation  
- manifest declarations  
- scaffold behavior  
- template listing outputs  

Examples of drift scenarios include:

- updating the contract document but not the runtime engine
- changing scaffold behavior without updating the contract
- introducing manifests that violate the certified composition matrix
- tooling implying broader support than the enforcement layer allows

Without automated detection, such drift may go unnoticed until runtime failures occur.

---

## 2. Governance Objective

Install a **contract drift detection layer** that continuously verifies alignment between:

```
universal-template-composition-contract.md
composition_contract.py
manifest definitions
template scaffold behavior
template listing outputs
```

Any divergence between these surfaces must be detected and reported immediately.

---

## 3. Drift Detection Model

The system must treat the following as **authoritative alignment surfaces**:

| Surface | Role |
|-------|------|
| universal-template-composition-contract.md | canonical human-readable contract |
| composition_contract.py | runtime decision authority |
| template_scaffold.py | scaffold admission enforcement |
| list-manifests | manifest compatibility validation |
| list_templates.py | template availability reporting |

All surfaces must reflect the **same supported and rejected matrix**.

---

## 4. Drift Scenarios to Detect

The system must detect the following classes of drift.

### 4.1 Contract → Runtime Drift

Contract lists a supported composition but the runtime engine rejects it.

Example:

```
contract: django + monorepo supported
runtime: unsupported
```

---

### 4.2 Runtime → Contract Drift

Runtime accepts a composition not declared in the contract.

Example:

```
runtime: laravel + cli-worker supported
contract: not present
```

---

### 4.3 Manifest Drift

A template manifest declares a composition that violates the contract.

Example:

```
manifest: django + monorepo
contract: unsupported
```

---

### 4.4 Tooling Surface Drift

A reporting surface implies broader support than enforcement.

Example:

```
list_templates.py reports composition as available
scaffold rejects it
```

---

## 5. Drift Detection Implementation

A new governance verification layer must be introduced.

Suggested test module:

```
tests/governance/test_template_composition_contract_drift.py
```

The tests must:

1. load the contract matrix
2. query the runtime contract engine
3. enumerate manifests
4. compare scaffold and listing surfaces
5. verify identical supported/rejected decisions

If any mismatch is detected, the test must fail.

---

## 6. Fail-Closed Requirement

Contract drift must never silently pass.

If any inconsistency is detected:

```
CONTRACT_DRIFT_DETECTED
```

The verification pipeline must fail immediately.

This prevents silent expansion or erosion of the certified composition matrix.

---

## 7. Artifact Bundle

Artifacts for this pipeline must be recorded under:

```
docs/pipelines/governance/establish-template-composition-contract-drift-detection/
```

Required artifacts:

1. problem-statement.md  
2. contract-authority-surfaces.md  
3. drift-detection-design.md  
4. implementation-summary.md  
5. verification-log.md  
6. drift-simulation-tests.md  
7. final-verdict.md  

---

## 8. Verification Procedure

Run governance verification tests.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected result:

```
Ran XX tests ... OK
```

Drift simulation tests must confirm that mismatches are detected.

Example simulated drift:

- contract entry modified
- runtime engine unchanged

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

## 9. Expected Outcome

After this pipeline:

- the template composition contract becomes self-protecting
- enforcement, documentation, and tooling cannot drift silently
- any misalignment is detected during governance verification
- future template expansions become safer

---

## 10. Final Verdict

Expected verdict:

```
TEMPLATE_COMPOSITION_CONTRACT_DRIFT_PROTECTION_ESTABLISHED
```