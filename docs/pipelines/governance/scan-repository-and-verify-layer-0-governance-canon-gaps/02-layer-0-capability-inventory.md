# Layer 0 Capability Inventory

## Governance Canon Vocabulary

- status: `ESTABLISHED`
- observed surfaces:
  - [governance-terminology.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-terminology.md)
  - [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md)
- explicitness:
  - explicit terminology doctrine exists
  - reused by higher-order doctrine and constitution

## Governance Authority Hierarchy

- status: `ESTABLISHED`
- observed surfaces:
  - [AGENTS.md](/home/ramjf/python-projects/codex-governance-os/AGENTS.md)
  - [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md)
  - [pipeline-registry-integrity-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/pipeline-registry-integrity-contract.md)
- explicitness:
  - authority precedence is stated directly and repeated consistently

## Governance Evidence Model

- status: `PARTIAL`
- observed surfaces:
  - [governance-terminology.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-terminology.md)
  - [pipeline-artifact-standard.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/pipeline-artifact-standard.md)
  - [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md)
  - [contract-discovery-ledger.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/contract-discovery-ledger.md)
  - [test_template_composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_contract.py)
- explicitness:
  - evidence is defined and artifact expectations exist
  - interpretation rules are still distributed rather than centralized as one Layer 0 evidence canon

## Governance Safety Invariants

- status: `PARTIAL`
- observed surfaces:
  - [AGENTS.md](/home/ramjf/python-projects/codex-governance-os/AGENTS.md)
  - [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md)
  - [governance-evolution-model.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-evolution-model.md)
  - [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
- explicitness:
  - fail-closed and no-silent-mutation rules exist in subsystem-specific and meta-governance surfaces
  - no single Layer 0 safety doctrine centralizes the invariant set repository-wide

## Governance Normalization Boundary Model

- status: `IMPLICIT_ONLY`
- observed surfaces:
  - [template_registry.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_registry.py)
  - [template_lint.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_lint.py)
  - [template-registry.yaml](/home/ramjf/python-projects/codex-governance-os/docs/governance/templates/template-registry.yaml)
- explicitness:
  - normalization aliases and safe normalization behavior exist in code and template metadata
  - no canonical Layer 0 doctrine explains what may be normalized automatically and what must block

## Governance Truth-Source Precedence

- status: `ESTABLISHED`
- observed surfaces:
  - [AGENTS.md](/home/ramjf/python-projects/codex-governance-os/AGENTS.md)
  - [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md)
  - [governance-terminology.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-terminology.md)
- explicitness:
  - repository state, constitution, doctrine, pipeline definitions, and artifacts are precedence-ordered directly

## Governance Lifecycle / State Canon

- status: `ESTABLISHED`
- observed surfaces:
  - [governance-lifecycle.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-lifecycle.md)
  - [governance-evolution-model.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-evolution-model.md)
- explicitness:
  - lifecycle stages and mutation classes are explicit and reusable

## Governed Claim Classification Model

- status: `PARTIAL`
- observed surfaces:
  - [governance-terminology.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/governance-terminology.md)
  - [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
  - [template-scaffold-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/template-scaffold-contract.md)
  - [contract-discovery-ledger.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/contract-discovery-ledger.md)
  - [tests/governance](/home/ramjf/python-projects/codex-governance-os/tests/governance)
- explicitness:
  - terms like `supported`, `unsupported`, `blocked`, `advisory`, `verified`, and `restricted` are materially used
  - no single canonical Layer 0 doctrine defines the full claim taxonomy and cross-surface semantics
