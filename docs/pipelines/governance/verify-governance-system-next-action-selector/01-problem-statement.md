# Problem Statement

Pipeline 172 established the governance system next-action selector, which is
supposed to resolve the roadmap's `recommended_next_target` into one governed
action.

Pipeline 173 verifies that this selector is deterministic, roadmap-aligned,
evidence-scoped, and fail-closed when the roadmap cannot resolve a valid target.
