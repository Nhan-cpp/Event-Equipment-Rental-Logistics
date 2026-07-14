from models.Rental import Rental
from services.RentalServices import RentalServices
from utils.ui import *
from datetime import datetime

class rentalMenu():
    def __init__(self, services : RentalServices):
        self.__services = services
        try:
            self.__services.loadRentals()
        except ValueError as e:
            UI_Warning(f"{e}")

    def saveRentals(self):
        try:
            self.__services.saveRentals()
        except ValueError as e:
            UI_Error(f"Error saving: {e}")

    def printRentalHistoryLog(self):
        try:
            logs = self.__services.readRentalHistoryLog()
            UI_Header("RENTAL HISTORY LOG", MAGENTA)
            log_headers = ["ID", "Eq ID", "Client Name", "Start Time", "Return Time", "Timestamp"]
            log_widths  = [12, 12, 16, 16, 16, 20]

            UI_Table_Header(log_headers, log_widths, MAGENTA)
            for log in logs:
                parts = log.split(',')
                if len(parts) >= 6:
                    values = [parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]]
                    UI_Table_Row(values, log_widths, MAGENTA)
            UI_Table_End(log_widths, MAGENTA)
            UI_Table_Total(len(logs))

        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()

    def searchById(self):
        UI_Header("SEARCH RENTAL BY ID", CYAN)
        newRental = Rental()

        print(f"\n  {CYAN}* Tip: Type 'exit' to cancel.{RESET}\n")
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
            start_str = rt.startTime.strftime('%d/%m/%Y %H')
            return_str = rt.expectedReturnTime.strftime('%d/%m/%Y %H')

            UI_Success("Rental found!")
            info_headers = ["Field", "Value"]
            info_widths  = [20, 26]
            UI_Table_Header(info_headers, info_widths, CYAN)
            UI_Table_Row(["ID", str(rt.Id)], info_widths, CYAN)
            UI_Table_Row(["Equipment ID", str(rt.equipmentId)], info_widths, CYAN)
            UI_Table_Row(["Client Name", str(rt.clientName)], info_widths, CYAN)
            UI_Table_Row(["Start Time", start_str], info_widths, CYAN)
            UI_Table_Row(["Return Time", return_str], info_widths, CYAN)
            UI_Table_End(info_widths, CYAN)

        except Exception as e:
            UI_Error(f"{e}")

        UI_Return_Prompt()

    def append(self):
        UI_Header("ADD NEW RENTAL RECORD", GREEN)
        newRental = Rental()

        newRental.startTime = datetime.now()
        start_time_str = newRental.startTime.strftime('%d/%m/%Y %H')
        print(f"  {CYAN}Start Time{RESET} : {start_time_str} (Auto-assigned)")

        fields = [
            ("Id", "Rental ID"),
            ("equipmentId", "Equipment ID"),
            ("clientName", "Client Name"),
            ("expectedReturnTime", "Return Time (dd/mm/yyyy HH)")
        ]
        print(f"\n  {CYAN}* Tip: Type 'exit' to cancel.{RESET}\n")
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

    def calculateFeesAndLatePenalties(self):
        UI_Header("CALCULATE RENTAL FEES & PENALTIES", YELLOW)

        print(f"\n  {CYAN}* Tip: Type 'exit' to cancel.{RESET}\n")
        while True:
            UI_Prompt("Rental ID")
            rentalID = input().strip()
            if rentalID.lower() == "exit":
                return

            try:
                base_fee, late_penalty, total_fee = self.__services.calculateFeesAndLatePenalties(rentalID)
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

            info_headers = ["ID", "Eq ID", "Client Name", "Start Time", "Return Time"]
            info_widths  = [12, 12, 16, 16, 16]
            UI_Table_Header(info_headers, info_widths, CYAN)

            for rt in sorted_list:
                start_str = rt.startTime.strftime('%d/%m/%Y %H')
                return_str = rt.expectedReturnTime.strftime('%d/%m/%Y %H')
                values = [rt.Id, rt.equipmentId, rt.clientName, start_str, return_str]
                UI_Table_Row(values, info_widths, CYAN)

            UI_Table_End(info_widths, CYAN)
            UI_Table_Total(len(sorted_list))

        except Exception as e:
            UI_Error(f"{e}")
        UI_Return_Prompt()
