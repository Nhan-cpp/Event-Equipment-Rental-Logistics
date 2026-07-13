from models.Equipment import Equipment
from services.EquipmentServices import EquipmentServices
from utils.ui_utils import *
import time
import os

class equipmentMenu():
    __services = None
    def __init__(self):
        self.__services = EquipmentServices()
        try:
            self.__services.loadEquipments()
        except ValueError as e:
            UI_Warning(f"{e}")

    def saveEquipments(self):
        try:
            self.__services.saveEquipments()
        except ValueError as e:
            UI_Error(f"Error saving: {e}")

    # ─── Equipment Table Constants ───
    __EQ_HEADERS = ["ID", "Power Rating", "Hourly Rate", "Status"]
    __EQ_WIDTHS  = [20, 12, 12, 12]

    def __printEquipmentTable(self, equipmentList, title, color=CYAN):
        UI_Header(title, color)
        if len(equipmentList) == 0:
            print(f"  {BRIGHT_BLACK}(Empty){RESET}")
        else:
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

    # ─── Maintenance Log ───
    __LOG_HEADERS = ["ID", "Power", "Rate", "Status", "Action", "Timestamp"]
    __LOG_WIDTHS  = [15, 8, 8, 10, 35, 20]

    def printEquipmentMaintenanceLog(self):
        try:
            logs = self.__services.readEquipmentMaintenanceLog()
            UI_Header("EQUIPMENT MAINTENANCE LOG", MAGENTA)
            
            if not logs:
                print(f"  {BRIGHT_BLACK}(Empty){RESET}")
            else:
                UI_Table_Header(self.__LOG_HEADERS, self.__LOG_WIDTHS, MAGENTA)
                for log in logs:
                    parts = log.split(',')
                    if len(parts) >= 6:
                        values = [
                            parts[0],
                            f"{float(parts[1]):.2f}",
                            f"{float(parts[2]):.2f}",
                            parts[3],
                            parts[4],
                            parts[5]
                        ]
                        UI_Table_Row(values, self.__LOG_WIDTHS, MAGENTA)
                UI_Table_End(self.__LOG_WIDTHS, MAGENTA)
            UI_Table_Total(len(logs))
            
        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    # ─── Search By ID ───
    def searchById(self):
        UI_Header("SEARCH EQUIPMENT BY ID", CYAN)
        newEquipment = Equipment()
        
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
            
            UI_Success("Equipment found!")
            info_headers = ["Field", "Value"]
            info_widths  = [20, 26]
            UI_Table_Header(info_headers, info_widths, CYAN)
            UI_Table_Row(["ID", str(eq.Id)], info_widths, CYAN)
            UI_Table_Row(["Power Rating", str(eq.powerRating)], info_widths, CYAN)
            UI_Table_Row(["Hourly Rate", str(eq.hourlyRentalRate)], info_widths, CYAN)
            UI_Table_Row(["Status", str(eq.currentStatus)], info_widths, CYAN)
            UI_Table_End(info_widths, CYAN)
            
        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()
    
    # ─── Search By Status ───
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

    # ─── Append ───
    def append(self):
        UI_Header("ADD NEW EQUIPMENT", GREEN)
        newEquipment = Equipment()
        
        fields = [
            ("Id", "Equipment ID"),
            ("powerRating", "Power Rating"),
            ("hourlyRentalRate", "Hourly Rate")
        ]
        
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

    # ─── Update ───
    def update(self):
        UI_Header("UPDATE EQUIPMENT", YELLOW)

        newEquipment = Equipment()
        # Nhập ID cần cập nhật
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

            info_headers = ["Field", "Value"]
            info_widths  = [20, 26]
            UI_Table_Header(info_headers, info_widths, CYAN)
            UI_Table_Row(["ID", str(foundEquipment.Id)], info_widths, CYAN)
            UI_Table_Row(["Power Rating", str(foundEquipment.powerRating)], info_widths, CYAN)
            UI_Table_Row(["Hourly Rate", str(foundEquipment.hourlyRentalRate)], info_widths, CYAN)
            UI_Table_Row(["Status", str(foundEquipment.currentStatus)], info_widths, CYAN)
            UI_Table_End(info_widths, CYAN)

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

    # ─── Sort ───
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
            
            if not sorted_list:
                UI_Warning("No equipment found.")
                return

            UI_Success(f"Sorted by {sortType}!")
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
        
    # ─── Group By Status ───
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