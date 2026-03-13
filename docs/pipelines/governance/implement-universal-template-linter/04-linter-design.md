# Linter Design

## Implemented Surface

- canonical implementation: `tools/governance/template_lint.py`
- supporting integration: `tools/governance/template_registry.py` now uses the governed lint decision for template admission

## Implemented Capabilities

- frontmatter parsing
- template-class classification
- required-section and ordering validation
- title and identifier validation
- overlay compatibility checks
- unresolved placeholder detection
- universal portability leakage detection
- contradictory status semantics detection
- safe normalization reporting for line endings, trailing whitespace, and derivable top headings
- deterministic text and JSON outputs
- single-template and repo-wide lint CLI commands

## Decision Model

- `VALID_AS_IS`
- `NORMALIZED_AND_VALID`
- `BLOCKED`
