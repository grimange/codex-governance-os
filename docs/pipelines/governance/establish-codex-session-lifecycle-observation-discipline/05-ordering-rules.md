# Ordering Rules

The new canon requires lifecycle observation ordering that remains compatible
with the state-machine canon and admission doctrine.

Core ordering rules:

- initialization must be observable before admission
- admission must be observable before activation
- activation must be observable before meaningful active execution is treated
  as governed execution
- closure preparation must precede terminal closure
- resumed continuity must not collapse handoff completion, resumed status,
  renewed admission, and later activation into one undifferentiated step

Observed ordering that contradicts the canonical lifecycle model should be
treated as lifecycle drift or insufficient evidence rather than normalized
away.
