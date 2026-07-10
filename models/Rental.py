from utils.utils import validate_ID

class Rental():
    _Id = None
    _clientName = None
    _startTime = None
    _expectedReturnTime = None
    MIN_ID_LEN = 8
    MAX_ID_LEN = 20
    def __init__(self,Id,clientName,startTime,expectedReturnTime):
        self._Id = Id
        self._clientName = clientName
        self._startTime = startTime
        self._expectedReturnTime = expectedReturnTime
    
    @property
    def Id(self):
        return self._Id
    @Id.setter
    def Id(self,new_value : str):
        if(len(new_value) < self.MIN_ID_LEN and self.MAX_ID_LEN < len(new_value)):
            raise ValueError(f"Rental id need length from {self.MIN_ID_LEN} to {self.MAX_ID_LEN}")
        for character in new_value:
            if not character.isalnum():
                raise ValueError("Rental Id only contain character or digit.")
        self._Id = new_value
    
    @property
    def clientName(self):
        return self._clientName
    @clientName.setter
    def clientName(self,new_value : str):
        self._clientName = str(new_value)
    @property
    def startTime(self):
        return self._startTime
    @startTime.setter
    def startTime(self,new_value):
        try:
            self._startTime = new_value
        except:
            raise ValueError("Need be a time format.")
    @property
    def expectedReturnTime(self):
        return self._expectedReturnTime
    @expectedReturnTime.setter
    def expectedReturnTime(self,new_value):
        try:
            if(self._startTime < new_value):
                raise ValueError("Rental expected return time must early than start time")
            self._expectedReturnTime = new_value
        except:
            raise ValueError("Rental expected return time have some error.")        