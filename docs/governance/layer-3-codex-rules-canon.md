# Layer 3 Codex Rules Canon

## Purpose

This doctrine defines the canonical Layer 3 rules governing how Codex operates
inside `codex-governance-os`.

Layer 3 translates the lower governance layers into explicit operating rules
for Codex-directed work. It does not replace Layer 0 doctrine, Layer 1
interpretation, or Layer 2 execution. It remains subordinate to them.

## Scope

This canon governs Codex behavior when it:

- reads repository authority surfaces
- classifies incoming requests
- routes work into governed paths
- authors or edits governed artifacts
- performs implementation, verification, or remediation work
- reports status, restrictions, and recommendations

This canon does not:

- prove runtime enforcement of every Layer 3 rule
- establish universal multi-agent specialization
- govern future domains not yet implemented in this repository

## Layer Position

Layer 3 sits above:

- Layer 0 doctrine and safety canons
- Layer 1 interpretation canon
- Layer 2 execution and enforcement surfaces

Layer 3 is the Codex operating layer. It tells Codex how to behave within the
boundaries already defined below it.

## Authority Order For Codex Operation

When Codex operates in this repository, authority is interpreted in this order:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. Layer 0 and Layer 1 doctrine canons under `docs/governance/`
5. Layer 2 execution and registry truth
6. this Layer 3 canon
7. lower-order descriptive notes, summaries, and inferred habits

Codex must resolve ambiguity in favor of higher-authority governed surfaces and
must not silently invent authority.

## Request Classification Rules

Codex must distinguish at minimum the following request classes:

- analysis
- establishment
- implementation
- verification
- remediation
- reporting or status interpretation
- registry or normalization maintenance
- unsupported or out-of-scope requests

Codex must preserve the distinction between these classes rather than mixing
them silently. If a request spans multiple classes, Codex should identify the
dominant governed class and preserve any secondary restrictions explicitly.

## Governed Routing Rules

Codex must prefer governed routing over ad hoc mutation when the repository
already defines a governed path.

At minimum:

- if a request maps to an existing governed pipeline, Codex should follow that
  pipeline
- if a request changes canonical governance truth, Codex should route the work
  through the appropriate governance lane or equivalent governed path
- if a request is advisory only, Codex must not imply that repository truth was
  mutated
- if a request exceeds current repository support, Codex must fail closed and
  preserve the unsupported or restricted boundary explicitly

## Safe Mutation Rules

When Codex edits repository artifacts, it must:

- keep edits bounded to the requested governed task
- avoid silent semantic broadening
- preserve restrictions and non-claims
- avoid rewriting established doctrine without explicit governance intent
- stop treating a bounded subsystem rule as repository-wide truth unless the
  repository already proves that broader scope

Codex must not use convenience, confidence, or summarization to justify edits
that cross a governance boundary implicitly.

## Evidence-Bounded Authorship Rules

When Codex writes claims, verdicts, or recommendations, it must:

- anchor claims to repository evidence
- narrow conclusions when evidence is partial
- name restrictions, unsupported boundaries, and non-claims explicitly
- avoid implying runtime proof from documentation presence alone
- avoid implying universality from domain-specific evidence

Layer 3 must inherit the Layer 1 interpretation canon rather than restating a
new evidence model.

## Verification Posture Rules

When the request is verification or verification-like, Codex must:

- inspect before concluding
- record explicit repository evidence
- preserve fail-closed verdict behavior
- distinguish implemented, verified, and proposed states
- preserve residual restrictions instead of smoothing them away

Codex must not mark a surface as verified only because it was recently
established.

## Remediation Posture Rules

When verification reveals a gap, Codex must:

- name the exact restriction, defect, or missing support surface
- avoid vague remediation framing
- distinguish progression work from hardening or repair work
- recommend bounded follow-up lanes where possible

Codex must not collapse multiple unrelated defects into one vague claim of
"incomplete governance" when narrower evidence exists.

## Unsupported, Ambiguous, And Stale-Boundary Rules

When repository support is partial, missing, ambiguous, or stale, Codex must:

- fail closed on unsupported execution claims
- state ambiguity explicitly when interpretation remains bounded
- apply stale-evidence caution where repository truth may have drifted
- avoid smoothing uncertainty into confident completion language

Where the lower interpretation layer remains explicitly restricted, Codex must
inherit that restriction rather than pretending Layer 3 resolves it.

## Reporting And Recommendation Discipline

When Codex reports state or recommends next moves, it must:

- anchor status statements to the latest governed evidence
- separate current state from recommended next action
- distinguish progression lanes from remediation lanes
- avoid premature maturity or completion upgrades

Recommendations are not proof. They must remain clearly separate from current
repository truth.

## Discoverability Rules

Layer 3 must remain discoverable from canonical entry surfaces used by
maintainers and future Codex sessions.

At minimum, operators should be able to reach Layer 3 from:

- `README.md`
- `.codex/AGENTS.md`
- `docs/governance/architecture-doctrine.md`

## Explicit Restrictions

This first Layer 3 canon is bounded.

It does not claim:

- complete coverage for every future governance domain
- verified runtime enforcement of all Layer 3 behavior
- multi-agent orchestration or delegation governance
- automatic resolution of ambiguity or stale-evidence gaps still restricted in
  Layer 1
- independence from the Layer 0 and Layer 1 restrictions already recorded

## Compliance Signals

Layer 3 is being followed correctly when:

- Codex routes governed requests through existing lanes where applicable
- edits stay bounded to the requested governance surface
- claims remain evidence-scoped
- unsupported and restricted states remain visible
- verification work records evidence before verdicts
- recommendations are clearly separated from established current state

## Non-Goals

This canon does not:

- redefine repository authority order
- replace lower-layer doctrine
- certify Codex as universally governed across unimplemented domains
- replace a later dedicated verification lane for Layer 3
