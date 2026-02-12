from typing import Optional
from django.db.models import QuerySet

def apply_price_filter(
    queryset: QuerySet,
    price_gte: Optional[float] = None,
    price_lte: Optional[float] = None,
) -> QuerySet:
    if price_gte is not None:
        queryset = queryset.filter(price__gte=price_gte)
    if price_lte is not None:
        queryset = queryset.filter(price__lte=price_lte)
    return queryset