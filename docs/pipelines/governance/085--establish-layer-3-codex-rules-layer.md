# 085 — Establish Layer 3 Codex Rules Layer

---

registry_id: governance.layer3.establish-layer-3-codex-rules-layer
status: proposed
stage: analysis
authoritative_phase: governance
parent_layer: layer-3
supports_layers:

* layer-4
* layer-5
  precedence: canonical
  blocking: false
  requires:
* 080--verify-layer-0-doctrine-closure-and-discoverability.md
* 081--verify-layer-1-interpretation-canon-closure.md
* 082--verify-layer-2-enforcement-and-execution-closure.md
  suggested_next:
* 086--verify-layer-3-codex-rules-layer.md
* 087--establish-layer-3-codex-request-classification-and-routing-boundary.md
* 088--establish-layer-3-codex-safe-mutation-and-artifact-editing-boundary.md
  title: Establish Layer 3 Codex Rules Layer

---

# Codex Pipeline — Establish Layer 3 Codex Rules Layer

## 1. Purpose

Establish the canonical Layer 3 rules that govern how Codex behaves inside `codex-governance-os`. This layer sits above Layer 0 doctrine, Layer 1 interpretation, and Layer 2 execution. Its role is to translate those lower-layer governance foundations into explicit operating rules for Codex-directed work.

This pipeline defines the canonical behavioral rules for governed Codex operation. It does not claim universal autonomous governance, complete multi-agent specialization, or full domain coverage across every future governance surface. It establishes the first canonical rules layer that Codex must follow when reading, interpreting, routing, authoring, editing, verifying, and reporting within the Governance OS.

## 2. Why this exists

Layer 0 now provides a bounded doctrine base.

Layer 1 now provides a bounded interpretation layer.

Layer 2 now provides a bounded enforcement and execution layer.

However, the repository still needs a dedicated layer that answers a separate question:

**What explicit rules must Codex follow when operating on top of those governance layers?**

Without a Layer 3 rules layer, Codex behavior remains partially implicit. A governance-aware repository can still have strong doctrine and execution machinery while leaving too much of Codex behavior to inferred habit or scattered instruction surfaces.

This lane closes that gap by establishing a canonical rules layer for:

* governed instruction intake
* request classification
* routing expectations
* evidence-bounded authoring
* safe mutation behavior
* restriction preservation
* verification posture
* bounded reporting
* authority-respecting interpretation
* fail-closed handling of unsupported asks

## 3. Scope

This pipeline establishes the canonical Layer 3 Codex rules surface.

In scope:

* defining the role of Layer 3 within the governance stack
* defining canonical Codex operating rules
* defining how Codex should classify work requests
* defining routing behavior into governed surfaces
* defining safe authoring and editing expectations
* defining restriction-preserving behavior during implementation and verification
* defining bounded reporting and verdict behavior
* defining how Codex should behave when repository support is partial, missing, or ambiguous
* defining discoverability and authority expectations for Layer 3 rules

Out of scope:

* proving runtime enforcement of every Layer 3 rule
* establishing universal multi-agent specialization
* establishing collaboration orchestration beyond single-agent governed operation
* claiming complete coverage for future governance domains not yet implemented
* replacing lower-layer doctrine, interpretation, or execution canons

## 4. Target outcome

The target outcome is a canonical Layer 3 rules artifact that can be treated as the governing operating layer for Codex behavior in the repository.

Preferred outcome:

* `LAYER_3_CODEX_RULES_LAYER_ESTABLISHED`

Allowed bounded outcomes if the implementation is necessarily partial:

* `LAYER_3_CODEX_RULES_LAYER_ESTABLISHED_WITH_RESTRICTIONS`

The lane must fail closed. If a rule boundary cannot be honestly established, the canon must record the restriction rather than imply that Codex is governed in ways not actually supported.

## 5. Canonical questions this layer must answer

The established Layer 3 rules layer should answer these questions explicitly:

