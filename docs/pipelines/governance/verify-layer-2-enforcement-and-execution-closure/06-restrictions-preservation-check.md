# Restrictions Preservation Check

Layer 2 preserves inherited restrictions rather than silently broadening them:

- unsupported composition requests fail closed with explicit reason codes
- drift detection surfaces report invalid state rather than smoothing it over
- registry validation returns invalid state explicitly when integrity breaks
- execution does not rewrite Layer 0 or Layer 1 restrictions into broader
  success claims

Executed evidence:

- `doctor-composition` rejected `laravel + cli-worker` explicitly
- `verify-composition-matrix` remained valid without broadening support
- `list-manifests` and `list_templates` succeeded against the current admitted
  inventory
- the full governance suite passed:
  - `python -m unittest discover -s tests/governance -p 'test_*.py'`
  - `Ran 131 tests ... OK`

Remaining restrictions preserved by this lane:

- Layer 2 is distributed across canonical tools rather than unified behind one
  governance runner
- Layer 2 inherits Layer 0 and Layer 1 bounded restrictions
- this lane does not prove generic governance execution for domains outside the
  current implemented template-governance tooling
