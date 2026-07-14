from ui.equipmentMenu import equipmentMenu
from ui.rentalMenu import rentalMenu
from services.EquipmentServices import EquipmentServices
from services.RentalServices import RentalServices

from utils.ui_utils import *
import time
import os

class mainMenu():
    def __init__(self):
        equipmentServices = EquipmentServices()
        rentalServices = RentalServices(equipmentServices)

        self.eqMenu = equipmentMenu(equipmentServices)
        self.rtMenu = rentalMenu(rentalServices)

    def __printMenu(self):
        print(f"\n{BOLD}{YELLOW}       EVENT EQUIPMENT RENTAL LOGISTICS SYSTEM{RESET}\n")

        UI_Card_Start("EQUIPMENT OPTIONS", CYAN)
        UI_Menu_Item(1, "Add New Equipment", CYAN)
        UI_Menu_Item(2, "Update Equipment Information", CYAN)
        UI_Menu_Item(3, "Search Equipment By ID", CYAN)
        UI_Menu_Item(4, "Search Equipment By Status", CYAN)
        UI_Menu_Item(5, "View & Group By Rental Status", CYAN)
        UI_Menu_Item(6, "View & Sort Equipment List", CYAN)

        UI_Menu_Item(7, "Add New Rental Order", CYAN)
        UI_Menu_Item(8, "Search Rental Order By ID", CYAN)
        UI_Menu_Item(9, "Calculate Rental Fees & Penalties", CYAN)
        UI_Menu_Item(10, "View & Sort Rental List", CYAN)

        UI_Menu_Item(11, "View Equipment Maintenance Log", CYAN)
        UI_Menu_Item(12, "View Rental History Log", CYAN)

        UI_Menu_Item(0, "EXIT", CYAN)
        UI_Card_End(CYAN)

    def display(self):
        while True:
            self.__printMenu()

            print(f"{BOLD}{YELLOW}  ❯ SELECT FUNCTION: {RESET}", end="")
            choice = input().strip()
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
                    self.rtMenu.searchById()
                case '9':
                    self.rtMenu.calculateFeesAndLatePenalties()
                case '10':
                    self.rtMenu.sort()
                case '11':
                    self.eqMenu.printEquipmentMaintenanceLog()
                case '12':
                    self.rtMenu.printRentalHistoryLog()
                case '0':
                    print(f"\n{CYAN}  ✔ LOGGED OUT SUCCESSFULLY! Goodbye!{RESET}\n")
                    return
                case _:
                    UI_Error("Invalid choice. Please try again.")
                    time.sleep(1.5)

            os.system('cls')

    def saveAll(self):
        try:
            self.eqMenu.saveEquipments()
            self.rtMenu.saveRentals()
        except Exception as e:
            UI_Error(f"Save failed: {e}")
            time.sleep(1.5)
