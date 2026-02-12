# inputs/user_input.py
import strawberry

@strawberry.input
class UserInput:
    username: str
    email: str
    password: str  # In a real app, you'd hash this