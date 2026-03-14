# Drift Boundary Checks

Drift boundary verification was recorded through
[`tests/governance/test_scheduler_generated_surface_conformance.py`](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_scheduler_generated_surface_conformance.py).

The checks confirm:

- changing the cron expression inside the protected region changes the extracted
  generated region and is therefore detectable as drift
- appending repository-local runtime integration after the generated region leaves
  the protected region unchanged
- the generated marker sequence is stable and ordered:
  - header
  - protected region start
  - protected region end
  - custom extension boundary

This establishes a governed distinction between:

- template-owned scheduler truth
- repository-owned extension logic
