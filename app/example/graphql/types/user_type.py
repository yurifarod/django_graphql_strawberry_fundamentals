# types/user_type.py
import strawberry_django
from inventory.models import User
from strawberry import auto


@strawberry_django.type(User)
class UserType:
    id: auto
    username: auto
    email: auto
