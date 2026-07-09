from repositories.RentalRepositories import RentalRepositories
from models.Rental import Rental

class RentalServices():

    __repositories = None

    def __init__(self):
        self.__repositories = RentalRepositories()

    def loadRentals(self):
        rentalList = self.__repositories.loadRentals()
        return rentalList

    def saveRentals(self):
        return self.__repositories.saveRentals()

    def writeRentalHistoryLog(self, rental):
        return self.__repositories.writeRentalHistoryLog(rental)

    def searchById(self, rentalID):
        return self.__repositories.searchById(rentalID)
    
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