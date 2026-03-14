# Boundary Definition

The unsupported composition boundary is:

```text
laravel + cli-worker
```

Formal reason:

`missing Laravel worker composition contract`

This means the repository does not currently define:

- Laravel-owned worker lifecycle semantics
- entrypoint coordination between `artisan` and generic worker surfaces
- deterministic ownership rules for `bin`, `jobs`, and `worker`

Until those semantics are designed and certified in a future lane, the pair must remain fail-closed.
