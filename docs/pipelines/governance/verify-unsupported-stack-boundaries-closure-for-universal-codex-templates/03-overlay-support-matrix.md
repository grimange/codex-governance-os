# Overlay Support Matrix

| overlay or shape | status | evidence |
|------------------|--------|----------|
| base-only | verified supported | scaffold realization and conformance test |
| laravel | verified supported | existing scaffold and conformance test |
| django | verified supported | existing scaffold and conformance test |
| python-package | verified supported | existing scaffold and conformance test |
| php-package | verified supported | existing scaffold and conformance test |
| service | verified supported | existing scaffold and conformance test |
| monorepo | verified supported | existing scaffold and conformance test |
| node-typescript-service | verified supported | manifest inventory, scaffold realization, and conformance test |
| cli-worker | verified supported | manifest inventory, scaffold realization, and conformance test |
| node-typescript-service + monorepo | verified supported | explicit scaffold realization and scaffold test |
| cli-worker + python-package | verified supported | explicit scaffold realization and scaffold test |
| laravel + cli-worker | fail-closed invalid combination | explicit scaffold rejection with compatibility error |
