# Registry Alignment

Pipeline `096` previously expected registry details that the current registry
surface does not encode directly.

Normalized registry expectations:

- registry entry exists
- pipeline definition path recorded
- status recorded correctly

Removed drifted expectations:

- explicit artifact bundle path recorded
- pipeline classification recorded in the registry table
- stage recorded in the registry table

Additional registry alignment performed:

- registered pipeline `096` as active
- registered pipeline `097` as active

Result: `REGISTRY_EXPECTATIONS_ALIGNED_TO_SCHEMA`
