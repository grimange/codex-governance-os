# Universal Governance Template System

## Purpose

This directory defines the canonical template families used to author governed artifacts in a shape-stable and machine-checkable way.

## Contents

- `template-registry.yaml`: canonical registry of template families, frontmatter requirements, sections, overlays, validator mapping, and scaffold mapping.
- `../registries/templates/index.yaml`: compiled admitted-template registry index.
- `../registries/templates/entries/`: one admitted registry entry per template identity.
- `../../codex/templates/`: admitted template bodies grouped by family under the docs-root Codex tree.
- `../../codex/templates/manifests/`: machine-readable universal scaffold manifests.
- `pipeline-template.md`: canonical template for pipeline definitions and design lanes.
- `verification-template.md`: canonical template for verification lanes and evidence-backed closure checks.
- `rule-template.md`: canonical template for governance rules and policy surfaces.
- `skill-template.md`: canonical template for skill contracts and invocation boundaries.
- `sub-agent-template.md`: canonical template for governed sub-agent specializations.
- `instruction-template.md`: canonical template for governed instruction artifacts.
- `report-template.md`: canonical template for governed report artifacts.
- `evidence-pack-template.md`: canonical template for evidence bundles and governed execution packs.
- `decision-template.md`: canonical template for governance and architecture decisions.
- `remediation-template.md`: canonical template for bounded remediation plans.

## Operating Rules

- The `docs/` directory is the authoritative root for all governance and Codex-related files in this repository.
- The universal core comes first; overlays may extend but must not weaken it.
- Template conformance is validated by `tools/governance/template_lint.py`.
- New governed artifacts may be scaffolded deterministically by `tools/governance/template_scaffold.py`.
- Repository scaffold manifests are listed by `tools/templates/list_templates.py` and governed by `tools/templates/manifest.schema.json`.
- Template family definitions, admitted template entries, compiled index construction, and deterministic resolution are loaded through `tools/governance/template_registry.py`.
- Use `python tools/governance/template_lint.py lint-template <path>` for single-template validation and `python tools/governance/template_lint.py lint-templates` for repo-wide template lint checks.

## Overlay Model

- Stack overlays are defined in the registry and may add stack-aware expectations without weakening the universal core.
- Project overlays are repository-local extensions and must preserve required sections, frontmatter keys, and fail-closed semantics.

## Enforcement Model

The template system starts in advisory mode and can move toward enforcing mode only after verification lanes prove registry, linter, and scaffold behavior across representative fixtures.

## Admitted Template Registry

- Template bodies under `docs/codex/templates/` are not authoritative unless they have an admitted registry entry under `docs/governance/registries/templates/entries/`.
- `docs/governance/registries/templates/index.yaml` is the compiled canonical view used for resolution evidence.
- Resolution fails closed on missing, ambiguous, restricted, deprecated-without-opt-in, archived, or invalid template requests.
