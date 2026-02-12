# order_input.py
import strawberry

from .order_product_input import OrderProductInput, OrderProductUpdateInput


@strawberry.input
class OrderInput:
    user_id: int
    products: list[OrderProductInput]


@strawberry.input
class OrderUpdateProductsInput:
    order_id: int
    products: list[OrderProductUpdateInput]
