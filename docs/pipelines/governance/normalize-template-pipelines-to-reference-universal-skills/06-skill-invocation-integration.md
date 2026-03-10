# Skill Invocation Integration

## Validity Check

- Every referenced skill exists under `skills/`.
- Skill references use canonical folder identity rather than ad hoc naming.
- No normalized pipeline references a project-local skill directly.

## Conflict Check

- No normalized pipeline invokes conflicting skills for the same task class.
- Where two skills are named in one pipeline, the boundary is explicit, for example discovery plus registry reconciliation or candidate discovery plus contract authoring.

## Clarity Check

- Invocation context is explicit near the top of each normalized pipeline.
- Phase-level references preserve artifact requirements and do not remove pipeline-specific outputs or verdict logic.

## Integration Conclusion

Skill invocation remains explicit and unambiguous after normalization.
