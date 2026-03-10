# Universal Skill Authoring

## Created Skill Set

- `skills/discovery/repository-discovery/`
- `skills/audit/governance-readiness-audit/`
- `skills/doctrine/architecture-doctrine-authoring/`
- `skills/contracts/contract-candidate-discovery/`
- `skills/contracts/canonical-contract-authoring/`
- `skills/audit/implementation-contract-audit/`
- `skills/remediation/implementation-drift-remediation/`
- `skills/verification/contract-alignment-verification/`
- `skills/governance/pipeline-registry-reconciliation/`
- `skills/bootstrap/governed-project-bootstrap/`

## Authoring Notes

- Each skill package uses a `SKILL.md` file with required `name` and `description` metadata.
- Each skill follows the governed section model defined by `docs/governance/skill-authoring-standard.md`.
- The initial set is generic and aligned to the existing governance pipeline catalog rather than to any domain-specific runtime stack.

## Packaging Decision

- No extra scripts, references, or assets were required for the first pass because the workflows are primarily procedural and documentation-oriented.
- The package structure leaves room for later deterministic helpers or reference bundles if later normalization work justifies them.
