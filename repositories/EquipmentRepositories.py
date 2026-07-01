from models.Equipment import Equipment

class EquipmentRepositories():
    FILE_PATH = 'data/equipmentData.txt'
    __equipmentList = []

    def __init__(self):
        self.__equipmentList = self.loadEquipments()
    
    def loadEquipments(self):
        pass
    def saveEquipments(self):
        pass

    def searchById(self):
        pass
    def searchByStatus(self):
        pass
    def append(self):
        pass
    def update(self):
        pass
    def sort(self):
        pass
    def groupByStatus(self):
        pass
