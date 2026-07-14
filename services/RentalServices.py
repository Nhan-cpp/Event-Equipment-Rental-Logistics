from repositories.RentalRepositories import RentalRepositories
from services.EquipmentServices import EquipmentServices
from models.Rental import Rental
import os

class RentalServices():
    def __init__(self, equipmentServices : EquipmentServices):
        self.__repositories = RentalRepositories()
        self.__equipmentServices = equipmentServices

    def __ensure_file_exists(self, file_path : str):
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        open(file_path, 'a', encoding='utf-8').close()

    def loadRentals(self):
        self.__ensure_file_exists(RentalRepositories.FILE_PATH)
        try:
            self.__repositories.loadRentals()
        except Exception as e:
            raise ValueError(f"Failed to load rental records: {e}")

    def saveRentals(self):
        self.__ensure_file_exists(RentalRepositories.FILE_PATH)
        try:
            self.__repositories.saveRentals()
        except Exception as e:
            raise ValueError(f"Failed to save rental records: {e}")

    def writeRentalHistoryLog(self, rental : Rental):
        self.__ensure_file_exists(RentalRepositories.HISTORY_FILE_PATH)
        try:
            self.__repositories.writeRentalHistoryLog(rental)
        except Exception as e:
            raise ValueError(f"Failed to write rental history log: {e}")

    def readRentalHistoryLog(self):
        self.__ensure_file_exists(RentalRepositories.HISTORY_FILE_PATH)
        return self.__repositories.readRentalHistoryLog()

    def searchById(self, rentalID : str):
        return self.__repositories.searchById(rentalID)

    def getRentalById(self, rentalID: str):
        index = self.searchById(rentalID)
        if index == -1:
            raise ValueError(f"Rental ID not found: {rentalID}")
        return self.__repositories.getRentalById(index)

    def append(self,new_rental : Rental):
        if self.__repositories.searchById(new_rental.Id) != -1:
            raise ValueError("Rental ID already exists.")

        equipment = self.__equipmentServices.getEquipmentById(new_rental.equipmentId)
        if equipment.currentStatus != "Available":
            raise ValueError("Equipment is not available for rental.")

        try:
            self.__repositories.append(new_rental)
            self.__equipmentServices.update(new_rental.equipmentId, "currentStatus", False)
            self.writeRentalHistoryLog(new_rental)
        except Exception as e:
            raise ValueError(f"Failed to add rental record: {e}")

    def calculateFeesAndLatePenalties(self,rentalId : str):
        rental = self.getRentalById(rentalId)
        equipment = self.__equipmentServices.getEquipmentById(rental.equipmentId)
        hourlyRentalRate = equipment.hourlyRentalRate
        return self.__repositories.calculateFeesAndLatePenalties(rental, hourlyRentalRate)

    def sort(self, sort_type : str,is_reverse=False):
        return self.__repositories.sort(sort_type,is_reverse)
