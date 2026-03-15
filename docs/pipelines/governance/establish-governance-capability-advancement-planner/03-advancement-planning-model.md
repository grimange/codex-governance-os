# Advancement Planning Model

Pipeline 156 uses the following deterministic planning model:

1. Extract capability gaps from any capability whose coverage state is not
   `fully implemented`.
2. Preserve the evidence boundary for each gap from the canonical gap analysis.
3. Identify the primary blocker preventing the capability from advancing.
4. Assign one recommended pipeline class that best fits the missing capability
   shape.
5. Order advancement targets by maturity leverage and safety, not aspiration.

Planning classes used in this pipeline:

- analytics pipelines
- orchestration pipelines
- autonomous governance pipelines

Priority interpretation:

- `high`
  - directly improves governance intelligence or removes a major maturity bound
- `medium`
  - materially improves capability coverage but depends on stable upstream
    intelligence or verification conditions
