# Universal Skills Compatibility

| archetype | compatible skills | partially compatible skills | incompatible skills | missing skills |
|-----------|-------------------|-----------------------------|---------------------|----------------|
| backend service | all current universal skills | none | none detected | none required for baseline |
| frontend application | repository-discovery, governance-readiness-audit, architecture-doctrine-authoring, contract-candidate-discovery, pipeline-registry-reconciliation, governed-project-bootstrap | canonical-contract-authoring, implementation-contract-audit, implementation-drift-remediation, contract-alignment-verification | none detected | optional UI-focused contract examples could help later |
| CLI tool | repository-discovery, governance-readiness-audit, architecture-doctrine-authoring, pipeline-registry-reconciliation, governed-project-bootstrap | contract-candidate-discovery, canonical-contract-authoring, implementation-contract-audit, implementation-drift-remediation, contract-alignment-verification | none detected | optional lightweight adoption examples |
| infrastructure automation | all current universal skills | none | none detected | none required for baseline |
| library or SDK | all current universal skills | none | none detected | none required for baseline |
| mixed monorepository | all current universal skills | none | none detected | optional future skill for multi-scope coordination |

## Findings

- The universal skill set stays generic because it is task-class oriented rather than language or runtime oriented.
- Discovery, audit, doctrine, registry, and bootstrap skills are broadly applicable even to small or non-service repositories.
- Contract-oriented skills are still meaningful outside backend systems, but they become optional until a repository has stable bounded surfaces worth formalizing.
- No skill currently encodes a telecom, SaaS, CI provider, framework, or language-ecosystem dependency.
