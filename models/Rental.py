from datetime import datetime
from utils.utils import validate_ID

class Rental():
    MIN_ID_LEN = 4
    MAX_ID_LEN = 20
    def __init__(self, Id="", clientName="", startTime=None, expectedReturnTime=None, equipmentId=""):
        self._Id = ""
        self._equipmentId = ""
        self._clientName = ""
        self._startTime = datetime.now()
        self._expectedReturnTime = datetime.now()

        if Id != "":
            self.Id = Id
        if equipmentId != "":
            self.equipmentId = equipmentId
        self.clientName = clientName
        if startTime is not None:
            self.startTime = startTime
        if expectedReturnTime is not None:
            self.expectedReturnTime = expectedReturnTime

    def __str__(self):
        start_str = self._startTime.strftime("%d/%m/%Y %H")
        return_str = self._expectedReturnTime.strftime("%d/%m/%Y %H")
        return f"ID: {self._Id} | Equipment: {self._equipmentId} | Client: {self._clientName} | Start: {start_str} | Return: {return_str}"

    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,new_value : str):
        if(len(new_value) < self.MIN_ID_LEN or self.MAX_ID_LEN < len(new_value)):
            raise ValueError(f"Rental id need length from {self.MIN_ID_LEN} to {self.MAX_ID_LEN}")
        for character in new_value:
            if not character.isalnum():
                raise ValueError("Rental Id only contain character or digit.")
        self._Id = new_value

    @property
    def equipmentId(self):
        return self._equipmentId
    @equipmentId.setter
    def equipmentId(self,new_value : str):
        if(len(new_value) < self.MIN_ID_LEN or self.MAX_ID_LEN < len(new_value)):
            raise ValueError(f"Equipment id need length from {self.MIN_ID_LEN} to {self.MAX_ID_LEN}")
        if(validate_ID(new_value) == False):
            raise ValueError("Equipment Id only contain character or digit.")
        self._equipmentId = new_value

    @property
    def clientName(self):
        return self._clientName
    @clientName.setter
    def clientName(self,new_value : str):
        self._clientName = new_value

    @property
    def startTime(self):
        return self._startTime
    @startTime.setter
    def startTime(self,new_value):
        try:
            if isinstance(new_value, str):
                new_value = datetime.strptime(new_value, "%d/%m/%Y %H")
            self._startTime = new_value
        except:
            raise ValueError("Invalid start time format. Use dd/mm/yyyy HH")

    @property
    def expectedReturnTime(self):
        return self._expectedReturnTime
    @expectedReturnTime.setter
    def expectedReturnTime(self,new_value):
        try:
            if isinstance(new_value, str):
                new_value = datetime.strptime(new_value, "%d/%m/%Y %H")
        except:
            raise ValueError("Invalid return time format. Use dd/mm/yyyy HH")

        if self._startTime and new_value:
            if self._startTime > new_value:
                raise ValueError("Expected return time must be later than start time.")

        self._expectedReturnTime = new_value
