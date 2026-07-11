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
        newRental = Rental()

        while True:
            userInput = input("👉 Enter Rental ID (Type 'exit' to exit): ").strip()
            if userInput.lower() == "exit":
                return
            
            try:
                newRental.Id = userInput
                break
            except Exception as e:
                print(f"Error : {e}")

        try:
            foundRental = self.__services.getRentalByIndex(newRental.Id)

            print("\nRental Information")
            print("-" * 40)
            print(foundRental)
            print("-" * 40)

        except Exception as e:
            print(f"Error : {e}")

        input("\nPress Enter to continue...")

    def append(self):
        pass

    def calculateFeesAndLatePenalties(self):
        pass

    def sort(self):
        pass