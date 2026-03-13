# Problem Statement

The repository had a basic family-structure validator from pipeline `018`, but it did not yet provide:

- canonical lint rule identifiers
- template-class classification without mandatory caller hints
- portability leakage detection for universal templates
- approved safe normalization reporting
- governed admission decisions
- stable JSON and text output suitable for future automation
- repo-wide template lint execution

Pipeline `020` closes that gap by turning template linting into a governed admission primitive rather than a narrow helper.
