# Negative Case Verification

Preserved explicit rejection:

- `scheduler + django` -> `explicitly-rejected`
- `conflict_code: framework-native-scheduler-required`
- `rejection_reason: missing Django-native scheduler composition contract`

Preserved restriction:

- `laravel + monorepo + scheduler` was not admitted by pipeline `064` and remains outside the supported matrix

This confirms:

- Laravel support did not silently broaden into generic framework scheduler support
- Django remains fail-closed pending a separate framework-native contract lane
