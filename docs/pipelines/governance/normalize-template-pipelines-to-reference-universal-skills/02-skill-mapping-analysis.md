# Skill Mapping Analysis

## Applied Mappings

- `000--initialize-governed-project.md`
  Mapped behaviors: bootstrap installation, discovery, registry integration.
  Skills referenced: `governed-project-bootstrap`, `repository-discovery`, `pipeline-registry-reconciliation`.
- `001--discover-existing-architecture-and-establish-doctrine.md`
  Mapped behaviors: evidence discovery, architecture mapping, doctrine design and authoring.
  Skills referenced: `repository-discovery`, `architecture-doctrine-authoring`.
- `002--audit-repository-governance-readiness.md`
  Mapped behaviors: readiness audit and registry integrity checks.
  Skills referenced: `governance-readiness-audit`, `pipeline-registry-reconciliation`.
- `003--discover-contract-candidates-and-authority-surfaces.md`
  Mapped behaviors: surface inventory, subsystem discovery, candidate matrix, recommendations.
  Skills referenced: `repository-discovery`, `contract-candidate-discovery`.
- `004--author-canonical-contract-for-highest-priority-subsystem.md`
  Mapped behaviors: candidate recheck and contract authoring.
  Skills referenced: `contract-candidate-discovery`, `canonical-contract-authoring`.
- `005--audit-implementation-against-canonical-contract.md`
  Mapped behaviors: audit extraction, implementation discovery, compliance matrix, drift assessment.
  Skills referenced: `implementation-contract-audit`.
- `006--remediate-implementation-drift-against-contract.md`
  Mapped behaviors: remediation planning and execution.
  Skills referenced: `implementation-drift-remediation`.
- `007--verify-contract-alignment.md`
  Mapped behaviors: verification extraction, reinspection, behavioral verification, matrix update.
  Skills referenced: `contract-alignment-verification`.

## Gaps Not Yet Mapped

- Pipeline `008` still contains reusable doctrine-foundation behavior that is not covered by a dedicated universal skill.
- Pipeline `009` still contains reusable skill-foundation behavior that is intentionally pipeline-specific until a later governance decision creates higher-order meta-skills.

## Invocation Format Decision

Pipelines now reference skills by canonical folder identity using the model defined in `docs/governance/skill-invocation-standard.md`, for example `repository-discovery` or `implementation-contract-audit`.
