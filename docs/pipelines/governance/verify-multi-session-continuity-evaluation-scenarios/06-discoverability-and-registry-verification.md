# Discoverability And Registry Verification

The lane body references non-canonical repository paths under
`docs/governance/canon/` and `docs/governance/layers/`.

For repository execution, those references were normalized to the canonical
discoverability surfaces:

- `docs/governance/multi-session-continuity-evidence-harness.md`
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
- `.codex/AGENTS.md`
- `README.md`
- `docs/pipelines/registry/pipeline-registry.md`

Verified discoverability:

- `docs/governance/multi-session-continuity-evidence-harness.md` references
  `docs/governance/multi-session-continuity-evaluation-scenarios.md`
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
  lists the continuity evaluation scenario canon
- `.codex/AGENTS.md` routes scenario-fixture work to the new canon
- `README.md` includes the continuity evaluation scenario canon in the
  repository governance index
- pipeline `134` is registered in
  `docs/pipelines/registry/pipeline-registry.md`
- pipeline `135` is now registered in
  `docs/pipelines/registry/pipeline-registry.md`

Verification command:

```text
python tools/governance/preflight.py
```

Observed result:

- `decision: PASS`
- `violations: 0`

Finding: discoverability and registry integration are complete on canonical
repository surfaces.
