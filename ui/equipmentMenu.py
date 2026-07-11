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

    def writeEquipmentMaintenanceLog(self):
        pass

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
            status_text = "Available" if foundEquipment.currentStatus else "Unavailable"
            print(f"Status: {status_text}")
            print("-" * 40)
            
        except Exception as e:
            print(f"❌ Error : {e}")
        input("\nPress Enter to continue...")
                        
    def searchByStatus(self):
        pass

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
        pass

    def sort(self):
        print("\n--- SORT EQUIPMENT ---")
        print("[1] Sort by Hourly Rental Rate")
        print("[2] Sort by Power Rating")
        print("[0] Exit")
        choice = input("👉 Choose sorting criteria (1 or 2): ").strip()
        
        while True:
            match choice:
                case '1':
                    sortType = "hourlyRentalRate"
                    break
                case '2':
                    sortType = "powerRating"
                    break
                case '0':
                    return
                case _:
                    print("❌ Invalid choice!")
        
        print("\n--- REVERSE ---")
        print("[1] Yes")
        print("[2] No")
        print("[0] Exit")
        choice = input("👉 Choose reveresed ? (1 or 2): ").strip()

        isReverse = None

        while True:
            match choice:
                case '1':
                    isReverse = True
                    break
                case '2':
                    isReverse = False
                    break
                case '0':
                    return
                case _:
                    print("❌ Invalid choice!")
        
        try:
            sorted_list = self.__services.sort(sortType, isReverse)
            
            if not sorted_list:
                print("No equipment found to sort or invalid criteria.")
                return

          
            print(f"\n✅ Sort Equipment successfully! (By {sortType})")
            print("-" * 65)
            print(f"{'ID'} | {'Power'} | {'Rate'} | {'Status'}")
            print("-" * 65)
            
            for eq in sorted_list:
                status_text = "Available" if eq.currentStatus else "Unavailable"
                print(f"{eq.Id:<15} | {eq.powerRating:<25.0f} | {eq.hourlyRentalRate:<25.0f} | {status_text:<15}")
            print("-" * 65)
            
        except Exception as e:
            print(f"❌ Error : {e}")
        input("\nPress Enter to continue...")
        
    def groupByStatus(self):
        pass