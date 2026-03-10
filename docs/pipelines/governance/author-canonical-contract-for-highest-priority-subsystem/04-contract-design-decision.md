# Contract Design Decision

## Purpose

Codify active-pipeline registration discipline so the registry becomes a reliable discoverability and audit surface.

## Required Rules

- every active pipeline must appear exactly once in the registry
- registry entries must resolve to real pipeline files
- registry IDs and paths must match pipeline identity
- registry updates must accompany operational activation

## Prohibited Behaviors

- operating active pipelines without registry representation
- registering placeholders as active pipelines
- using the registry to redefine substantive pipeline procedure

## Compliance Expectations

- audits should be able to determine active governance coverage from the registry
- future governance changes should update the registry in the same governed change set that activates a pipeline
- ledger and doctrine consumers should be able to rely on the registry as a bounded discoverability surface

## Relationship To Existing Authorities

- the constitution establishes that active pipelines must be registered
- the doctrine establishes that the registry is a projection surface, not the highest authority
- this contract operationalizes those principles for the registry subsystem specifically
