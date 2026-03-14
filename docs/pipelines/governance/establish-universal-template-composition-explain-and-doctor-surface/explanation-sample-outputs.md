# Explanation Sample Outputs

## Supported Example

```json
{
  "closest_supported": [],
  "decision_source": "docs/contracts/universal-template-composition-contract.md",
  "normalized_overlays": ["cli-worker", "python-package"],
  "reason_code": "certified-multi-overlay",
  "rejection_reason": null,
  "requested_overlays": ["cli-worker", "python-package"],
  "supported": true
}
```

## Unsupported Example

```json
{
  "closest_supported": [
    ["cli-worker", "monorepo"],
    ["cli-worker", "node-typescript-service"],
    ["cli-worker", "php-package"],
    ["cli-worker", "python-package"]
  ],
  "decision_source": "docs/contracts/universal-template-composition-contract.md",
  "normalized_overlays": ["cli-worker", "laravel"],
  "reason_code": "explicitly-rejected",
  "rejection_reason": "incompatible runtime assumptions",
  "requested_overlays": ["laravel", "cli-worker"],
  "supported": false
}
```
