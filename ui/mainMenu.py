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
        UI_Card_End(CYAN)

        UI_Card_Start("RENTAL OPTIONS", GREEN)
        UI_Menu_Item(7, "Add New Rental Record", GREEN)
        UI_Menu_Item(8, "Calculate Rental Fees & Penalties", GREEN)
        UI_Menu_Item(9, "View & Sort Rental List", GREEN)
        UI_Card_End(GREEN)

        UI_Card_Start("LOGS OPTIONS", MAGENTA)
        UI_Menu_Item(10, "View Equipment Maintenance Log", MAGENTA)
        UI_Menu_Item(11, "View Rental History Log", MAGENTA)
        UI_Card_End(MAGENTA)

        UI_Divider(YELLOW)
        UI_Menu_Item(0, "EXIT", YELLOW)
        UI_Card_End(YELLOW)

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
                    self.rtMenu.calculateFeesAndLatePenalties()
                case '9':
                    self.rtMenu.sort()
                case '10':
                    self.eqMenu.printEquipmentMaintenanceLog()
                case '11':
                    self.rtMenu.printRentalHistoryLog()
                case '0':
                    print(f"\n{BRIGHT_CYAN}  ✔ LOGGED OUT SUCCESSFULLY! Goodbye!{RESET}\n")
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