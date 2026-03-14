---
pipeline_id: "052"
registry_id: governance.templates.admit-first-capability-composed-triple-overlay
title: Admit First Capability-Composed Triple Overlay
stage: expansion
type: capability-expansion
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 052 — Admit First Capability-Composed Triple Overlay

## Problem Statement

Pipelines 050 and 051 introduced and verified the **capability-based template composition system**.

Key governance capabilities now exist:

- capability registry (`template_capability_registry.json`)
- capability declarations in template manifests
- capability resolution in `composition_contract.py`
- scaffold validation through `template_scaffold.py`
- preservation verification of the certified pairwise composition matrix

However, all currently certified compositions remain **pairwise overlays**.

To prove that the capability architecture supports scalable composition, the governance system must admit the **first certified triple-overlay composition**.

This pipeline introduces the first capability-composed triple overlay using the newly established capability registry.

---

## Governance Objective

Admit a three-overlay composition that:

- satisfies all capability requirements
- introduces no capability conflicts
- preserves existing certified behavior
- validates that the capability resolution engine supports multi-overlay composition

This pipeline provides the first operational proof that the template composition system can scale beyond pairwise overlay compatibility.

---

## Candidate Triple Overlay

The triple overlay selected for admission:

```
cli-worker + monorepo + python-package
```

Overlay roles:

| Overlay | Role |
|--------|------|
| cli-worker | worker runtime |
| monorepo | workspace orchestration |
| python-package | package runtime |

This combination extends the already certified pair:

```
cli-worker + python-package
```

and introduces the **workspace orchestration capability** without introducing runtime conflicts.

---

## Capability Compatibility Validation

The capability resolution engine must verify that the following capabilities are compatible.

### CLI Worker

```
provides:
  - worker-runtime
```

### Python Package

```
provides:
  - python-runtime
  - package-runtime
```

### Monorepo

```
provides:
  - workspace-orchestration
```

Capability resolution must confirm:

- no capability conflicts exist
- no required capabilities are missing
- composition roles do not collide

---

## Composition Admission

The following composition becomes certified.

```
cli-worker + monorepo + python-package
```

Expected classification:

```
certified-multi-overlay
```

This composition must be admitted through the capability resolution engine without introducing special-case pair rules.

---

## Composition Matrix Update

Update the canonical matrix snapshot.

File:

```
tools/governance/template_composition_matrix.json
```

Add entry under supported compositions:

```
["cli-worker", "monorepo", "python-package"]
```

The snapshot must remain consistent with runtime composition behavior.

---

## Scaffold Composition Verification

Verify scaffold behavior.

Run:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays cli-worker monorepo python-package
```

Expected output:

```
certified-multi-overlay
```

---

## Governance Test Coverage

Extend governance tests to cover triple-overlay composition.

Example test file:

```
tests/governance/test_template_capability_composition.py
```

Required test:

```
cli-worker + monorepo + python-package -> certified-multi-overlay
```

Tests must verify:

- capability compatibility
- absence of conflicts
- deterministic scaffold classification

---

## Verification Procedure

Run the following verification commands.

Verify composition matrix:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

Verify the triple overlay directly:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays cli-worker monorepo python-package
```

Run governance tests:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected results:

```
composition-matrix: OK
All tests pass
Triple overlay admitted successfully
```

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
admit-first-capability-composed-triple-overlay/
```

Artifacts:

```
01-problem-statement.md
02-capability-compatibility-analysis.md
03-triple-overlay-admission.md
04-composition-matrix-update.md
05-governance-test-coverage.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
FIRST_CAPABILITY_COMPOSED_TRIPLE_OVERLAY_ADMITTED
```

Meaning:

- the capability architecture successfully supports triple-overlay composition
- capability resolution correctly validates compatibility
- the composition matrix remains deterministic
- the template system now supports scalable multi-overlay composition

---

## Governance Impact

After this pipeline:

- the capability-based composition system is operationally validated
- multi-overlay template composition becomes a governed capability
- the template ecosystem can scale without pairwise rule explosion
- the governance system transitions to **universal template composition**

---

## Next Recommended Pipeline

```
053 — Reverify Template Composition Matrix After Triple Overlay Admission
```

This pipeline will confirm that admitting the first triple overlay does not introduce composition drift or unexpected compatibility changes.