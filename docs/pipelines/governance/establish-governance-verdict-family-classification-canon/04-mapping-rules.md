# 04 — Mapping Rules

Verdict families are determined by the first matching rule in this order.

```text
if verdict contains "_WITH_GAPS":
    FAMILY = WITH_GAPS
elif verdict matches r'_WITH_(LIMITATIONS|LIMITATION|RESTRICTION|RESTRICTIONS)':
    FAMILY = WITH_LIMITATIONS
elif verdict matches r'(^|_)NORMALIZED':
    FAMILY = NORMALIZED
elif verdict contains "VERIFIED":
    FAMILY = VERIFIED
elif verdict matches r'(^|_)ESTABLISHED':
    FAMILY = ESTABLISHED
elif verdict contains "_IMPLEMENTED":
    FAMILY = IMPLEMENTED
elif verdict contains "_RESTRICTED":
    FAMILY = RESTRICTED
else:
    FAMILY = OTHER
```

Rule order is explicit and literal to avoid interpretation drift.
