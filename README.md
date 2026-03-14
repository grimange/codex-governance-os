# Codex Governance Template

This repository is a documentation-first template for turning a standard repository into a governed Codex project.

The `docs/` directory is the authoritative root for all governance and Codex-related files in this repository.

## Start Here

- Quick start: `docs/adoption/quick-start.md`
- Full adoption guide: `docs/adoption/codex-governance-adoption-guide.md`
- Framework overview: `docs/adoption/framework-overview.md`
- Adoption guide: `docs/bootstrap/governed-project-bootstrap.md`
- Minimal setup checklist: `docs/bootstrap/minimal-setup-checklist.md`
- Skill inheritance model: `docs/bootstrap/skill-inheritance-model.md`
- Local override model: `docs/bootstrap/local-override-model.md`
- Active governance pipelines: `docs/pipelines/registry/pipeline-registry.md`

## What This Template Provides

- a repository constitution model in `AGENTS.md`
- repository-local Codex operating rules in `.codex/AGENTS.md`
- reusable governance doctrine under `docs/governance/`
- reusable governance pipelines under `docs/pipelines/governance/`
- reusable universal skills and a local override model
- publication-oriented adoption guides under `docs/adoption/`

## Adoption Profiles

- Small repository: start with bootstrap guidance, run pipelines `000`, `001`, and `002`, then add later contract-oriented pipelines only when the repository has stable bounded surfaces worth governing explicitly.
- Growing application or library: use `000` through `002` as the baseline, then use `003` through `007` once subsystem contracts, audits, remediation, and verification become operationally useful.
- Monorepository or multi-scope system: keep the same baseline, then apply later pipelines per bounded subsystem or local scope as complexity grows.

## Scope

This template is intended to remain domain-neutral, architecture-neutral, and language-neutral. It does not prescribe a single runtime model, framework, CI provider, or distribution pattern.

## Learn More

- Example adoption scenarios: `docs/adoption/example-adoption-scenarios.md`
- Governance lifecycle doctrine: `docs/governance/governance-lifecycle.md`
- Governance evidence interpretation canon: `docs/governance/governance-evidence-interpretation-canon.md`
- Governance safety invariants canon: `docs/governance/governance-safety-invariants-canon.md`
- Repository portability link invariant: canonical governance and repository-entry references must avoid machine-local filesystem paths and use portable relative paths or explicit external URLs instead.
- Governance preflight command: run `python tools/governance/preflight.py` to execute the active fail-closed portability reference scan before governed execution.
- Layer 3 Codex rules canon: `docs/governance/layer-3-codex-rules-canon.md`
- Layer 4 Codex role model: `docs/governance/layer-4-codex-role-model.md`
- Layer 5 Codex collaboration operating model: `docs/governance/layer-5-codex-collaboration-operating-model.md`
- Layer 6 Codex session orchestration and handoff discipline: `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
- Codex session registry: `docs/governance/codex-session-registry.md`
- Codex session execution ledger: `docs/governance/codex-session-ledger.md`
- Codex session handoff and resume evidence model: `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md`
- Codex session admission and activation rules: `docs/governance/codex-session-admission-and-activation-rules.md`
- Codex session runtime boundary and evidence model: `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
- Codex session lifecycle observation discipline: `docs/governance/codex-session-lifecycle-observation-discipline.md`
- Codex session evidence interpretation model: `docs/governance/codex-session-evidence-interpretation-model.md`
- Codex session reconstruction rules: `docs/governance/codex-session-reconstruction-rules.md`
- Session reconstruction verification harness: `docs/governance/session-reconstruction-verification-harness.md`
- Session reconstruction case verification model: `docs/governance/session-reconstruction-case-verification-model.md`
- Session reconstruction evidence packaging standard: `docs/governance/session-reconstruction-evidence-packaging-standard.md`
- Codex session state machine canon: `docs/contracts/codex-session-state-machine-canon.md`
- Codex session handoff packet contract: `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md`
- Codex governance surface schema contract: `docs/contracts/codex-governance-surface-schema-contract.md`
- Codex session handoff packet root: `docs/codex/sessions/handoffs/`
- Governed session lifecycle state semantics: Layer 6 session-governance surfaces should use the canonical states and transitions defined in `docs/contracts/codex-session-state-machine-canon.md`.
- Governed session resume claims must remain evidence-backed through explicit predecessor linkage, preserved restrictions, and fail-closed admissibility rules defined in `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md`.
- Governed session execution must pass admission before activation, with the first active action remaining bounded, evidence-backed, and fail-closed under `docs/governance/codex-session-admission-and-activation-rules.md`.
- Governed session closure discipline: required handoff packets must be created before closure when continuity evidence is required, with resulting packet references or continuity violations remaining visible in session-governance records.
- Governance evolution model: `docs/governance/governance-evolution-model.md`
- Governance template system: `docs/governance/templates/README.md`
- Template scaffold contract: `docs/governance/template-scaffold-contract.md`
- Universal template composition contract: `docs/contracts/universal-template-composition-contract.md`
- Admitted template registry index: `docs/governance/registries/templates/index.yaml`
- Admitted template bodies: `docs/codex/templates/`
- Universal skills index: `docs/governance/universal-skills-index.md`
