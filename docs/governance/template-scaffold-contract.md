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

Certified composition truth is delegated to `docs/contracts/universal-template-composition-contract.md`, including the rule that single admitted overlays remain valid while multi-overlay expansion is allowlisted explicitly.

Overlay composability rules currently supported:

- `laravel` may compose with `monorepo`
- `django` may compose with `monorepo`
- `service` may compose with `monorepo`
- `monorepo` may compose with `laravel`, `django`, `service`, `node-typescript-service`, and `cli-worker`
- `cli-worker` may compose with `python-package`, `php-package`, `node-typescript-service`, and `monorepo`
- `node-typescript-service` may compose with `monorepo` and `cli-worker`

Explicit fail-closed boundary examples recorded by the certified contract:

- `laravel` may not compose with `cli-worker`
- `laravel` may not compose with `django`

## Extension Rules

- projects may add runtime structure freely
- projects may not silently move or repurpose governance core surfaces
- downstream template lanes must declare whether they extend the base scaffold or add an overlay
