# product_mutation.py

from datetime import datetime

import strawberry
from django.db import transaction
from example.graphql.inputs.product_input import (
    ProductInput,
    ProductPartialUpdateInput,
    ProductUpdateInput,
    ProductWithStockInput,
)
from example.graphql.types.product_type import ProductType, ProductWithStockType
from inventory.models import Category, Product, StockManagement


@strawberry.type
class ProductPartialUpdateMutation:
    @strawberry.mutation
    def update_product_partial(self, input: ProductPartialUpdateInput) -> ProductType:
        product = Product.objects.get(id=input.id)

        if input.name is not None:
            product.name = input.name
        if input.slug is not None:
            product.slug = input.slug
        if input.description is not None:
            product.description = input.description
        if input.is_digital is not None:
            product.is_digital = input.is_digital
        if input.is_active is not None:
            product.is_active = input.is_active
        if input.price is not None:
            product.price = input.price

        product.save()
        return product


@strawberry.type
class ProductUpdateMutation:
    @strawberry.mutation
    def update_product(self, input: ProductUpdateInput) -> ProductType:
        try:
            product = Product.objects.get(id=input.id)
        except Product.DoesNotExist:
            raise ValueError(f"Product with ID {input.id} was not found.")

        try:
            category = Category.objects.get(id=input.category_id)
        except Category.DoesNotExist:
            raise ValueError(f"Category with ID {input.category_id} does not exist.")

        product.name = input.name
        product.slug = input.slug
        product.description = input.description
        product.is_digital = input.is_digital
        product.is_active = input.is_active
        product.price = input.price
        product.category = category

        product.save()
        return product


@strawberry.type
class ProductMutation:
    @strawberry.mutation
    def create_product(self, input: ProductInput) -> ProductType:
        category = Category.objects.filter(id=input.category_id).first()

        if not category:
            raise ValueError("Invalid category ID provided.")

        product = Product.objects.create(
            name=input.name,
            slug=input.slug,
            description=input.description,
            is_digital=input.is_digital,
            is_active=input.is_active,
            price=input.price,
            category=category,
        )
        return product


@strawberry.type
class ProductWithStockMutation:
    @strawberry.mutation
    def create_product_with_stock(
        self, input: ProductWithStockInput
    ) -> ProductWithStockType:
        with transaction.atomic():
            category = Category.objects.filter(id=input.category_id).first()

            if not category:
                raise ValueError("Invalid category ID provided.")

            product = Product.objects.create(
                name=input.name,
                slug=input.slug,
                description=input.description,
                is_digital=input.is_digital,
                is_active=input.is_active,
                price=input.price,
                category=category,
            )

            stock = StockManagement.objects.create(
                product=product,
                quantity=input.quantity if input.quantity is not None else 0,
                last_checked_at=datetime.now(),
            )

        return ProductWithStockType(product=product, stock=stock, category=category)
