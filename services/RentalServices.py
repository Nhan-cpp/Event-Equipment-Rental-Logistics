from repositories.RentalRepositories import RentalRepositories

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
    
    def append(self):
        pass
    def calculateFeesAndLatePenalties(self):
        pass
    def sort(self):
        pass