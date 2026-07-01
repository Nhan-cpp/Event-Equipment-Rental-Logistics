from models.Rental import Rental

class RentalRepositories():
    FILE_PATH = 'data/rentalData.txt'
    __rentalList = []

    def __init__(self):
        self.__rentalList = self.loadRentals()
    def loadRentals(self):
        pass
    def saveRentals(self):
        pass

    def searchById(self):
        pass
    def append(self):
        pass
    def calculateFeesAndLatePenalties(self):
        pass
    def sort(self):
        pass