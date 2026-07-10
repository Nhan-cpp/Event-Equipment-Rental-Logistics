from models.Rental import Rental
from services.RentalServices import RentalServices

class rentalMenu():
    __services = None
    def __init__(self):
        super().__init__()
        self.__services = RentalServices()
        if(self.__services.loadRentals() == False):
            raise ValueError("Load Rental Data Failed.")
        
    def saveRentals(self):
        if(self.__services.saveRentals() == False):
            raise ValueError("Save Rental Data Failed.")

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