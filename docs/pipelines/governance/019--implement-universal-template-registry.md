---
id: 019
canonical_title: "Implement Universal Template Registry"
registry_id: "governance.templates.implement-universal-template-registry"
status: proposed
stage: implementation
classification: governance
domain: templates
priority: high
owner: codex
change_type: additive
execution_mode: governed
safety: fail-closed
requires:
  - canonical template contract
  - governed registry persistence surface
  - verification harness for template resolution
produces:
  - template registry model
  - canonical registry file layout
  - template resolution rules
  - template validation rules
  - verification artifacts
successors:
  - "020 -- Verify Universal Template Registry"
---

# 019 -- Implement Universal Template Registry

## Why this pipeline exists

`codex-governance-os` needs a single governed place where reusable templates can be registered, resolved, validated, versioned, and consumed across stacks. Without a universal template registry, templates tend to fragment into ad hoc files, per-stack copies, or hidden conventions. That creates drift, weakens governance, and makes multi-stack execution less deterministic.

This pipeline establishes a canonical template registry that lets the governance system answer four critical questions safely and consistently:

1. what templates exist,
2. what each template is allowed to produce,
3. which stacks or contexts each template supports,
4. how a caller resolves the correct template without guessing.

## Target outcome

At the end of this pipeline, `codex-governance-os` should have a governed universal template registry that:

- registers templates as first-class governed assets,
- supports stack-agnostic and stack-specific template variants,
- resolves templates deterministically from declared metadata,
- fails closed when a template is missing, ambiguous, invalid, or out of policy,
- exposes enough evidence for later verification and audit.

## Scope

This pipeline covers:

- the canonical data model for template registration,
- registry storage format and file placement,
- template metadata requirements,
- resolution precedence,
- validation and admission rules,
- governance-safe consumption by future pipelines, rules, skills, and sub-agents.

This pipeline does not require:

- implementing every template itself,
- generating templates automatically,
- enabling autonomous template mutation,
- stack-specific rendering engines beyond the registry contract.

## Problem statement

Today, universal template behavior is usually implied rather than governed. In practice this causes several failure modes:

- duplicate templates with unclear authority,
- similar templates with inconsistent names,
- stack routing based on heuristics instead of declared capability,
- missing compatibility metadata,
- no authoritative version or lifecycle state,
- no safe way to mark deprecated, restricted, or experimental templates,
- verification difficulty because registry truth is not centralized.

A governance OS needs the opposite: explicit template authority, deterministic lookup, controlled admission, and durable evidence.

## Governance intent

The registry must behave like a governed contract surface, not just a folder of snippets. That means:

- registry entries are authoritative only when admitted,
- every template has declared purpose and compatibility boundaries,
- no silent fallback to arbitrary files,
- no ambiguous multi-match resolution,
- deprecation and restriction states are first-class,
- verification can reconstruct why a template was selected or rejected.

## Canonical design

### 1) Universal template registry model

Define a canonical registry made of entries, where each entry represents one template identity rather than one arbitrary file.

Each entry should include at minimum:

- `template_id`: globally unique identifier,
- `template_name`: human-readable title,
- `template_family`: broad grouping such as `pipeline`, `rule`, `skill`, `sub_agent`, `report`, `policy`, `artifact`,
- `template_kind`: the concrete kind within the family,
- `version`: explicit version string,
- `status`: one of `draft`, `active`, `deprecated`, `restricted`, `archived`,
- `authority_level`: whether the template is canonical, advisory, experimental, or local,
- `description`: concise purpose statement,
- `inputs_contract`: what structured inputs are expected,
- `outputs_contract`: what artifacts or behaviors are expected,
- `compatible_stacks`: list such as `agnostic`, `laravel`, `django`, `php`, `python`, `node`, `docs-only`,
- `compatible_modes`: list such as `analysis`, `implementation`, `verification`, `reporting`,
- `constraints`: explicit constraints and safety limits,
- `resolution_tags`: tags used for lookup,
- `file_path`: authoritative on-disk source,
- `checksum` or content fingerprint,
- `admitted_at` and `admitted_by`,
- `supersedes` or `replaces`, if applicable.

### 2) Canonical storage layout

Create a storage layout that separates registry truth from template bodies.

