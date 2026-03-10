# Codex Pipeline — Audit Repository Governance Readiness

**Filename**
docs/pipelines/governance/002--audit-repository-governance-readiness.md

**Pipeline ID:** 002  
**Category:** governance  
**Stage:** audit

---

# Purpose

Audit the repository to determine whether governance infrastructure, architecture doctrine, documentation surfaces, and pipeline controls are sufficiently established for reliable autonomous governance operations.

This pipeline evaluates whether the repository is **governance-operational**.

It does not modify code or documents.  
It produces a **governance readiness verdict** and identifies missing governance controls.

---

# Why This Pipeline Exists

A repository may have:

- governance scaffolding installed
- an architecture doctrine written
- pipelines created

…but still lack the conditions necessary for reliable governance.

Common problems include:

- missing pipeline registry
- undocumented authority boundaries
- ambiguous lifecycle vocabulary
- incomplete governance artifact structure
- pipelines operating without clear sequencing rules

This pipeline identifies those issues before large-scale audits and remediation pipelines begin.

---

## Universal Skill References

- `governance-readiness-audit`
  Use for governance-surface inventory, doctrine consistency review, sequencing checks, and readiness evaluation.
- `pipeline-registry-reconciliation`
  Use when validating registry identity, completeness, and active-pipeline discoverability.

# Phase 00 — Pipeline Summary

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/00-pipeline-summary.md

Document:

- repository under review
- governance initialization status
- architecture doctrine status
- governance audit objective
- expected governance readiness criteria

---

# Phase 01 — Governance Surface Inventory

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/01-governance-surface-inventory.md

Use the `governance-readiness-audit` skill to audit the presence of key governance surfaces.

| Surface | Expected Location |
|------|------|
| repository constitution | AGENTS.md |
| Codex governance surface | .codex/AGENTS.md |
| architecture doctrine | docs/governance/architecture-doctrine.md |
| contract folder | docs/contracts/ |
| pipeline catalog | docs/pipelines/ |
| pipeline registry | docs/pipelines/registry/pipeline-registry.md |
| modernization docs | docs/modernization/ |

Each surface must be classified as:

- present and complete
- present but incomplete
- present but outdated
- missing

---

# Phase 02 — Governance Doctrine Consistency Audit

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/02-governance-doctrine-consistency.md

Evaluate whether governance doctrine surfaces are internally consistent.

Check:

- AGENTS.md authority references
- architecture doctrine authority model
- contract authority expectations
- pipeline governance expectations

Document contradictions and classify severity.

---

# Phase 03 — Pipeline Catalog Integrity Audit

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/03-pipeline-catalog-integrity.md

Use the `governance-readiness-audit` skill, with `pipeline-registry-reconciliation` where registry identity is involved, to confirm:

- pipeline naming conventions
- coherent numbering system
- logical pipeline categories
- correct folder organization
- valid artifact paths

Identify:

- duplicate pipelines
- orphan pipelines
- pipelines missing from registry
- registry entries pointing to missing pipelines

---

# Phase 04 — Pipeline Registry Integrity Audit

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/04-pipeline-registry-integrity.md

Use the `pipeline-registry-reconciliation` skill to confirm:

- registry exists
- registry structure is valid
- entries correspond to real pipelines
- no stale entries
- identifiers match pipeline IDs

Classify registry issues:

- informational
- moderate
- high-risk

---

# Phase 05 — Governance Artifact Compliance Audit

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/05-governance-artifact-compliance.md

Use the `governance-readiness-audit` skill to evaluate whether pipelines follow governance artifact standards.

Expected artifacts include:

00-pipeline-summary.md  
phase artifacts  
final-verdict.md

Determine whether pipelines:

- produce deterministic artifacts
- follow numbering conventions
- store artifacts in proper directories

---

# Phase 06 — Governance Sequencing Audit

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/06-governance-sequencing-audit.md

Use the `governance-readiness-audit` skill to evaluate pipeline lifecycle sequencing against the governance lifecycle doctrine.

Typical lifecycle:

- initialization
- discovery
- audit
- remediation
- verification
- promotion

Identify:

- missing lifecycle stages
- sequencing conflicts
- circular dependencies
- invalid pipeline references

---

# Phase 07 — Governance Risk Assessment

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/07-governance-risk-assessment.md

For each risk record:

- description
- evidence
- affected governance surface
- severity

Severity levels:

LOW  
MODERATE  
HIGH  
BLOCKING

---

# Phase 08 — Governance Readiness Evaluation

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/08-governance-readiness-evaluation.md

Determine repository governance state.

Possible states:

GOVERNANCE_READY  
PARTIALLY_GOVERNED  
GOVERNANCE_FRAGMENTED  
GOVERNANCE_NOT_INITIALIZED

---

# Phase 09 — Promotion Decision

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/09-promotion-decision.md

Possible outcomes:

PROMOTE  
PROMOTE_WITH_REMEDIATION_PLAN  
REQUIRES_REMEDIATION  
BLOCKED

---

# Phase 10 — Final Verdict

Output artifact:

docs/pipelines/governance/audit-repository-governance-readiness/10-final-verdict.md

Allowed verdicts:

REPOSITORY_GOVERNANCE_READY  
REPOSITORY_GOVERNANCE_PARTIALLY_READY  
REPOSITORY_GOVERNANCE_FRAGMENTED  
REPOSITORY_GOVERNANCE_NOT_READY

The verdict must summarize:

- governance strengths
- missing controls
- remediation needs
- recommended next pipeline

---

# Completion Standard

This pipeline is complete only when the repository’s governance readiness state is clearly documented and a next governance action is identified.
