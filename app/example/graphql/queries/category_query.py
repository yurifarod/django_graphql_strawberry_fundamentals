from typing import List, Optional

import strawberry
from django.db.models import Count
from example.graphql.inputs.category_input import CategoryFilter, CategoryOrderBy
from example.graphql.inputs.utiliy_input import FirstLastInput
from example.graphql.types.category_type import (
    CategoryAnnotateType,
    CategoryListWithCountType,
    CategoryType,
)
from inventory.models import Category

ALLOWED_ORDER_FIELDS = {"name", "level", "created_at", "is_active"}


@strawberry.type
class CategoryAnnotateQuery:
    @strawberry.field
    def all_categories_annotate(
        self,
        min_products: Optional[int] = 0,
    ) -> List[CategoryAnnotateType]:
        categories = (
            Category.objects.annotate(product_count=Count("product"))
            .filter(product_count__gte=min_products)
            .order_by("id")
        )

        return [
            CategoryAnnotateType(
                name=category.name, product_count=category.product_count
            )
            for category in categories
        ]


@strawberry.type
class CategoryAllFilterQuery:
    @strawberry.field
    def all_categories_filter(
        self,
        where: Optional[CategoryFilter] = None,
        order_by: Optional[CategoryOrderBy] = None,
        first_last: Optional[FirstLastInput] = None,
    ) -> CategoryListWithCountType:
        queryset = Category.objects.all()

        if where:
            if where.is_active is not None:
                queryset = queryset.filter(is_active=where.is_active)
            if where.name:
                queryset = queryset.filter(name__icontains=where.name)

        if order_by:
            if order_by.field in ALLOWED_ORDER_FIELDS:
                direction = "" if order_by.direction == "asc" else "-"
                queryset = queryset.order_by(f"{direction}{order_by.field}")
            else:
                raise ValueError(f"Cannot order by {order_by.field}")

        # Handle first/last
        records = []
        if first_last:
            if first_last.first and first_last.last:
                raise ValueError("Cannot request both first and last at the same time.")

            if first_last.first:
                category = queryset.first()
                records = [category] if category else []

            if first_last.last:
                category = queryset.last()
                records = [category] if category else []
        else:
            records = list(queryset)

        return CategoryListWithCountType(
            count=len(records),
            records=records,
        )


@strawberry.type
class CategoryAllQuery:
    @strawberry.field
    def all_categories(self) -> list[CategoryType]:
        return Category.objects.all()
