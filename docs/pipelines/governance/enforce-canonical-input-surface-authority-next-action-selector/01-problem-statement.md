# Problem Statement

Pipelines 174 and 175 repaired and verified fail-closed roadmap resolution, but
the selector still needed explicit canonical-input authority enforcement.

Without that hardening layer, shadow or stale governance surfaces could
potentially influence next-action selection even when resolution logic itself is
correct.