1. What sources are authoritative when Codex operates in the repository?
2. How must Codex classify incoming requests?
3. When must Codex route work through governed pipeline or governance execution surfaces?
4. What kinds of edits are safe, bounded, or disallowed without explicit governance support?
5. How must Codex preserve evidence boundaries and restrictions when authoring or revising artifacts?
6. How must Codex behave during verification, implementation, remediation, and reporting work?
7. How must Codex respond when repository support is incomplete, unsupported, ambiguous, or stale?
8. How does Layer 3 remain subordinate to Layer 0, Layer 1, and Layer 2 rather than replacing them?

## 6. Required canonical outputs

This pipeline should establish at minimum these canonical outputs:

* `docs/governance/layer-3-codex-rules-canon.md`
* discoverability links from canonical entry surfaces where appropriate
* registry entry for pipeline 085
* a governed artifact bundle recording the establishment decision and boundaries

If the repository already has an equivalent codex-rules surface, this lane should normalize and elevate it rather than duplicating it.

## 7. Required rule domains

The Layer 3 canon established by this lane must cover at least the following domains.

### 7.1 Authority order and canonical sources

Define the authority order Codex must respect when multiple repository surfaces exist.

At minimum, the layer should clarify the relationship among:

* governance doctrine canons
* interpretation canons
* execution surfaces and registry truth
* canonical pipeline definitions
* repository entry surfaces such as `README.md` and `.codex/AGENTS.md`
* local non-canonical notes or implied habits

The canon must make clear that Codex should resolve ambiguity in favor of higher-authority governed surfaces and must not silently invent authority.

### 7.2 Request classification

Define the minimum request classes Codex must distinguish.

At minimum, the canon should classify asks into bounded categories such as:

* analysis
* establishment
* implementation
* verification
* remediation
* reporting or status interpretation
* registry or normalization maintenance
* unsupported or out-of-scope asks

The canon should require Codex to preserve the distinction between these classes rather than mixing them silently.

### 7.3 Governed routing

Define when Codex must route work through governed pipeline surfaces or governance execution entry points instead of acting directly.

This should cover at minimum:

* requests that map to an existing governed pipeline
* requests that change canonical governance surfaces
* requests that require registry-aligned lane execution
* requests that should remain advisory rather than mutating repository truth

The canon must explicitly prefer governed routing over ad hoc mutation when the repository already defines a governed path.

### 7.4 Safe mutation and artifact editing

Define how Codex may safely create or modify repository artifacts.

At minimum, the canon should require:

* bounded edits tied to the requested lane or governed task
* no silent semantic broadening during edits
* preservation of restrictions and non-claims
* no rewriting of established doctrine without explicit governance intent
* explicit handling when a requested edit crosses a governance boundary
* avoidance of hidden mutation outside the declared scope

### 7.5 Evidence-bounded authorship

Define how Codex should write claims, verdicts, and recommendations.

At minimum, the canon should require:

* claims anchored to repository evidence
* bounded conclusions when evidence is partial
* explicit naming of restrictions, unsupported boundaries, and non-claims
* no implication of runtime proof from documentation alone
* no implication of universality from domain-specific evidence

### 7.6 Verification posture

Define how Codex must behave when the request is a verification lane or verification-like task.

At minimum, the canon should require:

* inspection before conclusion
* explicit evidence recording
* fail-closed verdicts
* distinction between implemented, verified, and merely proposed states
* explicit preservation of residual restrictions

### 7.7 Remediation posture

Define how Codex should behave when verification reveals gaps.

At minimum, the canon should require:

* naming the exact restriction or defect
* avoiding vague “fix everything” remediation framing
* distinguishing progression lanes from hardening lanes
* recommending bounded follow-up pipelines instead of overclaiming closure

### 7.8 Unsupported, ambiguous, or stale-boundary handling

Define how Codex should behave when repository support is incomplete or evidence is weak.

At minimum, the canon should require:

* fail-closed behavior on unsupported execution claims
* explicit ambiguity statements when interpretation is bounded
* explicit stale-evidence caution where repository truth may have drifted
* no smoothing over of uncertainty into confident language

### 7.9 Reporting and recommendation discipline

