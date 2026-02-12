# query.py

import strawberry

from .category_query import (
    CategoryAllFilterQuery,
    CategoryAllQuery,
    CategoryAnnotateQuery,
)
from .order_query import OrderAllQuery
from .product_query import ProductAllQuery, ProductQuery


@strawberry.type
class Query(
    CategoryAllFilterQuery,
    CategoryAllQuery,
    ProductQuery,
    ProductAllQuery,
    OrderAllQuery,
    CategoryAnnotateQuery,
):
    pass
