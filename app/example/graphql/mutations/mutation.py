# mutation.py

import strawberry

from .category_mutation import CategoryDeleteMutation, CategoryMutation
from .order_mutation import OrderMutation, OrderUpdateMutation
from .product_mutation import (
    ProductMutation,
    ProductPartialUpdateMutation,
    ProductUpdateMutation,
    ProductWithStockMutation,
)
from .user_mutation import UserMutation


@strawberry.type
class Mutation(
    ProductMutation,
    CategoryMutation,
    ProductWithStockMutation,
    UserMutation,
    OrderMutation,
    ProductUpdateMutation,
    ProductPartialUpdateMutation,
    OrderUpdateMutation,
    CategoryDeleteMutation,
):
    pass
