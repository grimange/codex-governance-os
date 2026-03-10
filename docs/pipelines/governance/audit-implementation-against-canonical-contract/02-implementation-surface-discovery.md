# Implementation Surface Discovery

The repository implements this subsystem as a documentation-first governance surface rather than runtime code.

| Path | Responsibility | Relationship To Subsystem | Authority Classification |
|------|----------------|---------------------------|--------------------------|
| `AGENTS.md` | constitutional rule that active pipelines must be registered | higher-order authority constraining registry behavior | authoritative upstream |
| `.codex/AGENTS.md` | repository-local operating rule to register active pipelines and treat the contract as governing interpretation | operational instruction surface reinforcing contract behavior | authoritative local operating surface |
| `docs/governance/architecture-doctrine.md` | doctrine for source-of-truth, registry role, and artifact interpretation | higher-order interpretation of registry as discoverability surface | authoritative upstream |
| `docs/contracts/pipeline-registry-integrity-contract.md` | canonical registry-integrity rules | direct contract under audit | canonical subsystem authority |
| `docs/pipelines/registry/pipeline-registry.md` | durable registry state for active pipelines | primary implementation surface for activation/discoverability | canonical state surface |
| `docs/pipelines/governance/000--initialize-governed-project.md` | active pipeline definition and registered reference target | implementation instance governed by the contract | authoritative referenced definition |
| `docs/pipelines/governance/001--discover-existing-architecture-and-establish-doctrine.md` | active pipeline definition and registered reference target | implementation instance governed by the contract | authoritative referenced definition |
| `docs/pipelines/governance/002--audit-repository-governance-readiness.md` | active pipeline definition and registered reference target | implementation instance governed by the contract | authoritative referenced definition |
| `docs/pipelines/governance/003--discover-contract-candidates-and-authority-surfaces.md` | active pipeline definition and registered reference target | implementation instance governed by the contract | authoritative referenced definition |
| `docs/pipelines/governance/004--author-canonical-contract-for-highest-priority-subsystem.md` | active pipeline definition and registered reference target | implementation instance governed by the contract | authoritative referenced definition |
| `docs/pipelines/governance/005--audit-implementation-against-canonical-contract.md` | currently executed audit workflow | directly tests whether operational activation is reflected in the registry | active but unregistered implementation surface |
| `docs/pipelines/governance/006--remediate-implementation-drift-against-contract.md` | future remediation workflow definition | adjacent lifecycle surface that may later become active | defined, operational status unverified |
| `docs/pipelines/governance/007--verify-contract-alignment.md` | future verification workflow definition | adjacent lifecycle surface that may later become active | defined, operational status unverified |
| `docs/governance/contract-discovery-ledger.md` | planning surface that recommends auditing this contract | supporting evidence, not authoritative for activation state | planning / derived |
| `docs/pipelines/governance/author-canonical-contract-for-highest-priority-subsystem/*.md` | evidence that the contract was authored and registry updates previously occurred | supporting audit evidence for expected implementation behavior | generated evidence |

## Discovery Notes

- No application services, controllers, data stores, or event buses exist in repository evidence for this subsystem.
- The relevant implementation surface is therefore the governance document set itself.
- Current operational evidence clearly establishes `005` as active because this audit is being executed from that pipeline definition.
