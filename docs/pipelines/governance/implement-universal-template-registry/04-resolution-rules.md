# Resolution Rules

## Implemented Precedence

1. exact `template_id`
2. exact `template_family + template_kind + stack + mode`
3. exact `template_family + template_kind + agnostic + mode` only when `allow_agnostic_fallback=true`
4. exact `template_family + tags + stack`
5. fail closed

## Implemented Fail-Closed Cases

- missing template identity
- ambiguous exact resolution
- ambiguous agnostic fallback
- ambiguous tag-based resolution
- restricted template without explicit allowance
- deprecated template without explicit allowance
- archived template selection
- missing admissible match
