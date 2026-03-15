# Gap Integrity and Registry Cross-Reference Check

Explicit historical gaps re-verified:

- `docs/pipelines/governance/close-unsupported-framework-scheduler-composition-boundaries/`
  definition: `docs/pipelines/governance/062--close-unsupported-framework-scheduler-composition-boundaries.md`
  status: `registry_id` absent in governing definition
- `docs/pipelines/governance/establish-codex-session-lifecycle-observation-discipline/`
  definition: `docs/pipelines/governance/115--establish-codex-session-lifecycle-observation-discipline.md`
  status: `registry_id` absent in governing definition
- `docs/pipelines/governance/establish-codex-session-runtime-boundary-and-evidence-model/`
  definition: `docs/pipelines/governance/113--establish-codex-session-runtime-boundary-and-evidence-model.md`
  status: `registry_id` absent in governing definition
- `docs/pipelines/governance/migrate-core-governance-lanes-to-universal-templates/`
  definition: `docs/pipelines/governance/024--migrate-core-governance-lanes-to-universal-templates.md`
  status: `registry_id` absent in governing definition
- `docs/pipelines/governance/move-template-system-and-registry-under-docs-root-governance-tree/`
  definition: `docs/pipelines/governance/021--move-template-system-and-registry-under-docs-root-governance-tree.md`
  status: `registry_id` absent in governing definition
- `docs/pipelines/governance/verify-framework-scheduler-composition-boundaries-remain-non-drifting/`
  definition: `docs/pipelines/governance/063--verify-framework-scheduler-composition-boundaries-remain-non-drifting.md`
  status: `registry_id` absent in governing definition

Gap integrity result:

- explicit gap bundles still exist and remain inspectable: `PASS`
- every unresolved gap remains unresolved for the documented reason: `PASS`
- no unresolved gap was silently assigned an invented `registry_id`: `PASS`

Registry cross-reference result:

- `docs/pipelines/registry/pipeline-registry.md` still states that authoritative centralized execution history lives in `docs/governance/pipeline-run-ledger.md`
- Pipeline `142` is now registered with artifact bundle path `docs/pipelines/governance/verify-historical-pipeline-run-ledger-backfill-integrity/`

Governance preflight:

```text
governance_preflight
check: portability_reference_scan
decision: PASS
scope: active_governed_surfaces
scanned_files: 195
violations: 0
exceptions: 39
```
