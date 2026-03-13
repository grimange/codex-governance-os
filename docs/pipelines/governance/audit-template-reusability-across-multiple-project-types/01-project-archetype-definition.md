# Project Archetype Definition

## Backend Service Repository

- Expected structure: application code plus service configuration, operational docs, and subsystem boundaries.
- Governance needs: architecture doctrine, contracts for service boundaries, audit and remediation workflows, promotion discipline.
- Typical lifecycle: initialization, discovery, contract authoring, implementation audit, remediation, verification, promotion.
- Typical pipeline usage: broad use of pipelines `000` through `007`.

## Frontend Application Repository

- Expected structure: UI application code, asset pipeline, build tooling, optional component libraries, limited backend assumptions.
- Governance needs: architecture doctrine, governance readiness, selected contracts for build, state, or component boundaries.
- Typical lifecycle: bootstrap, architecture discovery, optional contract authoring, selective audits and verification.
- Typical pipeline usage: `000`, `001`, `002` always useful; `003` through `007` useful when stable subsystem contracts matter.

## CLI Tool Repository

- Expected structure: command entrypoints, packaging metadata, tests, lightweight docs, often small team ownership.
- Governance needs: lightweight doctrine, compact pipelines, optional contracts for CLI behavior or packaging boundaries.
- Typical lifecycle: bootstrap, discovery, readiness audit, selective contract work if the tool grows.
- Typical pipeline usage: `000`, `001`, and `002` universal; later pipelines conditional on repository scale.

## Infrastructure Automation Repository

- Expected structure: Terraform, Ansible, Kubernetes, or automation modules with environment or policy overlays.
- Governance needs: strong doctrine, clear source-of-truth rules, contracts for environment or policy boundaries, drift remediation.
- Typical lifecycle: bootstrap, discovery, contract discovery, contract authoring, audit, remediation, verification.
- Typical pipeline usage: strong fit for `000` through `007`.

## Library Or SDK Repository

- Expected structure: package source, API surface, examples, tests, release metadata, possibly multiple language bindings.
- Governance needs: doctrine, API or packaging contracts, verification emphasis, moderate remediation needs.
- Typical lifecycle: bootstrap, discovery, selective contract work, implementation audit where public API guarantees matter.
- Typical pipeline usage: `000`, `001`, `002` always useful; `003` through `007` apply once API or packaging contracts are formalized.

## Mixed Monorepository

- Expected structure: multiple packages, services, tools, or infrastructure roots with varied language ecosystems.
- Governance needs: clear doctrine, strong registry discipline, multiple contracts, local skill extensions, scalable pipeline usage.
- Typical lifecycle: full governance lifecycle across multiple bounded subsystems.
- Typical pipeline usage: full applicability of `000` through `007`, often repeated across local scopes.
