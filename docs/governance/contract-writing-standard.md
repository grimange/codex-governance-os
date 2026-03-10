# Contract Writing Standard

## Purpose

This doctrine defines the minimum writing standard for canonical subsystem contracts so future contract-authoring, audit, remediation, and verification pipelines can rely on a stable contract shape.

## Applicability

Use this standard when authoring a canonical contract under `docs/contracts/` unless a higher-authority governance surface explicitly authorizes a narrower format.

## Required Contract Sections

Every canonical subsystem contract should include:

1. purpose
2. scope
3. governing authority
4. canonical rules
5. allowed behaviors
6. prohibited behaviors
7. compliance signals
8. ambiguity handling
9. governance implications
10. non-goals

Additional sections may be added when needed, but the minimum section set should remain intact.

## Authority Expression

- The contract must state how it relates to the constitution, doctrine, and any higher-authority repository surfaces.
- The contract must not claim authority broader than its bounded subsystem or governance surface.
- If the contract depends on another doctrine or contract, that dependency should be named explicitly.

## Scope And Non-Goals Rules

- Scope must describe what the contract governs and what it does not govern.
- Non-goals must prevent readers from inferring broader authority than intended.
- Boundaries should be concrete enough that an audit can tell whether a surface is in scope.

## Lifecycle And State Rules

Where the subsystem has lifecycle or state semantics, the contract should define:

- important states or modes
- who may create, mutate, or terminate state
- ordering constraints or allowed transitions
- whether compatibility behavior exists and how it is treated

If lifecycle semantics are not relevant, the contract should say so instead of implying omission by accident.

## Interface And Event Semantics

Where relevant, the contract should define:

- command or request boundaries
- event publication or consumption rules
- externally visible interface expectations
- prohibited hidden side effects

These rules should be specific enough that audit and verification pipelines can derive criteria from them.

## Compatibility And Legacy Treatment

- Compatibility layers and legacy residuals must be called out explicitly when they influence the subsystem.
- The contract should distinguish between tolerated legacy behavior and the preferred canonical model.

## Governance Implications Requirement

The governance implications section should explain how downstream audits, remediations, verifications, or promotions are expected to use the contract.

## Writing Quality Rule

Contracts should be concise, operational, and audit-ready. They should define observable governance rules, not aspirational architecture prose.
