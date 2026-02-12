# inputs.py
from typing import Optional

import strawberry
import strawberry_django
from inventory.models import Category
from strawberry import auto


@strawberry.input
class CategoryOrderBy:
    field: str
    direction: str  # "asc" or "desc"


@strawberry.input
class CategoryFilter:
    is_active: Optional[bool] = None
    name: Optional[str] = None


@strawberry.input
class DeleteCategoryInput:
    id: int


@strawberry_django.input(Category)
class CategoryInput:
    name: auto
    slug: auto
    is_active: auto
    level: auto
    parent_id: int | None = None
