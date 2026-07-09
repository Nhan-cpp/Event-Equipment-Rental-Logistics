from repositories.RentalRepositories import RentalRepositories
from models.Rental import Rental

class RentalServices():

    __repositories = None

    def __init__(self):
        self.__repositories = RentalRepositories()

    def loadRentals(self):
        try:
            self.__repositories.loadRentals()
            return True
        except:
            return False

    def saveRentals(self):
        try:
            self.__repositories.saveRentals()
            return True
        except:
            return False

    def writeRentalHistoryLog(self, rental):
        try:
            self.__repositories.writeRentalHistoryLog(rental)
            return True
        except:
            return False

    def searchById(self, rentalID):
        try:
            rentalID = str(rentalID)
            return self.__repositories.searchById(rentalID)
        except:
            raise ValueError("rental Id need be a string.")
        
    def append(self,new_rental : Rental):
        if(self.__repositories.searchById(new_rental.Id) != -1):
            return False
        if(new_rental.startTime > new_rental.expectedReturnTime):
            return False
        
        self.__repositories.append(new_rental)
        return True
        
    def calculateFeesAndLatePenalties(self,rentalId):
        return self.__repositories.calculateFeesAndLatePenalties(rentalId)
    def sort(self, sort_type,is_reverse=False):
        return self.__repositories.sort(sort_type,is_reverse)