from decimal import Decimal

import strawberry
import strawberry_django
from inventory.models import Product
from strawberry import auto

@strawberry.input
class ProductPartialUpdateInput:
    id: int  # required to find the product
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    is_digital: bool | None = None
    is_active: bool | None = None
    price: Decimal | None = None


@strawberry.input
class ProductUpdateInput:
    id: int  # required to look up the product
    name: str
    slug: str
    description: str
    is_digital: bool
    is_active: bool
    price: Decimal
    category_id: int


@strawberry_django.input(Product)
class ProductInput:
    name: auto
    slug: auto
    description: auto
    is_digital: auto
    is_active: auto
    price: auto
    category_id: int  # This is the ForeignKey (must be passed as an ID)


@strawberry.input
class ProductWithStockInput(ProductInput):
    quantity: int | None = None  # Extra input, not in Product model
