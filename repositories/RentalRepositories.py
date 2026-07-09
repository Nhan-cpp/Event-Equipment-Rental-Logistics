from models.Rental import Rental
from datetime import datetime
import os

class RentalRepositories():
    FILE_PATH = 'data/rentalData.txt'
    HISTORY_FILE_PATH = 'data/rentalHistoryLog.txt'
    HOURLY_RENTAL_RATE = 0.2
    LATE_PENTALTY_RATE = 0.1
    __rentalList = []

    def __init__(self):
        self.__rentalList = self.loadRentals()
        
    def loadRentals(self):
        rentalList = []
        
        if not os.path.exists(self.FILE_PATH):
            os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                pass
            return rentalList

        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    data = line.strip().split(',')

                    if len(data) == 4:
                        rentalRecord = Rental(
                            data[0].strip(),
                            data[1].strip(),
                            datetime.strptime(data[2].strip(), "%d/%m/%Y %H:%M"),
                            datetime.strptime(data[3].strip(), "%d/%m/%Y %H:%M")
                        )
                        rentalList.append(rentalRecord)
        except FileNotFoundError:
            raise ValueError("Rental data file not found")
        except ValueError:
            raise ValueError("Invalid rental data format")

        return rentalList
    def saveRentals(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        try:
            with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
                for rental in self.__rentalList:
                    start_str = rental.startTime.strftime("%d/%m/%Y %H:%M") if rental.startTime else ""
                    return_str = rental.expectedReturnTime.strftime("%d/%m/%Y %H:%M") if rental.expectedReturnTime else ""
                    line = f"{rental.Id},{rental.clientName},{start_str},{return_str}\n"
                    file.write(line)
            return True
        except Exception:
            raise ValueError("Error while saving rental data")

    def writeRentalHistoryLog(self, rental):
        os.makedirs(os.path.dirname(self.HISTORY_FILE_PATH), exist_ok=True)
        try:
            with open(self.HISTORY_FILE_PATH, 'a', encoding='utf-8') as file:
                start_str = rental.startTime.strftime("%d/%m/%Y %H:%M") if rental.startTime else ""
                return_str = rental.expectedReturnTime.strftime("%d/%m/%Y %H:%M") if rental.expectedReturnTime else ""
                current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                line = f"{rental.Id},{rental.clientName},{start_str},{return_str},{current_time}\n"
                file.write(line)
            return True
        except Exception:
            raise ValueError("Error while writing rental history log")

    def searchById(self, rental_id):
        for index in range(len(self.__rental_list)):
            if self.__rental_list[index].ID == rental_id:
                return index
        return -1
    
    def append(self, rental):
        self.__rentalList.append(rental)

    def calculateFeesAndLatePenalties(self, rentalId):
        index = self.searchById(rentalId)
        if(index == -1):
            raise ValueError('Rental Id not found.')
        rental = self.__rentalList[index]
        current_time = datetime.now()

        rental_duration = rental.expectedReturnTime - rental.startTime
        rental_duration_hours = rental_duration.total_seconds() / 3600
        base_fee = rental_duration_hours * self.HOURLY_RENTAL_RATE

        if current_time > rental.expectedReturnTime:
            late_duration = current_time - rental.expectedReturnTime
            late_duration_hours = late_duration.total_seconds() / 3600
            late_penalty = late_duration_hours * self.LATE_PENTALTY_RATE
        else:
            late_penalty = 0

        total_fee = base_fee + late_penalty
        return total_fee
    
    def sort(self, sort_type, is_reverse=False):
        
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
        else:
            return None
            
        return sorted_list