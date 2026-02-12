# order_product_input.py
import strawberry


@strawberry.input
class OrderProductInput:
    product_id: int
    quantity: int


@strawberry.input
class OrderProductUpdateInput:
    product_id: int
    quantity: int
