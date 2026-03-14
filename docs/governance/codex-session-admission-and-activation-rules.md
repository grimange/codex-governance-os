# Codex Session Admission And Activation Rules

## Purpose

This canon defines when a governed Codex session may be admitted into execution
and when it may activate governed work in `codex-governance-os`.

It exists so Layer 6 can distinguish session existence from permitted
execution, enforce fail-closed admission boundaries, and require evidence-backed
first-action validation before active work begins.

## Scope

This canon governs:

- canonical meaning of session initialization, admission, and activation
- admission requirements for new sessions
- admission requirements for resumed sessions
- first-action validation before active execution
- fail-closed admission outcomes and blocked execution semantics
- Layer 6 surfaces that record or interpret admission and activation

This canon does not govern:

- runtime admission enforcement
- database-backed admission engines or persistence services
- lower-layer governance authority
- full closure or terminal-state doctrine
- replacement of the state-machine canon or handoff/resume canon

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/contracts/codex-session-state-machine-canon.md`
6. `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md`
7. `docs/governance/codex-session-registry.md`
8. `docs/governance/codex-session-ledger.md`
9. this canon
10. generated pipeline artifacts and session records

This canon clarifies the boundary between continuity and permitted execution
without overriding the higher state-machine or handoff/resume authorities.

## Canonical Rules

1. `SESSION_INITIALIZED` means the session exists for a tentative governed
   purpose but has not yet been admitted to execute governed work.
2. `SESSION_ADMITTED` means the session passed the admission gate and may begin
   governed execution, but active execution has not yet started.
3. `SESSION_ACTIVE` means the session was admitted and has begun a governed
   action consistent with scope, restrictions, and authoritative evidence.
4. Session admission must precede session activation.
5. A new session may be admitted only when:
   - the governed subject is explicit
   - the work remains within supported repository boundaries
   - scope is bounded enough to identify a next valid action
   - authoritative doctrine or artifacts for the work are known
   - known restrictions and unsupported edges are preserved
   - the first active action does not require unverified assumptions to be
     treated as fact
6. A resumed session must satisfy all applicable new-session admission rules
   plus:
   - explicit predecessor handoff linkage
   - valid predecessor handoff evidence
   - scope matching or strict narrowing
   - preserved restrictions imported without silent mutation
   - unsupported boundaries remaining explicit
   - no upgrade of pending or unverified claims into authoritative truth
   - an admissible next valid action under current doctrine
7. Activation is permitted only when:
   - the first active action is identified
   - that action is within scope
   - that action respects preserved restrictions
   - that action is supported by the authoritative evidence set
   - no fail-closed admission condition remains unresolved
8. Admission must fail closed when:
   - no governed subject is identifiable
   - authoritative doctrine or evidence is unavailable
   - scope is too ambiguous to define a next valid action
   - a resume claim lacks predecessor evidence
   - preserved restrictions are missing
   - the requested action requires silent scope broadening
   - unsupported boundaries are being crossed
   - provisional information would need to be treated as fact
9. Fail-closed outcomes may be expressed through bounded labels such as
   `NOT_ADMITTED`, `PENDING_EVIDENCE`, `REJECTED`, or
   `BLOCKED_UNSUPPORTED_BOUNDARY`, but those outcomes must not be smoothed into
   active execution.
10. Registry and ledger surfaces that record admission must be able to preserve:
    - admission status
    - activation status
    - predecessor linkage when applicable
    - rejection or pending-evidence reason
    - first admitted action

## Allowed Behaviors

- initializing a session without yet admitting it
- admitting a session before the first active step begins
- blocking admission when evidence or scope clarity is insufficient
- treating resumed admission as stricter than fresh initiation
- narrowing a resumed scope when the narrowing remains explicit and governed

## Prohibited Behaviors

- treating initialization as equivalent to governed execution
- activating a session before admission is satisfied
- claiming resumed execution from predecessor awareness alone
- using unverified assumptions as the basis for first-action validation
- silently broadening scope to get past the admission gate
- overstating runtime admission enforcement that the repository does not
  implement

## Compliance Signals

Compliance is indicated when:

- active Layer 6 surfaces distinguish initialized, admitted, and active states
- admission rules are explicit for both new and resumed sessions
- first-action validation is required before active execution
- fail-closed admission conditions are explicit and inspectable
- registry and ledger surfaces can represent admission outcomes and first
  admitted action
- entry surfaces reference the canon without implying runtime enforcement

## Ambiguity Handling

- If evidence is insufficient to decide admission safely, the session should be
  treated as not admitted or pending evidence rather than active.
- If a resumed session has a plausible predecessor but lacks explicit linkage
  or preserved restrictions, it must not be admitted as resumed execution.
- If older artifacts predate this canon, they may remain historical evidence as
  long as active authoritative surfaces use the admission model explicitly.

## Governance Implications

- Future verification lanes can audit whether admission preceded active
  execution.
- Future closure and exception lanes can distinguish activation failures from
  downstream execution failures more precisely.
- Session registry, ledger, and Layer 6 doctrine should use this canon to keep
  execution legitimacy evidence-backed and fail-closed.

## Non-Goals

This canon does not:

- create a runtime admission controller
- guarantee that every session is recorded automatically
- replace the state-machine canon or the handoff/resume canon
- define terminal-state closure evidence in full
