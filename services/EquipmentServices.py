from models.Equipment import Equipment
from repositories.EquipmentRepositories import EquipmentRepositories

class EquipmentServices():
    __repositories = None
    def __init__(self):
        self.__repositories = EquipmentRepositories()

    def loadEquipments(self):
        equipmentList = self.__repositories.loadEquipments()
        return True
    
    def saveEquipments(self):
        try:
            self.__repository.saveEquipments()
            return True
        except:
            return False
        
    def writeEquipmentMaintenanceLog(self, equipment, action):
        try:
            self.__repositories.writeEquipmentMaintenanceLog(equipment, action)
            return True
        except:
            return False
        
    def searchById(self,equipmentID):
        return self.__repositories.searchById(equipmentID)
    
    def searchByStatus(self, status : bool):
        return self.__repositories.searchByStatus(status)
    
    def append(self, new_equipment : Equipment):
        if self.__repositories.searchById(new_equipment.Id) != -1:
            return False
        if new_equipment.powerRating <= 0 or new_equipment.hourlyRentalRate <= 0:
            return False 

        self.__repositories.append(new_equipment)
        return True

    def update(self, equipmentID, selectedField, newValue):
        """
        Kiểm tra:
        1. Equipment có tồn tại không.
        2. Field hợp lệ không.
        3. Giá trị nhập hợp lệ không.
        """

        if self.__repositories.searchById(equipmentID) == -1:
            return False

        validFields = ["powerRating","hourlyRentalRate","currentStatus"]
        if selectedField not in validFields:
            return False
        if selectedField != "currentStatus":
            if newValue <= 0:
                return False
        self.__repositories.update(equipmentID,selectedField,newValue)
        return True
    
    def sort(self, sortType, isReverse):
        if sortType != "hourlyRentalRate" and sortType != "powerRating":
            return []  # Trả về danh sách rỗng nếu kiểu sort không hợp lệ

        return self.__repositories.sort(sortType, isReverse)
    
    def groupByStatus(self):
        return self.__repositories.groupByStatus()