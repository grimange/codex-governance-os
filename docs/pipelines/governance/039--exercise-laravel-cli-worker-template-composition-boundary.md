---
pipeline_id: 039
registry_id: governance.templates.exercise-laravel-cli-worker-template-composition-boundary
title: Exercise Laravel + CLI-worker Template Composition Boundary
stage: analysis
classification: governance
status: proposed
created_by: codex
depends_on:
  - 023
  - 027
  - 038
outputs:
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/01-problem-statement.md
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/02-current-boundary-observation.md
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/03-contract-surface-inventory.md
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/04-incompatibility-analysis.md
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/05-supportability-decision.md
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/06-verification-plan.md
  - docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/07-final-verdict.md
---

# 039 — Exercise Laravel + CLI-worker Template Composition Boundary

## Objective

Formally analyze the **Laravel + CLI-worker overlay composition boundary** to determine whether the combination:

```
laravel + cli-worker
```

should:

1. become a **supported template composition**, or  
2. remain an **explicitly unsupported composition boundary**.

This pipeline does **not implement support**.  
It only performs **contract analysis and compatibility evaluation**.

The result will guide the next pipeline:

- **040 — Implement Laravel + CLI-worker Composition Support**, or
- **040 — Codify Laravel + CLI-worker as Explicit Unsupported Boundary**

---

# Scope

This pipeline evaluates:

- template scaffold compatibility
- manifest declarations
- runtime contract surfaces
- directory layout conflicts
- entrypoint conflicts
- runtime model mismatches

It must **not modify templates** or scaffold behavior.

This is an **analysis-only governance lane**.

---

# Inputs

Evidence sources include:

```
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
```

Test evidence from pipeline 038 must also be referenced:

```
test_template_composition_post_service_monorepo_protections.py
```

---

# Expected Observations

The current system rejects:

```
laravel + cli-worker
```

The analysis must determine **why**.

Potential causes include:

- runtime entrypoint conflict
- application root ownership conflict
- command surface collision
- dependency stack mismatch
- directory structure incompatibility
- scaffold manifest incompatibility

---

# Analysis Steps

## 1. Observe Current Rejection

Run:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker \
  --output json
```

Record:

- rejection reason
- surface conflict
- manifest incompatibility

---

## 2. Inventory Contract Surfaces

Identify:

### Laravel runtime surfaces

Examples:

```
artisan
routes/
app/
bootstrap/
config/
```

### CLI-worker surfaces

Examples:

```
worker entrypoint
worker runtime
job loop
worker command surface
```

Determine where the two overlays overlap or conflict.

---

## 3. Template Manifest Comparison

Review:

```
tools/templates/manifests/*.json
```

Identify:

- missing compatibility declaration
- incompatible runtime model
- conflicting ownership of application root

---

## 4. Runtime Model Compatibility

Assess whether the CLI worker can run as:

```
php artisan worker
```

or similar bounded integration.

If yes, document the minimal scaffold changes required.

If no, explain the structural incompatibility.

---

## 5. Supportability Decision

Determine one of the following:

### Outcome A — Supportable

If conflicts are bounded and resolvable:

```
LARAVEL_CLI_WORKER_COMPOSITION_SUPPORTABLE
```

Document required changes:

- manifest update
- scaffold template
- runtime entrypoint integration
- contract boundaries

This will enable:

```
040 — Implement Laravel + CLI-worker Composition Support
```

---

### Outcome B — Explicit Unsupported Boundary

If the composition breaks scaffold invariants:

```
LARAVEL_CLI_WORKER_COMPOSITION_EXPLICITLY_UNSUPPORTED
```

Document why the boundary exists.

Then recommend:

```
040 — Codify Explicit Unsupported Composition Boundary
```

---

# Output Artifacts

The pipeline must generate the following artifact bundle:

```
docs/pipelines/governance/exercise-laravel-cli-worker-template-composition-boundary/
```

Files:

1. **01-problem-statement.md**

   Why the composition boundary must be analyzed.

2. **02-current-boundary-observation.md**

   Evidence of current rejection behavior.

3. **03-contract-surface-inventory.md**

   Inventory of Laravel and CLI worker runtime surfaces.

4. **04-incompatibility-analysis.md**

   Structural explanation of incompatibility.

5. **05-supportability-decision.md**

   Decision: supportable or unsupported.

6. **06-verification-plan.md**

   How a future implementation would be verified.

7. **07-final-verdict.md**

   Final outcome of the analysis pipeline.

---

# Verification

Verification requires confirming that the pipeline executed **without modifying scaffold behavior**.

Expected verification steps:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Ensure the existing matrix tests remain:

```
OK
```

Confirm the current rejection still occurs:

```
doctor-composition --overlays laravel cli-worker
```

Result should remain rejected during this pipeline.

---

# Final Verdict Format

The final verdict must be one of:

```
LARAVEL_CLI_WORKER_COMPOSITION_SUPPORTABLE
```

or

```
LARAVEL_CLI_WORKER_COMPOSITION_EXPLICITLY_UNSUPPORTED
```

---

# Safety Constraints

This pipeline must **not**:

- add new template overlays
- change scaffold manifests
- change scaffold logic
- change supported composition matrix

The lane is **analysis-only**.

---

# Expected Next Pipelines

Depending on the verdict:

### If supportable

```
040 — Implement Laravel + CLI-worker Composition Support
041 — Verify Laravel + CLI-worker Composition and Reclose Drift Protections
```

### If unsupported

```
040 — Codify Laravel + CLI-worker as Explicit Unsupported Boundary
041 — Verify Explicit Composition Boundary Enforcement
```