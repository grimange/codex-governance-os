# Template Registry Design

## Control Surface

- canonical path: `docs/governance/templates/template-registry.yaml`
- file format: JSON-compatible YAML for deterministic stdlib parsing

## Registry Contents

- schema version
- universal governance and execution modes
- universal core requirements
- overlay definitions
- template family definitions

## Validation Responsibilities

The registry loader rejects:

- malformed registry syntax
- duplicate template families
- duplicate overlay names
- alias collisions
- references to unknown overlays
- overlays that declare weakening behavior
