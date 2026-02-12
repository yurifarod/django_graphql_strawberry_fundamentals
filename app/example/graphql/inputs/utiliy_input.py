from typing import Optional

import strawberry


@strawberry.input
class FirstLastInput:
    first: Optional[bool] = None
    last: Optional[bool] = None

@strawberry.input
class PageInput:
    page: int = 1