from models.Equipment import Equipment
from repositories.EquipmentRepositories import EquipmentRepositories
import os

class EquipmentServices():
    def __init__(self):
        self.__repositories = EquipmentRepositories()

    def __ensure_file_exists(self, file_path : str):
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        open(file_path, 'a', encoding='utf-8').close()

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

    def writeEquipmentMaintenanceLog(self, equipment : Equipment, action : str):
        self.__ensure_file_exists(EquipmentRepositories.MAINTENANCE_FILE_PATH)
        try:
            self.__repositories.writeEquipmentMaintenanceLog(equipment, action)
        except Exception as e:
            raise ValueError(f"Failed to write maintenance log: {e}")

    def readEquipmentMaintenanceLog(self):
        self.__ensure_file_exists(EquipmentRepositories.MAINTENANCE_FILE_PATH)
        return self.__repositories.readEquipmentMaintenanceLog()

    def getEquipmentById(self, equipmentID : str):
        index = self.searchById(equipmentID)
        if index == -1:
            raise ValueError(f"Equipment ID not found: {equipmentID}")
        return self.__repositories.getEquipmentById(index)

    def searchById(self,equipmentID : str):
        return self.__repositories.searchById(equipmentID)

    def searchByStatus(self, status : str):
        return self.__repositories.searchByStatus(status)

    def append(self, new_equipment : Equipment):
        if self.searchById(new_equipment.Id) != -1:
            raise ValueError("Equipment ID already exists.")

        try:
            self.__repositories.append(new_equipment)
            self.writeEquipmentMaintenanceLog(new_equipment, "Added new equipment")
        except Exception as e:
            raise ValueError(f"Failed to add equipment: {e}")

    def update(self, equipmentID : str, selectedField : str, newValue):
        index = self.__repositories.searchById(equipmentID)
        if index == -1:
            raise ValueError("Equipment ID not found.")

        validFields = ["powerRating","hourlyRentalRate","currentStatus"]
        if selectedField not in validFields:
            raise ValueError("Invalid field selected for update.")

        try:
            self.__repositories.update(index, selectedField, newValue)
            updated_equipment = self.__repositories.getEquipmentById(index)
            self.writeEquipmentMaintenanceLog(updated_equipment, f"Updated {selectedField} to {newValue}")
        except Exception as e:
            raise ValueError(f"Failed to update equipment: {e}")

    def sort(self, sortType : str, isReverse : bool):
        if sortType != "hourlyRentalRate" and sortType != "powerRating":
            return []

        return self.__repositories.sort(sortType, isReverse)

    def groupByStatus(self):
        return self.__repositories.groupByStatus()
