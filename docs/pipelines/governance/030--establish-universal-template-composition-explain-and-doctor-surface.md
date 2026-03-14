---
pipeline: 030
title: Establish Universal Template Composition Explain and Doctor Surface
registry_id: governance.templates.establish-universal-template-composition-explain-and-doctor-surface
stage: observability
governance_layer: codex-governance-os
classification: GOVERNANCE_EXPLAINABILITY
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 027
  - 028
  - 029
---

# 030 — Establish Universal Template Composition Explain and Doctor Surface

## 1. Problem Statement

Pipeline 028 certified the **Universal Template Composition Contract**.

Pipeline 029 enforced the contract at runtime through:

- scaffold generation
- manifest inspection
- template listing surfaces

The system now correctly **fails closed** when unsupported overlay combinations are requested.

However, enforcement alone is insufficient for operational usability. When a composition fails, operators and agents must be able to determine:

- why the request was rejected
- how the overlay set was normalized
- which compositions are actually supported
- what alternatives exist within the certified matrix

Without an explainability surface, unsupported composition errors become difficult to diagnose and may lead to repeated invalid requests.

This pipeline introduces a **composition explain and doctor surface** that provides structured diagnostics for all template composition decisions.

---

## 2. Governance Objective

Expose a deterministic explanation surface for template composition validation so that:

- humans can understand rejection decisions
- Codex agents can diagnose composition errors programmatically
- governance tooling can produce consistent diagnostics
- enforcement decisions become transparent and auditable

This surface must **interpret the composition contract**, not modify it.

---

## 3. Doctor Surface Definition

A new diagnostic command must be introduced.

Example command:

```
python tools/governance/template_scaffold.py doctor-composition
```

Example invocation:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker
```

The command must:

1. Normalize the overlay set.
2. Validate the composition through `composition_contract.py`.
3. Return structured diagnostic output.

---

## 4. Structured Diagnostic Output

Doctor responses must include:

| Field | Description |
|------|-------------|
| requested_overlays | overlays provided by the user |
| normalized_overlays | overlays after normalization |
| supported | true/false decision |
| decision_source | contract authority file |
| rejection_reason | explanation if unsupported |
| closest_supported | suggested supported combinations |

Example output:

```json
{
  "requested_overlays": ["laravel", "cli-worker"],
  "normalized_overlays": ["laravel", "cli-worker"],
  "supported": false,
  "decision_source": "universal-template-composition-contract.md",
  "rejection_reason": "combination not present in certified multi-overlay allowlist",
  "closest_supported": [
    ["cli-worker", "python-package"],
    ["cli-worker", "php-package"]
  ]
}
```

---

## 5. Integration Surfaces

The doctor/explain capability must integrate with the following tooling.

### 5.1 Scaffold Generator

When scaffold validation fails:

```
template_scaffold.py scaffold
```

the error output must include the **doctor explanation summary**.

Example:

```
ERROR: unsupported template composition

requested: laravel + cli-worker
reason: combination not present in certified multi-overlay allowlist

Run:
template_scaffold.py doctor-composition --overlays laravel cli-worker
```

---

### 5.2 Manifest Inspection

When manifest compatibility fails during:

```
template_scaffold.py list-manifests
```

the failure must reference the same diagnostic explanation.

---

### 5.3 Template Listing

The following command must remain aligned with the contract:

```
python tools/templates/list_templates.py
```

If composition inconsistencies are discovered, the doctor surface must be referenced in diagnostics.

---

## 6. Implementation Strategy

All explanation logic must reuse the existing validation module:

```
tools/templates/composition_contract.py
```

Suggested extension:

```
explain_template_composition(overlays: list[str]) -> CompositionExplanation
```

Suggested structure:

```
CompositionExplanation:
    requested_overlays
    normalized_overlays
    supported
    rejection_reason
    closest_supported
```

The doctor command becomes a **thin wrapper** around this explanation surface.

---

## 7. Fail-Closed Guarantee

The explain/doctor surface must **never expand support**.

It must:

- interpret the certified contract
- describe validation decisions
- suggest alternatives only from the supported matrix

Unsupported combinations must remain unsupported unless the contract is updated through governance pipelines.

---

## 8. Artifact Bundle

Artifacts for this pipeline must be recorded under:

```
docs/pipelines/governance/establish-universal-template-composition-explain-and-doctor-surface/
```

Required artifacts:

1. problem-statement.md
2. composition-decision-explainability-design.md
3. doctor-command-specification.md
4. implementation-summary.md
5. verification-log.md
6. explanation-sample-outputs.md
7. final-verdict.md

---

## 9. Verification Procedure

Run governance tests.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected result:

```
Ran XX tests ... OK
```

Then test doctor responses.

Example supported case:

```
doctor-composition --overlays cli-worker python-package
```

Expected result:

```
supported: true
```

Example unsupported case:

```
doctor-composition --overlays laravel cli-worker
```

Expected result:

```
supported: false
reason: not present in certified multi-overlay allowlist
```

---

## 10. Expected Outcome

After this pipeline:

- template composition decisions become explainable
- governance tooling exposes structured diagnostics
- operators and agents can quickly diagnose invalid compositions
- enforcement remains strictly fail-closed

The composition contract becomes:

- canonical
- enforced
- observable
- explainable

---

## 11. Final Verdict

Expected verdict:

```
UNIVERSAL_TEMPLATE_COMPOSITION_EXPLAINABILITY_ESTABLISHED
```