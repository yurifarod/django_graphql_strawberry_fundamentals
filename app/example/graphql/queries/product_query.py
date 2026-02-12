from typing import List, Optional

import strawberry
from django.db.models import Avg, Max, Min, Q, Sum
from example.graphql.inputs.utiliy_input import PageInput
from example.graphql.types.product_type import (
    ProductListWithCountType,
    ProductSummaryType,
)
from inventory.models import Product

from .utils.range import apply_price_filter

PAGE_SIZE = 10  # 10 products per page


@strawberry.type
class ProductAllQuery:
    @strawberry.field
    def all_products(
        self,
        price_gte: Optional[float] = None,
        price_lte: Optional[float] = None,
        is_active: Optional[bool] = None,
        is_digital: Optional[bool] = None,
        category_ids: Optional[List[int]] = None,
        name_contains: Optional[str] = None,
    ) -> ProductSummaryType:
        products = Product.objects.all()
        products = apply_price_filter(products, price_gte, price_lte)

        logic = Q()

        if is_active is not None and is_digital is not None:
            logic &= Q(is_active=is_active) & Q(is_digital=is_digital)
        else:
            if is_active is not None:
                logic &= Q(is_active=is_active)
            if is_digital is not None:
                logic &= Q(is_digital=is_digital)

        if category_ids:
            logic &= Q(category_id__in=category_ids)

        if name_contains is not None:
            logic &= Q(name__icontains=name_contains)

        if logic:
            products = products.filter(logic)

        aggregation = products.aggregate(
            total_price=Sum("price"),
            average_price=Avg("price"),
            min_price=Min("price"),
            max_price=Max("price"),
        )

        return ProductSummaryType(
            products=list(products),
            total_price=aggregation["total_price"] or 0.0,
            average_price=aggregation["average_price"] or 0.0,
            min_price=aggregation["min_price"] or 0.0,
            max_price=aggregation["max_price"] or 0.0,
        )


@strawberry.type
class ProductQuery:
    @strawberry.field
    def all_products_pagination(
        self, pagination: Optional[PageInput] = None
    ) -> ProductListWithCountType:
        queryset = Product.objects.all().order_by("id")

        page = pagination.page if pagination else 1
        offset = (page - 1) * PAGE_SIZE
        limit = PAGE_SIZE

        total_count = queryset.count()
        products = queryset[offset : offset + limit]

        return ProductListWithCountType(count=total_count, records=list(products))
