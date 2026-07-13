from models.Rental import Rental
from datetime import datetime
import os

class RentalRepositories():
    FILE_PATH = 'data/rentalData.txt'
    HISTORY_FILE_PATH = 'data/rentalHistoryLog.txt'
    HOURLY_RENTAL_RATE = 0.2
    LATE_PENTALTY_RATE = 0.1

    def __init__(self):
        self.__rentalList = []
        
    def loadRentals(self):
        rentalList = []

        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(',')
                    rentalRecord = Rental(
                        data[0],
                        data[2],
                        datetime.strptime(data[3], "%d/%m/%Y %H:%M"),
                        datetime.strptime(data[4], "%d/%m/%Y %H:%M"),
                        equipmentId=data[1]
                    )
                    rentalList.append(rentalRecord)
        except FileNotFoundError:
            raise ValueError("Rental data file not found")
        except ValueError:
            raise ValueError("Invalid rental data format")

        self.__rentalList = rentalList
    
    def saveRentals(self):
        try:
            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                for rental in self.__rentalList:
                    start_str = rental.startTime.strftime("%d/%m/%Y %H:%M")
                    return_str = rental.expectedReturnTime.strftime("%d/%m/%Y %H:%M")

                    line = f"{rental.Id},{rental.equipmentId},{rental.clientName},{start_str},{return_str}\n"
                    file.write(line)
        except Exception:
            raise ValueError("Error while saving rental data")

    def writeRentalHistoryLog(self, rental : Rental):
        try:
            with open(self.HISTORY_FILE_PATH, 'a', encoding='utf-8') as file:
                start_str = rental.startTime.strftime("%d/%m/%Y %H:%M")
                return_str = rental.expectedReturnTime.strftime("%d/%m/%Y %H:%M")
                current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                line = f"{rental.Id},{rental.equipmentId},{rental.clientName},{start_str},{return_str},{current_time}\n"
                file.write(line)
        except Exception:
            raise ValueError("Error while writing rental history log")

    def readRentalHistoryLog(self):
        logs = []
        try:
            with open(self.HISTORY_FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    logs.append(line.strip())
            return logs
        except FileNotFoundError:
            return []

    def getRentalById(self, index: int):
        return self.__rentalList[index]

    def searchById(self, rentalId : str):
        for index in range(len(self.__rentalList)):
            if self.__rentalList[index].Id == rentalId:
                return index
        return -1
    
    def append(self, rental : Rental):
        self.__rentalList.append(rental)

    def calculateFeesAndLatePenalties(self, rental : Rental, hourlyRentalRate=None):
        current_time = datetime.now()
        hourlyRentalRate = self.HOURLY_RENTAL_RATE if hourlyRentalRate is None else float(hourlyRentalRate)
        if hourlyRentalRate <= 0:
            raise ValueError("Hourly rental rate must be greater than 0.")

        rental_duration = rental.expectedReturnTime - rental.startTime
        base_fee = (rental_duration.total_seconds() / 3600) * hourlyRentalRate

        if current_time > rental.expectedReturnTime:
            late_duration = current_time - rental.expectedReturnTime
            late_penalty = (late_duration.total_seconds() / 3600) * (hourlyRentalRate + self.LATE_PENTALTY_RATE)
        else:
            late_penalty = 0

        total_fee = base_fee + late_penalty
        return base_fee, late_penalty, total_fee
    
    def sort(self, sort_type, is_reverse=False):
        sorted_list = []
        if sort_type == "duration":
            sorted_list = sorted(
                self.__rentalList, 
                key=lambda rental: rental.expectedReturnTime - rental.startTime,
                reverse=is_reverse
            )
        elif sort_type == "clientName":
            sorted_list = sorted(
                self.__rentalList, 
                key=lambda rental: rental.clientName,
                reverse=is_reverse
            )
        return sorted_list
