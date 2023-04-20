import csv

class Item:
    def __init__(self):
        self.id = None
        self.name = None
        self.amount = 0
        
class Warehouse:
    def __init__(self):
        self.id = None
        self.name = None
        self.item = {}
        
    def add_item(self, item, quantity):
        if item.id in self.items:
            self.items[item.id] += quantity
        else:
            self.items[item.id] = quantity
            
    def remove_item(self, item, quantity):
        if item.id in self.items:
            if self.items[item.id] >= quantity:
                self.items[item.id] -= quantity
                return True
        return False
        
class Distributor:
    def __init__(self):
        self.id = None
        self.name = None
        self.address = None
        self.items = {}
        
    def add_item(self, item, quantity):
        if item.id in self.items:
            self.items[item.id] += quantity
        else:
            self.items[item.id] = quantity
            
    def remove_item(self, item, quantity):
        if item.id in self.items:
            if self.items[item.id] >= quantity:
                self.items[item.id] -= quantity
                return True
        return False
        
class InventoryManager:
    def __init__(self):
        self.items = {}
        self.warehouses = {}
        self.distributors = {}
        
    def add_item(self, id, name, description):
        item = Item(id, name, description)
        self.items[id] = item
        
    def add_warehouse(self, id, name):
        warehouse = Warehouse(id, name)
        self.warehouses[id] = warehouse
        
    def add_distributor(self, id, name, address):
        distributor = Distributor(id, name, address)
        self.distributors[id] = distributor
        
    def assign_item(self, warehouse_id, item_id, quantity):
        if item_id in self.items and warehouse_id in self.warehouses:
            item = self.items[item_id]
            warehouse = self.warehouses[warehouse_id]
            warehouse.add_item(item, quantity)
            return True
        return False
        
    def distribute_item(self, distributor_id, item_id, quantity):
        if item_id in self.items and distributor_id in self.distributors:
            item = self.items[item_id]
            distributor = self.distributors[distributor_id]
            if distributor.remove_item(item, quantity):
                filename = f"{distributor.name}_{item.name}_inventory.txt"
                with open(filename, "a") as file:
                    file.write(f"{item.name} - {quantity}\n")
                return True
        return False
