---
id: "022"
title: "Implement Universal Template Scaffold"
slug: "implement-universal-template-scaffold"
registry_id: "governance.foundation.implement-universal-template-scaffold"
stage: "implementation"
status: "proposed"
classification: "build"
priority: "high"
owner: "codex"
depends_on: []
outputs: ["docs/pipelines/governance/implement-universal-template-scaffold/01-problem-statement.md", "docs/pipelines/governance/implement-universal-template-scaffold/02-target-template-model.md", "docs/pipelines/governance/implement-universal-template-scaffold/03-scaffold-contract.md", "docs/pipelines/governance/implement-universal-template-scaffold/04-implementation-plan.md", "docs/pipelines/governance/implement-universal-template-scaffold/05-verification-plan.md", "docs/pipelines/governance/implement-universal-template-scaffold/06-final-verdict.md"]
success_criteria: ["A canonical universal template scaffold exists for governance-aware repositories.", "The scaffold separates required, optional, and project-specific template surfaces.", "The scaffold can be reused across Laravel, Django, package, service, and multi-repo governance contexts without changing the governance contract.", "Verification defines how to prove the scaffold is present, normalized, and safe to extend."]
---

# 022 -- Implement Universal Template Scaffold

## Purpose

Implement a canonical, reusable template scaffold that gives `codex-governance-os` a project-agnostic starting structure. The scaffold must be broad enough to support application repositories, packages, services, platform repositories, and modernization programs, while still remaining strict enough to preserve governed execution, evidence recording, and safe extensibility.

The main outcome of this lane is not a single app template. It is a universal scaffold contract that future repo templates, package templates, and specialization templates can inherit from without redefining governance from scratch.

## Why this pipeline exists

Without a universal scaffold, each new governed repository tends to reinvent structure, naming, and bootstrapping rules. That creates drift in:

- governance entrypoints
- artifact locations
- evidence conventions
- template composition
- specialization boundaries
- portability across stacks

This lane establishes one canonical template skeleton so the governance layer becomes reusable infrastructure rather than a one-off repo arrangement.

## Objectives

1. Define the minimum universal scaffold required for any governance-enabled repository.
2. Separate scaffold layers into:
   - governance core
   - repository template surfaces
   - specialization overlays
   - project runtime surfaces
3. Ensure the scaffold works across multiple stacks such as:
   - Laravel
   - Django
   - generic Python packages
   - PHP packages
   - service repositories
   - modernization monorepos
4. Preserve a governed path for future template specialization without allowing uncontrolled drift.
5. Make scaffold verification explicit and repeatable.

## In scope

This pipeline may define and stage:

- canonical top-level scaffold directories
- required governance directories
- template extension points
- specialization slots for stack-specific overlays
- naming rules for scaffolded assets
- minimal bootstrap files
- verification expectations
- evidence pack expectations for downstream template lanes

## Out of scope

This pipeline does not:

- hard-code a Laravel-only or Django-only repository structure
- require a specific CI provider
- require a specific language runtime
- implement every specialization template
- replace project-specific application architecture
- invent runtime behavior not needed for governance portability

## Canonical design principle

The universal scaffold must be **governance-first, stack-agnostic, extension-safe**.

That means:

- governance structure is stable
- stack specifics live in overlays
- project implementation remains free inside governed boundaries
- templates compose by inheritance and convention, not by duplication

## Required scaffold model

The universal scaffold should be organized into four layers.

### Layer 1 — Governance Core

This is the invariant base required in every governed repository.

Expected surfaces:

- `docs/pipelines/`
- `docs/pipelines/governance/`
- `docs/governance/`
- `tools/governance/`
- `tools/templates/`
- `artifacts/` or another canonical evidence surface if the repository uses a different governed evidence root
- canonical operator instructions for governed execution

Responsibilities:

- pipeline routing
- governance state handling
- admission and normalization rules
- evidence recording
- deterministic verification entrypoints
- template discovery and scaffold auditing

### Layer 2 — Universal Template Surface

This is the reusable, project-agnostic template layer.

Expected surfaces:

- `templates/base/`
- `templates/governance/`
- `templates/shared/`
- `templates/overlays/`