Define how Codex should report current state and recommend next moves.

At minimum, the canon should require:

* status statements anchored to the latest recorded governed evidence
* separation of current state from recommended next action
* recommendations that distinguish progression from remediation
* no premature declaration of completion or maturity upgrades

### 7.10 Discoverability and operator usability

Define how Layer 3 should be surfaced so operators and future Codex sessions can find it.

At minimum, the canon should require discoverability from appropriate canonical entry surfaces such as:

* `README.md`
* `.codex/AGENTS.md`
* `docs/governance/architecture-doctrine.md`

## 8. Required artifact bundle

Create an artifact bundle under:

* `docs/pipelines/governance/establish-layer-3-codex-rules-layer/`

The bundle must contain at least these files:

1. `01-problem-statement.md`
   Explain why doctrine, interpretation, and execution are insufficient without an explicit Codex rules layer.

2. `02-layer-3-role-definition.md`
   Define the purpose of Layer 3 in the governance stack and its relationship to Layers 0–2.

3. `03-codex-rule-domain-inventory.md`
   Inventory the rule domains the canon must cover.

4. `04-layer-3-codex-rules-canon.md`
   Draft or establish the canonical rules surface.

5. `05-discoverability-and-authority-integration.md`
   Record how Layer 3 is integrated into canonical entry surfaces and authority order.

6. `06-restrictions-and-non-claims.md`
   Record all remaining limitations and non-claims for the newly established layer.

7. `07-verification-plan.md`
   Define how a later verification lane should verify Layer 3.

8. `08-final-verdict.md`
   Record the final establishment verdict.

## 9. Execution method

1. Inspect the verified lower-layer boundaries from 080, 081, and 082.
2. Define the role of Layer 3 as subordinate to, and constrained by, Layers 0–2.
3. Inventory the rule domains needed for Codex behavior.
4. Establish the canonical Layer 3 rules surface.
5. Integrate Layer 3 discoverability into canonical repository entry points where appropriate.
6. Record explicit restrictions and non-claims.
7. Define a clear verification plan for the next lane.
8. Record the final bounded verdict.

## 10. Acceptance criteria

This lane is complete when all of the following are true:

* a canonical Layer 3 codex rules surface exists
* Layer 3’s role in the governance architecture is explicit
* the minimum required rule domains are covered
* authority order is explicit and does not contradict lower layers
* discoverability integration is recorded
* restrictions and non-claims are explicitly preserved
* a later verification lane is clearly defined
* the final verdict is bounded and evidence-respecting

## 11. Registry and reporting updates

When this lane is executed:

* register pipeline 085 in `docs/pipelines/registry/pipeline-registry.md`
* ensure the pipeline metadata is normalized
* record the final verdict in the artifact bundle
* update discoverability surfaces if Layer 3 becomes canonical

This lane must not claim that Layer 3 is verified merely because it is established. Verification belongs to the next lane.

## 12. Recommended follow-up

The immediate next lane after successful establishment should be:

* `086--verify-layer-3-codex-rules-layer.md`

Likely hardening follow-ups may include:

* `087--establish-layer-3-codex-request-classification-and-routing-boundary.md`
* `088--establish-layer-3-codex-safe-mutation-and-artifact-editing-boundary.md`
* a dedicated ambiguity and stale-evidence handling canon if Layer 3 needs to make those surfaces more explicit
* later collaboration and sub-agent specialization layers after the single-agent rules layer is verified

## 13. Safety notes

This lane must preserve governance safety invariants while establishing Codex rules:

* no unsupported expansion of Codex authority
* no silent replacement of lower-layer doctrine
* no implication of universal governance coverage from one domain
* no erasure of existing restrictions inherited from Layers 0–2
* no claim that established rules are automatically enforced unless separately verified

## 14. Definition of done

Done means the repository has an explicit canonical Layer 3 rules layer that defines how Codex should operate inside `codex-governance-os`, with authority order, routing discipline, safe mutation expectations, evidence-bounded authorship, reporting discipline, and all known limitations explicitly recorded.
