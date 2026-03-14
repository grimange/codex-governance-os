# Verification Scope

Pipeline `127` verifies the governance integrity of the session reconstruction
case verification model introduced by Pipeline `126`.

The verification scope includes:

- `docs/governance/session-reconstruction-case-verification-model.md`
- `docs/governance/session-reconstruction-verification-harness.md`
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
- `docs/governance/architecture-doctrine.md`
- `.codex/AGENTS.md`
- `README.md`
- `docs/pipelines/registry/pipeline-registry.md`
- `docs/pipelines/governance/establish-session-reconstruction-case-verification-model/`

Verification criteria:

1. each reconstruction case remains anchored on exactly one canonical
   `session_id`
2. the case model remains subordinate to the session reconstruction
   verification harness
3. explicit evidence citation remains mandatory
4. reconstruction assumptions remain explicit and inspectable
5. the required evaluation dimensions remain present and bounded
6. the case model introduces no new outcome types, runtime behavior, or
   governance mutation authority
7. the canon is discoverable from the required repository entry surfaces
8. Pipeline `126` is recorded correctly in the pipeline registry
