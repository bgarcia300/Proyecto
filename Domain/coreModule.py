class persistence:
    itemsList = []
    warehousesList = []
    
    @classmethod
    def addItem(self, obj):
        self.itemsList.append(obj)
    
    @classmethod    
    def getItem(self):
        return self.itemsList
    
    @classmethod
    def addWarehouse(self, obj):
        self.warehousesList.append(obj)
    
    @classmethod    
    def getWarehouse(self):
        return self.warehousesList