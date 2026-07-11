from models.Equipment import Equipment
from repositories.EquipmentRepositories import EquipmentRepositories
import os

class EquipmentServices():
    __repositories = None
    def __init__(self):
        self.__repositories = EquipmentRepositories()

    def __ensure_file_exists(self, file_path):
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                pass

    def loadEquipments(self):
        self.__ensure_file_exists(EquipmentRepositories.FILE_PATH)
        try:
            self.__repositories.loadEquipments()
        except Exception as e:
            raise ValueError(f"Failed to load equipment data: {e}")
    
    def saveEquipments(self):
        self.__ensure_file_exists(EquipmentRepositories.FILE_PATH)
        try:
            self.__repositories.saveEquipments()
        except Exception as e:
            raise ValueError(f"Failed to save equipment data: {e}")
        
    def writeEquipmentMaintenanceLog(self, equipment, action):
        self.__ensure_file_exists(EquipmentRepositories.MAINTENANCE_FILE_PATH)
        try:
            self.__repositories.writeEquipmentMaintenanceLog(equipment, action)
        except Exception as e:
            raise ValueError(f"Failed to write maintenance log: {e}")
        
    def getEquipmentById(self, equipmentID : str) -> Equipment:
        index = self.searchById(equipmentID)
        if index == -1:
            raise ValueError(f"Equipment ID not found: {equipmentID}")
        return self.__repositories.getEquipmentById(index)
    
    def searchById(self,equipmentID):
        return self.__repositories.searchById(equipmentID)
    
    def searchByStatus(self, status : bool):
        return self.__repositories.searchByStatus(status)
    
    def append(self, new_equipment : Equipment):
        if self.searchById(new_equipment.Id) != -1:
            raise ValueError("Equipment ID already exists.")
        if new_equipment.powerRating <= 0 or new_equipment.hourlyRentalRate <= 0:
            raise ValueError("Power rating and hourly rental rate must be greater than 0.") 

        try:
            self.__repositories.append(new_equipment)
        except Exception as e:
            raise ValueError(f"Failed to add equipment: {e}")

    def update(self, equipmentID, selectedField, newValue):
        index = self.__repositories.searchById(equipmentID)
        if index == -1:
            raise ValueError("Equipment ID not found.")

        validFields = ["powerRating","hourlyRentalRate","currentStatus"]
        if selectedField not in validFields:
            raise ValueError("Invalid field selected for update.")
            
        # if selectedField != "currentStatus":
        #     if newValue <= 0:
        #         raise ValueError("Numeric values must be greater than 0.")
                
        try:
            self.__repositories.update(index, selectedField, newValue)
        except Exception as e:
            raise ValueError(f"Failed to update equipment: {e}")
    
    def sort(self, sortType, isReverse):
        if sortType != "hourlyRentalRate" and sortType != "powerRating":
            return []  # Trả về danh sách rỗng nếu kiểu sort không hợp lệ

        return self.__repositories.sort(sortType, isReverse)
    
    def groupByStatus(self):
        return self.__repositories.groupByStatus()