from typing import List

import strawberry
from example.graphql.types.order_type import OrderAllType
from inventory.models import Order


@strawberry.type
class OrderAllQuery:
    @strawberry.field
    def all_orders(self) -> List[OrderAllType]:
        return Order.objects.all()
