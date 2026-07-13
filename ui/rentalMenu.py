from models.Rental import Rental
from services.RentalServices import RentalServices
from utils.ui_utils import *

class rentalMenu():
    __services = None
    def __init__(self):
        self.__services = RentalServices()
        try:
            self.__services.loadRentals()
        except ValueError as e:
            UI_Warning(f"{e}")
        
    def saveRentals(self):
        try:
            self.__services.saveRentals()
        except ValueError as e:
            UI_Error(f"Error saving: {e}")

    # ─── Rental Table Constants ───
    __RT_HEADERS = ["ID", "Client Name", "Start Time", "Return Time"]
    __RT_WIDTHS  = [20, 20, 16, 16]

    # ─── History Log Constants ───
    __LOG_HEADERS = ["ID", "Client Name", "Start Time", "Return Time", "Timestamp"]
    __LOG_WIDTHS  = [15, 20, 16, 16, 20]

    # ─── Rental History Log ───
    def printRentalHistoryLog(self):
        try:
            logs = self.__services.readRentalHistoryLog()
            UI_Header("RENTAL HISTORY LOG", MAGENTA)
            
            if not logs:
                print(f"  {BRIGHT_BLACK}(Empty){RESET}")
            else:
                UI_Table_Header(self.__LOG_HEADERS, self.__LOG_WIDTHS, MAGENTA)
                for log in logs:
                    parts = log.split(',')
                    if len(parts) >= 5:
                        values = [parts[0], parts[1], parts[2], parts[3], parts[4]]
                        UI_Table_Row(values, self.__LOG_WIDTHS, MAGENTA)
                UI_Table_End(self.__LOG_WIDTHS, MAGENTA)
            UI_Table_Total(len(logs))
            
        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    # ─── Search By ID ───
    def searchById(self):
        UI_Header("SEARCH RENTAL BY ID", CYAN)
        newRental = Rental()

        while True:
            UI_Prompt("Rental ID")
            userInput = input().strip()
            if userInput.lower() == "exit":
                return
            
            try:
                newRental.Id = userInput
                break
            except Exception as e:
                UI_Error(f"{e}")

        try:
            rt = self.__services.getRentalById(newRental.Id)
            start_str = rt.startTime.strftime('%d/%m/%Y %H:%M') if rt.startTime else ''
            return_str = rt.expectedReturnTime.strftime('%d/%m/%Y %H:%M') if rt.expectedReturnTime else ''

            UI_Success("Rental found!")
            info_headers = ["Field", "Value"]
            info_widths  = [20, 26]
            UI_Table_Header(info_headers, info_widths, CYAN)
            UI_Table_Row(["ID", str(rt.Id)], info_widths, CYAN)
            UI_Table_Row(["Client Name", str(rt.clientName)], info_widths, CYAN)
            UI_Table_Row(["Start Time", start_str], info_widths, CYAN)
            UI_Table_Row(["Return Time", return_str], info_widths, CYAN)
            UI_Table_End(info_widths, CYAN)

        except Exception as e:
            UI_Error(f"{e}")

        UI_Return_Prompt()

    # ─── Append ───
    def append(self):
        UI_Header("ADD NEW RENTAL RECORD", GREEN)
        newRental = Rental()
        fields = [
            ("Id", "Rental ID"),
            ("clientName", "Client Name"),
            ("startTime", "Start Time (dd/mm/yyyy HH:MM)"),
            ("expectedReturnTime", "Return Time (dd/mm/yyyy HH:MM)")
        ]
        for attr_name, label in fields:
            while True:
                UI_Prompt(label)
                userInput = input().strip()
                if userInput.lower() == "exit":
                    return

                try:
                    setattr(newRental, attr_name, userInput)
                    break

                except Exception as e:
                    UI_Error(f"{e}")

        try:
            self.__services.append(newRental)
            UI_Success("Rental order added successfully!")

        except Exception as e:
            UI_Error(f"{e}")
            
        UI_Return_Prompt()

    # ─── Calculate Fees ───
    def calculateFeesAndLatePenalties(self):
        UI_Header("CALCULATE RENTAL FEES & PENALTIES", YELLOW)

        while True:
            UI_Prompt("Rental ID")
            rentalID = input().strip()
            if rentalID.lower() == "exit":
                return

            try:
                base_fee, late_penalty, total_fee = self.__services.calculateFeesAndLatePenalties(rentalID)
                UI_Success("Calculated successfully!")
                fee_headers = ["Fee Type", "Amount"]
                fee_widths  = [20, 15]
                UI_Table_Header(fee_headers, fee_widths, YELLOW)
                UI_Table_Row(["Base Fee", f"{base_fee:.2f}"], fee_widths, YELLOW)
                UI_Table_Row(["Late Penalty", f"{late_penalty:.2f}"], fee_widths, YELLOW)
                UI_Table_Row(["Total Fee", f"{total_fee:.2f}"], fee_widths, YELLOW)
                UI_Table_End(fee_widths, YELLOW)
                break

            except Exception as e:
                UI_Error(f"{e}")

        UI_Return_Prompt()

    # ─── Sort ───
    def sort(self):
        UI_Header("SORT RENTAL", CYAN)
        sort_map = {'1': 'duration', '2': 'clientName'}
        
        UI_Card_Start("SORT BY", CYAN)
        UI_Menu_Item(1, "Duration", CYAN)
        UI_Menu_Item(2, "Client Name", CYAN)
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
                UI_Warning("No rental orders found.")
                return

            UI_Success(f"Sorted by {sortType}!")
            UI_Table_Header(self.__RT_HEADERS, self.__RT_WIDTHS, CYAN)
            for rt in sorted_list:
                start_str = rt.startTime.strftime('%d/%m/%Y %H:%M') if rt.startTime else ''
                return_str = rt.expectedReturnTime.strftime('%d/%m/%Y %H:%M') if rt.expectedReturnTime else ''
                values = [rt.Id, rt.clientName, start_str, return_str]
                UI_Table_Row(values, self.__RT_WIDTHS, CYAN)
            UI_Table_End(self.__RT_WIDTHS, CYAN)
            UI_Table_Total(len(sorted_list))
            
        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()