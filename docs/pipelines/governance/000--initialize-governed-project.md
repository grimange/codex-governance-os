# Codex Pipeline — Initialize Governed Project

**Filename**
`docs/pipelines/governance/000--initialize-governed-project.md`

---

## Purpose

Convert a standard repository into a **Codex-governed repository** by installing the minimum governance framework required for autonomous pipeline operation.

This pipeline establishes:

- repository governance constitution
- canonical documentation structure
- pipeline catalog structure
- pipeline registry surface
- governance authority doctrine

After execution, the repository becomes **governance-capable**.

---

## Universal Skill References

- `governed-project-bootstrap`
  Use for baseline governance-surface installation, bootstrap planning, and initialization execution.
- `repository-discovery`
  Use for repository discovery and current-state inventory before installation.
- `pipeline-registry-reconciliation`
  Use when registering active pipelines and checking registry identity.

# Phase 00 — Pipeline Summary

Output artifact:

`docs/pipelines/governance/initialize-governed-project/00-pipeline-summary.md`

Contents:

- pipeline purpose
- repository governance initialization scope
- initial repository governance status
- target governance baseline

---

# Phase 01 — Scope Definition

Output artifact:

`01-governance-scope.md`

Defines:

### Target governance capabilities

The repository must support:

- Codex agents
- Pipeline governance
- Architecture contracts
- Artifact verification
- Deterministic pipeline sequencing

### Out-of-scope

This pipeline does **not**:

- infer domain architecture
- generate business contracts
- perform code audits
- modernize implementations

Those are handled by later pipelines.

---

# Phase 02 — Repository Discovery

Output artifact:

`02-repository-discovery.md`

Use the `repository-discovery` skill to inventory existing repository structure.

Example discovery matrix:

| Surface | Exists | Notes |
|------|------|------|
| docs folder | yes/no | |
| governance docs | yes/no | |
| pipeline catalog | yes/no | |
| contracts | yes/no | |
| architecture doctrine | yes/no | |

The pipeline records:

- missing governance surfaces
- conflicts with expected structure

---

# Phase 03 — Governance Structure Design

Output artifact:

`03-governance-structure.md`

Define the canonical structure to install.

Target repository layout:

`project/
├── AGENTS.md
├── .codex/
│ └── AGENTS.md
├── docs/
│ ├── governance/
│ │ └── architecture-doctrine.md
│ ├── contracts/
│ ├── pipelines/
│ │ ├── governance/
│ │ ├── remediation/
│ │ ├── verification/
│ │ ├── promotion/
│ │ └── registry/
│ │ └── pipeline-registry.md
│ └── modernization/`


---

# Phase 04 — Initialization Plan

Output artifact:

`04-initialization-plan.md`

Define files to create.

### Governance constitution

`AGENTS.md`

### Codex local config

`.codex/AGENTS.md`

### Governance doctrine

`docs/governance/architecture-doctrine.md`

### Pipeline system

`docs/pipelines/`

### Pipeline registry

`docs/pipelines/registry/pipeline-registry.md`

---

# Phase 05 — Governance Initialization

Output artifact:

`05-initialization-execution.md`

Use the `governed-project-bootstrap` skill to install the repository constitution, local Codex operating surface, architecture doctrine, pipeline roots, and pipeline registry while preserving the canonical governed-project baseline.

---

# Phase 06 — Pipeline Registry Integration

Output artifact:

`06-registry-integration.md`

Use the `pipeline-registry-reconciliation` skill to register the initialization pipeline itself and verify that registry identity matches the pipeline filename and path.

---

# Phase 07 — Verification

Output artifact:

`07-initialization-verification.md`

Verification checklist:

| Control | Result |
|------|------|
| AGENTS.md exists | |
| governance docs exist | |
| pipeline catalog exists | |
| registry exists | |
| folder taxonomy correct | |

Verification outcome must confirm:

`repository is governance-capable`

---

# Phase 08 — Promotion Decision

Output artifact:

`08-promotion-decision.md`

Possible outcomes:

- PROMOTE
- REQUIRES_REPAIR
- BLOCKED

Criteria:

PROMOTE when:

- governance surfaces exist
- registry initialized
- documentation structure installed

---

# Phase 09 — Final Verdict

Output artifact:

`09-final-verdict.md`

Possible verdicts:

- GOVERNED_REPOSITORY_INITIALIZED
- INITIALIZATION_INCOMPLETE
- INITIALIZATION_BLOCKED

Example verdict:

`GOVERNED_REPOSITORY_INITIALIZED`

---

# Expected Result After Pipeline

Repository becomes:

- governance-ready
- pipeline-ready
- codex-operable

Meaning Codex agents can now safely run:

- audit pipelines
- remediation pipelines
- verification pipelines
- promotion pipelines

---

# Recommended Next Pipeline

After initialization, run:

`Codex Pipeline — Discover Existing Architecture and Establish Doctrine`

or

`Codex Pipeline — Audit Repository Governance Readiness`
