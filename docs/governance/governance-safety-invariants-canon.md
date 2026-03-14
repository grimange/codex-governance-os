# Governance Safety Invariants Canon

## Purpose

This doctrine defines the non-negotiable safety invariants of the Governance
OS.

It exists so governance work remains fail-closed, auditable, and authority-bound
even when repository state grows, pipelines multiply, or AI-assisted operation
accelerates execution.

## Scope

This canon governs the safety boundaries that apply across:

- governance doctrine under `docs/governance/`
- governance contracts under `docs/contracts/`
- pipeline definitions and their artifact bundles
- registry, matrix, and ledger-backed governance truth surfaces
- canonical governance tooling and verification routines
- agent-facing operating instructions that affect repository governance

This canon does not define normalization mechanics in full detail. It defines
the safety invariants that normalization and later Layer 3 rules must preserve.

## Safety Invariant Families

### Governed Execution Invariants

Structural governance mutation must occur only through admitted governance
execution or another explicitly authorized governed path.

### Evidence-Scoped Claim Invariants

Governance claims must not exceed the scope that repository evidence actually
proves.

### Canonical Surface Protection Invariants

Canonical governance truth surfaces must not be mutated casually, silently, or
outside their governing path.

### Restriction Preservation Invariants

Restrictions, partial states, unsupported boundaries, and blocked outcomes must
remain explicit.

### Authority Precedence Invariants

Canonical repository truth outranks narrative interpretation, convenience
reasoning, and unsupported AI inference.

### Semantic Safety Invariants

Editing, cleanup, or normalization must not silently change governance meaning.

### Repository Portability Link Invariants

Canonical governance and repository-entry surfaces must remain portable across
clone locations, users, and operating systems.

## Governed Execution Invariants

### Governed Execution Required

Structural changes affecting canonical governance truth must be made through a
documented governance lane or another explicitly authorized governed path.

The repository must not rely on ad hoc direct mutation for changes that alter:

- active pipeline meaning
- registry truth
- canonical doctrine
- canonical contracts
- certified matrix or ledger truth
- other repository-wide governance interpretation surfaces

### No Governance Bypass Through Convenience

Speed, convenience, local clarity, or operator confidence do not justify
bypassing governed execution when the change affects governance truth.

If a change materially alters repository governance meaning, the governed path
remains required.

### No Self-Authorizing Governance Mutation

A change must not grant itself broader authority merely by editing a lower-order
surface.

Governance mutation remains bounded by the existing authority order until the
change is explicitly installed in version control through the proper governing
path.

## Canonical Surface Protection Invariants

### Canonical Surfaces Must Remain Protected

Canonical governance surfaces must not be treated as casual documentation.

Protected surfaces include, by category:

- constitutional and doctrinal authority
- canonical contracts
- active pipeline definitions
- pipeline registry truth
- certified matrix, registry, and ledger truth for governed subsystems
- doctrine that controls interpretation of repository evidence or safety

### No Silent Mutation Of Canonical Truth

Canonical truth must not be changed through summary-only edits, side-channel
notes, or indirect narrative restatement.

If canonical meaning changes, the canonical surface itself must be updated
through governed execution.

### No Split-Authority Drift

If multiple surfaces appear to define the same governance truth, they must not
be left in contradictory active states.

Conflicts must be reconciled explicitly in version control rather than tolerated
as an informal convenience layer.

## Evidence-Scoped Claim Invariants

### Claims Must Not Exceed Evidence Scope

No governance claim may be broader than the evidence that supports it.

Examples of forbidden broadening include:

- turning a bounded verification into repository-wide conformance
- turning one certified composition into blanket stack support
- turning a documented possibility into an established surface

### Verdicts And Summaries Must Not Outrun Evidence

A verdict, summary, or closing statement must not be treated as stronger than
the evidence it summarizes.

Recorded success language cannot compensate for absent or insufficient proof.

### Local Proof Does Not Imply Global Safety

