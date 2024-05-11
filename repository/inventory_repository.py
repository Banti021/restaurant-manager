from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer
from models.inventory import Inventory
from database.database import SessionLocal


class InventoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_inventory(self):
        return self.session.query(Inventory).all()

    def get_inventory_by_id(self, item_id: int):
        return self.session.query(Inventory).filter(Inventory.item_id == cast(item_id, Integer)).first()

    def get_inventory_by_customer(self, customer: str):
        return self.session.query(Inventory).filter(Inventory.customer == cast(customer, String)).first()

    def create_inventory(self, item_id: int, item_name: str, item_price: float, item_quantity: int, customer: str):
        inventory = Inventory(item_id=item_id, item_name=item_name, item_price=item_price, item_quantity=item_quantity, customer=customer)
        self.session.add(inventory)
        self.session.commit()
        return inventory

    def update_inventory(self, item_id: int, item_name: str, item_price: float, item_quantity: int, customer: str):
        inventory = self.get_inventory_by_id(item_id)
        inventory.item_name = item_name
        inventory.item_price = item_price
        inventory.item_quantity = item_quantity
        inventory.customer = customer
        self.session.commit()
        self.session.refresh(inventory)
        return inventory

    def delete_inventory(self, item_id: int):
        inventory = self.get_inventory_by_id(item_id)
        self.session.delete(inventory)
        self.session.commit()
        return inventory

class InventoryRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = InventoryRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type:
            raise exc_val
        return True