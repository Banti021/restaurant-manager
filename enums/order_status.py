from enum import Enum


class OrderStatus(Enum):
    OPEN = 0
    IN_PROGRESS = 1
    DELIVERED = 2
    CANCELLED = 3
    CLOSED = 4