Responsibilities:

- base repository skeleton
- reusable governance documentation shells
- shared config examples
- scaffold manifests
- placeholder contracts for extension-safe generation

### Layer 3 — Specialization Overlay Surface

This is where stack-specific or topology-specific templates live.

Example overlays:

- `templates/overlays/laravel/`
- `templates/overlays/django/`
- `templates/overlays/php-package/`
- `templates/overlays/python-package/`
- `templates/overlays/service/`
- `templates/overlays/monorepo/`

Responsibilities:

- stack-aware directory additions
- language-aware starter contracts
- runtime-specific conventions
- optional integration packs

Rule:

No specialization overlay may redefine governance core semantics. It can extend scaffold structure, but it must not fork the governance contract.

### Layer 4 — Project Realization Surface

This is the instantiated repository produced from the scaffold plus overlays.

Responsibilities:

- actual application code
- actual configuration
- actual runtime integration
- actual domain artifacts
- project-owned extensions within governed rules

## Canonical scaffold tree

A recommended universal scaffold tree is shown below.

```text
/
├── docs/
│   ├── governance/
│   └── pipelines/
│       └── governance/
├── tools/
│   ├── governance/
│   └── templates/
├── templates/
│   ├── base/
│   ├── governance/
│   ├── shared/
│   └── overlays/
│       ├── laravel/
│       ├── django/
│       ├── php-package/
│       ├── python-package/
│       ├── service/
│       └── monorepo/
├── artifacts/
├── config/
├── scripts/
├── src/ or app/ or backend/ or service-specific runtime roots
└── README.md
```

This tree is illustrative, not rigid at the runtime layer. The governance and template layers are the stable part.

## Universal scaffold contract

The scaffold produced by this lane must satisfy the following contract.

### Contract A — Governance portability

A repository created from the scaffold must be capable of carrying the governance OS without requiring stack-specific rewrites to the governance core.

### Contract B — Overlay composition

A repository must be able to apply one or more overlays without replacing the base scaffold.

### Contract C — Safe defaults

The scaffold must default to the safest minimal shape:
- explicit docs surface
- explicit tools surface
- explicit templates surface
- explicit evidence surface
- no hidden assumptions about framework or deployment provider

### Contract D — Deterministic discoverability

A governance-aware agent must be able to discover:
- where pipelines live
- where governance tools live
- where templates live
- where evidence belongs
- where specialization overlays are declared

### Contract E — Non-destructive extension

Projects may add runtime structure freely, but may not silently alter the meaning of the governance core directories.

## Required implementation outputs

This pipeline should produce or normalize the following artifacts under:

`docs/pipelines/governance/implement-universal-template-scaffold/`

### 01-problem-statement.md

Must explain:
- why template drift is harmful
- why universal scaffolding is needed
- what portability problem this pipeline solves

### 02-target-template-model.md

Must define:
- the four-layer scaffold model
- required vs optional scaffold surfaces
- overlay rules

### 03-scaffold-contract.md

Must define:
- canonical directory contract
- naming conventions
- composition rules
- extension restrictions

### 04-implementation-plan.md

Must describe:
- how the scaffold is created
- how template manifests are declared
- how overlays are attached
- how downstream lanes can specialize safely

### 05-verification-plan.md

Must define:
- how to verify scaffold presence
- how to verify overlay compatibility
- how to verify governance core integrity
- how to detect template drift

### 06-final-verdict.md

Must conclude with a canonical verdict such as:

- `UNIVERSAL_TEMPLATE_SCAFFOLD_IMPLEMENTED`
- `UNIVERSAL_TEMPLATE_SCAFFOLD_IMPLEMENTED_WITH_GAPS`
- `UNIVERSAL_TEMPLATE_SCAFFOLD_DEFINED_BUT_NOT_REALIZED`

## Recommended file-level additions

The implementation side of this lane should strongly consider adding these governed assets:

- `templates/base/README.md`
- `templates/governance/README.md`
- `templates/shared/README.md`
- `templates/overlays/README.md`
- `tools/templates/manifest.schema.json` or equivalent machine-readable contract
- `tools/templates/list_templates.py` or equivalent discovery helper
- `docs/governance/template-scaffold-contract.md`

