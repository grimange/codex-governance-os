---
pipeline: 036
title: Close Service and Monorepo Template Composition Boundary
registry_id: governance.templates.close-service-monorepo-template-composition-boundary
stage: expansion
governance_layer: codex-governance-os
classification: GOVERNANCE_EXPANSION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 033
  - 034
  - 035
---

# 036 — Close Service and Monorepo Template Composition Boundary

## 1. Problem Statement

The Universal Template Composition system still defines several **explicit fail-closed boundaries**.

After pipeline **033**, the `django + monorepo` boundary was successfully closed and promoted into the supported matrix.

The remaining rejected compositions are:

| Composition | Status |
|-------------|--------|
| service + monorepo | unsupported |
| laravel + cli-worker | unsupported |
| laravel + django | unsupported |

The `service + monorepo` rejection exists primarily because the system previously lacked a canonical structure for placing **generic service templates inside monorepos**.

With the Django monorepo layout now established, the system already contains a partial foundation for nested service placement.

This pipeline closes the **service + monorepo** boundary by defining a canonical service placement model and extending scaffold generation accordingly.

---

## 2. Governance Objective

Promote the composition:

```
service + monorepo
```

from **unsupported** to **certified supported**, while maintaining:

- deterministic scaffold generation
- manifest compatibility
- enforcement alignment
- explainability consistency
- contract drift protection

The expansion must preserve the system’s **fail-closed safety guarantees**.

---

## 3. Current Rejection Reason

The combination is currently rejected due to the absence of:

- a canonical directory structure for generic services within a monorepo
- defined ownership boundaries between service overlays and monorepo root
- deterministic scaffold placement rules
- manifest metadata describing nested service placement

Without these definitions, scaffold generation cannot safely compose the overlays.

---

## 4. Canonical Monorepo Layout for Generic Services

The following layout becomes the canonical scaffold result for a service within a monorepo.

```
repo-root/
│
├─ services/
│   └─ service-app/
│       ├─ src/
│       ├─ tests/
│       ├─ pyproject.toml or package.json
│       ├─ README.md
│       └─ service_entrypoint
│
├─ packages/
│
├─ docs/
│
├─ .codex/
│
├─ AGENTS.md
└─ README.md
```

### Ownership Model

| Location | Ownership |
|---------|-----------|
| repo root | monorepo overlay |
| services/service-app | service overlay |
| .codex | governance root |
| docs | repository documentation |

---

## 5. Manifest Model

Service manifests must support monorepo placement metadata.

Example manifest structure:

```
type: service
overlay: service
placement: services/service-app
repository_structure: monorepo
```

The scaffold generator must interpret these values when resolving overlays.

---

## 6. Scaffold Generator Changes

The scaffold system must now support the following overlay composition model:

- monorepo overlay defines repository root structure
- service overlay generates the service within the defined placement directory
- governance files remain at repository root
- overlay ownership boundaries remain deterministic

Scaffold generation must remain reproducible.

---

## 7. Composition Contract Update

The composition contract must be updated.

File:

```
docs/codex/templates/universal-template-composition-contract.md
```

Add to the supported matrix:

| Composition |
|-------------|
| service + monorepo |

Remove the pair from the rejection matrix.

---

## 8. Enforcement Updates

The following components must recognize the new supported composition:

- `composition_contract.py`
- scaffold enforcement logic
- manifest validation
- doctor-composition output
- template listing surfaces

All surfaces must remain consistent with the updated contract.

---

## 9. Verification Requirements

The pipeline must prove that the new composition works correctly.

Verification steps:

1. Scaffold generation succeeds.

```
template_scaffold.py scaffold --overlays service monorepo
```

2. Generated repository layout matches the canonical structure.

3. Manifest validation accepts the composition.

4. Doctor surface reports:

```
supported: true
```

5. Cross-surface consistency tests still pass.

6. Drift detection continues to detect simulated divergence.

---

## 10. Test Coverage

New tests should be introduced:

```
tests/governance/test_service_monorepo_composition.py
```

Tests must confirm:

- scaffold layout correctness
- manifest compatibility
- contract alignment
- enforcement behavior
- doctor surface correctness

---

## 11. Artifact Bundle

Artifacts must be recorded under:

```
docs/pipelines/governance/close-service-monorepo-template-composition-boundary/
```

Required artifacts:

1. problem-statement.md  
2. boundary-diagnosis.md  
3. canonical-service-monorepo-layout.md  
4. scaffold-implementation-summary.md  
5. verification-log.md  
6. expanded-composition-matrix.md  
7. final-verdict.md  

---

## 12. Expected Outcome

After this pipeline:

- `service + monorepo` becomes a certified supported composition
- generic services can be safely scaffolded within monorepos
- governance enforcement and explainability surfaces remain aligned
- the universal template composition matrix expands safely

---

## 13. Final Verdict

Expected verdict:

```
SERVICE_MONOREPO_TEMPLATE_COMPOSITION_BOUNDARY_CLOSED
```