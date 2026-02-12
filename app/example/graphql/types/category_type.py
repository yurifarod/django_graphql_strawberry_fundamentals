# types.py
from typing import List

import strawberry
import strawberry_django
from inventory.models import Category
from strawberry import auto

@strawberry.type
class CategoryAnnotateType:
    name: str
    product_count: int

@strawberry.type
class DeleteStatus:
    success: bool
    message: str


@strawberry_django.type(Category)
class CategoryType:
    id: auto
    name: auto
    slug: auto
    is_active: auto
    level: auto


@strawberry.type
class CategoryListWithCountType:
    count: int
    records: List[CategoryType]
