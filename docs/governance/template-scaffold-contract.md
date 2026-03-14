# Template Scaffold Contract

## Purpose

This contract defines the canonical universal scaffold model for governed repositories derived from this governance OS.

The certified overlay composition boundary for this scaffold is governed by `docs/contracts/universal-template-composition-contract.md`.

## Canonical Rule

The universal scaffold is governance-first, stack-agnostic, and extension-safe.

## Layer Model

The scaffold has four canonical layers:

1. Governance core
2. Universal template surface
3. Specialization overlay surface
4. Project realization surface

## Governance Core Requirements

Every governed repository scaffold must preserve these minimum surfaces:

- `docs/governance/`
- `docs/pipelines/`
- `docs/pipelines/governance/`
- `docs/codex/templates/`
- `docs/governance/registries/templates/`
- `tools/governance/`
- `tools/templates/`
- `artifacts/`

## Overlay Rules

- overlays may add runtime-specific surfaces
- overlays must declare their compatible base template
- overlays that can coexist with other overlays must declare explicit overlay-to-overlay compatibility
- overlays must declare governed composition capabilities: `provides`, `requires`, `conflicts`, and `composition_role`
- overlays must not redefine governance core semantics
- overlays must remain discoverable through the scaffold manifest inventory

## Supported Overlay Set

The current supported overlay inventory is:

- `laravel`
- `django`
- `python-package`
- `php-package`
- `service`
- `monorepo`
- `node-typescript-service`
- `cli-worker`
- `scheduler`

Certified composition truth is delegated to `docs/contracts/universal-template-composition-contract.md`, including the rule that single admitted overlays remain valid while multi-overlay expansion is allowlisted explicitly.

The scheduler overlay is explicitly recognized as an admitted single-overlay realization in addition to its certified multi-overlay combinations. Framework-native scheduler admissions currently exist for the direct pairs `laravel + scheduler` and `django + scheduler`, and both remain bounded to direct-pair contracts.

Capability vocabulary is governed by `tools/governance/template_capability_registry.json`. Capability evaluation is used to verify that manifest declarations remain consistent with the certified matrix and explicit fail-closed boundaries.

Capability conflict semantics are also governed there. Rejected capability compositions must expose deterministic taxonomy via canonical conflict codes even when the top-level decision class remains `explicitly-rejected`, `capability-conflict`, or `capability-role-conflict`.

Overlay composability rules currently supported:

- `laravel` may compose with `monorepo` and `scheduler`
- `django` may compose with `monorepo` and `scheduler`
- `service` may compose with `monorepo`
- `monorepo` may compose with `laravel`, `django`, `service`, `node-typescript-service`, and `cli-worker`
- `monorepo` may compose with `laravel`, `django`, `service`, `node-typescript-service`, `cli-worker`, and `scheduler`
- `cli-worker` may compose with `python-package`, `php-package`, `node-typescript-service`, `monorepo`, and `scheduler`
- `python-package` may compose with `cli-worker` and `scheduler`
- `scheduler` may compose with `cli-worker`, `django`, `laravel`, `monorepo`, and `python-package`
- `node-typescript-service` may compose with `monorepo` and `cli-worker`
- the certified matrix may also admit explicit triple-overlay compositions validated through the governed capability registry

Explicit fail-closed boundary examples recorded by the certified contract:

- `laravel` may not compose with `cli-worker`
- `laravel` may not compose with `django`
Framework scheduler support is not generic within the universal overlay model. `laravel + scheduler` and `django + scheduler` are admitted only through dedicated framework-native scheduler contracts, and broader compound framework scheduler compositions remain unsupported unless a later lane admits them explicitly.

## Extension Rules

- projects may add runtime structure freely
- projects may not silently move or repurpose governance core surfaces
- downstream template lanes must declare whether they extend the base scaffold or add an overlay