Proof of one boundary, subsystem, or lane does not imply that adjacent or
broader surfaces are also safe unless those broader surfaces have been
explicitly verified.

## Restriction Preservation Invariants

### Restrictions Must Remain Explicit

If the repository proves only a bounded outcome, that restriction must remain
visible in the canonical record.

This applies to:

- partial establishment
- verified with restrictions
- blocked outcomes
- unsupported boundaries
- scoped or pair-only admissions

### Unsupported Must Remain Unsupported

Unsupported is its own governance state.

Unsupported boundaries must not be silently recast as:

- success
- failure
- omission
- deferred convenience interpretation

### Fail-Closed Boundaries Must Stay Visible

When the repository explicitly rejects a boundary, that rejection must remain
visible in contracts, verification, or other canonical truth surfaces where the
domain requires it.

## Authority Precedence Invariants

### Canonical Repository Truth Outranks Narrative

Where conflict exists, canonical repository truth outranks narrative,
interpretive, or convenience-oriented explanation.

This includes:

- governing doctrine over descriptive notes
- canonical contracts over local commentary
- registry or matrix truth over informal summary
- recorded verification evidence over unsupported inference

### AI Assistance Must Remain Authority-Bound

AI-assisted operation must not override repository truth, expand verified scope,
or erase explicit restrictions through confidence or summarization alone.

AI may assist execution, but it must remain bounded by the same authority order
and fail-closed safety rules as any other operator.

## Semantic Safety Invariants

### No Silent Semantic Mutation

Editing, cleanup, normalization, or refactoring must not silently change
governance meaning.

If meaning changes, that change must be explicit, governed, and inspectable.

### No Hidden Unsupported Boundary

The repository must not hide unsupported, blocked, or partial states behind
neutral wording that suggests broader readiness than the evidence permits.

### Normalization Must Preserve Governance Meaning

Normalization may improve consistency or routing only when it does not silently
change authority, support status, restriction state, or recorded governance
meaning.

If normalization would alter meaning, it must block or be handled through an
explicit higher-authority lane.

## Repository Portability Link Invariants

### Machine-Local Filesystem References Are Forbidden In Canonical Links

Canonical governance surfaces must not use machine-local absolute filesystem
references as live repository links, canonical references, navigation paths, or
doctrinal pointers.

Forbidden machine-local patterns include, but are not limited to:

- `/home/...`
- `/Users/...`
- `C:\...`
- `file://...`
- `~/...`

Portable repository references must instead use:

- document-relative links
- repository-relative paths
- intentional external URLs

### Historical Evidence Must Remain Visible

Historical artifacts may preserve older portability defects as evidence when a
later remediation or verification lane needs that record.

Those historical mentions must not be used as live canonical navigation or
treated as approval for future machine-local references in canonical surfaces.

### Examples And Pattern Definitions Are Not Live References

Literal pattern examples inside doctrine, contracts, or pipeline definitions
may mention forbidden path forms when they are being described as disallowed
inputs or remediation targets rather than used as live links or canonical
navigation.

### Deterministic Preflight Enforcement Is Allowed

Governed execution may enforce this invariant through a deterministic
repository preflight or admission scan that fails closed on new portability
violations while classifying rule examples, scan definitions, and preserved
historical evidence explicitly.

## Compliance Signals

This canon is being followed when:

- structural governance mutation is routed through documented lanes
- canonical surfaces are updated directly when meaning changes
- verification and verdict language remain evidence-scoped
- restrictions remain visible after establishment and verification work
- unsupported boundaries do not silently broaden
- narrative or AI summaries do not outrank repository truth
- cleanup or normalization does not silently rewrite governance meaning
- canonical links and repository references remain portable rather than
  machine-local

## Non-Goals

This canon does not:

- define the full normalization mechanics model
- replace subsystem-specific fail-closed contracts
- introduce Git or PR governance controls
- prescribe Codex collaboration behavior in full detail
- certify every current lane as compliant without later verification
