# mutations/user_mutation.py
import strawberry
from example.graphql.inputs.user_input import UserInput
from example.graphql.types.user_type import UserType
from inventory.models import User


@strawberry.type
class UserMutation:
    @strawberry.mutation
    def create_user(self, input: UserInput) -> UserType:
        user = User.objects.create(
            username=input.username,
            email=input.email,
            password=input.password,  # Note: store as-is for now
        )
        return user
