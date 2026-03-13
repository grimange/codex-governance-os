# Cli Worker Overlay Contract

## Overlay Name

`cli-worker`

## Applies To

- command-line applications
- queue or batch workers
- scheduled or daemon-like processors where HTTP routing is not the primary runtime surface

## Required Surfaces

- `bin/`
- `jobs/`
- `worker/`

## Optional Surfaces

- `tasks/`
- `scheduler/`
- `queue/`

## Compatibility Rules

- compatible with base scaffold
- compatible with `python-package`
- compatible with `php-package`
- compatible with `node-typescript-service`
- compatible with `monorepo`
- not compatible with `laravel`, `django`, or the generic `service` overlay unless explicitly modeled later

## Invariants

- does not require HTTP routing
- preserves governance core semantics
- keeps command and worker expectations explicit rather than implicit
