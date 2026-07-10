from models.Rental import Rental
from services.RentalServices import RentalServices

class rentalMenu():
    __services = None
    def __init__(self):
        super().__init__()
        self.__services = RentalServices()
        try:
            self.__services.loadRentals()
        except ValueError as e:
            print(f"Warning: {e}")
        
    def saveRentals(self):
        try:
            self.__services.saveRentals()
        except ValueError as e:
            print(f"Error saving: {e}")

    def writeRentalHistoryLog(self):
        pass

    def searchById(self):
        pass

    def append(self):
        pass

    def calculateFeesAndLatePenalties(self):
        pass

    def sort(self):
        pass