These are not mandatory if equivalent governed surfaces already exist, but the lane should record what fulfills their role.

## Template manifest recommendation

To support future automation, the scaffold should define a machine-readable template manifest with fields such as:

- template_name
- template_type
- base_template
- compatible_overlays
- required_surfaces
- optional_surfaces
- governance_compatibility
- maturity
- supported_runtime_shapes

Example conceptual manifest:

```json
{
  "template_name": "universal-base",
  "template_type": "base",
  "base_template": null,
  "compatible_overlays": [
    "laravel",
    "django",
    "php-package",
    "python-package",
    "service",
    "monorepo"
  ],
  "required_surfaces": [
    "docs/pipelines",
    "docs/governance",
    "tools/governance",
    "tools/templates",
    "templates"
  ],
  "governance_compatibility": "required",
  "maturity": "canonical"
}
```

## Safe specialization rules

Any downstream template lane built on top of this scaffold must obey these rules:

1. It may add files and directories.
2. It may specialize runtime structure.
3. It may provide stack-specific helpers.
4. It may not redefine the governance core contract.
5. It may not move evidence surfaces without an explicit governance lane.
6. It may not introduce hidden template assumptions that break discoverability.
7. It must declare whether it is a base template, overlay, or project realization.

## Verification expectations

Verification for this lane should prove all of the following:

1. A universal scaffold definition exists.
2. Governance core surfaces are explicitly represented.
3. Template overlays are explicitly separated from the base scaffold.
4. The scaffold is not tied to a single framework.
5. A downstream stack can be modeled as an overlay rather than a fork.
6. The final verdict is backed by repository evidence.

## Suggested verification commands

Use repository-appropriate commands, but the verification pack should consider commands such as:

```bash
find templates -maxdepth 3 -type d
find tools -maxdepth 3 -type d
find docs/pipelines/governance -maxdepth 2 -type f
python3 tools/governance/gov.py --format json preflight-lane 022
python3 tools/governance/gov.py --format json admit-lane 022
```

If the repository already has scaffold inspection tooling, include it as primary evidence.

## Downstream pipeline enablement

This lane should unlock later lanes such as:

- establish universal template manifest registry
- implement overlay compatibility validation
- add Laravel overlay template
- add Django overlay template
- add package template overlays
- implement scaffold drift detection
- generate new governed repositories from template manifests

## Risks and failure modes

### Risk 1 — Fake universality

A template may be called universal while actually encoding one framework's assumptions.

Mitigation:
Require explicit overlay separation and contract review.

### Risk 2 — Governance drift inside overlays

Stack templates may accidentally fork governance rules.

Mitigation:
State clearly that overlays extend runtime structure only and cannot redefine governance core semantics.

### Risk 3 — Too much abstraction

A scaffold can become so abstract that it stops being practically useful.

Mitigation:
Keep the core minimal, concrete, and discoverable.

### Risk 4 — Unverifiable template state

If the scaffold exists only conceptually, future automation cannot rely on it.

Mitigation:
Require machine-readable manifests or equivalent governed discovery surfaces.

## Completion criteria

This pipeline is complete when:

- a universal scaffold model is defined
- governance core surfaces are explicit
- template and overlay boundaries are explicit
- verification can distinguish universal scaffold from project-specific realization
- the final verdict is recorded with evidence

## Canonical final verdict

Preferred final verdict:

`UNIVERSAL_TEMPLATE_SCAFFOLD_IMPLEMENTED`

Allowed restricted verdicts:

- `UNIVERSAL_TEMPLATE_SCAFFOLD_IMPLEMENTED_WITH_GAPS`
- `UNIVERSAL_TEMPLATE_SCAFFOLD_DEFINED_BUT_NOT_REALIZED`

## Notes for `codex-governance-os`

For this repository specifically, this lane should be treated as a foundation pipeline that turns the repo from a single governed implementation into a reusable governance template platform. It is especially relevant if the repository will later support:

- repo template generation
- package distribution
- cross-language project bootstrapping
- multi-agent specialization packs
- governance overlays for different application types
