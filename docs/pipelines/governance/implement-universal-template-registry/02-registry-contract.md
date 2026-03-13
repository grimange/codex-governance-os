# Registry Contract

## Implemented Entry Model

Each admitted template entry now records:

- `template_id`
- `template_name`
- `template_family`
- `template_kind`
- `version`
- `status`
- `authority_level`
- `description`
- `inputs_contract`
- `outputs_contract`
- `compatible_stacks`
- `compatible_modes`
- `constraints`
- `resolution_tags`
- `file_path`
- `checksum_sha256`
- `admitted_at`
- `admitted_by`
- `supersedes`

## Implemented Safety Contract

- a template body without an admitted registry entry is not authoritative
- checksum mismatch blocks admission
- invalid lifecycle or authority metadata blocks admission
- duplicate active resolution keys block admission
- missing files or lint failures block admission
