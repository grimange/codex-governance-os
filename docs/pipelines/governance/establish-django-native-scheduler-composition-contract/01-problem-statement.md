# Problem Statement

After pipeline `064`, framework-native scheduler support existed only for
`laravel + scheduler`. Django remained a first-class framework overlay but still
lacked an equivalent governed scheduler contract.

Pipeline `066` closes that gap by establishing the second framework-native
scheduler contract:

- `django + scheduler`

This lane does not generalize framework-native scheduling as a broad abstraction.
It opens one explicit Django-native direct pair and leaves broader compound
framework scheduler combinations fail-closed.
