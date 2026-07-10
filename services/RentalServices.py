from repositories.RentalRepositories import RentalRepositories
from models.Rental import Rental

class RentalServices():

    __repositories = None

    def __init__(self):
        self.__repositories = RentalRepositories()

    def __ensure_file_exists(self, file_path):
        import os
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                pass

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

    def writeRentalHistoryLog(self, rental):
        self.__ensure_file_exists(RentalRepositories.HISTORY_FILE_PATH)
        try:
            self.__repositories.writeRentalHistoryLog(rental)
        except Exception as e:
            raise ValueError(f"Failed to write rental history log: {e}")

    def searchById(self, rentalID):
        try:
            rentalID = str(rentalID)
            return self.__repositories.searchById(rentalID)
        except:
            raise ValueError("Rental ID must be a string.")
            
    def getRentalByIndex(self, rentalID: str) -> Rental:
        index = self.searchById(rentalID)
        if index == -1:
            raise ValueError(f"Rental ID not found: {rentalID}")
        return self.__repositories.getRentalByIndex(index)
        
    def append(self,new_rental : Rental):
        if self.__repositories.searchById(new_rental.Id) != -1:
            raise ValueError("Rental ID already exists.")
        if new_rental.startTime > new_rental.expectedReturnTime:
            raise ValueError("Start time cannot be after expected return time.")
        
        try:
            self.__repositories.append(new_rental)
        except Exception as e:
            raise ValueError(f"Failed to add rental record: {e}")
        
    def calculateFeesAndLatePenalties(self,rentalId):
        return self.__repositories.calculateFeesAndLatePenalties(rentalId)
    
    def sort(self, sort_type,is_reverse=False):
        return self.__repositories.sort(sort_type,is_reverse)