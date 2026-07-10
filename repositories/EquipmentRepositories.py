from models.Equipment import Equipment
import os

class EquipmentRepositories():
    FILE_PATH = 'data/equipmentData.txt'
    MAINTENANCE_FILE_PATH = 'data/equipmentMaintenanceLog.txt'
    __equipmentList = []
    def __init__(self):
        self.__equipmentList = self.loadEquipments()
    
    def loadEquipments(self):
        equipmentList = []

        if not os.path.exists(self.FILE_PATH):
            os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)

            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                pass
            self.__equipmentList = equipmentList

        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(',')
                    
                    equipment = Equipment(parts[0],float(parts[1]),float(parts[2]),(parts[3] == 'True'))
                    equipmentList.append(equipment)
        except FileNotFoundError:
            raise ValueError("Equipment file not found. Start with empty list.")
        self.__equipmentList = equipmentList
    
    def saveEquipments(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        try:
            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                for equipment in self.__equipmentList:
                    line = f"{equipment.Id},{equipment.powerRating},{equipment.hourlyRentalRate},{equipment.currentStatus}\n"
                    file.write(line)
            
        except Exception:
            raise ValueError

    def writeEquipmentMaintenanceLog(self, equipment, action):
        os.makedirs(os.path.dirname(self.MAINTENANCE_FILE_PATH), exist_ok=True)
        try:
            from datetime import datetime
            with open(self.MAINTENANCE_FILE_PATH, 'a', encoding='utf-8') as file:
                current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                line = f"{equipment.Id},{equipment.powerRating},{equipment.hourlyRentalRate},{equipment.currentStatus},{action},{current_time}\n"
                file.write(line)
            return True
        except Exception:
            raise ValueError("Error while writing equipment maintenance log")

    def searchById(self, equipmentID):
        for index in range(len(self.__equipmentList)):
            if self.__equipmentList[index].Id == equipmentID:
                return index
        return -1
    
    def searchByStatus(self, status):
        resultList = []
        for equipment in self.__equipmentList:
            if equipment.currentStatus == status:
                resultList.append(equipment)
                    
        return resultList
    
    def append(self, new_equipment : Equipment):
        self.__equipmentList.append(new_equipment)
    
    def update(self, index : int, selectedField : str, newValue):
        equipment = self.__equipmentList[index]

        if selectedField == "powerRating":
            equipment.powerRating = newValue
        elif selectedField == "hourlyRentalRate":
            equipment.hourlyRentalRate = newValue
        elif selectedField == "currentStatus":
            equipment.currentStatus = newValue
        
        self.__equipmentList[index] = equipment
    
    def sort(self, sortType, isReverse):
        criteria = {
            "hourlyRentalRate": lambda x: x.hourlyRentalRate,
            "powerRating": lambda x: x.powerRating
        }
        return sorted(self.__equipmentList, key=criteria[sortType], reverse=isReverse)
    
    def groupByStatus(self):
        availableList = []
        rentedList = []

        for equipment in self.__equipmentList:
            if equipment.currentStatus:
                availableList.append(equipment)
            else:
                rentedList.append(equipment)
        return availableList, rentedList
