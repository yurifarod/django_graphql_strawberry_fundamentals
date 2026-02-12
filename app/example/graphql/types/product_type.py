# product_type

from typing import List

import strawberry
import strawberry_django
from inventory.models import Product
from strawberry import auto

from .category_type import CategoryType
from .stock_type import StockManagementType


@strawberry_django.type(Product)
class ProductType:
    id: auto
    name: auto
    slug: auto
    description: auto
    is_digital: auto
    is_active: auto
    created_at: auto
    updated_at: auto
    price: auto
    category: CategoryType
    stockmanagement: StockManagementType


@strawberry.type
class ProductSummaryType:
    products: List[ProductType]
    total_price: float
    average_price: float
    min_price: float
    max_price: float


@strawberry.type
class ProductWithStockType:
    product: ProductType
    stock: StockManagementType
    category: CategoryType


@strawberry.type
class ProductListWithCountType:
    count: int
    records: list[ProductType]
