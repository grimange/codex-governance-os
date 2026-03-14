# Codex Governance Surface Schema Contract

## Purpose

This contract defines the canonical field-naming and path-recording discipline
for Codex session-governance surfaces and related verification lanes in
`codex-governance-os`.

It exists so session-governance documentation, verification lanes, and registry
surfaces operate against one stable schema rather than drifting into
near-duplicate field names or inconsistent path assumptions.

## Scope

This contract governs:

- canonical session field names used in session-governance surfaces
- canonical path field names used in pipeline registry entries and related
  verification lanes
- field-name normalization expectations for future Codex session verification
  work

This contract does not govern:

- runtime data storage implementation
- product-domain schemas
- pipeline-internal substantive procedure beyond schema naming discipline

## Governing Authority

Authority for this contract is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/governance/codex-session-registry.md`
6. `docs/governance/codex-session-ledger.md`
7. `docs/contracts/pipeline-registry-integrity-contract.md`
8. this contract
9. generated pipeline artifacts and verification bundles

## Canonical Rules

1. Session lifecycle timestamps must use `start_date` and `closure_date`.
2. Verification lanes must not use deprecated aliases such as `session_start`
   or `session_end` when referring to the canonical session schema.
3. Session identity fields must use `session_id`.
4. Pipeline identity fields must use `registry_id` when the canonical pipeline
   identifier is intended.
5. Pipeline registry entries must record both `pipeline_definition_path` and
   `artifact_bundle_path`.
6. Verification lanes that inspect registry state must align their expectations
   with the canonical registry field names rather than inventing ad hoc
   alternatives.
7. Artifact bundle paths must point to the canonical pipeline artifact
   directory, normally `docs/pipelines/<category>/<pipeline-slug>/`.

## Canonical Field Set

The canonical Codex session-governance field set includes:

- `session_id`
- `start_date`
- `closure_date`
- `registry_id`
- `pipeline_definition_path`
- `artifact_bundle_path`

Additional bounded fields may exist in specific surfaces, but these core names
must not be drifted through synonymous aliases.

## Allowed Behaviors

- using the canonical field names in doctrine, contracts, registry surfaces,
  and verification lanes
- normalizing older lane definitions to canonical names
- recording compatibility notes for older historical artifacts without
  rewriting them

## Prohibited Behaviors

- introducing new alias field names for the same canonical meaning without
  governed normalization
- treating deprecated names as equal peers to canonical field names
- requiring verification lanes to infer artifact-bundle paths when the registry
  already records them canonically

## Compliance Signals

Compliance is indicated when:

- session-governance surfaces use `start_date` and `closure_date`
- registry entries expose both definition and artifact-bundle paths
- verification lanes inspect canonical field names directly
- historical drift is either normalized or explicitly recorded

## Ambiguity Handling

- If an older artifact uses deprecated field names, that artifact may remain as
  historical evidence, but new authoritative lane definitions should use the
  canonical names.
- If a registry entry predates artifact-bundle path recording, it should be
  normalized rather than left as a silent exception.

## Governance Implications

- Future verification lanes can use this contract as the canonical schema
  target for session-governance and registry checks.
- Future normalization and remediation lanes can distinguish real behavior drift
  from field-name or path-schema drift more precisely.

## Non-Goals

This contract does not:

- create runtime storage or validation code
- replace the session registry or execution ledger
- authorize incompatible product-domain schema changes
