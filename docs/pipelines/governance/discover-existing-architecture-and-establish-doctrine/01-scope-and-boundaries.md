# Scope And Boundaries

## In Scope

- repository structure relevant to architecture
- implementation evidence present in tracked files
- governance and contract documentation surfaces
- subsystem boundaries implied by the current documentation tree
- authority candidates for repository state and generated artifacts
- interface boundaries between constitution, doctrine, registry, pipeline definitions, and pipeline artifacts
- existing terminology used for governance lifecycle and authority
- descriptive architecture material already present in governance documents

## Out Of Scope

This pipeline does not:

- remediate code
- rewrite implementation beyond authoring the doctrine and supporting governance references
- verify production runtime behavior
- declare that architecture drift is permanently closed
- modernize legacy systems
- create subsystem contracts for absent application domains
- promote all existing documents to canonical authority automatically

## Discovery Boundary Decision

The discovery boundary is the repository itself as tracked in version control. Because no application code, runtime configuration, or operational infrastructure is present, architecture discovery is limited to governance surfaces and the relationships among them.
