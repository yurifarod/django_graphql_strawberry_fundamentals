# order_mutation.py
import strawberry
from django.db import transaction
from example.graphql.inputs.order_input import OrderInput, OrderUpdateProductsInput
from example.graphql.types.order_type import OrderType
from inventory.models import Order, OrderProduct, Product, User


@strawberry.type
class OrderUpdateMutation:
    @strawberry.mutation
    def update_order_products(self, input: OrderUpdateProductsInput) -> OrderType:
        try:
            order = Order.objects.get(id=input.order_id)
        except Order.DoesNotExist:
            raise ValueError(f"Order with ID {input.order_id} was not found.")

        with transaction.atomic():
            # Remove existing products from the order
            OrderProduct.objects.filter(order=order).delete()

            # Recreate order-product links
            for item in input.products:
                try:
                    product = Product.objects.get(id=item.product_id)
                except Product.DoesNotExist:
                    raise ValueError(
                        f"Product with ID {item.product_id} was not found."
                    )

                OrderProduct.objects.create(
                    order=order, product=product, quantity=item.quantity
                )

        return order


@strawberry.type
class OrderMutation:
    @strawberry.mutation
    def create_order(self, input: OrderInput) -> OrderType:
        with transaction.atomic():
            user = User.objects.get(id=input.user_id)
            order = Order.objects.create(user=user)

            for item in input.products:
                product = Product.objects.get(id=item.product_id)
                OrderProduct.objects.create(
                    order=order, product=product, quantity=item.quantity
                )

        return order
