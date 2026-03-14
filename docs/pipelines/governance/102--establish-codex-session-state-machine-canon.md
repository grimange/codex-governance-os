---
author: codex
created_date: 2026-03-14
governance_type: doctrine-establishment
layer: layer-6-codex-session-orchestration
pipeline_id: 102
registry_id: governance.codex.establish-session-state-machine-canon
stage: governance
status: proposed
title: Establish Codex Session State Machine Canon
verification_type: documentation
---

# Pipeline 102 --- Establish Codex Session State Machine Canon

## 1. Problem Statement

Pipelines 098 through 101 established and verified the
documentation-level governance needed for Codex session continuity,
handoff discipline, schema normalization, and registry alignment.

The repository now has:

-   Codex session handoff enforcement
-   end-to-end continuity verification
-   canonical governance surface schema
-   normalized registry path discipline
-   verified active use of canonical lifecycle field names

However, the Layer-6 Codex governance model still lacks a formally
declared **session state machine canon**.

At present, the lifecycle of a governed Codex session is implied across
multiple documents rather than defined in one canonical state model.
This creates risk in four areas:

-   lifecycle transitions are not yet expressed as explicit governed
    states
-   valid and invalid transitions are not yet codified
-   handoff and resumption semantics are described, but not yet modeled
    as authoritative state transitions
-   future verification and recovery lanes lack a canonical transition
    reference

Without a state machine canon, Layer-6 session governance remains
structurally disciplined but semantically incomplete.

This pipeline establishes the canonical Codex session lifecycle state
machine for the repository.

------------------------------------------------------------------------

## 2. Goals

This pipeline establishes:

1.  the canonical set of Codex session lifecycle states
2.  the allowed transition model between those states
3.  invalid transition boundaries
4.  authoritative meanings for handoff, resumption, and closure in
    lifecycle terms
5.  the governance surfaces that must conform to the state machine canon

This pipeline is a **doctrine and documentation establishment lane**.

It does not introduce runtime automation or enforcement code.

------------------------------------------------------------------------

## 3. Canonical State Machine Scope

The Codex Session State Machine Canon applies to the governed lifecycle
of a Codex work session as recorded in Layer-6 governance surfaces.

The canon governs:

-   session creation
-   active execution
-   handoff preparation
-   handoff completion
-   resumed execution
-   closure preparation
-   closure completion

The canon does not redefine lower-layer governance authority, pipeline
admission, or repository execution semantics.

It only defines the lifecycle model for Codex session state.

------------------------------------------------------------------------

## 4. Canonical Codex Session States

The canonical session lifecycle states are:

  -----------------------------------------------------------------------
  State                               Meaning
  ----------------------------------- -----------------------------------
  SESSION_INITIALIZED                 A governed Codex session has been
                                      created and recognized, but active
                                      execution has not yet begun

  SESSION_ACTIVE                      The session is actively executing
                                      governed work

  SESSION_HANDOFF_PENDING             The session is active but preparing
                                      a governed handoff to a subsequent
                                      Codex continuation

  SESSION_HANDOFF_COMPLETED           The required handoff packet and
                                      continuity evidence have been
                                      completed

  SESSION_RESUMED                     A subsequent governed session has
                                      resumed work using the recorded
                                      handoff continuity contract

  SESSION_CLOSURE_PENDING             The session is concluding and
                                      closure evidence is being finalized

  SESSION_CLOSED                      The session has been formally
                                      closed and no further work may
                                      occur within the same session
                                      lifecycle
  -----------------------------------------------------------------------

These state names are canonical and must be used consistently across all
active Layer-6 governance surfaces.

------------------------------------------------------------------------

## 5. Allowed State Transitions

The following transitions are canonical and allowed.

  From                        To
  --------------------------- ---------------------------
  SESSION_INITIALIZED         SESSION_ACTIVE
  SESSION_ACTIVE              SESSION_HANDOFF_PENDING
  SESSION_HANDOFF_PENDING     SESSION_HANDOFF_COMPLETED
  SESSION_HANDOFF_COMPLETED   SESSION_CLOSURE_PENDING
  SESSION_CLOSURE_PENDING     SESSION_CLOSED
  SESSION_HANDOFF_COMPLETED   SESSION_RESUMED
  SESSION_RESUMED             SESSION_ACTIVE
  SESSION_ACTIVE              SESSION_CLOSURE_PENDING

------------------------------------------------------------------------

## 6. Invalid Transition Boundaries

  -----------------------------------------------------------------------
  Invalid Transition                  Reason
  ----------------------------------- -----------------------------------
  SESSION_CLOSED -\> SESSION_ACTIVE   A closed session cannot be reopened

  SESSION_INITIALIZED -\>             A session cannot close without
  SESSION_CLOSED                      entering closure discipline

  SESSION_ACTIVE -\>                  Lifecycle cannot move backward
  SESSION_INITIALIZED                 

  SESSION_HANDOFF_COMPLETED -\>       Continuation must occur through
  SESSION_ACTIVE                      resumed governance semantics
  -----------------------------------------------------------------------

Invalid transitions must be treated as governance findings by future
verification lanes.

------------------------------------------------------------------------

## 7. Handoff and Resumption Semantics

The canon distinguishes between **handoff completion** and
**resumption**.

### Handoff Completion

A session reaches SESSION_HANDOFF_COMPLETED when:

-   the continuity packet is prepared
-   required context transfer is complete
-   downstream continuation is governance‑eligible

### Resumption

A session reaches SESSION_RESUMED when:

-   a successor governed session accepts and uses the handoff evidence
-   the continuity contract is materially in force

------------------------------------------------------------------------

## 8. Governance Surfaces Required To Conform

The following active governance surfaces must conform to this state
machine canon:

-   layer-6-codex-session-orchestration-and-handoff-discipline.md
-   codex-session-registry.md
-   codex-session-ledger.md
-   codex-session-handoff-packet-and-continuity-contract.md
-   future Layer‑6 session verification lanes
-   future Layer‑6 recovery and resumption lanes

------------------------------------------------------------------------

## 9. Restrictions

This pipeline is documentation and doctrine establishment only.

It must not:

-   introduce runtime enforcement code
-   alter pipeline execution logic
-   modify lower-layer governance authority
-   redefine registry discipline already normalized by pipelines 100 and
    101

------------------------------------------------------------------------

## 10. Verification Plan

Verification for this pipeline must confirm that:

1.  the canonical state list is explicitly defined
2.  allowed transitions are explicitly defined
3.  invalid transitions are explicitly defined
4.  handoff and resumption semantics are distinguished
5.  conformance surfaces are explicitly named

Verification method: documentation inspection.

------------------------------------------------------------------------

## 11. Expected Outcome

Upon completion:

-   the repository will have a canonical Codex session lifecycle model
-   future verification lanes will have an authoritative transition
    reference
-   future recovery lanes will be able to detect lifecycle breakage
    against canon

------------------------------------------------------------------------

## 12. Artifact Bundle Requirements

The artifact bundle for this lane should include:

01-problem-statement.md\
02-session-lifecycle-gap-analysis.md\
03-canonical-state-definition.md\
04-transition-model.md\
05-conformance-surface-alignment.md\
06-verification.md\
07-final-verdict.md

------------------------------------------------------------------------

## 13. Final Verdict Format

The artifact bundle must produce:

CODEX_SESSION_STATE_MACHINE_CANON_ESTABLISHED
