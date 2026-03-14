---
pipeline_id: 117
registry_id: governance.codex.normalize-verification-lane-architecture-doctrine-discoverability-path
title: Normalize Verification Lane Architecture Doctrine Discoverability Path
layer: 6
classification: normalization
status: proposed
governance_domain: codex-session-governance
---

# 117 — Normalize Verification Lane Architecture Doctrine Discoverability Path

## 1. Problem Statement

Pipeline **116 — Verify Codex Session Lifecycle Observation Discipline** produced the verdict:

CODEX_SESSION_LIFECYCLE_OBSERVATION_DISCIPLINE_VERIFIED_WITH_RESTRICTIONS

The restriction identified a **discoverability path mismatch** inside the verification lane text.

The lane referenced the architecture doctrine as:

docs/architecture/architecture-doctrine.md

However, the repository’s canonical doctrine surface is:

architecture-doctrine.md

This discrepancy exists **only in the verification lane description**, not in the governance doctrine itself.

To maintain strict governance precision, verification lanes must reference **canonical document paths exactly as they exist in the repository**.

---

## 2. Scope of Normalization

This pipeline performs a **documentation normalization only**.

It does NOT modify:

- governance doctrine semantics
- lifecycle observation canon
- session registry
- session ledger
- session state machine
- runtime boundary definitions

The change is restricted to **verification lane text accuracy**.

---

## 3. Target Canonical Path

The correct architecture doctrine path is:

architecture-doctrine.md

All verification surfaces must reference this canonical path.

---

## 4. Surfaces to Normalize

### Primary Surface

docs/pipelines/governance/116--verify-codex-session-lifecycle-observation-discipline.md

Required correction:

Replace

docs/architecture/architecture-doctrine.md

with

architecture-doctrine.md

---

### Verification Artifact Bundle (116)

If the incorrect path appears in any bundle artifacts, normalize those references as well:

verify-codex-session-lifecycle-observation-discipline/

Potential files:

- 02-surface-inventory.md
- 05-discoverability-verification.md
- 06-verification.md

Only path references are adjusted.

---

## 5. Invariants

The following governance invariants must remain unchanged:

- session state machine authority
- session_id authority
- session registry authority
- session ledger authority
- runtime-neutral lifecycle observation discipline

No semantic interpretation of lifecycle observation changes.

---

## 6. Verification Method

Manual inspection must confirm:

1. The incorrect path no longer appears in pipeline 116 or its artifact bundle.
2. The canonical path `architecture-doctrine.md` is used consistently.
3. No other governance surfaces were modified.

---

## 7. Verification Result

Expected outcome:

The verification lane becomes path-accurate and the previously recorded restriction is resolved.

No further governance drift should be introduced.

---

## 8. Final Verdict

Expected verdict:

VERIFICATION_LANE_ARCHITECTURE_DOCTRINE_DISCOVERABILITY_PATH_NORMALIZED

---

## 9. Governance Impact

This pipeline:

- resolves the restriction introduced during pipeline 116 verification
- restores strict discoverability accuracy for governance surfaces
- preserves Layer 6 session governance integrity

This pipeline performs **documentation-level normalization only**.

No runtime behavior is introduced.