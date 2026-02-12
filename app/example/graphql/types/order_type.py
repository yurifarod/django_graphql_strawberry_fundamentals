# order_type.py
from typing import List

import strawberry
import strawberry_django
from inventory.models import Order, OrderProduct
from strawberry import auto

from .product_type import ProductType
from .user_type import UserType


@strawberry_django.type(Order)
class OrderType:
    id: auto
    created_at: auto
    updated_at: auto
    user: UserType

    @strawberry.field
    def products(self) -> list["OrderProductItemType"]:
        return self.orderproduct_set.all()


@strawberry.type
class OrderProductItemType:
    quantity: int
    product: ProductType


@strawberry_django.type(OrderProduct)
class OrderProductType:
    id: auto
    quantity: auto
    order: OrderType
    product: ProductType


@strawberry_django.type(Order)
class OrderAllType:
    id: auto
    created_at: auto
    updated_at: auto
    user: UserType  # ForeignKey to User
    orderproduct_set: List[OrderProductType]
