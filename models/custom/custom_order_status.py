from sqlalchemy.types import TypeDecorator, Integer
from enums.order_status import OrderStatus


class OrderStatusType(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, dialect):
        if isinstance(value, OrderStatus):
            return value.value
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return OrderStatus(value)
        return value
