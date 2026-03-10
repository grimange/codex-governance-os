# Governance Terminology

## Purpose

This doctrine defines the controlled operational meaning of recurring governance terms used by this repository and by repositories that inherit this template.

These definitions exist to reduce ambiguity across doctrine, contracts, pipelines, audits, remediations, verifications, and promotion decisions.

## Usage Rule

- When a governance term defined here is used in a canonical governance surface, the meaning in this document governs unless a higher-authority source defines a narrower repository-specific meaning explicitly.
- Pipelines and contracts should reference this terminology doctrine rather than redefining common terms inline unless local narrowing is required for correctness.

## Canonical Terms

### Contract

A canonical rules document for a bounded subsystem or governance surface that defines responsibilities, authority, allowed behaviors, prohibited behaviors, and compliance signals.

### Authority

The right of a surface to govern interpretation or decision-making relative to other surfaces.

### Architecture Doctrine

The canonical document that explains the repository's architecture model, authority layers, source-of-truth rules, and interpretation boundaries.

### Pipeline

A documented governance workflow that defines ordered phases, required outputs, and a deterministic completion standard.

### Registry

A canonical catalog that records which pipelines are active governance surfaces and how they are identified.

### Drift

A meaningful deviation between current repository state and a higher-authority governance surface such as the constitution, a doctrine, a contract, or an active pipeline definition.

### Remediation

Governed work that changes repository state to reduce or eliminate identified drift.

### Verification

Governed work that confirms whether a previously stated rule, remediation, or compliance claim is now supported by inspectable evidence.

### Promotion

An explicit governance decision that a result is acceptable for downstream reliance.

### Canonical

Authoritative for decision-making within the applicable authority order.

### Compatibility Layer

A surface retained to preserve continuity with earlier behavior while not being the preferred long-term canonical model.

### Legacy Residual

A remaining artifact, behavior, or term from an earlier model that still exists after governance has identified a stronger canonical replacement.

### Subsystem

A bounded portion of repository behavior or governance responsibility that can be reasoned about, governed, and audited as a distinct unit.

### Evidence

Inspectable repository state or recorded execution output used to support a governance conclusion.

### Final Verdict

The explicit end-state statement of a pipeline run that summarizes the governance outcome and whether downstream work may rely on it.

## Interpretation Notes

- Evidence informs decisions but does not outrank higher-authority surfaces unless those surfaces explicitly delegate.
- A compatibility layer may remain operationally necessary without becoming the canonical model.
- A final verdict is stronger than an informal summary, but it still cannot override a higher-authority doctrine, contract, or constitution.
