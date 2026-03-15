# Current Pipeline History Surface

Repository execution history before Pipeline `139` was distributed across:

- `docs/pipelines/registry/pipeline-registry.md`
- canonical artifact bundle directories under `docs/pipelines/governance/`
- individual pipeline definition files
- final verdict artifacts inside pipeline bundles

Observed gaps before ledger establishment:

- the pipeline registry records active lanes but not centralized execution
  history
- artifact bundles preserve execution evidence, but do not provide one global
  chronological run list
- answering "what was the last pipeline run?" required repository inspection
  rather than a single authoritative history surface

Recent repository-truth runs available for bounded backfill:

- Pipeline `137`
- Pipeline `138`
- Pipeline `139`
