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
        id = input('Enter Equipment ID: ')
        try:
            record = self.__services.record(id)
            print(f"Found: {record.Id}, Power: {record.powerRating}")
        except Exception as e:
            print(f"Error : {e}")
                        
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
                    break 
                except Exception as e:
                    print(f"Error : {e}")

        try:
            self.__services.append(newEquipment)
            print("✅ Equipment added successfully!")
        except Exception as e:
            print(f"Error : {e}")

    def update(self):
        pass

    def sort(self):
        pass

    def groupByStatus(self):
        pass