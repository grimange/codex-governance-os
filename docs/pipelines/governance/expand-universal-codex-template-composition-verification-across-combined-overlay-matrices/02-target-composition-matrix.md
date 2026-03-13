# Target Composition Matrix

## Supported Cases Selected

| case | overlays | reason |
|------|----------|--------|
| base-only | none | confirms the invariant base scaffold |
| node-typescript-service + monorepo | `node-typescript-service`, `monorepo` | verifies runtime-plus-topology composition |
| node-typescript-service + cli-worker | `node-typescript-service`, `cli-worker` | verifies combined non-framework runtime overlays |
| cli-worker + monorepo | `cli-worker`, `monorepo` | verifies worker topology composition |
| cli-worker + python-package | `cli-worker`, `python-package` | verifies package-plus-worker composition |
| cli-worker + php-package | `cli-worker`, `php-package` | verifies package-plus-worker composition in the PHP branch |

## Invalid Cases Selected

| case | overlays | reason |
|------|----------|--------|
| laravel + cli-worker | `laravel`, `cli-worker` | framework plus worker combination documented as unsupported |
| django + monorepo | `django`, `monorepo` | unsupported framework-plus-topology combination |
| service + monorepo | `service`, `monorepo` | generic service overlay is not declared composable with monorepo |
| laravel + django | `laravel`, `django` | mutually exclusive framework overlays |
