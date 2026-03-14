---
title: "106 — Establish Codex Session Admission And Activation Rules"
pipeline_id: "106"
registry_id: "governance.codex.establish-codex-session-admission-and-activation-rules"
status: "proposed"
stage: "analysis"
authors:
  - "OpenAI ChatGPT"
created_at: "2026-03-14"
last_updated: "2026-03-14"
layer: "Layer 6 — Governed Session Orchestration"
predecessors:
  - "102 — Establish Codex Session State Machine Canon"
  - "104 — Establish Codex Session Handoff Contract And Resume Evidence Model"
  - "105 — Verify Codex Session Handoff Contract And Resume Evidence Model"
supersedes: []
related_documents:
  - "architecture-doctrine.md"
  - ".codex/AGENTS.md"
  - "README.md"
  - "docs/pipelines/registry/pipeline-registry.md"
  - "docs/governance/codex-session-state-machine-canon.md"
  - "docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md"
  - "docs/governance/codex-session-registry.md"
  - "docs/governance/codex-session-ledger.md"
  - "docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md"
artifact_bundle: "docs/pipelines/governance/establish-codex-session-admission-and-activation-rules/"
governing_principles:
  - "Governed execution"
  - "Evidence-scoped claims"
  - "Restriction preservation"
  - "Authority precedence"
  - "Fail-closed admission"
  - "Bounded activation"
---
# 106 — Establish Codex Session Admission And Activation Rules

## 1. Purpose

Establish the canonical Layer 6 rules that govern when a Codex session may be admitted into execution, when it may activate governed work, and when it must fail closed instead of proceeding.

This pipeline extends the Layer 6 sequence already established by prior pipelines:

- Pipeline 102 defined the session state machine canon.
- Pipeline 103 verified state transition conformance.
- Pipeline 104 defined the handoff contract and resume evidence model.
- Pipeline 105 verified that handoff and resume doctrine across repository surfaces, with explicit restrictions.

What remains insufficiently governed is the admission boundary between **session existence** and **session execution**.

A repository may know that a session exists, and may know how a prior session handed off work, while still lacking a canonical answer to these questions:

- When is a session allowed to start governed work?
- When is a resumed session allowed to continue?
- What minimum evidence must exist before a session becomes active?
- What happens when required evidence or restrictions are missing?

This pipeline establishes those rules.

---

## 2. Problem Statement

Without an explicit session admission and activation canon, Layer 6 remains structurally incomplete.

A session may be described, handed off, or resumed in principle, yet the repository still lacks a fail-closed rule for deciding whether actual governed execution is allowed to begin.

This creates several risks:

- a session starts active work without a valid governed subject
- a successor session claims resumed continuity without satisfying resume admissibility
- restrictions are known but not formally imported before work begins
- the first active step is taken before authoritative evidence is identified
- unsupported boundaries are only discovered after the session is already active
- entry surfaces imply execution legitimacy when the admission boundary was never checked

In short, the repository can become able to describe continuity without being able to govern activation.

---

## 3. Scope

### In scope

- defining canonical session admission
- defining canonical session activation
- defining the difference between initialized, admitted, and active states
- defining admission requirements for new sessions
- defining admission requirements for resumed sessions
- defining rejection and fail-closed conditions
- defining first-action validation expectations
- defining cross-surface alignment requirements for the admission canon
- defining expected evidence fields for registry and ledger usage where applicable

### Out of scope

- implementing runtime enforcement
- building a persistence service or admission engine
- adding database-backed session coordination
- modifying Layer 0 through Layer 5 authority structure
- redefining the already-established handoff contract except where required for admission linkage
- defining terminal-state closure doctrine in full detail
- introducing autonomous governance decisions beyond documented admission rules

---

## 4. Objectives

This pipeline must produce a canonical model that ensures:

1. **Admission precedes activity.**  
   A session must not be treated as actively governing work merely because it exists.

2. **Resume uses stricter evidence than initiation.**  
   A resumed session must satisfy predecessor linkage and continuity conditions before activation.