Recommended layout:

```text
registry/
  docs/codex/templates/
    index.yaml
    entries/
      pipeline.base.yaml
      pipeline.verification.yaml
      rule.safety.yaml
      skill.discovery.yaml
      subagent.architecture.yaml

docs/codex/templates/
  pipelines/
  rules/
  skills/
  subagents/
  reports/
  shared/
```

Rules:

- `docs/governance/registries/templates/index.yaml` is the canonical compiled view.
- `docs/governance/registries/templates/entries/` stores one declarative registration file per template identity.
- `docs/codex/templates/` stores the template bodies.
- registry entry and template body are separate but linked.
- a template body without an admitted registry entry is not authoritative.

### 3) Resolution contract

Template resolution must be deterministic.

Recommended precedence:

1. exact `template_id`,
2. exact `template_family + template_kind + stack + mode`,
3. exact `template_family + template_kind + agnostic + mode`,
4. exact `template_family + tags + stack`,
5. fail closed.

Do not allow:

- best-effort fuzzy matching as authoritative behavior,
- silent preference for newest file in a directory,
- implicit stack inheritance without declared compatibility,
- fallback from restricted template to unrestricted sibling unless policy explicitly allows it.

### 4) Status and lifecycle semantics

Every template entry must have lifecycle semantics.

- `draft`: visible for authoring but not eligible for governed execution.
- `active`: eligible for normal resolution.
- `deprecated`: resolvable only when explicitly allowed or when verifying legacy behavior.
- `restricted`: never selected unless a policy gate authorizes it.
- `archived`: retained for evidence only, never selected.

### 5) Universal compatibility model

The registry must support both universal and specialization patterns.

Compatibility model:

- `agnostic` means the template is intended to work across stacks with no stack-specific assumptions.
- stack-specific templates may override agnostic ones only through explicit precedence.
- stack specialization must be declared, not inferred from path names alone.
- a caller may request either `strict_stack_match=true` or `allow_agnostic_fallback=true`.

### 6) Validation and admission gate

A registry entry should not become active until it passes admission checks.

Minimum admission rules:

- all required metadata fields present,
- unique `template_id`,
- valid file path exists,
- declared family and kind allowed by schema,
- lifecycle status valid,
- compatibility list valid,
- no duplicate active entries for the same authoritative resolution key,
- template body passes lint or syntax validation appropriate to its type,
- fingerprint matches current file content,
- supersession chain is non-conflicting.

If any check fails, admission must return a blocked outcome with explicit reasons.

## Implementation plan

### Step 1: Define template registry schema

Create the canonical schema for registry entries and for the compiled registry index.

Implementation goals:

- define required and optional fields,
- define enumerations for family, kind, status, authority, and compatibility,
- define uniqueness rules,
- define validation error classes.

Deliverables:

- registry schema document,
- machine-readable schema file if supported,
- example valid and invalid entries.

### Step 2: Establish canonical filesystem layout

Create the registry and templates directory structure.

Implementation goals:

- ensure path conventions are deterministic,
- reserve distinct folders for registry metadata and template content,
- prevent mixed-purpose storage.

Deliverables:

- layout specification,
- bootstrapped folder structure,
- placeholder entries for initial canonical templates.

### Step 3: Implement registry loader

Implement a loader that reads entry files, validates them, and builds a compiled index.

Implementation goals:

- stable ordering,
- duplicate detection,
- strict schema enforcement,
- reproducible compiled output.

Deliverables:

- registry load command or module,
- compiled registry index,
- machine-readable validation output.

### Step 4: Implement deterministic resolver

Implement the resolver used by governance flows to select the correct template.

Implementation goals:

- exact-match semantics,
- explicit precedence,
- no silent ambiguity,
- traceable selection reason.

Deliverables:

- resolver function or command,
- resolution trace format,
- explicit blocked outcomes for miss, ambiguity, or policy conflict.

### Step 5: Add lifecycle and safety enforcement

Implement rules for active, deprecated, restricted, and archived templates.

Implementation goals:

- status-aware resolution,
- policy-aware restriction handling,
- deprecation warnings when allowed,
- hard stop on archived selection.

Deliverables:

- lifecycle enforcement logic,
- policy check integration point,
- blocked outcome catalog.

