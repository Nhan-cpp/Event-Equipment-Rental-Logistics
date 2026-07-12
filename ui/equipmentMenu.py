from models.Equipment import Equipment
from services.EquipmentServices import EquipmentServices
import time
import os

class equipmentMenu():
    __services = None
    def __init__(self):
        self.__services = EquipmentServices()
        try:
            self.__services.loadEquipments()
        except ValueError as e:
            print(f"Warning: {e}")

    def saveEquipments(self):
        try:
            self.__services.saveEquipments()
        except ValueError as e:
            print(f"Error saving: {e}")

    def printEquipmentMaintenanceLog(self):
        print("\n--- EQUIPMENT MAINTENANCE LOG ---")
        try:
            logs = self.__services.readEquipmentMaintenanceLog()
            if not logs:
                print("No maintenance logs found.")
            else:
                for log in logs:
                    print(log)
        except Exception as e:
            print(f"❌ Error : {e}")
        input("\nPress Enter to continue...")

    def searchById(self):
        newEquipment = Equipment()
        
        fields = [("Id", "👉 Enter Equipment ID")]
        for attr_name, prompt in fields:
            while True:
                userInput = input(f"{prompt} (Type 'exit' to exit): ").strip()
                if userInput == 'exit':
                    return
                try:
                    setattr(newEquipment, attr_name, userInput)
                    break 
                except Exception as e:
                    print(f"❌ Error : {e}")

        try:
          
            foundEquipment = self.__services.getEquipmentById(newEquipment.Id)
            
            print("\n✅ Search equipment successfully!")
            print("-" * 40)
            print(f"ID: {foundEquipment.Id}")
            print(f"Power Rating: {foundEquipment.powerRating}")
            print(f"Hourly Rental Rate: {foundEquipment.hourlyRentalRate}")
            print(f"Status: {foundEquipment.currentStatus}")
            print("-" * 40)
            
        except Exception as e:
            print(f"❌ Error : {e}")
        input("\nPress Enter to continue...")
    
    def __printEquipmentTable(self, equipmentList, title):
        print(f"\n{'=' * 75}")
        print(f" {title} ".center(75))
        print(f"{'=' * 75}")
        if len(equipmentList) == 0:
            print("  (Empty)")
        else:
            print(f"| {'ID':<20} | {'Power Rating':>12} | {'Hourly Rate':>12} | {'Status':<12} |")
            print(f"|{'-' * 22}|{'-' * 14}|{'-' * 14}|{'-' * 14}|")
            for eq in equipmentList:
                print(f"| {eq.Id:<20} | {eq.powerRating:>12.2f} | {eq.hourlyRentalRate:>12.2f} | {eq.currentStatus:<12} |")
        print(f"{'=' * 75}")
        print(f"  Total: {len(equipmentList)} record(s)")
                
    def searchByStatus(self):
        try:
            availableList, rentedList = (self.__services.groupByStatus())
        except Exception as e:
            print(f"Error : {e}")
        
        choice = None
        while True:
            print(f"[1] Available")
            print(f"[2] Rented")
            print(f"[0] Exit")
            choice = input("👉 Enter your choice: ").strip()
            
            match choice:
                case '1':
                    self.__AvailableEquipment_display(availableList)
                    break
                case '2':
                    self.__RentedEquipment_display(rentedList)
                    break
                case '0':
                    return
                case _:
                    print("\n❌ Invalid choice. Please try again.")
                    time.sleep(1.5)
        
        input("\nPress Enter to continue...")

    def append(self):
        newEquipment = Equipment()
        
        fields = [
            ("Id", "👉 Enter Equipment ID"),
            ("powerRating", "👉 Enter Equipment Power Rating"),
            ("hourlyRentalRate", "👉 Enter Equipment Hourly Rental Rate")
        ]
        
        for attr_name, prompt in fields:
            while True:
                userInput = input(f"{prompt} (Type 'exit' to exit): ").strip()
                if userInput == 'exit':
                    return
                try:
                    setattr(newEquipment, attr_name, userInput)
                    # if attr_name == "Id":
                    #     if self.__services.searchById(userInput) != -1:
                    #         raise ValueError("Equipment ID already exists.")
                    break 
                except Exception as e:
                    print(f"❌ Error : {e}")

        try:
            self.__services.append(newEquipment)
            print("✅ Equipment added successfully!")
        except Exception as e:
            print(f"❌ Error : {e}")
            
        input("\nPress Enter to continue...")

    def update(self):

        newEquipment = Equipment()
        # Nhập ID cần cập nhật
        while True:

            userInput = input(
                "👉 Enter Equipment ID (Type 'exit' to exit): ").strip()
            if userInput.lower() == "exit":
                return
            try:
                newEquipment.Id = userInput
                break
            except Exception as e:
                print(f"Error : {e}")

        try:
            foundEquipment = self.__services.getEquipmentById(newEquipment.Id)

            print("\nCurrent Equipment Information")
            print("-" * 40)
            print(f"ID: {foundEquipment.Id}")
            print(f"[1] Power Rating      : {foundEquipment.powerRating}")
            print(f"[2] Hourly Rental Rate: {foundEquipment.hourlyRentalRate}")
            print(f"[3] Status            : {foundEquipment.currentStatus}")
            print(f"[0] Exit")
            print("-" * 40)

            while True:
                choice = input("👉 Select field (1-3): ").strip()
                match choice:
                    case "1":
                        value = input("👉 New Power Rating: ")
                        self.__services.update(foundEquipment.Id,"powerRating",float(value))
                        break
                    case "2":
                        value = input("👉 New Hourly Rental Rate: ")
                        self.__services.update(foundEquipment.Id, "hourlyRentalRate",float(value))
                        break
                    case "3":
                        value = input("👉 Status (Available/Rented): ").strip()
                        self.__services.update(foundEquipment.Id,"currentStatus",value)
                        break
                    case "0":
                        return
                    case _:
                        print("\n❌ Invalid choice. Please try again.")
                        time.sleep(1.5)
            print("\n✅ Equipment updated successfully!")

        except Exception as e:
            print(f"Error : {e}")
        input("\nPress Enter to continue...")

    def sort(self):
        print("\n--- SORT EQUIPMENT ---")
        sort_map = {'1': 'hourlyRentalRate', '2': 'powerRating'}
        
        while True:
            choice = input("👉 Sort by\n [1] Hourly Rate\n [2] Power Rating\n [0] Exit: ").strip()
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
                print("No equipment found to sort or invalid criteria.")
                return
            
            print(f"\n✅ Sort Equipment successfully! (By {sortType})")
            print(f"{'=' * 75}")
            print(f"| {'ID':<20} | {'Power Rating':>12} | {'Hourly Rate':>12} | {'Status':<12} |")
            print(f"|{'-' * 22}|{'-' * 14}|{'-' * 14}|{'-' * 14}|")
            for eq in sorted_list:
                print(f"| {eq.Id:<20} | {eq.powerRating:>12.2f} | {eq.hourlyRentalRate:>12.2f} | {eq.currentStatus:<12} |")
            print(f"{'=' * 75}")
            print(f"  Total: {len(sorted_list)} record(s)")
            
        except Exception as e:
            print(f"❌ Error : {e}")
        input("\nPress Enter to continue...")
        
    def groupByStatus(self):
        try:
            availableList, rentedList = (self.__services.groupByStatus())
        except Exception as e:
            print(f"Error : {e}")

        self.__printEquipmentTable(availableList, "AVAILABLE EQUIPMENT")
        self.__printEquipmentTable(rentedList, "RENTED EQUIPMENT")

        input("\nPress Enter to continue...")