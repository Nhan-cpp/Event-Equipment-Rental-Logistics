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
    def searchById(self, equipmentID):
        for index in range(len(self.__equipmentList)):
            if self.__equipmentList[index].ID == equipmentID:
                return index
        return -1
    def searchByStatus(self):
        pass
    def append(self, new_equipment):
        self.__equipmentList.append(new_equipment)
        return True
    def update(self):
        pass
    def sort(self, sortType, isReverse):
        criteria = {
            "hourlyRentalRate": lambda x: x.hourlyRentalRate,
            "powerRating": lambda x: x.powerRating
        }
        return sorted(self.__equipmentList, key=criteria[sortType], reverse=isReverse)
    def groupByStatus(self):
        pass
