# Invalid Composition Fail-Closed Findings

| case | result | observed compatibility outcome |
|------|--------|--------------------------------|
| laravel + cli-worker | BLOCKED | `Overlay cli-worker is not compatible with overlay laravel` |
| django + monorepo | BLOCKED | `Overlay django is not compatible with overlay monorepo` |
| service + monorepo | BLOCKED | `Overlay monorepo is not compatible with overlay service` |
| laravel + django | BLOCKED | `Overlay django is not compatible with overlay laravel` |

All intentionally invalid combinations failed closed with explicit compatibility messaging instead of silent degradation.
