from services.RentalServices import RentalServices

class rentalMenu():
    __services = None
    def __init__(self):
        self.__services = RentalServices()

    