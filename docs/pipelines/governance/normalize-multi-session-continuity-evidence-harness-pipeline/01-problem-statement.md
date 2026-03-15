# Problem Statement

Pipeline `137` completed with an evidence-backed restricted verification result.
That result exposed two governance-surface defects:

- the lane body expected `tools/governance/gov.py`, which does not exist in the
  repository
- the lane title stem collides with Pipeline `133`, making naive artifact-bundle
  naming collision-prone

These were documentation and routing defects, not continuity-harness defects.

Pipeline `138` normalizes the lane so future execution matches repository truth
without broadening the original verification boundary or rewriting the
historical restricted verdict recorded for Pipeline `137`.
