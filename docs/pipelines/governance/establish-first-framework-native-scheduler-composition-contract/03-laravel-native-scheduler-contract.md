# Laravel-Native Scheduler Contract

The first framework-native scheduler contract established in this lane is the
direct pair:

- `laravel + scheduler`

Canonical support requirements:

- framework identity is Laravel, not a generic PHP package or service
- the canonical scheduler surface is `app/Console/Kernel.php`
- governed companion surfaces are:
  - `routes/console.php`
  - `config/scheduler.php`
  - `app/Console/Commands`
- the scheduler pair remains a direct-pair admission only

Ownership boundary:

- Laravel owns framework-native scheduling semantics through `app/Console/Kernel.php`
- the scheduler overlay contributes governed scheduler support surfaces and remains part of the composition contract
- this lane does not admit `laravel + monorepo + scheduler`
- this lane does not admit `django + scheduler`

Fail-closed rule:

- if the framework is Django, rejection remains explicit
- if a future lane tries to broaden Laravel scheduler support beyond the direct pair, it must update the matrix and contract explicitly
