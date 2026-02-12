# types/stock_type.py

import strawberry_django
from strawberry import auto
from inventory.models import StockManagement

@strawberry_django.type(StockManagement)
class StockManagementType:
    id: auto
    quantity: auto
    last_checked_at: auto