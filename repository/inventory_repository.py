from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer
from models.inventory import Inventory


class InventoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_inventory(self):
        return self.session.query(Inventory).all()

    def get_inventory_by_id(self, item_id: int):
        return self.session.query(Inventory).filter(Inventory.item_id == cast(item_id, Integer)).first()

    def get_inventory_by_customer(self, customer: str):
        return self.session.query(Inventory).filter(Inventory.customer == cast(customer, String)).first()

    def create_inventory(self, inventory: Inventory):
        self.session.add(inventory)
        self.session.commit()
        return inventory

    def update_inventory(self, inventory: Inventory):
        self.session.add(inventory)
        self.session.commit()
        return inventory

    def delete_inventory(self, inventory: Inventory):
        self.session.delete(inventory)
        self.session.commit()
        return inventory
