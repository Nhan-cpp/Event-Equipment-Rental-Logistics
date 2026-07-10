from models.Equipment import Equipment
from services.EquipmentServices import EquipmentServices

class equipmentMenu():
    __services = None
    def __init__(self):
        super().__init__()
        self.__services = EquipmentServices()
        if(self.__services.loadEquipments() == False):
            raise ValueError("Load data Failed.")

    def saveEquipments(self):
        if(self.__services.saveEquipments() == False):
            raise ValueError("Save data Failed.")

    def writeEquipmentMaintenanceLog(self):
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