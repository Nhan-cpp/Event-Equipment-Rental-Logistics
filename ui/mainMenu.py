from ui.equipmentMenu import equipmentMenu
from ui.rentalMenu import rentalMenu
import sys
import time
import os

class mainMenu():
    def __init__(self):
        self.eqMenu = equipmentMenu()
        self.rtMenu = rentalMenu()

    def __printMenu(self):
        print("\n" + "="*60)
        print("🌟 EVENT EQUIPMENT RENTAL LOGISTICS SYSTEM 🌟".center(60))
        print("="*60)
        print(" --- EQUIPMENT OPTIONS ---")
        print("  [1] Add New Equipment")
        print("  [2] Update Equipment Information")
        print("  [3] Search Equipment By ID")
        print("  [4] Search Equipment By Status")
        print("  [5] View & Group equipment by rental status")
        print("  [6] View & Sort Equipment List")
        print(" --- RENTAL OPTIONS ---")
        print("  [7] Add New Rental Record")
        print("  [8] Calculate Rental Fees & Penalties")
        print("  [9] View & Sort Rental List")
        print("  [0] Exit")
        print("-" * 60)

    def display(self):
        while True:
            self.__printMenu()
            
            choice = input("👉 Your choice: ").strip()
            match choice:
                case '1':
                    self.eqMenu.append()
                case '2':
                    self.eqMenu.update()
                case '3':
                    self.eqMenu.searchById()
                case '4':
                    self.eqMenu.searchByStatus()
                case '5':
                    self.eqMenu.groupByStatus()
                case '6':
                    self.eqMenu.sort()
                case '7':
                    self.rtMenu.append()
                case '8':
                    self.rtMenu.calculateFeesAndLatePenalties()
                case '9':
                    self.rtMenu.sort()
                case '0':
                    print("\n👋 Thank you for using the system. Goodbye!\n")
                    sys.exit(0)
                case _:
                    print("\n❌ Invalid choice. Please try again.")
                    time.sleep(1.5)

            os.system('cls')

    def saveAll(self):
        try:
            self.eqMenu.saveEquipments()
            self.rtMenu.saveRentals()
        except Exception as e:
            print(f"Error : {e}")