from models.Rental import Rental
from services.RentalServices import RentalServices

class rentalMenu():
    __services = None
    def __init__(self):
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
                print(f"❌ Error : {e}")

        try:
            foundRental = self.__services.getRentalById(newRental.Id)

            print("\nRental Information")
            print("-" * 40)
            print(foundRental)
            print("-" * 40)

        except Exception as e:
            print(f"❌ Error : {e}")

        input("\nPress Enter to continue...")

    def append(self):
        newRental = Rental()
        fields = [
            ("Id", "👉 Enter Rental ID"),
            ("clientName", "👉 Enter Client Name"),
            ("startTime", "👉 Enter Start Time (dd/mm/yyyy HH:MM)"),
            ("expectedReturnTime", "👉 Enter Expected Return Time (dd/mm/yyyy HH:MM)")
        ]
        for attr_name, prompt in fields:
            while True:
                userInput = input(f"{prompt} (Type 'exit' to exit): ").strip()
                if userInput.lower() == "exit":
                    return

                try:
                    setattr(newRental, attr_name, userInput)
                    break

                except Exception as e:
                    print(f"❌ Error : {e}")

        try:
            self.__services.append(newRental)
            print("✅ Rental order added successfully!")

        except Exception as e:
            print(f"❌ Error : {e}")
            
        input("\nPress Enter to continue...")

    def calculateFeesAndLatePenalties(self):

        while True:
            rentalID = input("👉 Enter Rental ID (Type 'exit' to exit): ").strip()
            if rentalID.lower() == "exit":
                return

            try:
                base_fee, late_penalty, total_fee = self.__services.calculateFeesAndLatePenalties(rentalID)
                print("\n✅ Calculate successfully!")
                print("-" * 40)
                print(f"Base Fee      : {base_fee:.2f}")
                print(f"Late Penalty  : {late_penalty:.2f}")
                print(f"Total Fee     : {total_fee:.2f}")
                print("-" * 40)
                break

            except Exception as e:
                print(f"❌ Error : {e}")

        input("\nPress Enter to continue...")

    def sort(self):
        print("\n--- SORT RENTAL ---")
        sort_map = {'1': 'duration', '2': 'clientName'}
        
        while True:
            choice = input("👉 Sort by\n [1] Duration\n [2] Client Name\n [0] Exit: ").strip()
            if choice == '0': 
                return
            if choice in sort_map:
                sortType = sort_map[choice]
                break
            print("❌ Invalid choice!")
            
        while True:
            choice = input("👉 Reverse order?\n [1] Yes\n [2] No\n [0] Exit: ").strip()
            if choice == '0':
                return
            if choice in ['1', '2']:
                isReverse = (choice == '1')
                break
            print("❌ Invalid choice!")
        
        try:
            sorted_list = self.__services.sort(sortType, isReverse)
            
            if not sorted_list:
                print("No rental orders found.")
                return

            print(f"\n✅ Sort Rental successfully! (By {sortType})")
            print("-" * 65)
            for rental in sorted_list:
                print(rental)
            print("-" * 65)
            
        except Exception as e:
            print(f"❌ Error : {e}")
        input("\nPress Enter to continue...")