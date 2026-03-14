# Decision Consistency Matrix

## Supported Cases

| composition | contract | doctor | scaffold |
|-------------|----------|--------|----------|
| base-only | supported | supported | supported |
| `node-typescript-service + monorepo` | supported | supported | supported |
| `node-typescript-service + cli-worker` | supported | supported | supported |
| `cli-worker + monorepo` | supported | supported | supported |
| `cli-worker + python-package` | supported | supported | supported |
| `cli-worker + php-package` | supported | supported | supported |

## Rejected Cases

| composition | contract | doctor | scaffold |
|-------------|----------|--------|----------|
| `laravel + cli-worker` | rejected | rejected | rejected |
| `django + monorepo` | rejected | rejected | rejected |
| `service + monorepo` | rejected | rejected | rejected |
| `laravel + django` | rejected | rejected | rejected |

## Inventory Drift Surfaces

| surface | invalid manifest mutation result |
|---------|----------------------------------|
| `list-manifests` | identical structured failure payload |
| `list_templates` | identical structured failure payload |
