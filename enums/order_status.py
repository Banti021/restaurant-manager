from enum import Enum


class OrderStatus(Enum):
    OPEN = 0
    IN_PROGRESS = 1
    DELIVERED = 2
    CANCELLED = 3
    CLOSED = 4

    @staticmethod
    def list_statuses():
        return [(status.name, status.value) for status in OrderStatus]
