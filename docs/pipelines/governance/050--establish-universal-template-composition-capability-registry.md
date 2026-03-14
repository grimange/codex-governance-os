---
pipeline_id: "050"
registry_id: governance.templates.establish-universal-template-composition-capability-registry
title: Establish Universal Template Composition Capability Registry
stage: governance
type: architecture
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 050 — Establish Universal Template Composition Capability Registry

## Problem Statement

Pipelines 045–049 established a stable and governed template composition system:

- supported template overlays are explicitly certified
- unsupported combinations are explicitly rejected
- the composition matrix is verified
- continuous drift detection is now enforced

However, the current system expresses composition truth primarily through **pairwise overlay compatibility rules**.

This model works for small overlay sets but does not scale well when additional overlays are introduced.

Future overlays may include capabilities such as:

- queue workers
- schedulers
- background workers
- monorepo orchestration
- CLI entrypoints
- runtime services
- package overlays

Under a pairwise model, the number of compatibility combinations grows rapidly and becomes difficult to govern.

The governance system must introduce a **capability-based composition model** that allows overlays to declare:

- what they provide
- what they require
- what they conflict with

This enables a universal composition engine capable of supporting future overlays without expanding the matrix exponentially.

---

## Governance Objective

Introduce a canonical **Template Composition Capability Registry** that allows overlays and templates to declare composition capabilities.

Composition compatibility will be determined through capability relationships rather than only pairwise overlay rules.

The existing matrix remains the **certified baseline**, and the capability system must preserve current behavior.

---

## Governance Scope

This pipeline introduces the following components:

- capability registry schema
- capability declaration fields in template manifests
- capability resolution logic
- compatibility verification against the existing composition matrix
- governance documentation updates

---

## Capability Model

Each template overlay may declare capability metadata.

Example capability fields:

```
provides
requires
conflicts
composition_role
```

Example manifest capability declaration:

```
capabilities:
  provides:
    - web-framework
    - http-runtime

  requires:
    - runtime-environment

  conflicts:
    - alternate-web-framework

  composition_role: framework
```

---

## Example Capability Definitions

Example capabilities for current overlays.

### Laravel

```
provides:
  - web-framework
  - php-runtime

conflicts:
  - python-framework
  - alternate-web-framework
```

### Django

```
provides:
  - web-framework
  - python-runtime

conflicts:
  - php-framework
  - alternate-web-framework
```

### CLI Worker

```
provides:
  - worker-runtime

requires:
  - runtime-environment

conflicts:
  - framework-managed-worker
```

### Monorepo

```
provides:
  - workspace-orchestration
```

---

## Capability Registry

Introduce a canonical capability registry file.

Example location:

```
tools/governance/template_capability_registry.json
```

Example structure:

```
{
  "capabilities": [
    "web-framework",
    "python-runtime",
    "php-runtime",
    "worker-runtime",
    "workspace-orchestration",
    "runtime-environment"
  ]
}
```

This registry defines the valid capability vocabulary used by template manifests.

---

## Capability Resolution Engine

Extend the composition engine so that compatibility checks can be evaluated through capability rules.

Resolution must verify:

- required capabilities are satisfied
- conflicting capabilities are not present
- composition roles do not collide

If a violation occurs, the scaffold must reject the composition.

---

## Compatibility Preservation

The capability system must **not change existing behavior**.

Current certified combinations must remain valid:

```
laravel + monorepo
service + monorepo
cli-worker + monorepo
cli-worker + python-package
```

Current rejected combinations must remain rejected:

```
laravel + cli-worker
django + laravel
```

Capability resolution must produce the same results as the current composition matrix.

---

## Governance Test Coverage

Extend governance tests to validate capability compatibility behavior.

Example test coverage:

```
tests/governance/test_template_capability_composition.py
```

Tests must confirm:

- capability resolution preserves the existing matrix
- conflicts correctly block incompatible overlays
- required capabilities are enforced

---

## Documentation Updates

Update template documentation to describe the capability model.

File:

```
docs/codex/templates/README.md
```

Document:

- capability declarations
- capability registry
- capability conflict rules
- capability resolution behavior

---

## Verification Procedure

Run the following commands.

List template manifests:

```
python tools/governance/template_scaffold.py list-manifests --output json
```

Verify composition matrix:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

Run governance tests:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected result:

```
All tests pass
Capability registry loaded
Composition compatibility preserved
```

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
establish-universal-template-composition-capability-registry/
```

Artifacts:

```
01-problem-statement.md
02-capability-model.md
03-capability-registry.md
04-capability-resolution-engine.md
05-governance-test-coverage.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
UNIVERSAL_TEMPLATE_COMPOSITION_CAPABILITY_REGISTRY_ESTABLISHED
```

Meaning:

- template composition is now capability-driven
- the system can scale beyond pairwise compatibility rules
- the current certified matrix remains preserved
- future overlays can be admitted safely using capability declarations

---

## Governance Impact

After this pipeline:

- template composition becomes capability-based
- future overlays can be added without expanding the pairwise matrix
- composition conflicts are governed through capability rules
- the template ecosystem becomes scalable and universal

This pipeline upgrades the template composition system into a **universal composition architecture**.

---

## Next Recommended Pipeline

```
051 — Migrate Existing Template Manifests to Capability-Based Composition Metadata
```

This pipeline will update all existing template manifests so they declare capability metadata compatible with the new capability registry.