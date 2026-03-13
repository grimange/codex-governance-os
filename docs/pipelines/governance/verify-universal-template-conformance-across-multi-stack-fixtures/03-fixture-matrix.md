# Fixture Matrix

| fixture | ecosystem / shape | overlay | status | reason |
|---------|-------------------|---------|--------|--------|
| minimal-governed-repo | governance-only bare repository | none | supported | verifies the base contract without runtime overlays |
| laravel-application | Laravel application / service | `laravel` | supported | verifies framework overlay composition |
| django-application | Django application / service | `django` | supported | verifies framework overlay composition |
| python-package | generic Python package | `python-package` | supported | verifies package-oriented overlay |
| php-package | PHP package or library | `php-package` | supported | verifies package-oriented overlay |
| service-repository | generic service repository | `service` | supported | verifies service topology overlay |
| monorepo | monorepo / modernization shape | `monorepo` | supported | verifies multi-scope topology overlay |
| node-typescript-service | Node or TypeScript service | none | unsupported | no manifest currently declares this overlay |
| cli-worker | CLI or worker repository | none | unsupported | no manifest currently declares this overlay |

Unsupported categories are treated as explicit current boundaries, not hidden passes.
