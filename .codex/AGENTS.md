# Codex Local Governance Surface

## Purpose

This file defines repository-local operating instructions for Codex agents working in this project.

## Operating Rules

- Follow repository governance artifacts before introducing new process.
- Prefer deterministic, file-backed pipeline execution over ad hoc changes.
- Record governance-relevant work in `docs/` so later agents can audit decisions.
- Preserve authority ordering defined in the repository constitution and architecture doctrine.
- Treat `docs/governance/architecture-doctrine.md` as the canonical interpretation layer for repository structure, authority, and pipeline artifact meaning.
- Use the doctrine foundation under `docs/governance/` as the canonical source for lifecycle, artifact, naming, contract-writing, and terminology rules.
- Use `docs/governance/governance-evidence-interpretation-canon.md` when deciding what evidence is sufficient to support a governance claim, verdict, restriction, or verification result.
- Use `docs/governance/governance-safety-invariants-canon.md` when deciding what governance mutation, summary, or normalization behavior must fail closed.
- Treat machine-local filesystem references such as `/home/...`, `/Users/...`, `C:\...`, `file://...`, and `~/...` as portability violations when they appear as live canonical links or repository navigation in governed surfaces.
- Use `docs/governance/layer-3-codex-rules-canon.md` as the canonical Codex operating layer for request classification, governed routing, safe mutation, verification posture, and bounded reporting.
- Use `docs/governance/layer-4-codex-role-model.md` when a task is framed in role-scoped Codex specialization terms, while preserving the single-agent bounded operating model unless a later lane verifies stronger orchestration.
- Use `docs/governance/layer-5-codex-collaboration-operating-model.md` when a task is framed in Codex collaboration, role handoff, restriction propagation, or bounded cross-role workflow terms, while preserving the doctrine-only operating model unless a later lane verifies stronger execution support.
- Use `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md` when a task is framed in session orchestration, session ownership, cross-session handoff discipline, or multi-session mutation control, while preserving the doctrine-only operating model unless a later lane verifies stronger execution support.
- Use `docs/governance/codex-session-registry.md` and `docs/governance/codex-session-ledger.md` when a task is framed in governed session identity, lifecycle-event recording, mutation-scope recording, or handoff traceability, while preserving documentation-level evidence boundaries unless a later lane verifies stronger execution support.
- Use `docs/contracts/codex-session-state-machine-canon.md` when a task is framed in governed session lifecycle states, allowed session transitions, invalid transition boundaries, or resumption semantics.
- Use `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` when a task is framed in predecessor-successor continuity, resume admissibility, restriction carry-forward, or fail-closed handoff evidence requirements.
- Use `docs/governance/codex-session-admission-and-activation-rules.md` when a task is framed in session admission, execution legitimacy, first-action validation, blocked activation, or fail-closed activation gating.
- Use `docs/governance/codex-session-runtime-boundary-and-evidence-model.md` when a task is framed in runtime session evidence, runtime-native session identifiers, runtime event compatibility, or the boundary between documentation governance and live session execution.
- Use `docs/governance/codex-session-lifecycle-observation-discipline.md` when a task is framed in lifecycle observation ordering, runtime lifecycle reconstruction, normalization of observed session transitions, or mapping observed lifecycle evidence into registry and ledger fields.
- Use `docs/governance/codex-session-evidence-interpretation-model.md` when a task is framed in session-truth reconstruction, evidence precedence across state machine / ledger / registry / observation surfaces, or conflict resolution between admissible session evidence sources.
- Use `docs/governance/codex-session-reconstruction-rules.md` when a task is framed in deterministic session reconstruction procedure, evidence-collection sequence, bounded timeline construction, or fail-closed reconstruction of a governed session narrative.
- Use `docs/governance/session-reconstruction-verification-harness.md` when a task is framed in verification of a reconstructed session narrative, deterministic narrative validation, evidence-anchoring checks, or classification of reconstruction outcomes as `VERIFIED`, `VERIFIED_WITH_RESTRICTIONS`, or `FAILED`.
- Use `docs/governance/session-reconstruction-case-verification-model.md` when a task is framed in structuring an individual session reconstruction case, declaring reconstruction scope and evidence sources, recording reconstruction assumptions, or preserving case restrictions for harness evaluation.
- Use `docs/governance/session-reconstruction-evidence-packaging-standard.md` when a task is framed in packaging reconstruction evidence, ordering packaged evidence sections, citing governed evidence surfaces, or preserving restrictions and assumptions in a formal evidence package.
- Use `docs/governance/multi-session-continuity-verification-model.md` when a task is framed in verifying continuity relationships across independently verified sessions, predecessor-successor linkage, cross-session governance artifact continuity, or bounded multi-session restriction handling.
- Use `docs/governance/multi-session-continuity-evidence-harness.md` when a task is framed in validating cross-session evidence types, applying minimum continuity evidence thresholds, classifying continuity evidence strength, or detecting boundary-violating continuity claims.
- Use `docs/governance/multi-session-continuity-evaluation-scenarios.md` when a task is framed in exercising the continuity stack through canonical verified, weak, none, or boundary-violation fixtures.
- Use `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` and `docs/codex/sessions/handoffs/` when a task is framed in inter-session continuity packets, handoff-close state capture, or next-session mutation boundaries, while preserving registry and ledger authority for session identity and event truth.
- Use `docs/contracts/codex-governance-surface-schema-contract.md` when normalizing or verifying session-governance field names, pipeline registry path recording, or related verification-lane schema expectations.
- Run `python tools/governance/preflight.py` before governed pipeline execution when you need the canonical repository preflight gate; it currently enforces the fail-closed portability reference scan across active governed surfaces.
- When closing or handing off a governed session that requires continuity evidence, produce the required handoff packet before treating the session as closed and preserve the packet reference or any continuity violation explicitly in the session registry and ledger.
- Do not claim resumed continuity unless the predecessor handoff packet, preserved restrictions, and first admissible successor action are explicit and evidence-backed.
- Do not treat an initialized or resumed session as active until admission conditions are satisfied and the first active action is admissible under current doctrine and scope.
- Use `docs/governance/governance-evolution-model.md` when changing governance doctrine, active pipeline structure, registry policy, or other meta-governance surfaces.
- Treat `docs/` as the authoritative root for all governance and Codex-related files in this repository.
- Use `docs/governance/templates/` and `tools/governance/` when authoring, validating, or scaffolding governed artifact families from the universal template system.
- Use `docs/governance/template-scaffold-contract.md` and `tools/templates/` when working on repository-level scaffold manifests or overlay discovery.
- Use `docs/contracts/universal-template-composition-contract.md` when changing or verifying certified overlay composition boundaries.
- Use `docs/governance/registries/templates/` and `docs/codex/templates/` when admitting, resolving, or auditing governed template identities.
- Treat `docs/bootstrap/` as the canonical adoption surface for future repositories inheriting this template's governance baseline.
- Use `docs/governance/universal-skills-index.md` and `docs/governance/skill-invocation-standard.md` to decide when universal or project-local skills apply.
- When following a normalized pipeline, prefer the pipeline's referenced universal skills for reusable operational behavior and keep pipeline-specific artifact and verdict requirements explicit.
- Treat `docs/contracts/pipeline-registry-integrity-contract.md` as the governing contract for registry completeness and active-pipeline discoverability.

## Repository Expectations

- Keep pipeline definitions under `docs/pipelines/`.
- Keep governance doctrine under `docs/governance/`.
- Keep canonical governance templates under `docs/governance/templates/`.
- Keep the universal scaffold contract under `docs/governance/template-scaffold-contract.md`.
- Keep the certified universal template composition contract under `docs/contracts/universal-template-composition-contract.md`.
- Keep admitted template registry metadata under `docs/governance/registries/templates/`.
- Keep admitted template bodies under `docs/codex/templates/`.
- Keep template manifest tooling under `tools/templates/`.
- Keep governed-project bootstrap guides under `docs/bootstrap/`.
- Keep universal reusable skills under `skills/`.
- Keep project-local skill extensions under `.codex/skills/`.
- Treat `docs/governance/contract-discovery-ledger.md` as the planning surface for future contract authoring and contract audit work.
- Register active pipelines in the pipeline registry.
- Treat verification and promotion outcomes as explicit deliverables.
