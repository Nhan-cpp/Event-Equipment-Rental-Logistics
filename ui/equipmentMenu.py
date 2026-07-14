from models.Equipment import Equipment
from services.EquipmentServices import EquipmentServices
from utils.ui import *
import time

class equipmentMenu():
    __EQ_HEADERS = ["ID", "Power Rating", "Hourly Rate", "Status"]
    __EQ_WIDTHS  = [20, 12, 12, 12]
    def __init__(self, services : EquipmentServices):
        self.__services = services
        try:
            self.__services.loadEquipments()
        except ValueError as e:
            UI_Warning(f"{e}")

    def saveEquipments(self):
        try:
            self.__services.saveEquipments()
        except ValueError as e:
            UI_Error(f"Error saving: {e}")

    def __printEquipmentTable(self, equipmentList : list, title : str, color=CYAN):
        UI_Header(title, color)
        UI_Table_Header(self.__EQ_HEADERS, self.__EQ_WIDTHS, color)

        for eq in equipmentList:
            values = [
                eq.Id,
                f"{eq.powerRating:.2f}",
                f"{eq.hourlyRentalRate:.2f}",
                eq.currentStatus
            ]
            UI_Table_Row(values, self.__EQ_WIDTHS, color)

        UI_Table_End(self.__EQ_WIDTHS, color)
        UI_Table_Total(len(equipmentList))

    def printEquipmentMaintenanceLog(self):
        try:
            logs = self.__services.readEquipmentMaintenanceLog()
            UI_Header("EQUIPMENT MAINTENANCE LOG", MAGENTA)

            info_widths  = [15, 8, 8, 10, 35, 20]
            UI_Table_Header(["ID", "Power", "Rate", "Status", "Action", "Timestamp"], info_widths, MAGENTA)

            for log in logs:
                parts = log.split(',')
                values = [
                    parts[0],
                    f"{float(parts[1]):.2f}",
                    f"{float(parts[2]):.2f}",
                    parts[3],
                    parts[4],
                    parts[5]
                ]
                UI_Table_Row(values, info_widths, MAGENTA)

            UI_Table_End(info_widths, MAGENTA)
            UI_Table_Total(len(logs))

        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    def searchById(self):
        UI_Header("SEARCH EQUIPMENT BY ID", CYAN)
        newEquipment = Equipment()

        print(f"\n  {CYAN}* Tip: Type 'exit' to cancel.{RESET}\n")
        while True:
            UI_Prompt("Equipment ID")
            userInput = input().strip()
            if userInput.lower() == 'exit':
                return
            try:
                newEquipment.Id = userInput
                break 
            except Exception as e:
                UI_Error(f"{e}")

        try:
            eq = self.__services.getEquipmentById(newEquipment.Id)

            print(f"  {CYAN}ID{RESET}           : {eq.Id}")
            print(f"  {CYAN}Power Rating{RESET} : {eq.powerRating}")
            print(f"  {CYAN}Hourly Rate{RESET}  : {eq.hourlyRentalRate}")
            print(f"  {CYAN}Status{RESET}       : {eq.currentStatus}")

        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    def searchByStatus(self):
        UI_Header("SEARCH EQUIPMENT BY STATUS", CYAN)
        try:
            availableList, rentedList = self.__services.groupByStatus()
        except Exception as e:
            UI_Error(f"{e}")
            UI_Return_Prompt()
            return

        UI_Card_Start("SELECT STATUS", YELLOW)
        UI_Menu_Item(1, "Available", YELLOW)
        UI_Menu_Item(2, "Rented", YELLOW)
        UI_Divider(YELLOW)
        UI_Menu_Item(0, "Exit", YELLOW)
        UI_Card_End(YELLOW)

        while True:
            print(f"{BOLD}{YELLOW}  ❯ SELECT FUNCTION: {RESET}", end="")
            choice = input().strip()

            match choice:
                case '1':
                    self.__printEquipmentTable(availableList, "AVAILABLE EQUIPMENT", GREEN)
                    break
                case '2':
                    self.__printEquipmentTable(rentedList, "RENTED EQUIPMENT", RED)
                    break
                case '0':
                    return
                case _:
                    UI_Error("Invalid choice. Please try again.")
                    time.sleep(1.5)

        UI_Return_Prompt()

    def append(self):
        UI_Header("ADD NEW EQUIPMENT", GREEN)
        newEquipment = Equipment()

        fields = [
            ("Id", "Equipment ID"),
            ("powerRating", "Power Rating"),
            ("hourlyRentalRate", "Hourly Rate")
        ]

        print(f"\n  {CYAN}* Tip: Type 'exit' to cancel.{RESET}\n")
        for attr_name, label in fields:
            while True:
                UI_Prompt(label)
                userInput = input().strip()
                if userInput.lower() == 'exit':
                    return
                try:
                    setattr(newEquipment, attr_name, userInput)
                    break 
                except Exception as e:
                    UI_Error(f"{e}")

        try:
            self.__services.append(newEquipment)
            UI_Success("Equipment added successfully!")
        except Exception as e:
            UI_Error(f"{e}")

        UI_Return_Prompt()

    def update(self):
        UI_Header("UPDATE EQUIPMENT", YELLOW)

        newEquipment = Equipment()

        print(f"\n  {CYAN}* Tip: Type 'exit' to cancel.{RESET}\n")
        while True:
            UI_Prompt("Equipment ID")
            userInput = input().strip()
            if userInput.lower() == "exit":
                return
            try:
                newEquipment.Id = userInput
                break
            except Exception as e:
                UI_Error(f"{e}")

        try:
            foundEquipment = self.__services.getEquipmentById(newEquipment.Id)

            print(f"\n  {CYAN}ID{RESET}           : {foundEquipment.Id}")
            print(f"  {CYAN}Power Rating{RESET} : {foundEquipment.powerRating}")
            print(f"  {CYAN}Hourly Rate{RESET}  : {foundEquipment.hourlyRentalRate}")
            print(f"  {CYAN}Status{RESET}       : {foundEquipment.currentStatus}")

            UI_Card_Start("UPDATE OPTIONS", YELLOW)
            UI_Menu_Item(1, "Power Rating", YELLOW)
            UI_Menu_Item(2, "Hourly Rental Rate", YELLOW)
            UI_Menu_Item(3, "Status", YELLOW)
            UI_Divider(YELLOW)
            UI_Menu_Item(0, "Exit", YELLOW)
            UI_Card_End(YELLOW)

            while True:
                print(f"{BOLD}{YELLOW}  ❯ SELECT FUNCTION: {RESET}", end="")
                choice = input().strip()
                match choice:
                    case "1":
                        UI_Prompt("New Power Rating")
                        value = input().strip()
                        self.__services.update(foundEquipment.Id,"powerRating",float(value))
                        break
                    case "2":
                        UI_Prompt("New Hourly Rate")
                        value = input().strip()
                        self.__services.update(foundEquipment.Id, "hourlyRentalRate",float(value))
                        break
                    case "3":
                        UI_Prompt("Status (Available/Rented)")
                        value = input().strip()
                        self.__services.update(foundEquipment.Id,"currentStatus",value)
                        break
                    case "0":
                        return
                    case _:
                        UI_Error("Invalid choice. Please try again.")
                        time.sleep(1.5)
            UI_Success("Equipment updated successfully!")

        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    def sort(self):
        UI_Header("SORT EQUIPMENT", CYAN)
        sort_map = {'1': 'hourlyRentalRate', '2': 'powerRating'}

        UI_Card_Start("SORT BY", CYAN)
        UI_Menu_Item(1, "Hourly Rate", CYAN)
        UI_Menu_Item(2, "Power Rating", CYAN)
        UI_Divider(CYAN)
        UI_Menu_Item(0, "Exit", CYAN)
        UI_Card_End(CYAN)

        while True:
            print(f"{BOLD}{YELLOW}  ❯ SELECT FUNCTION: {RESET}", end="")
            choice = input().strip()
            if choice == '0': 
                return
            if choice in sort_map:
                sortType = sort_map[choice]
                break
            UI_Error("Invalid choice!")

        UI_Card_Start("ORDER", CYAN)
        UI_Menu_Item(1, "Ascending", CYAN)
        UI_Menu_Item(2, "Descending", CYAN)
        UI_Divider(CYAN)
        UI_Menu_Item(0, "Exit", CYAN)
        UI_Card_End(CYAN)

        while True:
            print(f"{BOLD}{YELLOW}  ❯ SELECT FUNCTION: {RESET}", end="")
            choice = input().strip()
            if choice == '0':
                return
            if choice in ['1', '2']:
                isReverse = (choice == '2')
                break
            UI_Error("Invalid choice!")

        try:
            sorted_list = self.__services.sort(sortType, isReverse)

            UI_Table_Header(self.__EQ_HEADERS, self.__EQ_WIDTHS, CYAN)

            for eq in sorted_list:
                values = [
                    eq.Id,
                    f"{eq.powerRating:.2f}",
                    f"{eq.hourlyRentalRate:.2f}",
                    eq.currentStatus
                ]
                UI_Table_Row(values, self.__EQ_WIDTHS, CYAN)

            UI_Table_End(self.__EQ_WIDTHS, CYAN)
            UI_Table_Total(len(sorted_list))

        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    def groupByStatus(self):
        try:
            availableList, rentedList = self.__services.groupByStatus()
        except Exception as e:
            UI_Error(f"{e}")
            UI_Return_Prompt()
            return

        self.__printEquipmentTable(availableList, "AVAILABLE EQUIPMENT", GREEN)
        self.__printEquipmentTable(rentedList, "RENTED EQUIPMENT", RED)

        UI_Return_Prompt()
