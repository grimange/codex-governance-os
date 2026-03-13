# Template Scaffold Contract

## Purpose

This contract defines the canonical universal scaffold model for governed repositories derived from this governance OS.

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

Composability rules currently supported:

- `monorepo` may compose with `node-typescript-service` and `cli-worker`
- `cli-worker` may compose with `python-package`, `php-package`, `node-typescript-service`, and `monorepo`
- `node-typescript-service` may compose with `monorepo` and `cli-worker`

Explicit fail-closed boundary examples:

- `laravel` may not compose with `cli-worker`
- `django` may not compose with `monorepo`
- `service` may not compose with `monorepo`
- `laravel` may not compose with `django`

## Extension Rules

- projects may add runtime structure freely
- projects may not silently move or repurpose governance core surfaces
- downstream template lanes must declare whether they extend the base scaffold or add an overlay
