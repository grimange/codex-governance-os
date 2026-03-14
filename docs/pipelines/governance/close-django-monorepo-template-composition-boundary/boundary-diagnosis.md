# Boundary Diagnosis

The previous rejection was structural rather than conceptual.

Missing decisions were:

- where the Django service lives in a monorepo
- which overlay owns repository root versus application subtree
- how manifests communicate that nested placement
- how scaffold realization avoids root-level Django surfaces conflicting with monorepo surfaces

The selected diagnosis is:

- monorepo owns repository root
- Django owns `apps/backend/django-service/`
- governance surfaces remain rooted at repository top level
