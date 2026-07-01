from repositories.RentalRepositories import RentalRepositories

class RentalServices():

    __repositories = None

    def __init__(self):
        self.__repositories = RentalRepositories()

    def searchById(self):
        pass
    def append(self):
        pass
    def calculateFeesAndLatePenalties(self):
        pass
    def sort(self):
        pass