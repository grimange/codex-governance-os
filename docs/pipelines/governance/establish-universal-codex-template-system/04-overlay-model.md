# Overlay Model

## Layers

1. universal core
2. stack overlay
3. project overlay

## Implemented Rules

- Stack overlays are defined in the registry for `laravel`, `django`, `python-package`, `php-package`, `mcp-tools`, and `infrastructure`.
- Overlays may add sections but may not weaken core requirements.
- Only one stack overlay may be applied at a time by the scaffold tool to avoid ambiguous extension.
- Project overlays remain allowed conceptually but are not globally implemented by this pipeline; they remain repository-local extensions that must preserve the universal core.