3. **The first action is governed.**  
   The transition from admission to active work must respect scope, restrictions, and admissible next action.

4. **Failure is explicit.**  
   When admission conditions are not met, the repository must classify the session as not admitted or rejected rather than silently proceeding.

5. **Cross-surface meaning is consistent.**  
   Doctrine, agent instructions, README, and session continuity documents must use the same operational model.

---

## 5. Canonical Definitions

### 5.1 Session initialization

A **session initialization** is the bounded recognition that a session has been created or invoked for a governed purpose.

Initialization establishes that a session exists. It does **not** by itself authorize governed execution.

A session may be initialized by:

- a new governed request
- an explicitly routed pipeline lane
- an inspection or verification request
- a successor session intending to resume from valid handoff evidence

### 5.2 Session admission

A **session admission** is the governed determination that a session is eligible to begin or continue repository-governed execution.

Admission answers the question:

> “Is this session allowed to perform the next governed action under current doctrine, scope, and evidence?”

Admission is the gateway between session existence and permissible governed action.

### 5.3 Session activation

A **session activation** is the moment a validly admitted session enters active execution on the governed subject.

Activation requires more than initialization and more than descriptive continuity. It requires that admission conditions have been met and that a first active step is admissible.

### 5.4 Admission gate

The **admission gate** is the canonical rule set that determines whether a session may transition from initialized or resumed-pending status into admitted and then active execution.

### 5.5 First-action validation

**First-action validation** is the requirement that the first active step taken by the session is consistent with:

- governed subject
- scope boundary
- preserved restrictions
- current stage
- next valid action
- authoritative evidence set

### 5.6 Admission failure

**Admission failure** occurs when required evidence, scope clarity, continuity linkage, or restriction fidelity is insufficient to support governed activation.

Admission failure must fail closed.

---

## 6. Canonical State Semantics Clarification

This pipeline does not replace the session state machine canon. It clarifies how admission and activation operate within it.

### 6.1 SESSION_INITIALIZED

This state means:

- the session exists
- the session has a tentative governed purpose
- admission has not yet been established

This state does **not** mean:

- the session is authorized to execute governed work
- the first action is already valid
- resume continuity has been accepted

### 6.2 SESSION_ADMITTED

This state means:

- the session has passed the admission gate
- the governed subject is sufficiently bounded
- required restrictions are known and preserved
- the next active action is admissible in principle

This state does **not** require that active execution has already begun.

### 6.3 SESSION_ACTIVE

This state means:

- the session has been admitted
- the session has begun governed execution
- the current active step is within scope and consistent with doctrine

### 6.4 SESSION_REJECTED or non-admitted outcome

Where the repository canon includes a rejection or blocked outcome, it should represent:

- admission failure
- inadmissible resume
- unsupported boundary
- insufficient evidence
- prohibited scope broadening

If the current canon does not yet formalize a named rejection state, the admission doctrine must still require a fail-closed interpretation rather than silent activation.

---

## 7. Admission Model

The repository shall distinguish at least these phases:

1. **Initialized**  
   The session exists.

2. **Admission review**  
   The session’s evidence, scope, restrictions, and continuity context are assessed.

3. **Admitted**  
   The session is permitted to proceed.

4. **Active**  
   The session has begun governed execution.

5. **Rejected / Not admitted / Pending evidence**  
   The session may not proceed yet.

This model ensures that session existence is never confused with legitimate execution.

---

## 8. Admission Rules for New Sessions

A new session may be admitted when all of the following are true:

1. the governed subject is explicitly identified
2. the requested work falls within supported repository boundaries
3. the initial scope is bounded enough to identify a next valid action
4. authoritative doctrine or artifact references are known for the work being undertaken
5. known restrictions and unsupported edges are either absent or explicitly preserved
6. the first active action does not require unverified assumptions to be treated as fact

A new session must not be admitted if:

- the work request is structurally ambiguous beyond safe interpretation
- the requested work exceeds supported boundaries
- the session would need to broaden scope silently just to begin
- no authoritative reference surface exists for the claimed governed task

---

## 9. Admission Rules for Resumed Sessions

A resumed session must satisfy all applicable new-session admission rules plus the following continuity requirements:

1. a valid predecessor handoff packet exists
2. predecessor linkage is explicit
3. the governed subject matches the predecessor scope or is a strict narrowing
4. preserved restrictions are imported without silent mutation
5. unsupported boundaries remain explicit
6. the successor does not upgrade pending or unverified claims into established truth
7. the next valid action remains admissible under current doctrine

A resumed session must not be admitted if:

- predecessor linkage is missing
- the handoff packet is incomplete or non-canonical
- scope has silently expanded
- prior restrictions were dropped or weakened
- continuity is being reconstructed from memory alone
- the claimed next action contradicts the handoff packet or governing doctrine

---

## 10. Activation Rules

A session may transition from admitted to active only when:

1. the first active action is identified
2. that action is within scope
3. that action respects preserved restrictions
4. that action is supported by the authoritative evidence set
5. no fail-closed condition remains unresolved

Activation should be understood as the first governed act performed after admission, not merely the existence of intent to proceed.

Examples of admissible first active actions include:

- reading the canonical doctrine required by the lane
- inspecting the current artifact bundle
- normalizing a required documentation surface under admitted scope
- executing the next valid verification step defined by the handoff packet or lane doctrine

Examples of inadmissible activation include:

- introducing a new workstream outside admitted scope
- asserting registry truth without checking the canonical registry surface
- modifying restrictions during activation
- beginning execution while continuity evidence is still incomplete

---

## 11. First-Action Validation Contract

Before active execution, the session should be able to answer all of the following:

- What is the governed subject?
- What is the current stage?
- What is the exact next valid action?
- What authoritative materials define current truth?
- What restrictions must remain preserved?
- What unsupported boundaries remain out of scope?

If those questions cannot be answered from the evidence set, admission is incomplete and activation must not occur.

---

## 12. Fail-Closed Conditions

The session must fail closed and remain non-active if any of the following are true:

- no governed subject is identifiable
- authoritative doctrine is unavailable
- scope is too ambiguous to define a next valid action
- a resume claim lacks predecessor evidence
- preserved restrictions are missing
- the requested action requires silent scope broadening
- unsupported boundaries are being crossed
- the session would need to treat provisional information as authoritative fact

Fail-closed outcomes may be recorded as:

- not admitted
- pending evidence
- rejected
- blocked by unsupported boundary

The exact label may vary by repository surface, but the semantics must not.

---

## 13. Authority And Precedence Rules

Admission and activation are subordinate to the repository’s existing governance hierarchy.

### 13.1 Layer precedence

Admission doctrine in Layer 6 must not override:

- Layer 0 safety invariants
- Layer 1 architecture doctrine
- Layer 2 scaffold and template boundaries
- Layer 3 codex execution rules
- Layer 4 role and collaboration governance
- Layer 5 orchestration discipline already established

### 13.2 Canon precedence

Where ambiguity exists, precedence is:

1. safety and doctrine canon
2. explicit state machine canon
3. handoff and resume canon
4. admission and activation canon
5. derivative support documents and summaries

---

## 14. Repository Surface Requirements

The following surfaces must align to this canon after implementation.

### 14.1 architecture-doctrine.md

Must explain that session execution is governed not merely by existence or handoff, but by explicit admission and activation conditions.

### 14.2 .codex/AGENTS.md

Must instruct agents that:

- initialized is not the same as active
- resume requires admission, not just predecessor awareness
- the first active action must be admissible
- failure to satisfy admission conditions must fail closed

### 14.3 README.md

Must expose, at a high level, that Layer 6 includes admission and activation governance without implying runtime enforcement that does not exist.

### 14.4 Session registry and ledger surfaces

Where session registry or ledger documents exist, they should be able to record:

- initialization
- admission status
- activation status
- predecessor linkage when applicable
- rejection or pending-evidence reason
- first admitted action

---

## 15. Expected Deliverables

This pipeline should produce, at minimum:

1. **A canonical doctrine file**  
   Suggested target: `docs/governance/codex-session-admission-and-activation-rules.md`

2. **Cross-surface references** in:
   - `architecture-doctrine.md`
   - `.codex/AGENTS.md`
   - `README.md`

3. **Continuity-surface alignment updates** where relevant in:
   - `docs/governance/codex-session-registry.md`
   - `docs/governance/codex-session-ledger.md`
   - `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`

4. **Registry entry** for pipeline 106 in:
   - `docs/pipelines/registry/pipeline-registry.md`

5. **Artifact bundle** under:
   - `docs/pipelines/governance/establish-codex-session-admission-and-activation-rules/`

---

## 16. Recommended Artifact Bundle Structure

The artifact bundle should contain:

1. `01-problem-statement.md`
2. `02-session-admission-model.md`
3. `03-session-activation-state-rules.md`
4. `04-resume-admission-criteria.md`
5. `05-fail-closed-behavior.md`
6. `06-cross-surface-integration-plan.md`
7. `07-verification-plan.md`
8. `08-final-verdict.md`

---

## 17. Implementation Guidance

### 17.1 Keep the doctrine additive

Do not rewrite the state machine or handoff canon. This pipeline should govern the boundary between continuity and execution.

### 17.2 Preserve fail-closed rigor

Ambiguity at admission time must block activation rather than being papered over by best-effort interpretation.

### 17.3 Separate admission from action

Do not let a session become “active” merely because it can describe the work. Admission must exist first.

### 17.4 Keep operational claims honest

If runtime admission is not automatically enforced by the repository, say so explicitly.

### 17.5 Preserve restriction fidelity

Restrictions must be imported exactly, not restated in weaker language during admission.

---

## 18. Verification Criteria

A future verification pipeline should confirm:

1. a canonical admission and activation doctrine file exists
2. the doctrine distinguishes initialized, admitted, and active states
3. the doctrine defines new-session and resumed-session admission rules
4. the doctrine defines fail-closed conditions
5. the doctrine defines first-action validation expectations
6. cross-surface references exist in doctrine, README, and `.codex/AGENTS.md`
7. session registry and ledger surfaces can represent admission outcomes where applicable
8. repository surfaces do not overclaim runtime enforcement
9. pipeline 106 is registered with the correct artifact bundle path

---

## 19. Final Verdict Template

Recommended verdict constant:

`CODEX_SESSION_ADMISSION_AND_ACTIVATION_RULES_ESTABLISHED`

If implementation is complete but constrained by repository-surface limitations, an acceptable restricted verdict pattern is:

`CODEX_SESSION_ADMISSION_AND_ACTIVATION_RULES_ESTABLISHED_WITH_RESTRICTIONS`

---

## 20. Recommended Follow-Up Pipelines

### Immediate next

- **107 — Verify Codex Session Admission And Activation Rules**

### Strong next sequence

- **108 — Establish Codex Session Closure And Terminal-State Evidence Canon**
- **109 — Verify Codex Session Closure And Terminal-State Evidence Canon**

### Optional strengthening after closure

- **110 — Establish Codex Session Exception And Recovery Handling Canon**
- **111 — Verify Codex Session Exception And Recovery Handling Canon**

This preserves a clean Layer 6 lifecycle sequence:

- state machine
- transitions
- handoff
- resume evidence
- admission
- activation
- closure
- exception handling

---

## 21. Operator Notes

Pipeline 106 is the point where Layer 6 stops being only about continuity description and becomes a more complete execution-governance system.

A repository that can describe sessions, handoffs, and resume packets but cannot determine when execution is actually allowed remains structurally incomplete. This pipeline closes that gap and prepares the repository for terminal-state governance and, later, more credible autonomous governance loops.