### Step 6: Seed canonical starter templates

Register a minimal initial set of high-value templates so the registry is useful immediately.

Suggested starter set:

- universal pipeline template,
- universal verification pipeline template,
- universal codex rule template,
- universal codex skill template,
- universal sub-agent specialization template,
- universal governance report template.

Deliverables:

- admitted starter entries,
- registry index including the starter set,
- evidence that each starter template resolves correctly.

### Step 7: Expose registry evidence surface

The governance system must be able to report registry truth.

Evidence surface should support:

- list all templates,
- list active templates,
- show deprecated or restricted templates,
- explain how a given template request resolved,
- show why an entry failed admission.

Deliverables:

- CLI or governance command support,
- human-readable and machine-readable output,
- audit-friendly logs.

## Acceptance criteria

This pipeline is complete when all of the following are true:

1. there is a canonical template registry schema,
2. registry entries are separate from template bodies,
3. a compiled registry index can be reproduced deterministically,
4. resolution is deterministic and traceable,
5. ambiguity causes fail-closed behavior,
6. lifecycle states are enforced,
7. at least one agnostic template and one specialized template can coexist safely,
8. starter templates are admitted and queryable,
9. registry evidence can be surfaced for verification,
10. the system can distinguish authoritative templates from non-admitted files.

## Verification plan

Verification should prove behavior, not just file existence.

### Required checks

- schema validation passes for valid entries,
- schema validation fails for malformed entries,
- duplicate resolution key detection blocks admission,
- missing body file blocks admission,
- ambiguous resolution returns blocked,
- agnostic fallback works only when explicitly allowed,
- restricted template cannot resolve without policy authorization,
- deprecated template emits controlled warning or rejection based on mode,
- archived template never resolves,
- compiled registry output is stable across repeated runs.

### Example verification commands

These are representative and should be adapted to the repository runtime:

```bash
python3 tools/governance/template_registry.py validate
python3 tools/governance/template_registry.py build-index
python3 tools/governance/template_registry.py resolve --template-id pipeline.universal.base
python3 tools/governance/template_registry.py resolve --family pipeline --kind verification --stack django --mode verification
python3 tools/governance/template_registry.py list --status active
```

## Expected artifacts

Create a governed artifact bundle under a directory similar to:

```text
docs/pipelines/governance/implement-universal-template-registry/
```

Recommended artifact set:

1. `01-problem-statement.md`
2. `02-registry-contract.md`
3. `03-filesystem-layout.md`
4. `04-resolution-rules.md`
5. `05-validation-and-lifecycle-rules.md`
6. `06-implementation-plan.md`
7. `07-verification-plan.md`
8. `08-final-verdict.md`

## Final verdict language

Use one of these canonical outcomes:

- `UNIVERSAL_TEMPLATE_REGISTRY_IMPLEMENTED`
- `UNIVERSAL_TEMPLATE_REGISTRY_IMPLEMENTED_WITH_RESTRICTIONS`
- `UNIVERSAL_TEMPLATE_REGISTRY_DESIGN_READY_BUT_NOT_IMPLEMENTED`
- `UNIVERSAL_TEMPLATE_REGISTRY_BLOCKED`

## Recommended final verdict target

For a successful implementation lane, the target verdict is:

`UNIVERSAL_TEMPLATE_REGISTRY_IMPLEMENTED`

If the registry exists but starter templates, lifecycle gates, or deterministic resolution are incomplete, use:

`UNIVERSAL_TEMPLATE_REGISTRY_IMPLEMENTED_WITH_RESTRICTIONS`

## Non-goals and guardrails

Do not let this pipeline drift into unrelated work.

Non-goals:

- building a full template marketplace,
- runtime content generation policy,
- automatic template mutation without governance,
- semantic ranking of templates as authoritative behavior,
- stack-specific rendering engines for every language.

Guardrails:

- no silent template fallback,
- no authority without admission,
- no active duplicate identities,
- no unrestricted use of restricted or archived templates,
- no registry mutation without evidence.

## Follow-up pipeline

The immediate next lane should verify that the implementation behaves as designed:

- `020 -- Verify Universal Template Registry`

That verification lane should test schema enforcement, deterministic resolution, lifecycle handling, and starter-template coverage end to end.
