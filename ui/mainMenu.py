from ui.equipmentMenu import equipmentMenu
from ui.rentalMenu import rentalMenu
import sys
import time
import os

class mainMenu(equipmentMenu, rentalMenu):
    def __init__(self):
        super().__init__()

    def __printMenu(self):
        print("\n" + "="*60)
        print("🌟 EVENT EQUIPMENT RENTAL LOGISTICS SYSTEM 🌟".center(60))
        print("="*60)
        print(" --- EQUIPMENT OPTIONS ---")
        print("  [1] Add New Equipment")
        print("  [2] Update Equipment Information")
        print("  [3] Search Equipment (By ID or Status)")
        print("  [4] View & Sort Equipment List")
        print(" --- RENTAL OPTIONS ---")
        print("  [5] Create New Rental Record")
        print("  [6] Calculate Rental Fees & Penalties")
        print("  [7] View & Sort Rental List")
        print(" --- SYSTEM OPTIONS ---")
        print("  [8] Save All Data & Logs")
        print("  [0] Exit")
        print("-" * 60)

    def display(self):
        while True:
            self.__printMenu()
            
            choice = input("👉 Please select an option (0-8): ").strip()
            
            if choice == '1':
                print("\n[To do: Call self.add_equipment_ui()]")
            elif choice == '2':
                print("\n[To do: Call self.update_equipment_ui()]")
            elif choice == '3':
                print("\n[To do: Call self.search_equipment_ui()]")
            elif choice == '4':
                print("\n[To do: Call self.view_equipment_ui()]")
            elif choice == '5':
                print("\n[To do: Call self.add_rental_ui()]")
            elif choice == '6':
                print("\n[To do: Call self.calculate_fees_ui()]")
            elif choice == '7':
                print("\n[To do: Call self.view_rental_ui()]")
            elif choice == '0':
                print("\n👋 Thank you for using the system. Goodbye!\n")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice. Please try again.")
                time.sleep(1.5)

            os.system('cls' if os.name == 'nt' else 'clear')

    