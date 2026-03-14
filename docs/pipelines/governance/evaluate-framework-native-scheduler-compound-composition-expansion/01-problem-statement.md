# Problem Statement

Direct framework-native scheduler pairs are now established and verified:

- `laravel + scheduler`
- `django + scheduler`

Compound framework-native scheduler combinations remain closed:

- `laravel + monorepo + scheduler`
- `django + monorepo + scheduler`
- `laravel + cli-worker + scheduler`
- `django + cli-worker + scheduler`

The repository now needs an explicit design decision about which compounds are
safe next openings and which should remain closed. This lane evaluates that
question without implementing new support.
