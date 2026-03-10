# Universal Skill Taxonomy Design

## Taxonomy Principles

- Skills must be grouped by reusable governance function, not by one repository's business domain.
- A skill class is universal only if it can operate across future repositories without assuming product-specific runtime architecture.
- Pipeline-specific one-off logic should remain in pipelines unless it repeats broadly enough to justify a skill.

## Discovery Skills

- Purpose: gather repository evidence, structure, and authority surfaces.
- Tasks that belong: repository discovery, subsystem boundary discovery, evidence inventories.
- Outside the class: product-domain investigation techniques that depend on a specific stack.
- Universal status: universal.

## Audit Skills

- Purpose: compare repository state against doctrines, contracts, or other authority surfaces.
- Tasks that belong: governance readiness audits, implementation-versus-contract audits.
- Outside the class: runtime production incident response or domain-specific compliance checks.
- Universal status: universal.

## Doctrine-Authoring Skills

- Purpose: author canonical doctrine surfaces from repository evidence and governance rules.
- Tasks that belong: architecture doctrine authoring, governance surface refinement, doctrine normalization.
- Outside the class: business-policy writing unrelated to repository governance.
- Universal status: universal.

## Contract-Authoring Skills

- Purpose: discover contract candidates and author bounded canonical contracts.
- Tasks that belong: contract candidate discovery, canonical contract authoring.
- Outside the class: project-private legal agreements or domain-specific business contracts.
- Universal status: universal when scoped to repository governance and subsystem contracts.

## Remediation-Design Skills

- Purpose: convert drift findings into governed remediation plans and implementation sequences.
- Tasks that belong: remediation strategy design, impact analysis, bounded change planning.
- Outside the class: domain-specific operational playbooks.
- Universal status: universal.

## Verification Skills

- Purpose: confirm that changed repository state now conforms to the governing authority.
- Tasks that belong: contract alignment verification, doctrine installation verification.
- Outside the class: product-specific acceptance testing frameworks.
- Universal status: universal.

## Registry And Catalog Skills

- Purpose: maintain deterministic governance discoverability across pipeline and skill catalogs.
- Tasks that belong: pipeline registry reconciliation, catalog hygiene checks.
- Outside the class: arbitrary inventory reporting that is not governance-related.
- Universal status: universal.

## Template/Bootstrap Skills

- Purpose: initialize or extend governed project structure from the template baseline.
- Tasks that belong: governed project bootstrap, initial governance-surface installation.
- Outside the class: project-specific onboarding or business-logic scaffolding.
- Universal status: universal.

## Governance Hygiene Skills

- Purpose: keep naming, routing, and doctrinal surfaces aligned over time.
- Tasks that belong: normalization planning, stale-guidance detection, governance-surface cleanup.
- Outside the class: broad repository refactoring that is not primarily governance-driven.
- Universal status: partly universal, but initial pipeline `009` does not need a separate first-class skill here because the current selected set already covers the main reusable paths.
