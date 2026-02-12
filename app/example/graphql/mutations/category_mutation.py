# mutations.py

import strawberry
from example.graphql.inputs.category_input import CategoryInput, DeleteCategoryInput
from example.graphql.types.category_type import CategoryType, DeleteStatus
from inventory.models import Category


@strawberry.type
class CategoryDeleteMutation:
    @strawberry.mutation
    def delete_category(self, input: DeleteCategoryInput) -> DeleteStatus:
        try:
            category = Category.objects.get(id=input.id)
        except Category.DoesNotExist:
            return DeleteStatus(success=False, message="Category not found.")

        category.delete()
        return DeleteStatus(success=True, message="Category deleted.")


@strawberry.type
class CategoryMutation:
    @strawberry.mutation
    def create_category(self, input: CategoryInput) -> CategoryType:
        category = Category.objects.create(
            name=input.name,
            slug=input.slug,
            is_active=input.is_active,
            level=input.level,
            parent=input.parent_id,
        )
        return category
