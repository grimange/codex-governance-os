# Universal Governance Template System

## Purpose

This directory defines the canonical template families used to author governed artifacts in a shape-stable and machine-checkable way.

## Contents

- `template-registry.yaml`: canonical registry of template families, frontmatter requirements, sections, overlays, validator mapping, and scaffold mapping.
- `pipeline-template.md`: canonical template for pipeline definitions and design lanes.
- `verification-template.md`: canonical template for verification lanes and evidence-backed closure checks.
- `rule-template.md`: canonical template for governance rules and policy surfaces.
- `skill-template.md`: canonical template for skill contracts and invocation boundaries.
- `evidence-pack-template.md`: canonical template for evidence bundles and governed execution packs.
- `decision-template.md`: canonical template for governance and architecture decisions.
- `remediation-template.md`: canonical template for bounded remediation plans.

## Operating Rules

- The universal core comes first; overlays may extend but must not weaken it.
- Template conformance is validated by `tools/governance/template_lint.py`.
- New governed artifacts may be scaffolded deterministically by `tools/governance/template_scaffold.py`.
- Template family definitions and overlays are loaded through `tools/governance/template_registry.py`.

## Overlay Model

- Stack overlays are defined in the registry and may add stack-aware expectations without weakening the universal core.
- Project overlays are repository-local extensions and must preserve required sections, frontmatter keys, and fail-closed semantics.

## Enforcement Model

The template system starts in advisory mode and can move toward enforcing mode only after verification lanes prove registry, linter, and scaffold behavior across representative fixtures.
