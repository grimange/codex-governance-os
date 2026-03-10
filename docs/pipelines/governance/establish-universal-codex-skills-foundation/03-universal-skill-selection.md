# Universal Skill Selection

## Selection Strategy

The initial skill set is intentionally bounded to the strongest repeated governance workflows already visible in the template. Each selected skill maps to one or more existing or near-term governance pipelines.

## Selected Skills

- `repository-discovery`
  Purpose: discover repository structure, evidence surfaces, and authority candidates.
  Why universal: every governed repository needs structured discovery before doctrine, contract, or audit work.
  Why it belongs in the template: multiple pipelines already repeat this behavior.
  Expected users: Codex agents performing initialization, discovery, or audit work.
  Expected invocation contexts: architecture discovery, contract discovery, bootstrap analysis.

- `governance-readiness-audit`
  Purpose: audit whether repository governance surfaces are complete, consistent, and registered.
  Why universal: governance readiness checks apply across projects and stacks.
  Why it belongs in the template: pipeline `002` is a stable reusable pattern.
  Expected users: agents auditing governed repositories or template adopters.
  Expected invocation contexts: readiness reviews, governance maturity checks.

- `architecture-doctrine-authoring`
  Purpose: author or refine architecture doctrine from repository evidence.
  Why universal: every governed repository needs a consistent architecture interpretation layer.
  Why it belongs in the template: doctrine authoring is a core template workflow.
  Expected users: agents establishing or revising architecture doctrine.
  Expected invocation contexts: post-discovery doctrine installation, doctrine revision.

- `contract-candidate-discovery`
  Purpose: identify and rank canonical contract candidates and authority surfaces.
  Why universal: contract discovery is reusable across repositories even when the target subsystems differ.
  Why it belongs in the template: the repository already has a dedicated discovery pipeline and ledger.
  Expected users: agents preparing contract authoring work.
  Expected invocation contexts: governance inventories, contract-roadmap design.

- `canonical-contract-authoring`
  Purpose: author bounded canonical contracts that conform to the contract-writing standard.
  Why universal: repositories need consistent contract shape regardless of subsystem domain.
  Why it belongs in the template: pipeline `004` is one of the template's main reusable governance flows.
  Expected users: agents authoring contracts under `docs/contracts/`.
  Expected invocation contexts: selected subsystem contract creation, contract normalization.

- `implementation-contract-audit`
  Purpose: audit implementation or repository state against a canonical contract.
  Why universal: contract-versus-state audit logic is reusable across domains.
  Why it belongs in the template: pipeline `005` already defines this pattern.
  Expected users: agents performing compliance audits.
  Expected invocation contexts: post-contract audit, drift detection.

- `implementation-drift-remediation`
  Purpose: turn documented drift into a bounded remediation plan and execution path.
  Why universal: remediation design is a common governance task independent of domain.
  Why it belongs in the template: pipeline `006` depends on this logic.
  Expected users: agents resolving governance or implementation drift.
  Expected invocation contexts: post-audit remediation planning, change execution.

- `contract-alignment-verification`
  Purpose: verify that repository state now satisfies the governing contract after remediation.
  Why universal: verification is reusable wherever audit and remediation exist.
  Why it belongs in the template: pipeline `007` already provides the reusable structure.
  Expected users: agents closing remediation loops.
  Expected invocation contexts: post-remediation verification, promotion readiness checks.

- `pipeline-registry-reconciliation`
  Purpose: keep active governance pipelines and the registry aligned.
  Why universal: any governed repository with a pipeline registry needs this behavior.
  Why it belongs in the template: the registry-integrity contract already makes this operational.
  Expected users: agents activating or normalizing pipelines.
  Expected invocation contexts: pipeline addition, pipeline normalization, governance audits.

- `governed-project-bootstrap`
  Purpose: install or extend the baseline governed repository surface from the template.
  Why universal: governed adoption starts with a repeatable bootstrap path.
  Why it belongs in the template: initialization remains the entry point for future projects.
  Expected users: agents initializing new governed repositories.
  Expected invocation contexts: project adoption, baseline structure installation.

## Selection Conclusion

The initial ten-skill set is broad enough to cover the template's primary governance workflows while remaining bounded enough to keep each skill specific and reusable.
