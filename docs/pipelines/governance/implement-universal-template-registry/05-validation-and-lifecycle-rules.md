# Validation And Lifecycle Rules

## Admission Validation

Implemented validation checks include:

- required metadata presence
- unique `template_id`
- valid family, kind, status, authority, stack, and mode enumerations
- existing body file
- checksum match
- body lint success
- duplicate active resolution key rejection
- supersession sanity checks

## Lifecycle Enforcement

- `draft`: not eligible for governed execution
- `active`: eligible for normal resolution
- `deprecated`: blocked unless explicit allowance is provided
- `restricted`: blocked unless explicit allowance is provided
- `archived`: always blocked for selection
