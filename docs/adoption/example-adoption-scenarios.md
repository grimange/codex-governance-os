# Example Adoption Scenarios

## Backend Service Repository

- Start with pipelines `000`, `001`, and `002`.
- Continue into `003` through `007` once service boundaries, state ownership, or external interfaces need explicit contracts.

## CLI Tool Repository

- Adopt the governance baseline and establish local doctrine.
- Stop after `002` unless the tool grows enough to justify explicit contract governance.

## Frontend Application Repository

- Use bootstrap and architecture discovery first.
- Introduce contracts later for component systems, state boundaries, or build governance only if they become important.

## Infrastructure Automation Repository

- Adopt the full baseline early because source-of-truth, environment boundaries, and drift handling usually matter quickly.
- Contract and remediation pipelines often become relevant sooner than in small application repositories.

## Library Or SDK Repository

- Start with bootstrap, doctrine, and readiness.
- Introduce contract governance when public API, compatibility, or packaging guarantees need explicit canonical rules.

These examples demonstrate that the same framework can be adopted proportionally across multiple repository types.
